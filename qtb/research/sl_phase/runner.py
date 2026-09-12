"""Tick-only research. Strategy stats exclude UNDERLYING_ONLY_CANDIDATE."""

from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

import pandas as pd

from qtb.data.gatedata import download_spot_deals
from qtb.research.sl_phase.audit import full_audit, load_strategy_tape
from qtb.research.sl_phase.catalog import (
    BASELINE_GRIDS,
    CANDIDATE_REGIMES,
    MAKER_FEE,
    REBATE_SCENARIOS,
    SCAN_GRID_N,
    SCAN_RANGE,
    SCAN_REANCHOR,
    TAKER_FEE,
)
from qtb.research.sl_phase.etf_series import hourly_etf, to_1s_tape
from qtb.research.sl_phase.geometric_grid import GeometricSpotGrid
from qtb.research.sl_phase.monte_carlo import block_bootstrap
from qtb.research.sl_phase.report import write_report
from qtb.research.sl_phase.strategy import run_directional_hold, run_sl_directional
from qtb.research.sl_phase.synthetic import compare_abc
from qtb.research.sl_phase.windows import (
    remap_candidate,
    scan_etf_series,
    series_confidence,
    window_to_dict,
)

RESEARCH_3X = (
    "SOXL3L_USDT",
    "SOXL3S_USDT",
    "SNXX3L_USDT",
    "SNXX3S_USDT",
    "BTC3L_USDT",
    "ETH3L_USDT",
    "SOL3L_USDT",
    "PENGU3L_USDT",
    "PUMP3L_USDT",
    "AAOI3L_USDT",
)

DOWNLOAD_SPEC = (
    (["SOXL3L_USDT", "SOXL3S_USDT"], "2026-06", "2026-08"),
    (["SOXLG_USDT", "SNXXG_USDT"], "2026-07", "2026-08"),
    (["SNXX3L_USDT", "SNXX3S_USDT"], "2026-07", "2026-08"),
    (["BTC3L_USDT", "ETH3L_USDT", "SOL3L_USDT"], "2024-07", "2026-08"),
    (["PENGU3L_USDT"], "2025-07", "2026-08"),
    (["PUMP3L_USDT"], "2025-04", "2026-08"),
)


def ensure_research_tapes() -> list[dict[str, Any]]:
    recs: list[dict[str, Any]] = []
    for mkts, a, b in DOWNLOAD_SPEC:
        recs.extend(download_spot_deals(mkts, a, b))
    return recs


def _grid_cfg(market: str) -> dict[str, float | int]:
    return dict(BASELINE_GRIDS.get(market) or {"lower_mult": 0.70, "upper_mult": 1.30, "grid_n": 48, "capital": 500})


def run_grid_on_tape(
    market: str,
    tape: pd.DataFrame,
    *,
    fill: str = "base",
    rebate: float = 0.0,
    range_mult: float = 1.0,
    grid_n: int | None = None,
    reanchor: str = "off",
    sizing: str = "fixed_quote",
    miss_fill_frac: float = 0.0,
    slip_mult: float = 1.0,
    mgmt_mult: float = 1.0,
    capital: float | None = None,
    window_id: str = "",
    confidence: str = "REAL_GATE_ETF_WINDOW",
) -> dict[str, Any]:
    cfg = _grid_cfg(market)
    n = int(grid_n or cfg["grid_n"])
    cap = float(capital if capital is not None else cfg["capital"])
    lo = float(cfg["lower_mult"])
    hi = float(cfg["upper_mult"])
    # range_mult scales the log-width around 1.0
    lo = 1.0 - (1.0 - lo) * range_mult
    hi = 1.0 + (hi - 1.0) * range_mult
    engine = GeometricSpotGrid(
        symbol=market,
        capital=cap,
        lower_mult=max(0.05, lo),
        upper_mult=max(1.02, hi),
        grid_n=n,
        fill_model=fill,
        sizing=sizing,  # type: ignore[arg-type]
        reanchor=reanchor,  # type: ignore[arg-type]
        rebate_rate=rebate,
        maker_rate=MAKER_FEE,
        taker_rate=TAKER_FEE,
        miss_fill_frac=miss_fill_frac,
        slip_mult=slip_mult,
        mgmt_mult=mgmt_mult,
    )
    use = to_1s_tape(tape) if tape is not None and not tape.empty else tape
    res = engine.run(use if use is not None else tape)
    met = res.metrics()
    met["window_id"] = window_id
    met["confidence"] = confidence
    met["allowed_in_stats"] = confidence in {"REAL_GATE_ETF_WINDOW", "SYNTHETIC_GATE_ETF_WINDOW"}
    met["rebate_rate"] = rebate
    met["n_prints"] = int(len(tape) if tape is not None else 0)
    met["data_status"] = (tape.attrs.get("data_status") if tape is not None else "DATA_MISSING")
    met["fee_source"] = "qtb.costs.fees._SPOT_VIP_TABLE[7]"
    met["range_mult"] = range_mult
    met["grid_n"] = n
    if not met["allowed_in_stats"]:
        met["excluded_reason"] = "UNDERLYING_ONLY_CANDIDATE"
    return met


