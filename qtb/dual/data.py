"""Real Gate perpetual data + optional Binance history for template search."""

from __future__ import annotations

import json
import io
import zipfile
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.ab.data import (
    GATE_MAX_BARS,
    SeriesMeta,
    _meta_from_df,
    align_on_timestamp,
    attach_funding,
    fetch_series_cached,
    first_liquid_ts,
)
from qtb.data.candles import CACHE_DIR, _INTERVAL_SEC, cache_path, load_cache, save_cache
from qtb.data.contracts import fetch_contract_spec
from qtb.data.funding import fetch_funding_cached

from .universe import CRYPTO_CORE, SEED_WINDOWS, SYMBOL_PERP, SeedWindow, TECH_SYMBOLS

try:
    import httpx
except ImportError:  # pragma: no cover
    httpx = None  # type: ignore


@dataclass
class WindowCoverage:
    window: SeedWindow
    executable: bool
    status: Literal["EXECUTABLE", "STRUCTURAL_SEED_ONLY", "PARTIAL"]
    gate_bars: int
    gate_start: str | None
    gate_end: str | None
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class MarketData:
    symbol: str
    perp: str
    interval: str
    bars: pd.DataFrame
    funding: pd.DataFrame
    meta: SeriesMeta
    contract: Any = None
    trades: pd.DataFrame | None = None
    data_source: Literal["gate", "binance"] = "gate"
    trades_lazy: bool = False  # load daily aggTrades from disk per bar


@dataclass
class DualDataset:
    interval: str
    tech: dict[str, MarketData]
    crypto: dict[str, MarketData]
    aligned_index: pd.DatetimeIndex
    seed_coverage: list[WindowCoverage]
    overlap_start: pd.Timestamp
    overlap_end: pd.Timestamp
    provenance: dict[str, Any] = field(default_factory=dict)


def _binance_cache_path(symbol: str, interval: str) -> Path:
    return CACHE_DIR / f"binance_futures_{symbol}_{interval}_candles.csv"


