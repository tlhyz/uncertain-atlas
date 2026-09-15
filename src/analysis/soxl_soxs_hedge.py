"""SOXL vs SOXS inverse-pair hedge diagnostics and bar-mode grid comparison.

Data class: BAR (1h klines) unless caller supplies tick-VWAP closes (TICK).
Conclusions must use Base (2 bps) + Conservative (4 bps) fees only.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.ab.fills import FillConfig, PendingFill
from qtb.ab.grids import native_spec, rolling_atr
from qtb.data.binance_futures import fetch_agg_trades_day
from qtb.dual.tick_fills import resolve_tick_fills

FeePreset = Literal["base", "conservative"]
FeeEngine = Literal["bar", "tick"]
FEE_BPS = {"base": 2.0, "conservative": 4.0}

# Research default from LIVE_CANDIDATES / Tech template — not optimized on this window.
DEFAULT_ATR_STEP = 0.40
DEFAULT_ATR_RANGE = 5.0
GRID_SWEEP = ((0.30, 3.0), (0.40, 3.0), (0.40, 5.0), (0.50, 5.0))


class DayTradeCache:
    """Load one UTC day of aggTrades at a time (cache_only), indexed by hour."""

    def __init__(self, symbol: str):
        self.symbol = symbol
        self._day = None
        self._by_hour: dict[pd.Timestamp, pd.DataFrame] = {}

    def for_bar(self, ts: pd.Timestamp) -> pd.DataFrame:
        t = pd.Timestamp(ts)
        if t.tzinfo is None:
            t = t.tz_localize("UTC")
        else:
            t = t.tz_convert("UTC")
        d = t.date()
        if d != self._day:
            raw = fetch_agg_trades_day(self.symbol, d, cache_only=True)
            self._day = d
            self._by_hour = {}
            if raw is not None and not raw.empty:
                hours = pd.to_datetime(raw["timestamp"], utc=True).dt.floor("h")
                for hour, grp in raw.groupby(hours, sort=False):
                    self._by_hour[pd.Timestamp(hour)] = grp.reset_index(drop=True)
        key = t.floor("h")
        hour = self._by_hour.get(key)
        if hour is None or hour.empty:
            return pd.DataFrame()
        return _collapse_monotonic_path(hour)


def _collapse_monotonic_path(trades: pd.DataFrame) -> pd.DataFrame:
    """Keep turning points only — identical limit crossings, far fewer prints."""
    px = trades["price"].to_numpy(float)
    if len(px) <= 2:
        return trades
    keep = [0]
    for i in range(1, len(px)):
        if abs(px[i] - px[keep[-1]]) <= 1e-15:
            continue
        if len(keep) >= 2:
            d_prev = px[keep[-1]] - px[keep[-2]]
            d_now = px[i] - px[keep[-1]]
            if d_prev * d_now > 0:
                keep[-1] = i
                continue
        keep.append(i)
    if keep[-1] != len(px) - 1:
        keep.append(len(px) - 1)
    return trades.iloc[keep].reset_index(drop=True)


def validate_tick_coverage(symbol: str, bars: pd.DataFrame) -> dict[str, Any]:
    """Confirm every 1h bar has aggTrades; compare tick extrema to kline."""
    cache = DayTradeCache(symbol)
    missing = 0
    have = 0
    close_err: list[float] = []
    hi_gap: list[float] = []
    lo_gap: list[float] = []
    empty_days: set[str] = set()
    for row in bars.itertuples(index=False):
        tr = cache.for_bar(row.timestamp)
        if tr is None or tr.empty:
            missing += 1
            empty_days.add(str(pd.Timestamp(row.timestamp).date()))
            continue
        have += 1
        px = tr["price"].to_numpy(float)
        close_err.append(abs(float(px[-1]) / max(float(row.close), 1e-12) - 1.0))
        hi_gap.append((float(row.high) - float(px.max())) / max(float(row.high), 1e-12))
        lo_gap.append((float(px.min()) - float(row.low)) / max(float(row.low), 1e-12))
    n = max(len(bars), 1)
    return {
        "symbol": symbol,
        "data_class": "TICK",
        "n_bars": int(len(bars)),
        "bars_with_trades": have,
        "bars_missing_trades": missing,
        "coverage": have / n,
        "empty_days": sorted(empty_days),
        "median_close_rel_err": float(np.median(close_err)) if close_err else float("nan"),
        "p99_close_rel_err": float(np.quantile(close_err, 0.99)) if close_err else float("nan"),
        "median_high_gap": float(np.median(hi_gap)) if hi_gap else float("nan"),
        "median_low_gap": float(np.median(lo_gap)) if lo_gap else float("nan"),
        "pass": missing == 0 and have == len(bars),
    }


@dataclass(frozen=True)
class HedgeDiagnostics:
    n_bars: int
    corr_1h: float
    beta_soxs_on_soxl: float
    beta_soxl_on_soxs: float
    ols_hedge_ratio: float
    residual_vol_1to1: float
    residual_vol_ols: float
    soxl_vol: float
    soxs_vol: float
    product_vol_1to1: float


def _as_close(bars: pd.DataFrame) -> np.ndarray:
    return bars["close"].to_numpy(dtype=float)


def align_pair(soxl: pd.DataFrame, soxs: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Inner-join on timestamp; requires timestamp + OHLC columns."""
    a = soxl.copy()
    b = soxs.copy()
    a["timestamp"] = pd.to_datetime(a["timestamp"], utc=True)
    b["timestamp"] = pd.to_datetime(b["timestamp"], utc=True)
    a = a.dropna(subset=["timestamp", "close"]).sort_values("timestamp")
    b = b.dropna(subset=["timestamp", "close"]).sort_values("timestamp")
    merged = pd.merge(a, b, on="timestamp", suffixes=("_soxl", "_soxs"), how="inner")
    soxl_out = pd.DataFrame(
        {
            "timestamp": merged["timestamp"],
            "open": merged["open_soxl"],
            "high": merged["high_soxl"],
            "low": merged["low_soxl"],
            "close": merged["close_soxl"],
        }
    )
    soxs_out = pd.DataFrame(
        {
            "timestamp": merged["timestamp"],
            "open": merged["open_soxs"],
            "high": merged["high_soxs"],
            "low": merged["low_soxs"],
            "close": merged["close_soxs"],
        }
    )
    return soxl_out.reset_index(drop=True), soxs_out.reset_index(drop=True)


