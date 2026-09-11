"""Tick-driven spot moving-grid engine.

Fills come from the official Gate deals tape, not OHLC wicks:

- Resting buy at L fills when a print trades at or below L.
- Resting sell at L fills when a print trades at or above L.
- A print that exits the band shifts the window by one grid and re-hangs
  for *later* prints (the same print does not fill newly hung orders).

Candle open→low→high→close paths are intentionally unused: they invent
touches that never printed.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from qtb.costs.fees import fee_preset
from qtb.costs.model import CostModel
from qtb.engine.backtest import BacktestResult, compute_metrics
from qtb.engine.types import Book, Trade
from qtb.risk.exits import RiskConfig, hit_investment_sl, hit_max_dd_stop
from qtb.strategies.moving_grid import (
    MovingGridStrategy,
    build_moving_levels,
    remap_lots_shift_down,
    remap_lots_shift_up,
    shift_levels,
)


def _equity(quote: float, base: float, price: float) -> float:
    return quote + base * price


class SpotMovingGridEngine:
    def __init__(self, cfg: dict[str, Any]):
        strat_cfg = dict(cfg.get("strategy") or {})
        self.strategy = MovingGridStrategy(strat_cfg)
        costs_cfg = cfg.get("costs") or {}
        fee = fee_preset(
            market=costs_cfg.get("market") or cfg.get("market") or "spot",
            vip_tier=int(costs_cfg.get("vip_tier") or 7),
            rebate_rate=costs_cfg.get("rebate_rate"),
        )
        self.cost = CostModel(
            fee_config=fee,
            slippage_bps=float(costs_cfg.get("slippage_bps") or 0.0),
            use_maker=bool(costs_cfg.get("use_maker", True)),
            quanto=float(costs_cfg.get("quanto") or 1e-8),
            min_order_size=float(costs_cfg.get("min_order_size") or 1.0),
            min_notional=float(costs_cfg.get("min_notional") or 1.0),
            apply_funding=False,
        )
        self.risk = RiskConfig.from_dict(
            cfg.get("risk") or {},
            maintenance_rate=float(costs_cfg.get("maintenance_rate") or 0.0),
        )
        self.symbol = str(cfg.get("symbol") or "ETH3L_USDT")
        self.interval = str(cfg.get("interval") or "tick")
        self.order_size_quote = self.strategy.order_size_quote
        self.shift_on_exit = self.strategy.shift_on_exit
        self.fill_policy = str(strat_cfg.get("fill_policy") or "last_touch").strip().lower()
        eq_sec = float(strat_cfg.get("equity_sample_seconds") or 60.0)
        self.equity_sample = pd.Timedelta(seconds=max(eq_sec, 1.0))

        self.quote = self.strategy.quote_capital
        self.base = 0.0
        self.leftover = 0.0
        self.lots: dict[int, float] = {}
        self.levels = np.asarray([], dtype=float)
        self.shifts = 0
        self.rejected = 0
        self.halted = False
        self.trades: list[Trade] = []
        self._trade_id = 0
        self.book = Book(
            name="spot",
            direction="long",
            initial=self.strategy.quote_capital,
            wallet=self.strategy.quote_capital,
        )
        self._peak = self.strategy.quote_capital
        self._last_eq_ts: pd.Timestamp | None = None

    def _sync_book(self, mark: float) -> None:
        self.book.wallet = self.quote
        self.book.qty = self.base
        self.book.lots = dict(self.lots)

    def _record(
        self,
        ts: Any,
        side: str,
        price: float,
        qty: float,
        fee: float,
        reason: str,
        realized: float,
        mark: float,
    ) -> None:
        self._trade_id += 1
        eq = _equity(self.quote, self.base, mark)
        self.trades.append(
            Trade(
                trade_id=self._trade_id,
                timestamp=ts,
                symbol=self.symbol,
                book="spot",
                side=side,
                price=price,
                qty=qty,
                notional=qty * price,
                fee=fee,
                slippage=0.0,
                reason=reason,
                realized_pnl=realized,
                equity_after=eq,
                cycle_id=self.book.cycle_id,
                direction="long",
            )
        )

    def _buy_level(self, idx: int, ts: Any, mark: float) -> bool:
        raw = float(self.levels[idx])
        fill_px = self.cost.fill_price(raw, "buy")
        qty = self.cost.size_from_notional(self.order_size_quote, fill_px)
        if not self.cost.accept_order(qty, fill_px):
            self.rejected += 1
            return False
        notional = qty * fill_px
        fee = self.cost.fee(notional)
        if self.quote + 1e-12 < notional + fee:
            self.rejected += 1
            return False
        new_cost = self.book.avg_entry * self.base + notional
        self.quote -= notional + fee
        self.base += qty
        self.lots[idx] = self.lots.get(idx, 0.0) + qty
        self.book.avg_entry = new_cost / self.base if self.base > 0 else 0.0
        self.book.last_entry = fill_px
        self._sync_book(mark)
        self._record(ts, "buy", fill_px, qty, fee, "grid_buy", 0.0, mark)
        return True

    def _sell_qty(self, qty: float, raw_px: float, ts: Any, mark: float, reason: str, level_idx: int | None) -> bool:
        qty = min(qty, self.base)
        if qty <= 0:
            return False
        fill_px = self.cost.fill_price(raw_px, "sell")
        notional = qty * fill_px
        fee = self.cost.fee(notional)
        raw_pnl = qty * (fill_px - self.book.avg_entry) if self.book.avg_entry > 0 else 0.0
        realized = raw_pnl - fee
        self.quote += notional - fee
        self.base -= qty
        if level_idx is not None:
            self.lots.pop(level_idx, None)
        if self.base <= 1e-16:
            self.base = 0.0
            self.book.avg_entry = 0.0
        self.book.cycle_id += 1
        self.book.cycles += 1
        self.book.cycle_pnls.append(realized)
        if realized > 0:
            self.book.wins += 1
        self._sync_book(mark)
        self._record(ts, "sell", fill_px, qty, fee, reason, realized, mark)
        return True

    def _fill_against_print(self, px: float, ts: Any) -> None:
        n = len(self.levels)
        if n < 2:
            return
        # Buys: highest crossed first (tape traded down through them).
        buy_idxs = [i for i in range(n - 1) if i not in self.lots and px <= float(self.levels[i])]
        buy_idxs.sort(reverse=True)
        for i in buy_idxs:
            self._buy_level(i, ts, px)
        # Assigned sells: lowest TP first.
        sell_idxs = [i for i in list(self.lots) if i + 1 < n and px >= float(self.levels[i + 1])]
        sell_idxs.sort()
        for i in sell_idxs:
            self._sell_qty(self.lots[i], float(self.levels[i + 1]), ts, px, "grid_sell_tp", i)
        # Leftover from abandoned lots: sell at the new lowest TP only.
        if self.leftover > 0 and n > 1 and px >= float(self.levels[1]):
            sold = self.leftover
            self.leftover = 0.0
            self._sell_qty(sold, float(self.levels[1]), ts, px, "grid_sell_leftover", None)

    def _maybe_shift(self, px: float) -> int:
        if not self.shift_on_exit or len(self.levels) < 2:
            return 0
        moved = 0
        max_buy = int(self.strategy.grid_count) - 1
        # Same print can exit several grids; shift one at a time, no new fills.
        while px > float(self.levels[-1]) + 1e-12:
            self.lots, abandoned = remap_lots_shift_up(self.lots)
            self.leftover += abandoned
            self.levels = shift_levels(
                self.levels, "up", self.strategy.spacing_pct, self.strategy.spacing_mode
            )
            self.shifts += 1
            moved += 1
        while px < float(self.levels[0]) - 1e-12:
            self.lots, abandoned = remap_lots_shift_down(self.lots, max_buy)
            self.leftover += abandoned
            self.levels = shift_levels(
                self.levels, "down", self.strategy.spacing_pct, self.strategy.spacing_mode
            )
            self.shifts += 1
            moved += 1
        return moved

    def _flatten(self, px: float, ts: Any, reason: str) -> None:
        if self.base > 0:
            self.leftover = 0.0
            qty = self.base
            self.lots.clear()
            self._sell_qty(qty, px, ts, px, reason, None)
        self.halted = True
        if "sl" in reason or "stop" in reason:
            self.book.stop_outs += 1

    def _risk(self, px: float, ts: Any, eq: float) -> None:
        if self.book.qty > 0:
            upnl = self.base * (px - self.book.avg_entry) if self.book.avg_entry > 0 else 0.0
            if upnl < self.book.max_float_loss:
                self.book.max_float_loss = upnl
        if self.risk.investment_sl_pct and hit_investment_sl(
            eq - self.book.initial, self.book.initial, self.risk.investment_sl_pct
        ):
            # hit_investment_sl expects uPnL; equity drawdown == eq - initial.
            self._flatten(px, ts, "investment_sl")
            return
        if eq > self._peak:
            self._peak = eq
        dd_pct = (self._peak - eq) / self._peak if self._peak > 0 else 0.0
        if self.risk.max_drawdown_stop_pct and hit_max_dd_stop(dd_pct, self.risk.max_drawdown_stop_pct):
            self._flatten(px, ts, "max_dd_stop")

    def run(self, deals: pd.DataFrame) -> BacktestResult:
        if deals is None or deals.empty:
            raise ValueError("moving_grid requires a non-empty deals tape (feed=deals)")
        if "price" not in deals.columns:
            raise ValueError("deals frame must have a price column")
        work = deals.sort_values(
            [c for c in ("timestamp", "dealid") if c in deals.columns],
            kind="mergesort",
        ).reset_index(drop=True)
        mid = float(work["price"].iloc[0])
        self.levels = build_moving_levels(
            mid, self.strategy.grid_count, self.strategy.spacing_pct, self.strategy.spacing_mode
        )
        self.strategy.levels = self.levels

        equity_curve: list[float] = []
        dd_curve: list[float] = []
        pos_curve: list[float] = []
        timestamps: list[Any] = []

        def _sample(ts: Any, px: float, force: bool = False) -> None:
            t = pd.Timestamp(ts)
            if (
                not force
                and self._last_eq_ts is not None
                and t - self._last_eq_ts < self.equity_sample
            ):
                return
            eq = _equity(self.quote, self.base, px)
            if eq > self._peak:
                self._peak = eq
            equity_curve.append(eq)
            dd_curve.append(self._peak - eq)
            pos_curve.append(self.base)
            timestamps.append(t)
            self._last_eq_ts = t

        n_prints = 0
        for row in work.itertuples(index=False):
            px = float(row.price)
            ts = row.timestamp if hasattr(row, "timestamp") else n_prints
            n_prints += 1
            if not self.halted:
                n_before = self._trade_id
                self._fill_against_print(px, ts)
                self._maybe_shift(px)
                eq = _equity(self.quote, self.base, px)
                self._risk(px, ts, eq)
                _sample(ts, px, force=self._trade_id > n_before)
            else:
                _sample(ts, px, force=False)

        last_px = float(work["price"].iloc[-1])
        last_ts = work["timestamp"].iloc[-1] if "timestamp" in work.columns else n_prints
        self._sync_book(last_px)
        _sample(last_ts, last_px, force=True)

        metrics = compute_metrics(
            equity_curve,
            timestamps,
            self.trades,
            {"spot": self.book},
            self.book.initial,
            funding=0.0,
            rejected=self.rejected,
            min_cushion=1.0,
        )
        metrics["grid_shifts"] = self.shifts
        metrics["leftover_base"] = round(self.leftover, 8)
        metrics["n_prints"] = n_prints
        metrics["feed"] = "deals"
        metrics["liquidated"] = False
        metrics["liq_risk"] = 0.0
        return BacktestResult(
            symbol=self.symbol,
            interval=self.interval,
            strategy="moving_grid",
            books={"spot": self.book},
            trades=self.trades,
            equity_curve=equity_curve,
            drawdown_curve=dd_curve,
            position_curve=pos_curve,
            timestamps=list(timestamps),
            metrics=metrics,
            params={
                "leverage": 1.0,
                "strategy": dict(self.strategy.cfg),
                "risk": self.risk.__dict__,
                "costs": {
                    "label": self.cost.fee_config.label,
                    "eff_maker": self.cost.fee_config.effective_maker,
                    "eff_taker": self.cost.fee_config.effective_taker,
                    "slippage_bps": self.cost.slippage_bps,
                    "rebate": self.cost.fee_config.rebate_rate,
                },
                "feed": "deals",
                "n_prints": n_prints,
                "grid_shifts": self.shifts,
            },
            notes=[
                "feed=deals (official Gate tape; no OHLC wick path)",
                f"grid_count={self.strategy.grid_count} spacing_pct={self.strategy.spacing_pct} "
                f"mode={self.strategy.spacing_mode}",
                f"prints={n_prints} fills={len(self.trades)} shifts={self.shifts}",
            ],
        )


def run_spot_moving_grid(cfg: dict[str, Any], deals: pd.DataFrame) -> BacktestResult:
    return SpotMovingGridEngine(cfg).run(deals)
