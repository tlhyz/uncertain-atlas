#!/usr/bin/env python3
"""P6-02/03 — Live candidate promotion gate review."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.live_promotion import evaluate_promotion, render_promotion_markdown


def main() -> int:
    p = argparse.ArgumentParser(description="Evaluate live candidate promotion gates")
    p.add_argument("--asset", required=True, choices=["BTC", "ETH", "SOL"])
    p.add_argument("--current-confidence", default="MEDIUM")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path("outputs/experiments/p6_promotion_gates"),
    )
    args = p.parse_args()

    report = evaluate_promotion(args.asset, current_confidence=args.current_confidence)
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    stem = args.asset.lower()
    json_path = out_dir / f"{stem}_promotion_gate.json"
    md_path = out_dir / f"{stem}_promotion_gate.md"
    json_path.write_text(json.dumps(report.as_dict(), indent=2), encoding="utf-8")
    md_path.write_text(render_promotion_markdown(report), encoding="utf-8")

    print(
        f"[p6-promotion] {args.asset} verdict={report.promotion_verdict} "
        f"{report.current_confidence}→{report.recommended_confidence} "
        f"blocking={report.n_blocking_failures}",
        flush=True,
    )
    print(f"[p6-promotion] wrote {json_path}", flush=True)
    return 0 if report.promotion_verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