def log_returns(close: np.ndarray) -> np.ndarray:
    c = np.maximum(np.asarray(close, dtype=float), 1e-12)
    r = np.zeros(len(c), dtype=float)
    r[1:] = np.diff(np.log(c))
    return r


def hedge_diagnostics(soxl_close: np.ndarray, soxs_close: np.ndarray) -> HedgeDiagnostics:
    """OLS hedge: r_soxs ≈ α + β r_soxl. 1:1 residual is r_soxl + r_soxs."""
    rx = log_returns(soxl_close)[1:]
    ry = log_returns(soxs_close)[1:]
    if len(rx) < 8:
        raise ValueError("need ≥8 return observations")
    corr = float(np.corrcoef(rx, ry)[0, 1])
    vx = float(np.var(rx))
    vy = float(np.var(ry))
    cov = float(np.cov(ry, rx, ddof=1)[0, 1])
    beta_y_on_x = cov / vx if vx > 1e-16 else float("nan")
    cov_xy = float(np.cov(rx, ry, ddof=1)[0, 1])
    beta_x_on_y = cov_xy / vy if vy > 1e-16 else float("nan")
    # min-var hedge ratio: qty_soxs / qty_soxl in notional terms ≈ -cov(rx,ry)/var(ry)
    # For dollar-neutral: residual r_soxl + h * r_soxs; h* = -cov(rx,ry)/var(ry)
    h_star = -cov_xy / vy if vy > 1e-16 else -1.0
    resid_1 = rx + ry
    resid_h = rx + h_star * ry
    return HedgeDiagnostics(
        n_bars=int(len(soxl_close)),
        corr_1h=corr,
        beta_soxs_on_soxl=float(beta_y_on_x),
        beta_soxl_on_soxs=float(beta_x_on_y),
        ols_hedge_ratio=float(h_star),
        residual_vol_1to1=float(np.std(resid_1, ddof=1)),
        residual_vol_ols=float(np.std(resid_h, ddof=1)),
        soxl_vol=float(np.std(rx, ddof=1)),
        soxs_vol=float(np.std(ry, ddof=1)),
        product_vol_1to1=float(np.std(resid_1, ddof=1)),
    )


