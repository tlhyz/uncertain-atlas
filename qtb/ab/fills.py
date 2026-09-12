"""Shared fill model for ETF spot and perpetual grids.

Optimistic is implemented for diagnostics only.
Primary conclusions use Base and Conservative.
A bar that jumps across many grid levels never auto-fills all of them.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

FillMode = Literal["optimistic", "base", "conservative"]


@dataclass(frozen=True)
class FillConfig:
    mode: FillMode = "base"
    participation: float = 0.20
    extra_ticks: int = 0
    extra_slip_bps: float = 0.0
    tick_size: float = 0.0

    @staticmethod
    def preset(mode: FillMode, tick_size: float = 0.0) -> FillConfig:
        if mode == "optimistic":
            return FillConfig(mode=mode, participation=1.0, extra_ticks=0, extra_slip_bps=0.0, tick_size=tick_size)
        if mode == "base":
            return FillConfig(mode=mode, participation=0.20, extra_ticks=0, extra_slip_bps=0.0, tick_size=tick_size)
        return FillConfig(mode=mode, participation=0.05, extra_ticks=2, extra_slip_bps=3.0, tick_size=tick_size)


@dataclass
class PendingFill:
    side: Literal["buy", "sell"]
    price: float
    level_idx: int
    qty: float | None = None
    notional: float | None = None
    reduce_only: bool = False
    reason: str = ""


def infer_tick(price: float, fallback: float = 0.0) -> float:
    if fallback > 0:
        return fallback
    if price >= 1000:
        return 0.1
    if price >= 100:
        return 0.01
    if price >= 1:
        return 0.0001
    if price >= 0.1:
        return 0.00001
    return 1e-6


def bar_segments(o: float, h: float, l: float, c: float) -> list[tuple[float, float]]:
    """Adverse-first OHLC path. Up-bar: O→L→H→C. Down-bar: O→H→L→C."""
    if c >= o:
        return [(o, l), (l, h), (h, c)]
    return [(o, h), (h, l), (l, c)]


def _crosses_buy(p0: float, p1: float, limit: float, tick_need: float) -> bool:
    """Buy limit fills only when price trades down through (or to) the limit."""
    trigger = limit - tick_need
    if p1 >= p0:
        return False
    return p0 > trigger and p1 <= trigger


def _crosses_sell(p0: float, p1: float, limit: float, tick_need: float) -> bool:
    trigger = limit + tick_need
    if p1 <= p0:
        return False
    return p0 < trigger and p1 >= trigger


def apply_adverse_slip(price: float, side: str, extra_slip_bps: float) -> float:
    slip = abs(extra_slip_bps) / 10_000.0
    if side == "buy":
        return price * (1.0 + slip)
    return price * (1.0 - slip)


def resolve_bar_fills(
    opens: list[PendingFill],
    o: float,
    h: float,
    l: float,
    c: float,
    quote_volume: float,
    cfg: FillConfig,
) -> list[PendingFill]:
    """
    Walk the real bar path. Consume a participation-capped quote budget.
    Never fill every crossed level just because the wick touched them.
    """
    if not opens:
        return []
    if cfg.mode == "optimistic":
        # Touch = fill. Still sequential so we do not explode inventory in one shot
        # without a budget — optimistic uses full quote_volume (or unlimited if 0).
        budget = quote_volume if quote_volume > 0 else 1e18
    else:
        budget = max(float(quote_volume), 0.0) * cfg.participation
        if budget <= 0:
            return []

    tick = cfg.tick_size if cfg.tick_size > 0 else infer_tick((h + l) / 2.0)
    tick_need = tick * float(cfg.extra_ticks)

    buys = [f for f in opens if f.side == "buy"]
    sells = [f for f in opens if f.side == "sell"]
    buys.sort(key=lambda f: -f.price)  # hit nearest (higher) first on the way down
    sells.sort(key=lambda f: f.price)  # hit nearest (lower) first on the way up

    filled: list[PendingFill] = []
    buy_i = 0
    sell_i = 0

    for p0, p1 in bar_segments(o, h, l, c):
        if budget <= 1e-9:
            break
        if p1 < p0:
            while buy_i < len(buys) and budget > 1e-9:
                f = buys[buy_i]
                if not _crosses_buy(p0, p1, f.price, tick_need):
                    if f.price > p0:
                        buy_i += 1
                        continue
                    break
                px = apply_adverse_slip(f.price, "buy", cfg.extra_slip_bps)
                notional = f.notional if f.notional and f.notional > 0 else (f.qty or 0.0) * px
                if notional <= 0:
                    buy_i += 1
                    continue
                take = min(notional, budget)
                if take < notional * 0.25 and cfg.mode != "optimistic":
                    # refuse tiny residual crumbs that would distort lot accounting
                    budget = 0.0
                    break
                qty = (f.qty or 0.0) * (take / notional) if f.qty else None
                filled.append(
                    PendingFill(
                        side="buy",
                        price=px,
                        level_idx=f.level_idx,
                        qty=qty,
                        notional=take,
                        reduce_only=f.reduce_only,
                        reason=f.reason,
                    )
                )
                budget -= take
                buy_i += 1
        elif p1 > p0:
            while sell_i < len(sells) and budget > 1e-9:
                f = sells[sell_i]
                if not _crosses_sell(p0, p1, f.price, tick_need):
                    if f.price < p0:
                        sell_i += 1
                        continue
                    break
                px = apply_adverse_slip(f.price, "sell", cfg.extra_slip_bps)
                notional = f.notional if f.notional and f.notional > 0 else (f.qty or 0.0) * px
                if notional <= 0:
                    sell_i += 1
                    continue
                take = min(notional, budget)
                if take < notional * 0.25 and cfg.mode != "optimistic":
                    budget = 0.0
                    break
                qty = (f.qty or 0.0) * (take / notional) if f.qty else None
                filled.append(
                    PendingFill(
                        side="sell",
                        price=px,
                        level_idx=f.level_idx,
                        qty=qty,
                        notional=take,
                        reduce_only=f.reduce_only,
                        reason=f.reason,
                    )
                )
                budget -= take
                sell_i += 1
    return filled
