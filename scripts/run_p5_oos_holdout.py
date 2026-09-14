#!/usr/bin/env python3
"""P5-04 — OOS holdout report for research finalists."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.oos_holdout import build_oos_report, holdout_bar_split, render_oos_markdown, summarize_candidate
from src.analysis.walk_forward import slice_index_range


def _slice_bars(data, i0: int, i1: int):
    from qtb.dual.data import slice_window

    start, end = slice_index_range(data.aligned_index, i0, i1)
    return slice_window(data, start, end)


def _run_crypto_btc(data, i0: int, i1: int, *, initial: float) -> dict:
    from qtb.dual.experiments import summarize_portfolio
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.universe import CryptoParams, DualParams

    sub = _slice_bars(data, i0, i1)
    r = run_dual_portfolio(
        sub,
        DualParams(crypto=CryptoParams(leverage=1.5, grid_atr_step=0.4, grid_atr_range=5.0), unified_signal=False),
        name=f"oos_btc_{i0}_{i1}",
        fill_mode="base",
        tick_precise=False,
        crypto_tick_fills=False,
        tech_tick_fills=False,
        tech_disabled=True,
    )
    return summarize_portfolio(r, initial=initial)


def _run_dual_independent(data, i0: int, i1: int, *, initial: float) -> dict:
    from qtb.dual.experiments import summarize_portfolio
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.universe import DualParams

    sub = _slice_bars(data, i0, i1)
    r = run_dual_portfolio(
        sub,
        DualParams(unified_signal=False),
        name=f"oos_dual_{i0}_{i1}",
        fill_mode="base",
        tick_precise=False,
        crypto_tick_fills=False,
        tech_tick_fills=True,
        tech_tick_only=False,
    )
    return summarize_portfolio(r, initial=initial)


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("outputs/experiments/p5_oos_holdout")
    out_dir.mkdir(parents=True, exist_ok=True)

    from qtb.dual.data import load_binance_crypto_dataset, load_dual_dataset
    from qtb.dual.universe import CRYPTO_BOOK, GLOBAL_RESERVE, TECH_BOOK

    initial = float(CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
    candidates: list[dict] = []

    print("[p5-04] BTC crypto default — temporal holdout 2024...", flush=True)
    btc = load_binance_crypto_dataset(
        "2020-01-01",
        "2024-11-30",
        interval="1h",
        symbols=("BTC",),
        cache_only=True,
        download_trades=False,
        skip_tick_validation=True,
    )
    idx = btc.aligned_index
    import numpy as np

    train_idx = np.flatnonzero(idx.year < 2024)
    hold_idx = np.flatnonzero(idx.year == 2024)
    te0, te1 = int(hold_idx[0]), int(hold_idx[-1]) + 1
    hold_m = _run_crypto_btc(btc, te0, te1, initial=initial)
    train_m = {"total_return": -0.860777, "source": "P5-03 fixed split 2020-2021 train"}
    candidates.append(
        summarize_candidate(
            "btc_crypto_default",
            label="BTC PERP grid lev1.5 step0.4 range5",
            train=train_m,
            holdout=hold_m,
            train_window="2020-2023",
            holdout_window="2024",
            benchmark_return=-0.30,
            execution="BAR_crypto_klines_only",
            notes=["LIVE_CANDIDATES MEDIUM research row; C1 sweeps all ~-87%"],
        )
    )
    print(f"  holdout={100*hold_m['total_return']:.1f}% (train ref in-sample -86.1%)", flush=True)

    print("[p5-04] Dual independent — last 25% 65d tech window...", flush=True)
    dual = load_dual_dataset(
        "1h",
        cache_only=True,
        start="2026-07-09",
        end="2026-09-11",
        download_trades=False,
        tech_tick_only=False,
        crypto_download_trades=False,
    )
    split = holdout_bar_split(len(dual.aligned_index), holdout_fraction=0.25)
    if split:
        (_, _), (te0, te1) = split
        hold_d = _run_dual_independent(dual, te0, te1, initial=initial)
        train_d = {"total_return": -0.564, "source": "P4 65d dual-book independent in-sample"}
        t0, t1 = slice_index_range(dual.aligned_index, te0, te1)
        candidates.append(
            summarize_candidate(
                "dual_tech_crypto_independent",
                label="Dual book independent (default FSM)",
                train=train_d,
                holdout=hold_d,
                train_window="65d in-sample (P4 reference)",
                holdout_window=f"{t0}→{t1}",
                benchmark_return=-0.3349,
                execution="TICK tech + BAR crypto",
                notes=["C-05 FAIL; holdout vs B&H -33.49% on 65d full window"],
            )
        )
        print(f"  holdout={100*hold_d['total_return']:.1f}% (train ref in-sample -56.4%)", flush=True)

    report = build_oos_report(
        candidates,
        holdout_policy="temporal_holdout_no_retrain",
        meta={
            "gate_oos": {
                "status": "BLOCKED",
                "reason": "run_gate_oos.py stub; no MEDIUM tech candidate (P3-16)",
            },
            "finalist_source": "outputs/LIVE_CANDIDATES.md",
        },
    )
    json_path = out_dir / "oos_holdout.json"
    md_path = out_dir / "OOS_HOLDOUT_REPORT.md"
    json_path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    md_path.write_text(render_oos_markdown(report), encoding="utf-8")
    print(f"[p5-04] wrote {json_path} verdict={report['verdict']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
