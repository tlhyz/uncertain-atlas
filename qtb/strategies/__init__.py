"""Strategy registry: classic grid, trend grid, dual grid, (dual) martingale."""

from __future__ import annotations

from typing import Any

from .base import Strategy
from .classic_grid import ClassicGridStrategy
from .dual_grid import DualGridStrategy
from .martingale import DualMartingaleStrategy, MartingaleStrategy
from .trend_grid import TrendGridStrategy

STRATEGIES: dict[str, type[Strategy]] = {
    "classic_grid": ClassicGridStrategy,
    "trend_grid": TrendGridStrategy,
    "dual_grid": DualGridStrategy,
    "martingale": MartingaleStrategy,
    "dual_martingale": DualMartingaleStrategy,
    # aliases
    "grid": ClassicGridStrategy,
    "aggressive_dual": DualMartingaleStrategy,
    "aggressive-dual": DualMartingaleStrategy,
}


def build_strategy(cfg: dict[str, Any]) -> Strategy:
    name = str(cfg.get("name") or "dual_martingale").strip().lower()
    cls = STRATEGIES.get(name)
    if cls is None:
        raise ValueError(f"unknown strategy {name!r}; choose {sorted(STRATEGIES)}")
    return cls(cfg)


__all__ = [
    "Strategy",
    "ClassicGridStrategy",
    "TrendGridStrategy",
    "DualGridStrategy",
    "MartingaleStrategy",
    "DualMartingaleStrategy",
    "STRATEGIES",
    "build_strategy",
]
