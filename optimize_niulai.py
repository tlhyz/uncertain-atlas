#!/usr/bin/env python3
"""Optimize Gate futures Martingale for 牛来_USDT; write Chinese report."""

from __future__ import annotations

import json
import math
import sys
import time
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from data import fetch_gate_candles, fetch_gate_futures_candles
from fees import VIP7_FUTURES_75, VIP7_SPOT_70
from optimize import optimize_grid
from strategies.futures_martingale import FuturesMartingaleParams, FuturesMartingaleSimulator
from strategies.martingale import MartingaleParams, SpotMartingaleSimulator

OUT_JSON = ROOT / "opt_niulai_results.json"
OUT_MD = ROOT / "opt_niulai_report.md"
DEMO_SNIP = ROOT / "opt_niulai_demo_snippet.txt"


def notional_factor(multiplier: float, max_adds: int) -> float:
    """Sum of geometric notionals for base + max_adds adds (max_adds+1 fills)."""
    n = max_adds + 1
    if abs(multiplier - 1.0) < 1e-12:
        return float(n)
    return (multiplier**n - 1.0) / (multiplier - 1.0)


def sized_base(capital: float, leverage: float, multiplier: float, max_adds: int, fill_frac: float = 0.75) -> float:
    fac = notional_factor(multiplier, max_adds)
    # margin for full ladder ≈ base * fac / leverage
    base = (fill_frac * capital * leverage) / max(fac, 1e-9)
    return max(1.0, round(base, 4))


def risk_score(net_pnl: float, max_dd: float, liquidated: bool, total_fees: float = 0.0) -> float:
    if liquidated:
        return -1e9
    return net_pnl - 0.45 * max_dd - 0.10 * total_fees


def optimize_futures(
    df,
    directions=("long", "short"),
    capital: float = 1000.0,
    top_k: int = 15,
):
    max_adds_list = [4, 6, 8, 12, 20]
    multipliers = [1.2, 1.4, 1.5, 1.8, 2.0]
    drop_pcts = [0.008, 0.012, 0.018, 0.025, 0.035]  # 0.8%..3.5%
    tp_pcts = [0.004, 0.006, 0.008, 0.012, 0.015]
    leverages = [2, 3, 5]
    fee = VIP7_FUTURES_75

    results = []
    combos = list(product(directions, max_adds_list, multipliers, drop_pcts, tp_pcts, leverages))
    t0 = time.time()
    for i, (direction, max_adds, mult, drop, tp, lev) in enumerate(combos):
        base = sized_base(capital, lev, mult, max_adds)
        params = FuturesMartingaleParams(
            base_order_quote=base,
            multiplier=mult,
            add_drop_pct=drop,
            take_profit_pct=tp,
            max_adds=max_adds,
            initial_margin=capital,
            leverage=float(lev),
            direction=direction,
            fee_as_maker=False,
        )
        r = FuturesMartingaleSimulator(params, fee).run(df)
        s = r.summary()
        s["score"] = round(risk_score(r.net_pnl, r.max_drawdown, r.liquidated, r.total_fees), 4)
        s["params"] = {
            "direction": direction,
            "max_adds": max_adds,
            "multiplier": mult,
            "add_drop_pct": drop,
            "take_profit_pct": tp,
            "leverage": lev,
            "base_order_quote": base,
            "initial_margin": capital,
        }
        s["max_adds_hit"] = r.stats.get("max_adds_hit", 0)
        s["max_margin_used"] = round(r.stats.get("max_margin_used", 0), 2)
        results.append(s)
        if (i + 1) % 500 == 0:
            print(f"  ... {i+1}/{len(combos)} done ({time.time()-t0:.1f}s)", flush=True)

    results.sort(key=lambda x: x["score"], reverse=True)
    return results, combos


