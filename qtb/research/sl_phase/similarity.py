"""Path-only similarity. Never uses strategy PnL to pick windows."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


def hourly_close_from_ticks(tape: pd.DataFrame) -> pd.Series:
    if tape is None or tape.empty:
        return pd.Series(dtype=float)
    work = tape.copy()
    work["t"] = pd.to_datetime(work["timestamp"], utc=True)
    s = work.set_index("t")["price"].resample("1h").last().dropna()
    return s


def _z_norm(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        return x
    x = np.log(np.maximum(x, 1e-12))
    x = x - x[0]
    sd = float(np.std(x))
    if sd < 1e-12:
        return x
    return (x - float(np.mean(x))) / sd


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 5 or len(b) < 5:
        return float("nan")
    n = min(len(a), len(b))
    a = _z_norm(a[:n])
    b = _z_norm(b[:n])
    if np.std(a) < 1e-12 or np.std(b) < 1e-12:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def dtw_distance(a: np.ndarray, b: np.ndarray) -> float:
    """Classic DTW on z-normalized log paths. O(n*m), n capped."""
    a = _z_norm(a)
    b = _z_norm(b)
    if a.size == 0 or b.size == 0:
        return float("inf")
    n, m = len(a), len(b)
    inf = 1e18
    dp = np.full((n + 1, m + 1), inf)
    dp[0, 0] = 0.0
    for i in range(1, n + 1):
        j0 = max(1, i - 12)
        j1 = min(m, i + 12)
        ai = a[i - 1]
        for j in range(j0, j1 + 1):
            cost = abs(ai - b[j - 1])
            dp[i, j] = cost + min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1])
    return float(dp[n, m] / (n + m))


def window_features(px: np.ndarray) -> dict[str, float]:
    px = np.asarray(px, dtype=float)
    px = px[px > 0]
    if len(px) < 5:
        return {}
    lr = np.diff(np.log(px))
    eq = px / px[0]
    peak = np.maximum.accumulate(eq)
    dd = eq / peak - 1.0
    rebound = float(eq[-1] / eq.min() - 1.0)
    t = np.arange(len(px), dtype=float)
    slope = float(np.polyfit(t, np.log(px), 1)[0])
    atr = float(np.mean(np.abs(lr)))
    return {
        "log_return": float(np.log(px[-1] / px[0])),
        "realized_vol": float(np.std(lr) * np.sqrt(24 * 365)) if len(lr) else 0.0,
        "max_drawdown": float(dd.min()),
        "max_rebound": rebound,
        "atr": atr,
        "trend_slope": slope,
    }


@dataclass
class Match:
    start: str
    end: str
    pearson: float
    dtw: float
    features: dict[str, float]
    score: float


def template_mask(feat: dict[str, float], kind: str) -> bool:
    """Shape filters only. No PnL."""
    if not feat:
        return False
    if kind == "A":  # drop then rise
        return feat["max_drawdown"] <= -0.08 and feat["max_rebound"] >= 0.08 and feat["log_return"] > -0.05
    if kind == "B":  # rise then fall
        return feat["log_return"] < 0.0 and feat.get("trend_slope", 0) < 0
    return True


def top_similar(
    series: pd.Series,
    *,
    lengths: tuple[int, ...] = (20, 30, 45, 60, 90),
    kind: str = "A",
    top_n: int = 10,
    step: int = 12,
) -> list[Match]:
    """Scan hourly series. `lengths` are calendar-ish days → 24h bars."""
    if series is None or series.empty:
        return []
    px_all = series.to_numpy(dtype=float)
    idx = series.index
    cands: list[Match] = []
    templates = []
    # build a synthetic unit template for scoring (normalized V or inverted V)
    for Ldays in lengths:
        n = max(24, Ldays * 24)
        if n >= len(px_all):
            continue
        for start in range(0, len(px_all) - n, step):
            sl = px_all[start : start + n]
            feat = window_features(sl)
            if not template_mask(feat, kind):
                continue
            # compare to a geometric V / inverted-V of same length (path shape, not PnL)
            t = np.linspace(0, 1, n)
            if kind == "A":
                tmpl = np.concatenate([1 - 0.25 * t[: n // 2], 0.75 + 0.35 * t[: n - n // 2]])
                if len(tmpl) != n:
                    tmpl = np.resize(tmpl, n)
            else:
                tmpl = np.concatenate([1 + 0.25 * t[: n // 2], 1.25 - 0.40 * t[: n - n // 2]])
                if len(tmpl) != n:
                    tmpl = np.resize(tmpl, n)
            # downsample to ≤90 points for DTW
            stride = max(1, n // 90)
            a = sl[::stride]
            b = tmpl[::stride]
            pr = pearson(a, b)
            dt = dtw_distance(a, b)
            if not np.isfinite(pr):
                continue
            score = float(pr) - 0.15 * dt
            cands.append(
                Match(
                    start=str(idx[start]),
                    end=str(idx[start + n - 1]),
                    pearson=float(pr),
                    dtw=float(dt),
                    features=feat,
                    score=score,
                )
            )
    cands.sort(key=lambda m: m.score, reverse=True)
    # de-overlap
    kept: list[Match] = []
    for m in cands:
        if any(m.start <= k.end and m.end >= k.start for k in kept):
            continue
        kept.append(m)
        if len(kept) >= top_n:
            break
    return kept
