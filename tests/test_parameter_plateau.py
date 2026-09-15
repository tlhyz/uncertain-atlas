"""Tests for parameter plateau detector."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.parameter_plateau import analyze_sweep, detect_plateau, is_plateau, overfit_flag, robust_pick


def _rows(steps: list[float], metric_vals: list[float]) -> list[dict]:
    return [
        {"grid_atr_step": s, "calmar": m, "total_return": -0.87 + 0.001 * i}
        for i, (s, m) in enumerate(zip(steps, metric_vals))
    ]


def test_overfit_god_param():
    flag = overfit_flag([-0.2, 0.10, -0.3])
    assert flag["flag"] == "OVERFIT"


def test_overfit_plateau_small_spread():
    flag = overfit_flag([-0.87, -0.863, -0.875])
    assert flag["flag"] == "plateau"
    assert flag["spread"] < 0.15


def test_overfit_sensitive():
    flag = overfit_flag([-0.2, -0.5, -0.9])
    assert flag["flag"] == "sensitive"


def test_is_plateau_legacy():
    rows = _rows([0.3, 0.4, 0.5], [-16.6, -17.2, -15.3])
    assert is_plateau(rows, "grid_atr_step", "calmar", tol=0.15)


@pytest.mark.skipif(
    not (ROOT / "outputs/experiments/crypto_btc_grid_atr_step/crypto_results.json").exists(),
    reason="BTC ATR sweep artifact not present on this VM",
)
def test_detect_inert_plateau_btc_sweep():
    path = ROOT / "outputs/experiments/crypto_btc_grid_atr_step/crypto_results.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data["grid_rank"]
    det_ret = detect_plateau(rows, "grid_atr_step", "total_return", reference_param=0.4)
    assert det_ret["n"] == 4
    assert det_ret["flag"] == "PLATEAU_INERT"
    assert det_ret["actionable"] is False
    assert det_ret["return_spread"] < 0.01
    det_cal = detect_plateau(rows, "grid_atr_step", "calmar", reference_param=0.4)
    assert det_cal["flag"] == "SENSITIVE"
    assert det_cal["reference_rank"] == 4
    assert det_cal["reference_is_best"] is False


def test_robust_pick_median_rank():
    rows = _rows([0.3, 0.4, 0.5, 0.6], [-16.6, -17.2, -15.3, -17.17])
    assert robust_pick(rows, "grid_atr_step", "calmar") == 0.3


def test_analyze_sweep_multi_metric():
    rows = _rows([0.3, 0.4, 0.5], [-16.6, -17.2, -15.3])
    out = analyze_sweep(rows, "grid_atr_step", reference_param=0.4)
    assert "calmar" in out and "total_return" in out
