"""Tests for P6-04 Tech vs Cash→Long OOS module."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.tech_cash_long_oos import TechCashLongOosReport, render_tech_cash_long_markdown


def test_render_markdown_fail():
    rep = TechCashLongOosReport(
        holdout_window="2026-08-26→2026-09-11",
        holdout_bars=386,
        tech_fsm_return=-0.75,
        b4_cash_long_return=-0.25,
        delta_pp=-50.0,
        tech_beats_b4=False,
        in_sample_tech_return=-0.587,
        in_sample_b4_return=-0.252,
        in_sample_delta_pp=-33.5,
        execution="test",
        verdict="FAIL",
        notes=["Tech FAIL"],
    )
    md = render_tech_cash_long_markdown(rep)
    assert "FAIL" in md
    assert "-50.00pp" in md
