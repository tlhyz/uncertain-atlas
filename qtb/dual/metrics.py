"""Extended portfolio metrics and regime cross-stats."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from qtb.ab.metrics import underwater

from .portfolio import PortfolioResult


def summarize_portfolio(result: PortfolioResult, initial: float = 10_000.0) -> dict[str, Any]:
    eq = np.asarray(result.total_equity, dtype=float)
    if len(eq) == 0:
        return {"error": "empty"}
    final = float(eq[-1])
    net = final - initial
    max_dd, ttr, luw = underwater(eq)
    tech = np.asarray(result.tech_equity, dtype=float)
    crypto = np.asarray(result.crypto_equity, dtype=float)
    t_dd = underwater(tech)[0]
    c_dd = underwater(crypto)[0]

    s = pd.Series(eq, index=pd.to_datetime(result.timestamps, utc=True))
    daily = s.resample("1D").last().dropna().pct_change().dropna()
    sharpe = sortino = 0.0
    if len(daily) > 1 and float(daily.std()) > 0:
        sharpe = float(daily.mean() / daily.std() * np.sqrt(365))
        down = daily[daily < 0]
        if len(down) > 1 and float(down.std()) > 0:
            sortino = float(daily.mean() / down.std() * np.sqrt(365))

    days = max((pd.Timestamp(result.timestamps[-1]) - pd.Timestamp(result.timestamps[0])).total_seconds() / 86400, 1)
    ann = (final / initial) ** (365 / days) - 1 if initial > 0 and final > 0 else -1.0
    calmar = ann / max_dd if max_dd > 1e-12 else 0.0
    turnover = float(result.components.get("turnover") or 0)
    ppm = net / turnover * 1_000_000 if turnover > 1e-9 else 0.0

    return {
        "name": result.name,
        "initial_capital": initial,
        "final_equity": round(final, 2),
        "total_return": round(net / initial, 6),
        "max_dd_pct": round(max_dd, 6),
        "max_dd_usd": round(max_dd * initial, 2),
        "tech_max_dd_pct": round(t_dd, 6),
        "crypto_max_dd_pct": round(c_dd, 6),
        "sharpe": round(sharpe, 4),
        "sortino": round(sortino, 4),
        "calmar": round(float(calmar), 4),
        "time_underwater_frac": round(luw / max(len(eq), 1), 4),
        "liquidation_count": result.liquidation_count,
        "turnover": round(turnover, 2),
        "net_profit_per_1m_turnover": round(ppm, 4),
        "fees": round(float(result.components.get("futures_fee") or 0), 4),
        "rebate": round(float(result.components.get("rebate") or 0), 4),
        "net_funding": round(float(result.components.get("net_funding") or 0), 4),
        "liquidation_loss": round(float(result.components.get("liquidation_loss") or 0), 4),
        **{k: round(v, 4) if isinstance(v, float) else v for k, v in result.components.items()},
    }


def regime_cross_stats(
    tech_eq: np.ndarray,
    crypto_eq: np.ndarray,
    timestamps: list[Any],
) -> dict[str, dict[str, float]]:
    """Classify bars into Tech/Crypto up/down quadrants."""
    t = pd.Series(tech_eq, index=pd.to_datetime(timestamps, utc=True))
    c = pd.Series(crypto_eq, index=pd.to_datetime(timestamps, utc=True))
    tr = t.pct_change().fillna(0)
    cr = c.pct_change().fillna(0)
    regimes = {
        "tech_down_crypto_up": (tr < 0) & (cr > 0),
        "tech_up_crypto_down": (tr > 0) & (cr < 0),
        "both_up": (tr > 0) & (cr > 0),
        "both_down": (tr < 0) & (cr < 0),
    }
    out: dict[str, dict[str, float]] = {}
    for name, mask in regimes.items():
        n = int(mask.sum())
        out[name] = {
            "bars": n,
            "frac": round(n / max(len(tr), 1), 4),
            "avg_tech_ret": round(float(tr[mask].mean()), 6) if n else 0.0,
            "avg_crypto_ret": round(float(cr[mask].mean()), 6) if n else 0.0,
        }
    return out
