#!/usr/bin/env python3
"""Download SOXL UM aggTrades from Vision listing (2026-05-15) through 2026-07-14.

Fills the local 07-09→07-14 hole first (quality-gate manifest), then the
May–July prefix. FAIL_F1/F2 dates are not on Vision (listing = 2026-05-15).
"""

from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_agg_trades_day

LISTING = date(2026, 5, 15)
GAP_START = date(2026, 7, 9)
GAP_END = date(2026, 7, 14)
PREFIX_END = date(2026, 7, 8)


def _pull(start: date, end: date, label: str) -> tuple[int, int]:
    d = start
    ok = miss = 0
    while d <= end:
        df = fetch_agg_trades_day("SOXLUSDT", d)
        n = len(df)
        if n:
            ok += 1
        else:
            miss += 1
        print(f"[{label}] SOXL {d} rows={n}", flush=True)
        d += timedelta(days=1)
    return ok, miss


def main() -> int:
    g_ok, g_miss = _pull(GAP_START, GAP_END, "gap")
    p_ok, p_miss = _pull(LISTING, PREFIX_END, "prefix")
    print(
        f"DONE gap ok={g_ok} miss={g_miss} prefix ok={p_ok} miss={p_miss} "
        f"listing={LISTING} through={GAP_END}"
    )
    return 0 if (g_miss + p_miss) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
