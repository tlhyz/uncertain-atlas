"""
Binance USDT-M perpetual historical aggTrades (public, no API key).

Primary source: data.binance.vision daily ZIP (geo-block safe).
Fallback: GET /fapi/v1/aggTrades (may 451 in restricted regions).
"""

from __future__ import annotations

import io
import re
import time
import zipfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from qtb.data.candles import CACHE_DIR, load_cache, save_cache

try:
    import httpx
except ImportError:  # pragma: no cover
    httpx = None  # type: ignore

VISION = "https://data.binance.vision/data/futures/um/daily/aggTrades"
VISION_KLINES = "https://data.binance.vision/data/futures/um/daily/klines"
FAPI = "https://fapi.binance.com/fapi/v1/aggTrades"
DEFAULT_SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "SOXLUSDT", "SNXXUSDT")

_SYMBOL_MAP = {
    "BTC": "BTCUSDT",
    "ETH": "ETHUSDT",
    "SOL": "SOLUSDT",
    "SOXL": "SOXLUSDT",
    "SNXX": "SNXXUSDT",
    "BTCUSDT": "BTCUSDT",
    "ETHUSDT": "ETHUSDT",
    "SOLUSDT": "SOLUSDT",
    "SOXLUSDT": "SOXLUSDT",
    "SNXXUSDT": "SNXXUSDT",
}


def normalize_symbol(symbol: str) -> str:
    s = symbol.upper().replace("/", "").replace("_", "")
    if s in _SYMBOL_MAP:
        return _SYMBOL_MAP[s]
    if s.endswith("USDT"):
        return s
    return s + "USDT"


def _timestamp_to_ms(ts: pd.Series) -> pd.Series:
    """Convert datetime64 series to epoch milliseconds."""
    arr = ts.astype("int64")
    unit = getattr(ts.dtype, "unit", "ns")
    if unit == "ms":
        return arr
    if unit == "us":
        return arr // 1_000
    if unit == "s":
        return arr * 1_000
    return arr // 1_000_000  # ns → ms


