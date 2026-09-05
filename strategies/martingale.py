"""Spot Martingale simulator (cash-flow style, not leverage futures)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from fees import FeeConfig, fee_on_notional


@dataclass
class MartingaleParams:
    """Spot Martingale: add on dips, take profit on rebound."""

    base_order_quote: float = 100.0
    multiplier: float = 1.5  # each add size *= multiplier
    add_drop_pct: float = 0.02  # add when price drops X% from last entry
    take_profit_pct: float = 0.015  # TP from average cost
    max_adds: int = 5  # max additional buys after base (total fills = max_adds+1)
    initial_quote: float = 5000.0
    fee_as_maker: bool = False  # market-style adds often taker; configurable
    cooldown_bars: int = 0


@dataclass
class MartingaleResult:
    params: MartingaleParams
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
    equity_curve: list[float] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        return {
            "strategy": "spot_martingale",
            "fee_label": self.fee_config.label,
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
            "rebate_rate": self.fee_config.rebate_rate,
            "eff_maker": round(self.fee_config.effective_maker, 8),
            "eff_taker": round(self.fee_config.effective_taker, 8),
        }


class SpotMartingaleSimulator:
    """
    Spot-only Martingale:
    1. Open base buy with base_order_quote.
    2. If price drops add_drop_pct from last fill price, add next size *= multiplier.
    3. When price recovers take_profit_pct above average cost, sell all base.
    4. Cap adds at max_adds. If cash insufficient, skip add.
    No leverage, no shorts — cash-flow research only.
    """

    def __init__(self, params: MartingaleParams, fee_config: FeeConfig):
        self.params = params
        self.fee_config = fee_config

    def _fee_rate(self) -> float:
        if self.params.fee_as_maker:
            return self.fee_config.effective_maker
        return self.fee_config.effective_taker

    def run(self, df: pd.DataFrame) -> MartingaleResult:
        required = {"open", "high", "low", "close"}
        if not required.issubset(df.columns):
            raise ValueError(f"OHLCV missing columns: {required - set(df.columns)}")

        highs = df["high"].astype(float).values
        lows = df["low"].astype(float).values
        closes = df["close"].astype(float).values

        p = self.params
        fee_rate = self._fee_rate()
        quote = float(p.initial_quote)
        base = 0.0
        avg_cost = 0.0
        last_entry = 0.0
        adds = 0  # completed adds after base (0 = only base, or flat)
        in_position = False
        next_order_quote = p.base_order_quote
        cooldown = 0

        total_fees = 0.0
        cycles = 0
        wins = 0
        trades = 0
        equity_curve: list[float] = []
        peak = quote
        max_dd = 0.0
        max_dd_pct = 0.0
        cycle_pnls: list[float] = []
        max_adds_hit = 0

        def buy(price: float, order_q: float) -> bool:
            nonlocal quote, base, avg_cost, last_entry, total_fees, trades
            fee = fee_on_notional(order_q, fee_rate)
            need = order_q + fee
            if quote < need or order_q <= 0 or price <= 0:
                return False
            amt = order_q / price
            new_cost = avg_cost * base + order_q
            base += amt
            avg_cost = new_cost / base if base > 0 else 0.0
            quote -= need
            last_entry = price
            total_fees += fee
            trades += 1
            return True

        def sell_all(price: float) -> float:
            nonlocal quote, base, avg_cost, last_entry, total_fees, trades, in_position
            nonlocal next_order_quote, adds
            if base <= 0:
                return 0.0
            proceeds = base * price
            fee = fee_on_notional(proceeds, fee_rate)
            cost = avg_cost * base
            pnl = proceeds - fee - cost
            quote += proceeds - fee
            total_fees += fee
            trades += 1
            base = 0.0
            avg_cost = 0.0
            last_entry = 0.0
            in_position = False
            next_order_quote = p.base_order_quote
            adds = 0
            return pnl

        for i in range(len(closes)):
            lo, hi, cl = float(lows[i]), float(highs[i]), float(closes[i])

            if cooldown > 0:
                cooldown -= 1
                mtm = quote + base * cl
                equity_curve.append(mtm)
                if mtm > peak:
                    peak = mtm
                dd = peak - mtm
                if dd > max_dd:
                    max_dd = dd
                dd_pct = dd / peak if peak > 0 else 0.0
                if dd_pct > max_dd_pct:
                    max_dd_pct = dd_pct
                continue

            if not in_position:
                # Open at close (or mid of bar)
                entry = cl
                if buy(entry, next_order_quote):
                    in_position = True
                    adds = 0
                    next_order_quote = p.base_order_quote * p.multiplier
            else:
                # Check TP on high
                tp_price = avg_cost * (1.0 + p.take_profit_pct)
                if hi >= tp_price and base > 0:
                    pnl = sell_all(tp_price)
                    cycles += 1
                    cycle_pnls.append(pnl)
                    if pnl > 0:
                        wins += 1
                    cooldown = p.cooldown_bars
                else:
                    # Check add on low
                    trigger = last_entry * (1.0 - p.add_drop_pct)
                    if lo <= trigger and adds < p.max_adds:
                        add_price = trigger  # assume fill at trigger
                        order_q = next_order_quote
                        if buy(add_price, order_q):
                            adds += 1
                            max_adds_hit = max(max_adds_hit, adds)
                            next_order_quote = p.base_order_quote * (p.multiplier ** (adds + 1))

            mtm = quote + base * cl
            equity_curve.append(mtm)
            if mtm > peak:
                peak = mtm
            dd = peak - mtm
            if dd > max_dd:
                max_dd = dd
            dd_pct = dd / peak if peak > 0 else 0.0
            if dd_pct > max_dd_pct:
                max_dd_pct = dd_pct

        # Mark-to-market remaining position
        final_price = float(closes[-1])
        final_equity = quote + base * final_price
        initial = p.initial_quote
        net_pnl = final_equity - initial
        gross_pnl = net_pnl + total_fees
        win_rate = (wins / cycles) if cycles > 0 else 0.0
        fee_drag = total_fees / max(abs(gross_pnl), 1e-9)

        return MartingaleResult(
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
            equity_curve=equity_curve,
            stats={
                "open_position_base": base,
                "avg_cost": avg_cost,
                "max_adds_hit": max_adds_hit,
                "end_price": final_price,
                "avg_cycle_pnl": float(np.mean(cycle_pnls)) if cycle_pnls else 0.0,
                "cycle_pnls_sum": float(np.sum(cycle_pnls)) if cycle_pnls else 0.0,
            },
        )