def _max_dd(equity: np.ndarray) -> float:
    peak = np.maximum.accumulate(equity)
    dd = equity / np.maximum(peak, 1e-12) - 1.0
    return float(dd.min())


def _summary(equity: np.ndarray, label: str) -> dict[str, Any]:
    eq = np.asarray(equity, dtype=float)
    ret = float(eq[-1] / eq[0] - 1.0) if eq[0] else float("nan")
    dd = _max_dd(eq)
    n = max(len(eq) - 1, 1)
    # 1h bars → annualize ~ 24*365
    hours = float(n)
    ann = (1.0 + ret) ** (24.0 * 365.0 / hours) - 1.0 if hours > 0 and (1.0 + ret) > 0 else float("nan")
    calmar = abs(ann / dd) if dd < 0 else float("nan")
    return {
        "label": label,
        "return": ret,
        "max_dd": dd,
        "calmar": calmar,
        "end_equity": float(eq[-1]),
    }


def buy_hold(close: np.ndarray, capital: float = 10_000.0) -> np.ndarray:
    q = capital / close[0]
    return q * close


def buy_hold_pair(
    soxl_c: np.ndarray,
    soxs_c: np.ndarray,
    capital: float = 10_000.0,
    soxl_weight: float = 0.5,
    rebalance: Literal["none", "daily_24h"] = "none",
) -> np.ndarray:
    """Long both legs. soxl_weight is initial (and daily) notional share."""
    n = len(soxl_c)
    w = float(soxl_weight)
    cash_l = capital * w
    cash_s = capital * (1.0 - w)
    ql = cash_l / soxl_c[0]
    qs = cash_s / soxs_c[0]
    eq = np.empty(n, dtype=float)
    for i in range(n):
        eq[i] = ql * soxl_c[i] + qs * soxs_c[i]
        if rebalance == "daily_24h" and i > 0 and i % 24 == 0:
            total = eq[i]
            ql = (total * w) / soxl_c[i]
            qs = (total * (1.0 - w)) / soxs_c[i]
    return eq


def _fee_rate(preset: FeePreset) -> float:
    return FEE_BPS[preset] / 10_000.0


def _apply_long_tick_fills(
    pending: list[PendingFill],
    trades: pd.DataFrame,
    cfg: FillConfig,
    bar_open: float,
    bar_close: float,
    cash: float,
    qty: float,
    lots: dict[int, float],
    fee: float,
) -> tuple[float, float, dict[int, float], float, int]:
    fills = resolve_tick_fills(pending, trades, cfg, bar_open=bar_open, bar_close=bar_close)
    turnover = 0.0
    n = 0
    for tf in fills:
        px = float(tf.price)
        q = float(tf.qty)
        if q <= 0:
            continue
        if tf.reduce_only and tf.side == "sell":
            lot_idx = tf.level_idx - 1
            have = lots.get(lot_idx, 0.0)
            take = min(q, have)
            if take <= 0:
                continue
            cash += take * px * (1.0 - fee)
            qty -= take
            leftover = have - take
            if leftover <= 1e-12:
                lots.pop(lot_idx, None)
            else:
                lots[lot_idx] = leftover
            turnover += take * px
            n += 1
        elif (not tf.reduce_only) and tf.side == "buy":
            cash -= q * px * (1.0 + fee)
            qty += q
            lots[tf.level_idx] = lots.get(tf.level_idx, 0.0) + q
            turnover += q * px
            n += 1
    return cash, qty, lots, turnover, n


