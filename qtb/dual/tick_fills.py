"""Tick-level fill simulation from Binance aggTrades — no look-ahead."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from qtb.ab.fills import FillConfig, PendingFill, apply_adverse_slip, infer_tick


@dataclass
class TickFill:
    side: str
    price: float
    qty: float
    notional: float
    level_idx: int
    reason: str
    trade_ts: pd.Timestamp


def _crosses_buy(last_px: float, px: float, limit: float, tick_need: float) -> bool:
    trigger = limit - tick_need
    return last_px > trigger and px <= trigger


def _crosses_sell(last_px: float, px: float, limit: float, tick_need: float) -> bool:
    trigger = limit + tick_need
    return last_px < trigger and px >= trigger


def resolve_tick_fills(
    pending: list[PendingFill],
    bar_trades: pd.DataFrame,
    cfg: FillConfig,
) -> list[TickFill]:
    """
    Walk real aggTrades in time order. At most one new grid open per level per bar
    unless participation budget allows more. Never auto-fill all skipped levels.
    """
    if not pending or bar_trades.empty:
        return []

    tick = cfg.tick_size or infer_tick(float(bar_trades["price"].iloc[0]))
    tick_need = tick * max(cfg.extra_ticks, 0)
    budget = float(bar_trades["quote_qty"].sum()) * cfg.participation
    spent = 0.0
    fills: list[TickFill] = []
    filled_levels: set[int] = set()
    last_px = float(bar_trades["price"].iloc[0])

    for _, tr in bar_trades.iterrows():
        px = float(tr["price"])
        if cfg.mode == "conservative":
            px = apply_adverse_slip(px, "buy", cfg.extra_slip_bps)  # conservative slip on both sides handled per side below

        for pf in pending:
            if pf.level_idx in filled_levels:
                continue
            hit = False
            side = pf.side
            limit = pf.price
            if side == "buy":
                if cfg.mode == "conservative":
                    exec_px = apply_adverse_slip(limit, "buy", cfg.extra_slip_bps)
                else:
                    exec_px = limit
                hit = _crosses_buy(last_px, px, limit, tick_need)
            else:
                if cfg.mode == "conservative":
                    exec_px = apply_adverse_slip(limit, "sell", cfg.extra_slip_bps)
                else:
                    exec_px = limit
                hit = _crosses_sell(last_px, px, limit, tick_need)

            if not hit:
                continue

            if pf.qty is not None:
                notional = pf.qty * exec_px
            else:
                notional = pf.notional or 0.0
            if notional <= 0:
                continue
            if spent + notional > budget + 1e-9:
                remain = max(budget - spent, 0.0)
                if remain < max(notional * 0.05, 1.0):
                    continue
                notional = remain
            qty = notional / exec_px
            spent += notional
            filled_levels.add(pf.level_idx)
            fills.append(
                TickFill(
                    side=side,
                    price=exec_px,
                    qty=qty,
                    notional=notional,
                    level_idx=pf.level_idx,
                    reason=pf.reason,
                    trade_ts=tr["timestamp"],
                )
            )
            if cfg.mode != "optimistic":
                break  # one fill per trade row in base/conservative

        last_px = px

    return fills
