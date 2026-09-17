"""Precise perp leg execution at tick prices — mirrors qtb/ab/engine accounting."""

from __future__ import annotations

from typing import Literal

from qtb.ab.engine import FeeSpec, _PerpState


def perp_open(
    st: _PerpState,
    direction: Literal["long", "short"],
    leverage: float,
    qty_abs: float,
    px: float,
    fee: FeeSpec,
    *,
    maker: bool = True,
    level_idx: int | None = None,
) -> float:
    if qty_abs <= 0 or px <= 0 or st.liquidated:
        return 0.0
    sign = 1.0 if direction == "long" else -1.0
    lev = max(leverage, 1.0)
    notional = qty_abs * px
    fee_paid, reb = fee.fee_and_rebate(notional, maker=maker)
    margin = notional / lev
    if st.wallet < fee_paid + margin - 1e-12:
        scale = max(st.wallet - fee_paid, 0.0) / max(margin, 1e-12)
        qty_abs *= scale
        if qty_abs <= 0:
            return 0.0
        notional = qty_abs * px
        fee_paid, reb = fee.fee_and_rebate(notional, maker=maker)
        margin = notional / lev
    signed = sign * qty_abs
    if st.qty != 0 and (st.qty > 0) != (signed > 0):
        return 0.0
    st.wallet -= fee_paid + margin
    st.locked += margin
    new = abs(st.qty) * st.avg + notional
    st.qty += signed
    st.avg = new / abs(st.qty) if st.qty else 0.0
    st.fees += fee_paid
    st.rebates += reb
    st.turnover += notional
    if level_idx is not None:
        st.lots[level_idx] = st.lots.get(level_idx, 0.0) + qty_abs
    return qty_abs


def perp_close(
    st: _PerpState,
    direction: Literal["long", "short"],
    qty_abs: float,
    px: float,
    fee: FeeSpec,
    *,
    maker: bool = True,
    level_idx: int | None = None,
    is_grid: bool = False,
) -> float:
    if qty_abs <= 0 or px <= 0 or st.qty == 0:
        return 0.0
    qty_abs = min(qty_abs, abs(st.qty))
    notional = qty_abs * px
    fee_paid, reb = fee.fee_and_rebate(notional, maker=maker)
    raw = qty_abs * (px - st.avg) * (1.0 if st.qty > 0 else -1.0)
    frac = qty_abs / abs(st.qty)
    release = st.locked * frac
    st.wallet += release + raw - fee_paid
    st.locked = max(0.0, st.locked - release)
    st.qty = st.qty - (1.0 if st.qty > 0 else -1.0) * qty_abs
    if abs(st.qty) < 1e-12:
        st.qty = 0.0
        st.avg = 0.0
        st.locked = 0.0
        st.lots.clear()
    st.realized += raw - fee_paid
    st.fees += fee_paid
    st.rebates += reb
    st.turnover += notional
    if is_grid:
        st.gross_grid += raw - fee_paid
    if level_idx is not None:
        st.lots.pop(level_idx, None)
    return qty_abs


def adjust_notional_via_ticks(
    st: _PerpState,
    direction: Literal["long", "short"],
    leverage: float,
    target_notional: float,
    bar_trades,
    fee: FeeSpec,
    fill,
    *,
    participation_scale: float = 0.35,
) -> None:
    """Directional gap fill at tick prices (taker), participation-capped."""
    import pandas as pd

    if st.liquidated or bar_trades is None or (isinstance(bar_trades, pd.DataFrame) and bar_trades.empty):
        return

    mark = float(bar_trades["price"].iloc[-1])
    cur = abs(st.qty) * mark
    delta = target_notional - cur
    if abs(delta) < mark * 0.001:
        return

    budget = float(bar_trades["quote_qty"].sum()) * fill.participation * participation_scale
    spent = 0.0

    for _, tr in bar_trades.iterrows():
        if spent >= budget - 1e-9:
            break
        px = float(tr["price"])
        cur = abs(st.qty) * px
        delta = target_notional - cur
        if abs(delta) < px * 0.001:
            break
        if delta > 0:
            take = min(delta, budget - spent, float(tr["quote_qty"]) * fill.participation)
            if take <= 1.0:
                continue
            perp_open(st, direction, leverage, take / px, px, fee, maker=False)
            spent += take
        else:
            close_n = min(abs(delta), budget - spent)
            if close_n <= 1.0:
                continue
            perp_close(st, direction, close_n / px, px, fee, maker=False)
