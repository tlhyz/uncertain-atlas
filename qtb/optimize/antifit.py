"""Anti-overfit diagnostics: train/test, walk-forward, regimes, Monte Carlo, stability."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np
import pandas as pd

from .score import composite_score


def split_train_test(df: pd.DataFrame, train_ratio: float = 0.70) -> tuple[pd.DataFrame, pd.DataFrame]:
    n = len(df)
    cut = max(10, int(n * train_ratio))
    cut = min(cut, n - 5) if n > 15 else n // 2
    return df.iloc[:cut].reset_index(drop=True), df.iloc[cut:].reset_index(drop=True)


def walk_forward_slices(df: pd.DataFrame, folds: int = 3) -> list[tuple[pd.DataFrame, pd.DataFrame]]:
    """Expanding train, next fold test."""
    n = len(df)
    folds = max(int(folds), 2)
    fold_len = max(n // (folds + 1), 8)
    out: list[tuple[pd.DataFrame, pd.DataFrame]] = []
    for i in range(folds):
        train_end = fold_len * (i + 1)
        test_end = min(n, train_end + fold_len)
        if test_end - train_end < 5 or train_end < 8:
            continue
        out.append(
            (
                df.iloc[:train_end].reset_index(drop=True),
                df.iloc[train_end:test_end].reset_index(drop=True),
            )
        )
    return out


def regime_slices(df: pd.DataFrame, splits: int = 3) -> dict[str, pd.DataFrame]:
    """
    Multi-regime segments:
    - time thirds (early / mid / late)
    - volatility terciles via rolling close std
    """
    splits = max(int(splits), 2)
    n = len(df)
    chunk = max(n // splits, 5)
    out: dict[str, pd.DataFrame] = {}
    labels = ["early", "mid", "late"] + [f"seg_{i}" for i in range(3, splits)]
    for i in range(splits):
        a, b = i * chunk, n if i == splits - 1 else (i + 1) * chunk
        out[labels[i]] = df.iloc[a:b].reset_index(drop=True)

    close = df["close"].astype(float)
    vol = close.pct_change().rolling(24, min_periods=8).std().fillna(0.0)
    try:
        terc = pd.qcut(vol.rank(method="first"), 3, labels=["low_vol", "mid_vol", "high_vol"])
        for name in ("low_vol", "mid_vol", "high_vol"):
            part = df.loc[terc == name]
            if len(part) >= 8:
                out[name] = part.reset_index(drop=True)
    except Exception:
        pass
    return out


def monte_carlo_from_cycles(
    cycle_pnls: list[float],
    initial: float,
    paths: int = 40,
    seed: int = 7,
) -> dict[str, float]:
    """Bootstrap cycle PnLs; report terminal equity / max DD distribution."""
    rng = np.random.default_rng(seed)
    pnls = np.asarray(cycle_pnls, dtype=float)
    if len(pnls) < 2:
        return {
            "paths": 0,
            "p05_equity": float(initial),
            "p50_equity": float(initial),
            "p95_equity": float(initial),
            "mean_max_dd": 0.0,
            "ruin_rate": 0.0,
        }
    terminals = []
    max_dds = []
    ruins = 0
    for _ in range(int(paths)):
        sample = rng.choice(pnls, size=len(pnls), replace=True)
        eq = initial + np.cumsum(sample)
        eq = np.concatenate([[initial], eq])
        terminals.append(float(eq[-1]))
        peak = np.maximum.accumulate(eq)
        dd = float((peak - eq).max())
        max_dds.append(dd)
        if float(eq.min()) <= 0:
            ruins += 1
    arr = np.asarray(terminals)
    return {
        "paths": int(paths),
        "p05_equity": float(np.quantile(arr, 0.05)),
        "p50_equity": float(np.quantile(arr, 0.50)),
        "p95_equity": float(np.quantile(arr, 0.95)),
        "mean_max_dd": float(np.mean(max_dds)),
        "ruin_rate": ruins / max(paths, 1),
    }


def neighbor_stability(
    run_fn: Callable[[dict[str, Any]], float],
    center: dict[str, Any],
    keys: tuple[str, ...] = ("multiplier", "add_drop_pct", "take_profit_pct"),
) -> float:
    """
    Score smoothness around a parameter point. Returns 1 / (1 + cv) in [0, 1].
    """
    scores = [run_fn(center)]
    deltas = {
        "multiplier": 0.1,
        "add_drop_pct": 0.002,
        "take_profit_pct": 0.002,
        "max_adds": 10,
        "spacing_pct": 0.002,
        "grid_count": 4,
    }
    for key in keys:
        if key not in center or center[key] is None:
            continue
        step = deltas.get(key)
        if step is None:
            continue
        for sign in (-1.0, 1.0):
            nb = dict(center)
            val = float(center[key]) + sign * step
            if key in {"max_adds", "grid_count"}:
                val = max(2, int(round(val)))
            else:
                val = max(1e-6, val)
            nb[key] = val
            try:
                scores.append(run_fn(nb))
            except Exception:
                scores.append(-10.0)
    arr = np.asarray(scores, dtype=float)
    mu = float(np.mean(arr))
    sd = float(np.std(arr))
    if abs(mu) < 1e-9:
        return 0.0
    cv = abs(sd / mu)
    return float(1.0 / (1.0 + cv))


def anti_overfit_report(
    df: pd.DataFrame,
    run_metrics: Callable[[pd.DataFrame], dict[str, Any]],
    cfg_optimize: dict[str, Any],
    cycle_pnls: list[float],
    initial: float,
    weights: dict[str, float] | None = None,
) -> dict[str, Any]:
    train_ratio = float(cfg_optimize.get("train_ratio") or 0.70)
    folds = int(cfg_optimize.get("walk_forward_folds") or 3)
    mc_paths = int(cfg_optimize.get("monte_carlo_paths") or 40)
    regimes = int(cfg_optimize.get("regime_splits") or 3)

    train, test = split_train_test(df, train_ratio)
    tr = run_metrics(train)
    te = run_metrics(test)
    train_score = composite_score(tr, weights)
    test_score = composite_score(te, weights)
    gap = train_score - test_score

    wf = []
    for i, (tr_df, te_df) in enumerate(walk_forward_slices(df, folds)):
        a = run_metrics(tr_df)
        b = run_metrics(te_df)
        wf.append(
            {
                "fold": i,
                "train_score": composite_score(a, weights),
                "test_score": composite_score(b, weights),
                "train_return": a.get("return_pct"),
                "test_return": b.get("return_pct"),
                "test_max_dd_pct": b.get("max_dd_pct"),
                "test_liquidated": b.get("liquidated"),
            }
        )

    regime_scores = {}
    for name, part in regime_slices(df, regimes).items():
        m = run_metrics(part)
        regime_scores[name] = {
            "score": composite_score(m, weights),
            "return_pct": m.get("return_pct"),
            "max_dd_pct": m.get("max_dd_pct"),
            "liquidated": m.get("liquidated"),
            "bars": len(part),
        }

    mc = monte_carlo_from_cycles(cycle_pnls, initial, paths=mc_paths)

    return {
        "train_test": {
            "train_ratio": train_ratio,
            "train_bars": len(train),
            "test_bars": len(test),
            "train_score": train_score,
            "test_score": test_score,
            "score_gap": round(gap, 6),
            "train_metrics": tr,
            "test_metrics": te,
            "overfit_flag": bool(gap > 0.35 and test_score < 0),
        },
        "walk_forward": wf,
        "regimes": regime_scores,
        "monte_carlo": mc,
    }
