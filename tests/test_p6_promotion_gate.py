"""Tests for P6 promotion gate checklist."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.live_promotion import evaluate_promotion, render_promotion_markdown


def test_btc_promotion_fails_and_demotes():
    rep = evaluate_promotion("BTC", current_confidence="MEDIUM")
    assert rep.promotion_verdict == "FAIL"
    assert rep.recommended_confidence == "LOW"
    assert rep.n_blocking_failures >= 4
    md = render_promotion_markdown(rep)
    assert "FAIL" in md
    assert "oos_holdout" in rep.as_dict()["gates"][0]["gate_id"] or any(
        g.gate_id == "oos_holdout" for g in rep.gates
    )


def test_eth_promotion_fails():
    rep = evaluate_promotion("ETH")
    assert rep.promotion_verdict == "FAIL"
    assert rep.recommended_confidence == "LOW"