def simulate_long_grid(
    bars: pd.DataFrame,
    capital: float = 10_000.0,
    *,
    atr_step: float = DEFAULT_ATR_STEP,
    atr_range: float = DEFAULT_ATR_RANGE,
    fee_preset: FeePreset = "base",
    atr_n: int = 24,
    fill_engine: FeeEngine = "bar",
    get_trades=None,
) -> dict[str, Any]:
    """Independent long-only ATR grid.

    BAR: wick touch. TICK: path-exact aggTrades via resolve_tick_fills (Base/Conservative).
    """
    o = bars["open"].to_numpy(float)
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    ts = bars["timestamp"]
    atr = rolling_atr(h, l, c, n=atr_n)
    fee = _fee_rate(fee_preset)
    cfg = FillConfig.preset(fee_preset)
    cash = float(capital)
    qty = 0.0
    lots: dict[int, float] = {}
    spec = None
    equity = np.empty(len(c), dtype=float)
    turnover = 0.0
    fills = 0

    for i in range(len(c)):
        mid = float(c[i])
        a = max(float(atr[i]), mid * 0.002)
        if spec is None or mid < spec.lower or mid > spec.upper:
            spec = native_spec(mid, a, atr_step, atr_range, "geometric")
            lots = {k: v for k, v in lots.items() if 0 <= k < len(spec.levels)}
        remaining = max(capital - qty * mid, 0.0)
        empty = [idx for idx, lvl in enumerate(spec.levels) if idx not in lots and lvl <= spec.mid]
        baseline = remaining / max(len(empty), 1)

        if fill_engine == "tick" and get_trades is not None:
            pending: list[PendingFill] = []
            for idx, lvl in enumerate(spec.levels):
                if idx in lots or lvl > spec.mid:
                    continue
                if baseline >= 1.0:
                    pending.append(PendingFill("buy", float(lvl), idx, notional=baseline, reason="grid"))
            for idx, lot_q in list(lots.items()):
                si = idx + 1
                if si < len(spec.levels) and lot_q > 0:
                    pending.append(
                        PendingFill("sell", float(spec.levels[si]), si, qty=lot_q, reduce_only=True, reason="grid_tp")
                    )
            trades = get_trades(i, ts.iloc[i])
            if trades is not None and not trades.empty:
                cash, qty, lots, to, n = _apply_long_tick_fills(
                    pending, trades, cfg, float(o[i]), float(c[i]), cash, qty, lots, fee
                )
                turnover += to
                fills += n
        else:
            for idx, lvl in enumerate(spec.levels):
                if idx in lots or lvl > spec.mid:
                    continue
                if float(l[i]) <= float(lvl) <= float(h[i]):
                    notion = min(baseline, remaining)
                    if notion < 1.0:
                        continue
                    px = float(lvl)
                    q = notion / px
                    cash -= q * px * (1.0 + fee)
                    qty += q
                    lots[idx] = lots.get(idx, 0.0) + q
                    remaining -= notion
                    turnover += notion
                    fills += 1
            for idx, lot_q in list(lots.items()):
                si = idx + 1
                if si >= len(spec.levels) or lot_q <= 0:
                    continue
                tp = float(spec.levels[si])
                if float(h[i]) >= tp:
                    cash += lot_q * tp * (1.0 - fee)
                    qty -= lot_q
                    turnover += lot_q * tp
                    fills += 1
                    del lots[idx]
        equity[i] = cash + qty * float(c[i])

    inv_notional = abs(qty) * float(c[-1])
    out = _summary(equity, "long_grid")
    out.update(
        {
            "end_qty": float(qty),
            "end_inventory_notional": float(inv_notional),
            "inventory_frac": float(inv_notional / capital) if capital else 0.0,
            "turnover": float(turnover),
            "fills": int(fills),
            "fee_preset": fee_preset,
            "fill_engine": fill_engine,
            "atr_step": atr_step,
            "atr_range": atr_range,
        }
    )
    out["equity"] = equity
    return out


