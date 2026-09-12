"""Real Gate data only. Overlap windows. No synthetic ticks. No Binance proxy for A/B."""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal

import pandas as pd

from qtb.data.candles import (
    CACHE_DIR,
    _http_get_json,
    _INTERVAL_SEC,
    cache_path,
    load_cache,
    normalize_contract,
    save_cache,
)
from qtb.data.contracts import ContractSpec, fetch_contract_spec
from qtb.data.funding import fetch_funding_cached

from .universe import ABPair

Market = Literal["spot", "futures"]

# Gate public candlesticks: "Maximum 10000 points ago are allowed"
GATE_MAX_BARS = 10_000
FORBIDDEN_SOURCES = ("synthetic", "binance", "generated", "fake", "proxy")


@dataclass
class SeriesMeta:
    symbol: str
    market: str
    interval: str
    source: str
    start: str
    end: str
    bars: int
    nonzero_quote_bars: int
    cache_path: str
    api_calls: int = 0
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class OverlapWindow:
    pair: str
    etf: str
    perp: str
    underlying_spot: str
    interval: str
    ab_start: pd.Timestamp
    ab_end: pd.Timestamp
    bars: int
    etf_meta: SeriesMeta
    perp_meta: SeriesMeta
    spot_meta: SeriesMeta
    funding_source: str
    funding_rows: int
    snapshot: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["ab_start"] = str(self.ab_start)
        d["ab_end"] = str(self.ab_end)
        return d


def _assert_real_source(source: str, symbol: str) -> None:
    s = (source or "").lower()
    for bad in FORBIDDEN_SOURCES:
        if bad in s:
            raise RuntimeError(
                f"Refusing non-Gate / synthetic data for {symbol}: source={source!r}"
            )


def _parse_spot_rows(raw: list) -> list[dict]:
    rows = []
    for item in raw:
        if isinstance(item, dict):
            rows.append(
                {
                    "timestamp": pd.to_datetime(int(item["t"]), unit="s", utc=True),
                    "open": float(item["o"]),
                    "high": float(item["h"]),
                    "low": float(item["l"]),
                    "close": float(item["c"]),
                    "volume": float(item.get("v", item.get("base_volume", 0)) or 0),
                    "quote_volume": float(item.get("sum", item.get("quote_volume", 0)) or 0),
                }
            )
            continue
        # [ts, quote_vol, close, high, low, open, base_vol, is_closed]
        rows.append(
            {
                "timestamp": pd.to_datetime(int(item[0]), unit="s", utc=True),
                "open": float(item[5]),
                "high": float(item[3]),
                "low": float(item[4]),
                "close": float(item[2]),
                "volume": float(item[6]) if len(item) > 6 else 0.0,
                "quote_volume": float(item[1]) if len(item) > 1 else 0.0,
            }
        )
    return rows


def _parse_fut_rows(raw: list) -> list[dict]:
    rows = []
    for item in raw:
        if isinstance(item, dict):
            rows.append(
                {
                    "timestamp": pd.to_datetime(int(item["t"]), unit="s", utc=True),
                    "open": float(item["o"]),
                    "high": float(item["h"]),
                    "low": float(item["l"]),
                    "close": float(item["c"]),
                    "volume": float(item.get("v", 0) or 0),
                    "quote_volume": float(item.get("sum", 0) or 0),
                }
            )
        else:
            rows.extend(_parse_spot_rows([item]))
    return rows


def _rows_to_df(rows: list[dict], source: str, symbol: str, interval: str, market: str) -> pd.DataFrame:
    if not rows:
        raise RuntimeError(f"No real candles for {market} {symbol} {interval}")
    out = pd.DataFrame(rows).drop_duplicates(subset=["timestamp"]).sort_values("timestamp")
    out = out.reset_index(drop=True)
    out.attrs["source"] = source
    out.attrs["symbol"] = symbol
    out.attrs["interval"] = interval
    out.attrs["market"] = market
    _assert_real_source(source, symbol)
    return out


