"""Fair ETF-spot and perpetual grid engines.

Equity definitions (mandatory):
  ETF  = cash + ETF market value
  Perp = cash + margin + unrealized - funding - fees  (already in cash/upnl)
No extra 'volatility decay' deduction — that is already in the ETF price.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.costs.model import funding_pnl
from qtb.risk.liquidation import estimate_liq_price

from .fills import FillConfig, PendingFill, infer_tick, resolve_bar_fills
from .grids import (
    GridSpec,
    SizeMode,
    grid_quote_size,
    native_spec,
    realized_vol,
    rolling_atr,
    rolling_beta,
    static_spec,
    underlying_equiv_spec,
)

Side = Literal["long", "short"]
MarginMode = Literal["isolated", "cross"]
ReservePlan = Literal["P1", "P2", "P3"]

RESERVE_FRAC = {"P1": 0.0, "P2": 0.30, "P3": 0.50}


@dataclass
class TradeRec:
    ts: Any
    market: str
    side: str
    price: float
    qty: float
    notional: float
    fee: float
    rebate: float
    slippage: float
    reason: str
    equity: float


@dataclass
class EngineResult:
    name: str
    market: str
    symbol: str
    timestamps: list[Any]
    equity: np.ndarray
    cash: np.ndarray
    inventory_value: np.ndarray
    position_qty: np.ndarray
    margin_ratio: np.ndarray
    liq_buffer: np.ndarray
    trades: list[TradeRec]
    liquidated: bool
    liquidation_count: int
    margin_additions: list[dict[str, Any]]
    components: dict[str, float]
    extras: dict[str, Any] = field(default_factory=dict)

    @property
    def final_equity(self) -> float:
        return float(self.equity[-1]) if len(self.equity) else 0.0


@dataclass
class FeeSpec:
    maker: float
    taker: float
    rebate: float

    def effective(self, maker: bool) -> float:
        base = self.maker if maker else self.taker
        return base * (1.0 - self.rebate)

    def fee_and_rebate(self, notional: float, maker: bool) -> tuple[float, float]:
        base = (self.maker if maker else self.taker) * abs(notional)
        reb = base * self.rebate
        return base - reb, reb


def _warmup_bars(interval: str) -> int:
    return {
        "1s": 300,
        "10s": 180,
        "1m": 120,
        "5m": 48,
        "15m": 32,
        "1h": 24,
        "4h": 12,
        "1d": 7,
    }.get(interval, 24)


class _SpotState:
    def __init__(self, cash: float):
        self.cash = float(cash)
        self.qty = 0.0
        self.avg = 0.0
        self.lots: dict[int, float] = {}
        self.realized = 0.0
        self.fees = 0.0
        self.rebates = 0.0
        self.slip = 0.0
        self.turnover = 0.0
        self.gross_grid = 0.0


def _spot_equity(st: _SpotState, px: float) -> float:
    return st.cash + st.qty * px


def _buy_spot(st: _SpotState, qty: float, px: float, fee: float, rebate: float) -> None:
    cost = qty * px + fee
    if cost > st.cash + 1e-12:
        scale = st.cash / max(cost, 1e-12)
        qty *= scale
        fee *= scale
        rebate *= scale
        cost = qty * px + fee
    if qty <= 0 or cost > st.cash + 1e-9:
        return
    new = st.avg * st.qty + qty * px
    st.qty += qty
    st.avg = new / st.qty if st.qty else 0.0
    st.cash -= cost
    st.fees += fee
    st.rebates += rebate
    st.turnover += qty * px


def _sell_spot(st: _SpotState, qty: float, px: float, fee: float, rebate: float, is_grid: bool) -> float:
    qty = min(qty, st.qty)
    if qty <= 0:
        return 0.0
    pnl = qty * (px - st.avg) - fee
    st.qty -= qty
    st.cash += qty * px - fee
    st.realized += pnl
    st.fees += fee
    st.rebates += rebate
    st.turnover += qty * px
    if is_grid:
        st.gross_grid += pnl
    if st.qty <= 1e-16:
        st.qty = 0.0
        st.avg = 0.0
    return pnl


def _build_spec(
    mode: str,
    kind: str,
    mid: float,
    atr: float,
    beta: float,
    atr_step: float,
    atr_range: float,
    static_step: float,
    static_range: float,
    und_step: float,
    und_range: float,
) -> GridSpec:
    if mode == "native_atr":
        return native_spec(mid, max(atr, mid * 0.002), atr_step, atr_range, kind)  # type: ignore[arg-type]
    if mode == "underlying_equiv":
        return underlying_equiv_spec(mid, und_step, und_range, beta, kind)  # type: ignore[arg-type]
    return static_spec(mid, static_step, static_range, kind)  # type: ignore[arg-type]


def run_spot_grid(
    bars: pd.DataFrame,
    *,
    name: str,
    symbol: str,
    fee: FeeSpec,
    fill: FillConfig,
    initial: float = 1000.0,
    direction: Side = "long",
    dir_frac: float = 0.0,
    grid_mode: str = "native_atr",
    grid_kind: str = "geometric",
    atr_step: float = 0.40,
    atr_range: float = 5.0,
    static_step: float = 0.01,
    static_range: float = 0.15,
    und_step: float = 0.005,
    und_range: float = 0.15,
    und_close: np.ndarray | None = None,
    size_mode: SizeMode = "fixed_usdt",
    lower_boost: float = 1.0,
    reanchor: bool = True,
    interval: str = "1h",
    hold_only: bool = False,
) -> EngineResult:
    """Spot / ETF / underlying-spot. No external margin, no liquidation."""
    n = len(bars)
    ts = bars["timestamp"].to_numpy()
    o = bars["open"].to_numpy(float)
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    qv = bars["quote_volume"].to_numpy(float) if "quote_volume" in bars.columns else np.zeros(n)
    atr = rolling_atr(h, l, c, n=24)
    rv = realized_vol(c, n=24)
    beta = (
        rolling_beta(c, und_close, n=48)
        if und_close is not None and len(und_close) == n
        else np.full(n, 3.0)
    )
    warm = min(_warmup_bars(interval), max(n // 8, 8))
    st = _SpotState(initial)
    trades: list[TradeRec] = []
    eq = np.full(n, initial)
    cash_a = np.full(n, initial)
    inv_a = np.zeros(n)
    qty_a = np.zeros(n)
    spec: GridSpec | None = None
    atr_ref = float(atr[warm]) if warm < n else float(atr[0])
    tick = infer_tick(float(c[0]), fill.tick_size)
    fill = FillConfig(
        mode=fill.mode,
        participation=fill.participation,
        extra_ticks=fill.extra_ticks,
        extra_slip_bps=fill.extra_slip_bps,
        tick_size=tick,
    )

    def record(i: int, side: str, px: float, qty: float, fee_paid: float, rebate: float, reason: str) -> None:
        trades.append(
            TradeRec(
                ts=ts[i],
                market="spot",
                side=side,
                price=px,
                qty=qty,
                notional=qty * px,
                fee=fee_paid,
                rebate=rebate,
                slippage=0.0,
                reason=reason,
                equity=_spot_equity(st, c[i]),
            )
        )

    # directional open on first live bar (taker)
    if dir_frac > 0 and warm < n:
        px = float(o[warm])
        spend = initial * dir_frac
        fee_paid, reb = fee.fee_and_rebate(spend, maker=False)
        qty = max(spend - fee_paid, 0.0) / px
        _buy_spot(st, qty, px, fee_paid, reb)
        record(warm, "buy", px, qty, fee_paid, reb, "directional_open")

    if hold_only and warm < n and dir_frac <= 0:
        px = float(o[warm])
        fee_paid, reb = fee.fee_and_rebate(st.cash, maker=False)
        qty = max(st.cash - fee_paid, 0.0) / px
        _buy_spot(st, qty, px, fee_paid, reb)
        record(warm, "buy", px, qty, fee_paid, reb, "buy_hold")

    for i in range(n):
        if i == 0:
            eq[i] = _spot_equity(st, c[i])
            cash_a[i] = st.cash
            inv_a[i] = st.qty * c[i]
            qty_a[i] = st.qty
            continue
        if i < warm or hold_only:
            eq[i] = _spot_equity(st, c[i])
            cash_a[i] = st.cash
            inv_a[i] = st.qty * c[i]
            qty_a[i] = st.qty
            continue
        if spec is None or (
            reanchor
            and spec is not None
            and (c[i - 1] < spec.lower or c[i - 1] > spec.upper)
        ):
            spec = _build_spec(
                grid_mode,
                grid_kind,
                float(c[i - 1]),
                float(atr[i - 1]),
                float(beta[i - 1]),
                atr_step,
                atr_range,
                static_step,
                static_range,
                und_step,
                und_range,
            )
            # drop lots that no longer map; inventory stays
            st.lots = {k: v for k, v in st.lots.items() if 0 <= k < len(spec.levels)}

        n_lv = len(spec.levels)
        buy_budget = max(st.cash, 0.0)
        empty_buys = max(1, sum(1 for k in range(n_lv) if k not in st.lots and spec.levels[k] <= spec.mid))
        baseline = buy_budget / empty_buys if empty_buys else 0.0
        pending: list[PendingFill] = []
        if direction == "long":
            for idx, lvl in enumerate(spec.levels):
                if idx in st.lots:
                    continue
                if lvl > spec.mid * 1.0000001:
                    continue
                qsz = grid_quote_size(baseline, float(lvl), spec, size_mode, float(atr[i - 1]), atr_ref, lower_boost)
                if qsz < 1.0:
                    continue
                pending.append(PendingFill("buy", float(lvl), idx, notional=qsz, reason="grid_buy"))
            for idx, lot_qty in list(st.lots.items()):
                sell_idx = idx + 1
                if sell_idx >= n_lv:
                    continue
                pending.append(
                    PendingFill(
                        "sell",
                        float(spec.levels[sell_idx]),
                        idx,
                        qty=lot_qty,
                        notional=lot_qty * float(spec.levels[sell_idx]),
                        reduce_only=True,
                        reason="grid_sell",
                    )
                )
        else:
            # 3S / short-bias spot grid: sell inventory on the way up, buy back down.
            for idx, lvl in enumerate(spec.levels):
                if idx in st.lots:
                    continue
                if lvl < spec.mid * 0.999999:
                    continue
                if st.qty <= 0:
                    continue
                qsz = grid_quote_size(baseline, float(lvl), spec, size_mode, float(atr[i - 1]), atr_ref, lower_boost)
                qty = min(st.qty / max(1, n_lv // 2), qsz / max(float(lvl), 1e-12))
                if qty <= 0:
                    continue
                pending.append(PendingFill("sell", float(lvl), idx, qty=qty, notional=qty * float(lvl), reason="grid_short_spot"))
            for idx, lot_qty in list(st.lots.items()):
                cover = idx - 1
                if cover < 0:
                    continue
                pending.append(
                    PendingFill(
                        "buy",
                        float(spec.levels[cover]),
                        idx,
                        qty=lot_qty,
                        notional=lot_qty * float(spec.levels[cover]),
                        reduce_only=True,
                        reason="grid_cover_spot",
                    )
                )

        fills = resolve_bar_fills(pending, float(o[i]), float(h[i]), float(l[i]), float(c[i]), float(qv[i]), fill)
        for f in fills:
            if f.side == "buy":
                px = f.price
                notional = f.notional or 0.0
                fee_paid, reb = fee.fee_and_rebate(notional, maker=True)
                qty = notional / px if px > 0 else 0.0
                before = st.qty
                _buy_spot(st, qty, px, fee_paid, reb)
                got = st.qty - before
                if got > 0:
                    if f.reduce_only:
                        st.lots.pop(f.level_idx, None)
                    else:
                        st.lots[f.level_idx] = st.lots.get(f.level_idx, 0.0) + got
                    record(i, "buy", px, got, fee_paid, reb, f.reason)
            else:
                px = f.price
                qty = f.qty or ((f.notional or 0.0) / px if px else 0.0)
                qty = min(qty, st.qty)
                if qty <= 0:
                    continue
                fee_paid, reb = fee.fee_and_rebate(qty * px, maker=True)
                _sell_spot(st, qty, px, fee_paid, reb, is_grid=True)
                if f.level_idx in st.lots:
                    st.lots[f.level_idx] = max(0.0, st.lots[f.level_idx] - qty)
                    if st.lots[f.level_idx] <= 1e-16:
                        del st.lots[f.level_idx]
                record(i, "sell", px, qty, fee_paid, reb, f.reason)

        eq[i] = _spot_equity(st, c[i])
        cash_a[i] = st.cash
        inv_a[i] = st.qty * c[i]
        qty_a[i] = st.qty

    inventory_pnl = float(st.qty * c[-1] - (st.avg * st.qty if st.qty else 0.0))
    dir_pnl = float(eq[-1] - initial - st.gross_grid)
    components = {
        "gross_grid_profit": float(st.gross_grid),
        "spot_trading_fee": float(st.fees),
        "rebate": float(st.rebates),
        "spread_cost": 0.0,
        "slippage": float(st.slip),
        "inventory_pnl": inventory_pnl,
        "directional_pnl": dir_pnl,
        "turnover": float(st.turnover),
        "funding_paid": 0.0,
        "funding_received": 0.0,
        "net_funding": 0.0,
        "liquidation_loss": 0.0,
    }
    return EngineResult(
        name=name,
        market="spot",
        symbol=symbol,
        timestamps=list(ts),
        equity=eq,
        cash=cash_a,
        inventory_value=inv_a,
        position_qty=qty_a,
        margin_ratio=np.ones(n),
        liq_buffer=np.ones(n),
        trades=trades,
        liquidated=False,
        liquidation_count=0,
        margin_additions=[],
        components=components,
        extras={
            "dir_frac": dir_frac,
            "grid_mode": grid_mode,
            "fill": fill.mode,
            "rebate": fee.rebate,
            "final_qty": float(st.qty),
            "avg_cost": float(st.avg),
        },
    )


class _PerpState:
    def __init__(self, wallet: float, reserve: float):
        self.wallet = float(wallet)  # free allocated cash (not reserve, not locked IM)
        self.reserve = float(reserve)
        self.locked = 0.0
        self.qty = 0.0  # signed: +long -short
        self.avg = 0.0
        self.lots: dict[int, float] = {}
        self.realized = 0.0
        self.fees = 0.0
        self.rebates = 0.0
        self.turnover = 0.0
        self.gross_grid = 0.0
        self.funding_paid = 0.0
        self.funding_recv = 0.0
        self.liquidated = False
        self.liq_count = 0
        self.liq_loss = 0.0
        self.additions: list[dict[str, Any]] = []
        self.min_buffer = 1.0
        self.min_ratio = 10.0
        self.forced_delever = 0


def _perp_upnl(st: _PerpState, mark: float) -> float:
    if st.qty == 0:
        return 0.0
    return st.qty * (mark - st.avg)


def _perp_equity(st: _PerpState, mark: float, include_reserve: bool = True, isolated: bool = False) -> float:
    """TOTAL equity = free + locked IM + uPnL + optional reserve.

    Isolated liquidation uses only locked+uPnL. Cross uses free+locked+uPnL.
    Reserve is never at risk until a pre-defined add-margin rule moves it.
    """
    if st.liquidated and st.qty == 0:
        base = st.wallet + (st.reserve if include_reserve else 0.0)
        return max(base, 0.0)
    core = (st.locked + _perp_upnl(st, mark)) if isolated else (st.wallet + st.locked + _perp_upnl(st, mark))
    return core + (st.reserve if include_reserve else 0.0)


def run_perp_grid(
    bars: pd.DataFrame,
    *,
    name: str,
    symbol: str,
    fee: FeeSpec,
    fill: FillConfig,
    initial: float = 1000.0,
    direction: Side = "long",
    target_notional: float = 3000.0,
    dir_frac: float = 0.0,
    margin_mode: MarginMode = "isolated",
    reserve_plan: ReservePlan = "P1",
    add_trigger: float = 0.15,
    mm_rate: float = 0.005,
    quanto: float = 0.0001,
    min_contracts: float = 1.0,
    grid_mode: str = "native_atr",
    grid_kind: str = "geometric",
    atr_step: float = 0.40,
    atr_range: float = 5.0,
    static_step: float = 0.005,
    static_range: float = 0.15,
    und_step: float = 0.005,
    und_range: float = 0.15,
    size_mode: SizeMode = "fixed_usdt",
    lower_boost: float = 1.0,
    reanchor: bool = True,
    interval: str = "1h",
    hold_only: bool = False,
    leverage_hint: float = 3.0,
) -> EngineResult:
    """Closed 1000U perpetual account. No external top-up. Liquidation is terminal for the position."""
    n = len(bars)
    ts = bars["timestamp"].to_numpy()
    o = bars["open"].to_numpy(float)
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    qv = bars["quote_volume"].to_numpy(float) if "quote_volume" in bars.columns else np.zeros(n)
    fr = bars["funding_rate"].to_numpy(float) if "funding_rate" in bars.columns else np.zeros(n)
    atr = rolling_atr(h, l, c, n=24)
    warm = min(_warmup_bars(interval), max(n // 8, 8))
    rfrac = RESERVE_FRAC[reserve_plan]
    st = _PerpState(wallet=initial * (1.0 - rfrac), reserve=initial * rfrac)
    trades: list[TradeRec] = []
    eq = np.full(n, initial)
    cash_a = np.full(n, initial)
    inv_a = np.zeros(n)
    qty_a = np.zeros(n)
    mratio = np.ones(n)
    lbuf = np.ones(n)
    spec: GridSpec | None = None
    atr_ref = float(atr[warm]) if warm < n else float(atr[0])
    tick = infer_tick(float(c[0]), fill.tick_size)
    fill = FillConfig(fill.mode, fill.participation, fill.extra_ticks, fill.extra_slip_bps, tick)
    sign = 1.0 if direction == "long" else -1.0
    halted = False

    def equity_now(px: float) -> float:
        return _perp_equity(st, px, include_reserve=True, isolated=False)

    def risk_equity(px: float) -> float:
        return _perp_equity(st, px, include_reserve=False, isolated=(margin_mode == "isolated"))

    def maint(px: float) -> float:
        return abs(st.qty) * px * mm_rate

    def buffer(px: float) -> float:
        e = risk_equity(px)
        m = maint(px)
        if e <= 1e-12:
            return 0.0
        return (e - m) / e

    def ratio(px: float) -> float:
        m = maint(px)
        e = risk_equity(px)
        if m <= 1e-12:
            return 10.0
        return e / m

    def record(i: int, side: str, px: float, qty: float, fee_paid: float, rebate: float, reason: str) -> None:
        trades.append(
            TradeRec(
                ts=ts[i],
                market="perp",
                side=side,
                price=px,
                qty=qty,
                notional=abs(qty) * px,
                fee=fee_paid,
                rebate=rebate,
                slippage=0.0,
                reason=reason,
                equity=equity_now(c[i]),
            )
        )

    def try_add_margin(i: int, px: float) -> None:
        if st.reserve <= 1e-9 or st.qty == 0:
            return
        buf = buffer(px)
        if buf > add_trigger:
            return
        # Restore toward max(2*trigger, 0.40) without lookahead.
        target = max(add_trigger * 2.0, 0.40)
        e = risk_equity(px)
        m = maint(px)
        # (e+x - m) / (e+x) = target  => x(1-target)= m - e(1-target)
        need = (m - e * (1.0 - target)) / max(1.0 - target, 1e-9)
        need = max(need, initial * 0.10)
        x = min(st.reserve, max(need, 0.0))
        if x <= 1e-9:
            return
        st.reserve -= x
        if margin_mode == "isolated":
            st.locked += x
        else:
            st.wallet += x
        st.additions.append({"ts": str(ts[i]), "amount": x, "buffer_before": buf, "trigger": add_trigger})

    def liquidate(i: int, px: float) -> None:
        e_risk = max(risk_equity(px), 0.0)
        st.liq_loss += e_risk
        if margin_mode == "isolated":
            st.locked = 0.0
        else:
            st.wallet = 0.0
            st.locked = 0.0
        st.qty = 0.0
        st.avg = 0.0
        st.lots = {}
        st.liquidated = True
        st.liq_count += 1
        record(i, "sell" if sign > 0 else "buy", px, 0.0, 0.0, 0.0, "LIQUIDATED")

    def open_qty(i: int, px: float, qty_abs: float, is_maker: bool, reason: str, level: int | None) -> float:
        if qty_abs <= 0 or st.liquidated or halted or px <= 0:
            return 0.0
        lev = max(leverage_hint, 1e-9)
        # Size down so fee + IM fit in free cash. Never pull reserve here.
        notional = qty_abs * px
        fee_paid, reb = fee.fee_and_rebate(notional, maker=is_maker)
        margin = notional / lev
        if st.wallet < fee_paid + 1e-12:
            return 0.0
        if st.wallet < margin + fee_paid:
            max_notional = max(st.wallet - fee.effective(is_maker) * st.wallet, 0.0) * lev / max(1.0 + fee.effective(is_maker) * lev, 1e-9)
            qty_abs = max_notional / px
            contracts = qty_abs / max(quanto, 1e-12)
            if contracts + 1e-12 < min_contracts:
                return 0.0
            qty_abs = int(contracts) * quanto if quanto > 0 else qty_abs
            notional = qty_abs * px
            fee_paid, reb = fee.fee_and_rebate(notional, maker=is_maker)
            margin = notional / lev
        else:
            contracts = qty_abs / max(quanto, 1e-12)
            if contracts + 1e-12 < min_contracts:
                return 0.0
            qty_abs = int(contracts) * quanto if quanto > 0 else qty_abs
            notional = qty_abs * px
            fee_paid, reb = fee.fee_and_rebate(notional, maker=is_maker)
            margin = notional / lev
        if qty_abs <= 0 or st.wallet < fee_paid + margin - 1e-9:
            return 0.0
        signed = sign * qty_abs
        if not (st.qty == 0 or (st.qty > 0 and signed > 0) or (st.qty < 0 and signed < 0)):
            return 0.0
        st.wallet -= fee_paid + margin
        st.locked += margin
        new = abs(st.qty) * st.avg + notional
        st.qty += signed
        st.avg = new / abs(st.qty) if st.qty else 0.0
        st.fees += fee_paid
        st.rebates += reb
        st.turnover += notional
        if level is not None:
            st.lots[level] = st.lots.get(level, 0.0) + qty_abs
        record(i, "buy" if signed > 0 else "sell", px, qty_abs, fee_paid, reb, reason)
        return qty_abs

    def close_qty(i: int, px: float, qty_abs: float, is_maker: bool, reason: str, level: int | None, is_grid: bool) -> None:
        if qty_abs <= 0 or st.qty == 0:
            return
        qty_abs = min(qty_abs, abs(st.qty))
        notional = qty_abs * px
        fee_paid, reb = fee.fee_and_rebate(notional, maker=is_maker)
        raw = qty_abs * (px - st.avg) * (1.0 if st.qty > 0 else -1.0)
        frac = qty_abs / abs(st.qty)
        release = st.locked * frac
        st.wallet += release + raw - fee_paid
        st.locked = max(0.0, st.locked - release)
        if abs(st.qty) <= qty_abs + 1e-12:
            st.qty = 0.0
            st.avg = 0.0
            st.locked = 0.0
        else:
            st.qty = st.qty - float(np.sign(st.qty)) * qty_abs
        st.realized += raw - fee_paid
        st.fees += fee_paid
        st.rebates += reb
        st.turnover += notional
        if is_grid:
            st.gross_grid += raw - fee_paid
        if level is not None:
            st.lots.pop(level, None)
        record(i, "sell" if sign > 0 else "buy", px, qty_abs, fee_paid, reb, reason)

    # initial directional / hold
    if warm < n and (dir_frac > 0 or hold_only):
        px = float(o[warm])
        notional = target_notional if hold_only else target_notional * dir_frac
        open_qty(warm, px, notional / px, is_maker=False, reason="directional_open", level=None)

    for i in range(n):
        px_mark = float(c[i])
        if st.qty != 0 and not st.liquidated and abs(fr[i]) > 0:
            pnl = funding_pnl(st.qty, float(o[i]), float(fr[i]))
            st.wallet += pnl
            if st.wallet < 0 and st.locked > 0:
                take = min(st.locked, -st.wallet)
                st.locked -= take
                st.wallet += take
            if pnl < 0:
                st.funding_paid += -pnl
            else:
                st.funding_recv += pnl
            record(i, "funding", float(o[i]), abs(st.qty), 0.0, 0.0, "funding")

        if st.qty != 0 and not st.liquidated:
            adv = float(l[i]) if st.qty > 0 else float(h[i])
            try_add_margin(i, adv)
            e_adv = risk_equity(adv)
            m_adv = abs(st.qty) * adv * mm_rate
            if e_adv <= m_adv or e_adv <= 0:
                liquidate(i, adv)
                halted = True

        if (not hold_only) and (not halted) and (not st.liquidated) and i >= warm:
            if spec is None or (
                reanchor and spec is not None and (c[i - 1] < spec.lower or c[i - 1] > spec.upper)
            ):
                spec = _build_spec(
                    grid_mode,
                    grid_kind,
                    float(c[i - 1]),
                    float(atr[i - 1]),
                    1.0,
                    atr_step,
                    atr_range,
                    static_step,
                    static_range,
                    und_step,
                    und_range,
                )
                st.lots = {k: v for k, v in st.lots.items() if 0 <= k < len(spec.levels)}

            n_lv = len(spec.levels)
            remaining_notional = max(target_notional - abs(st.qty) * px_mark, 0.0)
            empty = max(1, sum(1 for k, lvl in enumerate(spec.levels) if k not in st.lots and (
                (direction == "long" and lvl <= spec.mid) or (direction == "short" and lvl >= spec.mid)
            )))
            baseline = remaining_notional / empty
            pending: list[PendingFill] = []
            if direction == "long":
                for idx, lvl in enumerate(spec.levels):
                    if idx in st.lots or lvl > spec.mid * 1.0000001:
                        continue
                    qsz = grid_quote_size(baseline, float(lvl), spec, size_mode, float(atr[i - 1]), atr_ref, lower_boost)
                    if qsz < 1.0:
                        continue
                    pending.append(PendingFill("buy", float(lvl), idx, notional=qsz, reason="grid_buy"))
                for idx, lot_qty in list(st.lots.items()):
                    sidx = idx + 1
                    if sidx >= n_lv:
                        continue
                    pending.append(
                        PendingFill(
                            "sell",
                            float(spec.levels[sidx]),
                            idx,
                            qty=lot_qty,
                            notional=lot_qty * float(spec.levels[sidx]),
                            reduce_only=True,
                            reason="grid_sell",
                        )
                    )
            else:
                for idx, lvl in enumerate(spec.levels):
                    if idx in st.lots or lvl < spec.mid * 0.999999:
                        continue
                    qsz = grid_quote_size(baseline, float(lvl), spec, size_mode, float(atr[i - 1]), atr_ref, lower_boost)
                    if qsz < 1.0:
                        continue
                    pending.append(PendingFill("sell", float(lvl), idx, notional=qsz, reason="grid_short"))
                for idx, lot_qty in list(st.lots.items()):
                    cidx = idx - 1
                    if cidx < 0:
                        continue
                    pending.append(
                        PendingFill(
                            "buy",
                            float(spec.levels[cidx]),
                            idx,
                            qty=lot_qty,
                            notional=lot_qty * float(spec.levels[cidx]),
                            reduce_only=True,
                            reason="grid_cover",
                        )
                    )
            fills = resolve_bar_fills(pending, float(o[i]), float(h[i]), float(l[i]), float(c[i]), float(qv[i]), fill)
            for f in fills:
                if f.reduce_only:
                    qty = f.qty or ((f.notional or 0.0) / f.price)
                    close_qty(i, f.price, qty, True, f.reason, f.level_idx, True)
                else:
                    qty = (f.notional or 0.0) / f.price if f.price else 0.0
                    open_qty(i, f.price, qty, True, f.reason, f.level_idx)

        e = equity_now(px_mark)
        eq[i] = e
        cash_a[i] = st.wallet + st.locked + st.reserve
        inv_a[i] = _perp_upnl(st, px_mark) + st.locked
        qty_a[i] = st.qty
        if st.qty != 0 and not st.liquidated:
            b = buffer(px_mark)
            r = ratio(px_mark)
            lbuf[i] = b
            mratio[i] = r
            st.min_buffer = min(st.min_buffer, b)
            st.min_ratio = min(st.min_ratio, r)
        else:
            lbuf[i] = 1.0 if not st.liquidated else 0.0
            mratio[i] = 10.0 if not st.liquidated else 0.0

    components = {
        "gross_grid_profit": float(st.gross_grid),
        "futures_fee": float(st.fees),
        "rebate": float(st.rebates),
        "funding_paid": float(st.funding_paid),
        "funding_received": float(st.funding_recv),
        "net_funding": float(st.funding_recv - st.funding_paid),
        "spread_cost": 0.0,
        "slippage": 0.0,
        "directional_pnl": float(eq[-1] - initial - st.gross_grid - (st.funding_recv - st.funding_paid)),
        "liquidation_loss": float(st.liq_loss),
        "turnover": float(st.turnover),
        "inventory_pnl": float(_perp_upnl(st, float(c[-1]))),
    }
    return EngineResult(
        name=name,
        market="perp",
        symbol=symbol,
        timestamps=list(ts),
        equity=eq,
        cash=cash_a,
        inventory_value=inv_a,
        position_qty=qty_a,
        margin_ratio=mratio,
        liq_buffer=lbuf,
        trades=trades,
        liquidated=st.liquidated,
        liquidation_count=st.liq_count,
        margin_additions=st.additions,
        components=components,
        extras={
            "min_liquidation_buffer": st.min_buffer,
            "min_margin_ratio": st.min_ratio,
            "forced_deleveraging_count": st.forced_delever,
            "reserve_left": st.reserve,
            "target_notional": target_notional,
            "margin_mode": margin_mode,
            "reserve_plan": reserve_plan,
            "leverage_hint": leverage_hint,
            "add_trigger": add_trigger,
            "fill": fill.mode,
            "rebate": fee.rebate,
        },
    )


def run_cash(bars: pd.DataFrame, initial: float = 1000.0, name: str = "A0_cash") -> EngineResult:
    n = len(bars)
    eq = np.full(n, initial)
    z = np.zeros(n)
    return EngineResult(
        name=name,
        market="cash",
        symbol="USDT",
        timestamps=list(bars["timestamp"]),
        equity=eq,
        cash=eq.copy(),
        inventory_value=z,
        position_qty=z,
        margin_ratio=np.ones(n),
        liq_buffer=np.ones(n),
        trades=[],
        liquidated=False,
        liquidation_count=0,
        margin_additions=[],
        components={"turnover": 0.0},
    )