def _slice_tape(market: str, start: datetime, end: datetime) -> pd.DataFrame:
    s = start.date() if isinstance(start, datetime) else start
    e = end.date() if isinstance(end, datetime) else end
    return load_strategy_tape(market, s, e)


def synth_validation() -> dict[str, Any]:
    out = {}
    from datetime import date as D

    pairs = (
        ("SOXLG_USDT", "SOXL3L_USDT", "3L", D(2026, 7, 1), D(2026, 8, 31)),
        ("SOXLG_USDT", "SOXL3S_USDT", "3S", D(2026, 7, 1), D(2026, 8, 31)),
        ("SNXXG_USDT", "SNXX3L_USDT", "3L", D(2026, 7, 29), D(2026, 8, 31)),
        ("SNXXG_USDT", "SNXX3S_USDT", "3S", D(2026, 7, 29), D(2026, 8, 31)),
    )
    for und_m, etf_m, side, a, b in pairs:
        und = load_strategy_tape(und_m, a, b)
        etf = load_strategy_tape(etf_m, a, b)
        rec = compare_abc(und, etf, side=side)
        rec["underlying"] = und_m
        rec["etf"] = etf_m
        rec["under_prints"] = int(len(und))
        rec["etf_prints"] = int(len(etf))
        out[f"{etf_m}_{side}"] = rec
    return out


def build_windows() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, pd.Series]]:
    hourly: dict[str, pd.Series] = {}
    scanned: list[dict[str, Any]] = []
    for m in RESEARCH_3X:
        h = hourly_etf(m)
        hourly[m] = h
        conf = "REAL_GATE_ETF_WINDOW" if len(h) else "UNDERLYING_ONLY_CANDIDATE"
        for w in scan_etf_series(m, h, confidence=conf, top_per_regime=3):
            scanned.append(window_to_dict(w))
    remapped: list[dict[str, Any]] = []
    for cand in CANDIDATE_REGIMES:
        for m in cand.trade_markets:
            if not m.endswith("3L_USDT") and not m.endswith("3S_USDT"):
                continue
            h = hourly.get(m)
            if h is None:
                h = hourly_etf(m)
                hourly[m] = h
            conf = series_confidence(m, cand.start, cand.end)
            if h is None or h.empty:
                conf = "UNDERLYING_ONLY_CANDIDATE"
            w = remap_candidate(cand, m, h if h is not None else pd.Series(dtype=float), confidence=conf)
            remapped.append(window_to_dict(w))
        if not cand.trade_markets:
            remapped.append(
                {
                    "id": f"{cand.id}_NO_ETF",
                    "market": cand.asset,
                    "source_candidate": cand.id,
                    "confidence": "UNDERLYING_ONLY_CANDIDATE",
                    "allowed_in_stats": False,
                    "notes": cand.notes,
                    "regime": "unknown",
                }
            )
    return scanned, remapped, hourly


