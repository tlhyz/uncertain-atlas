"""Drawdown triggers, reversal confirmation, EMA — no look-ahead."""

from __future__ import annotations

from typing import Literal

import numpy as np
import pandas as pd

from .universe import DRAWDOWN_SETS, AnchorMode, DrawdownSet, ReversalRule


def rolling_high(close: np.ndarray, n: int) -> np.ndarray:
    out = np.empty_like(close, dtype=float)
    for i in range(len(close)):
        lo = max(0, i - n + 1)
        out[i] = float(np.max(close[lo : i + 1]))
    return out


def drawdown_from_anchor(close: np.ndarray, anchor: np.ndarray) -> np.ndarray:
    """Negative when price below anchor."""
    return close / np.maximum(anchor, 1e-12) - 1.0


def compute_anchor(close: np.ndarray, mode: AnchorMode, rolling_n: int = 20 * 24) -> np.ndarray:
    if mode == "start":
        a0 = float(close[0])
        return np.full_like(close, a0, dtype=float)
    rh = rolling_high(close, rolling_n)
    # lag by 1 bar — anchor at i uses data through i-1 for rolling case
    out = np.empty_like(close, dtype=float)
    out[0] = float(close[0])
    out[1:] = rh[:-1]
    return out


def dd_tier(dd: float, thresholds: tuple[float, ...]) -> int:
    """Return tier 0..4 based on how many thresholds crossed."""
    tier = 0
    for t in thresholds:
        if dd <= t:
            tier += 1
    return tier


def ema(series: np.ndarray, span: int) -> np.ndarray:
    out = np.empty_like(series, dtype=float)
    alpha = 2.0 / (span + 1.0)
    out[0] = series[0]
    for i in range(1, len(series)):
        out[i] = alpha * series[i] + (1.0 - alpha) * out[i - 1]
    return out


def reversal_r1(close_4h: np.ndarray, i: int) -> bool:
    """4H EMA12 > EMA24 at bar i (uses only data <= i)."""
    if i < 24:
        return False
    e12 = ema(close_4h[: i + 1], 12)
    e24 = ema(close_4h[: i + 1], 24)
    return e12[-1] > e24[-1]


def _swing_lows(highs: np.ndarray, lows: np.ndarray, n: int = 3) -> list[tuple[int, float]]:
    pts: list[tuple[int, float]] = []
    for j in range(n, len(lows) - n):
        if lows[j] == min(lows[j - n : j + n + 1]):
            pts.append((j, float(lows[j])))
    return pts


def _swing_highs(highs: np.ndarray, lows: np.ndarray, n: int = 3) -> list[tuple[int, float]]:
    pts: list[tuple[int, float]] = []
    for j in range(n, len(highs) - n):
        if highs[j] == max(highs[j - n : j + n + 1]):
            pts.append((j, float(highs[j])))
    return pts


def reversal_r2(high: np.ndarray, low: np.ndarray, close: np.ndarray, i: int) -> bool:
    """4H higher-low + break prior swing high."""
    if i < 30:
        return False
    sl = _swing_lows(high[: i + 1], low[: i + 1])
    sh = _swing_highs(high[: i + 1], low[: i + 1])
    if len(sl) < 2 or len(sh) < 1:
        return False
    hl = sl[-1][1] > sl[-2][1]
    prev_high = sh[-2][1] if len(sh) >= 2 else sh[-1][1]
    break_hi = close[i] > prev_high
    return hl and break_hi


def reversal_r3(close: np.ndarray, i: int, bounce_pct: float = 0.15) -> bool:
    """Bounce from rolling low by bounce_pct."""
    if i < 10:
        return False
    window = close[max(0, i - 20 * 24) : i + 1]
    rlow = float(np.min(window))
    if rlow <= 0:
        return False
    return close[i] / rlow - 1.0 >= bounce_pct


def reversal_r4(
    soxl_close: np.ndarray,
    snxx_close: np.ndarray,
    i: int,
) -> bool:
    """Both SOXL and SNXX EMA12 > EMA24 on 4h resampled proxy (hourly EMA scaled)."""
    if i < 48:
        return False
    for s in (soxl_close, snxx_close):
        e12 = ema(s[: i + 1], 12 * 4)
        e24 = ema(s[: i + 1], 24 * 4)
        if e12[-1] <= e24[-1]:
            return False
    return True


def reversal_r5(
    close: np.ndarray,
    high: np.ndarray,
    low: np.ndarray,
    snxx_close: np.ndarray,
    i: int,
    bounce_pct: float = 0.15,
) -> bool:
    """Composite right-side: at least 2 of R1–R4 (no look-ahead — delegates to causal rules)."""
    votes = sum(
        [
            reversal_r1(close, i),
            reversal_r2(high, low, close, i),
            reversal_r3(close, i, bounce_pct),
            reversal_r4(close, snxx_close, i),
        ]
    )
    return votes >= 2


def check_reversal(
    rule: ReversalRule,
    i: int,
    close: np.ndarray,
    high: np.ndarray,
    low: np.ndarray,
    snxx_close: np.ndarray | None = None,
    bounce_pct: float = 0.15,
) -> bool:
    if rule == "R1":
        return reversal_r1(close, i)
    if rule == "R2":
        return reversal_r2(high, low, close, i)
    if rule == "R3":
        return reversal_r3(close, i, bounce_pct)
    if rule == "R4" and snxx_close is not None:
        return reversal_r4(close, snxx_close, i)
    if rule == "R5" and snxx_close is not None:
        return reversal_r5(close, high, low, snxx_close, i, bounce_pct)
    return False


def grid_mix_fractions(
    mix: str,
    phase: Literal["base", "reversal", "trend", "strong"],
) -> tuple[float, float]:
    """Return (grid_frac, directional_frac) of long exposure."""
    static = {
        "G100": (1.0, 0.0),
        "G75": (0.75, 0.25),
        "G50": (0.50, 0.50),
        "G25": (0.25, 0.75),
    }
    if mix in static:
        return static[mix]
    dynamic = {
        "base": (0.80, 0.20),
        "reversal": (0.60, 0.40),
        "trend": (0.40, 0.60),
        "strong": (0.20, 0.80),
    }
    return dynamic.get(phase, (0.50, 0.50))


def thresholds_for(set_id: DrawdownSet) -> tuple[float, ...]:
    return DRAWDOWN_SETS[set_id]
