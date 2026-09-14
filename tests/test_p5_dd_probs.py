"""Tests for P5-05 DD probability extraction."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.run_p5_dd_probs import dd_probability_table, render_dd_markdown


def test_dd_probability_table():
    mc = {
        "blocks": {
            "3d": {
                "prob_dd_10": 0.5,
                "prob_dd_20": 0.2,
                "prob_dd_30": 0.05,
                "prob_loss": 0.15,
                "median_max_dd": 0.12,
                "p50_final": 9000,
            }
        }
    }
    table = dd_probability_table(mc)
    assert table["3d"]["prob_dd_20"] == 0.2
    md = render_dd_markdown({"config": "test", "bars": 100, "monte_carlo": {"daily_obs": 6, "n_paths": 1000}, "dd_probabilities": table})
    assert "P(DD>20%)" in md