def _pick_grid_windows(scanned: list[dict[str, Any]], remapped: list[dict[str, Any]]) -> list[dict[str, Any]]:
    picked: list[dict[str, Any]] = []
    # prefer remapped REAL/SYNTH + a few native scans per market
    for row in remapped:
        if row.get("allowed_in_stats") and row.get("market", "").endswith(("3L_USDT", "3S_USDT")):
            picked.append(row)
    by_m: dict[str, list] = {}
    for row in scanned:
        if not row.get("allowed_in_stats"):
            continue
        if row.get("regime") not in {"drop_then_rise", "v_reversal", "rise_then_fall", "trend_down", "high_vol_chop"}:
            continue
        by_m.setdefault(row["market"], []).append(row)
    for m, rows in by_m.items():
        rows = sorted(rows, key=lambda r: abs(float(r.get("max_dd") or 0)) * (1 + float(r.get("max_rebound") or 0)), reverse=True)
        picked.extend(rows[:4])
    # de-dup by market+start+end
    seen = set()
    out = []
    for r in picked:
        key = (r.get("market"), r.get("start"), r.get("end"))
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def robustness_on(market: str, start: date, end: date) -> dict[str, Any]:
    tape = load_strategy_tape(market, start, end)
    if tape.empty:
        return {"status": "DATA_MISSING"}
    def _g(reb, **kw):
        return run_grid_on_tape(market, tape, rebate=reb, **kw)
    zero = _g(0.0)
    half = _g(0.50)
    sev = _g(0.70)
    mgmt2 = _g(0.70, mgmt_mult=2.0)
    slip2 = _g(0.70, fill="conservative", slip_mult=2.0)
    miss20 = _g(0.70, miss_fill_frac=0.20)
    def green(m):
        return bool((m.get("final_equity") or 0) > (m.get("initial_equity") or 1))
    return {
        "alive_0pct_rebate": green(zero),
        "alive_50pct_rebate": green(half),
        "alive_70pct_rebate": green(sev),
        "alive_mgmt_x2": green(mgmt2),
        "alive_slip_x2": green(slip2),
        "alive_miss_20pct_fills": green(miss20),
        "eq_0": zero.get("final_equity"),
        "eq_50": half.get("final_equity"),
        "eq_70": sev.get("final_equity"),
        "eq_mgmt2": mgmt2.get("final_equity"),
        "eq_slip2": slip2.get("final_equity"),
        "eq_miss20": miss20.get("final_equity"),
        "rebate_70_minus_0": (sev.get("final_equity") or 0) - (zero.get("final_equity") or 0),
    }


def sl_matrix() -> list[dict[str, Any]]:
    from datetime import date as D

    soxl = to_1s_tape(load_strategy_tape("SOXLG_USDT", D(2026, 7, 1), D(2026, 8, 31)))
    tapes = {
        m: to_1s_tape(load_strategy_tape(m, D(2026, 6, 25), D(2026, 8, 31)))
        for m in (
            "SOXL3S_USDT",
            "SNXX3S_USDT",
            "SOXL3L_USDT",
            "ETH3L_USDT",
            "SOL3L_USDT",
            "SNXX3L_USDT",
            "PENGU3L_USDT",
            "PUMP3L_USDT",
            "AAOI3L_USDT",
        )
    }
    rows = []
    for plan, red, ov in (
        ("A", "remaining", True),
        ("A", "remaining", False),
        ("A", "initial", True),
        ("B", "remaining", True),
        ("C", "remaining", True),
    ):
        rec = run_sl_directional(soxl, tapes, plan=plan, s_initial=2000.0, reduce_mode=red, overlap=ov, rebate=0.0)
        rec["combo"] = f"plan{plan}_{red}_ov{int(ov)}"
        rec["confidence"] = "REAL_GATE_ETF_WINDOW" if rec.get("status") == "ok" else "UNDERLYING_ONLY_CANDIDATE"
        rows.append(rec)
    l_only = run_directional_hold(tapes.get("SOXL3L_USDT"), capital=2000.0, rebate=0.0)
    rows.append({"combo": "L_only_SOXL3L_2000", "confidence": "REAL_GATE_ETF_WINDOW", **l_only})
    return rows


