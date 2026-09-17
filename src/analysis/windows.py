"""Window extraction for regime labeling — extend in STEP 4+."""

from __future__ import annotations

import pandas as pd


def slice_window(bars: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    t0 = pd.Timestamp(start, tz="UTC")
    t1 = pd.Timestamp(end, tz="UTC") + pd.Timedelta(hours=23)
    m = (bars["timestamp"] >= t0) & (bars["timestamp"] <= t1)
    return bars.loc[m].reset_index(drop=True)
