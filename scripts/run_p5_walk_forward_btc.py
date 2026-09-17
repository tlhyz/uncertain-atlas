#!/usr/bin/env python3
"""P5-03 — BTC walk-forward split from 2019+ (BAR crypto fills)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.walk_forward import (
    bar_index_splits,
    calendar_year_folds,
    slice_index_range,
    walk_forward_report,
)


def _slice_bars(data, i0: int, i1: int):
    from qtb.dual.data import slice_window

    start, end = slice_index_range(data.aligned_index, i0, i1)
    return slice_window(data, start, end)


def _eval_crypto(data, i0: int, i1: int, *, initial: float) -> dict:
    from qtb.dual.experiments import summarize_portfolio
    from qtb.dual.portfolio import run_dual_portfolio
    from qtb.dual.universe import DualParams

    sub = _slice_bars(data, i0, i1)
    r = run_dual_portfolio(
        sub,
        DualParams(unified_signal=False),
        name=f"wf_{i0}_{i1}",
        fill_mode="base",
        tick_precise=False,
        crypto_tick_fills=False,
        tech_tick_fills=False,
        tech_disabled=True,
        tech_tick_only=False,
    )
    return summarize_portfolio(r, initial=initial)


def main() -> int:
    start = sys.argv[1] if len(sys.argv) > 1 else "2019-09-01"
    end = sys.argv[2] if len(sys.argv) > 2 else "2024-11-30"
    out_dir = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("outputs/experiments/crypto_btc_walk_forward_2019")
    out_dir.mkdir(parents=True, exist_ok=True)

    from qtb.dual.data import load_binance_crypto_dataset, write_provenance
    from qtb.dual.universe import CRYPTO_BOOK, GLOBAL_RESERVE, TECH_BOOK

    initial = float(CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
    print(f"[p5-03] loading BTC {start} → {end} (BAR fills)...", flush=True)
    data = load_binance_crypto_dataset(
        start,
        end,
        interval="1h",
        symbols=("BTC",),
        cache_only=False,
        download_trades=False,
        skip_tick_validation=True,
    )
    data.provenance["execution"] = "BAR_crypto_klines_only"
    write_provenance(data, out_dir)
    n = len(data.aligned_index)
    print(f"[p5-03] bars={n} range={data.aligned_index[0]} → {data.aligned_index[-1]}", flush=True)

    eval_fn = lambda i0, i1: _eval_crypto(data, i0, i1, initial=initial)

    folds = calendar_year_folds(data.aligned_index, min_train_years=2)
    print(f"[p5-03] calendar folds={len(folds)}", flush=True)
    cal_report = walk_forward_report(folds, eval_fn)

    fixed = bar_index_splits(n)
    fixed_report: dict = {"skipped": not fixed}
    if fixed:
        i0_tr, i1_tr = fixed["train"]
        i0_va, i1_va = fixed["validation"]
        i0_te, i1_te = fixed["test"]
        fixed_report = {
            "splits": fixed,
            "train": eval_fn(i0_tr, i1_tr),
            "validation": eval_fn(i0_va, i1_va),
            "test": eval_fn(i0_te, i1_te),
        }

    payload = {
        "experiment_id": "crypto_btc_walk_forward_2019",
        "symbol": "BTC",
        "start": start,
        "end": end,
        "bars": n,
        "execution": "BAR_crypto_klines_only",
        "initial": initial,
        "calendar_walk_forward": cal_report,
        "fixed_split_50_25_25": fixed_report,
        "provenance": data.provenance,
    }
    out_path = out_dir / "walk_forward.json"
    out_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"[p5-03] wrote {out_path}", flush=True)
    if cal_report.get("folds"):
        for row in cal_report["folds"]:
            print(
                f"  y{row['test_year']}: test={100*row['test_return']:.1f}% "
                f"train={100*row['train_return']:.1f}%",
                flush=True,
            )
        print(
            f"  mean_test={100*(cal_report.get('mean_test_return') or 0):.1f}% "
            f"positive_folds={cal_report.get('positive_oos_folds')}/{cal_report.get('n_folds')}",
            flush=True,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