def blowup_demo(df, capital: float = 1000.0):
    """Show why max_adds=90 is catastrophic (margin ladder explosion)."""
    rows = []
    for mult in (1.2, 1.5, 2.0):
        for max_adds in (8, 20, 40, 90):
            fac = notional_factor(mult, max_adds)
            for lev in (5,):
                # If user forces base such that first order is small but 90 adds
                # Use same sizing as if they set investment and still allow 90 (won't fit)
                base_fit = sized_base(capital, lev, mult, min(max_adds, 12))
                margin_if_full = base_fit * fac / lev
                rows.append(
                    {
                        "multiplier": mult,
                        "max_adds": max_adds,
                        "leverage": lev,
                        "base_used": base_fit,
                        "notional_factor": round(fac, 2),
                        "margin_if_full_ladder": round(margin_if_full, 2),
                        "capital": capital,
                        "overshoot_x": round(margin_if_full / capital, 2),
                    }
                )
    # Also run a dangerous mid-aggressive backtest (max_adds=20, mult=1.5, drop=1.2%, lev=5)
    danger_params = FuturesMartingaleParams(
        base_order_quote=sized_base(capital, 5, 1.5, 20),
        multiplier=1.5,
        add_drop_pct=0.012,
        take_profit_pct=0.008,
        max_adds=20,
        initial_margin=capital,
        leverage=5.0,
        direction="long",
    )
    danger = FuturesMartingaleSimulator(danger_params, VIP7_FUTURES_75).run(df).summary()
    danger["params"] = {
        "max_adds": 20,
        "multiplier": 1.5,
        "add_drop_pct": 0.012,
        "take_profit_pct": 0.008,
        "leverage": 5,
    }
    return rows, danger


def dual_proxy(best_long, best_short, capital_each: float):
    """Naive dual = run independent L+S with split capital (no netting)."""
    return {
        "note": "独立双开近似：各用一半/指定保证金，盈亏与回撤简单相加（未模拟对锁/净仓）",
        "capital_each": capital_each,
        "long": best_long,
        "short": best_short,
        "combined_net_pnl": round(best_long["net_pnl"] + best_short["net_pnl"], 4),
        "combined_max_dd_proxy": round(best_long["max_drawdown"] + best_short["max_drawdown"], 4),
        "either_liquidated": best_long.get("liquidated") or best_short.get("liquidated"),
    }