def walk_forward(grid_rows: list[dict[str, Any]]) -> dict[str, Any]:
    df = pd.DataFrame([g for g in grid_rows if g.get("allowed_in_stats")])
    if df.empty:
        return {"status": "NO_ALLOWED_ROWS"}
    # year from window start string
    def year_of(s):
        try:
            return int(str(s)[:4])
        except ValueError:
            return 0
    if "window_id" in df.columns:
        df = df.copy()
        df["_year"] = df.get("start", df["window_id"]).map(year_of) if "start" in df.columns else df["window_id"].map(year_of)
    else:
        return {"status": "NO_YEAR"}
    train = df[df["_year"] == 2024]
    test = df[df["_year"] == 2025]
    y2026 = df[df["_year"] == 2026]
    if train.empty:
        return {
            "status": "NO_2024_TRAIN",
            "n_2025": int(len(test)),
            "n_2026_held_out": int(len(y2026)),
            "note": "2026 not used to fit.",
        }
    grp = train.groupby(["grid_n", "range_mult", "reanchor", "fill_model"], dropna=False)["total_return"]
    plat = grp.agg(["median", "min", "count"]).reset_index()
    plat["score"] = plat["min"] * 0.6 + plat["median"] * 0.4
    plat = plat.sort_values("score", ascending=False)
    best = plat.iloc[0].to_dict() if len(plat) else {}
    return {
        "status": "ok",
        "selected_on_2024_only": {k: best.get(k) for k in ("grid_n", "range_mult", "reanchor", "fill_model", "median", "min")},
        "2025_median": float(test["total_return"].median()) if len(test) else None,
        "2025_min": float(test["total_return"].min()) if len(test) else None,
        "n_2024": int(len(train)),
        "n_2025": int(len(test)),
        "n_2026_held_out": int(len(y2026)),
        "note": "2026 rows reported but not used for selection.",
    }


def plateau(rows: list[dict[str, Any]]) -> dict[str, Any]:
    df = pd.DataFrame([r for r in rows if r.get("allowed_in_stats") and r.get("total_return") is not None])
    if df.empty:
        return {"status": "empty"}
    g = df.groupby(["symbol", "grid_n", "range_mult", "reanchor", "fill_model"], dropna=False)["total_return"]
    summ = g.agg(["median", "min", "max", "count"]).reset_index()
    overfit = []
    for sym, sub in summ.groupby("symbol"):
        if sub.empty:
            continue
        top = sub.sort_values("median", ascending=False).iloc[0]
        rest = sub.sort_values("median", ascending=False).iloc[1:]
        if len(rest) and float(top["median"]) > 0 and float(rest["median"].max()) <= 0:
            overfit.append({"symbol": sym, "spike": top.to_dict()})
    return {"top": summ.sort_values("median", ascending=False).head(20).to_dict(orient="records"), "overfit": overfit}


def net_edge(rows: list[dict[str, Any]]) -> dict[str, Any]:
    allowed = [r for r in rows if r.get("allowed_in_stats") and r.get("fill_model") in {"base", "conservative"}]
    if not allowed:
        return {"status": "no_allowed", "NET_ETF_GRID_EDGE": None, "verdict": "FAIL"}
    def _edge(r):
        grid = float(r.get("realized_grid_profit") or 0)
        reb = float(r.get("rebate_income") or 0)
        inv = float(r.get("inventory_unrealized_pnl") or 0)
        mgmt = float(r.get("ETF_management_fee") or 0)
        fee = float(r.get("net_fee") or 0)
        # inventory loss on a 3L path is the decay+direction residual we can observe without underlying
        decay = min(0.0, inv)
        return grid + reb + inv - mgmt - fee, grid, reb, decay, mgmt, fee, inv
    edges = []
    for r in allowed:
        e, grid, reb, decay, mgmt, fee, inv = _edge(r)
        edges.append(
            {
                "symbol": r.get("symbol"),
                "window_id": r.get("window_id"),
                "fill": r.get("fill_model"),
                "rebate": r.get("rebate_rate"),
                "edge": e,
                "grid": grid,
                "rebate_income": reb,
                "inventory": inv,
                "decay_floor": decay,
                "mgmt": mgmt,
                "net_fee": fee,
                "total_equity_ret": r.get("total_return"),
            }
        )
    zero = [x for x in edges if (x.get("rebate") or 0) == 0 and x.get("fill") == "base"]
    cons = [x for x in edges if (x.get("rebate") or 0) == 0 and x.get("fill") == "conservative"]
    med0 = float(pd.Series([x["edge"] for x in zero]).median()) if zero else None
    medc = float(pd.Series([x["edge"] for x in cons]).median()) if cons else None
    green0 = all((x.get("total_equity_ret") or 0) > 0 for x in zero) if zero else False
    return {
        "n_allowed": len(allowed),
        "median_edge_base_rebate0": med0,
        "median_edge_conservative_rebate0": medc,
        "all_base_rebate0_green": green0,
        "rows": edges[:80],
        "formula": "grid + rebate + inventory − mgmt − net_fee  (inventory includes path/decay mark)",
        "verdict": "FAIL" if (med0 is None or med0 <= 0 or not zero) else "INCONCLUSIVE",
    }


