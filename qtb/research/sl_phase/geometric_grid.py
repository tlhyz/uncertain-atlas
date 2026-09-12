"""Geometric spot grid on official deals. Initial 底仓 is a taker buy. Judge TOTAL EQUITY."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

import numpy as np
import pandas as pd

from qtb.research.sl_phase.catalog import ETF_MGMT_FEE_DAILY, MAKER_FEE, TAKER_FEE
from qtb.research.sl_phase.fees_ledger import FeeLedger
from qtb.research.sl_phase.fills import FillPolicy, buy_matches, fill_price, infer_tick, sell_matches, take_qty

Reanchor = Literal["off", "7_day", "14_day", "volatility_triggered"]
Sizing = Literal["fixed_quote", "fixed_qty", "vol_adjusted"]


def geometric_levels(center: float, lower_mult: float, upper_mult: float, n: int) -> np.ndarray:
    lo = center * lower_mult
    hi = center * upper_mult
    if lo <= 0 or hi <= lo or n < 1:
        raise ValueError(f"bad geometric window C={center} {lower_mult}-{upper_mult} n={n}")
    # n grids → n+1 prices
    ratio = (hi / lo) ** (1.0 / n)
    return lo * ratio ** np.arange(n + 1, dtype=float)


@dataclass
class _Lot:
    qty: float
    cost: float
    buy_fee: float


@dataclass
class GridResult:
    symbol: str
    fill_model: str
    sizing: str
    reanchor: str
    initial_equity: float
    final_equity: float
    cash: float
    base: float
    last_px: float
    realized_grid_profit: float
    inventory_unrealized_pnl: float
    directional_pnl: float
    initial_market_buy: float
    initial_taker_fee: float
    initial_slippage: float
    number_of_grid_fills: int
    number_of_round_trips: int
    ledger: FeeLedger
    equity_daily: pd.Series
    notes: list[str] = field(default_factory=list)
    paused_buys: bool = False
    reanchors: int = 0
    closed_grid_loss: float = 0.0

    def metrics(self) -> dict:
        days = max(len(self.equity_daily), 1)
        eq = self.equity_daily.to_numpy(dtype=float) if len(self.equity_daily) else np.array([self.initial_equity])
        peak = np.maximum.accumulate(eq)
        dd = eq / np.maximum(peak, 1e-12) - 1.0
        rets = np.diff(eq) / np.maximum(eq[:-1], 1e-12) if len(eq) > 1 else np.array([0.0])
        tot = self.final_equity / self.initial_equity - 1.0 if self.initial_equity else 0.0
        sharpe = 0.0
        sortino = 0.0
        if len(rets) > 2 and np.std(rets) > 1e-12:
            sharpe = float(np.mean(rets) / np.std(rets) * np.sqrt(365.0))
            dn = rets[rets < 0]
            if len(dn) and np.std(dn) > 1e-12:
                sortino = float(np.mean(rets) / np.std(dn) * np.sqrt(365.0))
        underwater = 0
        longest = 0
        for x in dd:
            if x < 0:
                underwater += 1
                longest = max(longest, underwater)
            else:
                underwater = 0
        turn = self.ledger.turnover_usdt
        profit = self.final_equity - self.initial_equity
        return {
            "symbol": self.symbol,
            "fill_model": self.fill_model,
            "sizing": self.sizing,
            "reanchor": self.reanchor,
            "initial_equity": self.initial_equity,
            "final_equity": self.final_equity,
            "total_return": tot,
            "annualized_return": (1.0 + tot) ** (365.0 / max(days, 1)) - 1.0 if days >= 14 else None,
            "max_drawdown": float(dd.min()) if len(dd) else 0.0,
            "max_intraday_drawdown": float(dd.min()) if len(dd) else 0.0,
            "realized_grid_profit": self.realized_grid_profit,
            "inventory_unrealized_pnl": self.inventory_unrealized_pnl,
            "directional_pnl": self.directional_pnl,
            "gross_trading_profit": self.realized_grid_profit + self.inventory_unrealized_pnl,
            "gross_fee": self.ledger.gross_fee,
            "rebate_income": self.ledger.rebate_income,
            "net_fee": self.ledger.net_trading_fee,
            "ETF_management_fee": self.ledger.etf_management_fee,
            "total_turnover_USDT": turn,
            "daily_average_turnover": turn / days,
            "number_of_grid_fills": self.number_of_grid_fills,
            "number_of_round_trips": self.number_of_round_trips,
            "maker_fill_count": self.ledger.maker_fill_count,
            "taker_fill_count": self.ledger.taker_fill_count,
            "profit_per_100k_turnover": profit / turn * 100_000 if turn else 0.0,
            "profit_per_1m_turnover": profit / turn * 1_000_000 if turn else 0.0,
            "return / max_drawdown": tot / abs(dd.min()) if len(dd) and dd.min() < 0 else None,
            "Sharpe": sharpe,
            "Sortino": sortino,
            "worst_day": float(rets.min()) if len(rets) else 0.0,
            "best_day": float(rets.max()) if len(rets) else 0.0,
            "longest_underwater_period": longest,
            "capital_utilization": 1.0 - (self.cash / self.final_equity if self.final_equity else 0.0),
            "grid_profit": self.realized_grid_profit,
            "initial_market_buy": self.initial_market_buy,
            "initial_taker_fee": self.initial_taker_fee,
            "initial_slippage": self.initial_slippage,
            "reanchors": self.reanchors,
            "closed_grid_loss": self.closed_grid_loss,
            "paused_buys": self.paused_buys,
        }


class GeometricSpotGrid:
    def __init__(
        self,
        *,
        symbol: str,
        capital: float,
        lower_mult: float,
        upper_mult: float,
        grid_n: int,
        fill_model: str = "base",
        sizing: Sizing = "fixed_quote",
        reanchor: Reanchor = "off",
        rebate_rate: float = 0.70,
        maker_rate: float = MAKER_FEE,
        taker_rate: float = TAKER_FEE,
        mgmt_fee_daily: float = ETF_MGMT_FEE_DAILY,
        miss_fill_frac: float = 0.0,
        slip_mult: float = 1.0,
        mgmt_mult: float = 1.0,
        allow_reanchor_up: bool = True,
        pause_buys_on_breakdown: bool = True,
    ):
        self.symbol = symbol
        self.capital = float(capital)
        self.lower_mult = float(lower_mult)
        self.upper_mult = float(upper_mult)
        self.grid_n = int(grid_n)
        self.policy = FillPolicy.of(fill_model)  # type: ignore[arg-type]
        if slip_mult != 1.0 and self.policy.slip_ticks:
            object.__setattr__(self.policy, "slip_ticks", int(round(self.policy.slip_ticks * slip_mult)))
        self.sizing: Sizing = sizing
        self.reanchor: Reanchor = reanchor
        self.miss_fill_frac = float(miss_fill_frac)
        self.allow_reanchor_up = allow_reanchor_up
        self.pause_buys_on_breakdown = pause_buys_on_breakdown
        self.ledger = FeeLedger(maker_rate, taker_rate, rebate_rate, mgmt_fee_daily * mgmt_mult)
        self.cash = float(capital)
        self.base = 0.0
        self.lots: list[_Lot] = []
        self.levels = np.asarray([], dtype=float)
        self.buy_qty: dict[int, float] = {}
        self.sell_from: dict[int, int] = {}  # sell level -> lot index? use lot queue
        self.rest_buy: set[int] = set()
        self.rest_sell: dict[int, _Lot] = {}
        self.center = 0.0
        self.realized = 0.0
        self.fills = 0
        self.rounds = 0
        self.dir_pnl = 0.0
        self.init_buy = 0.0
        self.init_fee = 0.0
        self.init_slip = 0.0
        self.notes: list[str] = []
        self.paused_buys = False
        self.reanchors = 0
        self.closed_loss = 0.0
        self._anchor_ts: pd.Timestamp | None = None

    def _equity(self, px: float) -> float:
        return self.cash + self.base * px

    def _hang(self, center: float, last: float) -> None:
        self.center = center
        self.levels = geometric_levels(center, self.lower_mult, self.upper_mult, self.grid_n)
        self.rest_buy.clear()
        self.rest_sell.clear()
        n = len(self.levels)
        quote_each = self.capital / self.grid_n
        for i, lv in enumerate(self.levels):
            if lv < last:
                self.rest_buy.add(i)
            elif lv > last:
                # need inventory for this sell
                qty = (quote_each / lv) if self.sizing == "fixed_quote" else (quote_each / last)
                self.rest_sell[i] = _Lot(0.0, last, 0.0)  # placeholder until 底仓
                self.rest_sell[i].qty = qty

    def _open_inventory(self, last: float) -> None:
        need = sum(lot.qty for lot in self.rest_sell.values())
        if need <= 0:
            return
        notional = need * last
        fee = self.ledger.charge(notional, maker=False)
        slip = 0.0
        if self.policy.slip_ticks:
            tick = infer_tick(last)
            px = last + self.policy.slip_ticks * tick
            slip = need * (px - last)
            last = px
            notional = need * last
        if self.cash < notional + fee:
            # scale down to cash
            scale = max(0.0, (self.cash * 0.999) / max(notional + fee, 1e-12))
            need *= scale
            notional = need * last
            fee = self.ledger.charge(notional, maker=False)
            for i in list(self.rest_sell):
                self.rest_sell[i].qty *= scale
            self.notes.append(f"initial_inventory_scaled={scale:.4f}")
        self.cash -= notional + fee
        self.base += need
        lot = _Lot(need, last, fee)
        self.lots.append(lot)
        # attach cost to each sell slot
        for i in self.rest_sell:
            self.rest_sell[i].cost = last
            self.rest_sell[i].buy_fee = fee * (self.rest_sell[i].qty / need if need else 0.0)
        self.init_buy = notional
        self.init_fee = fee
        self.init_slip = slip

    def _qty_at(self, level_px: float, last: float) -> float:
        quote_each = self.capital / self.grid_n
        if self.sizing == "fixed_quote":
            return quote_each / level_px
        return quote_each / last

    def _buy_fill(self, i: int, px: float, fee: float) -> None:
        qty = self._qty_at(self.levels[i], px)
        notional = qty * px
        if self.cash < notional + fee:
            return
        self.cash -= notional + fee
        self.base += qty
        lot = _Lot(qty, px, fee)
        self.lots.append(lot)
        self.rest_buy.discard(i)
        # hang sell at next level up
        j = i + 1
        if j < len(self.levels):
            self.rest_sell[j] = lot
        self.fills += 1

    def _sell_fill(self, i: int, px: float, fee: float, lot: _Lot) -> None:
        qty = lot.qty
        if qty <= 0 or self.base + 1e-15 < qty:
            self.rest_sell.pop(i, None)
            return
        notional = qty * px
        self.cash += notional - fee
        self.base -= qty
        pnl = qty * (px - lot.cost) - fee - lot.buy_fee
        self.realized += pnl
        self.rounds += 1
        self.fills += 1
        self.rest_sell.pop(i, None)
        # rehang buy at next level down unless paused
        j = i - 1
        if j >= 0 and not self.paused_buys:
            self.rest_buy.add(j)

    def _close_grid(self, px: float) -> None:
        if self.base > 0:
            notional = self.base * px
            fee = self.ledger.charge(notional, maker=False)
            pnl = notional - sum(l.qty * l.cost for l in self.lots) - fee - sum(l.buy_fee for l in self.lots)
            self.cash += notional - fee
            self.closed_loss += min(0.0, pnl)
            self.realized += pnl
            self.base = 0.0
            self.lots.clear()
        self.rest_buy.clear()
        self.rest_sell.clear()

    def run(self, tape: pd.DataFrame) -> GridResult:
        if tape is None or tape.empty:
            led = self.ledger
            return GridResult(
                self.symbol,
                self.policy.model,
                self.sizing,
                self.reanchor,
                self.capital,
                self.capital,
                self.capital,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0,
                0,
                led,
                pd.Series(dtype=float),
                notes=["EMPTY_TAPE"],
            )
        ts = pd.to_datetime(tape["timestamp"], utc=True)
        px = tape["price"].to_numpy(dtype=float)
        amt = tape["amount"].to_numpy(dtype=float) if "amount" in tape.columns else np.ones(len(px))
        ts_ns = ts.astype("int64").to_numpy()
        day_id = ((ts_ns + 8 * 3600 * 10**9) // (86400 * 10**9)).astype(np.int64)
        last = float(px[0])
        self._hang(last, last)
        self._open_inventory(last)
        self._anchor_ts = ts.iloc[0]
        anchor_ns = int(ts_ns[0])
        daily: dict[int, float] = {}
        last_mgmt_day = int(day_id[0])
        rng = np.random.default_rng(1)
        ema = last
        reanchor_ns = 14 * 86400 * 10**9 if self.reanchor == "14_day" else 7 * 86400 * 10**9
        do_cal = self.reanchor in {"7_day", "14_day"}
        do_vol = self.reanchor == "volatility_triggered"
        n = len(px)
        for k in range(n):
            p = float(px[k])
            tns = int(ts_ns[k])
            day = int(day_id[k])
            if day != last_mgmt_day:
                fee = self.ledger.charge_mgmt(self.base * p)
                self.cash -= fee
                last_mgmt_day = day
            if do_cal and tns - anchor_ns >= reanchor_ns:
                self._close_grid(p)
                self._hang(p, p)
                self._open_inventory(p)
                anchor_ns = tns
                self.reanchors += 1
                self.paused_buys = False
            elif do_vol and self.center > 0:
                dist = abs(p / self.center - 1.0)
                broke_up = p > self.levels[-1]
                broke_dn = p < self.levels[0]
                ema = 0.94 * ema + 0.06 * p
                if broke_up or dist >= 0.25:
                    if self.allow_reanchor_up and ema >= self.center:
                        self._close_grid(p)
                        self._hang(p, p)
                        self._open_inventory(p)
                        anchor_ns = tns
                        self.reanchors += 1
                        self.paused_buys = False
                    elif broke_up:
                        self.notes.append("up_break_no_reanchor")
                if broke_dn and self.pause_buys_on_breakdown:
                    self.paused_buys = True
                    self.rest_buy.clear()
            tick = infer_tick(p)
            remaining = float(amt[k])
            if remaining > 0 and self.rest_sell:
                for i in sorted(self.rest_sell):
                    lv = float(self.levels[i])
                    if not sell_matches(p, lv, tick, self.policy):
                        continue
                    if self.miss_fill_frac > 0 and rng.random() < self.miss_fill_frac:
                        continue
                    lot = self.rest_sell[i]
                    want = lot.qty
                    got = take_qty(remaining, want, self.policy)
                    if got <= 0:
                        break
                    if got + 1e-15 < want:
                        frac = got / want
                        part = _Lot(got, lot.cost, lot.buy_fee * frac)
                        lot.qty -= got
                        lot.buy_fee *= 1.0 - frac
                        fpx = fill_price("sell", lv, tick, self.policy)
                        fee = self.ledger.charge(got * fpx, maker=True)
                        self._sell_partial(i, fpx, fee, part, keep=True)
                        remaining -= got
                        if remaining <= 0:
                            break
                        continue
                    fpx = fill_price("sell", lv, tick, self.policy)
                    fee = self.ledger.charge(got * fpx, maker=True)
                    self._sell_fill(i, fpx, fee, lot)
                    remaining -= got
                    if remaining <= 0:
                        break
            if remaining > 0 and self.rest_buy and not self.paused_buys:
                for i in sorted(self.rest_buy, reverse=True):
                    lv = float(self.levels[i])
                    if not buy_matches(p, lv, tick, self.policy):
                        continue
                    if self.miss_fill_frac > 0 and rng.random() < self.miss_fill_frac:
                        continue
                    want = self._qty_at(lv, p)
                    got = take_qty(remaining, want, self.policy)
                    if got <= 0:
                        break
                    fpx = fill_price("buy", lv, tick, self.policy)
                    fee = self.ledger.charge(got * fpx, maker=True)
                    self._buy_fill_qty(i, fpx, fee, got)
                    remaining -= got
                    if remaining <= 0:
                        break
            if k == n - 1 or int(day_id[k + 1]) != day:
                daily[day] = self._equity(p)
        last_px = float(px[-1])
        inv_cost = sum(l.qty * l.cost for l in self.lots)
        unreal = self.base * last_px - inv_cost
        eq = self._equity(last_px)
        ser = pd.Series(
            daily,
            index=pd.to_datetime(np.array(list(daily.keys()), dtype="int64") * 86400, unit="s", utc=True)
            if daily
            else None,
        )
        return GridResult(
            self.symbol,
            self.policy.model,
            self.sizing,
            self.reanchor,
            self.capital,
            eq,
            self.cash,
            self.base,
            last_px,
            self.realized,
            unreal,
            self.dir_pnl,
            self.init_buy,
            self.init_fee,
            self.init_slip,
            self.fills,
            self.rounds,
            self.ledger,
            ser,
            notes=self.notes,
            paused_buys=self.paused_buys,
            reanchors=self.reanchors,
            closed_grid_loss=self.closed_loss,
        )

    def _buy_fill_qty(self, i: int, px: float, fee: float, qty: float) -> None:
        notional = qty * px
        if qty <= 0 or self.cash < notional + fee:
            return
        self.cash -= notional + fee
        self.base += qty
        lot = _Lot(qty, px, fee)
        self.lots.append(lot)
        self.rest_buy.discard(i)
        j = i + 1
        if j < len(self.levels):
            self.rest_sell[j] = lot
        self.fills += 1

    def _sell_partial(self, i: int, px: float, fee: float, lot: _Lot, keep: bool) -> None:
        qty = lot.qty
        self.cash += qty * px - fee
        self.base -= qty
        pnl = qty * (px - lot.cost) - fee - lot.buy_fee
        self.realized += pnl
        self.fills += 1
        if not keep:
            self.rounds += 1
            self.rest_sell.pop(i, None)
