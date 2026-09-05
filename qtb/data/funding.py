"""Optional Gate USDT-M funding-rate history with disk cache."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .candles import (
    CACHE_DIR,
    _http_get_json,
    cache_path,
    load_cache,
    load_csv,
    normalize_contract,
    save_cache,
)  # noqa: F401


def load_funding_csv(path: str | Path) -> pd.DataFrame:
    df = load_csv(path)
    if "funding_rate" not in df.columns and "r" in df.columns:
        df = df.rename(columns={"r": "funding_rate"})
    return df


def fetch_gate_funding(
    contract: str,
    limit: int = 1000,
) -> pd.DataFrame:
    """
    Public GET /futures/usdt/funding_rate (no key).
    Gate returns recent settlements (typically 8h). Paginate by `from`/`to` if needed.
    """
    pair = normalize_contract(contract)
    url = "https://api.gateio.ws/api/v4/futures/usdt/funding_rate"
    raw = _http_get_json(url, {"contract": pair, "limit": min(int(limit), 1000)})
    rows = []
    for item in raw or []:
        ts = item.get("t") or item.get("time")
        rate = item.get("r") if item.get("r") is not None else item.get("rate")
        if ts is None or rate is None:
            continue
        rows.append(
            {
                "timestamp": pd.to_datetime(int(ts), unit="s", utc=True),
                "funding_rate": float(rate),
                "contract": pair,
            }
        )
    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.drop_duplicates(subset=["timestamp"]).sort_values("timestamp").reset_index(drop=True)
    df.attrs["source"] = "gate_futures_usdt_funding_rate"
    df.attrs["symbol"] = pair
    df.attrs["market"] = "futures"
    return df


def fetch_funding_cached(
    contract: str,
    cache_only: bool = False,
    force_refresh: bool = False,
) -> pd.DataFrame:
    pair = normalize_contract(contract)
    path = cache_path(pair, "8h", market="futures", kind="funding")
    cached = None if force_refresh else load_cache(path)
    if cache_only:
        if cached is None or cached.empty:
            raise RuntimeError(f"--cache-only but no funding cache at {path}")
        return cached
    if cached is not None and not cached.empty:
        # Refresh only if last settlement is older than ~10h
        last = cached["timestamp"].iloc[-1]
        age_h = (pd.Timestamp.now(tz="UTC") - last).total_seconds() / 3600.0
        if age_h < 10:
            cached.attrs["cache_hit"] = True
            return cached
    try:
        fresh = fetch_gate_funding(pair)
    except Exception as exc:  # noqa: BLE001
        if cached is not None and not cached.empty:
            cached.attrs["fetch_error"] = str(exc)
            return cached
        raise
    if cached is not None and not cached.empty and not fresh.empty:
        merged = pd.concat([cached, fresh], ignore_index=True)
        merged = merged.drop_duplicates(subset=["timestamp"]).sort_values("timestamp").reset_index(drop=True)
        merged.attrs["source"] = "cache+funding"
        save_cache(merged, path)
        return merged
    if not fresh.empty:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        save_cache(fresh, path)
    return fresh


def synthetic_funding(
    timestamps: pd.Series,
    rate: float = 0.0001,
    hours: int = 8,
) -> pd.Series:
    """
    Assign a constant funding rate on 00:00/08:00/16:00 UTC bars (or every `hours`).
    Used when history is missing so the cost model still runs.
    """
    ts = pd.to_datetime(timestamps, utc=True)
    hours_ok = ts.dt.hour % hours == 0
    minute_ok = ts.dt.minute == 0
    return pd.Series(rate, index=timestamps.index).where(hours_ok & minute_ok, 0.0)


def align_funding_to_bars(
    bars: pd.DataFrame,
    funding: pd.DataFrame | None,
    fallback_rate: float = 0.0001,
) -> pd.DataFrame:
    """Add a `funding_rate` column to OHLCV (0 on non-settlement bars)."""
    out = bars.copy()
    if funding is None or funding.empty or "funding_rate" not in funding.columns:
        out["funding_rate"] = synthetic_funding(out["timestamp"], rate=fallback_rate)
        out.attrs["funding_source"] = "synthetic"
        return out
    f = funding[["timestamp", "funding_rate"]].copy()
    f["timestamp"] = pd.to_datetime(f["timestamp"], utc=True).astype("datetime64[ns, UTC]")
    out["timestamp"] = pd.to_datetime(out["timestamp"], utc=True).astype("datetime64[ns, UTC]")
    merged = pd.merge_asof(
        out.sort_values("timestamp"),
        f.sort_values("timestamp"),
        on="timestamp",
        direction="backward",
        tolerance=pd.Timedelta("1h"),
    )
    # Apply rate only on bars near a settlement (avoid carrying last rate every bar)
    if "funding_rate" not in merged.columns:
        merged["funding_rate"] = 0.0
    settled = merged["funding_rate"].notna()
    # Zero-out if the asof match is older than ~1h already handled by tolerance
    merged["funding_rate"] = merged["funding_rate"].fillna(0.0)
    merged.loc[~settled, "funding_rate"] = 0.0
    merged.attrs["funding_source"] = funding.attrs.get("source", "history")
    return merged.reset_index(drop=True)


