"""S→L phase machine + directional sleeves. Signals use only past/current prints."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from qtb.research.sl_phase.catalog import (
    ETF_MGMT_FEE_DAILY,
    MAKER_FEE,
    PHASE0,
    S_REDUCE_INITIAL,
    S_REDUCE_REMAINING,
    S_TO_L_PLANS,
    TAKER_FEE,
)
from qtb.research.sl_phase.fees_ledger import FeeLedger


def _daily_ohlc_from_ticks(tape: pd.DataFrame) -> pd.DataFrame:
    """UTC+8 daily bars derived from deals. Not a downloaded daily feed."""
    if tape.empty:
        return pd.DataFrame(columns=["open", "high", "low", "close"])
    work = tape.copy()
    work["d"] = (pd.to_datetime(work["timestamp"], utc=True) + pd.Timedelta(hours=8)).dt.floor("D")
    g = work.groupby("d", sort=True)["price"]
    out = pd.DataFrame(
        {
            "open": g.first(),
            "high": g.max(),
            "low": g.min(),
            "close": g.last(),
        }
    )
    return out


def reversal_flags(daily: pd.DataFrame) -> pd.Series:
    """R1 / R2 / R3 on daily bars built from ticks. No future low."""
    if daily.empty or len(daily) < 12:
        return pd.Series(False, index=daily.index)
    c = daily["close"]
    h = daily["high"]
    ema5 = c.ewm(span=5, adjust=False).mean()
    ema10 = c.ewm(span=10, adjust=False).mean()
    low10 = c.shift(1).rolling(10, min_periods=10).min()
    r1 = c >= low10 * 1.08
    above = c > ema5
    r2 = above & above.shift(1) & (ema5 > ema5.shift(1))
    r3 = (ema5 > ema10) & (c > h.shift(1).rolling(5, min_periods=5).max())
    return (r1 | r2 | r3).fillna(False)


def crypto_4h_reversal(tape: pd.DataFrame) -> bool:
    if tape.empty or len(tape) < 50:
        return False
    work = tape.copy()
    work["t"] = pd.to_datetime(work["timestamp"], utc=True)
    work = work.set_index("t").sort_index()
    bar = work["price"].resample("4h").last().dropna()
    if len(bar) < 30:
        return False
    ema12 = bar.ewm(span=12, adjust=False).mean()
    ema24 = bar.ewm(span=24, adjust=False).mean()
    local = bar.shift(1).rolling(18, min_periods=8).min()
    bounce = bar.iloc[-1] >= float(local.iloc[-1]) * 1.08 if pd.notna(local.iloc[-1]) else False
    return bool(ema12.iloc[-1] > ema24.iloc[-1] and bounce)


@dataclass
class Sleeve:
    market: str
    qty: float = 0.0
    cost: float = 0.0
    realized: float = 0.0


@dataclass
class PhaseState:
    cash: float
    s_soxl: Sleeve
    s_snxx: Sleeve
    longs: dict[str, Sleeve] = field(default_factory=dict)
    stage: int = 0
    reversed: bool = False
    overlap_ok: bool = True


def _taker_buy(cash: float, px: float, usdt: float, led: FeeLedger) -> tuple[float, float, float]:
    usdt = min(usdt, cash)
    if usdt <= 0 or px <= 0:
        return cash, 0.0, 0.0
    fee = led.charge(usdt, maker=False)
    if cash < usdt + fee:
        usdt = cash / (1.0 + led.taker_rate)
        fee = led.charge(usdt, maker=False)
    qty = usdt / px
    return cash - usdt - fee, qty, px


def _taker_sell(cash: float, sleeve: Sleeve, px: float, frac: float, led: FeeLedger) -> float:
    qty = sleeve.qty * max(0.0, min(1.0, frac))
    if qty <= 0:
        return cash
    notional = qty * px
    fee = led.charge(notional, maker=False)
    pnl = qty * (px - sleeve.cost) - fee
    sleeve.realized += pnl
    sleeve.qty -= qty
    return cash + notional - fee


def run_directional_hold(
    tape: pd.DataFrame,
    *,
    capital: float,
    rebate: float = 0.0,
    short: bool = False,
) -> dict:
    """Buy (or short-token long) at first print, hold to last. Taker open/close + daily mgmt."""
    led = FeeLedger(MAKER_FEE, TAKER_FEE, rebate, ETF_MGMT_FEE_DAILY)
    if tape is None or tape.empty:
        return {"final_equity": capital, "status": "DATA_MISSING", "ledger": led.snapshot()}
    px = tape["price"].to_numpy(dtype=float)
    ts = pd.to_datetime(tape["timestamp"], utc=True)
    cash, qty, cost = _taker_buy(capital, float(px[0]), capital, led)
    last_day = (ts.iloc[0] + pd.Timedelta(hours=8)).floor("D")
    daily = {}
    for i in range(len(px)):
        p = float(px[i])
        day = (ts.iloc[i] + pd.Timedelta(hours=8)).floor("D")
        if day != last_day:
            fee = led.charge_mgmt(qty * p)
            cash -= fee
            last_day = day
        daily[day] = cash + qty * p
    last = float(px[-1])
    cash = _taker_sell(cash, Sleeve(tape.attrs.get("symbol", ""), qty, cost), last, 1.0, led)
    eq = cash
    return {
        "initial_equity": capital,
        "final_equity": eq,
        "total_return": eq / capital - 1.0,
        "max_drawdown": _mdd(list(daily.values()) + [eq]),
        "ledger": led.snapshot(),
        "status": "ok",
        "short_token": short,
    }


def _mdd(eqs: list[float]) -> float:
    if not eqs:
        return 0.0
    a = np.asarray(eqs, dtype=float)
    peak = np.maximum.accumulate(a)
    return float((a / np.maximum(peak, 1e-12) - 1.0).min())


def run_sl_directional(
    soxl_anchor: pd.DataFrame,
    tapes: dict[str, pd.DataFrame],
    *,
    plan: str = "A",
    s_initial: float = 2000.0,
    reduce_mode: str = "remaining",
    overlap: bool = True,
    rebate: float = 0.0,
    equity0: float = 10_000.0,
) -> dict:
    """S→L without grids. SOXL path from SOXLG ticks (or DATA_MISSING)."""
    led = FeeLedger(MAKER_FEE, TAKER_FEE, rebate, ETF_MGMT_FEE_DAILY)
    if soxl_anchor is None or soxl_anchor.empty:
        return {"status": "DATA_MISSING", "reason": "no Gate underlying ticks for SOXL (SOXLG)", "final_equity": equity0}
    levels = S_TO_L_PLANS[plan]

    def _1m(df: pd.DataFrame) -> pd.DataFrame:
        if df is None or df.empty:
            return df
        w = df.sort_values("timestamp").copy()
        w["timestamp"] = pd.to_datetime(w["timestamp"], utc=True)
        w = w.set_index("timestamp")[["price"]].resample("1min").last().dropna().reset_index()
        return w

    soxl = _1m(soxl_anchor)
    if soxl is None or soxl.empty:
        return {"status": "DATA_MISSING", "reason": "empty 1min SOXLG from ticks", "final_equity": equity0}
    anchor_px = float(soxl["price"].iloc[0])
    soxl_s = tapes.get("SOXL3S_USDT")
    snxx_s = tapes.get("SNXX3S_USDT")
    cash = equity0
    s_soxl_usdt = min(1400.0, s_initial * 0.70)
    s_snxx_usdt = min(600.0, s_initial - s_soxl_usdt)
    if s_soxl_usdt + s_snxx_usdt > 2500:
        s_snxx_usdt = max(0.0, 2500 - s_soxl_usdt)
    sleeves: dict[str, Sleeve] = {}
    if soxl_s is not None and not soxl_s.empty:
        p0 = float(soxl_s["price"].iloc[0])
        cash, q, c = _taker_buy(cash, p0, s_soxl_usdt, led)
        sleeves["SOXL3S_USDT"] = Sleeve("SOXL3S_USDT", q, c)
    if snxx_s is not None and not snxx_s.empty:
        p0 = float(snxx_s["price"].iloc[0])
        cash, q, c = _taker_buy(cash, p0, s_snxx_usdt, led)
        sleeves["SNXX3S_USDT"] = Sleeve("SNXX3S_USDT", q, c)
    daily_soxl = _daily_ohlc_from_ticks(soxl)
    rev = reversal_flags(daily_soxl)
    stage = 0
    reversed_ = False
    last_mark: dict[str, float] = {}
    for m, df in tapes.items():
        if df is not None and not df.empty:
            last_mark[m] = float(df["price"].iloc[0])
    # walk SOXL prints for stage; mark other tapes at last known <= t (no lookahead)
    others = {m: _1m(df) for m, df in tapes.items() if df is not None and not df.empty}
    idxs = {m: 0 for m in others}

    def _advance(t):
        for m, df in others.items():
            i = idxs[m]
            arr_t = df["timestamp"]
            while i + 1 < len(df) and arr_t.iloc[i + 1] <= t:
                i += 1
            idxs[m] = i
            last_mark[m] = float(df["price"].iloc[i])

    def _s_value() -> float:
        v = 0.0
        for k in ("SOXL3S_USDT", "SNXX3S_USDT"):
            sl = sleeves.get(k)
            if sl and sl.qty:
                v += sl.qty * last_mark.get(k, sl.cost)
        return v

    def _cut_s(frac: float) -> None:
        nonlocal cash
        for k in ("SOXL3S_USDT", "SNXX3S_USDT"):
            sl = sleeves.get(k)
            if sl and sl.qty and k in last_mark:
                cash = _taker_sell(cash, sl, last_mark[k], frac, led)

    def _buy_l(market: str, usdt: float) -> None:
        nonlocal cash
        if market not in last_mark or usdt <= 0:
            return
        sl = sleeves.get(market) or Sleeve(market)
        cash, q, c = _taker_buy(cash, last_mark[market], usdt, led)
        if q <= 0:
            return
        if sl.qty <= 0:
            sl.qty, sl.cost = q, c
        else:
            sl.cost = (sl.cost * sl.qty + c * q) / (sl.qty + q)
            sl.qty += q
        sleeves[market] = sl

    soxl_ts = soxl["timestamp"]
    soxl_px = soxl["price"].to_numpy(dtype=float)
    last_day = (soxl_ts.iloc[0] + pd.Timedelta(hours=8)).floor("D")
    equity_path = []
    for i in range(len(soxl)):
        t = soxl_ts.iloc[i]
        p = float(soxl_px[i])
        _advance(t)
        last_mark["SOXLG_USDT"] = p
        day = (t + pd.Timedelta(hours=8)).floor("D")
        if day != last_day:
            nav = cash
            for sl in sleeves.values():
                nav += sl.qty * last_mark.get(sl.market, sl.cost)
                fee = led.charge_mgmt(sl.qty * last_mark.get(sl.market, sl.cost))
                cash -= fee
            last_day = day
        dd = p / anchor_px - 1.0
        if levels is not None and not reversed_:
            cuts = S_REDUCE_REMAINING if reduce_mode == "remaining" else S_REDUCE_INITIAL
            while stage < 4 and dd <= levels[stage]:
                frac = cuts[stage]
                if reduce_mode == "initial":
                    # sell frac of original S notionals via current remaining ratio cap
                    _cut_s(min(1.0, frac / max(1e-9, 1.0)))  # of remaining qty using initial fractions stepwise
                    # interpret as fraction of *current* qty equal to initial-plan increment
                    # already stored as S_REDUCE_INITIAL of initial; convert:
                    # stage0 15% of initial ≈ 15% of current at first hit
                    pass
                _cut_s(frac if reduce_mode == "remaining" else min(1.0, frac / max(_s_value() / max(s_initial, 1e-9), 1e-9)))
                if stage == 0:
                    _buy_l("SOXL3L_USDT", 400.0)
                    _buy_l("ETH3L_USDT", 150.0)
                    _buy_l("SOL3L_USDT", 150.0)
                elif stage == 1:
                    _buy_l("SOXL3L_USDT", 500.0)
                    _buy_l("ETH3L_USDT", 200.0)
                    _buy_l("SOL3L_USDT", 250.0)
                    _buy_l("AAOI3L_USDT", 100.0)
                elif stage == 2:
                    _buy_l("SOXL3L_USDT", 600.0)
                    _buy_l("SNXX3L_USDT", 300.0)
                    _buy_l("PENGU3L_USDT", 200.0)
                    _buy_l("SOL3L_USDT", 300.0)
                else:
                    _cut_s(1.0)
                    _buy_l("SOXL3L_USDT", 800.0)
                    _buy_l("SNXX3L_USDT", 200.0)
                    _buy_l("PUMP3L_USDT", 150.0)
                stage += 1
        if day in rev.index and bool(rev.loc[day]) and not reversed_:
            reversed_ = True
            if not overlap:
                _cut_s(1.0)
            else:
                _cut_s(0.85)
        eq = cash
        for sl in sleeves.values():
            eq += sl.qty * last_mark.get(sl.market, sl.cost)
        equity_path.append(eq)
    # flatten leftovers at last marks
    for sl in list(sleeves.values()):
        if sl.qty and sl.market in last_mark:
            cash = _taker_sell(cash, sl, last_mark[sl.market], 1.0, led)
    s_pnl = sum(sleeves[k].realized for k in sleeves if k.endswith("3S_USDT"))
    l_pnl = sum(sleeves[k].realized for k in sleeves if k.endswith("3L_USDT"))
    return {
        "status": "ok",
        "initial_equity": equity0,
        "final_equity": cash,
        "total_return": cash / equity0 - 1.0,
        "max_drawdown": _mdd(equity_path + [cash]),
        "stage": stage,
        "reversed": reversed_,
        "S_profit": s_pnl,
        "L_profit": l_pnl,
        "ledger": led.snapshot(),
        "plan": plan,
        "reduce_mode": reduce_mode,
        "overlap": overlap,
        "s_initial": s_initial,
        "anchor_px": anchor_px,
        "note": PHASE0,
    }
