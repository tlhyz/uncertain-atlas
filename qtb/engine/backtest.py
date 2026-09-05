"""Unified bar-driven backtest engine for Gate USDT-M strategies."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from qtb.costs.fees import fee_preset
from qtb.costs.model import CostModel
from qtb.risk.exits import (
    RiskConfig,
    hit_investment_sl,
    hit_max_dd_stop,
    hit_per_trade_sl,
    hit_per_trade_tp,
    hit_portfolio_equity_sl,
    hit_portfolio_tp,
    near_liquidation,
    price_breaks_range,
    should_stop_adding,
    time_tp_due,
    trailing_stop_price,
)
from qtb.risk.liquidation import estimate_liq_price, force_exit_price
from qtb.strategies import build_strategy

from .types import Book, OrderIntent, Trade


@dataclass
class BacktestResult:
    symbol: str
    interval: str
    strategy: str
    books: dict[str, Book]
    trades: list[Trade]
    equity_curve: list[float]
    drawdown_curve: list[float]
    position_curve: list[float]
    timestamps: list[Any]
    metrics: dict[str, Any] = field(default_factory=dict)
    params: dict[str, Any] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)

    @property
    def liquidated(self) -> bool:
        return any(b.liquidated for b in self.books.values())


class BacktestEngine:
    def __init__(
        self,
        cost: CostModel,
        risk: RiskConfig,
        strategy,
        leverage: float = 5.0,
        symbol: str = "BTC_USDT",
        interval: str = "1h",
        cooldown_bars: int = 0,
    ):
        self.cost = cost
        self.risk = risk
        self.strategy = strategy
        self.leverage = max(float(leverage), 1e-9)
        self.symbol = symbol
        self.interval = interval
        self.cooldown_bars = int(cooldown_bars)
        self.books: dict[str, Book] = {}
        self.trades: list[Trade] = []
        self._trade_id = 0
        self._cooldown: dict[str, int] = {}
        self._halt_all = False
        self._grid_lo: float | None = None
        self._grid_hi: float | None = None
        self._peak_equity = 0.0
        self._min_eq_cushion = 1e9
        self._funding_paid = 0.0
        self._rejected = 0

    def _init_books(self) -> None:
        self.books = {}
        for name, direction, capital in self.strategy.books_spec():
            self.books[name] = Book(
                name=name,
                direction=direction,  # type: ignore[arg-type]
                initial=float(capital),
                wallet=float(capital),
            )
            self._cooldown[name] = 0

    def portfolio_equity(self, price: float) -> float:
        return sum(b.equity(price) for b in self.books.values())

    def initial_capital(self) -> float:
        return sum(b.initial for b in self.books.values())

    def net_position(self) -> float:
        net = 0.0
        for b in self.books.values():
            signed = b.qty if b.direction == "long" else -b.qty
            net += signed
        return net

    def _record_trade(
        self,
        ts: Any,
        book: Book,
        side: str,
        price: float,
        qty: float,
        fee: float,
        slippage: float,
        reason: str,
        realized: float,
        equity: float,
    ) -> None:
        self._trade_id += 1
        self.trades.append(
            Trade(
                trade_id=self._trade_id,
                timestamp=ts,
                symbol=self.symbol,
                book=book.name,
                side=side,
                price=price,
                qty=qty,
                notional=qty * price,
                fee=fee,
                slippage=slippage,
                reason=reason,
                realized_pnl=realized,
                equity_after=equity,
                cycle_id=book.cycle_id,
                direction=book.direction,
            )
        )

    def _open_or_add(self, book: Book, intent: OrderIntent, ts: Any, mark: float) -> bool:
        side = intent.side
        raw = float(intent.price)
        fill_px = self.cost.fill_price(raw, side)
        if intent.qty and intent.qty > 0:
            qty = float(intent.qty)
        else:
            notional_in = float(intent.notional or 0.0)
            qty = self.cost.size_from_notional(notional_in, fill_px)
        if not self.cost.accept_order(qty, fill_px):
            self._rejected += 1
            return False
        notional = qty * fill_px
        fee = self.cost.fee(notional)
        margin = notional / self.leverage
        if book.wallet + 1e-12 < margin + fee:
            self._rejected += 1
            return False
        new_cost = book.avg_entry * book.qty + notional
        book.qty += qty
        book.avg_entry = new_cost / book.qty if book.qty > 0 else 0.0
        book.wallet -= margin + fee
        book.margin_locked += margin
        book.last_entry = fill_px
        if intent.reason in {"mart_add", "grid_buy", "grid_short"} and book.in_position:
            if intent.reason == "mart_add":
                book.adds += 1
                book.max_adds_hit = max(book.max_adds_hit, book.adds)
        book.max_margin_used = max(book.max_margin_used, book.margin_locked)
        if intent.level_idx is not None:
            book.lots[intent.level_idx] = book.lots.get(intent.level_idx, 0.0) + qty
        slip = abs(fill_px - raw)
        eq = self.portfolio_equity(mark)
        self._record_trade(ts, book, side, fill_px, qty, fee, slip, intent.reason, 0.0, eq)
        return True

    def _close(
        self,
        book: Book,
        price: float,
        qty: float,
        side: str,
        reason: str,
        ts: Any,
        mark: float,
        level_idx: int | None = None,
    ) -> float:
        if book.qty <= 0 or qty <= 0:
            return 0.0
        qty = min(qty, book.qty)
        fill_px = self.cost.fill_price(price, side)
        notional = qty * fill_px
        fee = self.cost.fee(notional)
        if book.direction == "long":
            raw = qty * (fill_px - book.avg_entry)
        else:
            raw = qty * (book.avg_entry - fill_px)
        frac = qty / book.qty
        release = book.margin_locked * frac
        book.wallet += release + raw - fee
        book.margin_locked -= release
        book.qty -= qty
        realized = raw - fee
        book.cycle_realized += realized
        if level_idx is not None and level_idx in book.lots:
            del book.lots[level_idx]
        # Grid lot TP is a completed round-trip even if other lots remain.
        if reason in {"grid_sell_tp", "grid_cover_tp"} and book.qty > 1e-16:
            book.cycles += 1
            book.cycle_pnls.append(realized)
            if realized > 0:
                book.wins += 1
            book.cycle_realized -= realized
        if book.qty <= 1e-16:
            book.cycle_id += 1
            book.cycles += 1
            book.cycle_pnls.append(book.cycle_realized)
            if book.cycle_realized > 0:
                book.wins += 1
            if "sl" in reason or "stop" in reason or "liq" in reason or "range" in reason:
                book.stop_outs += 1
            book.reset_position()
            book.cycle_realized = 0.0
            self._cooldown[book.name] = self.cooldown_bars
        slip = abs(fill_px - price)
        eq = self.portfolio_equity(mark)
        self._record_trade(ts, book, side, fill_px, qty, fee, slip, reason, realized, eq)
        return realized

    def _flatten_book(self, book: Book, price: float, reason: str, ts: Any, mark: float) -> None:
        if book.qty <= 0:
            return
        side = "sell" if book.direction == "long" else "buy"
        self._close(book, price, book.qty, side, reason, ts, mark)

    def _flatten_all(self, price: float, reason: str, ts: Any, mark: float) -> None:
        for book in self.books.values():
            self._flatten_book(book, price, reason, ts, mark)

    def _apply_funding(self, rate: float, mark: float, ts: Any) -> None:
        if abs(rate) < 1e-16:
            return
        for book in self.books.values():
            if book.qty <= 0 or book.liquidated:
                continue
            signed = book.qty if book.direction == "long" else -book.qty
            pnl = self.cost.funding(signed, mark, rate)
            book.wallet += pnl
            self._funding_paid += pnl
            if pnl != 0:
                self._record_trade(
                    ts, book, "funding", mark, book.qty, 0.0, 0.0, "funding", pnl, self.portfolio_equity(mark)
                )

    def _check_book_risk(self, book: Book, bar: dict[str, Any]) -> None:
        if book.liquidated or not book.in_position:
            return
        lo, hi, cl = float(bar["low"]), float(bar["high"]), float(bar["close"])
        ts = bar["timestamp"]
        adverse = lo if book.direction == "long" else hi
        favor = hi if book.direction == "long" else lo
        close_side = "sell" if book.direction == "long" else "buy"

        # Liquidation / force-exit
        notional_adv = book.qty * adverse
        eq_adv = book.equity(adverse)
        if near_liquidation(eq_adv, notional_adv, self.risk.maintenance_rate, 0.0) or eq_adv <= 0:
            book.wallet = 0.0
            book.liquidated = True
            book.halted = True
            book.reset_position()
            self._record_trade(ts, book, close_side, adverse, 0.0, 0.0, 0.0, "liquidation", -book.initial, 0.0)
            return

        if self.risk.force_exit_before_liq_buffer_pct and book.in_position:
            liq = estimate_liq_price(
                book.direction,
                book.avg_entry,
                book.qty,
                book.wallet + book.margin_locked,
                self.risk.maintenance_rate,
            )
            fx = force_exit_price(book.direction, liq, self.risk.force_exit_before_liq_buffer_pct)
            if fx is not None:
                hit = (book.direction == "long" and lo <= fx) or (book.direction == "short" and hi >= fx)
                if hit:
                    fill = min(max(fx, lo), hi)
                    self._flatten_book(book, fill, "force_exit_pre_liq", ts, cl)
                    book.halted = True
                    return

        # Update trailing
        if self.risk.trailing_tp_pct:
            book.trailing.update(
                book.direction, favor, book.avg_entry, self.risk.trailing_activation_pct
            )
            if book.trailing.activated and book.trailing.extreme > 0:
                trail_px = trailing_stop_price(
                    book.direction, book.trailing.extreme, self.risk.trailing_tp_pct
                )
                hit = (book.direction == "long" and lo <= trail_px) or (
                    book.direction == "short" and hi >= trail_px
                )
                if hit:
                    fill = min(max(trail_px, lo), hi)
                    self._flatten_book(book, fill, "trailing_tp", ts, cl)
                    return

        # Scaled / partial TP
        if self.risk.scaled_tp and book.avg_entry > 0:
            for i, lvl in enumerate(self.risk.scaled_tp):
                if i in book.scaled_taken:
                    continue
                if hit_per_trade_tp(book.direction, book.avg_entry, favor, lvl.profit_pct):
                    tp_px = (
                        book.avg_entry * (1.0 + lvl.profit_pct)
                        if book.direction == "long"
                        else book.avg_entry * (1.0 - lvl.profit_pct)
                    )
                    fill = min(max(tp_px, lo), hi)
                    qty = book.qty * float(lvl.close_frac)
                    self._close(book, fill, qty, close_side, f"scaled_tp_{i}", ts, cl)
                    if book.in_position:
                        book.scaled_taken.add(i)
                    if not book.in_position:
                        return

        # Per-trade TP (risk overlay; strategy may also emit TP)
        if self.risk.per_trade_tp_pct and hit_per_trade_tp(
            book.direction, book.avg_entry, favor, self.risk.per_trade_tp_pct
        ):
            tp_px = (
                book.avg_entry * (1.0 + self.risk.per_trade_tp_pct)
                if book.direction == "long"
                else book.avg_entry * (1.0 - self.risk.per_trade_tp_pct)
            )
            fill = min(max(tp_px, lo), hi)
            self._flatten_book(book, fill, "per_trade_tp", ts, cl)
            return

        # Time-based TP
        if time_tp_due(book.bars_in_trade, self.risk.time_tp_bars):
            self._flatten_book(book, cl, "time_tp", ts, cl)
            return

        # Per-trade SL (price %)
        if self.risk.per_trade_sl_pct and hit_per_trade_sl(
            book.direction, book.avg_entry, adverse, self.risk.per_trade_sl_pct
        ):
            sl_px = (
                book.avg_entry * (1.0 - self.risk.per_trade_sl_pct)
                if book.direction == "long"
                else book.avg_entry * (1.0 + self.risk.per_trade_sl_pct)
            )
            fill = min(max(sl_px, lo), hi)
            self._flatten_book(book, fill, "per_trade_sl", ts, cl)
            return

        # Investment drawdown SL (50% / 70%)
        if self.risk.investment_sl_pct and hit_investment_sl(
            book.unrealized(adverse), book.initial, self.risk.investment_sl_pct
        ):
            loss = self.risk.investment_sl_pct * book.initial
            sl_px = (
                book.avg_entry - loss / book.qty
                if book.direction == "long"
                else book.avg_entry + loss / book.qty
            )
            fill = min(max(sl_px, lo), hi)
            self._flatten_book(book, fill, "investment_sl", ts, cl)
            return

        # Stop adding on floating loss
        if self.risk.stop_adding_float_loss_pct:
            if should_stop_adding(
                book.unrealized(adverse), book.initial, self.risk.stop_adding_float_loss_pct
            ):
                book.stopped_adding = True

        # Range break
        if self.risk.stop_if_price_breaks_range:
            if price_breaks_range(cl, self._grid_lo, self._grid_hi) or price_breaks_range(
                adverse, self._grid_lo, self._grid_hi
            ):
                self._flatten_book(book, cl, "range_break", ts, cl)
                book.halted = True

    def _check_portfolio_risk(self, bar: dict[str, Any]) -> None:
        cl = float(bar["close"])
        ts = bar["timestamp"]
        eq = self.portfolio_equity(cl)
        initial = self.initial_capital()
        if eq > self._peak_equity:
            self._peak_equity = eq
        dd_pct = (self._peak_equity - eq) / self._peak_equity if self._peak_equity > 0 else 0.0

        if self.risk.portfolio_tp_pct and hit_portfolio_tp(eq, initial, self.risk.portfolio_tp_pct):
            self._flatten_all(cl, "portfolio_tp", ts, cl)
            self._halt_all = True
            return
        if self.risk.portfolio_equity_sl_pct and hit_portfolio_equity_sl(
            eq, initial, self.risk.portfolio_equity_sl_pct
        ):
            self._flatten_all(cl, "portfolio_equity_sl", ts, cl)
            self._halt_all = True
            return
        if self.risk.max_drawdown_stop_pct and hit_max_dd_stop(dd_pct, self.risk.max_drawdown_stop_pct):
            self._flatten_all(cl, "max_dd_stop", ts, cl)
            self._halt_all = True

    def _execute_intents(self, intents: list[OrderIntent], bar: dict[str, Any]) -> None:
        ts = bar["timestamp"]
        cl = float(bar["close"])
        for intent in intents:
            book = self.books.get(intent.book)
            if book is None or book.halted or book.liquidated:
                continue
            if intent.reduce_only:
                if book.qty <= 0:
                    continue
                qty = intent.qty if intent.qty is not None else book.qty
                self._close(book, intent.price, qty, intent.side, intent.reason, ts, cl, intent.level_idx)
            else:
                if self._cooldown.get(book.name, 0) > 0:
                    continue
                if book.stopped_adding and book.in_position:
                    continue
                self._open_or_add(book, intent, ts, cl)

    def run(self, df: pd.DataFrame) -> BacktestResult:
        required = {"open", "high", "low", "close"}
        if not required.issubset(df.columns):
            raise ValueError(f"OHLCV missing columns: {required - set(df.columns)}")
        work = df.copy().reset_index(drop=True)
        if "timestamp" not in work.columns:
            work["timestamp"] = pd.RangeIndex(len(work))
        if "funding_rate" not in work.columns:
            work["funding_rate"] = 0.0

        self._init_books()
        self.strategy.setup(work)
        self._grid_lo, self._grid_hi = self.strategy.grid_range()
        self._peak_equity = self.initial_capital()

        equity_curve: list[float] = []
        dd_curve: list[float] = []
        pos_curve: list[float] = []
        timestamps: list[Any] = []

        for i, row in work.iterrows():
            bar = {
                "timestamp": row["timestamp"],
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "funding_rate": float(row.get("funding_rate") or 0.0),
            }
            cl = bar["close"]
            ts = bar["timestamp"]

            if self._halt_all or all(b.liquidated or b.halted for b in self.books.values()):
                eq = self.portfolio_equity(cl)
                equity_curve.append(eq)
                peak = max(self._peak_equity, eq)
                self._peak_equity = peak
                dd_curve.append(peak - eq)
                pos_curve.append(self.net_position())
                timestamps.append(ts)
                continue

            self._apply_funding(bar["funding_rate"], float(row["open"]), ts)

            for name in list(self._cooldown):
                if self._cooldown[name] > 0:
                    self._cooldown[name] -= 1

            for book in self.books.values():
                if book.in_position:
                    book.bars_in_trade += 1
                    upnl = book.unrealized(bar["low"] if book.direction == "long" else bar["high"])
                    if upnl < book.max_float_loss:
                        book.max_float_loss = upnl

            for book in self.books.values():
                self._check_book_risk(book, bar)

            self._check_portfolio_risk(bar)

            if not self._halt_all:
                intents = self.strategy.on_bar(int(i), bar, self.books)
                self._execute_intents(intents, bar)

            eq = self.portfolio_equity(cl)
            if eq > self._peak_equity:
                self._peak_equity = eq
            equity_curve.append(eq)
            dd_curve.append(self._peak_equity - eq)
            pos_curve.append(self.net_position())
            timestamps.append(ts)

            # Track liq cushion
            for book in self.books.values():
                if book.qty > 0:
                    notional = book.qty * cl
                    maint = notional * self.risk.maintenance_rate
                    cushion = (book.equity(cl) - maint) / max(book.initial, 1e-9)
                    self._min_eq_cushion = min(self._min_eq_cushion, cushion)

        metrics = compute_metrics(
            equity_curve,
            timestamps,
            self.trades,
            self.books,
            self.initial_capital(),
            funding=self._funding_paid,
            rejected=self._rejected,
            min_cushion=self._min_eq_cushion,
        )
        notes = [
            f"funding_paid={self._funding_paid:.4f}",
            f"rejected_orders={self._rejected}",
        ]
        return BacktestResult(
            symbol=self.symbol,
            interval=self.interval,
            strategy=getattr(self.strategy, "name", "unknown"),
            books=self.books,
            trades=self.trades,
            equity_curve=equity_curve,
            drawdown_curve=dd_curve,
            position_curve=pos_curve,
            timestamps=list(timestamps),
            metrics=metrics,
            params={
                "leverage": self.leverage,
                "strategy": getattr(self.strategy, "cfg", {}),
                "risk": self.risk.__dict__,
                "costs": {
                    "label": self.cost.fee_config.label,
                    "eff_maker": self.cost.fee_config.effective_maker,
                    "eff_taker": self.cost.fee_config.effective_taker,
                    "slippage_bps": self.cost.slippage_bps,
                    "rebate": self.cost.fee_config.rebate_rate,
                },
            },
            notes=notes,
        )


def compute_metrics(
    equity: list[float],
    timestamps: list[Any],
    trades: list[Trade],
    books: dict[str, Book],
    initial: float,
    funding: float = 0.0,
    rejected: int = 0,
    min_cushion: float = 1e9,
) -> dict[str, Any]:
    if not equity:
        return {"error": "empty_equity"}
    eq = np.asarray(equity, dtype=float)
    final = float(eq[-1])
    net = final - initial
    peak = np.maximum.accumulate(eq)
    dd = peak - eq
    max_dd = float(dd.max()) if len(dd) else 0.0
    max_dd_pct = float((dd / np.maximum(peak, 1e-12)).max()) if len(dd) else 0.0

    rets = np.diff(eq) / np.maximum(eq[:-1], 1e-12) if len(eq) > 1 else np.array([0.0])
    # Daily-ish Sharpe via timestamp resample when possible
    sharpe = 0.0
    try:
        s = pd.Series(eq, index=pd.to_datetime(timestamps, utc=True))
        daily = s.resample("1D").last().dropna().pct_change().dropna()
        if len(daily) > 1 and float(daily.std()) > 0:
            sharpe = float(daily.mean() / daily.std() * np.sqrt(365.0))
        elif float(np.std(rets)) > 0:
            sharpe = float(np.mean(rets) / np.std(rets) * np.sqrt(365.0 * 24.0))
    except Exception:
        if float(np.std(rets)) > 0:
            sharpe = float(np.mean(rets) / np.std(rets) * np.sqrt(252.0))

    days = 1.0
    try:
        t0 = pd.Timestamp(timestamps[0])
        t1 = pd.Timestamp(timestamps[-1])
        days = max((t1 - t0).total_seconds() / 86400.0, 1.0 / 24.0)
    except Exception:
        days = max(len(eq) / 24.0, 1.0)
    ann_ret = (final / initial) ** (365.0 / days) - 1.0 if initial > 0 and final > 0 else -1.0
    calmar = ann_ret / max_dd_pct if max_dd_pct > 1e-12 else (ann_ret if ann_ret > 0 else 0.0)

    cycle_pnls = [p for b in books.values() for p in b.cycle_pnls]
    wins = [p for p in cycle_pnls if p > 0]
    losses = [p for p in cycle_pnls if p <= 0]
    win_rate = (len(wins) / len(cycle_pnls)) if cycle_pnls else 0.0
    gp = float(sum(wins))
    gl = abs(float(sum(losses)))
    profit_factor = (gp / gl) if gl > 1e-12 else (gp if gp > 0 else 0.0)
    total_fees = float(sum(t.fee for t in trades))
    gross = net + total_fees
    fee_ratio = total_fees / max(abs(gross), 1e-9)
    max_float = float(sum(b.max_float_loss for b in books.values()))
    liquidated = any(b.liquidated for b in books.values())
    liq_risk = 1.0 if liquidated else float(max(0.0, min(1.0, 1.0 - max(min_cushion, 0.0))))
    cycles = int(sum(b.cycles for b in books.values()))
    stop_outs = int(sum(b.stop_outs for b in books.values()))

    return {
        "initial_capital": round(initial, 4),
        "final_equity": round(final, 4),
        "net_pnl": round(net, 4),
        "return_pct": round(net / initial, 6) if initial else 0.0,
        "ann_return": round(float(ann_ret), 6),
        "max_dd": round(max_dd, 4),
        "max_dd_pct": round(max_dd_pct, 6),
        "sharpe": round(sharpe, 4),
        "calmar": round(float(calmar), 4),
        "win_rate": round(win_rate, 4),
        "profit_factor": round(float(profit_factor), 4),
        "max_float_loss": round(max_float, 4),
        "liq_risk": round(liq_risk, 4),
        "liquidated": liquidated,
        "fee_ratio": round(fee_ratio, 6),
        "total_fees": round(total_fees, 4),
        "funding_pnl": round(funding, 4),
        "cycles": cycles,
        "stop_outs": stop_outs,
        "num_trades": len(trades),
        "rejected_orders": rejected,
        "days": round(days, 3),
        "cycle_pnl_sum": round(float(sum(cycle_pnls)), 4),
    }


def run_backtest(cfg: dict[str, Any], df: pd.DataFrame) -> BacktestResult:
    costs_cfg = cfg.get("costs") or {}
    fee = fee_preset(
        market=costs_cfg.get("market") or cfg.get("market") or "futures",
        vip_tier=int(costs_cfg.get("vip_tier") or 7),
        rebate_rate=costs_cfg.get("rebate_rate"),
    )
    cost = CostModel(
        fee_config=fee,
        slippage_bps=float(costs_cfg.get("slippage_bps") or 0.0),
        use_maker=bool(costs_cfg.get("use_maker")),
        quanto=float(costs_cfg.get("quanto") or 0.0001),
        min_order_size=float(costs_cfg.get("min_order_size") or 1.0),
        min_notional=float(costs_cfg.get("min_notional") or 1.0),
        apply_funding=bool(costs_cfg.get("apply_funding", True)),
    )
    risk = RiskConfig.from_dict(cfg.get("risk") or {}, maintenance_rate=float(costs_cfg.get("maintenance_rate") or 0.005))
    strat_cfg = dict(cfg.get("strategy") or {})
    strategy = build_strategy(strat_cfg)
    engine = BacktestEngine(
        cost=cost,
        risk=risk,
        strategy=strategy,
        leverage=float(strat_cfg.get("leverage") or 5.0),
        symbol=str(cfg.get("symbol") or "BTC_USDT"),
        interval=str(cfg.get("interval") or "1h"),
        cooldown_bars=int(strat_cfg.get("cooldown_bars") or 0),
    )
    return engine.run(df)
