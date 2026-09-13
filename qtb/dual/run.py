"""CLI runner for dual-engine backtest job."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

import pandas as pd

from .data import load_dual_dataset, write_provenance
from .experiments import (
    compare_independent_vs_unified,
    run_benchmarks,
    run_binance_crypto_c1,
    run_fill_modes,
    run_parameter_sweep,
    run_plans,
    run_seed_windows,
    run_stress_leverage,
    rank_leverage,
    rank_short_structures,
    rank_grid_atr,
)
from .report import write_outputs
from .window_search import search_similar_windows


def _load_quality_thresholds(cfg: dict[str, Any]):
    from src.data.quality_gate import DataQualityThresholds

    path = Path(str(cfg.get("data_quality_config") or "configs/data_quality.yaml"))
    if path.exists():
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return DataQualityThresholds(
            min_rows=int(raw.get("min_rows", 1)),
            max_missing_rate=float(raw.get("max_missing_rate", 0.05)),
            max_gap_fraction=float(raw.get("max_gap_fraction", 0.10)),
            max_duplicate_rate=float(raw.get("max_duplicate_rate", 0.001)),
            max_time_disorder_rate=float(raw.get("max_time_disorder_rate", 0.0)),
            min_file_bytes=int(raw.get("min_file_bytes", 64)),
            require_manifest_rows_match=bool(raw.get("require_manifest_rows_match", False)),
        )
    return DataQualityThresholds()


def _run_data_quality_gate(cfg: dict[str, Any], out_dir: Path) -> None:
    if cfg.get("skip_data_quality") or cfg.get("allow_skip"):
        print("[data-quality] skipped (config)")
        return
    if not cfg.get("tick_precise", True):
        print("[data-quality] skipped (bar mode — no tick manifest required)")
        return
    from src.data.quality_gate import gate_binance_symbols

    dq_cfg = yaml.safe_load(Path(str(cfg.get("data_quality_config") or "configs/data_quality.yaml")).read_text(encoding="utf-8")) if Path(str(cfg.get("data_quality_config") or "configs/data_quality.yaml")).exists() else {}
    symbols = list(dq_cfg.get("dual_tech_symbols") or ["SOXL", "SNXX"])
    th = _load_quality_thresholds(cfg)
    print(f"[data-quality] checking manifests for {symbols}...")
    report = gate_binance_symbols(symbols, out_dir, th, required=True)
    print(f"[data-quality] PASS — wrote {out_dir / 'DATA_QUALITY_REPORT.json'} rows={sum(m.recounted_rows for m in report.manifest_checks)}")


def load_dual_config(path: str | None) -> dict[str, Any]:
    defaults: dict[str, Any] = {
        "interval": "1h",
        "cache_only": False,
        "output_dir": "outputs/dual_engine_perp",
        "run_benchmarks": True,
        "run_sweep": True,
        "sweep_max_runs": 24,
        "run_seed_windows": True,
        "run_plans": True,
        "run_similar_search": True,
        "run_stress": True,
        "fill_mode": "base",
        "run_binance_c1": False,
        "binance_c1_start": "2024-09-01",
        "binance_c1_end": "2024-11-30",
        "download_binance_trades": False,
        "data_start": "2026-07-09",
        "data_end": "",
        "download_trades": True,
        "tick_precise": True,
        "skip_data_quality": False,
        "data_quality_config": "configs/data_quality.yaml",
        "run_independent_vs_unified": True,
        "run_short_structures": True,
        "run_leverage_rank": True,
        "run_grid_atr_rank": True,
        "run_fill_modes": True,
    }
    if path:
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        defaults.update(raw)
    return defaults


def run_job(cfg: dict[str, Any]) -> dict[str, Any]:
    out_dir = Path(cfg.get("output_dir") or "outputs/dual_engine_perp")
    out_dir.mkdir(parents=True, exist_ok=True)
    _run_data_quality_gate(cfg, out_dir)
    interval = str(cfg.get("interval") or "1h")
    cache_only = bool(cfg.get("cache_only"))

    print(f"\n======== Dual-Engine Backtest {interval} (Binance SOXL/SNXX) ========")
    data_start = str(cfg.get("data_start") or "2026-07-09")
    data_end = str(cfg.get("data_end") or "").strip() or None
    download_trades = bool(cfg.get("download_trades", True))
    tick_precise = bool(cfg.get("tick_precise", True))
    data = load_dual_dataset(
        interval,
        cache_only=cache_only,
        start=data_start,
        end=data_end,
        download_trades=download_trades,
    )
    write_provenance(data, out_dir)
    print(f"overlap {data.overlap_start} -> {data.overlap_end} bars={len(data.aligned_index)}")

    payload: dict[str, Any] = {
        "provenance": data.provenance,
        "interval": interval,
    }

    if cfg.get("run_benchmarks", True):
        print("[run] benchmarks...")
        payload["benchmarks"] = run_benchmarks(
            data, fill_mode=str(cfg.get("fill_mode") or "base"), tick_precise=tick_precise,
        )

    if cfg.get("run_sweep", True):
        print("[run] parameter sweep...")
        payload["sweep"] = run_parameter_sweep(
            data,
            max_runs=int(cfg.get("sweep_max_runs") or 24),
            fill_mode=str(cfg.get("fill_mode") or "base"),
            tick_precise=tick_precise,
        )

    if cfg.get("run_seed_windows", True):
        print("[run] seed windows...")
        payload["seed_windows"] = run_seed_windows(data, tick_precise=tick_precise)

    if cfg.get("run_plans", True):
        print("[run] three plans...")
        payload["plans"] = run_plans(data, tick_precise=tick_precise)

    if cfg.get("run_independent_vs_unified", True):
        print("[run] independent vs unified...")
        payload["independent_vs_unified"] = compare_independent_vs_unified(data, tick_precise=tick_precise)

    if cfg.get("run_short_structures", True):
        print("[run] short structure rank...")
        payload["short_structures"] = rank_short_structures(data, tick_precise=tick_precise)

    if cfg.get("run_leverage_rank", True):
        print("[run] leverage rank...")
        payload["leverage_rank"] = rank_leverage(data, tick_precise=tick_precise)

    if cfg.get("run_grid_atr_rank", True):
        print("[run] grid ATR rank...")
        payload["grid_atr_rank"] = rank_grid_atr(data, tick_precise=tick_precise)

    if cfg.get("run_fill_modes", True):
        payload["fill_modes"] = run_fill_modes(data, tick_precise=tick_precise)

    if cfg.get("run_stress", True):
        print("[run] 3x stress...")
        payload["stress_3x"] = run_stress_leverage(data, tick_precise=tick_precise)

    if cfg.get("run_similar_search", True):
        print("[run] similar window search...")
        try:
            payload["similar_windows"] = [w.as_dict() for w in search_similar_windows(data)]
        except Exception as exc:  # noqa: BLE001
            payload["similar_windows"] = [{"error": str(exc)}]

    if cfg.get("download_binance_trades"):
        from qtb.data.binance_futures import download_symbols_range

        print("[run] downloading Binance aggTrades (tech)...")
        syms = cfg.get("binance_symbols") or ["SOXL", "SNXX"]
        payload["binance_download"] = {
            k: len(v) for k, v in download_symbols_range(
                syms,
                data_start,
                data_end or pd.Timestamp.now(tz="UTC").strftime("%Y-%m-%d"),
                cache_only=cache_only,
            ).items()
        }

    if cfg.get("run_binance_c1", True):
        print("[run] CRYPTO_C1 on Binance aggTrades (2024-09 -> 2024-11)...")
        try:
            payload["binance_crypto_c1"] = run_binance_crypto_c1(
                start=str(cfg.get("binance_c1_start") or "2024-09-01"),
                end=str(cfg.get("binance_c1_end") or "2024-11-30"),
                cache_only=cache_only,
                fill_mode=str(cfg.get("fill_mode") or "base"),
            )
        except Exception as exc:  # noqa: BLE001
            payload["binance_crypto_c1"] = {"error": str(exc)}
            print(f"[warn] binance C1 failed: {exc}")

    report_path = write_outputs(payload, out_dir)
    print(f"\n[done] report -> {report_path}")
    return payload


def main(argv: list[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(description="Dual-engine state-switching perpetual backtest")
    p.add_argument("-c", "--config", default="configs/dual_engine_perp.yaml")
    p.add_argument("--cache-only", action="store_true")
    p.add_argument("--output-dir", default="")
    p.add_argument(
        "--download-trades",
        action="store_true",
        help="Download Binance USDT-M aggTrades for binance_c1 window then run C1 backtest",
    )
    args = p.parse_args(argv)
    cfg = load_dual_config(args.config)
    if args.cache_only:
        cfg["cache_only"] = True
    if args.output_dir:
        cfg["output_dir"] = args.output_dir
    if args.download_trades:
        cfg["download_binance_trades"] = True
        cfg["run_binance_c1"] = True
    run_job(cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
