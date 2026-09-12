#!/usr/bin/env python3
"""qtb CLI: backtest | optimize | report | batch | screen | ab."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from qtb.config import load_config
from qtb.live.broker import LiveBroker, is_dry_run_forced


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="qtb",
        description=(
            "Gate USDT-M backtest / optimize / report / screen / "
            "ETF-vs-perp A/B (default mode=backtest, live is DRY_RUN stub)."
        ),
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_common(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("-c", "--config", default="", help="YAML/TOML config path")
        sp.add_argument("--symbol", default="", help="Override symbol, e.g. BTC_USDT")
        sp.add_argument("--interval", default="", help="1m/5m/15m/1h/4h/1d")
        sp.add_argument("--days", type=int, default=0)
        sp.add_argument("--cache-only", action="store_true")
        sp.add_argument("--prefer-sample", action="store_true")
        sp.add_argument("--output-dir", default="")
        sp.add_argument("--run-name", default="")
        sp.add_argument("--strategy", default="", help="classic_grid|trend_grid|dual_grid|martingale|dual_martingale")
        sp.add_argument("--stop-loss", type=float, default=-1.0, help="Investment SL 0.5 or 0.7")

    bt = sub.add_parser("backtest", help="Run a single backtest and write outputs/")
    add_common(bt)

    opt = sub.add_parser("optimize", help="Search + anti-overfit + ranked composite score")
    add_common(opt)
    opt.add_argument("--grid", default="", help="compact|medium|full")

    rp = sub.add_parser("report", help="Show / refresh artifacts from an existing run dir")
    rp.add_argument("run_dir", nargs="?", default="")
    rp.add_argument("-c", "--config", default="")
    rp.add_argument("--prefer-sample", action="store_true")

    bat = sub.add_parser("batch", help="Multi-symbol / multi-interval backtests")
    add_common(bat)

    live = sub.add_parser("live", help="Live stub (always DRY_RUN unless dangerous override)")
    live.add_argument("-c", "--config", default="")
    live.add_argument("--ping", action="store_true")

    from qtb.screen import add_screen_flags

    screen = sub.add_parser(
        "screen",
        help="Screen liquid Gate USDT perps for high vol + low path efficiency",
    )
    add_screen_flags(screen, batch_default=False)

    batch_screen = sub.add_parser(
        "batch-screen",
        help="Screen then batch-backtest top K picks (aggressive dual SL50)",
    )
    add_screen_flags(batch_screen, batch_default=True)

    ab = sub.add_parser("ab", help="Fair 3L ETF spot grid vs underlying perpetual grid A/B")
    ab.add_argument("-c", "--config", default="configs/ab_etf_vs_perp.yaml")
    ab.add_argument("--cache-only", action="store_true")
    ab.add_argument("--pairs", default="", help="comma list, e.g. BTC,ETH,SOL")
    ab.add_argument("--output-dir", default="")
    ab.add_argument("--skip-fine", action="store_true")
    ab.add_argument("--skip-mc", action="store_true")

    dual = sub.add_parser("dual", help="Dual-engine Tech/Crypto state-switching perpetual backtest")
    dual.add_argument("-c", "--config", default="configs/dual_engine_perp.yaml")
    dual.add_argument("--cache-only", action="store_true")
    dual.add_argument("--output-dir", default="")
    dual.add_argument(
        "--download-trades",
        action="store_true",
        help="Download Binance aggTrades for CRYPTO_C1 window (2024-09~11)",
    )
    return p


def _overrides(args: argparse.Namespace) -> dict[str, Any]:
    o: dict[str, Any] = {}
    if getattr(args, "symbol", ""):
        o["symbol"] = args.symbol
        # Reuse style YAML on another contract: don't keep the bundled sample unless asked.
        o["prefer_sample"] = False
    if getattr(args, "interval", ""):
        o["interval"] = args.interval
    if getattr(args, "days", 0):
        o["days"] = args.days
    if getattr(args, "cache_only", False):
        o["cache_only"] = True
    if getattr(args, "prefer_sample", False):
        o["prefer_sample"] = True
    if getattr(args, "output_dir", ""):
        o["output_dir"] = args.output_dir
    if getattr(args, "run_name", ""):
        o["run_name"] = args.run_name
    if getattr(args, "strategy", ""):
        o.setdefault("strategy", {})["name"] = args.strategy
    if getattr(args, "stop_loss", -1.0) is not None and getattr(args, "stop_loss", -1.0) >= 0:
        o.setdefault("risk", {})["investment_sl_pct"] = float(args.stop_loss)
    if getattr(args, "grid", ""):
        o.setdefault("optimize", {})["grid"] = args.grid
    return o


def _cfg(args: argparse.Namespace) -> dict[str, Any]:
    path = getattr(args, "config", "") or None
    return load_config(path, overrides=_overrides(args))


def cmd_backtest(args: argparse.Namespace) -> int:
    from qtb.runner import run_backtest_job

    cfg = _cfg(args)
    cfg["mode"] = "backtest"
    result, written = run_backtest_job(cfg)
    print(json.dumps({"metrics": result.metrics, "artifacts": written}, indent=2, ensure_ascii=False, default=str))
    print(f"\nsummary: {written.get('summary')}")
    return 0


def cmd_optimize(args: argparse.Namespace) -> int:
    from qtb.runner import run_optimize_job

    cfg = _cfg(args)
    result, opt, written = run_optimize_job(cfg)
    best = opt.get("best") or {}
    print(
        json.dumps(
            {
                "n_combos": opt.get("n_combos"),
                "best_params": best.get("params"),
                "best_score": best.get("score"),
                "metrics": result.metrics,
                "anti_overfit": {
                    "train_test": (opt.get("anti_overfit") or {}).get("train_test"),
                    "monte_carlo": (opt.get("anti_overfit") or {}).get("monte_carlo"),
                },
                "artifacts": written,
            },
            indent=2,
            ensure_ascii=False,
            default=str,
        )
    )
    return 0


def cmd_report(args: argparse.Namespace) -> int:
    from qtb.runner import run_backtest_job, run_report_job

    if args.run_dir:
        info = run_report_job(args.run_dir)
        print(json.dumps(info, indent=2, ensure_ascii=False))
        summary = Path(info["summary"]) if "summary" in info else None
        if summary and summary.exists():
            print(summary.read_text(encoding="utf-8"))
        return 0
    cfg = _cfg(args)
    result, written = run_backtest_job(cfg)
    print(Path(written["summary"]).read_text(encoding="utf-8"))
    return 0


def cmd_batch(args: argparse.Namespace) -> int:
    from qtb.runner import run_batch_job

    cfg = _cfg(args)
    reports = run_batch_job(cfg)
    slim = [
        {"symbol": r["symbol"], "interval": r["interval"], "metrics": r["metrics"], "artifacts": r["artifacts"]}
        for r in reports
    ]
    print(json.dumps(slim, indent=2, ensure_ascii=False, default=str))
    return 0


def cmd_screen(args: argparse.Namespace) -> int:
    from qtb.screen import execute_screen

    return execute_screen(args)


def cmd_ab(args: argparse.Namespace) -> int:
    from qtb.ab.run import main as ab_main

    argv = ["-c", args.config]
    if args.cache_only:
        argv.append("--cache-only")
    if args.pairs:
        argv.extend(["--pairs", args.pairs])
    if args.output_dir:
        argv.extend(["--output-dir", args.output_dir])
    if args.skip_fine:
        argv.append("--skip-fine")
    if args.skip_mc:
        argv.append("--skip-mc")
    return ab_main(argv)


def cmd_dual(args: argparse.Namespace) -> int:
    from qtb.dual.run import load_dual_config, run_job

    cfg = load_dual_config(args.config)
    if args.cache_only:
        cfg["cache_only"] = True
    if args.output_dir:
        cfg["output_dir"] = args.output_dir
    if getattr(args, "download_trades", False):
        cfg["download_binance_trades"] = True
        cfg["run_binance_c1"] = True
    run_job(cfg)
    return 0


def cmd_live(args: argparse.Namespace) -> int:
    cfg = _cfg(args)
    broker = LiveBroker(config=cfg)
    print(
        json.dumps(
            {
                "dry_run": broker.dry_run,
                "forced": is_dry_run_forced(cfg),
                "mode": cfg.get("mode"),
                "note": (cfg.get("live") or {}).get("note"),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    if args.ping:
        rec = broker.send_order({"symbol": cfg.get("symbol"), "side": "buy", "size": 1})
        print(json.dumps(rec, indent=2, ensure_ascii=False))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {
        "backtest": cmd_backtest,
        "optimize": cmd_optimize,
        "report": cmd_report,
        "batch": cmd_batch,
        "live": cmd_live,
        "screen": cmd_screen,
        "batch-screen": cmd_screen,
        "ab": cmd_ab,
        "dual": cmd_dual,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
