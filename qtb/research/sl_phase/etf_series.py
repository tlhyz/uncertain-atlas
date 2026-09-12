"""Build Gate ETF price series: real deals after listing, synthetic only before.

Stitch must report synthetic_last / real_first / gaps. Do not silently rewrite returns.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone

import numpy as np
import pandas as pd

from qtb.research.sl_phase.audit import load_strategy_tape
from qtb.research.sl_phase.catalog import PRODUCTS
from qtb.research.sl_phase.synthetic import model_a_from_ticks
from qtb.research.sl_phase.windows import Confidence, series_confidence


def to_1s_tape(tape: pd.DataFrame) -> pd.DataFrame:
    """Last print per UTC second + summed qty. Still official deals, not a downloaded kline."""
    if tape is None or tape.empty:
        return tape
    work = tape.copy()
    work["timestamp"] = pd.to_datetime(work["timestamp"], utc=True).dt.floor("s")
    g = work.groupby("timestamp", sort=True)
    out = pd.DataFrame(
        {
            "dealid": g["dealid"].last() if "dealid" in work.columns else 0,
            "price": g["price"].last(),
            "amount": g["amount"].sum() if "amount" in work.columns else 1.0,
            "side": g["side"].last() if "side" in work.columns else "buy",
        }
    ).reset_index()
    out.attrs.update(getattr(tape, "attrs", {}))
    out.attrs["compressed"] = "1s_last_print"
    return out


@dataclass
class Stitch:
    market: str
    synthetic_last_price: float | None
    real_first_price: float | None
    price_gap: float | None
    nav_gap: float | None
    scale: float
    confidence: Confidence
    note: str


def load_real_etf(market: str, start: date | None = None, end: date | None = None) -> pd.DataFrame:
    return load_strategy_tape(market, start, end)


def synthesize_from_underlying(
    under: pd.DataFrame,
    *,
    side: str,
    start_nav: float = 1.0,
) -> pd.DataFrame:
    """Gate-rule path model on underlying ticks/prints. Not underlying_return * 3."""
    if under is None or under.empty:
        return pd.DataFrame(columns=["timestamp", "price", "amount", "side", "dealid"])
    nav = model_a_from_ticks(under, side=side, start_nav=start_nav)
    out = pd.DataFrame(
        {
            "timestamp": nav["timestamp"],
            "dealid": np.arange(len(nav), dtype=np.int64),
            "price": nav["nav"],
            "amount": 1.0,
            "side": "synth",
        }
    )
    out.attrs["feed"] = "synthetic_gate_etf"
    out.attrs["model"] = "A_gate_bands"
    out.attrs["leverage"] = nav["leverage"]
    return out


def stitch_synth_then_real(
    market: str,
    synth: pd.DataFrame,
    real: pd.DataFrame,
) -> tuple[pd.DataFrame, Stitch]:
    """Concat synth (strictly before first real print) + real. Scale synth level to real open; keep returns."""
    if real is None or real.empty:
        st = Stitch(market, None, None, None, None, 1.0, "SYNTHETIC_GATE_ETF_WINDOW", "real missing")
        return synth.copy() if synth is not None else real, st
    if synth is None or synth.empty:
        st = Stitch(market, None, float(real["price"].iloc[0]), None, None, 1.0, "REAL_GATE_ETF_WINDOW", "no synth")
        return real.copy(), st
    t0 = real["timestamp"].iloc[0]
    syn = synth.loc[synth["timestamp"] < t0].copy()
    if syn.empty:
        st = Stitch(market, None, float(real["price"].iloc[0]), None, None, 1.0, "REAL_GATE_ETF_WINDOW", "synth empty before real")
        return real.copy(), st
    syn_last = float(syn["price"].iloc[-1])
    real_first = float(real["price"].iloc[0])
    gap = real_first / syn_last - 1.0 if syn_last else None
    # level-match only: multiply synth prices by scale so last synth == first real. Returns unchanged.
    scale = real_first / syn_last if syn_last else 1.0
    syn["price"] = syn["price"] * scale
    out = pd.concat([syn, real], ignore_index=True)
    out = out.sort_values("timestamp").reset_index(drop=True)
    out.attrs["feed"] = "stitched_gate_etf"
    out.attrs["scale_applied_to_synth_level_only"] = scale
    st = Stitch(
        market,
        syn_last,
        real_first,
        gap,
        gap,
        scale,
        "SYNTHETIC_GATE_ETF_WINDOW" if len(syn) else "REAL_GATE_ETF_WINDOW",
        "synth level scaled to real first print; return path not rewritten",
    )
    return out, st


def hourly_etf(market: str, start: date | None = None, end: date | None = None) -> pd.Series:
    tape = load_real_etf(market, start, end)
    if tape.empty:
        return pd.Series(dtype=float)
    work = tape.copy()
    work["t"] = pd.to_datetime(work["timestamp"], utc=True)
    return work.set_index("t")["price"].resample("1h").last().dropna()
