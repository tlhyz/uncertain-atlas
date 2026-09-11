"""Write backtest / optimize artifacts under outputs/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from qtb.engine.backtest import BacktestResult


def _maybe_mpl():
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        return plt
    except Exception:
        return None


def trades_frame(result: BacktestResult) -> pd.DataFrame:
    rows = []
    for t in result.trades:
        rows.append(
            {
                "trade_id": t.trade_id,
                "timestamp": t.timestamp,
                "symbol": t.symbol,
                "book": t.book,
                "direction": t.direction,
                "side": t.side,
                "price": t.price,
                "qty": t.qty,
                "notional": t.notional,
                "fee": t.fee,
                "slippage": t.slippage,
                "reason": t.reason,
                "realized_pnl": t.realized_pnl,
                "equity_after": t.equity_after,
                "cycle_id": t.cycle_id,
            }
        )
    return pd.DataFrame(rows)


def _plot_curves(result: BacktestResult, out_dir: Path) -> dict[str, str]:
    plt = _maybe_mpl()
    paths: dict[str, str] = {}
    ts = result.timestamps
    if plt is None:
        # CSV fallbacks so reports are still real
        pd.DataFrame(
            {
                "timestamp": ts,
                "equity": result.equity_curve,
                "drawdown": result.drawdown_curve,
                "position": result.position_curve,
            }
        ).to_csv(out_dir / "curves.csv", index=False)
        paths["curves_csv"] = str(out_dir / "curves.csv")
        return paths

    def _x(values):
        try:
            return pd.to_datetime(values)
        except Exception:
            return range(len(values))

    x = _x(ts)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, result.equity_curve, color="#1f77b4", lw=1.2)
    ax.set_title(f"Equity — {result.symbol} {result.strategy}")
    ax.set_ylabel("USDT")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    p = out_dir / "equity_curve.png"
    fig.savefig(p, dpi=120)
    plt.close(fig)
    paths["equity_curve"] = str(p)

    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.fill_between(x, result.drawdown_curve, color="#d62728", alpha=0.55)
    ax.set_title("Drawdown")
    ax.set_ylabel("USDT")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    p = out_dir / "drawdown_curve.png"
    fig.savefig(p, dpi=120)
    plt.close(fig)
    paths["drawdown_curve"] = str(p)

    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.plot(x, result.position_curve, color="#2ca02c", lw=1.0)
    ax.axhline(0.0, color="black", lw=0.6)
    ax.set_title("Net position (base qty, long+, short-)")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    p = out_dir / "position_chart.png"
    fig.savefig(p, dpi=120)
    plt.close(fig)
    paths["position_chart"] = str(p)
    return paths


def _plot_heatmap(heatmap: dict[str, Any], out_dir: Path) -> str | None:
    cells = heatmap.get("cells") or []
    if not cells:
        return None
    df = pd.DataFrame(cells)
    pivot = df.pivot_table(index="y", columns="x", values="score", aggfunc="mean")
    csv_path = out_dir / "parameter_heatmap.csv"
    pivot.to_csv(csv_path)
    plt = _maybe_mpl()
    if plt is None:
        return str(csv_path)
    fig, ax = plt.subplots(figsize=(7, 5))
    im = ax.imshow(pivot.to_numpy(), aspect="auto", origin="lower", cmap="RdYlGn")
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels([str(c) for c in pivot.columns], rotation=45, ha="right")
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels([str(i) for i in pivot.index])
    ax.set_xlabel(str(heatmap.get("x")))
    ax.set_ylabel(str(heatmap.get("y")))
    ax.set_title("Parameter heatmap (composite score)")
    fig.colorbar(im, ax=ax, fraction=0.046)
    fig.tight_layout()
    png = out_dir / "parameter_heatmap.png"
    fig.savefig(png, dpi=120)
    plt.close(fig)
    return str(png)


def chinese_summary(result: BacktestResult, extra: dict[str, Any] | None = None) -> str:
    m = result.metrics
    liq = "是（参数应丢弃）" if m.get("liquidated") else "否"
    sl = (result.params.get("risk") or {}).get("investment_sl_pct")
    sl_txt = f"{float(sl):.0%}" if sl else "关闭"
    lines = [
        f"# 回测摘要 — {result.symbol} / {result.interval} / {result.strategy}",
        "",
        "## 结论（研究用，非实盘）",
        f"- 净收益：{m.get('net_pnl')} USDT（收益率 {float(m.get('return_pct') or 0)*100:.2f}%）",
        f"- 最大回撤：{m.get('max_dd')} USDT（{float(m.get('max_dd_pct') or 0)*100:.2f}%）",
        f"- Sharpe：{m.get('sharpe')}  | Calmar：{m.get('calmar')}",
        f"- 胜率：{float(m.get('win_rate') or 0)*100:.1f}%  | 盈亏比(PF)：{m.get('profit_factor')}",
        f"- 周期数：{m.get('cycles')}  | 止损次数：{m.get('stop_outs')}  | 成交：{m.get('num_trades')}",
        f"- 最大浮亏：{m.get('max_float_loss')}  | 强平风险分：{m.get('liq_risk')}  | 是否强平：{liq}",
        f"- 费用占比：{m.get('fee_ratio')}  | 总手续费：{m.get('total_fees')}  | 资金费：{m.get('funding_pnl')}",
        f"- 投资额止损：{sl_txt}（按 wallet/投资额回撤，不是价格%）",
    ]
    if m.get("feed") == "deals" or m.get("grid_shifts") is not None:
        lines.append(
            f"- 行情源：逐笔 deals（{m.get('n_prints', '?')} 笔打印）  | 移格：{m.get('grid_shifts')}  | "
            f"剩余底仓：{m.get('leftover_base')}"
        )
        if m.get("grid_harvest") is not None:
            lines.append(
                f"- 网格已实现差价：{m.get('grid_income', m.get('grid_harvest'))} USDT"
                f"（窗内 {m.get('grid_harvest')} + 移格后仍按原+1格卖出 {m.get('leftover_harvest')}）"
            )
            lines.append(
                f"- 移格遗留卖出：{m.get('leftover_harvest')}  | 期末底仓浮盈亏：{m.get('inventory_mtm')}  | "
                f"停机：{'是' if m.get('halted') else '否'}"
            )
    lines.extend(
        [
        "",
        "## 稳健性提示",
        "- 网格/马丁在单边行情会深套或反复止损；回测盈利 ≠ 未来盈利。",
        "- 复合分同时惩罚回撤、浮亏、强平风险和费用，不要只看收益率。",
        "- 若 train/test 分数缺口大，或高波动区间翻脸，视为过拟合。",
        "",
        "## 费用模型",
        f"- {((result.params.get('costs') or {}).get('label'))}",
        f"- 有效 maker/taker：{(result.params.get('costs') or {}).get('eff_maker')} / {(result.params.get('costs') or {}).get('eff_taker')}",
        f"- 滑点：{(result.params.get('costs') or {}).get('slippage_bps')} bps",
        "",
        "## 风险声明",
        "本框架默认只做回测。实盘模块强制 DRY_RUN，没有真实下单通道。",
        "作者不对任何资金损失负责；只用闲置资金做研究。",
        ]
    )
    if extra:
        ao = extra.get("anti_overfit") or extra
        tt = (ao.get("train_test") if isinstance(ao, dict) else None) or {}
        if tt:
            lines.extend(
                [
                    "",
                    "## 防过拟合",
                    f"- 训练分：{tt.get('train_score')}  测试分：{tt.get('test_score')}  缺口：{tt.get('score_gap')}",
                    f"- 过拟合标记：{tt.get('overfit_flag')}",
                ]
            )
        mc = ao.get("monte_carlo") if isinstance(ao, dict) else None
        if mc:
            lines.append(
                f"- Monte Carlo 终值 P05/P50/P95：{mc.get('p05_equity')} / {mc.get('p50_equity')} / {mc.get('p95_equity')}；ruin={mc.get('ruin_rate')}"
            )
    return "\n".join(lines) + "\n"


def write_report(
    result: BacktestResult,
    out_dir: str | Path,
    optimize: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
) -> dict[str, str]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    written: dict[str, str] = {}

    tf = trades_frame(result)
    trades_path = out / "trades.csv"
    tf.to_csv(trades_path, index=False)
    written["trades"] = str(trades_path)

    curves = _plot_curves(result, out)
    written.update(curves)

    metrics_path = out / "metrics.json"
    metrics_path.write_text(json.dumps(result.metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    written["metrics"] = str(metrics_path)

    if config is not None:
        try:
            from qtb.config import dump_yaml

            dump_yaml(config, out / "config.used.yaml")
            written["config"] = str(out / "config.used.yaml")
        except Exception:
            (out / "config.used.json").write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")

    extra = optimize or {}
    if optimize and optimize.get("heatmap"):
        hp = _plot_heatmap(optimize["heatmap"], out)
        if hp:
            written["heatmap"] = hp
        (out / "optimize.json").write_text(
            json.dumps(
                {
                    "n_combos": optimize.get("n_combos"),
                    "best": optimize.get("best"),
                    "top": optimize.get("top"),
                    "anti_overfit": optimize.get("anti_overfit"),
                },
                indent=2,
                ensure_ascii=False,
                default=str,
            ),
            encoding="utf-8",
        )
        written["optimize"] = str(out / "optimize.json")

    summary = chinese_summary(result, extra)
    (out / "summary.md").write_text(summary, encoding="utf-8")
    written["summary"] = str(out / "summary.md")
    return written
