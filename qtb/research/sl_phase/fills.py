"""Limit-grid fill models on a deals print. No order-book queue claim."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

FillModel = Literal["optimistic", "base", "conservative"]


@dataclass(frozen=True)
class FillPolicy:
    model: FillModel
    # Fraction of this print's quantity the strategy may take.
    max_vol_frac: float
    # Extra ticks the print must trade through (sell: above limit; buy: below).
    through_ticks: int
    # Adverse ticks added to fill price after a match.
    slip_ticks: int

    @staticmethod
    def of(model: FillModel) -> FillPolicy:
        if model == "optimistic":
            return FillPolicy("optimistic", max_vol_frac=1.0, through_ticks=0, slip_ticks=0)
        if model == "base":
            return FillPolicy("base", max_vol_frac=0.20, through_ticks=0, slip_ticks=0)
        if model == "conservative":
            return FillPolicy("conservative", max_vol_frac=0.05, through_ticks=1, slip_ticks=1)
        raise ValueError(model)


def infer_tick(price: float) -> float:
    """Infer a 1-tick size from the print. Not a real exchange tick table."""
    if price >= 100:
        return 0.01
    if price >= 1:
        return 0.0001
    if price >= 0.01:
        return 0.000001
    return 1e-8


def buy_matches(print_px: float, limit: float, tick: float, policy: FillPolicy) -> bool:
    """Buy limit: optimistic touch; base requires print < limit; conservative through N ticks."""
    if policy.model == "optimistic":
        return print_px <= limit
    need = limit - policy.through_ticks * tick
    return print_px < need if policy.through_ticks == 0 else print_px <= need - 1e-15


def sell_matches(print_px: float, limit: float, tick: float, policy: FillPolicy) -> bool:
    if policy.model == "optimistic":
        return print_px >= limit
    need = limit + policy.through_ticks * tick
    return print_px > need if policy.through_ticks == 0 else print_px >= need + 1e-15


def fill_price(side: str, limit: float, tick: float, policy: FillPolicy) -> float:
    if policy.slip_ticks <= 0:
        return limit
    if side == "buy":
        return limit + policy.slip_ticks * tick
    return max(tick, limit - policy.slip_ticks * tick)


def take_qty(print_qty: float, want_qty: float, policy: FillPolicy) -> float:
    cap = max(0.0, float(print_qty) * policy.max_vol_frac)
    if policy.model == "optimistic":
        return min(want_qty, want_qty)  # unlimited vs this print; still sequential across levels
    return min(want_qty, cap)