def _save_trades_cache(df: pd.DataFrame, path: Path) -> None:
    out = df.copy()
    if "ts_ms" in out.columns:
        out["ts_ms"] = pd.to_numeric(out["ts_ms"], errors="coerce").astype("Int64")
    else:
        out["ts_ms"] = _timestamp_to_ms(out["timestamp"])
    cols = ["ts_ms", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"]
    path.parent.mkdir(parents=True, exist_ok=True)
    out[cols].to_csv(path, index=False)
    path.with_suffix(".meta.json").write_text(
        '{"source":"binance_vision_daily_aggTrades","format":"ts_ms"}', encoding="utf-8"
    )


def _load_trades_cache(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    raw = pd.read_csv(path)
    if raw.empty:
        return None
    if "ts_ms" in raw.columns:
        ts_ms = pd.to_numeric(raw["ts_ms"], errors="coerce")
        # Corrupt cache: ms values far below year 2020 epoch
        if ts_ms.max() < 1_500_000_000_000:
            path.unlink(missing_ok=True)
            path.with_suffix(".meta.json").unlink(missing_ok=True)
            return None
        raw["timestamp"] = pd.to_datetime(ts_ms, unit="ms", utc=True)
    elif "timestamp" in raw.columns:
        raw["timestamp"] = pd.to_datetime(raw["timestamp"], utc=True, errors="coerce")
    for c in ("price", "qty", "quote_qty"):
        raw[c] = raw[c].astype(float)
    if "timestamp" not in raw.columns or raw["timestamp"].isna().sum() > len(raw) * 0.05:
        path.unlink(missing_ok=True)
        return None
    raw.attrs["source"] = "binance_futures_cached_aggTrades"
    return raw[["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"]].reset_index(drop=True)


def trades_day_cache_path(symbol: str, day: date) -> Path:
    sym = normalize_symbol(symbol)
    return CACHE_DIR / f"binance_futures_{sym}_aggTrades_{day.isoformat()}.csv"


def vision_zip_url(symbol: str, day: date) -> str:
    sym = normalize_symbol(symbol)
    return f"{VISION}/{sym}/{sym}-aggTrades-{day.isoformat()}.zip"


def vision_klines_url(symbol: str, interval: str, day: date) -> str:
    sym = normalize_symbol(symbol)
    return f"{VISION_KLINES}/{sym}/{interval}/{sym}-{interval}-{day.isoformat()}.zip"


def klines_range_cache_path(symbol: str, interval: str, start: date, end: date) -> Path:
    sym = normalize_symbol(symbol)
    return CACHE_DIR / f"binance_futures_{sym}_{interval}_{start.isoformat()}_{end.isoformat()}_klines.csv"


def _download_vision_klines_day(symbol: str, interval: str, day: date) -> pd.DataFrame:
    if httpx is None:
        raise RuntimeError("httpx required")
    url = vision_klines_url(symbol, interval, day)
    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        r = client.get(url)
        if r.status_code == 404:
            return pd.DataFrame()
        r.raise_for_status()
        zf = zipfile.ZipFile(io.BytesIO(r.content))
        text = zf.read(zf.namelist()[0]).decode("utf-8")
    df = pd.read_csv(io.StringIO(text))
    if df.empty:
        return df
    df["timestamp"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
    for col in ("open", "high", "low", "close", "volume", "quote_volume"):
        if col in df.columns:
            df[col] = df[col].astype(float)
    out = df[["timestamp", "open", "high", "low", "close", "volume", "quote_volume"]].sort_values("timestamp")
    out.attrs["source"] = "binance_vision_daily_klines"
    return out.reset_index(drop=True)


def _load_klines_from_overlap_cache(
    sym: str, interval: str, t0: date, t1: date,
) -> pd.DataFrame | None:
    """If exact range cache missing, slice from a superset cached range."""
    pat = re.compile(
        rf"binance_futures_{re.escape(sym)}_{re.escape(interval)}_"
        r"(?P<s>\d{4}-\d{2}-\d{2})_(?P<e>\d{4}-\d{2}-\d{2})_klines\.csv$"
    )
    best: pd.DataFrame | None = None
    for p in CACHE_DIR.glob(f"binance_futures_{sym}_{interval}_*_klines.csv"):
        m = pat.match(p.name)
        if not m:
            continue
        c0 = date.fromisoformat(m.group("s"))
        c1 = date.fromisoformat(m.group("e"))
        if c0 <= t0 and c1 >= t1:
            df = load_cache(p)
            if df is None or df.empty:
                continue
            sub = df[
                (df["timestamp"] >= pd.Timestamp(t0, tz="UTC"))
                & (df["timestamp"] <= pd.Timestamp(t1, tz="UTC") + pd.Timedelta(hours=23))
            ]
            if not sub.empty and (best is None or len(sub) > len(best)):
                best = sub.copy()
    if best is not None:
        best.attrs["source"] = "binance_vision_klines_cached_subset"
        return best.reset_index(drop=True)
    return None


def fetch_binance_klines_range(
    symbol: str,
    interval: str,
    start: str | pd.Timestamp,
    end: str | pd.Timestamp,
    *,
    cache_only: bool = False,
) -> pd.DataFrame:
    """Download 1h (or other) klines from Binance Vision daily ZIPs."""
    sym = normalize_symbol(symbol)
    t0 = pd.Timestamp(start, tz="UTC").date()
    t1 = pd.Timestamp(end, tz="UTC").date()
    path = klines_range_cache_path(sym, interval, t0, t1)
    cached = load_cache(path)
    if cached is not None and not cached.empty:
        cached.attrs["source"] = "binance_vision_klines_cached"
        return cached
    overlap = _load_klines_from_overlap_cache(sym, interval, t0, t1)
    if overlap is not None and not overlap.empty:
        return overlap
    if cache_only:
        raise RuntimeError(f"cache-only missing {path}")

    parts: list[pd.DataFrame] = []
    d = t0
    while d <= t1:
        part = _download_vision_klines_day(sym, interval, d)
        if not part.empty:
            parts.append(part)
        d += timedelta(days=1)
    if not parts:
        raise RuntimeError(f"Binance Vision klines empty {sym} {start}->{end}")
    out = pd.concat(parts, ignore_index=True).drop_duplicates(subset=["timestamp"]).sort_values("timestamp")
    out.attrs["source"] = "binance_vision_klines_range"
    out.attrs["symbol"] = sym
    save_cache(out, path)
    print(f"[binance-klines] {sym} {interval} {start}->{end} bars={len(out)}")
    return out.reset_index(drop=True)


def _parse_vision_csv(text: str) -> pd.DataFrame:
    df = pd.read_csv(io.StringIO(text))
    if df.empty:
        return pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])
    df = df.rename(
        columns={
            "agg_trade_id": "agg_id",
            "quantity": "qty",
            "transact_time": "ts_ms",
        }
    )
    df["timestamp"] = pd.to_datetime(df["ts_ms"], unit="ms", utc=True)
    df["price"] = df["price"].astype(float)
    df["qty"] = df["qty"].astype(float)
    df["quote_qty"] = df["price"] * df["qty"]
    df["is_buyer_maker"] = df["is_buyer_maker"].astype(str).str.lower().isin(("true", "1", "yes"))
    out = df[["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id", "ts_ms"]].sort_values("timestamp")
    out.attrs["source"] = "binance_vision_daily_aggTrades"
    return out.reset_index(drop=True)


def _download_vision_day(symbol: str, day: date) -> pd.DataFrame:
    if httpx is None:
        raise RuntimeError("httpx required for Binance Vision download")
    url = vision_zip_url(symbol, day)
    with httpx.Client(timeout=120.0, follow_redirects=True) as client:
        r = client.get(url)
        if r.status_code == 404:
            return pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])
        r.raise_for_status()
        zf = zipfile.ZipFile(io.BytesIO(r.content))
        name = zf.namelist()[0]
        text = zf.read(name).decode("utf-8")
    return _parse_vision_csv(text)


