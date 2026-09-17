"""Tests for OOS holdout report."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.oos_holdout import (
    build_oos_report,
    holdout_bar_split,
    holdout_year_split,
    oos_pass,
    render_oos_markdown,
    summarize_candidate,
)


def test_holdout_bar_split():
    tr, ho = holdout_bar_split(1000, holdout_fraction=0.25)
    assert tr == (0, 750)
    assert ho == (750, 1000)


def test_holdout_year_split():
    train, ho = holdout_year_split([2020, 2021, 2022, 2023, 2024], holdout_year=2024)
    assert train == [2020, 2021, 2022, 2023]
    assert ho == [2024]


def test_oos_pass():
    assert oos_pass({"total_return": 0.05}, benchmark_return=0.0)
    assert not oos_pass({"total_return": -0.5}, benchmark_return=-0.3)


def test_build_report_fail():
    rows = [
        summarize_candidate(
            "x",
            label="test",
            train={"total_return": 0.1},
            holdout={"total_return": -0.2, "calmar": -1},
            holdout_window="2024",
        )
    ]
    rep = build_oos_report(rows, holdout_policy="test")
    assert rep["verdict"] == "FAIL"
    assert rep["all_fail"]
    assert "FAIL" in render_oos_markdown(rep)
