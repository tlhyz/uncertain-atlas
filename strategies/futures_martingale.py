"""USDT-M futures Martingale simulator (LONG / SHORT) with leverage + margin DD."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np
import pandas as pd

from fees import FeeConfig, fee_on_notional

Direction = Literal["long", "short"]


@dataclass
class FuturesMartingaleParams:
    base_order_quote: float = 20.0  # notional of first order (USDT)
    multiplier: float = 1.5
    add_drop_pct: float = 0.018  # adverse move % to add
    take_profit_pct: float = 0.012  # TP from average entry
    max_adds: int = 6
    initial_margin: float = 1000.0  # wallet / investment
    leverage: float = 5.0
    direction: Direction = "long"
    fee_as_maker: bool = False
    maintenance_rate: float = 0.025  # Gate contract maintenance ~2.5%
    cooldown_bars: int = 0
    # Stop-loss as fraction of bot investment (initial_margin).
    # When set (e.g. 0.70), force-close the open cycle if uPnL/initial_margin <= -stop_loss_pct,
    # realize the loss, then allow a new cycle. None/0 disables.
    # NOTE: Gate UI "止损%" is documented as % of avg entry price (bot terminates);
    # this simulator's primary mode is investment/equity drawdown as above.
    stop_loss_pct: float | None = None


@dataclass
class FuturesMartingaleResult:
    params: FuturesMartingaleParams
    fee_config: FeeConfig
    net_pnl: float
    gross_pnl: float
    total_fees: float
    max_drawdown: float
    max_drawdown_pct: float
    cycles: int
    win_rate: float
    num_trades: int
    final_equity: float
    fee_drag: float
    liquidated: bool = False
    equity_curve: list[float] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        return {
            "strategy": f"futures_martingale_{self.params.direction}",
            "fee_label": self.fee_config.label,
            "direction": self.params.direction,
            "leverage": self.params.leverage,
            "net_pnl": round(self.net_pnl, 4),
            "gross_pnl": round(self.gross_pnl, 4),
            "total_fees": round(self.total_fees, 4),
            "max_drawdown": round(self.max_drawdown, 4),
            "max_drawdown_pct": round(self.max_drawdown_pct, 4),
            "cycles": self.cycles,
            "win_rate": round(self.win_rate, 4),
            "num_trades": self.num_trades,
            "final_equity": round(self.final_equity, 4),
            "fee_drag": round(self.fee_drag, 6),
            "liquidated": self.liquidated,
            "stop_outs": int(self.stats.get("stop_outs", 0)),
            "rebate_rate": self.fee_config.rebate_rate,
            "eff_maker": round(self.fee_config.effective_maker, 8),
            "eff_taker": round(self.fee_config.effective_taker, 8),
            "risk_score": round(
                self.net_pnl / max(self.max_drawdown, 1.0) if not self.liquidated else -1e9,
                4,
            ),
        }


class FuturesMartingaleSimulator:
    """
    Isolated-margin style futures Martingale:
    - Each fill consumes margin = notional / leverage (+ fee from wallet).
    - LONG: add on dips; TP above avg. SHORT: add on rallies; TP below avg.
    - Optional stop_loss_pct: close cycle when uPnL / initial_margin <= -stop_loss_pct
      (investment drawdown stop), then allow a new cycle (not permanent halt).
    - Liquidation when equity <= maintenance * position_notional (approx).
    Funding is NOT modeled (noted separately in reports).
    """

    def __init__(self, params: FuturesMartingaleParams, fee_config: FeeConfig):
        self.params = params
        self.fee_config = fee_config

    def _fee_rate(self) -> float:
        if self.params.fee_as_maker:
            return self.fee_config.effective_maker
        return self.fee_config.effective_taker

    def run(self, df: pd.DataFrame) -> FuturesMartingaleResult:
        required = {"open", "high", "low", "close"}
        if not required.issubset(df.columns):
            raise ValueError(f"OHLCV missing columns: {required - set(df.columns)}")

        highs = df["high"].astype(float).values
        lows = df["low"].astype(float).values
        closes = df["close"].astype(float).values

        p = self.params
        fee_rate = self._fee_rate()
        wallet = float(p.initial_margin)
        pos_qty = 0.0  # base coin amount (>0 long, <0 short conceptually we use signed)
        avg_entry = 0.0
        last_entry = 0.0
        adds = 0
        in_position = False
        next_notional = p.base_order_quote
        cooldown = 0
        liquidated = False

        total_fees = 0.0
        cycles = 0
        wins = 0
        trades = 0
        stop_outs = 0
        stop_out_pnl_sum = 0.0
        equity_curve: list[float] = []
        peak = wallet
        max_dd = 0.0
        max_dd_pct = 0.0
        cycle_pnls: list[float] = []
        max_adds_hit = 0
        max_margin_used = 0.0
        sl_pct = float(p.stop_loss_pct) if p.stop_loss_pct and p.stop_loss_pct > 0 else 0.0

        def margin_for(notional: float) -> float:
            return abs(notional) / max(p.leverage, 1e-9)

        def unrealized_pnl(price: float) -> float:
            if pos_qty <= 0:
                return 0.0
            if p.direction == "long":
                return pos_qty * (price - avg_entry)
            return abs(pos_qty) * (avg_entry - price)

        def mtm_equity(price: float) -> float:
            if pos_qty == 0:
                return wallet
            # While open: equity = free wallet + locked margin + uPnL
            nonlocal margin_locked
            return wallet + margin_locked + unrealized_pnl(price)

        def investment_stop_price() -> float | None:
            """Price where uPnL / initial_margin == -sl_pct (investment drawdown stop)."""
            if sl_pct <= 0 or pos_qty <= 0:
                return None
            loss = sl_pct * p.initial_margin
            if p.direction == "long":
                # qty*(price-avg) = -loss  => price = avg - loss/qty
                return avg_entry - loss / pos_qty
            # short: qty*(avg-price) = -loss => price = avg + loss/qty
            return avg_entry + loss / pos_qty

        def hit_investment_stop(price: float) -> bool:
            if sl_pct <= 0 or pos_qty <= 0:
                return False
            return unrealized_pnl(price) / max(p.initial_margin, 1e-9) <= -sl_pct

        margin_locked = 0.0

        def open_or_add(price: float, notional: float) -> bool:
            nonlocal wallet, pos_qty, avg_entry, last_entry, total_fees, trades, margin_locked
            fee = fee_on_notional(notional, fee_rate)
            marg = margin_for(notional)
            need = marg + fee
            if wallet < need or notional <= 0 or price <= 0:
                return False
            qty = notional / price
            if p.direction == "short":
                # accumulate short qty as positive magnitude; sign handled in PnL
                new_cost = avg_entry * abs(pos_qty) + notional
                pos_qty = abs(pos_qty) + qty
                avg_entry = new_cost / pos_qty if pos_qty > 0 else 0.0
            else:
                new_cost = avg_entry * pos_qty + notional
                pos_qty = pos_qty + qty
                avg_entry = new_cost / pos_qty if pos_qty > 0 else 0.0
            wallet -= need
            margin_locked += marg
            last_entry = price
            total_fees += fee
            trades += 1
            return True

        def close_all(price: float) -> float:
            nonlocal wallet, pos_qty, avg_entry, last_entry, total_fees, trades
            nonlocal in_position, next_notional, adds, margin_locked
            if pos_qty <= 0:
                return 0.0
            notional = pos_qty * price
            fee = fee_on_notional(notional, fee_rate)
            raw = (
                pos_qty * (price - avg_entry)
                if p.direction == "long"
                else pos_qty * (avg_entry - price)
            )
            # free cash + return locked margin + realize raw PnL - close fee
            wallet = wallet + margin_locked + raw - fee
            total_fees += fee
            trades += 1
            realized = raw - fee
            pos_qty = 0.0
            avg_entry = 0.0
            last_entry = 0.0
            margin_locked = 0.0
            in_position = False
            next_notional = p.base_order_quote
            adds = 0
            return realized

        def check_liq(price: float) -> bool:
            if pos_qty <= 0:
                return False
            eq = mtm_equity(price)
            notional = pos_qty * price
            # bankrupt / liq if equity below maintenance margin
            return eq <= notional * p.maintenance_rate or eq <= 0

        for i in range(len(closes)):
            lo, hi, cl = float(lows[i]), float(highs[i]), float(closes[i])

            if liquidated:
                equity_curve.append(0.0)
                continue

            if cooldown > 0:
                cooldown -= 1
                eq = mtm_equity(cl)
                equity_curve.append(eq)
                if eq > peak:
                    peak = eq
                dd = peak - eq
                if dd > max_dd:
                    max_dd = dd
                dd_pct = dd / peak if peak > 0 else 0.0
                if dd_pct > max_dd_pct:
                    max_dd_pct = dd_pct
                continue

            if not in_position:
                entry = cl
                if open_or_add(entry, next_notional):
                    in_position = True
                    adds = 0
                    next_notional = p.base_order_quote * p.multiplier
                    max_margin_used = max(max_margin_used, margin_locked)
            else:
                closed_this_bar = False
                if p.direction == "long":
                    tp_price = avg_entry * (1.0 + p.take_profit_pct)
                    if hi >= tp_price and pos_qty > 0:
                        pnl = close_all(tp_price)
                        cycles += 1
                        cycle_pnls.append(pnl)
                        if pnl > 0:
                            wins += 1
                        cooldown = p.cooldown_bars
                        closed_this_bar = True
                    else:
                        # Process adverse adds first (avg improves), then investment SL
                        trigger = last_entry * (1.0 - p.add_drop_pct)
                        if lo <= trigger and adds < p.max_adds:
                            if open_or_add(trigger, next_notional):
                                adds += 1
                                max_adds_hit = max(max_adds_hit, adds)
                                next_notional = p.base_order_quote * (p.multiplier ** (adds + 1))
                                max_margin_used = max(max_margin_used, margin_locked)
                        if in_position and hit_investment_stop(lo):
                            sl_px = investment_stop_price()
                            # Clamp to bar range (cannot fill better/worse than printed extremes)
                            fill = max(min(sl_px if sl_px is not None else lo, hi), lo)
                            pnl = close_all(fill)
                            cycles += 1
                            stop_outs += 1
                            stop_out_pnl_sum += pnl
                            cycle_pnls.append(pnl)
                            if pnl > 0:
                                wins += 1
                            cooldown = p.cooldown_bars
                            closed_this_bar = True
                else:  # short
                    tp_price = avg_entry * (1.0 - p.take_profit_pct)
                    if lo <= tp_price and pos_qty > 0:
                        pnl = close_all(tp_price)
                        cycles += 1
                        cycle_pnls.append(pnl)
                        if pnl > 0:
                            wins += 1
                        cooldown = p.cooldown_bars
                        closed_this_bar = True
                    else:
                        trigger = last_entry * (1.0 + p.add_drop_pct)
                        if hi >= trigger and adds < p.max_adds:
                            if open_or_add(trigger, next_notional):
                                adds += 1
                                max_adds_hit = max(max_adds_hit, adds)
                                next_notional = p.base_order_quote * (p.multiplier ** (adds + 1))
                                max_margin_used = max(max_margin_used, margin_locked)
                        if in_position and hit_investment_stop(hi):
                            sl_px = investment_stop_price()
                            fill = max(min(sl_px if sl_px is not None else hi, hi), lo)
                            pnl = close_all(fill)
                            cycles += 1
                            stop_outs += 1
                            stop_out_pnl_sum += pnl
                            cycle_pnls.append(pnl)
                            if pnl > 0:
                                wins += 1
                            cooldown = p.cooldown_bars
                            closed_this_bar = True

            # Adverse extreme for liq check within bar
            stress = lo if p.direction == "long" else hi
            if in_position and check_liq(stress):
                # force close at stress as liquidation loss
                eq_before = mtm_equity(stress)
                # wipe to ~0
                wallet = 0.0
                pos_qty = 0.0
                avg_entry = 0.0
                margin_locked = 0.0
                in_position = False
                liquidated = True
                equity_curve.append(0.0)
                max_dd = max(max_dd, peak)
                max_dd_pct = 1.0
                continue

            eq = mtm_equity(cl)
            equity_curve.append(eq)
            if eq > peak:
                peak = eq
            dd = peak - eq
            if dd > max_dd:
                max_dd = dd
            dd_pct = dd / peak if peak > 0 else 0.0
            if dd_pct > max_dd_pct:
                max_dd_pct = dd_pct

        final_price = float(closes[-1])
        if liquidated:
            final_equity = 0.0
        else:
            final_equity = mtm_equity(final_price)
        initial = p.initial_margin
        net_pnl = final_equity - initial
        gross_pnl = net_pnl + total_fees
        win_rate = (wins / cycles) if cycles > 0 else 0.0
        fee_drag = total_fees / max(abs(gross_pnl), 1e-9)

        return FuturesMartingaleResult(
            params=self.params,
            fee_config=self.fee_config,
            net_pnl=net_pnl,
            gross_pnl=gross_pnl,
            total_fees=total_fees,
            max_drawdown=max_dd,
            max_drawdown_pct=max_dd_pct,
            cycles=cycles,
            win_rate=win_rate,
            num_trades=trades,
            final_equity=final_equity,
            fee_drag=fee_drag,
            liquidated=liquidated,
            equity_curve=equity_curve,
            stats={
                "open_position_qty": pos_qty,
                "avg_entry": avg_entry,
                "max_adds_hit": max_adds_hit,
                "end_price": final_price,
                "avg_cycle_pnl": float(np.mean(cycle_pnls)) if cycle_pnls else 0.0,
                "cycle_pnls_sum": float(np.sum(cycle_pnls)) if cycle_pnls else 0.0,
                "max_margin_used": max_margin_used,
                "margin_locked_end": margin_locked,
                "stop_outs": stop_outs,
                "stop_out_pnl_sum": float(stop_out_pnl_sum),
                "stop_loss_pct": sl_pct if sl_pct > 0 else None,
                "stop_loss_mode": "investment_drawdown" if sl_pct > 0 else None,
            },
        )
