#!/usr/bin/env python3
"""CLI for Gate.io spot grid + Martingale backtesting with fee rebates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow running as `python cli.py` from package root
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtest import format_comparison, recommended_params, side_by_side
from data import fetch_ohlcv, generate_sample_ohlcv
from fees import VIP7_SPOT_70, FeeConfig
from optimize import run_optimize
from strategies.grid import GridParams
from strategies.martingale import MartingaleParams


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Gate.io spot grid + Martingale backtester (VIP rebate aware)"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    demo = sub.add_parser("demo", help="One-command demo: fetch + compare + recommend")
    demo.add_argument("--symbol", default="BTCUSDT")
    demo.add_argument("--interval", default="1h", choices=["15m", "1h", "4h"])
    demo.add_argument("--days", type=int, default=90)
    demo.add_argument("--prefer", default="gate", choices=["binance", "gate", "sample"])
    demo.add_argument("--capital", type=float, default=5000.0)
    demo.add_argument("--optimize", action="store_true", help="Also run a small grid search")
    demo.add_argument("-o", "--output", default="", help="Write full report to file")

    bt = sub.add_parser("backtest", help="Run backtest with explicit params")
    bt.add_argument("--symbol", default="BTCUSDT")
    bt.add_argument("--interval", default="1h")
    bt.add_argument("--days", type=int, default=90)
    bt.add_argument("--prefer", default="gate", choices=["binance", "gate", "sample"])
    bt.add_argument("--capital", type=float, default=5000.0)
    bt.add_argument("--rebate", type=float, default=0.70)
    bt.add_argument("--grid-spacing", type=float, default=0.008)
    bt.add_argument("--grid-count", type=int, default=24)
    bt.add_argument("--mart-mult", type=float, default=1.4)
    bt.add_argument("--mart-drop", type=float, default=0.018)
    bt.add_argument("--mart-tp", type=float, default=0.012)
    bt.add_argument("--mart-max-adds", type=int, default=4)
    bt.add_argument("-o", "--output", default="")

    opt = sub.add_parser("optimize", help="Grid-search hyperparameters")
    opt.add_argument("--symbol", default="BTCUSDT")
    opt.add_argument("--interval", default="1h")
    opt.add_argument("--days", type=int, default=90)
    opt.add_argument("--prefer", default="gate", choices=["binance", "gate", "sample"])
    opt.add_argument("--capital", type=float, default=5000.0)
    opt.add_argument("-o", "--output", default="")

    fee = sub.add_parser("fee-example", help="Print VIP7 fee/rebate math")
    fee.add_argument("--notional", type=float, default=10000.0)
    fee.add_argument("--rebate", type=float, default=0.70)

    sub.add_parser("recommend", help="Print recommended starter params")

    gen = sub.add_parser("gen-sample", help="Write bundled synthetic CSV sample")
    gen.add_argument(
        "--path",
        default=str(ROOT / "data_sample" / "BTCUSDT_1h_sample.csv"),
    )
    gen.add_argument("--bars", type=int, default=90 * 24)

    return p


def _load_data(args: argparse.Namespace):
    df = fetch_ohlcv(
        symbol=getattr(args, "symbol", "BTCUSDT"),
        interval=getattr(args, "interval", "1h"),
        days=getattr(args, "days", 90),
        prefer=getattr(args, "prefer", "gate"),
    )
    return df


def cmd_demo(args: argparse.Namespace) -> int:
    df = _load_data(args)
    rec = recommended_params()
    gp = GridParams(
        spacing_pct=rec["spot_grid"]["spacing_pct"],
        grid_count=rec["spot_grid"]["grid_count"],
        order_size_quote=rec["spot_grid"]["order_size_quote"],
        initial_quote=args.capital,
        fee_as_maker=True,
    )
    mp = MartingaleParams(
        base_order_quote=rec["spot_martingale"]["base_order_quote"],
        multiplier=rec["spot_martingale"]["multiplier"],
        add_drop_pct=rec["spot_martingale"]["add_drop_pct"],
        take_profit_pct=rec["spot_martingale"]["take_profit_pct"],
        max_adds=rec["spot_martingale"]["max_adds"],
        initial_quote=args.capital,
        fee_as_maker=False,
    )
    report = side_by_side(df, grid_params=gp, martingale_params=mp)
    text = format_comparison(report)
    print(text)
    print("\n" + "=" * 72)
    print("RECOMMENDED STARTER PARAMS (VIP7 + 70% spot rebate fee edge)")
    print("=" * 72)
    print(json.dumps(rec, indent=2, ensure_ascii=False))

    if args.optimize:
        print("\n" + "=" * 72)
        print("OPTIMIZE (top results under VIP7+70%)")
        print("=" * 72)
        opt = run_optimize(df, VIP7_SPOT_70)
        print(json.dumps(opt, indent=2))

    if args.output:
        Path(args.output).write_text(text + "\n\n" + json.dumps(rec, indent=2), encoding="utf-8")
        print(f"\nWrote report to {args.output}")
    return 0


def cmd_backtest(args: argparse.Namespace) -> int:
    df = _load_data(args)
    rebate_cfg = FeeConfig(rebate_rate=args.rebate, label=f"VIP7 + {args.rebate:.0%} rebate")
    no_rebate = FeeConfig(rebate_rate=0.0, label="VIP7 no rebate")
    gp = GridParams(
        spacing_pct=args.grid_spacing,
        grid_count=args.grid_count,
        initial_quote=args.capital,
    )
    mp = MartingaleParams(
        multiplier=args.mart_mult,
        add_drop_pct=args.mart_drop,
        take_profit_pct=args.mart_tp,
        max_adds=args.mart_max_adds,
        initial_quote=args.capital,
    )
    report = side_by_side(df, gp, mp, rebate_config=rebate_cfg, no_rebate_config=no_rebate)
    text = format_comparison(report)
    print(text)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    return 0


def cmd_optimize(args: argparse.Namespace) -> int:
    df = _load_data(args)
    opt = run_optimize(df, VIP7_SPOT_70)
    print(json.dumps(opt, indent=2))
    if args.output:
        Path(args.output).write_text(json.dumps(opt, indent=2), encoding="utf-8")
    return 0


def cmd_fee_example(args: argparse.Namespace) -> int:
    from fees import compare_fee_drag, effective_fee

    base_m, base_t = 0.0008, 0.00085
    print(f"VIP7 maker base={base_m} -> effective={effective_fee(base_m, args.rebate)}")
    print(f"VIP7 taker base={base_t} -> effective={effective_fee(base_t, args.rebate)}")
    print(json.dumps(compare_fee_drag(args.notional, base_m, args.rebate), indent=2))
    return 0


def cmd_recommend(_: argparse.Namespace) -> int:
    print(json.dumps(recommended_params(), indent=2, ensure_ascii=False))
    return 0


def cmd_gen_sample(args: argparse.Namespace) -> int:
    df = generate_sample_ohlcv(Path(args.path), bars=args.bars)
    print(f"Wrote {len(df)} bars to {args.path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {
        "demo": cmd_demo,
        "backtest": cmd_backtest,
        "optimize": cmd_optimize,
        "fee-example": cmd_fee_example,
        "recommend": cmd_recommend,
        "gen-sample": cmd_gen_sample,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
