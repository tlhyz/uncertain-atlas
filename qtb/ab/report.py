"""Research report: tables, Q1–Q15, three plans. Driven only by computed rows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from .metrics import composite_score


def _md_table(rows: list[dict[str, Any]], cols: list[tuple[str, str]]) -> str:
    head = "| " + " | ".join(c[1] for c in cols) + " |"
    sep = "| " + " | ".join("---" for _ in cols) + " |"
    body = []
    for r in rows:
        cells = []
        for k, _ in cols:
            v = r.get(k, "")
            if isinstance(v, float):
                cells.append(f"{v:.4f}" if abs(v) < 1000 else f"{v:.2f}")
            elif isinstance(v, bool):
                cells.append("**YES**" if v else "no")
            else:
                cells.append(str(v))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([head, sep, *body])


def _pick(rows: list[dict[str, Any]], name: str) -> dict[str, Any] | None:
    for r in rows:
        if r.get("name") == name:
            return r
    return None


def _best(rows: list[dict[str, Any]], pred) -> dict[str, Any] | None:
    cand = [r for r in rows if pred(r)]
    if not cand:
        return None
    return max(cand, key=lambda r: r.get("score", -999))


def pair_section(bundle: dict[str, Any]) -> str:
    name = bundle["pair"]
    win = bundle.get("window") or {}
    rows = bundle.get("rows") or []
    dec = bundle.get("decision") or {}
    extra = bundle.get("extras") or {}
    lines = [
        f"## {name}",
        "",
        f"- ETF `{win.get('etf')}` vs perp `{win.get('perp')}`",
        f"- Overlap **{win.get('ab_start')} → {win.get('ab_end')}** ({win.get('bars')} bars, `{win.get('interval')}`)",
        f"- Funding source: `{win.get('funding_source')}` rows={win.get('funding_rows')}",
        f"- Decision: **{dec.get('winner', 'n/a')}**  primary={dec.get('primary')}  secondary={dec.get('secondary')}  do-not-use={dec.get('not_recommended')}",
        "",
    ]
    snap = extra.get("snapshot") or win.get("snapshot") or {}
    if snap:
        lines.append(
            f"- ETF snapshot leverage={snap.get('etf_leverage')} NAV={snap.get('etf_net_value')} "
            f"premium={snap.get('premium_discount')} (NAV history: {snap.get('nav_history')})"
        )
        lines.append("")
    drag = extra.get("path_drag") or {}
    if drag:
        lines.append(
            f"- Path-drag attribution (not a PnL debit): ETF hold {drag.get('etf_return')} vs "
            f"theo 3x und {drag.get('theo_lev_return')} → drag={drag.get('path_drag')}"
        )
        lines.append("")

    core_names = [
        "A0_cash", "A1_etf_hold", "B1_spot_hold", "B2_spot_grid",
        "A2_etf_native_atr_d0.0_reb_base", "A2_etf_native_atr_d0.0_noreb_base",
        "A2_etf_native_atr_d0.5_reb_base",
        "B_perp_1.5x_iso_P1_d0.0_reb_base", "B_perp_2.0x_iso_P1_d0.0_reb_base",
        "B_perp_2.5x_iso_P1_d0.0_reb_base", "B_perp_3.0x_iso_P1_d0.0_reb_base",
        "B_perp_3.0x_iso_P1_d0.0_noreb_base",
        "B_perp_3x_iso_P2_reb_base", "B_perp_3x_cross_P1_reb_base", "B6_hold_3x_dir",
        "A2_same_expo_base", "B_same_expo_base", "A2_same_risk_base", "B_same_risk_base",
        "A2_etf_native_atr_d0.0_reb_conservative", "B_perp_3.0x_iso_P1_d0.0_reb_conservative",
    ]
    show = []
    for n in core_names:
        r = _pick(rows, n)
        if r:
            show.append(r)
    cols = [
        ("name", "name"),
        ("lens", "lens"),
        ("final_equity", "final"),
        ("total_return", "ret"),
        ("max_dd_pct", "maxDD"),
        ("net_profit_per_1m_turnover", "pnl/1M"),
        ("capital_efficiency", "capEff"),
        ("sharpe", "sharpe"),
        ("sortino", "sortino"),
        ("calmar", "calmar"),
        ("turnover", "turnover"),
        ("net_funding", "funding"),
        ("liquidated", "LIQ"),
        ("score", "score"),
    ]
    if show:
        lines.append(_md_table(show, cols))
        lines.append("")
    of = extra.get("plateau_overfit") or {}
    if of:
        lines.append(f"- Parameter plateau: ETF `{of.get('etf')}`  PERP `{of.get('perp')}`")
        lines.append("")
    sh = bundle.get("short")
    if sh and not sh.get("skipped"):
        lines.append("### Short sleeve (3S vs perp short)")
        lines.append(
            f"- Window {sh.get('start')} → {sh.get('end')} bars={sh.get('bars')}"
        )
        e = sh.get("etf_3s") or {}
        p = sh.get("perp_short") or {}
        lines.append(
            f"- 3S final={e.get('final_equity')} DD={e.get('max_dd_pct')} | "
            f"perp short final={p.get('final_equity')} DD={p.get('max_dd_pct')} LIQ={p.get('liquidated')}"
        )
        lines.append("")
    return "\n".join(lines)


def _q_same_wallet(all_pairs: list[dict[str, Any]]) -> tuple[str, str]:
    etf_w = 0
    perp_w = 0
    details = []
    for b in all_pairs:
        rows = b.get("rows") or []
        e = _pick(rows, "A2_etf_native_atr_d0.0_reb_base")
        p = _pick(rows, "B_perp_3.0x_iso_P1_d0.0_reb_base")
        if not e or not p:
            continue
        winner = "ETF" if e["final_equity"] >= p["final_equity"] else "PERP"
        if winner == "ETF":
            etf_w += 1
        else:
            perp_w += 1
        details.append(f"{b['pair']}: ETF {e['final_equity']:.1f} vs PERP3x {p['final_equity']:.1f} → {winner}")
    champ = "ETF" if etf_w > perp_w else ("PERP" if perp_w > etf_w else "TIE")
    return champ, "; ".join(details)


def build_report(payload: dict[str, Any]) -> str:
    pairs = payload.get("pairs") or []
    pf = payload.get("portfolio") or {}
    limits = payload.get("data_limits") or {}
    lines = [
        "# Gate 3L ETF Spot Grid vs Underlying Perpetual Grid — A/B",
        "",
        "This report is computed from **real Gate public data** on overlapping timestamps only.",
        "Optimistic fills are not used in conclusions. Synthetic ETF ticks were not generated.",
        "",
        "## Data limits (do not hide)",
        "",
        f"- Gate REST candlesticks cap: **{limits.get('gate_max_bars', 10000)} bars**.",
        f"- Primary interval: `{limits.get('primary_interval', '1h')}` (covers 60–180d windows).",
        f"- Execution-sensitivity interval: `{limits.get('fine_interval', '5m')}` (last ~35d).",
        "- Historical **ticks / 1s** exist for hours, not for 3–180d. Conclusions use Base + Conservative bar fills.",
        "- Historical ETF **NAV series is not published**. Snapshot NAV/premium is recorded; path-drag uses price vs theoretical 3x underlying.",
        "- Perpetual mark/liquidation uses last-price OHLC plus contract `maintenance_rate`. Research-grade, not an exchange replica.",
        "- Gate public funding history pages back ~180 days / ~1000 prints. Earlier overlap bars have funding=0 (not a synthetic average).",
        "",
        "## Verdict by asset (no 'it depends' cop-out)",
        "",
    ]
    for b in pairs:
        dec = b.get("decision") or {}
        lines.append(
            f"- **{b['pair']}**: {dec.get('winner')} — 首选 `{dec.get('primary')}` / 次选 `{dec.get('secondary')}` / 不推荐 `{dec.get('not_recommended')}`"
        )
    lines.append("")

    # Q&A
    q1, q1d = _q_same_wallet(pairs)

    def agg(name_etf: str, name_perp: str, field: str, lower_better: bool = False) -> str:
        e_win = p_win = 0
        bits = []
        for b in pairs:
            e = _pick(b.get("rows") or [], name_etf)
            p = _pick(b.get("rows") or [], name_perp)
            if not e or not p:
                continue
            ev, pv = e.get(field), p.get(field)
            if ev is None or pv is None:
                continue
            if lower_better:
                w = "ETF" if ev <= pv else "PERP"
            else:
                w = "ETF" if ev >= pv else "PERP"
            e_win += w == "ETF"
            p_win += w == "PERP"
            bits.append(f"{b['pair']} ETF={ev} PERP={pv}")
        champ = "ETF" if e_win > p_win else ("PERP" if p_win > e_win else "TIE")
        return f"{champ} ({e_win}-{p_win}). " + "; ".join(bits)

    lines += [
        "## Answers to the required questions",
        "",
        f"**Q1 same 1000U, 3L ETF grid vs 3x perp grid — who has higher final equity?**  {q1}. {q1d}",
        "",
        "**Q2 who has lower max DD?**  "
        + agg("A2_etf_native_atr_d0.0_reb_base", "B_perp_3.0x_iso_P1_d0.0_reb_base", "max_dd_pct", True),
        "",
        "**Q3 who keeps more net profit per 1M turnover?**  "
        + agg("A2_etf_native_atr_d0.0_reb_base", "B_perp_3.0x_iso_P1_d0.0_reb_base", "net_profit_per_1m_turnover"),
        "",
    ]
    # Q4 path drag
    lines.append("**Q4 how much edge did ETF path drag eat?**")
    for b in pairs:
        d = (b.get("extras") or {}).get("path_drag") or {}
        lines.append(
            f"- {b['pair']}: ETF {d.get('etf_return')} vs theo3x {d.get('theo_lev_return')} drag={d.get('path_drag')} und={d.get('und_return')}"
        )
    lines.append("")
    lines.append("**Q5 how much edge did perp funding eat?**")
    for b in pairs:
        p = _pick(b.get("rows") or [], "B_perp_3.0x_iso_P1_d0.0_reb_base")
        if p:
            lines.append(
                f"- {b['pair']}: net_funding={p.get('net_funding')} paid={p.get('funding_paid')} recv={p.get('funding_received')} vs net_profit={p.get('net_profit')}"
            )
    lines.append("")
    liq_any = any((_pick(b.get("rows") or [], "B_perp_3.0x_iso_P1_d0.0_reb_base") or {}).get("liquidated") for b in pairs)
    lines.append(
        f"**Q6 is perp liquidation risk worth lower path drag?**  "
        f"{'NO — liquidation occurred on the 3x isolated book.' if liq_any else 'In-sample 3x isolated did not print LIQUIDATED, but MC tail and min buffer still count. See pair extras / MC.'}"
    )
    lines.append("")
    lines.append("**Q7 rebate value-add (baseline vs 0%)**")
    for b in pairs:
        rv = (b.get("extras") or {}).get("rebate_value_add") or {}
        lines.append(f"- {b['pair']}: {rv}")
    lines.append("")
    # Q8
    flip = []
    for b in pairs:
        e0 = _pick(b.get("rows") or [], "A2_etf_native_atr_d0.0_noreb_base")
        p0 = _pick(b.get("rows") or [], "B_perp_3.0x_iso_P1_d0.0_noreb_base")
        e1 = _pick(b.get("rows") or [], "A2_etf_native_atr_d0.0_reb_base")
        p1 = _pick(b.get("rows") or [], "B_perp_3.0x_iso_P1_d0.0_reb_base")
        if not all([e0, p0, e1, p1]):
            continue
        w1 = "ETF" if e1["final_equity"] >= p1["final_equity"] else "PERP"
        w0 = "ETF" if e0["final_equity"] >= p0["final_equity"] else "PERP"
        flip.append(f"{b['pair']}: with-rebate {w1} / zero-rebate {w0}")
    lines.append("**Q8 if rebate is zero, does the winner flip?**  " + "; ".join(flip))
    lines.append("")

    # regime questions from windows
    def regime_winner(pred) -> str:
        etf = perp = 0
        n = 0
        for b in pairs:
            for w in (b.get("windows") or {}).get("windows") or []:
                if not pred(w):
                    continue
                n += 1
                if w["etf"]["total_return"] >= w["perp"]["total_return"]:
                    etf += 1
                else:
                    perp += 1
        if n == 0:
            return "NO WINDOW FOUND (do not invent)"
        return f"ETF {etf} vs PERP {perp} over {n} windows → {'ETF' if etf > perp else ('PERP' if perp > etf else 'TIE')}"

    lines += [
        "**Q9 high-vol range (−5%..+5% und, high RV):**  "
        + regime_winner(lambda w: abs(w.get("und_ret") or 99) <= 0.05 and (w.get("und_rv") or 0) >= 0.008),
        "",
        "**Q10 one-way up (≥20%):**  " + regime_winner(lambda w: (w.get("und_ret") or 0) >= 0.20),
        "",
        "**Q11 crash (≤−15%):**  " + regime_winner(lambda w: (w.get("und_ret") or 0) <= -0.15),
        "",
        "**Q12 V-reversal:**  " + regime_winner(lambda w: w.get("regime") == "v_reversal"),
        "",
    ]

    # Q13 unattended
    etf_pref = sum(1 for b in pairs if (b.get("decision") or {}).get("primary") == "ETF")
    perp_pref = sum(1 for b in pairs if str((b.get("decision") or {}).get("primary", "")).startswith("PERP"))
    hyb_pref = sum(1 for b in pairs if (b.get("decision") or {}).get("primary") == "HYBRID")
    liq_pairs = []
    for b in pairs:
        p = (b.get("decision") or {}).get("perp_3x") or {}
        if p.get("liquidated"):
            liq_pairs.append(b["pair"])
    if perp_pref > etf_pref and perp_pref >= hyb_pref:
        unattended = "PERP at 1.5x–2x (do not unattended-run 3x where it liquidated)"
    elif etf_pref > perp_pref:
        unattended = "ETF"
    else:
        unattended = "HYBRID"
    lines.append(
        f"**Q13 long-run unattended:**  {unattended}. "
        f"Per-asset primaries ETF={etf_pref} PERP={perp_pref} HYBRID={hyb_pref}. "
        f"Liquidated 3x books: {liq_pairs or 'none in-sample'}."
    )
    lines.append("")

    # Q14 turnover + DD
    lines.append("**Q14 max turnover/rebate with controlled DD:**")
    for b in pairs:
        rows = b.get("rows") or []
        cands = [r for r in rows if r.get("name") in {
            "A2_etf_native_atr_d0.0_reb_base", "B_perp_1.5x_iso_P1_d0.0_reb_base",
            "B_perp_2.0x_iso_P1_d0.0_reb_base", "B_perp_3.0x_iso_P1_d0.0_reb_base",
        }]
        if not cands:
            continue
        def key(r):
            dd = max(float(r.get("max_dd_pct") or 0), 1e-6)
            to = float(r.get("turnover") or 0)
            return (to / 1e6) / dd - 5.0 * float(r.get("liquidated") or 0)
        best = max(cands, key=key)
        lines.append(f"- {b['pair']}: {best['name']} turnover={best.get('turnover')} DD={best.get('max_dd_pct')}")
    lines.append("")

    if pf and not pf.get("skipped"):
        lines.append("**Q15 portfolio risk-adjusted: Pure ETF vs Pure Perp vs Hybrid**")
        for k in ("pure_etf", "pure_perp", "hybrid_60_20_20", "hybrid_70_15_15"):
            m = pf.get(k) or {}
            lines.append(
                f"- {k}: final={m.get('final_equity')} ret={m.get('total_return')} DD={m.get('max_dd_pct')} "
                f"sharpe={m.get('sharpe')} score={m.get('score')} LIQ={m.get('liquidated')}"
            )
        scored = []
        for k in ("pure_etf", "pure_perp", "hybrid_60_20_20", "hybrid_70_15_15"):
            if pf.get(k):
                scored.append((k, pf[k].get("score") or -999))
        scored.sort(key=lambda x: -x[1])
        lines.append(f"- **Portfolio winner: {scored[0][0] if scored else 'n/a'}**")
        lines.append("")
    else:
        lines.append(f"**Q15 portfolio:** skipped ({pf.get('reason')}).")
        lines.append("")

    # Three fairness lenses
    lines.append("## Three fairness lenses (must not be collapsed)")
    lines.append("")
    for lens, e_name, p_name in (
        ("same_wallet 3x", "A2_etf_native_atr_d0.0_reb_base", "B_perp_3.0x_iso_P1_d0.0_reb_base"),
        ("same_exposure", "A2_same_expo_base", "B_same_expo_base"),
        ("same_risk", "A2_same_risk_base", "B_same_risk_base"),
    ):
        lines.append(f"### {lens}")
        e_w = p_w = 0
        for b in pairs:
            e = _pick(b.get("rows") or [], e_name)
            p = _pick(b.get("rows") or [], p_name)
            if not e or not p:
                continue
            se = composite_score(e)
            sp = composite_score(p)
            w = "ETF" if se >= sp else "PERP"
            e_w += w == "ETF"
            p_w += w == "PERP"
            lines.append(
                f"- {b['pair']}: ETF eq={e['final_equity']:.1f} score={se:.3f} | "
                f"PERP eq={p['final_equity']:.1f} score={sp:.3f} LIQ={p.get('liquidated')} → **{w}**"
            )
        lines.append(f"- Lens tally: ETF {e_w} / PERP {p_w} → **{'ETF' if e_w > p_w else ('PERP' if p_w > e_w else 'TIE')}**")
        lines.append("")

    # Plans
    lines += _plans(pairs, pf)
    lines.append("## Per-asset detail")
    lines.append("")
    for b in pairs:
        lines.append(pair_section(b))
    if pf and not pf.get("skipped"):
        lines.append("## Portfolio (10_000 USDT, overlapping history only)")
        lines.append("")
        lines.append(f"- Overlap {pf.get('ab_start')} → {pf.get('ab_end')} bars={pf.get('bars')}")
        lines.append(f"- Weights {pf.get('weights')} cash={pf.get('cash_frac')}")
        lines.append("")
    return "\n".join(lines) + "\n"


def _plans(pairs: list[dict[str, Any]], pf: dict[str, Any]) -> list[str]:
    # Derive spacing from plateau medians when present
    etf_assets = []
    perp_assets = []
    for b in pairs:
        dec = b.get("decision") or {}
        prim = dec.get("primary")
        if prim == "ETF":
            etf_assets.append(b["pair"])
        elif str(prim).startswith("PERP"):
            perp_assets.append(b["pair"])
    lines = [
        "## PLAN A — ETF dominant",
        "",
        f"- Assets (primaries): {etf_assets or 'none — do not force ETF if it lost'}",
        "- Allocation (if A is chosen): majors 28/28, SOXL ≤24%, meme ≤8% each, rest cash.",
        "- Grid: geometric native 0.40 ATR (use 0.30–0.50 plateau only if not flagged OVERFIT), range ±5 ATR, reanchor on range exit.",
        "- Expected turnover / DD: see per-asset A2 native ATR base rows — do not invent a constant.",
        "",
        "## PLAN B — PERP dominant",
        "",
        f"- Assets (primaries): {perp_assets or 'none — do not force perp if it lost'}",
        "- Leverage: start 1.5–2.0x wallet notional; 3x only if that pair's 3x score beat 1.5x and no liquidation.",
        "- Margin: isolated P2 (70/30) unless P1 clearly won without approaching liq.",
        "- Liquidation buffer trigger 15% (test 10/20 shown in rows). Funding: halt if rolling 7d net funding < −1.5% of equity.",
        "",
        "## PLAN C — HYBRID",
        "",
        "- Default book: ETF grid 60% / perp grid 20% / cash 20% (alt 70/15/15).",
        "- ETF sleeve: SOL3L + ETH3L core; SOXL3L only inside its real overlap; meme ≤8%.",
        "- Perp sleeve: same underlyings, **2x** wallet cap, isolated, 30% reserve.",
        "- Use hybrid when single-mechanism scores split across regimes (see Q9–Q12).",
        "",
    ]
    if pf and not pf.get("skipped"):
        scored = []
        for k in ("pure_etf", "pure_perp", "hybrid_60_20_20", "hybrid_70_15_15"):
            if pf.get(k):
                scored.append((k, pf[k].get("score") or -999, pf[k].get("final_equity")))
        scored.sort(key=lambda x: -x[1])
        if scored:
            lines.append(f"Portfolio scores rank: {scored}")
            lines.append("")
    return lines


def write_outputs(out_dir: Path, payload: dict[str, Any]) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    js = out_dir / "ab_results.json"
    md = out_dir / "AB_REPORT.md"
    js.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    md.write_text(build_report(payload), encoding="utf-8")
    # flat CSV-ish table
    flat = []
    for b in payload.get("pairs") or []:
        for r in b.get("rows") or []:
            flat.append({"pair": b["pair"], **{k: v for k, v in r.items() if not isinstance(v, (list, dict))}})
    if flat:
        import pandas as pd

        pd.DataFrame(flat).to_csv(out_dir / "ab_rows.csv", index=False)
    return {"json": str(js), "report": str(md), "csv": str(out_dir / "ab_rows.csv")}