def simulate_short_grid(
    bars: pd.DataFrame,
    capital: float = 10_000.0,
    *,
    atr_step: float = DEFAULT_ATR_STEP,
    atr_range: float = DEFAULT_ATR_RANGE,
    fee_preset: FeePreset = "base",
    atr_n: int = 24,
    fill_engine: FeeEngine = "bar",
    get_trades=None,
) -> dict[str, Any]:
    """Independent short-only ATR grid on one symbol (same-symbol hedge leg)."""
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    atr = rolling_atr(h, l, c, n=atr_n)
    fee = _fee_rate(fee_preset)
    cash = float(capital)
    short_qty = 0.0
    lots: dict[int, float] = {}
    spec = None
    equity = np.empty(len(c), dtype=float)
    turnover = 0.0
    fills = 0

    for i in range(len(c)):
        mid = float(c[i])
        a = max(float(atr[i]), mid * 0.002)
        if spec is None or mid < spec.lower or mid > spec.upper:
            spec = native_spec(mid, a, atr_step, atr_range, "geometric")
            lots = {k: v for k, v in lots.items() if 0 <= k < len(spec.levels)}
        remaining = max(capital - short_qty * mid, 0.0)
        empty = [idx for idx, lvl in enumerate(spec.levels) if idx not in lots and lvl >= spec.mid]
        baseline = remaining / max(len(empty), 1)
        for idx, lvl in enumerate(spec.levels):
            if idx in lots or lvl < spec.mid:
                continue
            if float(h[i]) >= float(lvl):
                notion = min(baseline, remaining)
                if notion < 1.0:
                    continue
                px = float(lvl)
                q = notion / px
                cash += q * px * (1.0 - fee)
                short_qty += q
                lots[idx] = lots.get(idx, 0.0) + q
                remaining -= notion
                turnover += notion
                fills += 1
        for idx, lot_q in list(lots.items()):
            si = idx - 1
            if si < 0 or lot_q <= 0:
                continue
            tp = float(spec.levels[si])
            if float(l[i]) <= tp:
                cash -= lot_q * tp * (1.0 + fee)
                short_qty -= lot_q
                turnover += lot_q * tp
                fills += 1
                del lots[idx]
        # short MTM: cash includes sale proceeds; liability is short_qty * close
        equity[i] = cash - short_qty * float(c[i])

    inv_notional = abs(short_qty) * float(c[-1])
    out = _summary(equity, "short_grid")
    out.update(
        {
            "end_qty": float(-short_qty),
            "end_inventory_notional": float(inv_notional),
            "inventory_frac": float(inv_notional / capital) if capital else 0.0,
            "turnover": float(turnover),
            "fills": int(fills),
            "fee_preset": fee_preset,
            "fill_engine": fill_engine,
            "atr_step": atr_step,
            "atr_range": atr_range,
        }
    )
    out["equity"] = equity
    return out


def combine_books(a: dict[str, Any], b: dict[str, Any], label: str) -> dict[str, Any]:
    eq = np.asarray(a["equity"]) + np.asarray(b["equity"])
    out = _summary(eq, label)
    out["end_inventory_notional"] = float(a["end_inventory_notional"] + b["end_inventory_notional"])
    cap = float(a["equity"][0] + b["equity"][0])
    out["inventory_frac"] = out["end_inventory_notional"] / cap if cap else 0.0
    out["net_qty_units"] = float(a.get("end_qty", 0.0) + b.get("end_qty", 0.0))
    out["fills"] = int(a["fills"] + b["fills"])
    out["turnover"] = float(a["turnover"] + b["turnover"])
    out["equity"] = eq
    return out


