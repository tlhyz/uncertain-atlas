#!/usr/bin/env python3
"""P5-02 — parameter plateau detector on ATR step sweep."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.parameter_plateau import analyze_sweep


def main() -> int:
    sweep_path = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else "outputs/experiments/crypto_btc_grid_atr_step/crypto_results.json"
    )
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else sweep_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    data = json.loads(sweep_path.read_text(encoding="utf-8"))
    rows = data.get("grid_rank") or data.get("rows") or []
    if not rows:
        print(f"[p5-02] no sweep rows in {sweep_path}", file=sys.stderr)
        return 1

    report = {
        "source": str(sweep_path),
        "experiment_id": data.get("experiment_id"),
        "param_key": "grid_atr_step",
        "reference_param": 0.4,
        "analysis": analyze_sweep(rows, "grid_atr_step", reference_param=0.4),
    }
    out_path = out_dir / "plateau_report.json"
    out_path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")

    cal = report["analysis"]["calmar"]
    ret = report["analysis"]["total_return"]
    print(f"[p5-02] wrote {out_path}", flush=True)
    print(
        f"  return flag={ret['flag']} actionable={ret['actionable']} spread={ret['return_spread']:.4f}",
        flush=True,
    )
    print(
        f"  calmar flag={cal['flag']} ref_rank={cal.get('reference_rank')} robust_pick={cal.get('robust_pick')}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
