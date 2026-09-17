"""Geometric / arithmetic grids. Native ATR and underlying-equivalent mappings.

Beta used for ETF step mapping is rolling and lagged — never future beta.
ETF mapped step is clipped to [0.5%, 4%].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd

GridKind = Literal["geometric", "arithmetic"]
GridMode = Literal["native_atr", "underlying_equiv", "static_pct"]
SizeMode = Literal["fixed_usdt", "fixed_qty", "vol_adj"]


@dataclass
class GridSpec:
    kind: GridKind
    mode: GridMode
    mid: float
    levels: np.ndarray
    spacing_pct: float
    range_pct: float
    atr: float
    beta: float
    lower: float
    upper: float


def true_range(high: np.ndarray, low: np.ndarray, close: np.ndarray) -> np.ndarray:
    prev = np.roll(close, 1)
    prev[0] = close[0]
    return np.maximum(high - low, np.maximum(np.abs(high - prev), np.abs(low - prev)))


def rolling_atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 24) -> np.ndarray:
    tr = true_range(high, low, close)
    out = np.empty_like(tr, dtype=float)
    csum = np.cumsum(tr)
    for i in range(len(tr)):
        lo = max(0, i - n + 1)
        span = i - lo + 1
        out[i] = (csum[i] - (csum[lo - 1] if lo else 0.0)) / span
    return out


def realized_vol(close: np.ndarray, n: int = 24) -> np.ndarray:
    ret = np.zeros_like(close, dtype=float)
    ret[1:] = np.diff(close) / np.maximum(close[:-1], 1e-12)
    out = np.zeros_like(close, dtype=float)
    for i in range(len(close)):
        lo = max(1, i - n + 1)
        w = ret[lo : i + 1]
        if len(w) >= 2:
            out[i] = float(np.std(w, ddof=1))
        elif len(w) == 1:
            out[i] = abs(float(w[0]))
    return out


def rolling_beta(etf_close: np.ndarray, und_close: np.ndarray, n: int = 48) -> np.ndarray:
    """Lagged OLS beta of ETF returns on underlying returns. Index i uses data < i+1 but we
    shift by 1 when applying so the live step never sees the current bar return."""
    ye = np.zeros_like(etf_close)
    xu = np.zeros_like(und_close)
    ye[1:] = np.diff(etf_close) / np.maximum(etf_close[:-1], 1e-12)
    xu[1:] = np.diff(und_close) / np.maximum(und_close[:-1], 1e-12)
    out = np.full(len(etf_close), 3.0, dtype=float)
    for i in range(len(etf_close)):
        lo = max(1, i - n + 1)
        y = ye[lo : i + 1]
        x = xu[lo : i + 1]
        if len(x) < 8:
            continue
        vx = float(np.var(x))
        if vx < 1e-16:
            continue
        out[i] = float(np.cov(x, y, ddof=1)[0, 1] / vx)
    # clip insane estimates; do not use future
    return np.clip(out, 0.2, 8.0)


def build_levels(
    mid: float,
    spacing_pct: float,
    range_pct: float,
    kind: GridKind = "geometric",
) -> np.ndarray:
    if mid <= 0 or spacing_pct <= 0 or range_pct <= 0:
        raise ValueError("mid/spacing/range must be positive")
    if kind == "geometric":
        lo = mid * (1.0 - range_pct)
        hi = mid * (1.0 + range_pct)
        if lo <= 0:
            lo = mid * 0.05
        levels = [mid]
        px = mid
        while px * (1.0 - spacing_pct) >= lo:
            px *= 1.0 - spacing_pct
            levels.append(px)
        px = mid
        while px * (1.0 + spacing_pct) <= hi:
            px *= 1.0 + spacing_pct
            levels.append(px)
        return np.array(sorted(set(round(x, 12) for x in levels)), dtype=float)
    lo = mid * (1.0 - range_pct)
    hi = mid * (1.0 + range_pct)
    step = mid * spacing_pct
    n = max(2, int(round((hi - lo) / max(step, 1e-12))))
    return np.linspace(lo, hi, n + 1)


def clip_etf_step(step: float, lo: float = 0.005, hi: float = 0.04) -> float:
    return float(min(max(step, lo), hi))


def native_spec(mid: float, atr: float, atr_step: float, atr_range: float, kind: GridKind) -> GridSpec:
    spacing = (atr_step * atr) / mid
    rng = (atr_range * atr) / mid
    spacing = float(min(max(spacing, 0.001), 0.08))
    rng = float(min(max(rng, spacing * 2.0), 0.80))
    levels = build_levels(mid, spacing, rng, kind)
    return GridSpec(kind, "native_atr", mid, levels, spacing, rng, atr, 1.0, float(levels[0]), float(levels[-1]))


def static_spec(mid: float, spacing_pct: float, range_pct: float, kind: GridKind) -> GridSpec:
    levels = build_levels(mid, spacing_pct, range_pct, kind)
    return GridSpec(kind, "static_pct", mid, levels, spacing_pct, range_pct, 0.0, 1.0, float(levels[0]), float(levels[-1]))


def underlying_equiv_spec(
    mid_etf: float,
    und_step: float,
    und_range: float,
    beta: float,
    kind: GridKind,
) -> GridSpec:
    """Map an underlying percent step onto the ETF using *past* beta only."""
    step = clip_etf_step(und_step * max(beta, 0.2))
    rng = float(min(max(und_range * max(beta, 0.2), step * 3.0), 0.80))
    levels = build_levels(mid_etf, step, rng, kind)
    return GridSpec(kind, "underlying_equiv", mid_etf, levels, step, rng, 0.0, float(beta), float(levels[0]), float(levels[-1]))


def lower_zone_mult(level_price: float, lower: float, upper: float, boost: float) -> float:
    """Increase size near the bottom of the range. Cap boost at 1.5 — no martingale."""
    if boost <= 1.0 or upper <= lower:
        return 1.0
    boost = min(float(boost), 1.5)
    pos = (level_price - lower) / (upper - lower)
    if pos <= 0.30:
        return boost
    if pos >= 0.50:
        return 1.0
    # linear fade 0.30 → 0.50
    t = (pos - 0.30) / 0.20
    return boost * (1.0 - t) + 1.0 * t


def grid_quote_size(
    baseline: float,
    level_price: float,
    spec: GridSpec,
    size_mode: SizeMode,
    atr_now: float,
    atr_ref: float,
    lower_boost: float,
) -> float:
    size = baseline
    if size_mode == "vol_adj" and atr_now > 0 and atr_ref > 0:
        size = baseline * float(np.clip(atr_ref / atr_now, 0.5, 1.5))
    size *= lower_zone_mult(level_price, spec.lower, spec.upper, lower_boost)
    return max(size, 0.0)
