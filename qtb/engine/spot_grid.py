"""Tick-driven spot moving-grid engine.

Fills come from the official Gate deals tape, not OHLC wicks:

- Resting buy at L fills when a print trades at or below L.
- Buys are hung only strictly below the last hang / shift reference
  (the robot never bids through the market on the opening print).
- Resting sell at L fills when a print trades at or above L.
- Gate 突破移动: last price must exceed the band by at least one grid
  spacing; then the whole window slides one grid (not re-centered on last).
  See https://www.gate.com/zh/help/bots/spot-grid/36108

Each grid rung keeps its own buy price. Harvest is sell − that buy − fees,
not mark-to-market versus the portfolio average. The native robot does not
flatten on drawdown; halt is opt-in only.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd

from qtb.costs.fees import fee_preset
from qtb.costs.model import CostModel
from qtb.data.gatedata import audit_deals_tape
from qtb.engine.backtest import BacktestResult, compute_metrics
from qtb.engine.types import Book, Trade
from qtb.risk.exits import RiskConfig, hit_investment_sl, hit_max_dd_stop
from qtb.strategies.moving_grid import (
    MovingGridStrategy,
    build_moving_levels,
    count_pct_crosses,
    shift_levels,
)


def _equity(quote: float, base: float, price: float) -> float:
    return quote + base * price


@dataclass
class _Lot:
    qty: float
    cost: float
    buy_fee: float


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
        eq_sec = float(strat_cfg.get("equity_sample_seconds") or 60.0)
        self.equity_sample = pd.Timedelta(seconds=max(eq_sec, 1.0))

        self.quote = self.strategy.quote_capital
        self.base = 0.0
        self.leftover_lots: list[_Lot] = []
        self.lots: dict[int, _Lot] = {}
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
        self._hang_ref = 0.0
        self._resting_buys: set[int] = set()

    def _open_lots(self) -> list[_Lot]:
        return list(self.lots.values()) + self.leftover_lots

    def _leftover_base(self) -> float:
        return float(sum(lot.qty for lot in self.leftover_lots))

    def _grid_step(self) -> float:
        if len(self.levels) > 1:
            step = float(np.median(np.diff(self.levels)))
            if step > 0:
                return step
        return float(self.strategy.spacing_pct) * float(self.levels[0] if len(self.levels) else 1.0)

    def _lot_take_profit(self, lot: _Lot) -> float:
        """+1 grid from this lot's own cost. 等差 uses the constant spacing q."""
        if self.strategy.spacing_mode == "arithmetic":
            return lot.cost + self._grid_step()
        return lot.cost * (1.0 + float(self.strategy.spacing_pct))

    def _rebuild_avg(self) -> None:
        held = self._open_lots()
        qty = float(sum(lot.qty for lot in held))
        if qty <= 1e-16:
            self.book.avg_entry = 0.0
            return
        self.book.avg_entry = float(sum(lot.qty * lot.cost for lot in held) / qty)

    def _sync_book(self, mark: float) -> None:
        self.book.wallet = self.quote
        self.book.qty = self.base
        self.book.lots = {i: lot.qty for i, lot in self.lots.items()}
        self._rebuild_avg()

    def _inventory_mtm(self, mark: float) -> float:
        return float(sum(lot.qty * (mark - lot.cost) for lot in self._open_lots()))

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
        self.quote -= notional + fee
        self.base += qty
        self.lots[idx] = _Lot(qty=qty, cost=fill_px, buy_fee=fee)
        self.book.last_entry = fill_px
        self._sync_book(mark)
        self._record(ts, "buy", fill_px, qty, fee, "grid_buy", 0.0, mark)
        return True

    def _close_lot(self, lot: _Lot, raw_px: float, ts: Any, mark: float, reason: str) -> float:
        qty = min(lot.qty, self.base)
        if qty <= 0:
            return 0.0
        fill_px = self.cost.fill_price(raw_px, "sell")
        notional = qty * fill_px
        sell_fee = self.cost.fee(notional)
        buy_fee = lot.buy_fee * (qty / lot.qty) if lot.qty > 0 else 0.0
        # Grid income = this rung's sell − its own buy − both fees.
        realized = qty * (fill_px - lot.cost) - sell_fee - buy_fee
        self.quote += notional - sell_fee
        self.base -= qty
        if self.base <= 1e-16:
            self.base = 0.0
        if reason == "grid_sell_tp":
            self.book.cycle_id += 1
            self.book.cycles += 1
            self.book.cycle_pnls.append(realized)
            if realized > 0:
                self.book.wins += 1
        self._sync_book(mark)
        self._record(ts, "sell", fill_px, qty, sell_fee, reason, realized, mark)
        return realized

    def _rehang_buys(self, ref: float) -> None:
        """Rest buys only strictly below the hang reference (native robot never bids through last)."""
        self._hang_ref = float(ref)
        n = len(self.levels)
        self._resting_buys = {
            i
            for i in range(max(n - 1, 0))
            if i not in self.lots and float(self.levels[i]) < self._hang_ref - 1e-12
        }

    def _fill_against_print(self, px: float, ts: Any) -> None:
        n = len(self.levels)
        if n < 2:
            return
        min_quote = self.order_size_quote * 1.01
        # Inventory TPs first so a bounce frees quote before new dip-buys.
        sell_idxs = [i for i in list(self.lots) if i + 1 < n and px >= float(self.levels[i + 1])]
        sell_idxs.sort()
        for i in sell_idxs:
            lot = self.lots.pop(i)
            self._close_lot(lot, float(self.levels[i + 1]), ts, px, "grid_sell_tp")
            if float(self.levels[i]) < self._hang_ref - 1e-12:
                self._resting_buys.add(i)
        still: list[_Lot] = []
        for lot in self.leftover_lots:
            tp = self._lot_take_profit(lot)
            if px >= tp:
                self._close_lot(lot, tp, ts, px, "grid_sell_leftover")
            else:
                still.append(lot)
        self.leftover_lots = still
        buy_idxs = [
            i
            for i in self._resting_buys
            if i not in self.lots and px <= float(self.levels[i]) + 1e-12
        ]
        buy_idxs.sort(reverse=True)
        for i in buy_idxs:
            if self.quote < min_quote:
                break
            if self._buy_level(i, ts, px):
                self._resting_buys.discard(i)

    def _maybe_shift(self, px: float, ts: Any | None = None) -> int:
        """Gate 突破移动: slide the whole window one grid when last is ≥1 grid outside."""
        if not self.shift_on_exit or len(self.levels) < 2:
            return 0
        moved = 0
        max_buy = int(self.strategy.grid_count) - 1
        while True:
            step = self._grid_step()
            hi = float(self.levels[-1])
            if px + 1e-12 < hi + step:
                break
            if self.strategy.stop_move_up is not None and hi >= float(self.strategy.stop_move_up):
                break
            abandoned = self.lots.get(0)
            self.lots = {i - 1: lot for i, lot in self.lots.items() if i > 0}
            if abandoned is not None:
                self.leftover_lots.append(abandoned)
            self.levels = shift_levels(
                self.levels, "up", self.strategy.spacing_pct, self.strategy.spacing_mode
            )
            self.strategy.levels = self.levels
            self.shifts += 1
            moved += 1
        while True:
            step = self._grid_step()
            lo = float(self.levels[0])
            if px - 1e-12 > lo - step:
                break
            if self.strategy.stop_move_down is not None and lo <= float(self.strategy.stop_move_down):
                break
            abandoned = self.lots.get(max_buy)
            self.lots = {i + 1: lot for i, lot in self.lots.items() if i < max_buy}
            if abandoned is not None:
                self.leftover_lots.append(abandoned)
            self.levels = shift_levels(
                self.levels, "down", self.strategy.spacing_pct, self.strategy.spacing_mode
            )
            self.strategy.levels = self.levels
            self.shifts += 1
            moved += 1
        if moved:
            self._rehang_buys(px)
        return moved

    def _flatten(self, px: float, ts: Any, reason: str) -> None:
        open_lots = list(self.lots.values()) + self.leftover_lots
        self.lots.clear()
        self.leftover_lots.clear()
        for lot in open_lots:
            self._close_lot(lot, px, ts, px, reason)
        self.halted = True
        if "sl" in reason or "stop" in reason:
            self.book.stop_outs += 1

    def _risk(self, px: float, ts: Any, eq: float) -> None:
        if self.book.qty > 0:
            upnl = self._inventory_mtm(px)
            if upnl < self.book.max_float_loss:
                self.book.max_float_loss = upnl
        # Opt-in only. Native moving grid keeps running; do not default-halt.
        if self.risk.investment_sl_pct and hit_investment_sl(
            eq - self.book.initial, self.book.initial, self.risk.investment_sl_pct
        ):
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
            mid,
            self.strategy.grid_count,
            self.strategy.spacing_pct,
            self.strategy.spacing_mode,
            range_up_pct=self.strategy.range_up_pct,
            range_down_pct=self.strategy.range_down_pct,
        )
        self.strategy.levels = self.levels
        self._rehang_buys(mid)

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
                self._maybe_shift(px, ts)
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
        grid_harvest = float(sum(t.realized_pnl for t in self.trades if t.reason == "grid_sell_tp"))
        leftover_harvest = float(sum(t.realized_pnl for t in self.trades if t.reason == "grid_sell_leftover"))
        range_exit_pnl = float(
            sum(t.realized_pnl for t in self.trades if t.reason == "range_exit_rebalance")
        )
        other_realized = float(
            sum(
                t.realized_pnl
                for t in self.trades
                if t.side == "sell"
                and t.reason not in {"grid_sell_tp", "grid_sell_leftover", "range_exit_rebalance"}
            )
        )
        inventory_mtm = self._inventory_mtm(last_px)
        residual_buy_fees = float(sum(lot.buy_fee for lot in self._open_lots()))
        end_eq = float(equity_curve[-1]) if equity_curve else self.book.initial
        net = end_eq - self.book.initial
        explained = (
            grid_harvest
            + leftover_harvest
            + range_exit_pnl
            + other_realized
            + inventory_mtm
            - residual_buy_fees
        )
        tape = audit_deals_tape(work)
        metrics.update(tape)
        tp_n = int(sum(1 for t in self.trades if t.reason == "grid_sell_tp"))
        left_n = int(sum(1 for t in self.trades if t.reason == "grid_sell_leftover"))
        n_rounds = tp_n + left_n
        income = grid_harvest + leftover_harvest
        metrics["grid_harvest"] = round(grid_harvest, 4)
        metrics["leftover_harvest"] = round(leftover_harvest, 4)
        metrics["grid_income"] = round(income, 4)
        metrics["range_exit_pnl"] = round(range_exit_pnl, 4)
        metrics["grid_rounds_tp"] = tp_n
        metrics["grid_rounds_leftover"] = left_n
        metrics["avg_harvest_per_round"] = round(income / n_rounds, 6) if n_rounds else 0.0
        metrics["grid_step"] = round(self._grid_step(), 8)
        metrics["quote_in_inventory"] = round(self.base * last_px, 4)
        step_pct = float(self.strategy.spacing_pct)
        crosses = count_pct_crosses(work["price"].to_numpy(), step_pct)
        crosses_10bps = count_pct_crosses(work["price"].to_numpy(), 0.001)
        metrics["tape_up_crosses"] = int(crosses["up_crosses"])
        metrics["tape_down_crosses"] = int(crosses["down_crosses"])
        metrics["tape_up_crosses_10bps"] = int(crosses_10bps["up_crosses"])
        metrics["tape_down_crosses_10bps"] = int(crosses_10bps["down_crosses"])
        metrics["inventory_mtm"] = round(inventory_mtm, 4)
        metrics["residual_buy_fees"] = round(residual_buy_fees, 4)
        metrics["pnl_explained"] = round(explained, 4)
        metrics["pnl_identity_gap"] = round(net - explained, 4)
        metrics["end_quote"] = round(self.quote, 4)
        metrics["end_base"] = round(self.base, 8)
        metrics["grid_shifts"] = self.shifts
        metrics["leftover_base"] = round(self._leftover_base(), 8)
        metrics["n_prints"] = n_prints
        metrics["feed"] = "deals"
        metrics["halted"] = self.halted
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
                "buys rest only below last hang; never bid through the opening print",
                "no default drawdown halt; grid harvest is per-rung sell-buy-fees",
                f"grid_count={self.strategy.grid_count} spacing_pct={self.strategy.spacing_pct} "
                f"mode={self.strategy.spacing_mode} range=±{self.strategy.range_up_pct}/{self.strategy.range_down_pct}",
                f"prints={n_prints} fills={len(self.trades)} shifts={self.shifts} "
                f"harvest={grid_harvest:.4f} tape_ok={tape.get('tape_ok')} "
                f"identity_gap={net - explained:.6f}",
            ],
        )


def run_spot_moving_grid(cfg: dict[str, Any], deals: pd.DataFrame) -> BacktestResult:
    return SpotMovingGridEngine(cfg).run(deals)
