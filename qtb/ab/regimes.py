"""Price-path regime labels. Classification never looks at strategy PnL."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


REGIME_NAMES = (
    "uptrend",
    "downtrend",
    "v_reversal",
    "inverted_v",
    "high_vol_range",
    "low_vol_range",
    "double_bottom",
    "false_break",
    "crash_recovery",
    "persistent_trend",
)


@dataclass
class Window:
    start: pd.Timestamp
    end: pd.Timestamp
    i0: int
    i1: int
    horizon_days: int
    regime: str
    features: dict[str, float]


def _feat(close: np.ndarray, high: np.ndarray, low: np.ndarray, vol: np.ndarray) -> dict[str, float]:
    if len(close) < 5:
        return {"ret": 0.0, "rv": 0.0, "eff": 0.0, "max_dd": 0.0, "max_run": 0.0, "amp": 0.0}
    ret = float(close[-1] / close[0] - 1.0)
    r = np.diff(close) / np.maximum(close[:-1], 1e-12)
    rv = float(np.std(r)) if len(r) else 0.0
    path = float(np.sum(np.abs(r)))
    eff = abs(ret) / max(path, 1e-12)
    peak = np.maximum.accumulate(close)
    dd = float(((peak - close) / np.maximum(peak, 1e-12)).max())
    trough = np.minimum.accumulate(close)
    run = float(((close - trough) / np.maximum(trough, 1e-12)).max())
    amp = float((high.max() - low.min()) / max(close[0], 1e-12))
    mid = close[len(close) // 2]
    return {
        "ret": ret,
        "rv": rv,
        "eff": eff,
        "max_dd": dd,
        "max_run": run,
        "amp": amp,
        "mid_ret": float(mid / close[0] - 1.0),
        "second_half_ret": float(close[-1] / max(mid, 1e-12) - 1.0),
        "min_ret": float(close.min() / close[0] - 1.0),
        "max_ret": float(close.max() / close[0] - 1.0),
        "mean_quote": float(np.mean(vol)) if len(vol) else 0.0,
    }


def classify(f: dict[str, float]) -> str:
    ret = f["ret"]
    rv = f["rv"]
    eff = f["eff"]
    dd = f["max_dd"]
    mid = f.get("mid_ret", 0.0)
    sh = f.get("second_half_ret", 0.0)
    mn = f.get("min_ret", 0.0)
    mx = f.get("max_ret", 0.0)

    # V: drop then recover above start
    if mid <= -0.12 and ret >= 0.02:
        return "v_reversal"
    if mn <= -0.20 and ret >= -0.05 and sh > 0.10:
        return "crash_recovery"
    # inverted V
    if mid >= 0.12 and ret <= 0.02:
        return "inverted_v"
    # double bottom: deep dip, bounce, retest-ish, finish mixed
    if mn <= -0.12 and abs(ret) < 0.08 and sh > 0.04 and mid < -0.05:
        return "double_bottom"
    # false break: excursion then fade
    if mx >= 0.10 and ret <= 0.02 and sh < 0:
        return "false_break"
    if mn <= -0.10 and ret >= -0.02 and mid > -0.04:
        return "false_break"
    # range
    if abs(ret) <= 0.05:
        return "high_vol_range" if rv >= np.median([rv, 0.008]) and (f.get("amp", 0) >= 0.12 or rv >= 0.012) else "low_vol_range"
    # trends
    if ret >= 0.20 and eff >= 0.35:
        return "persistent_trend" if eff >= 0.55 else "uptrend"
    if ret <= -0.15 and eff >= 0.35:
        return "persistent_trend" if eff >= 0.55 else "downtrend"
    if ret > 0.05:
        return "uptrend"
    if ret < -0.05:
        return "downtrend"
    return "high_vol_range" if rv > 0.01 else "low_vol_range"


def slice_windows(
    bars: pd.DataFrame,
    horizons_days: list[int],
    interval: str,
    max_per_horizon: int = 8,
) -> list[Window]:
    """Non-PnL windows. Step = half horizon. Cap samples to avoid explosion."""
    step_bars = {
        "1m": 1440,
        "5m": 288,
        "15m": 96,
        "1h": 24,
        "4h": 6,
        "1d": 1,
    }.get(interval, 24)
    close = bars["close"].to_numpy(float)
    high = bars["high"].to_numpy(float)
    low = bars["low"].to_numpy(float)
    vol = bars["quote_volume"].to_numpy(float) if "quote_volume" in bars.columns else np.zeros(len(bars))
    ts = pd.to_datetime(bars["timestamp"], utc=True)
    out: list[Window] = []
    for hz in horizons_days:
        length = max(int(hz * step_bars), 8)
        if length >= len(bars):
            continue
        stride = max(length // 2, 1)
        starts = list(range(0, len(bars) - length + 1, stride))
        if len(starts) > max_per_horizon:
            # even sample across the history — not the best-PnL windows
            pick = np.linspace(0, len(starts) - 1, max_per_horizon, dtype=int)
            starts = [starts[i] for i in pick]
        for i0 in starts:
            i1 = i0 + length
            f = _feat(close[i0:i1], high[i0:i1], low[i0:i1], vol[i0:i1])
            out.append(
                Window(
                    start=pd.Timestamp(ts.iloc[i0]),
                    end=pd.Timestamp(ts.iloc[i1 - 1]),
                    i0=i0,
                    i1=i1,
                    horizon_days=hz,
                    regime=classify(f),
                    features=f,
                )
            )
    return out


def special_masks(und: pd.DataFrame, interval: str) -> dict[str, list[Window]]:
    """Find requested special tests from underlying path only."""
    days = 30 if interval in {"1h", "4h", "1d"} else 14
    wins = slice_windows(und, [days], interval, max_per_horizon=16)
    buckets: dict[str, list[Window]] = {
        "range_high_vol": [],
        "up_20": [],
        "up_30": [],
        "up_50": [],
        "crash_15": [],
        "crash_25": [],
        "crash_40": [],
        "v_reversal": [],
    }
    for w in wins:
        r = w.features.get("ret", 0.0)
        rv = w.features.get("rv", 0.0)
        if abs(r) <= 0.05 and rv >= 0.008:
            buckets["range_high_vol"].append(w)
        if r >= 0.50:
            buckets["up_50"].append(w)
        elif r >= 0.30:
            buckets["up_30"].append(w)
        elif r >= 0.20:
            buckets["up_20"].append(w)
        if r <= -0.40:
            buckets["crash_40"].append(w)
        elif r <= -0.25:
            buckets["crash_25"].append(w)
        elif r <= -0.15:
            buckets["crash_15"].append(w)
        if w.regime == "v_reversal":
            buckets["v_reversal"].append(w)
    return buckets
