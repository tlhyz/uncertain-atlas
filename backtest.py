"""Backtest runner and comparison stats."""

from __future__ import annotations

from typing import Any

import pandas as pd

from fees import VIP7_SPOT_70, VIP7_SPOT_NO_REBATE, FeeConfig, compare_fee_drag, effective_fee
from strategies.grid import GridParams, SpotGridSimulator
from strategies.martingale import MartingaleParams, SpotMartingaleSimulator


def run_grid(
    df: pd.DataFrame,
    fee_config: FeeConfig,
    params: GridParams | None = None,
) -> dict[str, Any]:
    params = params or GridParams()
    result = SpotGridSimulator(params, fee_config).run(df)
    return result.summary()


def run_martingale(
    df: pd.DataFrame,
    fee_config: FeeConfig,
    params: MartingaleParams | None = None,
) -> dict[str, Any]:
    params = params or MartingaleParams()
    result = SpotMartingaleSimulator(params, fee_config).run(df)
    return result.summary()


def side_by_side(
    df: pd.DataFrame,
    grid_params: GridParams | None = None,
    martingale_params: MartingaleParams | None = None,
    rebate_config: FeeConfig = VIP7_SPOT_70,
    no_rebate_config: FeeConfig = VIP7_SPOT_NO_REBATE,
) -> dict[str, Any]:
    """Run both strategies under no-rebate vs rebate fee models."""
    grid_params = grid_params or GridParams()
    martingale_params = martingale_params or MartingaleParams()

    out = {
        "meta": {
            "bars": len(df),
            "source": df.attrs.get("source", "unknown"),
            "symbol": df.attrs.get("symbol", ""),
            "interval": df.attrs.get("interval", ""),
            "start": str(df["timestamp"].iloc[0]) if "timestamp" in df.columns else "",
            "end": str(df["timestamp"].iloc[-1]) if "timestamp" in df.columns else "",
            "start_close": float(df["close"].iloc[0]),
            "end_close": float(df["close"].iloc[-1]),
        },
        "fee_example": {
            "vip7_maker_base": rebate_config.maker_rate,
            "vip7_taker_base": rebate_config.taker_rate,
            "rebate_rate": rebate_config.rebate_rate,
            "eff_maker": effective_fee(rebate_config.maker_rate, rebate_config.rebate_rate),
            "eff_taker": effective_fee(rebate_config.taker_rate, rebate_config.rebate_rate),
            "fee_on_10k_maker": compare_fee_drag(10_000, rebate_config.maker_rate, rebate_config.rebate_rate),
        },
        "grid": {
            "no_rebate": run_grid(df, no_rebate_config, grid_params),
            "with_rebate": run_grid(df, rebate_config, grid_params),
        },
        "martingale": {
            "no_rebate": run_martingale(df, no_rebate_config, martingale_params),
            "with_rebate": run_martingale(df, rebate_config, martingale_params),
        },
    }

    for strat in ("grid", "martingale"):
        a = out[strat]["no_rebate"]
        b = out[strat]["with_rebate"]
        out[strat]["fees_saved_by_rebate"] = round(a["total_fees"] - b["total_fees"], 4)
        out[strat]["pnl_lift_by_rebate"] = round(b["net_pnl"] - a["net_pnl"], 4)

    return out


def format_comparison(report: dict[str, Any]) -> str:
    """Human-readable side-by-side text report."""
    lines: list[str] = []
    m = report["meta"]
    lines.append("=" * 72)
    lines.append("Gate.io Spot Grid + Martingale Backtest (cash-flow research)")
    lines.append("=" * 72)
    lines.append(
        f"Data: {m.get('symbol')} {m.get('interval')} | bars={m.get('bars')} | "
        f"source={m.get('source')}"
    )
    lines.append(f"Range: {m.get('start')} -> {m.get('end')}")
    lines.append(f"Close: {m.get('start_close'):.2f} -> {m.get('end_close'):.2f}")
    fe = report["fee_example"]
    lines.append("-" * 72)
    lines.append(
        f"VIP7 base maker/taker: {fe['vip7_maker_base']*100:.3f}% / {fe['vip7_taker_base']*100:.3f}%"
    )
    lines.append(
        f"With {fe['rebate_rate']*100:.0f}% rebate -> eff maker/taker: "
        f"{fe['eff_maker']*100:.4f}% / {fe['eff_taker']*100:.4f}%"
    )
    ex = fe["fee_on_10k_maker"]
    lines.append(
        f"Example on 10,000 USDT maker notional: fee {ex['fee_no_rebate']:.4f} -> "
        f"{ex['fee_with_rebate']:.4f} (saved {ex['fee_saved']:.4f})"
    )
    lines.append("-" * 72)

    def block(title: str, key: str) -> None:
        lines.append(f"\n### {title}")
        hdr = f"{'metric':<22} {'no_rebate':>14} {'with_rebate':>14} {'delta':>12}"
        lines.append(hdr)
        a = report[key]["no_rebate"]
        b = report[key]["with_rebate"]
        for metric in (
            "net_pnl",
            "gross_pnl",
            "total_fees",
            "max_drawdown",
            "max_drawdown_pct",
            "cycles",
            "win_rate",
            "num_trades",
            "final_equity",
            "fee_drag",
        ):
            va, vb = a[metric], b[metric]
            if isinstance(va, float):
                lines.append(f"{metric:<22} {va:>14.4f} {vb:>14.4f} {vb-va:>12.4f}")
            else:
                lines.append(f"{metric:<22} {va:>14} {vb:>14} {vb-va:>12}")
        lines.append(
            f"{'fees_saved_by_rebate':<22} {report[key]['fees_saved_by_rebate']:>14.4f}"
        )
        lines.append(
            f"{'pnl_lift_by_rebate':<22} {report[key]['pnl_lift_by_rebate']:>14.4f}"
        )

    block("Spot Grid", "grid")
    block("Spot Martingale", "martingale")
    return "\n".join(lines)


def recommended_params(report: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    Starter parameter set tuned for VIP7 + 70% spot rebate fee edge.
    Tighter grids / slightly lower TP become viable when fee drag is cut ~70%.
    """
    return {
        "note": (
            "Starter set for Gate VIP7 + 70% spot rebate. "
            "Prefer spot over high-leverage futures Martingale. "
            "This is cash-flow research, NOT arbitrage. Size conservatively."
        ),
        "fee": {
            "maker_base": 0.0008,
            "taker_base": 0.00085,
            "rebate_rate": 0.70,
            "eff_maker": round(effective_fee(0.0008, 0.70), 8),
            "eff_taker": round(effective_fee(0.00085, 0.70), 8),
        },
        "spot_grid": {
            "spacing_pct": 0.008,  # 0.8% — viable with rebate (vs ~1.2% without)
            "grid_count": 24,
            "order_size_quote": 50.0,
            "initial_quote": 5000.0,
            "fee_as_maker": True,
            "rationale": "Tighter spacing OK because effective maker fee ~0.024%",
        },
        "spot_martingale": {
            "base_order_quote": 80.0,
            "multiplier": 1.4,
            "add_drop_pct": 0.018,
            "take_profit_pct": 0.012,  # slightly lower TP viable with rebate
            "max_adds": 4,
            "initial_quote": 5000.0,
            "fee_as_maker": False,
            "rationale": (
                "Mild multiplier + capped adds; rebate reduces fee drag on add/TP churn. "
                "Avoid leverage."
            ),
        },
        "risk_warning": (
            "Grid/Martingale can lock capital in drawdowns; past candles ≠ future. "
            "No live trading in this toolkit. Never risk funds you cannot afford to idle."
        ),
    }
