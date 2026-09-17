#!/usr/bin/env python3
"""P2-13 — PENGU/PUMP satellite cap 5% test (Gate BAR mode)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.ab.data import attach_funding, fetch_series_cached
from qtb.ab.engine import FeeSpec, run_perp_grid
from qtb.ab.fills import FillConfig
from qtb.data.funding import fetch_funding_cached
from qtb.dual.universe import (
    CRYPTO_MEME,
    MEME_MAX_ACCOUNT_FRAC,
    SYMBOL_PERP,
    TOTAL_CAPITAL,
    satellite_cap_budgets,
    satellite_cap_ok,
)


def _fee(rebate: float = 0.75) -> FeeSpec:
    return FeeSpec(0.00008, 0.0002, rebate)


def run_satellite_backtest(
    symbol: str,
    *,
    budget_usdt: float,
    leverage: float = 1.0,
    cache_only: bool = True,
) -> dict:
    perp = SYMBOL_PERP[symbol]
    bars = fetch_series_cached(perp, "1h", "futures", cache_only=cache_only)
    funding = fetch_funding_cached(perp, cache_only=cache_only)
    merged = attach_funding(bars, funding)

    fill = FillConfig("base", 0.05, 1, 2.0, 0.0001)
    r = run_perp_grid(
        merged,
        name=f"satellite_{symbol.lower()}",
        symbol=perp,
        fee=_fee(),
        fill=fill,
        initial=budget_usdt,
        target_notional=budget_usdt * leverage,
        leverage_hint=leverage,
        atr_step=0.50,
        atr_range=5.0,
        interval="1h",
    )

    start_eq = float(r.equity[0]) if len(r.equity) else budget_usdt
    final_eq = float(r.final_equity)
    ret = (final_eq - start_eq) / start_eq if start_eq > 0 else 0.0
    eq = r.equity
    peak = float(eq[0]) if len(eq) else start_eq
    max_dd = 0.0
    for v in eq:
        peak = max(peak, float(v))
        if peak > 0:
            max_dd = max(max_dd, (peak - float(v)) / peak)
    max_notional = max((abs(t.qty * t.price) for t in r.trades), default=0.0)

    return {
        "symbol": symbol,
        "perp": perp,
        "execution": "BAR",
        "data_source": "gate_futures_usdt_candlesticks",
        "bars": len(merged),
        "window_start": str(merged["timestamp"].iloc[0]),
        "window_end": str(merged["timestamp"].iloc[-1]),
        "budget_usdt": budget_usdt,
        "budget_frac_of_account": budget_usdt / TOTAL_CAPITAL,
        "leverage": leverage,
        "initial_equity": start_eq,
        "final_equity": final_eq,
        "total_return": ret,
        "max_drawdown": max_dd,
        "liquidated": bool(r.liquidated),
        "max_trade_notional": max_notional,
        "cap_respected": max_notional <= budget_usdt * leverage * 1.05,
    }


def write_report(out_dir: Path, results: list[dict], meta: dict) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "satellite_results.json").write_text(
        json.dumps({"meta": meta, "results": results}, indent=2, default=str),
        encoding="utf-8",
    )
    lines = [
        "# Crypto Satellite Cap Test — PENGU/PUMP",
        "",
        f"- **execution:** BAR (Gate 1h klines — no Binance aggTrades)",
        f"- **account cap:** {MEME_MAX_ACCOUNT_FRAC:.0%} combined ({TOTAL_CAPITAL * MEME_MAX_ACCOUNT_FRAC:.0f} USDT)",
        f"- **symbols:** {', '.join(CRYPTO_MEME)}",
        "",
        "## Results",
        "",
        "| Symbol | Budget | Return | MaxDD | Liq | Cap OK | Window |",
        "|--------|--------|--------|-------|-----|--------|--------|",
    ]
    for row in results:
        lines.append(
            f"| {row['symbol']} | {row['budget_usdt']:.0f}U "
            f"({100*row['budget_frac_of_account']:.1f}%) | "
            f"{100*row['total_return']:.1f}% | "
            f"{100*row['max_drawdown']:.1f}% | "
            f"{'Y' if row['liquidated'] else 'N'} | "
            f"{'Y' if row['cap_respected'] else 'N'} | "
            f"{row['window_start'][:10]}→{row['window_end'][:10]} |"
        )
    lines.extend([
        "",
        "## Policy check",
        "",
        f"- Combined budget: **{sum(r['budget_usdt'] for r in results):.0f} USDT** "
        f"({100 * sum(r['budget_frac_of_account'] for r in results):.1f}% of account)",
        f"- satellite_cap_ok: **{meta['cap_ok']}**",
        "",
        "## Notes",
        "",
        "- C1 tick-precise (2024-09→11) **blocked** — no Binance aggTrades manifests for PENGU/PUMP.",
        "- Gate history ~10k bars; PENGU list Jul-2025+, short sample — **WEAK evidence**.",
        "- Meme leverage capped at 1.0x per STRATEGY_CRYPTO.md.",
    ])
    (out_dir / "CRYPTO_SATELLITE_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="P2-13 satellite cap test")
    ap.add_argument("--output", default="outputs/experiments/crypto_satellite_cap")
    ap.add_argument("--leverage", type=float, default=1.0)
    ap.add_argument("--cache-only", action="store_true", default=True)
    args = ap.parse_args()

    budgets = satellite_cap_budgets()
    if not satellite_cap_ok(budgets):
        raise RuntimeError(f"satellite budgets exceed cap: {budgets}")

    results = []
    for sym in CRYPTO_MEME:
        print(f"[satellite] {sym} budget={budgets[sym]:.0f}U lev={args.leverage}x...")
        results.append(
            run_satellite_backtest(sym, budget_usdt=budgets[sym], leverage=args.leverage, cache_only=args.cache_only)
        )
        row = results[-1]
        print(
            f"[satellite] {sym} done return={100*row['total_return']:.1f}% "
            f"liq={row['liquidated']} cap_ok={row['cap_respected']}"
        )

    meta = {
        "task": "P2-13",
        "total_capital": TOTAL_CAPITAL,
        "meme_max_frac": MEME_MAX_ACCOUNT_FRAC,
        "combined_budget_usdt": sum(budgets.values()),
        "cap_ok": satellite_cap_ok(budgets),
        "leverage": args.leverage,
        "execution": "BAR",
    }
    out_dir = Path(args.output)
    write_report(out_dir, results, meta)
    print(f"[satellite] wrote {out_dir / 'CRYPTO_SATELLITE_REPORT.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