def fetch_binance_futures_klines(
    symbol: str,
    interval: str = "1h",
    start_ms: int | None = None,
    end_ms: int | None = None,
    cache_only: bool = False,
) -> pd.DataFrame:
    """Download Binance USDT-M futures klines for template matching (not execution)."""
    path = _binance_cache_path(symbol, interval)
    step_ms = _INTERVAL_SEC.get(interval, 3600) * 1000
    cached = load_cache(path)
    if cached is not None and not cached.empty:
        if start_ms or end_ms:
            t0 = pd.Timestamp(start_ms, unit="ms", tz="UTC") if start_ms else cached["timestamp"].iloc[0]
            t1 = pd.Timestamp(end_ms, unit="ms", tz="UTC") if end_ms else cached["timestamp"].iloc[-1]
            sub = cached[(cached["timestamp"] >= t0) & (cached["timestamp"] <= t1)].copy()
            if len(sub) >= 24:
                sub.attrs = cached.attrs.copy()
                if cache_only:
                    return sub
        elif cache_only:
            cached.attrs["source"] = "binance_futures_cached"
            return cached
        elif not cache_only and len(cached) >= 100:
            # use cache tail incremental only when no explicit range
            last = int(cached["timestamp"].iloc[-1].timestamp() * 1000)
            if end_ms is None or last >= (end_ms or last) - step_ms * 2:
                if start_ms is None:
                    cached.attrs["source"] = "binance_futures_cached"
                    return cached

    if httpx is None:
        if cached is not None:
            return cached
        raise RuntimeError("httpx required for Binance fetch")

    interval_map = {"1h": "1h", "4h": "4h", "1d": "1d", "1m": "1m"}
    bi = interval_map.get(interval, "1h")
    rows: list[list] = []
    cur = start_ms or int(pd.Timestamp("2020-01-01", tz="UTC").timestamp() * 1000)
    end = end_ms or int(time.time() * 1000)

    with httpx.Client(timeout=30.0) as client:
        while cur < end:
            params = {
                "symbol": symbol,
                "interval": bi,
                "startTime": cur,
                "endTime": end,
                "limit": 1500,
            }
            r = client.get("https://fapi.binance.com/fapi/v1/klines", params=params)
            r.raise_for_status()
            batch = r.json()
            if not batch:
                break
            rows.extend(batch)
            last_open = int(batch[-1][0])
            nxt = last_open + step_ms
            if nxt <= cur:
                break
            cur = nxt
            time.sleep(0.12)

    if not rows:
        if cached is not None:
            return cached
        raise RuntimeError(f"Binance {symbol} {interval}: no data")

    df = pd.DataFrame(
        rows,
        columns=[
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "quote_volume", "trades", "taker_buy_base",
            "taker_buy_quote", "ignore",
        ],
    )
    df["timestamp"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
    for col in ("open", "high", "low", "close", "volume", "quote_volume"):
        df[col] = df[col].astype(float)
    df = df[["timestamp", "open", "high", "low", "close", "volume", "quote_volume"]]
    df.attrs["source"] = "binance_futures_public_klines"
    df.attrs["symbol"] = symbol
    df.attrs["interval"] = interval
    df.attrs["market"] = "binance_futures"
    save_cache(df, path)
    return df


def load_perp(symbol: str, interval: str = "1h", cache_only: bool = False) -> MarketData:
    perp = SYMBOL_PERP[symbol]
    bars = fetch_series_cached(perp, interval, "futures", cache_only=cache_only)
    funding = fetch_funding_cached(perp, cache_only=cache_only)
    if funding is None or funding.empty:
        funding = pd.DataFrame({"timestamp": bars["timestamp"], "funding_rate": 0.0})
    bars = attach_funding(bars, funding)
    spec = fetch_contract_spec(perp) if not cache_only else None
    meta = _meta_from_df(bars)
    return MarketData(symbol=symbol, perp=perp, interval=interval, bars=bars, funding=funding, meta=meta, contract=spec)


def check_seed_window(cov: SeedWindow, data: MarketData) -> WindowCoverage:
    start = pd.Timestamp(cov.start, tz="UTC")
    end = pd.Timestamp(cov.end, tz="UTC") + pd.Timedelta(hours=23)
    df = data.bars
    mask = (df["timestamp"] >= start) & (df["timestamp"] <= end)
    sub = df.loc[mask]
    notes: list[str] = []
    if sub.empty:
        notes.append("no Gate bars in seed range")
        return WindowCoverage(cov, False, "STRUCTURAL_SEED_ONLY", 0, None, None, notes)
    qv = sub["quote_volume"].fillna(0) if "quote_volume" in sub.columns else pd.Series(0, index=sub.index)
    liq = int((qv > 0).sum())
    if liq < 24:
        notes.append(f"only {liq} bars with quote_volume in range")
    full_span = (sub["timestamp"].iloc[-1] - sub["timestamp"].iloc[0]).total_seconds() / 86400
    expected = (end - start).days
    if full_span < expected * 0.6:
        notes.append(f"partial span {full_span:.0f}d vs expected {expected}d")
        status: Literal["EXECUTABLE", "STRUCTURAL_SEED_ONLY", "PARTIAL"] = "PARTIAL"
        executable = liq >= 48
    else:
        status = "EXECUTABLE"
        executable = liq >= 48
    return WindowCoverage(
        cov,
        executable,
        status,
        len(sub),
        str(sub["timestamp"].iloc[0]),
        str(sub["timestamp"].iloc[-1]),
        notes,
    )


def load_dual_dataset(interval: str = "1h", cache_only: bool = False) -> DualDataset:
    tech: dict[str, MarketData] = {}
    crypto: dict[str, MarketData] = {}
    for sym in TECH_SYMBOLS:
        tech[sym] = load_perp(sym, interval, cache_only)
    for sym in CRYPTO_CORE:
        crypto[sym] = load_perp(sym, interval, cache_only)

    frames = [tech["SOXL"].bars, tech["SNXX"].bars] + [crypto[s].bars for s in CRYPTO_CORE]
    aligned = align_on_timestamp(*frames)
    tech["SOXL"] = MarketData(
        "SOXL", tech["SOXL"].perp, interval,
        aligned[0], tech["SOXL"].funding, tech["SOXL"].meta, tech["SOXL"].contract,
    )
    tech["SNXX"] = MarketData(
        "SNXX", tech["SNXX"].perp, interval,
        aligned[1], tech["SNXX"].funding, tech["SNXX"].meta, tech["SNXX"].contract,
    )
    for j, sym in enumerate(CRYPTO_CORE):
        crypto[sym] = MarketData(
            sym, crypto[sym].perp, interval,
            aligned[2 + j], crypto[sym].funding, crypto[sym].meta, crypto[sym].contract,
        )

    idx = pd.DatetimeIndex(aligned[0]["timestamp"])
    start = max(first_liquid_ts(tech["SOXL"].bars), first_liquid_ts(tech["SNXX"].bars))
    for s in CRYPTO_CORE:
        start = max(start, first_liquid_ts(crypto[s].bars))
    end = idx[-1]

    seed_cov: list[WindowCoverage] = []
    for sw in SEED_WINDOWS:
        sym = sw.symbol
        md = tech.get(sym) or crypto.get("BTC")
        if md:
            seed_cov.append(check_seed_window(sw, md))

    prov = {
        "interval": interval,
        "tech_symbols": list(TECH_SYMBOLS),
        "crypto_symbols": list(CRYPTO_CORE),
        "overlap_start": str(start),
        "overlap_end": str(end),
        "bars": len(idx),
        "seed_windows": [c.as_dict() for c in seed_cov],
    }
    return DualDataset(
        interval=interval,
        tech=tech,
        crypto=crypto,
        aligned_index=idx,
        seed_coverage=seed_cov,
        overlap_start=start,
        overlap_end=end,
        provenance=prov,
    )


def slice_window(data: DualDataset, start: str, end: str) -> DualDataset:
    t0 = pd.Timestamp(start, tz="UTC")
    t1 = pd.Timestamp(end, tz="UTC") + pd.Timedelta(hours=23)

    def _slice_md(md: MarketData) -> MarketData:
        m = (md.bars["timestamp"] >= t0) & (md.bars["timestamp"] <= t1)
        sub = md.bars.loc[m].reset_index(drop=True)
        return MarketData(md.symbol, md.perp, md.interval, sub, md.funding, md.meta, md.contract)

    tech = {k: _slice_md(v) for k, v in data.tech.items()}
    crypto = {k: _slice_md(v) for k, v in data.crypto.items()}
    idx = pd.DatetimeIndex(tech["SOXL"].bars["timestamp"])
    return DualDataset(
        data.interval, tech, crypto, idx, data.seed_coverage,
        t0, t1, data.provenance,
    )


def write_provenance(data: DualDataset, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "provenance.json").write_text(
        json.dumps(data.provenance, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )


def load_binance_crypto_dataset(
    start: str,
    end: str,
    interval: str = "1h",
    *,
    cache_only: bool = False,
    download_trades: bool = True,
    symbols: tuple[str, ...] = CRYPTO_CORE,
) -> DualDataset:
    """
    Crypto book on Binance USDT-M: real 1h klines + aggTrades + funding.
    Tech book is empty placeholders (cash) — for CRYPTO_C1 decoupling tests.
    """
    from datetime import timedelta

    from qtb.data.binance_futures import fetch_agg_trades_day, fetch_binance_klines_range, normalize_symbol

    crypto: dict[str, MarketData] = {}
    frames: list[pd.DataFrame] = []
    agg_rows: dict[str, int] = {}

    t0 = pd.Timestamp(start, tz="UTC").date()
    t1 = pd.Timestamp(end, tz="UTC").date()

    for sym in symbols:
        bn = normalize_symbol(sym)
        bars = fetch_binance_klines_range(bn, interval, start, end, cache_only=cache_only)
        if bars.empty:
            raise RuntimeError(f"Binance klines empty for {bn} {start} -> {end}")

        n_rows = 0
        if download_trades:
            d = t0
            while d <= t1:
                day_df = fetch_agg_trades_day(bn, d, cache_only=cache_only)
                n_rows += len(day_df)
                d += timedelta(days=1)
        agg_rows[sym] = n_rows

        funding = _fetch_binance_funding(bn, start, end, cache_only=cache_only)
        bars = _attach_binance_funding(bars, funding)
        meta = SeriesMeta(
            symbol=bn,
            market="binance_futures",
            interval=interval,
            source="binance_vision_klines+aggTrades",
            start=str(bars["timestamp"].iloc[0]),
            end=str(bars["timestamp"].iloc[-1]),
            bars=len(bars),
            nonzero_quote_bars=int((bars["quote_volume"].fillna(0) > 0).sum()),
            cache_path="",
            notes=[f"aggTrades_cached_rows={n_rows}", "trades_lazy=true"],
        )
        crypto[sym] = MarketData(
            sym, bn, interval, bars, funding, meta,
            trades=None, data_source="binance", trades_lazy=bool(download_trades),
        )
        frames.append(bars)

    aligned = align_on_timestamp(*frames)
    for j, sym in enumerate(symbols):
        md = crypto[sym]
        crypto[sym] = MarketData(
            sym, md.perp, interval, aligned[j], md.funding, md.meta, md.contract,
            None, "binance", md.trades_lazy,
        )

    # Minimal SOXL/SNXX placeholders so portfolio can run tech=cash
    empty = aligned[0].copy()
    empty["close"] = 1.0
    empty["open"] = 1.0
    empty["high"] = 1.0
    empty["low"] = 1.0
    empty["funding_rate"] = 0.0
    meta_e = SeriesMeta("SOXL", "cash_placeholder", interval, "placeholder", str(empty["timestamp"].iloc[0]), str(empty["timestamp"].iloc[-1]), len(empty), 0, "")
    tech = {
        "SOXL": MarketData("SOXL", "SOXL_USDT", interval, empty, pd.DataFrame(), meta_e, data_source="gate"),
        "SNXX": MarketData("SNXX", "SNXX_USDT", interval, empty.copy(), pd.DataFrame(), meta_e, data_source="gate"),
    }

    idx = pd.DatetimeIndex(aligned[0]["timestamp"])
    prov = {
        "source": "binance_futures",
        "interval": interval,
        "crypto_symbols": list(symbols),
        "overlap_start": str(idx[0]),
        "overlap_end": str(idx[-1]),
        "bars": len(idx),
        "aggTrades_cached_rows": agg_rows,
    }
    return DualDataset(
        interval=interval,
        tech=tech,
        crypto=crypto,
        aligned_index=idx,
        seed_coverage=[],
        overlap_start=idx[0],
        overlap_end=idx[-1],
        provenance=prov,
    )


def _fetch_binance_funding(symbol: str, start: str, end: str, cache_only: bool = False) -> pd.DataFrame:
    from qtb.data.binance_futures import normalize_symbol

    sym = normalize_symbol(symbol)
    path = CACHE_DIR / f"binance_futures_{sym}_funding.csv"
    cached = load_cache(path)
    if cached is not None and not cached.empty and not cache_only:
        return cached
    if cache_only:
        return cached if cached is not None else pd.DataFrame(columns=["timestamp", "funding_rate"])

    if httpx is None:
        return pd.DataFrame(columns=["timestamp", "funding_rate"])

    t0 = pd.Timestamp(start, tz="UTC")
    t1 = pd.Timestamp(end, tz="UTC")
    months = pd.period_range(t0.to_period("M"), t1.to_period("M"), freq="M")
    rows: list[dict] = []
    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        for per in months:
            url = (
                f"https://data.binance.vision/data/futures/um/monthly/fundingRate/"
                f"{sym}/{sym}-fundingRate-{per.strftime('%Y-%m')}.zip"
            )
            r = client.get(url)
            if r.status_code == 404:
                continue
            if r.status_code in (451, 403):
                break
            r.raise_for_status()
            zf = zipfile.ZipFile(io.BytesIO(r.content))
            text = zf.read(zf.namelist()[0]).decode("utf-8")
            part = pd.read_csv(io.StringIO(text))
            rows.extend(part.to_dict("records"))

    if not rows:
        return pd.DataFrame(columns=["timestamp", "funding_rate"])

    df = pd.DataFrame(rows)
    ts_col = "calc_time" if "calc_time" in df.columns else "fundingTime"
    rate_col = "last_funding_rate" if "last_funding_rate" in df.columns else "fundingRate"
    out = pd.DataFrame(
        {
            "timestamp": pd.to_datetime(df[ts_col], unit="ms", utc=True, errors="coerce"),
            "funding_rate": pd.to_numeric(df[rate_col], errors="coerce"),
        }
    ).dropna(subset=["timestamp"]).drop_duplicates("timestamp").sort_values("timestamp")
    out["timestamp"] = out["timestamp"].astype("datetime64[ns, UTC]")
    save_cache(out, path)
    return out


def _attach_binance_funding(bars: pd.DataFrame, funding: pd.DataFrame) -> pd.DataFrame:
    if funding.empty:
        out = bars.copy()
        out["funding_rate"] = 0.0
        return out
    m = pd.merge_asof(
        bars.sort_values("timestamp").assign(timestamp=lambda x: x["timestamp"].astype("datetime64[ns, UTC]")),
        funding.sort_values("timestamp").assign(timestamp=lambda x: x["timestamp"].astype("datetime64[ns, UTC]")),
        on="timestamp",
        direction="backward",
    )
    m["funding_rate"] = m["funding_rate"].fillna(0.0)
    return m.reset_index(drop=True)