def _parse_agg_batch(batch: list[dict[str, Any]]) -> pd.DataFrame:
    if not batch:
        return pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])
    rows = []
    for t in batch:
        px = float(t["p"])
        qty = float(t["q"])
        rows.append(
            {
                "timestamp": pd.to_datetime(int(t["T"]), unit="ms", utc=True),
                "price": px,
                "qty": qty,
                "quote_qty": px * qty,
                "is_buyer_maker": bool(t["m"]),
                "agg_id": int(t["a"]),
                "ts_ms": int(t["T"]),
            }
        )
    df = pd.DataFrame(rows)
    df.attrs["source"] = "binance_futures_public_aggTrades"
    return df


def _fetch_rest_day(symbol: str, day: date, sleep_s: float = 0.08) -> pd.DataFrame:
    if httpx is None:
        return pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])
    sym = normalize_symbol(symbol)
    start = datetime(day.year, day.month, day.day, tzinfo=timezone.utc)
    end = start + timedelta(days=1) - timedelta(milliseconds=1)
    start_ms = int(start.timestamp() * 1000)
    end_ms = int(end.timestamp() * 1000)
    rows: list[dict[str, Any]] = []
    cur = start_ms
    with httpx.Client(timeout=60.0) as client:
        while cur <= end_ms:
            params = {"symbol": sym, "startTime": cur, "endTime": end_ms, "limit": 1000}
            r = client.get(FAPI, params=params)
            if r.status_code in (451, 403):
                return pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])
            if r.status_code == 429:
                time.sleep(2.0)
                continue
            r.raise_for_status()
            batch = r.json()
            if not batch:
                break
            rows.extend(batch)
            cur = int(batch[-1]["T"]) + 1
            if len(batch) < 1000:
                break
            time.sleep(sleep_s)
    return _parse_agg_batch(rows)