def fetch_gate_candles_capped(
    symbol: str,
    interval: str,
    market: Market,
    max_bars: int = GATE_MAX_BARS,
    max_pages: int = 12,
) -> pd.DataFrame:
    """Paginate Gate public candles, stop at exchange 10000-bar ceiling."""
    pair = normalize_contract(symbol) if market == "futures" else (
        symbol.strip().upper() if symbol.isascii() else symbol.strip()
    )
    if market == "futures":
        url = "https://api.gateio.ws/api/v4/futures/usdt/candlesticks"
        id_key = "contract"
        parse = _parse_fut_rows
        source = "gate_futures_usdt_candlesticks"
    else:
        url = "https://api.gateio.ws/api/v4/spot/candlesticks"
        id_key = "currency_pair"
        parse = _parse_spot_rows
        source = "gate_public_spot_candlesticks"
    extra_sec = {"1s": 1, "10s": 10}
    step = _INTERVAL_SEC.get(interval) or extra_sec.get(interval)
    if step is None:
        raise ValueError(f"unsupported interval {interval}")
    cursor_to = int(time.time())
    rows: list[dict] = []
    pages = 0
    while len(rows) < max_bars and pages < max_pages:
        pages += 1
        remain = max_bars - len(rows)
        batch = _http_get_json(
            url,
            {id_key: pair, "interval": interval, "to": cursor_to, "limit": min(1000, remain)},
        )
        if not batch:
            break
        parsed = parse(batch)
        if not parsed:
            break
        rows.extend(parsed)
        earliest = min(int(r["timestamp"].timestamp()) for r in parsed)
        next_to = earliest - step
        if next_to >= cursor_to:
            break
        cursor_to = next_to
        if len(batch) < 1000:
            break
    df = _rows_to_df(rows, source, pair, interval, market)
    df.attrs["api_pages"] = pages
    return df


