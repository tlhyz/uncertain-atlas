"""Real Binance USDT-M perpetual data (Vision klines + aggTrades)."""

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
    SeriesMeta,
    _meta_from_df,
    align_on_timestamp,
    first_liquid_ts,
)
from qtb.data.candles import CACHE_DIR, _INTERVAL_SEC, load_cache, save_cache

from .universe import BINANCE_SYMBOL, CRYPTO_CORE, SEED_WINDOWS, SeedWindow, TECH_SYMBOLS

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
    data_source: Literal["gate", "binance"] = "binance"
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


def _fetch_binance_funding(symbol: str, start: str, end: str, cache_only: bool = False) -> pd.DataFrame:
    from qtb.data.binance_futures import normalize_symbol

    sym = normalize_symbol(symbol)
    path = CACHE_DIR / f"binance_futures_{sym}_funding.csv"

    def _load_fund() -> pd.DataFrame | None:
        if not path.exists():
            return None
        raw = pd.read_csv(path)
        if "ts_ms" in raw.columns:
            raw["timestamp"] = pd.to_datetime(raw["ts_ms"], unit="ms", utc=True)
        elif "timestamp" in raw.columns:
            raw["timestamp"] = pd.to_datetime(raw["timestamp"], utc=True, errors="coerce")
        else:
            return None
        if raw["timestamp"].isna().sum() > len(raw) * 0.05:
            return None
        return raw[["timestamp", "funding_rate"]].dropna()

    cached = _load_fund()
    if cached is not None and not cached.empty:
        return cached
    if cache_only:
        return pd.DataFrame(columns=["timestamp", "funding_rate"])

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
    save_df = out.copy()
    save_df["ts_ms"] = (save_df["timestamp"].astype("int64") // 1_000_000).astype(int)
    path.parent.mkdir(parents=True, exist_ok=True)
    save_df[["ts_ms", "funding_rate"]].to_csv(path, index=False)
    return out[["timestamp", "funding_rate"]]


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


def load_binance_market(
    symbol: str,
    interval: str = "1h",
    *,
    start: str,
    end: str,
    cache_only: bool = False,
    download_trades: bool = False,
) -> MarketData:
    """Load one symbol from Binance Vision: klines + optional lazy aggTrades."""
    from datetime import timedelta

    from qtb.data.binance_futures import fetch_agg_trades_day, fetch_binance_klines_range, normalize_symbol

    bn = normalize_symbol(BINANCE_SYMBOL.get(symbol, symbol))
    bars = fetch_binance_klines_range(bn, interval, start, end, cache_only=cache_only)
    if bars.empty:
        raise RuntimeError(f"Binance klines empty for {bn} {start} -> {end}")

    n_rows = 0
    trades_lazy = False
    t0 = pd.Timestamp(start, tz="UTC").date()
    t1 = pd.Timestamp(end, tz="UTC").date()
    if download_trades:
        d = t0
        while d <= t1:
            day_df = fetch_agg_trades_day(bn, d, cache_only=cache_only)
            n_rows += len(day_df)
            d += timedelta(days=1)
        trades_lazy = n_rows > 0
    elif cache_only:
        from qtb.data.binance_futures import trades_day_cache_path

        d = t0
        while d <= t1:
            if trades_day_cache_path(bn, d).exists():
                trades_lazy = True
                break
            d += timedelta(days=1)

    funding = _fetch_binance_funding(bn, start, end, cache_only=cache_only)
    bars = _attach_binance_funding(bars, funding)
    notes = [f"aggTrades_cached_rows={n_rows}", "trades_lazy=true"] if trades_lazy else []
    meta = SeriesMeta(
        symbol=bn,
        market="binance_futures",
        interval=interval,
        source="binance_vision_klines+aggTrades" if trades_lazy else "binance_vision_klines",
        start=str(bars["timestamp"].iloc[0]),
        end=str(bars["timestamp"].iloc[-1]),
        bars=len(bars),
        nonzero_quote_bars=int((bars["quote_volume"].fillna(0) > 0).sum()),
        cache_path="",
        notes=notes,
    )
    return MarketData(
        symbol=symbol,
        perp=bn,
        interval=interval,
        bars=bars,
        funding=funding,
        meta=meta,
        trades=None,
        data_source="binance",
        trades_lazy=trades_lazy,
    )


def _default_binance_range() -> tuple[str, str]:
    """Tech overlap: SNXX launch (~2026-07-09) through latest cached day."""
    start = "2026-07-09"
    end = pd.Timestamp.now(tz="UTC").strftime("%Y-%m-%d")
    return start, end


def check_seed_window(cov: SeedWindow, data: MarketData) -> WindowCoverage:
    start = pd.Timestamp(cov.start, tz="UTC")
    end = pd.Timestamp(cov.end, tz="UTC") + pd.Timedelta(hours=23)
    df = data.bars
    mask = (df["timestamp"] >= start) & (df["timestamp"] <= end)
    sub = df.loc[mask]
    notes: list[str] = []
    if sub.empty:
        notes.append("no Binance bars in seed range")
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


def load_dual_dataset(
    interval: str = "1h",
    cache_only: bool = False,
    *,
    start: str | None = None,
    end: str | None = None,
    download_trades: bool = True,
    tech_tick_only: bool = True,
    crypto_download_trades: bool | None = None,
) -> DualDataset:
    """
    Binance-only dual dataset: SOXL/SNXX tech with aggTrades; crypto klines only.
    Default window = SNXX launch overlap through today.
    """
    t0, t1 = start or _default_binance_range()[0], end or _default_binance_range()[1]

    tech: dict[str, MarketData] = {}
    for sym in TECH_SYMBOLS:
        tech[sym] = load_binance_market(
            sym, interval, start=t0, end=t1,
            cache_only=cache_only, download_trades=download_trades,
        )

    crypto_dl = (not tech_tick_only) if crypto_download_trades is None else bool(crypto_download_trades)

    crypto: dict[str, MarketData] = {}
    for sym in CRYPTO_CORE:
        crypto[sym] = load_binance_market(
            sym, interval, start=t0, end=t1,
            cache_only=cache_only,
            download_trades=crypto_dl,
        )

    frames = [tech["SOXL"].bars, tech["SNXX"].bars] + [crypto[s].bars for s in CRYPTO_CORE]
    aligned = align_on_timestamp(*frames)
    tech["SOXL"] = MarketData(
        "SOXL", tech["SOXL"].perp, interval,
        aligned[0], tech["SOXL"].funding, tech["SOXL"].meta, tech["SOXL"].contract,
        None, "binance", tech["SOXL"].trades_lazy,
    )
    tech["SNXX"] = MarketData(
        "SNXX", tech["SNXX"].perp, interval,
        aligned[1], tech["SNXX"].funding, tech["SNXX"].meta, tech["SNXX"].contract,
        None, "binance", tech["SNXX"].trades_lazy,
    )
    for j, sym in enumerate(CRYPTO_CORE):
        md = crypto[sym]
        crypto[sym] = MarketData(
            sym, md.perp, interval, aligned[2 + j], md.funding, md.meta, md.contract,
            None, "binance", md.trades_lazy,
        )

    idx = pd.DatetimeIndex(aligned[0]["timestamp"])
    overlap_start = max(first_liquid_ts(tech["SOXL"].bars), first_liquid_ts(tech["SNXX"].bars))
    for s in CRYPTO_CORE:
        overlap_start = max(overlap_start, first_liquid_ts(crypto[s].bars))
    overlap_end = idx[-1]

    seed_cov: list[WindowCoverage] = []
    for sw in SEED_WINDOWS:
        md = tech.get(sw.symbol)
        if md:
            seed_cov.append(check_seed_window(sw, md))

    tick_validation: dict[str, dict] = {}
    tick_coverage: dict[str, dict] = {}
    if download_trades:
        from .tick_validate import validate_every_bar_has_ticks, validate_lazy_trades_coverage

        for sym in TECH_SYMBOLS:
            md = tech[sym]
            if md.trades_lazy:
                v = validate_lazy_trades_coverage(md.bars, sym, md.perp, interval, cache_only=True)
                tick_validation[sym] = v.as_dict()
                if not v.passed:
                    raise RuntimeError(
                        f"aggTrades vs kline validation FAIL for {sym}: "
                        f"coverage={v.bars_with_trades}/{v.bars_checked} failures={v.failures[:2]}"
                    )
                cov = validate_every_bar_has_ticks(md.bars, md.perp, interval, cache_only=True)
                tick_coverage[sym] = cov.as_dict()
                if not cov.passed:
                    raise RuntimeError(
                        f"Missing aggTrades for {sym}: {cov.bars_with_trades}/{cov.bars_checked} bars — "
                        f"refuse bar approximation. First: {cov.failures[:3]}"
                    )

    prov = {
        "source": "binance_futures",
        "interval": interval,
        "tech_symbols": list(TECH_SYMBOLS),
        "crypto_symbols": list(CRYPTO_CORE),
        "window_start": t0,
        "window_end": t1,
        "overlap_start": str(overlap_start),
        "overlap_end": str(overlap_end),
        "bars": len(idx),
        "seed_windows": [c.as_dict() for c in seed_cov],
        "tick_validation": tick_validation,
        "tick_coverage": tick_coverage,
        "execution": "tick_precise_aggTrades_tech_every_bar",
    }
    return DualDataset(
        interval=interval,
        tech=tech,
        crypto=crypto,
        aligned_index=idx,
        seed_coverage=seed_cov,
        overlap_start=overlap_start,
        overlap_end=overlap_end,
        provenance=prov,
    )


def slice_window(data: DualDataset, start: str, end: str) -> DualDataset:
    t0 = pd.Timestamp(start, tz="UTC")
    t1 = pd.Timestamp(end, tz="UTC") + pd.Timedelta(hours=23)

    def _slice_md(md: MarketData) -> MarketData:
        m = (md.bars["timestamp"] >= t0) & (md.bars["timestamp"] <= t1)
        sub = md.bars.loc[m].reset_index(drop=True)
        return MarketData(
            md.symbol, md.perp, md.interval, sub, md.funding, md.meta, md.contract,
            md.trades, md.data_source, md.trades_lazy,
        )

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
    skip_tick_validation: bool = False,
) -> DualDataset:
    """
    Crypto book on Binance USDT-M: real 1h klines + aggTrades + funding.
    Tech book is empty placeholders (cash) — for CRYPTO_C1 decoupling tests.
    """
    crypto: dict[str, MarketData] = {}
    frames: list[pd.DataFrame] = []
    agg_rows: dict[str, int] = {}

    for sym in symbols:
        md = load_binance_market(
            sym, interval, start=start, end=end,
            cache_only=cache_only, download_trades=download_trades,
        )
        agg_rows[sym] = int((md.meta.notes or [""])[0].split("=")[-1]) if md.meta.notes else 0
        crypto[sym] = md
        frames.append(md.bars)

    aligned = align_on_timestamp(*frames)
    for j, sym in enumerate(symbols):
        md = crypto[sym]
        crypto[sym] = MarketData(
            sym, md.perp, interval, aligned[j], md.funding, md.meta, md.contract,
            None, "binance", md.trades_lazy,
        )

    empty = aligned[0].copy()
    empty["close"] = 1.0
    empty["open"] = 1.0
    empty["high"] = 1.0
    empty["low"] = 1.0
    empty["funding_rate"] = 0.0
    meta_e = SeriesMeta("SOXL", "cash_placeholder", interval, "placeholder", str(empty["timestamp"].iloc[0]), str(empty["timestamp"].iloc[-1]), len(empty), 0, "")
    tech = {
        "SOXL": MarketData("SOXL", "SOXLUSDT", interval, empty, pd.DataFrame(), meta_e, data_source="binance"),
        "SNXX": MarketData("SNXX", "SNXXUSDT", interval, empty.copy(), pd.DataFrame(), meta_e, data_source="binance"),
    }

    idx = pd.DatetimeIndex(aligned[0]["timestamp"])
    tick_validation: dict[str, dict] = {}
    from .tick_validate import validate_lazy_trades_coverage

    for sym in symbols:
        md = crypto[sym]
        if md.trades_lazy and not skip_tick_validation:
            v = validate_lazy_trades_coverage(md.bars, sym, md.perp, interval, cache_only=True)
            tick_validation[sym] = v.as_dict()
            if not v.passed:
                raise RuntimeError(
                    f"aggTrades vs kline validation FAIL for {sym}: "
                    f"coverage={v.bars_with_trades}/{v.bars_checked} failures={v.failures[:2]}"
                )
        elif md.trades_lazy and skip_tick_validation:
            tick_validation[sym] = {"skipped": True, "reason": "P1 manifests validated"}

    prov = {
        "source": "binance_futures",
        "interval": interval,
        "crypto_symbols": list(symbols),
        "overlap_start": str(idx[0]),
        "overlap_end": str(idx[-1]),
        "bars": len(idx),
        "aggTrades_cached_rows": agg_rows,
        "tick_validation": tick_validation,
        "execution": "tick_precise_aggTrades_only",
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