def fetch_agg_trades_day(
    symbol: str,
    day: date,
    *,
    cache_only: bool = False,
    force_refresh: bool = False,
    sleep_s: float = 0.08,
) -> pd.DataFrame:
    """Download one UTC calendar day of aggTrades from Binance Vision (preferred)."""
    sym = normalize_symbol(symbol)
    path = trades_day_cache_path(sym, day)
    if not force_refresh:
        cached = _load_trades_cache(path)
        if cached is not None and not cached.empty:
            cached.attrs["symbol"] = sym
            cached.attrs["day"] = day.isoformat()
            return cached
        # Legacy corrupt CSV (ISO timestamps with subseconds) — force re-download
        legacy = load_cache(path)
        if legacy is not None and legacy["timestamp"].isna().sum() > len(legacy) * 0.05:
            path.unlink(missing_ok=True)

    if cache_only:
        return pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])

    df = _download_vision_day(sym, day)
    if df.empty:
        df = _fetch_rest_day(sym, day, sleep_s=sleep_s)
    df.attrs["symbol"] = sym
    df.attrs["day"] = day.isoformat()
    df.attrs["market"] = "binance_futures"
    if not df.empty:
        _save_trades_cache(df, path)
        print(f"[binance-trades] {sym} {day} rows={len(df)} source={df.attrs.get('source')}")
    return df


def fetch_agg_trades_range(
    symbol: str,
    start: str | pd.Timestamp,
    end: str | pd.Timestamp,
    *,
    cache_only: bool = False,
    force_refresh: bool = False,
) -> pd.DataFrame:
    """Concatenate daily aggTrades caches for [start, end] inclusive (UTC dates)."""
    t0 = pd.Timestamp(start, tz="UTC").date()
    t1 = pd.Timestamp(end, tz="UTC").date()
    parts: list[pd.DataFrame] = []
    d = t0
    while d <= t1:
        part = fetch_agg_trades_day(symbol, d, cache_only=cache_only, force_refresh=force_refresh)
        if not part.empty:
            parts.append(part)
        d += timedelta(days=1)
    if not parts:
        out = pd.DataFrame(columns=["timestamp", "price", "qty", "quote_qty", "is_buyer_maker", "agg_id"])
    else:
        out = pd.concat(parts, ignore_index=True).drop_duplicates(subset=["agg_id"]).sort_values("timestamp")
    sym = normalize_symbol(symbol)
    out.attrs["source"] = "binance_vision_aggTrades_range"
    out.attrs["symbol"] = sym
    out.attrs["start"] = str(t0)
    out.attrs["end"] = str(t1)
    out.attrs["rows"] = len(out)
    return out.reset_index(drop=True)


def download_symbols_range(
    symbols: list[str],
    start: str,
    end: str,
    *,
    cache_only: bool = False,
) -> dict[str, pd.DataFrame]:
    """Download aggTrades for multiple symbols; returns {symbol: df}."""
    out: dict[str, pd.DataFrame] = {}
    for sym in symbols:
        bn = normalize_symbol(sym)
        print(f"\n[download] {bn} {start} -> {end}")
        out[bn] = fetch_agg_trades_range(bn, start, end, cache_only=cache_only)
    return out


def trades_quote_volume_in_window(trades: pd.DataFrame, t0: pd.Timestamp, t1: pd.Timestamp) -> float:
    if trades.empty:
        return 0.0
    m = (trades["timestamp"] >= t0) & (trades["timestamp"] < t1)
    sub = trades.loc[m]
    if sub.empty:
        return 0.0
    return float(sub["quote_qty"].sum())


def slice_trades_for_bar(trades: pd.DataFrame, bar_open: pd.Timestamp, interval: str = "1h") -> pd.DataFrame:
    """Return aggTrades belonging to one bar [open, next_open)."""
    if trades.empty:
        return trades
    step = {"1h": pd.Timedelta(hours=1), "4h": pd.Timedelta(hours=4), "1m": pd.Timedelta(minutes=1)}.get(
        interval, pd.Timedelta(hours=1)
    )
    t1 = bar_open + step
    m = (trades["timestamp"] >= bar_open) & (trades["timestamp"] < t1)
    return trades.loc[m].sort_values("timestamp").reset_index(drop=True)
