"""Walk-forward split utilities — STEP 9 (P5-03)."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np
import pandas as pd


def bar_index_splits(
    n: int,
    *,
    train_ratio: float = 0.50,
    val_ratio: float = 0.25,
) -> dict[str, tuple[int, int]]:
    """
    Fixed train / validation / test bar ranges (half-open [i0, i1)).

    Default mirrors ``qtb.ab.experiments.walk_forward``: 50% / 25% / 25%.
    """
    if n < 200:
        return {}
    i_tr = int(n * train_ratio)
    i_va = int(n * (train_ratio + val_ratio))
    return {
        "train": (0, i_tr),
        "validation": (i_tr, i_va),
        "test": (i_va, n),
    }


def calendar_year_folds(
    index: pd.DatetimeIndex,
    *,
    min_train_years: int = 2,
) -> list[dict[str, Any]]:
    """
    Expanding calendar-year walk-forward folds.

    Each fold: train on years < test_year, test on test_year bars.
    Requires at least *min_train_years* before first test year.
    """
    if index.empty:
        return []
    years = sorted(set(int(ts.year) for ts in index))
    if len(years) < min_train_years + 1:
        return []
    folds: list[dict[str, Any]] = []
    for test_year in years[min_train_years:]:
        train_mask = index.year < test_year
        test_mask = index.year == test_year
        if not train_mask.any() or not test_mask.any():
            continue
        train_idx = np.flatnonzero(train_mask)
        test_idx = np.flatnonzero(test_mask)
        folds.append(
            {
                "fold": len(folds),
                "test_year": test_year,
                "train": (int(train_idx[0]), int(train_idx[-1]) + 1),
                "test": (int(test_idx[0]), int(test_idx[-1]) + 1),
                "train_bars": int(train_mask.sum()),
                "test_bars": int(test_mask.sum()),
                "train_start": str(index[train_idx[0]]),
                "train_end": str(index[train_idx[-1]]),
                "test_start": str(index[test_idx[0]]),
                "test_end": str(index[test_idx[-1]]),
            }
        )
    return folds


def slice_index_range(index: pd.DatetimeIndex, i0: int, i1: int) -> tuple[str, str]:
    """Return (start_date, end_date) strings for ``slice_window`` from bar indices."""
    start = pd.Timestamp(index[i0]).strftime("%Y-%m-%d")
    end = pd.Timestamp(index[i1 - 1]).strftime("%Y-%m-%d")
    return start, end


def summarize_fold_metrics(metrics: dict[str, Any]) -> dict[str, Any]:
    """Extract key fields from portfolio summary dict."""
    return {
        "total_return": float(metrics.get("total_return", 0)),
        "calmar": float(metrics.get("calmar", 0)),
        "max_dd_pct": float(metrics.get("max_dd_pct", 0)),
        "liquidation_count": int(metrics.get("liquidation_count", 0)),
        "final_equity": float(metrics.get("final_equity", 0)),
    }


def walk_forward_report(
    folds: list[dict[str, Any]],
    eval_fn: Callable[[int, int], dict[str, Any]],
) -> dict[str, Any]:
    """
    Run *eval_fn(i0, i1)* on each fold train/test split and aggregate.
    """
    rows: list[dict[str, Any]] = []
    for fold in folds:
        i0_tr, i1_tr = fold["train"]
        i0_te, i1_te = fold["test"]
        train_m = summarize_fold_metrics(eval_fn(i0_tr, i1_tr))
        test_m = summarize_fold_metrics(eval_fn(i0_te, i1_te))
        rows.append(
            {
                **{k: fold[k] for k in ("fold", "test_year", "train_bars", "test_bars", "train_start", "test_start")},
                "train_return": train_m["total_return"],
                "test_return": test_m["total_return"],
                "train_calmar": train_m["calmar"],
                "test_calmar": test_m["calmar"],
                "test_max_dd_pct": test_m["max_dd_pct"],
                "test_liquidated": test_m["liquidation_count"] > 0,
                "oos_gap_return": train_m["total_return"] - test_m["total_return"],
            }
        )
    test_returns = [r["test_return"] for r in rows]
    return {
        "n_folds": len(rows),
        "folds": rows,
        "mean_test_return": float(np.mean(test_returns)) if test_returns else None,
        "median_test_return": float(np.median(test_returns)) if test_returns else None,
        "positive_oos_folds": sum(1 for r in test_returns if r > 0),
        "all_test_negative": bool(test_returns) and all(r < 0 for r in test_returns),
    }
