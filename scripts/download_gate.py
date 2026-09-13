#!/usr/bin/env python3
"""Download Gate data for OOS calibration."""

from __future__ import annotations

import argparse

from qtb.data.candles import fetch_gate_futures_candles


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--contract", default="BTC_USDT")
    p.add_argument("--interval", default="1h")
    args = p.parse_args()
    df = fetch_gate_futures_candles(args.contract, args.interval)
    print(f"[gate] {args.contract} {args.interval} bars={len(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
