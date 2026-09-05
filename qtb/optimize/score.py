"""Composite ranking score: return-stable, DD-controlled, hard-to-liquidate."""

from __future__ import annotations

from typing import Any

import numpy as np

DEFAULT_WEIGHTS: dict[str, float] = {
    "return": 1.0,
    "max_dd": 0.9,
    "sharpe": 0.6,
    "calmar": 0.5,
    "win_rate": 0.25,
    "profit_factor": 0.35,
    "max_float_loss": 0.5,
    "liq_risk": 2.0,
    "fee_ratio": 0.3,
    "stability": 0.4,
}


def _clip(x: float, lo: float, hi: float) -> float:
    return float(min(max(x, lo), hi))


def score_metrics(metrics: dict[str, Any], weights: dict[str, float] | None = None, stability: float = 0.0) -> float:
    """
    Higher is better. Components are squashed so a single outlier cannot dominate.
    Liquidation applies a hard penalty.
    """
    w = {**DEFAULT_WEIGHTS, **(weights or {})}
    if metrics.get("liquidated"):
        return -1_000.0 + float(metrics.get("net_pnl") or 0.0)

    ret = float(metrics.get("return_pct") or 0.0)
    dd = float(metrics.get("max_dd_pct") or 0.0)
    sharpe = float(metrics.get("sharpe") or 0.0)
    calmar = float(metrics.get("calmar") or 0.0)
    wr = float(metrics.get("win_rate") or 0.0)
    pf = float(metrics.get("profit_factor") or 0.0)
    float_loss = abs(float(metrics.get("max_float_loss") or 0.0))
    initial = float(metrics.get("initial_capital") or 1.0)
    float_pct = float_loss / max(initial, 1e-9)
    liq_risk = float(metrics.get("liq_risk") or 0.0)
    fee_ratio = float(metrics.get("fee_ratio") or 0.0)

    ret_s = np.tanh(ret * 3.0)
    dd_s = _clip(dd, 0.0, 1.5)
    sharpe_s = np.tanh(sharpe / 3.0)
    calmar_s = np.tanh(calmar / 5.0)
    pf_s = np.tanh(pf / 3.0)
    fee_s = _clip(fee_ratio, 0.0, 2.0)
    stab_s = _clip(stability, 0.0, 1.0)

    score = (
        w["return"] * ret_s
        + w["sharpe"] * sharpe_s
        + w["calmar"] * calmar_s
        + w["win_rate"] * wr
        + w["profit_factor"] * pf_s
        + w["stability"] * stab_s
        - w["max_dd"] * dd_s
        - w["max_float_loss"] * _clip(float_pct, 0.0, 2.0)
        - w["liq_risk"] * _clip(liq_risk, 0.0, 1.0)
        - w["fee_ratio"] * fee_s
    )
    return float(round(score, 6))


def composite_score(
    metrics: dict[str, Any],
    weights: dict[str, float] | None = None,
    stability: float = 0.0,
) -> float:
    return score_metrics(metrics, weights=weights, stability=stability)
