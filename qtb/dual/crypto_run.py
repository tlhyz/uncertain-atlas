"""Crypto independent regime experiment runner — Book B only."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .data import load_binance_crypto_dataset, write_provenance
from .experiments import run_binance_crypto_c1, summarize_portfolio
from .portfolio import run_dual_portfolio
from .universe import CRYPTO_BOOK, GLOBAL_RESERVE, DualParams, TECH_BOOK, CryptoParams


def load_crypto_config(path: str | None) -> dict[str, Any]:
    defaults: dict[str, Any] = {
        "experiment_id": "crypto_regime_v1",
        "enabled": False,
        "data": {
            "venue": "binance",
            "symbols": ["BTC", "ETH", "SOL"],
            "interval": "1h",
            "start": "2024-09-01",
            "end": "2024-11-30",
            "auto_start_date": False,
            "tick_precise": True,
            "cache_only": True,
            "download_trades": False,
        },
        "execution": {
            "fill_modes_primary": ["base", "conservative"],
            "decouple_from_tech": True,
        },
        "leverage_scan": [1.25, 1.5, 1.75, 2.0],
        "grid": {
            "atr_step_scan": [0.30, 0.40, 0.50, 0.60],
            "atr_range_scan": [3.0, 5.0, 7.0],
        },
        "output": {"dir": "outputs/experiments/crypto_regime_v1"},
        "run_leverage_scan": True,
        "run_grid_scan": True,
        "run_c1_baseline": True,
        "smoke": False,
        "skip_tick_validation": False,
    }
    if path:
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        defaults.update(raw)
        if isinstance(raw.get("data"), dict):
            defaults["data"] = {**defaults["data"], **raw["data"]}
        if isinstance(raw.get("output"), dict):
            defaults["output"] = {**defaults["output"], **raw["output"]}
    return defaults


def _rank_crypto_leverage(
    data,
    *,
    levels: list[float],
    fill_mode: str = "base",
    tick_precise: bool = True,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for lev in levels:
        cp = CryptoParams(leverage=lev)
        dp = DualParams(crypto=cp, unified_signal=False)
        r = run_dual_portfolio(
            data,
            dp,
            name=f"crypto_lev{lev}",
            fill_mode=fill_mode,
            tick_precise=tick_precise,
            crypto_tick_fills=True,
            tech_tick_fills=False,
            tech_disabled=True,
            tech_tick_only=False,
        )
        m = summarize_portfolio(r, initial=CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
        m["leverage"] = lev
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def _rank_crypto_grid(
    data,
    *,
    steps: list[float],
    ranges: list[float],
    fill_mode: str = "base",
    tick_precise: bool = True,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for step in steps:
        for rng in ranges:
            cp = CryptoParams(grid_atr_step=step, grid_atr_range=rng)
            dp = DualParams(crypto=cp, unified_signal=False)
            r = run_dual_portfolio(
                data,
                dp,
                name=f"crypto_atr{step}_r{rng}",
                fill_mode=fill_mode,
                tick_precise=tick_precise,
                crypto_tick_fills=True,
                tech_tick_fills=False,
                tech_disabled=True,
                tech_tick_only=False,
            )
            m = summarize_portfolio(r, initial=CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
            m["grid_atr_step"] = step
            m["grid_atr_range"] = rng
            rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def _write_crypto_report(payload: dict[str, Any], out_dir: Path) -> Path:
    lev = payload.get("leverage_rank") or []
    grid = payload.get("grid_rank") or []
    c1 = payload.get("c1_baseline") or {}
    lines = [
        "# Crypto Independent Regime Report",
        "",
        f"- Experiment: **{payload.get('experiment_id', 'crypto_regime_v1')}**",
        f"- Window: {payload.get('start')} → {payload.get('end')}",
        f"- Symbols: {', '.join(payload.get('symbols') or [])}",
        f"- Execution: tick-precise crypto book (tech disabled)",
        "",
        "## Leverage rank (Calmar desc)",
        "",
        "| Lev | Return | MaxDD | Calmar | Liq |",
        "|---:|---:|---:|---:|---:|",
    ]
    for r in lev[:8]:
        lines.append(
            f"| {r.get('leverage', '?')} | {100 * float(r.get('total_return', 0)):.2f}% "
            f"| {100 * float(r.get('max_dd_pct', 0)):.2f}% "
            f"| {float(r.get('calmar', 0)):.2f} "
            f"| {int(r.get('liquidation_count', 0))} |"
        )
    if grid:
        lines.extend(["", "## Grid ATR top 5", ""])
        for r in grid[:5]:
            lines.append(
                f"- step={r.get('grid_atr_step')} range={r.get('grid_atr_range')} "
                f"return={100 * float(r.get('total_return', 0)):.2f}% calmar={float(r.get('calmar', 0)):.2f}"
            )
    if c1:
        ind = c1.get("independent") or {}
        lines.extend([
            "",
            "## C1 baseline (independent vs unified)",
            "",
            f"- Independent return: {100 * float(ind.get('total_return', 0)):.2f}%",
            f"- Delta (ind - uni): {100 * float(c1.get('delta_return', 0)):.4f}%",
        ])
    path = out_dir / "CRYPTO_REPORT.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def run_crypto_job(cfg: dict[str, Any]) -> dict[str, Any]:
    if not cfg.get("enabled") and not cfg.get("smoke"):
        raise RuntimeError("crypto_regime.yaml has enabled=false — pass --smoke or set enabled: true")

    data_cfg = cfg.get("data") or {}
    out_dir = Path((cfg.get("output") or {}).get("dir") or "outputs/experiments/crypto_regime_v1")
    out_dir.mkdir(parents=True, exist_ok=True)

    start = str(data_cfg.get("start") or "2024-09-01")
    end = str(data_cfg.get("end") or "2024-11-30")
    interval = str(data_cfg.get("interval") or "1h")
    symbols = tuple(str(s).upper() for s in (data_cfg.get("symbols") or ["BTC", "ETH", "SOL"]))
    cache_only = bool(data_cfg.get("cache_only", True))
    download_trades = bool(data_cfg.get("download_trades", False))
    tick_precise = bool(data_cfg.get("tick_precise", True))

    if cfg.get("smoke"):
        symbols = symbols[:1]
        cfg = {**cfg, "leverage_scan": [1.5], "run_grid_scan": False, "run_c1_baseline": False}

    print(f"\n======== Crypto Regime {start} → {end} ({','.join(symbols)}) ========")
    data = load_binance_crypto_dataset(
        start,
        end,
        interval=interval,
        cache_only=cache_only,
        download_trades=download_trades,
        symbols=symbols,
        skip_tick_validation=bool(cfg.get("skip_tick_validation")),
    )
    write_provenance(data, out_dir)
    print(f"bars={len(data.aligned_index)} tick_precise={tick_precise}")

    payload: dict[str, Any] = {
        "experiment_id": cfg.get("experiment_id"),
        "start": start,
        "end": end,
        "symbols": list(symbols),
        "provenance": data.provenance,
    }

    fill_mode = "base"
    if cfg.get("run_leverage_scan", True):
        levels = [float(x) for x in (cfg.get("leverage_scan") or [1.5])]
        print(f"[run] crypto leverage scan {levels}...")
        payload["leverage_rank"] = _rank_crypto_leverage(
            data, levels=levels, fill_mode=fill_mode, tick_precise=tick_precise,
        )

    if cfg.get("run_grid_scan", True) and not cfg.get("smoke"):
        steps = [float(x) for x in ((cfg.get("grid") or {}).get("atr_step_scan") or [0.40])]
        ranges = [float(x) for x in ((cfg.get("grid") or {}).get("atr_range_scan") or [5.0])]
        print(f"[run] crypto grid scan steps={steps} ranges={ranges}...")
        payload["grid_rank"] = _rank_crypto_grid(
            data, steps=steps, ranges=ranges, fill_mode=fill_mode, tick_precise=tick_precise,
        )

    if cfg.get("run_c1_baseline", True) and not cfg.get("smoke"):
        print("[run] C1 baseline...")
        payload["c1_baseline"] = run_binance_crypto_c1(
            start=start, end=end, cache_only=cache_only, fill_mode=fill_mode,
        )

    json_path = out_dir / "crypto_results.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    report_path = _write_crypto_report(payload, out_dir)
    print(f"\n[done] report -> {report_path}")
    return payload


def main(argv: list[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(description="Crypto independent regime experiment")
    p.add_argument("-c", "--config", default="configs/experiments/crypto_regime.yaml")
    p.add_argument("--cache-only", action="store_true")
    p.add_argument("--smoke", action="store_true", help="BTC-only, single leverage — fast validation")
    p.add_argument("--output-dir", default="")
    args = p.parse_args(argv)
    cfg = load_crypto_config(args.config)
    if args.cache_only:
        cfg.setdefault("data", {})["cache_only"] = True
    if args.smoke:
        cfg["smoke"] = True
        cfg["enabled"] = True
    if args.output_dir:
        cfg.setdefault("output", {})["dir"] = args.output_dir
    run_crypto_job(cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
