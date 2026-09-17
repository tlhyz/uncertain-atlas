#!/usr/bin/env python3
"""P6-04 — Tech row OOS check vs Cash→Long (B4 proxy)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.tech_cash_long_oos import evaluate_tech_vs_cash_long_oos, render_tech_cash_long_markdown


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("outputs/experiments/p6_tech_cash_long_oos")
    out_dir.mkdir(parents=True, exist_ok=True)

    from qtb.dual.data import load_dual_dataset
    from qtb.dual.universe import CRYPTO_BOOK, GLOBAL_RESERVE, TECH_BOOK

    initial = float(CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
    pk = {
        "fill_mode": "base",
        "tick_precise": False,
        "crypto_tick_fills": False,
        "tech_tick_fills": True,
        "tech_tick_only": False,
        "execution_label": "TICK tech + BAR crypto (P5-04 parity)",
    }

    print("[p6-04] loading 65d dual dataset...", flush=True)
    data = load_dual_dataset(
        "1h",
        cache_only=True,
        start="2026-07-09",
        end="2026-09-11",
        download_trades=False,
        tech_tick_only=False,
        crypto_download_trades=False,
    )

    print(f"[p6-04] bars={len(data.aligned_index)} running holdout eval...", flush=True)
    report = evaluate_tech_vs_cash_long_oos(
        data,
        initial=initial,
        portfolio_kwargs=pk,
        in_sample_refs=(-0.5870, -0.2519),  # P3-12 65d tick benchmarks
    )

    payload = report.as_dict()
    json_path = out_dir / "tech_cash_long_oos.json"
    md_path = out_dir / "report.md"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_path.write_text(render_tech_cash_long_markdown(report), encoding="utf-8")

    print(
        f"[p6-04] holdout tech={100*report.tech_fsm_return:.2f}% "
        f"B4={100*report.b4_cash_long_return:.2f}% delta={report.delta_pp:+.2f}pp "
        f"verdict={report.verdict}",
        flush=True,
    )
    print(f"[p6-04] wrote {json_path}", flush=True)
    return 0 if report.verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
