"""Tick-driven Gate 现货网格 + 突破移动.

Official rules (help 36108 / FAQ 36427):

- Long-only. Split quote into equal grid slices.
- Open 底仓 at last (taker) so sell slots above last can hang.
- Rest buys strictly below last; rest sells strictly above last.
- A filled buy hangs a sell on the next grid up. A filled sell hangs a
  buy on the next grid down. 套利次数 = completed buy→sell cycles.
- 网格利润 = Σ (卖出价 − 该笔买入价) × qty − fees. First sells match
  入场价 (the opening 底仓). Later sells match the previous buy.
- 突破移动: last ≥ 上限 + 一格 → slide the whole window up one grid;
  last ≤ 下限 − 一格 → slide down one grid. Amplitude, grid count and
  q stay fixed. Cancel working orders and re-hang; keep the position.
  Newly hung orders do not fill on the trigger print.
- Arithmetic windows never slide through a non-positive lower bound.
- The native robot does not flatten on drawdown; halt is opt-in only.

Fills come from the official Gate deals tape, not OHLC wicks.
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
    sell_px: float = 0.0


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
        self.lots: list[_Lot] = []
        self.levels = np.asarray([], dtype=float)
        self.q = 0.0
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
        self._resting_buys: list[float] = []

    def _grid_step(self) -> float:
        if self.q > 0:
            return float(self.q)
        if len(self.levels) > 1:
            step = float(np.median(np.diff(self.levels)))
            if step > 0:
                return step
        return float(self.strategy.spacing_pct) * float(self.levels[0] if len(self.levels) else 1.0)

    def _level_list(self) -> list[float]:
        return [float(x) for x in self.levels]

    def _next_level(self, px: float) -> float:
        for lv in self._level_list():
            if lv > px + 1e-12:
                return lv
        return float(px + self._grid_step())

    def _prev_level(self, px: float) -> float:
        prev = None
        for lv in self._level_list():
            if lv < px - 1e-12:
                prev = lv
            else:
                break
        if prev is not None:
            return prev
        return float(max(px - self._grid_step(), 0.0))

    def _slots(self, ref: float) -> tuple[list[float], list[float]]:
        buys = [lv for lv in self._level_list() if lv < float(ref) - 1e-12]
        sells = [lv for lv in self._level_list() if lv > float(ref) + 1e-12]
        return buys, sells

    def _rebuild_avg(self) -> None:
        qty = float(sum(lot.qty for lot in self.lots))
        if qty <= 1e-16:
            self.book.avg_entry = 0.0
            return
        self.book.avg_entry = float(sum(lot.qty * lot.cost for lot in self.lots) / qty)

    def _sync_book(self, mark: float) -> None:
        self.book.wallet = self.quote
        self.book.qty = self.base
        self.book.lots = {i: lot.qty for i, lot in enumerate(self.lots)}
        self._rebuild_avg()

    def _inventory_mtm(self, mark: float) -> float:
        return float(sum(lot.qty * (mark - lot.cost) for lot in self.lots))

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

    def _rehang_sells(self, ref: float) -> None:
        """Cancel working sells and place them on new-window levels above last."""
        _, sell_lvls = self._slots(ref)
        if not sell_lvls:
            step = self._grid_step()
            sell_lvls = [float(ref) + step] if step > 0 else []
        for lot, sp in zip(self.lots, sell_lvls):
            lot.sell_px = sp
        extra = sell_lvls[-1] if sell_lvls else float(ref)
        for lot in self.lots[len(sell_lvls) :]:
            lot.sell_px = extra

    def _rehang_buys(self, ref: float) -> None:
        """Rest buys only strictly below last (never bid through the market)."""
        self._hang_ref = float(ref)
        if self.strategy.sells_only:
            self._resting_buys = []
            return
        buy_lvls, _ = self._slots(ref)
        self._resting_buys = buy_lvls

    def _buy(
        self,
        raw_px: float,
        ts: Any,
        mark: float,
        reason: str,
        *,
        maker: bool,
        sell_px: float,
    ) -> bool:
        fill_px = self.cost.fill_price(raw_px, "buy", is_maker=maker)
        qty = self.cost.size_from_notional(self.order_size_quote, fill_px)
        if not self.cost.accept_order(qty, fill_px):
            self.rejected += 1
            return False
        notional = qty * fill_px
        fee = self.cost.fee(notional, is_maker=maker)
        if self.quote + 1e-12 < notional + fee:
            self.rejected += 1
            return False
        self.quote -= notional + fee
        self.base += qty
        self.lots.append(_Lot(qty=qty, cost=fill_px, buy_fee=fee, sell_px=sell_px))
        self.book.last_entry = fill_px
        self._sync_book(mark)
        self._record(ts, "buy", fill_px, qty, fee, reason, 0.0, mark)
        return True

    def _open_base(self, ts: Any, last: float) -> None:
        """Gate 建仓: market-buy 底仓 for every sell slot above last."""
        if not self.strategy.open_base_inventory:
            return
        _, sell_lvls = self._slots(last)
        for sl in sell_lvls:
            if not self._buy(last, ts, last, "grid_base_buy", maker=False, sell_px=sl):
                break

    def _close_lot(self, lot: _Lot, raw_px: float, ts: Any, mark: float, reason: str) -> float:
        qty = min(lot.qty, self.base)
        if qty <= 0:
            return 0.0
        fill_px = self.cost.fill_price(raw_px, "sell")
        notional = qty * fill_px
        sell_fee = self.cost.fee(notional)
        buy_fee = lot.buy_fee * (qty / lot.qty) if lot.qty > 0 else 0.0
        # FAQ: 单网格差价 = 卖出价 − 买入价(上笔订单); first sell matches 入场价.
        realized = qty * (fill_px - lot.cost) - sell_fee - buy_fee
        self.quote += notional - sell_fee
        self.base -= qty
        if self.base <= 1e-16:
            self.base = 0.0
        self.book.cycle_id += 1
        self.book.cycles += 1
        self.book.cycle_pnls.append(realized)
        if realized > 0:
            self.book.wins += 1
        self._sync_book(mark)
        self._record(ts, "sell", fill_px, qty, sell_fee, reason, realized, mark)
        return realized

    def _fill_against_print(self, px: float, ts: Any) -> None:
        if len(self.levels) < 2:
            return
        min_quote = self.order_size_quote * 1.01
        due = [(lot.sell_px, lot) for lot in self.lots if lot.sell_px > 0 and px >= lot.sell_px]
        due.sort(key=lambda row: row[0])
        for sell_px, lot in due:
            if lot not in self.lots:
                continue
            self.lots.remove(lot)
            self._close_lot(lot, sell_px, ts, px, "grid_sell")
            if self.strategy.sells_only:
                continue
            buy_px = self._prev_level(sell_px)
            if buy_px > 1e-12 and buy_px < self._hang_ref - 1e-12:
                if buy_px not in self._resting_buys:
                    self._resting_buys.append(buy_px)
        buy_lvls = [lv for lv in self._resting_buys if px <= lv + 1e-12]
        buy_lvls.sort(reverse=True)
        for lv in buy_lvls:
            if self.quote < min_quote:
                break
            sell_px = self._next_level(lv)
            if self._buy(lv, ts, px, "grid_buy", maker=True, sell_px=sell_px):
                self._resting_buys = [x for x in self._resting_buys if abs(x - lv) > 1e-12]

    def _can_shift_up(self, px: float) -> bool:
        if not self.strategy.allow_move_up or len(self.levels) < 2:
            return False
        hi = float(self.levels[-1])
        if self.strategy.stop_move_up is not None and hi >= float(self.strategy.stop_move_up):
            return False
        if self.strategy.spacing_mode == "geometric":
            return px + 1e-12 >= hi * (1.0 + float(self.strategy.spacing_pct))
        return px + 1e-12 >= hi + self._grid_step()

    def _can_shift_down(self, px: float) -> bool:
        if not self.strategy.allow_move_down or len(self.levels) < 2:
            return False
        lo = float(self.levels[0])
        if self.strategy.stop_move_down is not None and lo <= float(self.strategy.stop_move_down):
            return False
        step = self._grid_step()
        if self.strategy.spacing_mode == "geometric":
            nxt = lo / (1.0 + float(self.strategy.spacing_pct))
            return px - 1e-12 <= nxt and nxt > 0
        # 等差: 整窗下移一格，下限不能落到 0 或以下。
        if lo - step <= 1e-12:
            return False
        return px - 1e-12 <= lo - step

    def _slide(self, direction: str) -> bool:
        if self.strategy.spacing_mode == "arithmetic":
            step = self._grid_step()
            delta = step if direction == "up" else -step
            nxt = self.levels + delta
            if float(nxt[0]) <= 1e-12:
                return False
            self.levels = nxt
        else:
            self.levels = shift_levels(
                self.levels, direction, self.strategy.spacing_pct, self.strategy.spacing_mode
            )
            if float(self.levels[0]) <= 1e-12:
                return False
        self.strategy.levels = self.levels
        self.q = self._grid_step() if self.strategy.spacing_mode != "arithmetic" else self.q
        self.shifts += 1
        return True

    def _maybe_shift(self, px: float, ts: Any | None = None) -> int:
        """Gate 突破移动: slide one grid when last is ≥1 grid outside the band."""
        if not self.shift_on_exit or len(self.levels) < 2:
            return 0
        moved = 0
        while self._can_shift_up(px):
            if not self._slide("up"):
                break
            moved += 1
        while self._can_shift_down(px):
            if not self._slide("down"):
                break
            moved += 1
        if moved:
            self._rehang_sells(px)
            self._rehang_buys(px)
        return moved

    def _flatten(self, px: float, ts: Any, reason: str) -> None:
        open_lots = list(self.lots)
        self.lots.clear()
        self._resting_buys = []
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
        first_ts = work["timestamp"].iloc[0] if "timestamp" in work.columns else 0
        self.levels = build_moving_levels(
            mid,
            self.strategy.grid_count,
            self.strategy.spacing_pct,
            self.strategy.spacing_mode,
            range_up_pct=self.strategy.range_up_pct,
            range_down_pct=self.strategy.range_down_pct,
        )
        self.strategy.levels = self.levels
        n = max(int(self.strategy.grid_count), 1)
        self.q = (float(self.levels[-1]) - float(self.levels[0])) / n
        self._hang_ref = mid
        self._open_base(first_ts, mid)
        self._rehang_sells(mid)
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
        sells = [t for t in self.trades if t.side == "sell" and t.reason == "grid_sell"]
        other_realized = float(
            sum(t.realized_pnl for t in self.trades if t.side == "sell" and t.reason != "grid_sell")
        )
        grid_profit = float(sum(t.realized_pnl for t in sells))
        win_sells = [t for t in sells if t.realized_pnl > 0]
        loss_sells = [t for t in sells if t.realized_pnl <= 0]
        inventory_mtm = self._inventory_mtm(last_px)
        residual_buy_fees = float(sum(lot.buy_fee for lot in self.lots))
        end_eq = float(equity_curve[-1]) if equity_curve else self.book.initial
        net = end_eq - self.book.initial
        explained = grid_profit + other_realized + inventory_mtm - residual_buy_fees
        tape = audit_deals_tape(work)
        metrics.update(tape)
        arb_rounds = len(sells)
        metrics["grid_profit"] = round(grid_profit, 4)
        metrics["grid_harvest"] = round(grid_profit, 4)
        metrics["leftover_harvest"] = 0.0
        metrics["grid_income"] = round(grid_profit, 4)
        metrics["range_exit_pnl"] = 0.0
        metrics["arb_rounds"] = arb_rounds
        metrics["grid_rounds_tp"] = arb_rounds
        metrics["grid_rounds_leftover"] = 0
        metrics["n_completed_sells"] = arb_rounds
        metrics["n_win_sells"] = len(win_sells)
        metrics["n_loss_sells"] = len(loss_sells)
        metrics["grid_profit_win"] = round(float(sum(t.realized_pnl for t in win_sells)), 4)
        metrics["grid_profit_loss"] = round(float(sum(t.realized_pnl for t in loss_sells)), 4)
        metrics["first_clip_ts"] = str(sells[0].timestamp) if sells else None
        metrics["last_clip_ts"] = str(sells[-1].timestamp) if sells else None
        metrics["avg_harvest_per_round"] = round(grid_profit / arb_rounds, 6) if arb_rounds else 0.0
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
        metrics["unrealized_pnl"] = round(inventory_mtm, 4)
        metrics["residual_buy_fees"] = round(residual_buy_fees, 4)
        metrics["pnl_explained"] = round(explained, 4)
        metrics["pnl_identity_gap"] = round(net - explained, 4)
        metrics["end_quote"] = round(self.quote, 4)
        metrics["end_base"] = round(self.base, 8)
        metrics["end_equity"] = round(end_eq, 4)
        metrics["grid_shifts"] = self.shifts
        metrics["leftover_base"] = round(self.base, 8)
        metrics["n_prints"] = n_prints
        metrics["n_base_buys"] = int(sum(1 for t in self.trades if t.reason == "grid_base_buy"))
        metrics["feed"] = "deals"
        metrics["halted"] = self.halted
        metrics["liquidated"] = False
        metrics["liq_risk"] = 0.0
        metrics["move_mode"] = self.strategy.move_mode
        metrics["open_base_inventory"] = self.strategy.open_base_inventory
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
                "Gate 现货网格 + 突破移动; feed=deals (official tape, no OHLC wick path)",
                "建仓底仓挂现价以上卖单; 现价以下挂买单; 买后挂上一格卖, 卖后挂下一格买",
                "网格利润 = Σ(卖−该笔买−费); 套利次数 = 已完成卖单; 浮动盈亏 = 未卖底仓盯市",
                f"grid_count={self.strategy.grid_count} q={self._grid_step()} "
                f"mode={self.strategy.spacing_mode} move={self.strategy.move_mode}",
                f"prints={n_prints} fills={len(self.trades)} shifts={self.shifts} "
                f"arb={arb_rounds} grid_profit={grid_profit:.4f} mtm={inventory_mtm:.4f} "
                f"tape_ok={tape.get('tape_ok')} identity_gap={net - explained:.6f}",
            ],
        )


def run_spot_moving_grid(cfg: dict[str, Any], deals: pd.DataFrame) -> BacktestResult:
    return SpotMovingGridEngine(cfg).run(deals)
