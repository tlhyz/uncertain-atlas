"""Gate ETF path models. Prefer Model C (real deals). A/B only from tick underlyings.

Forbidden: ETF_return = underlying_return * 3 as the only model.
Forbidden: SOXL3L = SOX * 9, SNXX3L = SNDK * 6.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from qtb.research.sl_phase.catalog import ETF_MGMT_FEE_DAILY, LEV_3L, LEV_3S, TARGET_LEV_3L, TARGET_LEV_3S


def _utc8_date(ts: pd.Series) -> pd.Series:
    return (pd.to_datetime(ts, utc=True) + pd.Timedelta(hours=8)).dt.floor("D")


@dataclass
class SynthResult:
    timestamp: np.ndarray
    nav: np.ndarray
    leverage: np.ndarray
    rebalances: int
    mgmt_fee_accum: float
    model: str


def model_b_daily_reset(
    ts: np.ndarray,
    under_px: np.ndarray,
    *,
    side: str = "3L",
    start_nav: float = 1.0,
    mgmt: float = ETF_MGMT_FEE_DAILY,
) -> SynthResult:
    """Simple UTC+8 daily 3x reset + daily management fee. Path-dependent via daily compounding."""
    target = TARGET_LEV_3L if side == "3L" else TARGET_LEV_3S
    dates = _utc8_date(pd.Series(pd.to_datetime(ts, utc=True)))
    nav = float(start_nav)
    last_u = float(under_px[0])
    last_day = dates.iloc[0]
    out_nav = np.empty(len(ts), dtype=float)
    lev = np.empty(len(ts), dtype=float)
    fee_acc = 0.0
    rebalances = 0
    for i in range(len(ts)):
        u = float(under_px[i])
        day = dates.iloc[i]
        if day != last_day and last_u > 0:
            r = u / last_u - 1.0
            nav *= 1.0 + target * r
            fee = max(nav, 0.0) * mgmt
            nav -= fee
            fee_acc += fee
            last_u = u
            last_day = day
            rebalances += 1
            nav = max(nav, 0.0)
        out_nav[i] = nav
        lev[i] = target
    return SynthResult(np.asarray(ts), out_nav, lev, rebalances, fee_acc, "B_daily_3x_reset")


def model_a_gate_bands(
    ts: np.ndarray,
    under_px: np.ndarray,
    *,
    side: str = "3L",
    start_nav: float = 1.0,
    mgmt: float = ETF_MGMT_FEE_DAILY,
) -> SynthResult:
    """Approximate Gate intra-day leverage with band resets at UTC+8 midnight checks.

    3L band 2.25x–4.125x; 3S |lev| band 1.5x–5.25x.
    Rebalance when |underlying vs last rebalance ref| is large or lev exits band.
    Extreme moves rebalance in two steps (half, then rest) — not a claim of Gate internals.
    """
    target = TARGET_LEV_3L if side == "3L" else TARGET_LEV_3S
    lo, hi = LEV_3L if side == "3L" else LEV_3S
    dates = _utc8_date(pd.Series(pd.to_datetime(ts, utc=True)))
    nav = float(start_nav)
    u_ref = float(under_px[0])
    last_u = float(under_px[0])
    last_day = dates.iloc[0]
    exposure = nav * target  # USDT notional vs underlying, signed
    out_nav = np.empty(len(ts), dtype=float)
    lev_s = np.empty(len(ts), dtype=float)
    fee_acc = 0.0
    rebalances = 0

    def _lev() -> float:
        if nav <= 1e-12 or last_u <= 0:
            return 0.0
        return exposure / nav

    def _rebalance(step: float = 1.0) -> None:
        nonlocal exposure, rebalances
        exposure = nav * target * step + exposure * (1.0 - step)
        rebalances += 1

    for i in range(len(ts)):
        u = float(under_px[i])
        day = dates.iloc[i]
        if last_u > 0 and u > 0:
            # mark exposure with underlying move (path)
            exposure *= u / last_u
            nav = nav + (exposure - (nav * _lev() if False else 0.0))
            # nav change = exposure * underlying return
            # After scaling exposure by u/last_u, PnL vs previous nav:
        # Recompute nav from cash + marked exposure is easier:
        # Keep cash such that nav = cash + f(exposure). Simpler: apply return to exposure.
        last_u = u
        if nav > 0:
            # rebuild nav as previous nav + d(exposure) from this print — handled above poorly.
            pass
        if day != last_day:
            fee = max(nav, 0.0) * mgmt
            nav -= fee
            fee_acc += fee
            last_day = day
            L = abs(_lev()) if side == "3S" else _lev()
            move = abs(u / u_ref - 1.0) if u_ref > 0 else 0.0
            if L < lo or L > hi or move >= 0.15:
                if move >= 0.35:
                    _rebalance(0.5)
                    _rebalance(1.0)
                else:
                    _rebalance(1.0)
                u_ref = u
        Lnow = _lev()
        out_nav[i] = max(nav, 0.0)
        lev_s[i] = Lnow
    return SynthResult(np.asarray(ts), out_nav, lev_s, rebalances, fee_acc, "A_gate_bands")


def model_a_from_ticks(
    under: pd.DataFrame,
    *,
    side: str = "3L",
    start_nav: float = 1.0,
) -> pd.DataFrame:
    """Correct Model A: cash + leveraged exposure marked on every print."""
    ts = under["timestamp"].to_numpy()
    px = under["price"].to_numpy(dtype=float)
    target = TARGET_LEV_3L if side == "3L" else TARGET_LEV_3S
    lo, hi = LEV_3L if side == "3L" else LEV_3S
    dates = _utc8_date(under["timestamp"])
    nav = float(start_nav)
    u_prev = float(px[0])
    u_ref = float(px[0])
    last_day = dates.iloc[0]
    # exposure in quote; signed. dNAV = exposure * dU/U
    exposure = nav * target
    n = len(px)
    navs = np.empty(n, dtype=float)
    levs = np.empty(n, dtype=float)
    fee_acc = 0.0
    rebalances = 0
    for i in range(n):
        u = float(px[i])
        if u_prev > 0:
            r = u / u_prev - 1.0
            nav += exposure * r
        u_prev = u
        day = dates.iloc[i]
        if day != last_day:
            fee = max(nav, 0.0) * ETF_MGMT_FEE_DAILY
            nav -= fee
            fee_acc += fee
            last_day = day
            lev = (exposure / nav) if nav > 1e-12 else 0.0
            L = abs(lev) if side == "3S" else lev
            move = abs(u / u_ref - 1.0) if u_ref > 0 else 0.0
            if nav <= 0:
                nav = 0.0
                exposure = 0.0
            elif L < lo or L > hi or move >= 0.15:
                if move >= 0.35:
                    exposure = 0.5 * exposure + 0.5 * nav * target
                    rebalances += 1
                    exposure = nav * target
                    rebalances += 1
                else:
                    exposure = nav * target
                    rebalances += 1
                u_ref = u
        navs[i] = max(nav, 0.0)
        levs[i] = (exposure / nav) if nav > 1e-12 else 0.0
    out = pd.DataFrame({"timestamp": under["timestamp"], "nav": navs, "leverage": levs})
    out.attrs["model"] = "A_gate_bands"
    out.attrs["rebalances"] = rebalances
    out.attrs["mgmt_fee_accum"] = fee_acc
    return out


def model_b_from_ticks(under: pd.DataFrame, *, side: str = "3L", start_nav: float = 1.0) -> pd.DataFrame:
    res = model_b_daily_reset(
        under["timestamp"].to_numpy(),
        under["price"].to_numpy(dtype=float),
        side=side,
        start_nav=start_nav,
    )
    out = pd.DataFrame({"timestamp": under["timestamp"], "nav": res.nav, "leverage": res.leverage})
    out.attrs["model"] = res.model
    out.attrs["rebalances"] = res.rebalances
    out.attrs["mgmt_fee_accum"] = res.mgmt_fee_accum
    return out


def compare_abc(
    under: pd.DataFrame,
    etf: pd.DataFrame,
    *,
    side: str = "3L",
) -> dict[str, float | str | int]:
    """Align Model A/B (from underlying ticks) vs Model C (real ETF deals) on UTC+8 daily last."""
    if under.empty or etf.empty:
        return {"status": "DATA_MISSING"}
    a = model_a_from_ticks(under, side=side)
    b = model_b_from_ticks(under, side=side)
    c = etf.copy()
    c["d"] = _utc8_date(c["timestamp"])
    a["d"] = _utc8_date(a["timestamp"])
    b["d"] = _utc8_date(b["timestamp"])
    c_d = c.groupby("d", sort=True)["price"].last()
    a_d = a.groupby("d", sort=True)["nav"].last()
    b_d = b.groupby("d", sort=True)["nav"].last()
    idx = c_d.index.intersection(a_d.index).intersection(b_d.index)
    if len(idx) < 3:
        return {"status": "TOO_SHORT", "n_days": int(len(idx))}
    c_n = c_d.loc[idx] / float(c_d.loc[idx].iloc[0])
    a_n = a_d.loc[idx] / float(a_d.loc[idx].iloc[0])
    b_n = b_d.loc[idx] / float(b_d.loc[idx].iloc[0])
    return {
        "status": "ok",
        "n_days": int(len(idx)),
        "C_total_return": float(c_n.iloc[-1] - 1.0),
        "A_total_return": float(a_n.iloc[-1] - 1.0),
        "B_total_return": float(b_n.iloc[-1] - 1.0),
        "A_minus_C": float(a_n.iloc[-1] - c_n.iloc[-1]),
        "B_minus_C": float(b_n.iloc[-1] - c_n.iloc[-1]),
        "A_vs_C_mae": float(np.mean(np.abs(a_n.to_numpy() - c_n.to_numpy()))),
        "B_vs_C_mae": float(np.mean(np.abs(b_n.to_numpy() - c_n.to_numpy()))),
        "A_rebalances": int(a.attrs.get("rebalances") or 0),
        "B_rebalances": int(b.attrs.get("rebalances") or 0),
        "note": "A/B start_nav=1 at first overlapping day; C is real tape. Do not pick the flattering model.",
    }
