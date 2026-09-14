#!/usr/bin/env python3
"""P6-01 — Gate fill ratio calibration vs Binance on overlapping BTC 1h bars."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.data.candles import CACHE_DIR

from src.analysis.gate_fill_calibration import (
    _load_ohlcv_csv,
    render_calibration_markdown,
    run_fill_calibration,
)

DEFAULT_GATE = CACHE_DIR / "futures_BTC_USDT_1h_ab_candles.csv"
DEFAULT_BINANCE = CACHE_DIR / "binance_futures_BTCUSDT_1h_2026-07-09_2026-09-12_klines.csv"
DEFAULT_OUT = Path("outputs/experiments/gate_calibration_v1")


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    out_dir.mkdir(parents=True, exist_ok=True)

    gate_path = DEFAULT_GATE
    binance_path = DEFAULT_BINANCE
    if not gate_path.exists():
        print(f"[p6-01] FAIL missing Gate cache: {gate_path}", file=sys.stderr)
        return 1
    if not binance_path.exists():
        print(f"[p6-01] FAIL missing Binance cache: {binance_path}", file=sys.stderr)
        return 1

    gate_df = _load_ohlcv_csv(gate_path)
    binance_df = _load_ohlcv_csv(binance_path)

    print(f"[p6-01] Gate bars={len(gate_df)} Binance bars={len(binance_df)}", flush=True)

    base = run_fill_calibration(gate_df, binance_df, fill_mode="base")
    cons = run_fill_calibration(gate_df, binance_df, fill_mode="conservative")

    base_path = out_dir / "fill_calibration_base.json"
    cons_path = out_dir / "fill_calibration_conservative.json"
    payload = {
        "experiment_id": "gate_calibration_v1",
        "task": "P6-01",
        "precision": "BAR BACKTEST",
        "gate_cache": str(gate_path),
        "binance_cache": str(binance_path),
        "base": base.as_dict(),
        "conservative": cons.as_dict(),
    }
    base_path.write_text(json.dumps(base.as_dict(), indent=2), encoding="utf-8")
    cons_path.write_text(json.dumps(cons.as_dict(), indent=2), encoding="utf-8")
    (out_dir / "fill_calibration.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md = render_calibration_markdown(base)
    md += "\n---\n\n" + render_calibration_markdown(cons).replace(
        "# Gate Fill Ratio Calibration vs Binance",
        "## Conservative fill mode",
    )
    (out_dir / "report.md").write_text(md, encoding="utf-8")

    print(
        f"[p6-01] overlap={base.n_bars} bars "
        f"fill_ratio={base.fill_ratio_gate_over_binance_count:.3f} (base count) "
        f"vol_ratio={base.volume_ratio_gate_over_binance:.3f}",
        flush=True,
    )
    print(f"[p6-01] wrote {out_dir}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
