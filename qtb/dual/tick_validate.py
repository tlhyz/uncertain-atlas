"""Validate aggTrades against kline bars — refuse backtest if mismatch too large."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from qtb.data.binance_futures import slice_trades_for_bar


@dataclass
class BarTickValidation:
    symbol: str
    bars_checked: int
    bars_with_trades: int
    max_high_err_pct: float
    max_low_err_pct: float
    max_vol_err_pct: float
    median_vol_err_pct: float
    passed: bool
    failures: list[str]

    def as_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "bars_checked": self.bars_checked,
            "bars_with_trades": self.bars_with_trades,
            "max_high_err_pct": round(self.max_high_err_pct, 6),
            "max_low_err_pct": round(self.max_low_err_pct, 6),
            "max_vol_err_pct": round(self.max_vol_err_pct, 6),
            "median_vol_err_pct": round(self.median_vol_err_pct, 6),
            "passed": self.passed,
            "failures": self.failures[:5],
        }


def validate_bars_vs_ticks(
    bars: pd.DataFrame,
    trades: pd.DataFrame,
    symbol: str,
    interval: str = "1h",
    *,
    max_high_low_err: float = 0.002,
    max_vol_err: float = 0.05,
    min_coverage: float = 0.95,
) -> BarTickValidation:
    """
    Cross-check each bar OHLCV vs aggTrades in the same window.
    Tolerance: 0.2% on high/low, 5% on quote volume (Vision klines use slightly different aggregation).
    """
    failures: list[str] = []
    high_errs: list[float] = []
    low_errs: list[float] = []
    vol_errs: list[float] = []
    with_trades = 0

    for _, bar in bars.iterrows():
        ts = pd.Timestamp(bar["timestamp"])
        sub = slice_trades_for_bar(trades, ts, interval) if not trades.empty else trades
        if sub.empty:
            continue
        with_trades += 1
        th = float(sub["price"].max())
        tl = float(sub["price"].min())
        tv = float(sub["quote_qty"].sum())
        bh = float(bar["high"])
        bl = float(bar["low"])
        bv = float(bar.get("quote_volume") or 0.0)

        if bh > 0:
            he = abs(th - bh) / bh
            high_errs.append(he)
            if he > max_high_low_err:
                failures.append(f"{ts} high tick={th} bar={bh} err={he:.4f}")

        if bl > 0:
            le = abs(tl - bl) / bl
            low_errs.append(le)
            if le > max_high_low_err:
                failures.append(f"{ts} low tick={tl} bar={bl} err={le:.4f}")

        if bv > 0:
            ve = abs(tv - bv) / bv
            vol_errs.append(ve)
            if ve > max_vol_err:
                failures.append(f"{ts} vol tick={tv:.0f} bar={bv:.0f} err={ve:.4f}")

    checked = len(bars)
    coverage = with_trades / max(checked, 1)
    passed = (
        coverage >= min_coverage
        and (not high_errs or max(high_errs) <= max_high_low_err * 2)
        and (not low_errs or max(low_errs) <= max_high_low_err * 2)
        and len(failures) <= max(3, int(checked * 0.01))
    )

    return BarTickValidation(
        symbol=symbol,
        bars_checked=checked,
        bars_with_trades=with_trades,
        max_high_err_pct=max(high_errs) if high_errs else 0.0,
        max_low_err_pct=max(low_errs) if low_errs else 0.0,
        max_vol_err_pct=max(vol_errs) if vol_errs else 0.0,
        median_vol_err_pct=float(np.median(vol_errs)) if vol_errs else 0.0,
        passed=passed,
        failures=failures,
    )


def validate_every_bar_has_ticks(
    bars: pd.DataFrame,
    perp: str,
    interval: str = "1h",
    *,
    cache_only: bool = True,
) -> BarTickValidation:
    """Require aggTrades for every bar — refuse backtest if any hour is missing ticks."""
    from qtb.data.binance_futures import fetch_agg_trades_day

    failures: list[str] = []
    with_trades = 0
    day_cache: dict = {}

    for _, bar in bars.iterrows():
        ts = pd.Timestamp(bar["timestamp"])
        d = ts.date()
        if d not in day_cache:
            day_cache[d] = fetch_agg_trades_day(perp, d, cache_only=cache_only)
        sub = slice_trades_for_bar(day_cache[d], ts, interval) if not day_cache[d].empty else day_cache[d]
        if sub.empty:
            failures.append(f"missing aggTrades bar {ts}")
            if len(failures) >= 10:
                break
        else:
            with_trades += 1

    checked = len(bars)
    coverage = with_trades / max(checked, 1)
    passed = coverage >= 0.999 and len(failures) == 0

    return BarTickValidation(
        symbol=perp,
        bars_checked=checked,
        bars_with_trades=with_trades,
        max_high_err_pct=0.0,
        max_low_err_pct=0.0,
        max_vol_err_pct=0.0,
        median_vol_err_pct=0.0,
        passed=passed,
        failures=failures,
    )


def validate_lazy_trades_coverage(
    bars: pd.DataFrame,
    symbol: str,
    perp: str,
    interval: str = "1h",
    *,
    cache_only: bool = True,
    sample_every: int | None = None,
) -> BarTickValidation:
    """Sample daily cached aggTrades vs klines without loading full range."""
    from qtb.data.binance_futures import fetch_agg_trades_day

    n = len(bars)
    if sample_every is None:
        sample_every = 1 if n <= 168 else 24
    min_cov = 0.95 if n >= 168 else max(0.5, min(1.0, 24 / max(n, 1)))

    parts: list[pd.DataFrame] = []
    days_seen: set = set()
    for i in range(0, n, sample_every):
        ts = pd.Timestamp(bars["timestamp"].iloc[i])
        d = ts.date()
        if d in days_seen:
            continue
        days_seen.add(d)
        parts.append(fetch_agg_trades_day(perp, d, cache_only=cache_only))
    trades = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    sub_bars = bars.iloc[::sample_every].reset_index(drop=True)
    v = validate_bars_vs_ticks(sub_bars, trades, symbol, interval, min_coverage=min_cov)
    return v