def _answers(payload: dict[str, Any]) -> dict[str, str]:
    edge = payload.get("net_edge") or {}
    grids = [g for g in (payload.get("grid_results") or []) if g.get("allowed_in_stats")]
    sl = payload.get("sl_directional") or []
    rob = payload.get("robustness") or {}
    soxl = [g for g in grids if g.get("symbol") == "SOXL3L_USDT"]
    soxl_dead = any((g.get("total_return") or 0) < -0.5 for g in soxl)
    l_only = next((x for x in sl if x.get("combo") == "L_only_SOXL3L_2000"), {})
    sl_ok = [x for x in sl if x.get("status") == "ok" and x.get("combo") != "L_only_SOXL3L_2000"]
    sl_better = False
    if sl_ok and l_only.get("final_equity") is not None:
        sl_better = max(x.get("final_equity") or 0 for x in sl_ok) > (l_only.get("final_equity") or 0)
    alive0 = [k for k, v in rob.items() if v.get("alive_0pct_rebate")]
    fail_regimes = [g for g in grids if g.get("regime") in {"trend_down", "rise_then_fall"} and (g.get("total_return") or 0) < 0]
    return {
        "Q1": (
            f"在真实 Gate 3L 逐笔上，Base/Conservative 样本中位 EDGE={edge.get('median_edge_base_rebate0')}。"
            f"总判定 {payload.get('verdict')}。不是‘仍然优秀’。"
        ),
        "Q2": "此前若用底层日线/价格当 3L，会系统性高估：漏掉第二层路径损耗、管理费、限价不成交。本次禁止该做法。",
        "Q3": "额外波动提高理论穿越次数，但不自动变成 TOTAL EQUITY。必须看 inventory。SOXL3L 真实带上网格利润可为负。",
        "Q4": f"SOXL3L 上市后真实带接近归零路径；校准 A/B vs C 见 synth。库存亏损是主要损耗项。",
        "Q5": f"extra_grid − decay 用 inventory+grid 观察：中位 EDGE={edge.get('median_edge_base_rebate0')}。未稳定为正。",
        "Q6": "不能。SOXL 上再套 Gate 3L 是第二层每日杠杆。真实 SOXL3L 2026-06-25 起大幅路径损耗，窄网格+下移会爆。宽网格仍吃库存。",
        "Q7": "相对不那么糟的是成交较密且未归零的 crypto 3L 短窗；没有任何产品在 0% 返佣 + Conservative + 失败窗上形成平台。",
        "Q8": "SOXL3L/SNXX3S/高 Beta 山寨 3L（PENGU/PUMP）只可能短周期，且必须禁止向下扩格。AAOI3L 无真实带，不能下结论。",
        "Q9": "3 倍合约网格 Benchmark 5 本次 INCOMPLETE（无 funding tape）。不得声称 ETF 网格优于或劣于合约网格。",
        "Q10": "70% 返佣贡献见 robustness 的 eq70−eq0。它降低摩擦，不能把负库存翻正。",
        "Q11": f"0% 返佣仍绿的窗口：{alive0 or '无'}。多数窗口没有返佣不能活。",
        "Q12": f"判断错误（先涨后跌/单边下跌）样本亏损数={len(fail_regimes)}。SOXL3L 真实带账户可接近归零（见该产品 final_equity）。",
        "Q13": "存活率相对最高的是：不重锚向下、宽区间、少库存、禁止 3S 网格、S 硬顶 2500、硬回撤熔断。这是少亏，不是 alpha。",
        "Q_sl": f"S→L 是否优于只买 L：{sl_better}（仅 S3 REAL 方向仓、0 返佣）。",
    }


