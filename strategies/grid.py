"""Spot grid trading simulator (cash-flow style, not arb)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from fees import FeeConfig, fee_on_notional


@dataclass
class GridParams:
    """Arithmetic spot grid parameters."""

    lower: float | None = None  # if None, derived from data
    upper: float | None = None
    grid_count: int = 20
    spacing_pct: float | None = None  # alternative to grid_count over [lower,upper]
    order_size_quote: float = 50.0  # USDT per grid level
    initial_quote: float = 5000.0
    use_maker: bool = True  # assume limit fills at grid prices
    fee_as_maker: bool = True


@dataclass
class GridResult:
    params: GridParams
    fee_config: FeeConfig
    net_pnl: float
    gross_pnl: float
    total_fees: float
    max_drawdown: float
    max_drawdown_pct: float
    cycles: int  # completed buy->sell round trips
    win_rate: float
    num_trades: int
    final_equity: float
    fee_drag: float  # total_fees / max(abs(gross_pnl), 1e-9)
    equity_curve: list[float] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        return {
            "strategy": "spot_grid",
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


class SpotGridSimulator:
    """
    Classic arithmetic spot grid:
    - Place buy limits on lower levels, sell limits on upper levels relative to mid.
    - On each candle: if low touches a buy level with quote available -> buy base.
      If high touches a sell level with inventory -> sell base.
    - Round-trip profit = spacing * size minus fees.
    """

    def __init__(self, params: GridParams, fee_config: FeeConfig):
        self.params = params
        self.fee_config = fee_config

    def _fee_rate(self) -> float:
        if self.params.fee_as_maker:
            return self.fee_config.effective_maker
        return self.fee_config.effective_taker

    def _build_levels(self, prices: pd.Series) -> np.ndarray:
        p = self.params
        lower = p.lower if p.lower is not None else float(prices.min()) * 0.98
        upper = p.upper if p.upper is not None else float(prices.max()) * 1.02
        if upper <= lower:
            mid = float(prices.iloc[0])
            lower, upper = mid * 0.9, mid * 1.1

        if p.spacing_pct is not None and p.spacing_pct > 0:
            # geometric-ish spacing from mid; still produce arithmetic levels via count
            mid = (lower + upper) / 2
            step = mid * p.spacing_pct
            n = max(2, int((upper - lower) / step))
            levels = np.linspace(lower, upper, n + 1)
        else:
            levels = np.linspace(lower, upper, p.grid_count + 1)
        return levels

    def run(self, df: pd.DataFrame) -> GridResult:
        """
        df must have columns: open, high, low, close (and optionally timestamp).
        """
        required = {"open", "high", "low", "close"}
        if not required.issubset(df.columns):
            raise ValueError(f"OHLCV missing columns: {required - set(df.columns)}")

        prices = df["close"].astype(float)
        highs = df["high"].astype(float).values
        lows = df["low"].astype(float).values
        closes = prices.values

        levels = self._build_levels(prices)
        n_levels = len(levels)
        # inventory at each grid interval (buy at level i, sell at level i+1)
        # Track base lots bought at each buy level index
        lots: dict[int, float] = {}  # level_idx -> base amount held from buys at that level
        quote = float(self.params.initial_quote)
        base = 0.0
        fee_rate = self._fee_rate()
        order_quote = self.params.order_size_quote

        total_fees = 0.0
        cycles = 0
        wins = 0
        trades = 0
        equity_curve: list[float] = []
        peak = quote
        max_dd = 0.0
        max_dd_pct = 0.0
        round_trip_pnls: list[float] = []

        # Start: assume we hold cash; buy when price drops to lower grids
        start_price = float(closes[0])

        for i in range(len(closes)):
            lo, hi, cl = float(lows[i]), float(highs[i]), float(closes[i])

            # Process buys: price dipped to level (from high to low scan for realism)
            for idx in range(n_levels - 1, -1, -1):
                lvl = float(levels[idx])
                if lo <= lvl <= hi or (i > 0 and float(closes[i - 1]) > lvl >= lo):
                    # Buy opportunity at this level if we don't already hold a lot here
                    # and level is below current mid bias (buy low)
                    if idx not in lots and quote >= order_quote and lvl < cl * 1.001:
                        # only buy if level is at or below close / touched from above
                        if lo <= lvl:
                            base_amt = order_quote / lvl
                            fee = fee_on_notional(order_quote, fee_rate)
                            if quote >= order_quote + fee:
                                quote -= order_quote + fee
                                base += base_amt
                                lots[idx] = base_amt
                                total_fees += fee
                                trades += 1

            # Process sells: sell lots at next higher level
            for idx in list(lots.keys()):
                sell_lvl_idx = idx + 1
                if sell_lvl_idx >= n_levels:
                    continue
                sell_lvl = float(levels[sell_lvl_idx])
                if hi >= sell_lvl:
                    base_amt = lots[idx]
                    proceeds = base_amt * sell_lvl
                    fee = fee_on_notional(proceeds, fee_rate)
                    cost_basis = base_amt * float(levels[idx])
                    pnl = proceeds - cost_basis - fee
                    # buy fee was already paid; approximate round-trip
                    buy_fee_approx = fee_on_notional(cost_basis, fee_rate)
                    net_rt = proceeds - cost_basis - fee  # sell fee; buy fee already in total
                    quote += proceeds - fee
                    base -= base_amt
                    del lots[idx]
                    total_fees += fee
                    trades += 1
                    cycles += 1
                    round_trip_pnls.append(net_rt - buy_fee_approx)
                    if net_rt - buy_fee_approx > 0:
                        wins += 1

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

        final_price = float(closes[-1])
        final_equity = quote + base * final_price
        # Liquidate remaining base for PnL reporting (mark-to-market, no extra fee on MTM)
        initial = self.params.initial_quote
        net_pnl = final_equity - initial
        gross_pnl = net_pnl + total_fees
        win_rate = (wins / cycles) if cycles > 0 else 0.0
        fee_drag = total_fees / max(abs(gross_pnl), 1e-9)

        return GridResult(
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
                "levels": len(levels),
                "lower": float(levels[0]),
                "upper": float(levels[-1]),
                "open_lots": len(lots),
                "start_price": start_price,
                "end_price": final_price,
                "avg_cycle_pnl": float(np.mean(round_trip_pnls)) if round_trip_pnls else 0.0,
            },
        )
