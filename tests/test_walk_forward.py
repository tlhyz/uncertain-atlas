"""Tests for walk-forward split utilities."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.walk_forward import (
    bar_index_splits,
    calendar_year_folds,
    slice_index_range,
    walk_forward_report,
)


def test_bar_index_splits_default():
    s = bar_index_splits(1000)
    assert s["train"] == (0, 500)
    assert s["validation"] == (500, 750)
    assert s["test"] == (750, 1000)


def test_bar_index_splits_short():
    assert bar_index_splits(100) == {}


def test_calendar_year_folds():
    idx = pd.date_range("2019-09-01", "2024-12-31", freq="h", tz="UTC")
    folds = calendar_year_folds(idx, min_train_years=2)
    years = [f["test_year"] for f in folds]
    assert 2021 in years
    assert years[0] == 2021
    assert all(f["train_bars"] > 0 and f["test_bars"] > 0 for f in folds)


def test_walk_forward_report_synthetic():
    idx = pd.date_range("2019-01-01", "2023-12-31", freq="h", tz="UTC")
    folds = calendar_year_folds(idx, min_train_years=2)

    def eval_fn(i0: int, i1: int) -> dict:
        span = i1 - i0
        return {"total_return": -0.01 * span / 1000, "calmar": -1.0, "max_dd_pct": 0.1, "liquidation_count": 0}

    rep = walk_forward_report(folds, eval_fn)
    assert rep["n_folds"] == len(folds)
    assert rep["all_test_negative"]


def test_slice_index_range():
    idx = pd.date_range("2020-01-01", periods=48, freq="h", tz="UTC")
    start, end = slice_index_range(idx, 0, 24)
    assert start == "2020-01-01"
    assert end == "2020-01-01"
