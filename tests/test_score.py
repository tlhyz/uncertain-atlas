"""Composite score ranking behavior."""

from __future__ import annotations

from qtb.optimize.score import composite_score


def _base(**kw):
    m = {
        "return_pct": 0.10,
        "max_dd_pct": 0.08,
        "sharpe": 1.2,
        "calmar": 1.5,
        "win_rate": 0.7,
        "profit_factor": 1.8,
        "max_float_loss": -50.0,
        "initial_capital": 1000.0,
        "liq_risk": 0.1,
        "fee_ratio": 0.05,
        "liquidated": False,
        "net_pnl": 100.0,
    }
    m.update(kw)
    return m


def test_higher_return_better():
    a = composite_score(_base(return_pct=0.20))
    b = composite_score(_base(return_pct=0.02))
    assert a > b


def test_drawdown_and_liq_penalized():
    good = composite_score(_base(max_dd_pct=0.05, liq_risk=0.05))
    bad_dd = composite_score(_base(max_dd_pct=0.60, liq_risk=0.05))
    bad_liq = composite_score(_base(max_dd_pct=0.05, liq_risk=0.90))
    assert good > bad_dd
    assert good > bad_liq


def test_liquidation_hard_penalty():
    alive = composite_score(_base())
    dead = composite_score(_base(liquidated=True, net_pnl=-800.0))
    assert dead < -500
    assert dead < alive


def test_stability_bonus():
    a = composite_score(_base(), stability=0.9)
    b = composite_score(_base(), stability=0.0)
    assert a > b


def test_weights_applied():
    m = _base(return_pct=0.5, max_dd_pct=0.4)
    hi_ret = composite_score(m, weights={"return": 5.0, "max_dd": 0.1})
    hi_dd = composite_score(m, weights={"return": 0.1, "max_dd": 5.0})
    assert hi_ret > hi_dd