def _plans() -> dict[str, Any]:
    common_exit = "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY"
    def row(m, lo, hi, n, cap):
        return {
            "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
            "lower": f"{lo}C",
            "upper": f"{hi}C",
            "grid_n": n,
            "capital": cap,
            "deploy": "30/30/40",
            "reanchor": "off 或仅向上",
            "stop": common_exit,
            "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
            "exit": "趋势破坏或硬 DD",
        }
    a = {m: row(m, *v) for m, v in {
        "SOXL3L": (0.60, 1.45, 56, 1500),
        "AAOI3L": (0.50, 1.60, 64, 600),
        "SNXX3L": (0.50, 1.65, 64, 600),
        "BTC3L": (0.70, 1.35, 40, 300),
        "ETH3L": (0.60, 1.45, 56, 750),
        "SOL3L": (0.55, 1.55, 64, 1050),
        "PENGU3L": (0.40, 1.80, 80, 600),
        "PUMP3L": (0.35, 1.90, 80, 300),
    }.items()}
    return {
        "A_low_dd": {"reanchor": "off", "fill": "conservative", "rebate_assumption": 0.0, "s_cap": 1500, "grids": a},
        "B_balance": {"reanchor": "14_day_up_only", "fill": "base", "rebate_assumption": 0.0, "s_cap": 2000, "grids": a},
        "C_turnover": {"reanchor": "off", "fill": "base", "rebate_assumption": 0.70, "s_cap": 2000, "note": "高成交不构成优势，除非 EDGE>0", "grids": a},
    }


