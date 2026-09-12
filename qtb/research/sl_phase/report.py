"""Adversarial Chinese report. UNDERLYING_ONLY_CANDIDATE never enters strategy totals."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _pct(x: Any) -> str:
    if x is None:
        return "n/a"
    try:
        return f"{float(x):.2%}"
    except (TypeError, ValueError):
        return str(x)


def _f(x: Any, nd: int = 2) -> str:
    if x is None:
        return "n/a"
    try:
        return f"{float(x):.{nd}f}"
    except (TypeError, ValueError):
        return str(x)


def write_report(payload: dict[str, Any], path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    a = payload.get("audit") or {}
    synth = payload.get("synth") or {}
    wins = payload.get("etf_windows") or {}
    remap = payload.get("candidate_remap") or []
    grids = payload.get("grid_results") or []
    allowed = [g for g in grids if g.get("confidence") in {"REAL_GATE_ETF_WINDOW", "SYNTHETIC_GATE_ETF_WINDOW"}]
    forbidden = [g for g in grids if g.get("confidence") == "UNDERLYING_ONLY_CANDIDATE"]
    sl = payload.get("sl_directional") or []
    wf = payload.get("walk_forward") or {}
    plat = payload.get("plateau") or {}
    rob = payload.get("robustness") or {}
    mc = payload.get("monte_carlo") or {}
    edge = payload.get("net_edge") or {}
    fee = payload.get("fee") or {}
    verdict = payload.get("verdict") or "FAIL"

    lines: list[str] = []
    w = lines.append
    w("# Gate 3L/3S 现货网格 + S→L 对抗回测报告")
    w("")
    w("判定标准：NET ETF GRID EDGE 必须在 Base/Conservative、0% 返佣、失败窗口、Walk-forward、Monte Carlo 下仍稳健。否则判失败。")
    w("")
    w(f"**总判定：{verdict}**")
    w("")
    w("## 1. ETF 真实数据完整性")
    w("")
    w("主数据：`download.gatedata.org/spot/deals` 官方逐笔。禁止 Yahoo/Stooq 日线做网格或策略 PnL。")
    w("")
    w(f"- maker={fee.get('maker')} taker={fee.get('taker')} 来源：{fee.get('source')}")
    w("- 返佣情景：0% / 50% / 70% 分开记账，不并进隐藏费率。")
    w("")
    pump = (a.get("pump_contamination") or {})
    w("### PUMP 污染")
    w("")
    w(f"- 规则：{pump.get('rule')}")
    w(f"- 旧带月份：{pump.get('legacy_PUMP3L_months')}")
    w(f"- 现行月份：{pump.get('live_PUMP3L_months')}")
    w(f"- 是否合并：{pump.get('merged')}")
    w("")
    w("### 各产品")
    w("")
    for p in a.get("products") or []:
        tap = p.get("tape") or {}
        w(
            f"- `{p.get('market')}` listed={p.get('listed')} months={p.get('cached_months')} "
            f"strategy_prints={p.get('strategy_prints', tap.get('n_prints'))} status={p.get('data_status')}"
        )
    w("")
    w("## 2. 哪些区间是真实 Gate ETF")
    w("")
    real_w = [x for x in (wins.get("scanned") or []) if x.get("confidence") == "REAL_GATE_ETF_WINDOW"]
    w(f"自动扫描得到 REAL 窗口 {len(real_w)} 个（按 ETF 自身小时序列，不用底层日期）。")
    w("")
    w("## 3. 哪些区间是 Synthetic")
    w("")
    syn_w = [x for x in (wins.get("scanned") or []) if x.get("confidence") == "SYNTHETIC_GATE_ETF_WINDOW"]
    w(f"SYNTHETIC 窗口 {len(syn_w)} 个。上市前无 Gate 3L 逐笔且无合格高频底层时，**不会**伪造窗口。")
    w("")
    w("AAOI3L：官方 deals 不存在（上市 2026-09-09，9 月文件未发布）。不得用 AAOI 日线代替 AAOI3L 进统计。")
    w("")
    w("SOXL3L/3S 上市前：无 Gate 逐笔，无 SOXLG。S1/S2 保持 UNDERLYING_ONLY_CANDIDATE，**不进最终统计**。")
    w("")
    w("## 4. Synthetic vs Real 校准")
    w("")
    if not synth:
        w("无重叠校准（缺底层逐笔或真实 ETF）。")
    for k, rec in synth.items():
        w(
            f"- {k}: status={rec.get('status')} n_days={rec.get('n_days')} "
            f"C={_pct(rec.get('C_total_return'))} A={_pct(rec.get('A_total_return'))} "
            f"B={_pct(rec.get('B_total_return'))} A-C={_pct(rec.get('A_minus_C'))} "
            f"B-C={_pct(rec.get('B_minus_C'))} A_MAE={_f(rec.get('A_vs_C_mae'), 4)} "
            f"B_MAE={_f(rec.get('B_vs_C_mae'), 4)}"
        )
        if rec.get("status") == "ok":
            mae = rec.get("A_vs_C_mae")
            if mae is not None and float(mae) > 0.15:
                w("  - **LOW CONFIDENCE**：A vs C MAE > 15% 归一化路径。更早 synthetic 不得当高置信。")
    w("")
    w("## 5. 每只 ETF 最相似 / 自动窗口（ETF 自身）")
    w("")
    by_m: dict[str, list] = {}
    for x in real_w + syn_w:
        by_m.setdefault(x.get("market", "?"), []).append(x)
    for m, rows in by_m.items():
        w(f"### {m}")
        for r in rows[:12]:
            w(
                f"- {r.get('regime')} {r.get('start')} → {r.get('end')} "
                f"ret={_pct(r.get('etf_ret'))} dd={_pct(r.get('max_dd'))} "
                f"rebound={_pct(r.get('max_rebound'))} x1%={ (r.get('grid_cross') or {}).get('1.0%') } "
                f"`{r.get('confidence')}`"
            )
        w("")
    w("## 6–9. 先跌后涨 / 先涨后跌 / 横盘 / 单边（ETF 自身）")
    w("")
    for lab, title in (
        ("drop_then_rise", "先跌后涨"),
        ("v_reversal", "V 反"),
        ("rise_then_fall", "先涨后跌"),
        ("high_vol_chop", "高波动横盘"),
        ("trend_down", "单边下跌"),
        ("trend_up", "单边上涨"),
        ("double_bottom", "二次探底"),
    ):
        sub = [x for x in real_w + syn_w if x.get("regime") == lab]
        w(f"### {title} ({len(sub)})")
        for r in sub[:8]:
            w(f"- {r.get('market')} {r.get('start')} → {r.get('end')} ret={_pct(r.get('etf_ret'))} dd={_pct(r.get('max_dd'))}")
        w("")
    w("## Candidate remap（底层日期 ±15/30 天，禁止沿用 underlying_bottom）")
    w("")
    for r in remap:
        w(
            f"- candidate `{r.get('source_candidate')}` → {r.get('market')} "
            f"{r.get('confidence')} regime={r.get('regime')} "
            f"start={r.get('start')} bottom={r.get('bottom')} reversal={r.get('reversal')} end={r.get('end')} "
            f"allowed={r.get('allowed_in_stats')}"
        )
    w("")
    w("## 10. 各策略收益（仅 REAL + SYNTHETIC）")
    w("")
    w(f"网格结果条数：全部 {len(grids)}，进统计 {len(allowed)}，剔除 UNDERLYING_ONLY {len(forbidden)}。")
    w("")
    w("| window | symbol | fill | rebate | init | final | ret | MDD | grid_pnl | inv_pnl | gross_fee | rebate | mgmt | n_prints | conf |")
    w("|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    for g in allowed:
        w(
            f"| {g.get('window_id','')} | {g.get('symbol')} | {g.get('fill_model')} | {_pct(g.get('rebate_rate'))} "
            f"| {_f(g.get('initial_equity'))} | {_f(g.get('final_equity'))} | {_pct(g.get('total_return'))} "
            f"| {_pct(g.get('max_drawdown'))} | {_f(g.get('realized_grid_profit'))} | {_f(g.get('inventory_unrealized_pnl'))} "
            f"| {_f(g.get('gross_fee'))} | {_f(g.get('rebate_income'))} | {_f(g.get('ETF_management_fee'))} "
            f"| {g.get('n_prints')} | {g.get('confidence')} |"
        )
    w("")
    w("S→L 方向仓（S3 / REAL SOXLG+3L/3S，无网格）：")
    w("")
    for r in sl:
        if r.get("status") == "DATA_MISSING":
            w(f"- {r.get('combo')}: DATA_MISSING {r.get('reason','')}")
            continue
        w(
            f"- {r.get('combo')}: equity={_f(r.get('final_equity'))} ret={_pct(r.get('total_return'))} "
            f"S={_f(r.get('S_profit'))} L={_f(r.get('L_profit'))} stage={r.get('stage')} rev={r.get('reversed')}"
        )
    w("")
    w("## 11–12. ETF 网格 vs 底层现货网格 vs 3 倍合约网格")
    w("")
    w("底层现货网格只在 SOXLG/SNXXG 有逐笔时作为 **Benchmark**，不替代 3L PnL。")
    w("3 倍永续网格需要 funding / 强平 / 保证金；本次未下载合约资金费 tape，**Benchmark 5 标 INCOMPLETE**，不编造优势。")
    w("")
    w("## 13. ETF 路径损耗")
    w("")
    w("SOXL3L 是 3×SOXL，不是 9×SOX。SNXX3L 是 3×SNXX，不是 6×SNDK。")
    w("校准见 §4。Crypto 3L 未下载 BTC/ETH/SOL 现货逐笔（单月 40–150MB），衰减只在有 SOXLG/SNXXG 重叠处量化。")
    w("")
    w("## 14. 返佣贡献")
    w("")
    for k, rec in rob.items():
        w(
            f"- {k}: eq0={_f(rec.get('eq_0'))} eq50={_f(rec.get('eq_50'))} eq70={_f(rec.get('eq_70'))} "
            f"70-0={_f(rec.get('rebate_70_minus_0'))} alive0={rec.get('alive_0pct_rebate')} "
            f"mgmt×2={rec.get('alive_mgmt_x2')} slip×2={rec.get('alive_slip_x2')} miss20={rec.get('alive_miss_20pct_fills')}"
        )
    w("")
    w("## 15. 最大回撤")
    w("")
    if allowed:
        worst = min(allowed, key=lambda g: g.get("max_drawdown") if g.get("max_drawdown") is not None else 0)
        w(f"统计样本最差 MDD：{worst.get('symbol')} {worst.get('window_id')} {_pct(worst.get('max_drawdown'))} equity={_f(worst.get('final_equity'))}")
    w("")
    w("## 16. 失败案例")
    w("")
    fails = [g for g in allowed if (g.get("final_equity") or 0) < (g.get("initial_equity") or 0)]
    w(f"进统计样本中亏损 {len(fails)} / {len(allowed)}。")
    for g in sorted(fails, key=lambda x: (x.get("final_equity") or 0) - (x.get("initial_equity") or 1))[:12]:
        w(
            f"- {g.get('symbol')} {g.get('window_id')} fill={g.get('fill_model')} "
            f"eq {_f(g.get('initial_equity'))}→{_f(g.get('final_equity'))} "
            f"grid={_f(g.get('realized_grid_profit'))} inv={_f(g.get('inventory_unrealized_pnl'))}"
        )
    w("")
    w("## 17. 参数平台")
    w("")
    w(json.dumps(plat, ensure_ascii=False, indent=2, default=str)[:4000])
    w("")
    w("## 18. Walk-forward")
    w("")
    w("Train = 2024 REAL crypto ETF 窗口；Test = 2025 REAL；2026 **不参与选参**。")
    w("")
    w(f"```\n{json.dumps(wf, ensure_ascii=False, indent=2, default=str)}\n```")
    w("")
    w("## 19. Monte Carlo")
    w("")
    w(f"```\n{json.dumps(mc, ensure_ascii=False, indent=2, default=str)[:6000]}\n```")
    w("")
    w("## 20. 最终建议 / 三套方案 / Q1–Q13")
    w("")
    w(f"### NET ETF GRID EDGE")
    w("")
    w(json.dumps(edge, ensure_ascii=False, indent=2, default=str)[:5000])
    w("")
    plans = payload.get("plans") or {}
    w("### Plan A / B / C")
    w("")
    w(json.dumps(plans, ensure_ascii=False, indent=2, default=str)[:5000])
    w("")
    qa = payload.get("answers") or {}
    for i in range(1, 14):
        w(f"### Q{i}")
        w(qa.get(f"Q{i}", "未计算"))
        w("")
    path.write_text("\n".join(lines), encoding="utf-8")
