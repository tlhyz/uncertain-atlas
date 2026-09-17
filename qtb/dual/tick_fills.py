"""Tick-level fill simulation from Binance aggTrades — path-exact, no look-ahead."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
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
    reduce_only: bool = False


def _crosses_buy(p0: float, p1: float, limit: float, tick_need: float) -> bool:
    trigger = limit - tick_need
    if p1 >= p0:
        return False
    return p0 > trigger and p1 <= trigger


def _crosses_sell(p0: float, p1: float, limit: float, tick_need: float) -> bool:
    trigger = limit + tick_need
    if p1 <= p0:
        return False
    return p0 < trigger and p1 >= trigger


def _tick_path(bar_open: float, bar_close: float, trade_prices: np.ndarray) -> list[tuple[float, float]]:
    """Real tick path: open → each aggTrade price → close."""
    pts: list[float] = [float(bar_open)]
    for p in trade_prices:
        pts.append(float(p))
    if not pts or abs(pts[-1] - bar_close) > 1e-12:
        pts.append(float(bar_close))
    segs: list[tuple[float, float]] = []
    for j in range(1, len(pts)):
        if abs(pts[j] - pts[j - 1]) > 1e-15:
            segs.append((pts[j - 1], pts[j]))
    return segs


def resolve_tick_fills(
    pending: list[PendingFill],
    bar_trades: pd.DataFrame,
    cfg: FillConfig,
    *,
    bar_open: float,
    bar_close: float,
) -> list[TickFill]:
    """
    Walk the exact aggTrade price path (open → ticks → close).
    Same crossing/participation rules as resolve_bar_fills — never multi-level touch fill.
    """
    if not pending or bar_trades.empty:
        return []

    budget = float(bar_trades["quote_qty"].sum()) * cfg.participation
    if cfg.mode != "optimistic" and budget <= 0:
        return []

    tick = cfg.tick_size if cfg.tick_size > 0 else infer_tick(float(bar_trades["price"].iloc[0]))
    tick_need = tick * float(cfg.extra_ticks)

    buys = [f for f in pending if f.side == "buy" and not f.reduce_only]
    sells = [f for f in pending if f.side == "sell" and not f.reduce_only]
    tp_sells = [f for f in pending if f.side == "sell" and f.reduce_only]
    tp_buys = [f for f in pending if f.side == "buy" and f.reduce_only]

    buys.sort(key=lambda f: -f.price)
    sells.sort(key=lambda f: f.price)
    tp_sells.sort(key=lambda f: f.price)
    tp_buys.sort(key=lambda f: -f.price)

    prices = bar_trades["price"].to_numpy(float)
    ts = bar_trades["timestamp"].to_numpy()
    segments = _tick_path(bar_open, bar_close, prices)

    filled: list[TickFill] = []
    filled_open_levels: set[int] = set()
    spent = 0.0

    def _emit(side: str, px: float, f: PendingFill, ts_val) -> bool:
        nonlocal spent
        if f.level_idx in filled_open_levels and not f.reduce_only:
            return False
        notional = f.notional if f.notional and f.notional > 0 else (f.qty or 0.0) * px
        if notional <= 0:
            return False
        take = min(notional, budget - spent) if cfg.mode != "optimistic" else notional
        if take < notional * 0.25 and cfg.mode != "optimistic":
            return False
        qty = (f.qty or 0.0) * (take / notional) if f.qty else take / px
        spent += take
        if not f.reduce_only:
            filled_open_levels.add(f.level_idx)
        filled.append(
            TickFill(
                side=side,
                price=px,
                qty=qty,
                notional=take,
                level_idx=f.level_idx,
                reason=f.reason,
                trade_ts=pd.Timestamp(ts_val),
                reduce_only=f.reduce_only,
            )
        )
        return True

    buy_i = sell_i = tp_s_i = tp_b_i = 0
    ts_idx = 0

    for p0, p1 in segments:
        if cfg.mode != "optimistic" and spent >= budget - 1e-9:
            break
        ts_val = ts[min(ts_idx, len(ts) - 1)] if len(ts) else bar_trades["timestamp"].iloc[0]
        if p1 < p0:
            while buy_i < len(buys) and spent < budget + 1e-9:
                f = buys[buy_i]
                if not _crosses_buy(p0, p1, f.price, tick_need):
                    if f.price > p0:
                        buy_i += 1
                        continue
                    break
                px = apply_adverse_slip(f.price, "buy", cfg.extra_slip_bps)
                if _emit("buy", px, f, ts_val):
                    buy_i += 1
                else:
                    break
            while tp_b_i < len(tp_buys) and spent < budget + 1e-9:
                f = tp_buys[tp_b_i]
                if not _crosses_buy(p0, p1, f.price, tick_need):
                    break
                px = apply_adverse_slip(f.price, "buy", cfg.extra_slip_bps)
                if _emit("buy", px, f, ts_val):
                    tp_b_i += 1
                else:
                    break
        elif p1 > p0:
            while sell_i < len(sells) and spent < budget + 1e-9:
                f = sells[sell_i]
                if not _crosses_sell(p0, p1, f.price, tick_need):
                    if f.price < p0:
                        sell_i += 1
                        continue
                    break
                px = apply_adverse_slip(f.price, "sell", cfg.extra_slip_bps)
                if _emit("sell", px, f, ts_val):
                    sell_i += 1
                else:
                    break
            while tp_s_i < len(tp_sells) and spent < budget + 1e-9:
                f = tp_sells[tp_s_i]
                if not _crosses_sell(p0, p1, f.price, tick_need):
                    break
                px = apply_adverse_slip(f.price, "sell", cfg.extra_slip_bps)
                if _emit("sell", px, f, ts_val):
                    tp_s_i += 1
                else:
                    break
        if p1 in prices:
            ts_idx = min(ts_idx + 1, len(ts) - 1)

    return filled
