"""SOXL vs SOXS inverse-pair hedge diagnostics and bar-mode grid comparison.

Data class: BAR (1h klines) unless caller supplies tick-VWAP closes (TICK).
Conclusions must use Base (2 bps) + Conservative (4 bps) fees only.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.ab.grids import native_spec, rolling_atr

FeePreset = Literal["base", "conservative"]
FEE_BPS = {"base": 2.0, "conservative": 4.0}


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


def simulate_long_grid(
    bars: pd.DataFrame,
    capital: float = 10_000.0,
    *,
    atr_step: float = 0.40,
    atr_range: float = 5.0,
    fee_preset: FeePreset = "base",
    atr_n: int = 24,
) -> dict[str, Any]:
    """Independent long-only ATR grid. BAR conservative penetration (low/high touch)."""
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    atr = rolling_atr(h, l, c, n=atr_n)
    fee = _fee_rate(fee_preset)
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
        }
    )
    out["equity"] = equity
    return out


def simulate_short_grid(
    bars: pd.DataFrame,
    capital: float = 10_000.0,
    *,
    atr_step: float = 0.40,
    atr_range: float = 5.0,
    fee_preset: FeePreset = "base",
    atr_n: int = 24,
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
    atr_step: float = 0.40,
    atr_range: float = 5.0,
) -> dict[str, Any]:
    """Compare same-symbol L+S vs SOXL+SOXS pair long-grids vs baselines.

    Evidence class: BAR unless input closes are tick-VWAP.
    """
    a, b = align_pair(soxl, soxs)
    if len(a) < 48:
        raise ValueError(f"aligned bars {len(a)} < 48")
    diag = hedge_diagnostics(_as_close(a), _as_close(b))
    half = capital / 2.0
    soxl_only = simulate_long_grid(a, capital, atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset)
    soxl_l = simulate_long_grid(a, half, atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset)
    soxl_s = simulate_short_grid(a, half, atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset)
    same_ls = combine_books(soxl_l, soxl_s, "same_symbol_long_short")
    pair_l = simulate_long_grid(a, half, atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset)
    pair_s = simulate_long_grid(b, half, atr_step=atr_step, atr_range=atr_range, fee_preset=fee_preset)
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
        "data_class": "BAR",
        "n_bars": int(len(a)),
        "start": str(a["timestamp"].iloc[0]),
        "end": str(a["timestamp"].iloc[-1]),
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
