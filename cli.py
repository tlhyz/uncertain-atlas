#!/usr/bin/env python3
"""CLI for Gate.io multi-coin futures/spot grid + Martingale research (VIP rebate aware)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtest import format_comparison, recommended_params, side_by_side
from data import (
    WS_FUTURES_TRADES_DOC,
    api_stats,
    cache_path,
    fetch_candles_cached,
    fetch_gate_futures_trades,
    fetch_ohlcv,
    generate_sample_ohlcv,
    normalize_contract,
    reset_api_stats,
    resolve_gate_futures_contract,
)
from qtb.screen import add_screen_flags, execute_screen
from fees import VIP7_FUTURES_75, VIP7_SPOT_70, FeeConfig
from optimize import run_optimize
from optimize_futures import demo_fixed, estimate_combos, run_aggressive_dual
from strategies.grid import GridParams
from strategies.martingale import MartingaleParams


def build_parser() -> argparse.ArgumentParser:
    argv0 = Path(sys.argv[0]).as_posix() if sys.argv else "cli.py"
    prog = "python -m qtb.cli" if "qtb" in argv0 else "cli.py"
    p = argparse.ArgumentParser(
        prog=prog,
        description=(
            "Gate.io multi-coin backtester — USDT-M futures Martingale (aggressive dual) "
            "+ spot grid/martingale. Public market data only; no live orders / no API keys."
        ),
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    # ---- fetch (quota-aware candles) ----
    fetch = sub.add_parser("fetch", help="Fetch/cache Gate candlesticks (incremental, disk cache)")
    fetch.add_argument("--symbol", required=True, help="Gate contract e.g. BTC_USDT / ETH_USDT / 牛来_USDT")
    fetch.add_argument("--interval", default="5m", help="Prefer 5m/15m/1h over ticks (default 5m)")
    fetch.add_argument("--days", type=int, default=30)
    fetch.add_argument("--market", default="futures", choices=["futures", "spot"])
    fetch.add_argument("--cache-only", action="store_true", help="Never hit network; use disk cache only")
    fetch.add_argument("--force-refresh", action="store_true", help="Ignore cache and re-download")
    fetch.add_argument("--trades", action="store_true", help="Also pull a small REST trades sample (NOT for history)")
    fetch.add_argument("--trades-limit", type=int, default=200)
    fetch.add_argument("--show-ws-doc", action="store_true", help="Print WebSocket futures.trades howto")

    # ---- optimize (futures aggressive dual by default) ----
    opt = sub.add_parser("optimize", help="Optimize strategy params for a symbol")
    opt.add_argument("--symbol", default="BTC_USDT")
    opt.add_argument("--style", default="aggressive-dual", choices=["aggressive-dual", "spot"])
    opt.add_argument("--stop-loss", type=float, default=0.5, help="Investment-drawdown stop 0.5|0.7 (futures)")
    opt.add_argument("--interval", default="5m")
    opt.add_argument("--days", type=int, default=14)
    opt.add_argument("--market", default="futures", choices=["futures", "spot"])
    opt.add_argument("--cache-only", action="store_true")
    opt.add_argument("--grid", default="compact", choices=["compact", "medium", "full"],
                     help="Search size: compact(default, fast) | medium | full(heavy≈10k+/side)")
    opt.add_argument("--long-cap", type=float, default=950.0)
    opt.add_argument("--short-cap", type=float, default=1380.0)
    opt.add_argument("--leverage", type=float, default=5.0)
    opt.add_argument("--prefer", default="gate_futures", choices=["gate_futures", "gate", "binance", "sample"])
    opt.add_argument("-o", "--output", default="", help="Output prefix for json/md (futures)")
    opt.add_argument("--capital", type=float, default=5000.0, help="Spot optimize capital")

    # ---- demo ----
    demo = sub.add_parser("demo", help="Fast demo: fetch + fixed aggressive dual (or spot compare)")
    demo.add_argument("--symbol", default="BTC_USDT")
    demo.add_argument("--stop-loss", type=float, default=0.7)
    demo.add_argument("--interval", default="5m")
    demo.add_argument("--days", type=int, default=14)
    demo.add_argument("--style", default="aggressive-dual", choices=["aggressive-dual", "spot"])
    demo.add_argument("--cache-only", action="store_true")
    demo.add_argument("--long-cap", type=float, default=950.0)
    demo.add_argument("--short-cap", type=float, default=1380.0)
    demo.add_argument("--leverage", type=float, default=5.0)
    demo.add_argument("--prefer", default="gate_futures", choices=["gate_futures", "gate", "binance", "sample"])
    demo.add_argument("--capital", type=float, default=5000.0)
    demo.add_argument("--optimize", action="store_true", help="Also run compact optimize (futures) or spot search")
    demo.add_argument("-o", "--output", default="")

    # ---- legacy spot backtest ----
    bt = sub.add_parser("backtest", help="Spot grid+martingale backtest with explicit params")
    bt.add_argument("--symbol", default="BTC_USDT")
    bt.add_argument("--interval", default="1h")
    bt.add_argument("--days", type=int, default=90)
    bt.add_argument("--prefer", default="gate", choices=["binance", "gate", "gate_futures", "sample"])
    bt.add_argument("--capital", type=float, default=5000.0)
    bt.add_argument("--rebate", type=float, default=0.70)
    bt.add_argument("--grid-spacing", type=float, default=0.008)
    bt.add_argument("--grid-count", type=int, default=24)
    bt.add_argument("--mart-mult", type=float, default=1.4)
    bt.add_argument("--mart-drop", type=float, default=0.018)
    bt.add_argument("--mart-tp", type=float, default=0.012)
    bt.add_argument("--mart-max-adds", type=int, default=4)
    bt.add_argument("--cache-only", action="store_true")
    bt.add_argument("-o", "--output", default="")

    fee = sub.add_parser("fee-example", help="Print VIP7 fee/rebate math")
    fee.add_argument("--notional", type=float, default=10000.0)
    fee.add_argument("--rebate", type=float, default=0.70)
    fee.add_argument("--futures", action="store_true", help="Show futures VIP7+75% instead of spot")

    sub.add_parser("recommend", help="Print recommended starter params")

    gen = sub.add_parser("gen-sample", help="Write bundled synthetic CSV sample")
    gen.add_argument("--path", default=str(ROOT / "data_sample" / "BTCUSDT_1h_sample.csv"))
    gen.add_argument("--bars", type=int, default=90 * 24)

    screen = sub.add_parser(
        "screen",
        help="Screen liquid Gate USDT perps for high vol + low path efficiency",
    )
    add_screen_flags(screen, batch_default=False)

    batch = sub.add_parser(
        "batch-screen",
        help="Screen then batch-backtest top K picks (aggressive dual SL50)",
    )
    add_screen_flags(batch, batch_default=True)

    return p


def _resolve_symbol(symbol: str, market: str) -> str:
    if market == "futures":
        if symbol.endswith("_USDT") or symbol.endswith("_USD") or not symbol.isascii():
            # Chinese names often already end with _USDT
            if symbol.endswith("_USDT") or symbol.endswith("_USD"):
                return normalize_contract(symbol)
            try:
                return resolve_gate_futures_contract(symbol)
            except Exception:
                return normalize_contract(symbol)
        return normalize_contract(symbol)
    return normalize_contract(symbol) if symbol.isascii() else symbol.strip()


def _load_futures(args: argparse.Namespace):
    reset_api_stats()
    symbol = _resolve_symbol(args.symbol, getattr(args, "market", "futures"))
    df = fetch_candles_cached(
        symbol,
        interval=getattr(args, "interval", "5m"),
        days=getattr(args, "days", 14),
        market="futures",
        cache_only=getattr(args, "cache_only", False),
        force_refresh=getattr(args, "force_refresh", False),
    )
    return symbol, df


def _load_spotish(args: argparse.Namespace):
    reset_api_stats()
    prefer = getattr(args, "prefer", "gate")
    return fetch_ohlcv(
        symbol=getattr(args, "symbol", "BTC_USDT"),
        interval=getattr(args, "interval", "1h"),
        days=getattr(args, "days", 90),
        prefer=prefer,
        cache_only=getattr(args, "cache_only", False),
    )


def cmd_fetch(args: argparse.Namespace) -> int:
    if args.show_ws_doc:
        print(WS_FUTURES_TRADES_DOC)
    reset_api_stats()
    symbol = _resolve_symbol(args.symbol, args.market)
    print(f"Symbol resolved: {symbol} | market={args.market} | interval={args.interval} | days={args.days}")
    print(f"Cache file: {cache_path(symbol, args.interval, market=args.market)}")
    df = fetch_candles_cached(
        symbol,
        interval=args.interval,
        days=args.days,
        market=args.market,
        cache_only=args.cache_only,
        force_refresh=args.force_refresh,
    )
    stats = api_stats()
    print(
        f"bars={len(df)} | {df['timestamp'].iloc[0]} -> {df['timestamp'].iloc[-1]} | "
        f"close {df['close'].iloc[0]} -> {df['close'].iloc[-1]}"
    )
    print(
        f"source={df.attrs.get('source')} | cache_hit={df.attrs.get('cache_hit')} | "
        f"api_calls={df.attrs.get('api_calls', stats['calls'])} | retries_429={stats['retries_429']}"
    )
    if args.trades:
        if args.days > 2:
            print(
                "WARNING: REST trades are NOT for multi-day history. "
                "Pulling a small recent sample only. Use WS futures.trades for live."
            )
        tdf = fetch_gate_futures_trades(symbol, limit=args.trades_limit)
        print(f"trades sample rows={len(tdf)} source={tdf.attrs.get('source')}")
        print(tdf.attrs.get("note", ""))
    return 0


def cmd_optimize(args: argparse.Namespace) -> int:
    if args.style == "spot":
        df = _load_spotish(args)
        opt = run_optimize(df, VIP7_SPOT_70)
        print(json.dumps(opt, indent=2))
        if args.output:
            Path(args.output).write_text(json.dumps(opt, indent=2), encoding="utf-8")
        return 0

    # futures aggressive dual
    n = estimate_combos(args.grid)
    print(f"Search grid={args.grid} → ~{n} combinations per side (LONG+SHORT ≈ {2*n})")
    if args.grid == "full" and args.days >= 14:
        print(
            "HINT: full×14d can take a long time. Default is --grid compact. "
            "Re-run with --grid compact|medium if this is too heavy."
        )
    symbol, df = _load_futures(args)
    print(f"Data bars={len(df)} source={df.attrs.get('source')} api_calls={df.attrs.get('api_calls')}")
    payload = run_aggressive_dual(
        df,
        symbol=symbol,
        stop_loss=args.stop_loss,
        long_cap=args.long_cap,
        short_cap=args.short_cap,
        leverage=args.leverage,
        grid=args.grid,
        days=args.days,
        interval=args.interval,
        out_prefix=args.output or None,
    )
    dual = payload["best_dual"]
    print(json.dumps({
        "symbol": symbol,
        "stop_loss": args.stop_loss,
        "grid": args.grid,
        "dual_score": dual["dual_score"],
        "combined_realized_cashflow": dual["combined_realized_cashflow"],
        "combined_cycles": dual["combined_cycles"],
        "combined_stop_outs": dual.get("combined_stop_outs"),
        "long_params": dual["long"]["params"],
        "short_params": dual["short"]["params"],
        "api_stats": api_stats(),
    }, indent=2, ensure_ascii=False))
    return 0


def cmd_demo(args: argparse.Namespace) -> int:
    if args.style == "spot":
        df = _load_spotish(args)
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
        if args.optimize:
            print(json.dumps(run_optimize(df, VIP7_SPOT_70), indent=2))
        if args.output:
            Path(args.output).write_text(text, encoding="utf-8")
        return 0

    symbol, df = _load_futures(args)
    print(f"Demo {symbol} SL={args.stop_loss} bars={len(df)} source={df.attrs.get('source')}")
    dual = demo_fixed(
        df,
        stop_loss_pct=args.stop_loss,
        long_cap=args.long_cap,
        short_cap=args.short_cap,
        leverage=args.leverage,
    )
    print(json.dumps({
        "symbol": symbol,
        "fee": VIP7_FUTURES_75.label,
        "stop_loss": args.stop_loss,
        "dual": {
            "score": dual["dual_score"],
            "cashflow": dual["combined_realized_cashflow"],
            "net_pnl": dual["combined_net_pnl"],
            "cycles": dual["combined_cycles"],
            "stop_outs": dual["combined_stop_outs"],
            "long_liq": dual["long_liq"],
            "short_liq": dual["short_liq"],
        },
        "long_params": dual["long"]["params"],
        "short_params": dual["short"]["params"],
        "api_stats": api_stats(),
    }, indent=2, ensure_ascii=False))

    if args.optimize:
        print("\n--- compact optimize ---")
        run_aggressive_dual(
            df,
            symbol=symbol,
            stop_loss=args.stop_loss,
            long_cap=args.long_cap,
            short_cap=args.short_cap,
            leverage=args.leverage,
            grid="compact",
            days=args.days,
            interval=args.interval,
            out_prefix=args.output or None,
        )
    elif args.output:
        Path(args.output).write_text(json.dumps(dual, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote {args.output}")
    return 0


def cmd_backtest(args: argparse.Namespace) -> int:
    df = _load_spotish(args)
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


def cmd_fee_example(args: argparse.Namespace) -> int:
    from fees import compare_fee_drag, effective_fee

    if args.futures:
        cfg = VIP7_FUTURES_75
        print(f"{cfg.label}")
        print(f"maker base={cfg.maker_rate} -> effective={cfg.effective_maker}")
        print(f"taker base={cfg.taker_rate} -> effective={cfg.effective_taker}")
        print(json.dumps(compare_fee_drag(args.notional, cfg.maker_rate, cfg.rebate_rate), indent=2))
        return 0
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


def cmd_screen(args: argparse.Namespace) -> int:
    return execute_screen(args)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {
        "fetch": cmd_fetch,
        "optimize": cmd_optimize,
        "demo": cmd_demo,
        "backtest": cmd_backtest,
        "fee-example": cmd_fee_example,
        "recommend": cmd_recommend,
        "gen-sample": cmd_gen_sample,
        "screen": cmd_screen,
        "batch-screen": cmd_screen,
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