def run_hedge_experiment(
    soxl: pd.DataFrame,
    soxs: pd.DataFrame,
    *,
    capital: float = 10_000.0,
    fee_preset: FeePreset = "base",
    atr_step: float = DEFAULT_ATR_STEP,
    atr_range: float = DEFAULT_ATR_RANGE,
    fill_engine: FeeEngine = "bar",
    get_trades_soxl=None,
    get_trades_soxs=None,
) -> dict[str, Any]:
    """Compare same-symbol L+S vs SOXL+SOXS pair long-grids vs baselines."""
    a, b = align_pair(soxl, soxs)
    if len(a) < 48:
        raise ValueError(f"aligned bars {len(a)} < 48")
    print(f"[hedge] {fill_engine} {fee_preset} step={atr_step} range={atr_range} bars={len(a)}", flush=True)
    diag = hedge_diagnostics(_as_close(a), _as_close(b))
    half = capital / 2.0
    kw = dict(atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset, fill_engine=fill_engine)
    soxl_only = simulate_long_grid(a, capital, get_trades=get_trades_soxl, **kw)
    soxl_l = simulate_long_grid(a, half, get_trades=get_trades_soxl, **kw)
    soxl_s = simulate_short_grid(a, half, atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset)
    same_ls = combine_books(soxl_l, soxl_s, "same_symbol_long_short")
    pair_l = simulate_long_grid(a, half, get_trades=get_trades_soxl, **kw)
    pair_s = simulate_long_grid(b, half, get_trades=get_trades_soxs, **kw)
    pair = combine_books(pair_l, pair_s, "pair_soxl_soxs_long_grids")
    bh_soxl = _summary(buy_hold(_as_close(a), capital), "bh_soxl")
    bh_pair = _summary(buy_hold_pair(_as_close(a), _as_close(b), capital, 0.5, "none"), "bh_50_50_static")
    bh_pair_d = _summary(
        buy_hold_pair(_as_close(a), _as_close(b), capital, 0.5, "daily_24h"),
        "bh_50_50_daily",
    )
    # residual of pair grid equity vs SOXL path (should be flatter if hedge works)
    pair_eq = np.asarray(pair["equity"], dtype=float)
    soxl_eq = buy_hold(_as_close(a), capital)
    pair_r = log_returns(pair_eq)[1:]
    soxl_r = log_returns(soxl_eq)[1:]
    hedge_corr = float(np.corrcoef(pair_r, soxl_r)[0, 1]) if len(pair_r) > 3 else float("nan")

    inverse_ok = diag.corr_1h < -0.70 and diag.beta_soxs_on_soxl < -0.50
    pair_beats_same = pair["max_dd"] > same_ls["max_dd"]  # less negative is better
    pair_beats_soxl_dd = pair["max_dd"] > soxl_only["max_dd"]
    pair_beats_bh = pair["return"] > bh_pair["return"]

    if not inverse_ok:
        verdict = "FAIL"
        reason = "SOXS is not a usable inverse of SOXL on this window (corr/beta gate)"
    elif pair_beats_same and pair_beats_soxl_dd and pair["return"] > same_ls["return"]:
        verdict = "CONDITIONAL PASS"
        reason = "pair reduces DD vs same-symbol L+S and SOXL-only; still check vs B&H"
    elif pair_beats_same:
        verdict = "CONDITIONAL FAIL"
        reason = "pair better than same-symbol L+S on DD but does not clear SOXL-only / B&H gates"
    else:
        verdict = "FAIL"
        reason = "pair does not improve on same-symbol long+short inventory hedge"

    return {
        "data_class": "TICK" if fill_engine == "tick" else "BAR",
        "n_bars": int(len(a)),
        "start": str(a["timestamp"].iloc[0]),
        "end": str(a["timestamp"].iloc[-1]),
        "atr_step": atr_step,
        "atr_range": atr_range,
        "fill_engine": fill_engine,
        "fee_preset": fee_preset,
        "diagnostics": asdict(diag),
        "inverse_gate": inverse_ok,
        "strategies": {
            "soxl_only_long_grid": {k: v for k, v in soxl_only.items() if k != "equity"},
            "same_symbol_long_short": {k: v for k, v in same_ls.items() if k != "equity"},
            "pair_soxl_soxs_long_grids": {k: v for k, v in pair.items() if k != "equity"},
            "bh_soxl": bh_soxl,
            "bh_50_50_static": bh_pair,
            "bh_50_50_daily": bh_pair_d,
        },
        "pair_vs_soxl_return_corr": hedge_corr,
        "verdict": verdict,
        "reason": reason,
        "pair_beats_same_dd": bool(pair_beats_same),
        "pair_beats_soxl_dd": bool(pair_beats_soxl_dd),
        "pair_beats_bh_return": bool(pair_beats_bh),
    }


def sweep_pair_grids(
    soxl: pd.DataFrame,
    soxs: pd.DataFrame,
    *,
    fee_preset: FeePreset = "base",
    fill_engine: FeeEngine = "bar",
    get_trades_soxl=None,
    get_trades_soxs=None,
    grid: tuple[tuple[float, float], ...] = GRID_SWEEP,
) -> list[dict[str, Any]]:
    """Sweep ATR step/range; rank by pair max_dd then return."""
    rows: list[dict[str, Any]] = []
    for step, rng in grid:
        rep = run_hedge_experiment(
            soxl,
            soxs,
            fee_preset=fee_preset,
            atr_step=step,
            atr_range=rng,
            fill_engine=fill_engine,
            get_trades_soxl=get_trades_soxl,
            get_trades_soxs=get_trades_soxs,
        )
        pair = rep["strategies"]["pair_soxl_soxs_long_grids"]
        rows.append(
            {
                "atr_step": step,
                "atr_range": rng,
                "verdict": rep["verdict"],
                "pair_return": pair["return"],
                "pair_max_dd": pair["max_dd"],
                "pair_inventory_frac": pair["inventory_frac"],
                "same_ls_max_dd": rep["strategies"]["same_symbol_long_short"]["max_dd"],
                "daily_bh_max_dd": rep["strategies"]["bh_50_50_daily"]["max_dd"],
            }
        )
    rows.sort(key=lambda r: (-r["pair_max_dd"], -r["pair_return"]))
    return rows
