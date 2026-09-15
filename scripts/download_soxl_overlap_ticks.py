#!/usr/bin/env python3
"""Download SOXLUSDT aggTrades for the SOXS overlap window."""

from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.binance_futures import fetch_agg_trades_day

START = date(2026, 7, 16)
END = date(2026, 9, 11)


def main() -> int:
    d = START
    ok = miss = 0
    while d <= END:
        df = fetch_agg_trades_day("SOXLUSDT", d)
        n = len(df)
        if n:
            ok += 1
        else:
            miss += 1
        print(f"SOXL {d} rows={n}", flush=True)
        d += timedelta(days=1)
    print(f"DONE ok={ok} miss={miss} window={START}->{END}")
    return 0 if miss == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