def main():
    symbol = "牛来_USDT"
    days = 18  # listing ~2026-08-18; use all available (~18d)
    interval = "5m"
    capital = 1000.0

    print(f"Fetching Gate futures {symbol} {interval} days={days} ...")
    df = fetch_gate_futures_candles(symbol, interval=interval, days=days)
    print(f"Got {len(df)} bars | {df['timestamp'].iloc[0]} -> {df['timestamp'].iloc[-1]}")
    print(f"Close {df['close'].iloc[0]:.5f} -> {df['close'].iloc[-1]:.5f}")

    # Spot data for grid comparison
    spot_err = None
    try:
        df_spot = fetch_gate_candles(symbol, interval="15m", days=days)
        print(f"Spot bars: {len(df_spot)}")
    except Exception as e:
        df_spot = df.copy()
        spot_err = str(e)
        print(f"Spot fetch failed ({e}); using futures candles as proxy for spot grid")

    print("Running futures martingale grid search (LONG+SHORT) ...")
    all_res, combos = optimize_futures(df, capital=capital, top_k=20)
    print(f"Evaluated {len(combos)} combos; top score={all_res[0]['score']}")

    long_res = [r for r in all_res if r["params"]["direction"] == "long"]
    short_res = [r for r in all_res if r["params"]["direction"] == "short"]
    # Prefer non-liquidated and score
    def pick(res_list, safer=True):
        pool = [r for r in res_list if not r.get("liquidated")]
        if safer:
            # prefer max_adds <= 8 and leverage <= 3 among top 50 by score
            safe = [r for r in pool[:80] if r["params"]["max_adds"] <= 8 and r["params"]["leverage"] <= 3]
            if safe:
                # among safe, best score with secondary: higher net/dd
                safe.sort(
                    key=lambda x: (
                        x["score"],
                        x["net_pnl"] / max(x["max_drawdown"], 1.0),
                    ),
                    reverse=True,
                )
                return safe[0]
        return pool[0] if pool else res_list[0]

    best_long_raw = long_res[0]
    best_short_raw = short_res[0]
    best_long_safe = pick(long_res, safer=True)
    best_short_safe = pick(short_res, safer=True)

    # Primary recommendation: pick better of safe long/short by score
    primary = best_long_safe if best_long_safe["score"] >= best_short_safe["score"] else best_short_safe

    # Dual proxy with recommended safer params (re-run each side with same style caps)
    dual = dual_proxy(best_long_safe, best_short_safe, capital_each=capital)

    blowup_rows, danger = blowup_demo(df, capital=capital)

    # Spot grid + spot martingale on same window
    print("Running spot grid optimize ...")
    grid_top = optimize_grid(
        df_spot,
        fee_config=VIP7_SPOT_70,
        spacing_pcts=(0.008, 0.012, 0.018, 0.025),
        grid_counts=(12, 20, 24),
        order_sizes=(30.0, 50.0),
        initial_quote=capital,
        top_k=5,
    )
    spot_mart = SpotMartingaleSimulator(
        MartingaleParams(
            base_order_quote=80.0,
            multiplier=1.4,
            add_drop_pct=0.018,
            take_profit_pct=0.012,
            max_adds=4,
            initial_quote=capital,
        ),
        VIP7_SPOT_70,
    ).run(df_spot).summary()

    # Aggressive user-style proxy (max_adds capped at 20 for runnable size; 90 flagged separately)
    user_style_long = FuturesMartingaleSimulator(
        FuturesMartingaleParams(
            base_order_quote=sized_base(950, 5, 1.5, 20),
            multiplier=1.5,
            add_drop_pct=0.012,
            take_profit_pct=0.006,
            max_adds=20,
            initial_margin=950.0,
            leverage=5.0,
            direction="long",
        ),
        VIP7_FUTURES_75,
    ).run(df).summary()
    user_style_short = FuturesMartingaleSimulator(
        FuturesMartingaleParams(
            base_order_quote=sized_base(1383, 5, 1.5, 20),
            multiplier=1.5,
            add_drop_pct=0.012,
            take_profit_pct=0.006,
            max_adds=20,
            initial_margin=1383.0,
            leverage=5.0,
            direction="short",
        ),
        VIP7_FUTURES_75,
    ).run(df).summary()

    payload = {
        "meta": {
            "symbol": symbol,
            "interval": interval,
            "days_requested": days,
            "bars": len(df),
            "start": str(df["timestamp"].iloc[0]),
            "end": str(df["timestamp"].iloc[-1]),
            "start_close": float(df["close"].iloc[0]),
            "end_close": float(df["close"].iloc[-1]),
            "source": df.attrs.get("source"),
            "fee_model": {
                "maker_base": VIP7_FUTURES_75.maker_rate,
                "taker_base": VIP7_FUTURES_75.taker_rate,
                "rebate": VIP7_FUTURES_75.rebate_rate,
                "eff_maker": VIP7_FUTURES_75.effective_maker,
                "eff_taker": VIP7_FUTURES_75.effective_taker,
                "funding": "omitted (Gate funding_interval=4h; rate varies; not in backtest)",
            },
            "combos_evaluated": len(combos),
            "capital_per_side": capital,
            "spot_err": spot_err,
        },
        "top20": all_res[:20],
        "top_long": long_res[:10],
        "top_short": short_res[:10],
        "best_long_raw": best_long_raw,
        "best_short_raw": best_short_raw,
        "best_long_safe": best_long_safe,
        "best_short_safe": best_short_safe,
        "primary": primary,
        "dual_proxy": dual,
        "blowup_ladder": blowup_rows,
        "danger_deep_add": danger,
        "user_style_proxy": {"long": user_style_long, "short": user_style_short},
        "spot_grid_top": grid_top,
        "spot_martingale": spot_mart,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")

    # Demo snippet
    demo_lines = [
        f"$ python optimize_niulai.py",
        f"Fetching Gate futures {symbol} {interval} days={days} ...",
        f"Got {len(df)} bars | {df['timestamp'].iloc[0]} -> {df['timestamp'].iloc[-1]}",
        f"Close {df['close'].iloc[0]:.5f} -> {df['close'].iloc[-1]:.5f}",
        f"Evaluated {len(combos)} combos",
        f"PRIMARY direction={primary['params']['direction']} score={primary['score']} "
        f"net_pnl={primary['net_pnl']} maxDD={primary['max_drawdown']} "
        f"params={primary['params']}",
        f"Eff fees maker/taker={VIP7_FUTURES_75.effective_maker}/{VIP7_FUTURES_75.effective_taker}",
    ]
    DEMO_SNIP.write_text("\n".join(demo_lines) + "\n", encoding="utf-8")

    write_report(payload)
    print(f"Wrote {OUT_MD}")
    return 0


def pct(x: float) -> str:
    return f"{x * 100:.2f}%"


def write_report(payload: dict) -> None:
    m = payload["meta"]
    p = payload["primary"]["params"]
    prim = payload["primary"]
    bl = payload["best_long_safe"]
    bs = payload["best_short_safe"]
    ug = payload["user_style_proxy"]
    grid = payload["spot_grid_top"][0] if payload["spot_grid_top"] else {}
    spot_m = payload["spot_martingale"]

    # Capital split suggestion based on ~2333 total from screenshot
    total_cap = 1383 + 950  # ~2333
    # Safer: 60% primary, 25% opposite light, 15% cash buffer — or single direction
    if p["direction"] == "long":
        split = {
            "主策略_LONG": round(total_cap * 0.55, 0),
            "轻仓对侧_SHORT": round(total_cap * 0.20, 0),
            "现金缓冲": round(total_cap * 0.25, 0),
        }
    else:
        split = {
            "主策略_SHORT": round(total_cap * 0.55, 0),
            "轻仓对侧_LONG": round(total_cap * 0.20, 0),
            "现金缓冲": round(total_cap * 0.25, 0),
        }

    lines = []
    lines.append("# 牛来_USDT 期货马丁参数优化报告")
    lines.append("")
    lines.append(f"> 生成时间（UTC）：{m['end']} 附近 | 研究用途，非投资建议，无实盘下单。")
    lines.append("")
    lines.append("## 1. 数据与费用模型")
    lines.append("")
    lines.append(f"- **合约**：`{m['symbol']}`（Gate USDT 永续，公开接口可解析中文名）")
    lines.append(f"- **K线**：`{m['interval']}`，约 {m['days_requested']} 天可用窗口（上线约 2026-08-18）")
    lines.append(f"- **样本**：{m['bars']} 根 | {m['start']} → {m['end']}")
    lines.append(f"- **价格**：{m['start_close']:.5f} → {m['end_close']:.5f}")
    lines.append(f"- **来源**：`{m['source']}`")
    lines.append("- **VIP7 期货费率**：Maker 0.008% / Taker 0.02%；返佣 75%")
    lines.append(
        f"  - 有效费率 ≈ Maker **{pct(m['fee_model']['eff_maker'])}** / Taker **{pct(m['fee_model']['eff_taker'])}**"
    )
    lines.append(f"- **资金费**：{m['fee_model']['funding']}（回测未计入，实盘双向持仓时尤需注意）")
    lines.append(f"- **搜索组合数**：{m['combos_evaluated']}（LONG+SHORT × 安全网格参数）")
    lines.append("")
    lines.append("## 2. 风格诊断（对照截图 OCR）")
    lines.append("")
    lines.append("| 项目 | Bot A SHORT | Bot B LONG | 解读 |")
    lines.append("|---|---|---|---|")
    lines.append("| 方向/杠杆 | SHORT 5x | LONG 5x | 激进双向对开 |")
    lines.append("| 运行时长 | ~9h49m | ~10h39m | 高换手短周期 |")
    lines.append("| 投资额 | ~1383 USDT | ~950 USDT | 合计约 2333 |")
    lines.append("| 已实现 | +67.76 (+4.89%) | +41.85 (+4.4%) | 震荡里好看 |")
    lines.append("| 加仓 | 0/90 | **23/90** | B 已深套路径 |")
    lines.append("| 均价 vs 现价 | 均 0.11484 / 现 0.11478 | 均 **0.12205** / 现 **0.11478** | LONG 浮亏扩大 |")
    lines.append("| 强平价 | ~2.94（远离） | **0.033** | 深加仓后名义敞口巨大，强平价被“撑远”但保证金消耗极快 |")
    lines.append("| 完成轮次 | ~42 | ~101 | 小止盈高频，费用与滑点敏感 |")
    lines.append("")
    lines.append("**风格标签**：山寨币 + 双向期货马丁 + **max_adds=90（极端）** + 5x + 高换手。")
    lines.append("VIP7+75% 返佣只能降低费用拖累，**不能对冲单边趋势与保证金耗尽风险**。")
    lines.append("")
    lines.append("## 3. 为何 max_adds=90 + 双向 5x 危险")
    lines.append("")
    lines.append("1. **几何加仓爆炸**：保证金需求随 `multiplier^(max_adds)` 级增长。max=90 在任何 `multiplier≥1.2` 下都会使满仓阶梯保证金远超账户（见下表）。")
    lines.append("2. **Bot B 已示警**：23/90 且现价显著低于均价 → 路径依赖已进入“越跌越加”；剩余 67 次加仓额度是心理安慰，不是安全垫。")
    lines.append("3. **双向 5x**：同币种 LONG+SHORT 在剧烈单边时，一侧盈利往往覆盖不了另一侧保证金占用与强平；再叠加 4h 资金费，双边都可能付钱。")
    lines.append("4. **强平价“看起来很远”是幻觉**：深度加仓后名义仓位巨大，一次急跌/插针即可打穿维持保证金。")
    lines.append("5. **回测代理**：本工具将 max_adds=90 标为 **blowup risk**，搜索空间刻意不含 90，只用 [4,6,8,12,20]。")
    lines.append("")
    lines.append("### 加仓阶梯保证金超限示意（投资 1000 USDT，5x，同口径底仓）")
    lines.append("")
    lines.append("| 乘数 | max_adds | 名义倍数合计 | 满阶梯保证金 | 相对本金倍数 |")
    lines.append("|---:|---:|---:|---:|---:|")
    for row in payload["blowup_ladder"]:
        if row["multiplier"] in (1.2, 1.5, 2.0) and row["max_adds"] in (8, 20, 90):
            lines.append(
                f"| {row['multiplier']} | {row['max_adds']} | {row['notional_factor']} | "
                f"{row['margin_if_full_ladder']} | **{row['overshoot_x']}x** |"
            )
    lines.append("")
    lines.append(
        f"用户风格代理回测（max_adds=20 封顶可跑，非 90）："
        f" LONG net={ug['long']['net_pnl']} liq={ug['long']['liquidated']} maxDD={ug['long']['max_drawdown']}；"
        f" SHORT net={ug['short']['net_pnl']} liq={ug['short']['liquidated']} maxDD={ug['short']['max_drawdown']}。"
    )
    lines.append("")
    lines.append("## 4. 优化结果摘要（风险调整：净盈亏 − 0.45×最大回撤 − 0.1×费用）")
    lines.append("")
    lines.append("### 4.1 主推荐（Primary，偏安全：max_adds≤8 且杠杆≤3）")
    lines.append("")
    lines.append(f"- **方向**：`{p['direction'].upper()}`")
    lines.append(f"- **投资额（单策略回测本金）**：{p['initial_margin']} USDT")
    lines.append(f"- **首单名义**：{p['base_order_quote']} USDT（按满阶梯约占本金 75% 保证金自动缩放到可存活）")
    lines.append(f"- **加仓倍数 multiplier**：{p['multiplier']}")
    lines.append(f"- **跌/涨多少加仓 drop**：{pct(p['add_drop_pct'])}")
    lines.append(f"- **止盈 tp（相对均价）**：{pct(p['take_profit_pct'])}")
    lines.append(f"- **最大加仓次数 max_adds**：{p['max_adds']}  （**禁止 90**）")
    lines.append(f"- **杠杆 leverage**：{p['leverage']}x")
    lines.append(
        f"- **回测表现**：净盈亏 **{prim['net_pnl']}** | 最大回撤 **{prim['max_drawdown']}** "
        f"({pct(prim['max_drawdown_pct'])}) | 轮次 {prim['cycles']} | 胜率 {pct(prim['win_rate'])} | "
        f"强平={prim['liquidated']} | score={prim['score']}"
    )
    lines.append("")
    lines.append("### 4.2 安全 LONG / SHORT 对照")
    lines.append("")
    lines.append("| | LONG 安全最优 | SHORT 安全最优 |")
    lines.append("|---|---|---|")
    lines.append(
        f"| 参数 | mult={bl['params']['multiplier']}, drop={pct(bl['params']['add_drop_pct'])}, "
        f"tp={pct(bl['params']['take_profit_pct'])}, adds={bl['params']['max_adds']}, "
        f"lev={bl['params']['leverage']}x | "
        f"mult={bs['params']['multiplier']}, drop={pct(bs['params']['add_drop_pct'])}, "
        f"tp={pct(bs['params']['take_profit_pct'])}, adds={bs['params']['max_adds']}, "
        f"lev={bs['params']['leverage']}x |"
    )
    lines.append(
        f"| 净盈亏 / 最大回撤 | {bl['net_pnl']} / {bl['max_drawdown']} | {bs['net_pnl']} / {bs['max_drawdown']} |"
    )
    lines.append(f"| score | {bl['score']} | {bs['score']} |")
    lines.append("")
    lines.append("### 4.3 原始最高分（可能更激进，仅供对照，不作为主推荐）")
    lines.append("")
    br, bsr = payload["best_long_raw"], payload["best_short_raw"]
    lines.append(
        f"- LONG raw: {br['params']} → net={br['net_pnl']} dd={br['max_drawdown']} liq={br['liquidated']} score={br['score']}"
    )
    lines.append(
        f"- SHORT raw: {bsr['params']} → net={bsr['net_pnl']} dd={bsr['max_drawdown']} liq={bsr['liquidated']} score={bsr['score']}"
    )
    lines.append("")
    lines.append("### 4.4 双开代理（不推荐作为默认）")
    lines.append("")
    d = payload["dual_proxy"]
    lines.append(
        f"- 将安全 LONG + 安全 SHORT 简单相加：合计净盈亏 ≈ {d['combined_net_pnl']}，"
        f"回撤代理合计 ≈ {d['combined_max_dd_proxy']}（高估分散、低估相关风险）。"
    )
    lines.append("- **建议默认只跑主推荐单方向**；若坚持双开，对侧仓位 ≤ 主仓 1/3，且两边 max_adds≤6。")
    lines.append("")
    lines.append("### 4.5 现货网格备选（同币种窗口）")
    lines.append("")
    if grid:
        gp = grid.get("params", {})
        lines.append(
            f"- 现货网格 Top1：spacing={pct(gp.get('spacing_pct', 0))}, grids≈{gp.get('grid_count')}, "
            f"单格 {gp.get('order_size_quote')} → net={grid.get('net_pnl')} dd={grid.get('max_drawdown')} "
            f"score={grid.get('score')}（VIP7+70% 现货返佣）"
        )
    lines.append(
        f"- 现货马丁（温和）：mult=1.4 drop=1.8% tp=1.2% adds=4 → net={spot_m.get('net_pnl')} "
        f"dd={spot_m.get('max_drawdown')}（无杠杆，更抗插针）"
    )
    lines.append("- 若无法接受期货强平风险，优先降级为 **现货网格/现货马丁**。")
    lines.append("")
    lines.append("## 5. Gate 机器人字段映射（主推荐）")
    lines.append("")
    lines.append("| Gate 字段 | 填写值 | 说明 |")
    lines.append("|---|---|---|")
    lines.append(f"| 投资额 | **{int(split[list(split.keys())[0]])} USDT**（见资金分配） | 单机器人保证金预算 |")
    lines.append(f"| 加仓倍数 | **{p['multiplier']}** | 每层名义 = 上层 × 倍数 |")
    lines.append(
        f"| 跌多少加仓 / 涨多少加仓 | **{p['add_drop_pct']*100:.1f}%** | LONG 看跌幅；SHORT 看涨幅 |"
    )
    lines.append(f"| 止盈 | **{p['take_profit_pct']*100:.1f}%** | 相对持仓均价 |")
    lines.append(f"| 最大加仓次数 | **{p['max_adds']}** | 严禁 90；建议硬顶 ≤8 |")
    lines.append(f"| 杠杆 | **{p['leverage']}x** | 5x 仅在 max_adds≤4 且 drop≥2.5% 时偶发可试 |")
    lines.append(f"| 方向 | **{p['direction'].upper()}** | 主策略只开一侧 |")
    lines.append(f"| 首单/底仓名义（参考） | **{p['base_order_quote']} USDT** | 若 UI 要“每格数量”，按名义/现价换算张数 |")
    lines.append("")
    lines.append("## 6. 建议资金分配（按截图合计 ≈2333 USDT）")
    lines.append("")
    for k, v in split.items():
        lines.append(f"- **{k}**：{v:.0f} USDT")
    lines.append("- 不要把返佣当成“可以提高杠杆/加仓次数”的理由。")
    lines.append("- 山寨波动远大于 BTC；同一套参数在 BTC 上安全，在 牛来 上可能直接打穿。")
    lines.append("")
    lines.append("## 7. Demo 命令与输出摘录")
    lines.append("")
    lines.append("```bash")
    lines.append("cd /workspace/gate-grid-martingale")
    lines.append("source .venv/bin/activate")
    lines.append("python optimize_niulai.py")
    lines.append("```")
    lines.append("")
    lines.append("```")
    snip = (ROOT / "opt_niulai_demo_snippet.txt").read_text(encoding="utf-8")
    lines.append(snip.rstrip())
    lines.append("```")
    lines.append("")
    lines.append("详细数值见 `opt_niulai_results.json`。")
    lines.append("")
    lines.append("## 8. 风险声明")
    lines.append("")
    lines.append("- 回测 ≠ 实盘；未计入资金费、滑点、部分成交、限价挂单失败。")
    lines.append("- 马丁在单边行情会锁死保证金；5x + 深加仓可被强平。")
    lines.append("- 本仓库仅研究工具，不含 API Key / 下单。")
    lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
