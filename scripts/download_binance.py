#!/usr/bin/env python3
"""Download Binance official historical data to data/raw/binance/."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.binance_public import (
    SYMBOLS_CRYPTO,
    SYMBOLS_TECH,
    download_symbols_range,
    detect_earliest_available,
    normalize_symbol,
)


def main() -> int:
    p = argparse.ArgumentParser(description="Download Binance USDT-M aggTrades + klines")
    p.add_argument("--symbols", nargs="+", default=list(SYMBOLS_CRYPTO) + list(SYMBOLS_TECH))
    p.add_argument("--start", default="")
    p.add_argument("--end", default="")
    p.add_argument("--detect-start", action="store_true")
    p.add_argument("--cache-only", action="store_true")
    args = p.parse_args()

    Path("data/raw/binance").mkdir(parents=True, exist_ok=True)
    for sym in args.symbols:
        bn = normalize_symbol(sym)
        start = args.start
        if args.detect_start or not start:
            detected = detect_earliest_available(bn, cache_only=args.cache_only)
            start = detected or "2020-01-01"
            print(f"[detect] {bn} earliest ~ {start}")
        end = args.end or __import__("datetime").date.today().isoformat()
        print(f"[download] {bn} {start} -> {end}")
        download_symbols_range([bn], start, end, cache_only=args.cache_only)
    print("[done] run scripts/build_manifest.py next")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
