"""Total-equity metrics, scoring, path-drag attribution, break-even helpers."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from .engine import EngineResult


def _daily_returns(equity: np.ndarray, timestamps: list[Any]) -> pd.Series:
    s = pd.Series(equity, index=pd.to_datetime(timestamps, utc=True))
    daily = s.resample("1D").last().dropna()
    return daily.pct_change().dropna()


def underwater(equity: np.ndarray) -> tuple[float, int, int]:
    """Return max_dd_pct, time_to_recovery_bars (from max-dd trough), longest_underwater_bars."""
    if len(equity) == 0:
        return 0.0, 0, 0
    peak = np.maximum.accumulate(equity)
    dd = (peak - equity) / np.maximum(peak, 1e-12)
    max_dd = float(dd.max())
    trough = int(dd.argmax())
    rec = 0
    for j in range(trough + 1, len(equity)):
        if equity[j] >= peak[trough] - 1e-12:
            rec = j - trough
            break
    else:
        rec = len(equity) - trough
    longest = 0
    cur = 0
    for x in dd:
        if x > 1e-12:
            cur += 1
            longest = max(longest, cur)
        else:
            cur = 0
    return max_dd, rec, longest


def summarize(result: EngineResult, initial: float = 1000.0) -> dict[str, Any]:
    eq = np.asarray(result.equity, dtype=float)
    if len(eq) == 0:
        return {"error": "empty"}
    final = float(eq[-1])
    net = final - initial
    max_dd, ttr, luw = underwater(eq)
    rets = _daily_returns(eq, result.timestamps)
    sharpe = 0.0
    sortino = 0.0
    if len(rets) > 1 and float(rets.std()) > 0:
        sharpe = float(rets.mean() / rets.std() * np.sqrt(365.0))
        down = rets[rets < 0]
        dstd = float(down.std()) if len(down) > 1 else 0.0
        if dstd > 0:
            sortino = float(rets.mean() / dstd * np.sqrt(365.0))
    days = 1.0
    try:
        t0 = pd.Timestamp(result.timestamps[0])
        t1 = pd.Timestamp(result.timestamps[-1])
        days = max((t1 - t0).total_seconds() / 86400.0, 1.0 / 24.0)
    except Exception:
        days = max(len(eq) / 24.0, 1.0)
    ann = (final / initial) ** (365.0 / days) - 1.0 if initial > 0 and final > 0 else -1.0
    calmar = ann / max_dd if max_dd > 1e-12 else (ann if ann > 0 else 0.0)
    d_eq = pd.Series(eq, index=pd.to_datetime(result.timestamps, utc=True)).resample("1D").last().dropna()
    dret = d_eq.pct_change().dropna()
    worst = float(dret.min()) if len(dret) else 0.0
    best = float(dret.max()) if len(dret) else 0.0
    turnover = float(result.components.get("turnover") or 0.0)
    ppm = (net / turnover * 1_000_000.0) if turnover > 1e-9 else 0.0
    # capital tied: inventory value for spot; |locked+upnl| proxy already in inventory_value
    tied = np.asarray(result.inventory_value, dtype=float)
    avg_tied = float(np.mean(np.abs(tied))) if len(tied) else initial
    cap_eff = net / max(avg_tied, 1e-9)
    fees = float(
        result.components.get("spot_trading_fee")
        or result.components.get("futures_fee")
        or 0.0
    )
    return {
        "name": result.name,
        "market": result.market,
        "symbol": result.symbol,
        "initial_capital": initial,
        "final_equity": round(final, 4),
        "total_return": round(net / initial, 6) if initial else 0.0,
        "net_profit": round(net, 4),
        "max_dd": round(max_dd * initial, 4),
        "max_dd_pct": round(max_dd, 6),
        "worst_day": round(worst, 6),
        "best_day": round(best, 6),
        "turnover": round(turnover, 2),
        "net_profit_per_1m_turnover": round(ppm, 4),
        "capital_efficiency": round(cap_eff, 6),
        "avg_capital_tied": round(avg_tied, 4),
        "time_to_recovery_bars": ttr,
        "longest_underwater_bars": luw,
        "time_underwater_frac": round(luw / max(len(eq), 1), 6),
        "sharpe": round(sharpe, 4),
        "sortino": round(sortino, 4),
        "calmar": round(float(calmar), 4),
        "liquidated": result.liquidated,
        "liquidation_count": result.liquidation_count,
        "num_trades": len(result.trades),
        "days": round(days, 3),
        "fees": round(fees, 4),
        **{k: (round(v, 6) if isinstance(v, float) else v) for k, v in result.components.items()},
        **{f"x_{k}": v for k, v in result.extras.items() if isinstance(v, (int, float, bool, str))},
    }


def composite_score(row: dict[str, Any], extras: dict[str, float] | None = None) -> float:
    """
    25% return / 25% tail / 15% profit-per-turnover / 15% capital efficiency
    / 10% regime robustness / 10% OOS stability.
    Frequent liquidation is a hard penalty.
    """
    extras = extras or {}
    ret = float(row.get("total_return") or 0.0)
    dd = float(row.get("max_dd_pct") or 0.0)
    ppm = float(row.get("net_profit_per_1m_turnover") or 0.0)
    ce = float(row.get("capital_efficiency") or 0.0)
    robust = float(extras.get("regime_robustness") or extras.get("robustness") or 0.5)
    oos = float(extras.get("oos_stability") or extras.get("oos") or 0.5)
    liq_n = int(row.get("liquidation_count") or 0)
    liquidated = bool(row.get("liquidated"))

    ret_s = float(np.tanh(ret * 2.0))
    tail_s = float(np.clip(1.0 - dd * 1.4 - 0.15 * max(liq_n, int(liquidated)), -1.0, 1.0))
    ppm_s = float(np.tanh(ppm / 2000.0))
    ce_s = float(np.tanh(ce * 2.0))
    score = (
        0.25 * ret_s
        + 0.25 * tail_s
        + 0.15 * ppm_s
        + 0.15 * ce_s
        + 0.10 * float(np.clip(robust, 0.0, 1.0))
        + 0.10 * float(np.clip(oos, 0.0, 1.0))
    )
    if liquidated or liq_n:
        score -= 0.35 * min(liq_n + int(liquidated), 4)
    return float(round(score, 6))


def path_drag(etf: pd.DataFrame, und: pd.DataFrame, leverage: float = 3.0) -> dict[str, float]:
    """Attribution only. Daily product of (1+L*r_und) vs actual ETF. Not a PnL deduction."""
    a = etf[["timestamp", "close"]].copy()
    b = und[["timestamp", "close"]].copy()
    a["timestamp"] = pd.to_datetime(a["timestamp"], utc=True)
    b["timestamp"] = pd.to_datetime(b["timestamp"], utc=True)
    m = pd.merge(a, b, on="timestamp", suffixes=("_etf", "_und"))
    if m.empty:
        return {"path_drag": 0.0, "etf_return": 0.0, "theo_lev_return": 0.0}
    s = m.set_index("timestamp")
    daily = s.resample("1D").last().dropna()
    if len(daily) < 3:
        etf_r = float(daily["close_etf"].iloc[-1] / daily["close_etf"].iloc[0] - 1.0)
        und_r = float(daily["close_und"].iloc[-1] / daily["close_und"].iloc[0] - 1.0)
        theo = leverage * und_r
        return {"path_drag": etf_r - theo, "etf_return": etf_r, "theo_lev_return": theo, "und_return": und_r}
    re_e = daily["close_etf"].pct_change().dropna()
    re_u = daily["close_und"].pct_change().dropna()
    idx = re_e.index.intersection(re_u.index)
    re_e = re_e.loc[idx]
    re_u = re_u.loc[idx]
    etf_cum = float(np.prod(1.0 + re_e.to_numpy()) - 1.0)
    theo_cum = float(np.prod(1.0 + leverage * re_u.to_numpy()) - 1.0)
    und_cum = float(np.prod(1.0 + re_u.to_numpy()) - 1.0)
    return {
        "path_drag": etf_cum - theo_cum,
        "etf_return": etf_cum,
        "theo_lev_return": theo_cum,
        "und_return": und_cum,
        "days": int(len(re_e)),
    }


def value_add(grid: EngineResult, hold: EngineResult) -> float:
    if len(grid.equity) == 0 or len(hold.equity) == 0:
        return 0.0
    return float(grid.equity[-1] - hold.equity[-1])


def rebate_value(with_reb: EngineResult, zero_reb: EngineResult) -> float:
    if len(with_reb.equity) == 0 or len(zero_reb.equity) == 0:
        return 0.0
    return float(with_reb.equity[-1] - zero_reb.equity[-1])
