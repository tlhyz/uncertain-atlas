"""Simple grid search over strategy hyperparameters."""

from __future__ import annotations

from itertools import product
from typing import Any, Iterable

import pandas as pd

from fees import FeeConfig, VIP7_SPOT_70
from strategies.grid import GridParams, SpotGridSimulator
from strategies.martingale import MartingaleParams, SpotMartingaleSimulator


def _score(net_pnl: float, max_dd: float, total_fees: float) -> float:
    """Higher is better: reward PnL, penalize drawdown and fees."""
    return net_pnl - 0.35 * max_dd - 0.15 * total_fees


def optimize_grid(
    df: pd.DataFrame,
    fee_config: FeeConfig = VIP7_SPOT_70,
    spacing_pcts: Iterable[float] = (0.005, 0.008, 0.01, 0.012, 0.015),
    grid_counts: Iterable[int] = (12, 20, 24, 30),
    order_sizes: Iterable[float] = (40.0, 50.0, 80.0),
    initial_quote: float = 5000.0,
    top_k: int = 5,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for spacing, gcount, osize in product(spacing_pcts, grid_counts, order_sizes):
        params = GridParams(
            spacing_pct=spacing,
            grid_count=gcount,
            order_size_quote=osize,
            initial_quote=initial_quote,
            fee_as_maker=True,
        )
        r = SpotGridSimulator(params, fee_config).run(df)
        s = r.summary()
        s["score"] = round(_score(r.net_pnl, r.max_drawdown, r.total_fees), 4)
        s["params"] = {
            "spacing_pct": spacing,
            "grid_count": gcount,
            "order_size_quote": osize,
        }
        results.append(s)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


def optimize_martingale(
    df: pd.DataFrame,
    fee_config: FeeConfig = VIP7_SPOT_70,
    multipliers: Iterable[float] = (1.3, 1.4, 1.5, 1.8),
    add_drops: Iterable[float] = (0.012, 0.015, 0.018, 0.02, 0.025),
    take_profits: Iterable[float] = (0.01, 0.012, 0.015, 0.02),
    max_adds_list: Iterable[int] = (3, 4, 5),
    initial_quote: float = 5000.0,
    base_order_quote: float = 80.0,
    top_k: int = 5,
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for mult, drop, tp, max_adds in product(multipliers, add_drops, take_profits, max_adds_list):
        params = MartingaleParams(
            base_order_quote=base_order_quote,
            multiplier=mult,
            add_drop_pct=drop,
            take_profit_pct=tp,
            max_adds=max_adds,
            initial_quote=initial_quote,
            fee_as_maker=False,
        )
        r = SpotMartingaleSimulator(params, fee_config).run(df)
        s = r.summary()
        s["score"] = round(_score(r.net_pnl, r.max_drawdown, r.total_fees), 4)
        s["params"] = {
            "multiplier": mult,
            "add_drop_pct": drop,
            "take_profit_pct": tp,
            "max_adds": max_adds,
            "base_order_quote": base_order_quote,
        }
        results.append(s)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


def run_optimize(df: pd.DataFrame, fee_config: FeeConfig = VIP7_SPOT_70) -> dict[str, Any]:
    return {
        "grid_top": optimize_grid(df, fee_config),
        "martingale_top": optimize_martingale(df, fee_config),
    }