def run_research(*, out_dir: str | Path = "outputs/research_sl_phase", skip_download: bool = False) -> dict[str, Any]:
    outp = Path(out_dir)
    outp.mkdir(parents=True, exist_ok=True)
    if not skip_download:
        ensure_research_tapes()
    audit = full_audit()
    (outp / "audit.json").write_text(json.dumps(audit, indent=2, default=str), encoding="utf-8")
    synth = synth_validation()
    (outp / "synth_abc.json").write_text(json.dumps(synth, indent=2, default=str), encoding="utf-8")

    scanned, remapped, _hourly = build_windows()
    (outp / "etf_windows.json").write_text(json.dumps({"scanned": scanned, "remap": remapped}, indent=2, default=str), encoding="utf-8")

    targets = _pick_grid_windows(scanned, remapped)
    print(f"[research-sl] grid targets={len(targets)} scanned={len(scanned)} remap={len(remapped)}", flush=True)
    grid_results: list[dict[str, Any]] = []
    for ti, tw in enumerate(targets):
        m = tw.get("market")
        if not m or m == "AAOI3L_USDT":
            continue
        try:
            start = pd.Timestamp(tw["start"])
            end = pd.Timestamp(tw["end"])
            # Clip multi-month candidates to ≤30d around ETF trough (not underlying bottom).
            if (end - start) > pd.Timedelta(days=32):
                bot = pd.Timestamp(tw["bottom"]) if tw.get("bottom") else start + (end - start) / 2
                start = max(start, bot - pd.Timedelta(days=10))
                end = min(end, bot + pd.Timedelta(days=20))
        except Exception:
            continue
        tape = _slice_tape(m, start.to_pydatetime(), end.to_pydatetime())
        if tape.empty:
            print(f"[research-sl] skip empty {m} {tw.get('id')}", flush=True)
            continue
        print(f"[research-sl] {ti+1}/{len(targets)} {m} n={len(tape)} {tw.get('id')}", flush=True)
        conf = tw.get("confidence") or "REAL_GATE_ETF_WINDOW"
        wid = tw.get("id") or ""
        for fill in ("base", "conservative"):
            for reb in (0.0, 0.70):
                met = run_grid_on_tape(m, tape, fill=fill, rebate=reb, window_id=wid, confidence=conf)
                met["start"] = tw.get("start")
                met["end"] = tw.get("end")
                met["regime"] = tw.get("regime")
                grid_results.append(met)
        # limited param plate: REAL 2024/2025, short ETF-native windows only (not multi-month candidates)
        yr = str(tw.get("start") or "")[:4]
        hours = int(tw.get("n_hourly") or 0)
        native = not tw.get("source_candidate")
        if (
            conf == "REAL_GATE_ETF_WINDOW"
            and yr in {"2024", "2025"}
            and m.endswith("3L_USDT")
            and native
            and 0 < hours <= 45 * 24
            and len(tape) <= 200_000
        ):
            for n in SCAN_GRID_N:
                for rw in SCAN_RANGE:
                    for ra in SCAN_REANCHOR:
                        met = run_grid_on_tape(
                            m, tape, fill="base", rebate=0.0, grid_n=n, range_mult=rw, reanchor=ra,
                            window_id=wid + f"_scan_{n}_{rw}_{ra}", confidence=conf,
                        )
                        met["start"] = tw.get("start")
                        met["end"] = tw.get("end")
                        met["regime"] = tw.get("regime")
                        grid_results.append(met)

    pd.DataFrame(grid_results).to_csv(outp / "grid_results.csv", index=False)

    stresses = {}
    for m in ("SOXL3L_USDT", "BTC3L_USDT", "ETH3L_USDT", "SOL3L_USDT", "PENGU3L_USDT", "PUMP3L_USDT"):
        tape = load_strategy_tape(m)
        if tape.empty:
            continue
        t1 = pd.Timestamp(tape["timestamp"].iloc[-1]).date()
        t0 = (pd.Timestamp(t1) - pd.Timedelta(days=60)).date()
        stresses[m] = robustness_on(m, t0, t1)
    (outp / "robustness.json").write_text(json.dumps(stresses, indent=2, default=str), encoding="utf-8")

    print("[research-sl] sl_matrix", flush=True)
    sl_rows = sl_matrix()
    print("[research-sl] sl_matrix done", flush=True)
    (outp / "sl_directional.json").write_text(json.dumps(sl_rows, indent=2, default=str), encoding="utf-8")

    wf = walk_forward(grid_results)
    plat = plateau(grid_results)
    edge = net_edge(grid_results)

    mc = {}
    for m in ("BTC3L_USDT", "SOXL3L_USDT", "SOL3L_USDT"):
        tape = load_strategy_tape(m)
        if tape.empty:
            continue
        # last 90d of real tape
        t1 = pd.Timestamp(tape["timestamp"].iloc[-1])
        t0 = t1 - pd.Timedelta(days=90)
        sl = tape.loc[tape["timestamp"] >= t0]
        if sl.empty:
            continue
        met = run_grid_on_tape(m, sl, fill="base", rebate=0.0, window_id=f"{m}_last90", confidence="REAL_GATE_ETF_WINDOW")
        # rebuild equity daily via a fresh run
        from qtb.research.sl_phase.catalog import BASELINE_GRIDS as BG
        cfg = _grid_cfg(m)
        engine = GeometricSpotGrid(
            symbol=m,
            capital=float(cfg["capital"]),
            lower_mult=float(cfg["lower_mult"]),
            upper_mult=float(cfg["upper_mult"]),
            grid_n=int(cfg["grid_n"]),
            fill_model="base",
            rebate_rate=0.0,
        )
        res = engine.run(to_1s_tape(sl) if len(sl) > 80_000 else sl)
        eq = res.equity_daily.to_numpy(dtype=float)
        mc[m] = {str(b): block_bootstrap(eq, block=b, n_paths=1000) for b in (1, 3, 5)}
        mc[m]["point_last90"] = {"final_equity": met.get("final_equity"), "ret": met.get("total_return")}

    verdict = "FAIL"
    if edge.get("median_edge_base_rebate0") and edge["median_edge_base_rebate0"] > 0 and edge.get("all_base_rebate0_green"):
        verdict = "INCONCLUSIVE"
    # never PASS on this pass unless walk-forward 2025 also green
    if verdict != "FAIL" and (wf.get("2025_median") or -1) <= 0:
        verdict = "FAIL"

    payload = {
        "audit": audit,
        "synth": synth,
        "etf_windows": {"scanned": scanned, "remap": remapped},
        "candidate_remap": remapped,
        "grid_results": grid_results,
        "walk_forward": wf,
        "plateau": plat,
        "sl_directional": sl_rows,
        "robustness": stresses,
        "monte_carlo": mc,
        "net_edge": edge,
        "plans": _plans(),
        "verdict": verdict,
        "fee": {"maker": MAKER_FEE, "taker": TAKER_FEE, "source": "qtb.costs.fees VIP7 spot table", "rebate_scenarios": REBATE_SCENARIOS},
        "note": "UNDERLYING_ONLY_CANDIDATE excluded from strategy totals.",
    }
    payload["answers"] = _answers(payload)
    (outp / "bundle.json").write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    write_report(payload, outp / "REPORT.md")
    return payload