def fetch_series_cached(
    symbol: str,
    interval: str,
    market: Market,
    cache_only: bool = False,
    force_refresh: bool = False,
    max_bars: int = GATE_MAX_BARS,
) -> pd.DataFrame:
    pair = normalize_contract(symbol) if market == "futures" else symbol.strip().upper()
    path = cache_path(pair, interval, market=market, kind="ab_candles")
    cached = None if force_refresh else load_cache(path)
    if cached is not None and not cached.empty:
        if "quote_volume" not in cached.columns:
            cached["quote_volume"] = 0.0
        src = str(cached.attrs.get("source") or "")
        _assert_real_source(src, pair)
        if cache_only or (not force_refresh and len(cached) >= min(200, max_bars // 20)):
            # Incremental tail fill when not cache-only
            if cache_only:
                cached.attrs["cache_hit"] = True
                cached.attrs["cache_path"] = str(path)
                return cached
            last = int(cached["timestamp"].iloc[-1].timestamp())
            now = int(time.time())
            step = _INTERVAL_SEC.get(interval, 3600)
            if now - last < int(step * 1.6):
                cached.attrs["cache_hit"] = True
                cached.attrs["cache_path"] = str(path)
                return cached
    if cache_only:
        if cached is None or cached.empty:
            raise RuntimeError(f"cache-only missing {market} {pair} {interval} at {path}")
        return cached
    fresh = fetch_gate_candles_capped(pair, interval, market, max_bars=max_bars)
    if cached is not None and not cached.empty:
        fresh = (
            pd.concat([cached, fresh], ignore_index=True)
            .drop_duplicates(subset=["timestamp"])
            .sort_values("timestamp")
            .reset_index(drop=True)
        )
        fresh.attrs["source"] = f"cache+gate:{pair}"
        fresh.attrs["symbol"] = pair
        fresh.attrs["interval"] = interval
        fresh.attrs["market"] = market
    save_cache(fresh, path)
    fresh.attrs["cache_path"] = str(path)
    fresh.attrs["cache_hit"] = False
    print(f"[ab-data] {market} {pair} {interval} bars={len(fresh)} {fresh['timestamp'].iloc[0]} -> {fresh['timestamp'].iloc[-1]}")
    return fresh


def fetch_etf_snapshot(symbol: str) -> dict[str, Any]:
    """Live ETF ticker: NAV / effective leverage / spread. Snapshot only (no NAV history)."""
    url = "https://api.gateio.ws/api/v4/spot/tickers"
    raw = _http_get_json(url, {"currency_pair": symbol})
    row = raw[0] if isinstance(raw, list) and raw else raw
    if not isinstance(row, dict):
        return {"symbol": symbol, "nav_available": False}
    last = float(row.get("last") or 0)
    nav = row.get("etf_net_value")
    nav_f = float(nav) if nav not in (None, "") else None
    prem = (last / nav_f - 1.0) if nav_f and nav_f > 0 and last > 0 else None
    bid = float(row.get("highest_bid") or 0) or None
    ask = float(row.get("lowest_ask") or 0) or None
    spread = ((ask - bid) / last) if bid and ask and last else None
    lev = row.get("etf_leverage")
    return {
        "symbol": symbol,
        "last": last,
        "etf_net_value": nav_f,
        "etf_pre_net_value": float(row["etf_pre_net_value"]) if row.get("etf_pre_net_value") else None,
        "etf_pre_timestamp": row.get("etf_pre_timestamp"),
        "etf_leverage": float(lev) if lev not in (None, "") else None,
        "premium_discount": prem,
        "bid": bid,
        "ask": ask,
        "spread": spread,
        "quote_volume_24h": float(row.get("quote_volume") or 0),
        "nav_available": nav_f is not None,
        "nav_history": False,
        "source": "gate_spot_tickers",
    }


def _meta_from_df(df: pd.DataFrame, cache: str = "") -> SeriesMeta:
    q = df["quote_volume"] if "quote_volume" in df.columns else pd.Series(0.0, index=df.index)
    return SeriesMeta(
        symbol=str(df.attrs.get("symbol") or ""),
        market=str(df.attrs.get("market") or ""),
        interval=str(df.attrs.get("interval") or ""),
        source=str(df.attrs.get("source") or ""),
        start=str(df["timestamp"].iloc[0]),
        end=str(df["timestamp"].iloc[-1]),
        bars=int(len(df)),
        nonzero_quote_bars=int((q.fillna(0) > 0).sum()),
        cache_path=cache or str(df.attrs.get("cache_path") or ""),
        api_calls=int(df.attrs.get("api_pages") or df.attrs.get("api_calls") or 0),
        notes=["real_gate_only"],
    )


def align_on_timestamp(*frames: pd.DataFrame) -> list[pd.DataFrame]:
    if not frames:
        return []
    idx = frames[0]["timestamp"]
    for f in frames[1:]:
        idx = idx[idx.isin(f["timestamp"])]
    out = []
    for f in frames:
        g = f.loc[f["timestamp"].isin(idx)].drop_duplicates("timestamp").sort_values("timestamp")
        out.append(g.reset_index(drop=True))
    return out


def first_liquid_ts(df: pd.DataFrame, min_quote: float = 1.0) -> pd.Timestamp:
    if "quote_volume" in df.columns:
        hit = df.loc[df["quote_volume"].fillna(0) >= min_quote]
        if not hit.empty:
            return pd.Timestamp(hit["timestamp"].iloc[0])
    return pd.Timestamp(df["timestamp"].iloc[0])


@dataclass
class PairData:
    pair: ABPair
    interval: str
    etf: pd.DataFrame
    perp: pd.DataFrame
    spot: pd.DataFrame
    funding: pd.DataFrame
    contract: ContractSpec
    window: OverlapWindow
    snapshot: dict[str, Any]
    etf_short: pd.DataFrame | None = None


def load_pair_data(
    pair: ABPair,
    interval: str,
    cache_only: bool = False,
    include_short: bool = False,
) -> PairData:
    if not pair.has_perp:
        raise RuntimeError(f"{pair.name}: NO DIRECT PERPETUAL COMPARATOR")

    etf = fetch_series_cached(pair.etf_spot, interval, "spot", cache_only=cache_only)
    perp = fetch_series_cached(pair.perp, interval, "futures", cache_only=cache_only)
    spot = fetch_series_cached(pair.underlying_spot, interval, "spot", cache_only=cache_only)
    funding = fetch_funding_cached(pair.perp, cache_only=cache_only)
    if funding is None or funding.empty:
        raise RuntimeError(f"{pair.perp}: real funding history unavailable — refusing synthetic substitute")
    spec = fetch_contract_spec(pair.perp)
    snap = fetch_etf_snapshot(pair.etf_spot) if not cache_only else {"symbol": pair.etf_spot, "nav_history": False}

    etf_a, perp_a, spot_a = align_on_timestamp(etf, perp, spot)
    if etf_a.empty:
        raise RuntimeError(f"{pair.name}: empty overlap after timestamp align")

    start = max(first_liquid_ts(etf_a), first_liquid_ts(perp_a), first_liquid_ts(spot_a))
    mask = etf_a["timestamp"] >= start
    etf_a = etf_a.loc[mask].reset_index(drop=True)
    perp_a = perp_a.loc[perp_a["timestamp"].isin(etf_a["timestamp"])].reset_index(drop=True)
    spot_a = spot_a.loc[spot_a["timestamp"].isin(etf_a["timestamp"])].reset_index(drop=True)
    if len(etf_a) < 24:
        raise RuntimeError(f"{pair.name} {interval}: overlap too short ({len(etf_a)} bars)")

    etf_short = None
    if include_short and pair.etf_short:
        try:
            raw_s = fetch_series_cached(pair.etf_short, interval, "spot", cache_only=cache_only)
            etf_short = raw_s
        except Exception as exc:  # noqa: BLE001
            print(f"[ab-data] short ETF {pair.etf_short} skipped: {exc}")

    window = OverlapWindow(
        pair=pair.name,
        etf=pair.etf_spot,
        perp=pair.perp or "",
        underlying_spot=pair.underlying_spot,
        interval=interval,
        ab_start=pd.Timestamp(etf_a["timestamp"].iloc[0]),
        ab_end=pd.Timestamp(etf_a["timestamp"].iloc[-1]),
        bars=int(len(etf_a)),
        etf_meta=_meta_from_df(etf_a),
        perp_meta=_meta_from_df(perp_a),
        spot_meta=_meta_from_df(spot_a),
        funding_source=str(funding.attrs.get("source") or "gate_futures_usdt_funding_rate"),
        funding_rows=int(len(funding)),
        snapshot=snap,
    )
    return PairData(
        pair=pair,
        interval=interval,
        etf=etf_a,
        perp=perp_a,
        spot=spot_a,
        funding=funding,
        contract=spec,
        window=window,
        snapshot=snap,
        etf_short=etf_short,
    )


def attach_funding(perp: pd.DataFrame, funding: pd.DataFrame) -> pd.DataFrame:
    """Align real funding prints onto bars. Rate is 0 except near a settlement."""
    out = perp.copy()
    f = funding[["timestamp", "funding_rate"]].copy()
    f["timestamp"] = pd.to_datetime(f["timestamp"], utc=True)
    out["timestamp"] = pd.to_datetime(out["timestamp"], utc=True)
    out = out.sort_values("timestamp")
    f = f.sort_values("timestamp")
    merged = pd.merge_asof(out, f, on="timestamp", direction="backward", tolerance=pd.Timedelta("50min"))
    merged["funding_rate"] = merged["funding_rate"].fillna(0.0)
    # Only keep the print on the first bar after settlement, not every subsequent bar.
    settled = merged["funding_rate"] != 0.0
    dup = settled & settled.shift(1, fill_value=False) & (merged["funding_rate"] == merged["funding_rate"].shift(1))
    merged.loc[dup, "funding_rate"] = 0.0
    merged.attrs["funding_source"] = funding.attrs.get("source", "history")
    return merged.reset_index(drop=True)


def write_provenance(path: Path, windows: list[OverlapWindow], extra: dict[str, Any] | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": pd.Timestamp.now(tz="UTC").isoformat(),
        "rule": "real_gate_only_no_synthetic_ticks",
        "gate_max_bars": GATE_MAX_BARS,
        "windows": [w.as_dict() for w in windows],
        "extra": extra or {},
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    return path
