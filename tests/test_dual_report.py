"""Dual report must use measured payload, not static templates."""

from __future__ import annotations

from pathlib import Path

from qtb.dual.report import _build_q_answers, write_report


def _mock_payload() -> dict:
    return {
        "provenance": {
            "overlap_start": "2026-09-05",
            "overlap_end": "2026-09-11",
            "bars": 168,
            "interval": "1h",
            "source": "binance_futures",
            "execution": "tick_precise_aggTrades_tech_every_bar",
            "tech_symbols": ["SOXL", "SNXX"],
            "crypto_symbols": ["BTC", "ETH", "SOL"],
            "seed_windows": [{"window": {"id": "FAIL_F1"}, "status": "STRUCTURAL_SEED_ONLY", "gate_bars": 0, "notes": []}],
        },
        "benchmarks": [
            {"benchmark": "B2_buy_hold", "total_return": 0.01, "max_dd_pct": 0.1, "sharpe": 1, "calmar": 1, "liquidation_count": 0},
            {"benchmark": "B3_long_grid_only", "total_return": -0.25, "max_dd_pct": 0.08, "sharpe": 1, "calmar": -3, "liquidation_count": 0},
            {"benchmark": "B4_directional_long_only", "total_return": -0.25, "max_dd_pct": 0.08, "sharpe": 1, "calmar": -3, "liquidation_count": 0},
            {"benchmark": "B10_independent_books", "total_return": -0.78, "max_dd_pct": 0.11, "sharpe": 1, "calmar": -7, "liquidation_count": 0},
        ],
        "sweep": [
            {"fill": "base", "calmar": -5.0, "total_return": -0.7, "tech": {"drawdown_set": "A", "reversal": "R1", "grid_mix": "dynamic", "soxl_weight": 0.75}},
            {"fill": "base", "calmar": -4.0, "total_return": -0.65, "tech": {"drawdown_set": "B", "reversal": "R2", "grid_mix": "G50", "soxl_weight": 0.70}},
        ],
        "short_structures": [
            {"short_structure": "directional", "calmar": -8.0, "total_return": -0.78},
            {"short_structure": "grid", "calmar": -9.0, "total_return": -0.80},
        ],
        "leverage_rank": [
            {"leverage": 1.25, "calmar": -6.0},
            {"leverage": 1.5, "calmar": -5.5},
            {"leverage": 2.0, "calmar": -7.0},
        ],
        "grid_atr_rank": [
            {"grid_atr_step": 0.30, "grid_atr_range": 5.0, "calmar": -6.0},
            {"grid_atr_step": 0.40, "grid_atr_range": 5.0, "calmar": -5.0},
            {"grid_atr_step": 0.50, "grid_atr_range": 3.0, "calmar": -7.0},
        ],
        "independent_vs_unified": {"delta_return": 0.0, "delta_dd": 0.0},
        "stress_3x": {"total_return": -0.95, "liquidation_count": 0},
        "seed_windows": [{"seed_id": "FAIL_F1", "status": "STRUCTURAL_SEED_ONLY"}],
        "plans": {},
    }


def test_q_answers_reference_measured_leverage():
    lines = _build_q_answers(_mock_payload())
    q8 = next(l for l in lines if l.startswith("**Q8"))
    assert "1.25x" in q8 or "1.5x" in q8
    assert "0.40 ATR near Pareto center" not in "\n".join(lines)


def test_q3_fail_when_grid_beats_dual():
    lines = _build_q_answers(_mock_payload())
    q3 = next(l for l in lines if l.startswith("**Q3"))
    assert "FAIL" in q3


def test_write_report_from_mock_payload(tmp_path: Path):
    out = write_report(_mock_payload(), tmp_path)
    text = out.read_text()
    assert "from measured payload" in text
    assert "Q8 Leverage" in text
    assert "0.40 ATR near Pareto center" not in text
    assert "STRUCTURAL_SEED_ONLY" in text
