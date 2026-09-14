"""Block bootstrap Monte Carlo — STEP 9 (P5-01)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


def daily_returns_from_equity(
    equity: np.ndarray,
    timestamps: list[Any] | None = None,
) -> np.ndarray:
    """Resample to daily last equity and return pct_change array."""
    eq = np.asarray(equity, dtype=float)
    if timestamps is not None and len(timestamps) == len(eq):
        s = pd.Series(eq, index=pd.to_datetime(timestamps, utc=True))
        daily = s.resample("1D").last().dropna()
        return daily.pct_change().dropna().to_numpy(float)
    if len(eq) < 2:
        return np.array([], dtype=float)
    return np.diff(eq) / np.maximum(eq[:-1], 1e-12)


def block_bootstrap_paths(
    daily: np.ndarray,
    *,
    block_days: int = 3,
    n_paths: int = 1000,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """
    Block bootstrap daily returns into n_paths synthetic return sequences (length n).

    Returns array shape (n_paths, n) of daily simple returns.
    """
    daily = np.asarray(daily, dtype=float)
    n = len(daily)
    if n == 0:
        return np.zeros((n_paths, 0))
    rng = rng or np.random.default_rng()
    blk = max(int(block_days), 1)
    out = np.zeros((n_paths, n))
    for p in range(n_paths):
        seq: list[float] = []
        while len(seq) < n:
            s = int(rng.integers(0, n))
            seq.extend(daily[s : s + blk].tolist())
        out[p] = np.asarray(seq[:n], dtype=float)
    return out


def _max_drawdown(equity: np.ndarray) -> float:
    peak = np.maximum.accumulate(equity)
    dd = (peak - equity) / np.maximum(peak, 1e-12)
    return float(dd.max()) if len(dd) else 0.0


def summarize_bootstrap_paths(
    return_paths: np.ndarray,
    *,
    initial: float = 10_000.0,
) -> dict[str, float]:
    """Summarize bootstrapped return paths into percentiles and probabilities."""
    n_paths = return_paths.shape[0]
    if n_paths == 0:
        return {"n_paths": 0}
    finals: list[float] = []
    dds: list[float] = []
    loss = dd10 = dd20 = dd30 = 0
    for p in range(n_paths):
        curve = initial * np.cumprod(1.0 + return_paths[p])
        final = float(curve[-1]) if len(curve) else initial
        finals.append(final)
        dd = _max_drawdown(curve)
        dds.append(dd)
        if final < initial:
            loss += 1
        if dd > 0.10:
            dd10 += 1
        if dd > 0.20:
            dd20 += 1
        if dd > 0.30:
            dd30 += 1
    arr = np.asarray(finals)
    return {
        "n_paths": float(n_paths),
        "p5_final": float(np.percentile(arr, 5)),
        "p25_final": float(np.percentile(arr, 25)),
        "p50_final": float(np.percentile(arr, 50)),
        "p75_final": float(np.percentile(arr, 75)),
        "p95_final": float(np.percentile(arr, 95)),
        "prob_loss": loss / n_paths,
        "prob_dd_10": dd10 / n_paths,
        "prob_dd_20": dd20 / n_paths,
        "prob_dd_30": dd30 / n_paths,
        "median_max_dd": float(np.median(dds)),
    }


def block_bootstrap_mc(
    equity_curve: np.ndarray,
    *,
    timestamps: list[Any] | None = None,
    block_days: tuple[int, ...] = (1, 3, 5),
    n_paths: int = 1000,
    initial: float | None = None,
    rng: np.random.Generator | None = None,
) -> dict[str, Any]:
    """
    Run block bootstrap MC on an equity curve.

    Returns per-block-day summaries plus input metadata.
    """
    eq = np.asarray(equity_curve, dtype=float)
    if len(eq) == 0:
        return {"status": "EMPTY", "n_paths": n_paths}
    init = float(initial if initial is not None else eq[0])
    daily = daily_returns_from_equity(eq, timestamps)
    if len(daily) < 2:
        return {"status": "INSUFFICIENT_DAILY", "n_paths": n_paths, "daily_bars": len(daily)}
    rng = rng or np.random.default_rng(42)
    out: dict[str, Any] = {
        "status": "OK",
        "n_paths": n_paths,
        "daily_obs": len(daily),
        "initial": init,
        "in_sample_final": float(eq[-1]),
        "in_sample_return": float(eq[-1] / init - 1.0),
        "blocks": {},
    }
    for blk in block_days:
        paths = block_bootstrap_paths(daily, block_days=blk, n_paths=n_paths, rng=rng)
        out["blocks"][f"{blk}d"] = summarize_bootstrap_paths(paths, initial=init)
    return out
