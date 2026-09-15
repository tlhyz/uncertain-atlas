#!/usr/bin/env python3
"""Three independent audits of the SOXL-only lab. Exit 0 only if all pass.

Pass 1 = data (files, gaps, sha256 sample, coverage)
Pass 2 = params (yaml vs USER_* constants vs runner)
Pass 3 = results (P7-04 floats, P7-05 daily CSV, review-log strings)

Run three times:  python3 scripts/verify_three_passes.py --times 3
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARENT = Path(os.environ.get("SOXLLAB_PARENT", ROOT.parent))
CACHE = Path(os.environ.get("SOXLLAB_CACHE", PARENT / "cache"))
MANIFEST = ROOT / "data" / "manifests" / "binance_SOXLUSDT_aggTrades_2026-07-15_2026-09-11.json"
TICK_COV = ROOT / "results" / "p7_tick_coverage.soxl.json"
TICK_HEDGE = ROOT / "results" / "p7_tick_hedge_report.json"
P705_JSON = ROOT / "results" / "p7_05_usdt20.json"
P705_CSV = ROOT / "results" / "p7_05_usdt20_daily.csv"
P705_PCT_JSON = ROOT / "results" / "p7_05_pct20.json"
P705_PCT_CSV = ROOT / "results" / "p7_05_pct20_daily.csv"
REVIEW = PARENT / "outputs" / "review_logs" / "2026-09-15_P7-04_tick_pair_hedge_FAIL.md"
CODE = PARENT / "src" / "analysis" / "user_moving_grid.py"
RUNNER = PARENT / "scripts" / "run_p7_user_soxl_ls_grid.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def pass1_data() -> list[str]:
    errs: list[str] = []
    if not MANIFEST.exists():
        return [f"missing manifest {MANIFEST}"]
    man = json.loads(MANIFEST.read_text())
    if man.get("symbol") != "SOXLUSDT":
        errs.append("manifest symbol")
    if man.get("start") != "2026-07-15" or man.get("end") != "2026-09-11":
        errs.append(f"manifest window {man.get('start')}->{man.get('end')}")
    if int(man.get("rows") or 0) != 31_190_286:
        errs.append(f"manifest rows {man.get('rows')}")
    if len(man.get("files") or []) != 59:
        errs.append(f"manifest files {len(man.get('files') or [])}")

    files = sorted(CACHE.glob("binance_futures_SOXLUSDT_aggTrades_*.csv"))
    if not files:
        errs.append("cache absent — sha256 sample skipped (set SOXLLAB_CACHE)")
        return errs
    if len(files) != 59:
        errs.append(f"expected 59 SOXL day files, got {len(files)}")
    days = [re.search(r"(\d{4}-\d{2}-\d{2})", f.name).group(1) for f in files]  # type: ignore[union-attr]
    if days[0] != "2026-07-15" or days[-1] != "2026-09-11":
        errs.append(f"day span {days[0]}->{days[-1]} != 2026-07-15->2026-09-11")
    d0, d1 = date.fromisoformat(days[0]), date.fromisoformat(days[-1])
    have = set(days)
    miss = []
    d = d0
    while d <= d1:
        if d.isoformat() not in have:
            miss.append(d.isoformat())
        d += timedelta(days=1)
    if miss:
        errs.append(f"gap days {miss}")
    if len(man["files"]) != len(files):
        errs.append(f"manifest files {len(man['files'])} vs cache {len(files)}")
    bytes_total = sum(f.stat().st_size for f in files)
    if bytes_total != 1_646_097_593:
        errs.append(f"bytes_total {bytes_total}")
    sample_idx = [0, len(man["files"]) // 2, len(man["files"]) - 1]
    for i in sample_idx:
        rec = man["files"][i]
        p = PARENT / rec["path"]
        if not p.exists():
            errs.append(f"missing {rec['path']}")
            continue
        if p.stat().st_size != rec["bytes"]:
            errs.append(f"bytes mismatch {p.name}")
        if sha256_file(p) != rec["sha256"]:
            errs.append(f"sha256 mismatch {p.name}")
    cov = json.loads(TICK_COV.read_text())["soxl"]
    if cov["bars_with_trades"] != 1392 or cov["bars_missing_trades"] != 0:
        errs.append(f"coverage {cov}")
    return errs


def pass2_params() -> list[str]:
    errs: list[str] = []
    text = (ROOT / "params" / "user_moving_grid.yaml").read_text()
    for needle in (
        "leverage: 5",
        "n_grids: 200",
        "capital_per_side_usdt: 5000",
        "range_usdt: 20",
        "range_pct: 0.20",
        "symbol: SOXLUSDT",
    ):
        if needle not in text:
            errs.append(f"params missing {needle}")
    if not CODE.exists():
        errs.append(f"engine missing {CODE}")
        return errs
    code = CODE.read_text()
    for needle in (
        "USER_LEVERAGE = 5.0",
        "USER_RANGE_USDT = 20.0",
        "USER_RANGE_PCT = 0.20",
        "USER_N_GRIDS = 200",
        "USER_CAPITAL_PER_SIDE = 5_000.0",
    ):
        if needle not in code:
            errs.append(f"code missing {needle}")
    runner = RUNNER.read_text() if RUNNER.exists() else ""
    if "SOXLUSDT" not in runner:
        errs.append("runner missing SOXLUSDT")
    if 'for mode in ("usdt", "pct")' not in runner:
        errs.append("runner does not sweep usdt and pct")
    win = (ROOT / "params" / "windows.yaml").read_text()
    for needle in ("days: 59", "rows: 31190286", "bytes: 1646097593"):
        if needle not in win:
            errs.append(f"windows.yaml missing {needle}")
    return errs


def pass3_results() -> list[str]:
    errs: list[str] = []
    rep = json.loads(TICK_HEDGE.read_text())
    base = rep["reports"]["base"]["strategies"]
    checks = {
        ("soxl_only_long_grid", "return"): 0.09294857771169296,
        ("soxl_only_long_grid", "max_dd"): -0.4523858193921777,
        ("same_symbol_long_short", "return"): 0.12265694723873422,
        ("same_symbol_long_short", "max_dd"): -0.1768218024214585,
        ("pair_soxl_soxs_long_grids", "return"): -0.059711155429567175,
        ("pair_soxl_soxs_long_grids", "max_dd"): -0.2006603284068864,
        ("bh_50_50_daily", "return"): 0.029391248512844248,
        ("bh_50_50_daily", "max_dd"): -0.02264370545918526,
    }
    for (strat, field), exp in checks.items():
        got = float(base[strat][field])
        if abs(got - exp) > 1e-12:
            errs.append(f"{strat}.{field} {got} != {exp}")
    if base["soxl_only_long_grid"].get("fill_engine") != "tick":
        errs.append("soxl_only not tick")

    p705 = json.loads(P705_JSON.read_text())
    expect_705 = {
        "return": -0.12777656047524233,
        "max_dd": -0.8015703503012668,
        "end_equity": 8722.234395247577,
        "n_days": 58,
        "win_days": 28,
        "best_day": 4606.532998124249,
        "worst_day": -5543.7182427782245,
    }
    for k, exp in expect_705.items():
        got = p705[k]
        if isinstance(exp, float):
            if abs(float(got) - exp) > 1e-12:
                errs.append(f"p705.{k} {got} != {exp}")
        elif got != exp:
            errs.append(f"p705.{k} {got} != {exp}")
    if p705.get("liquidated_long") is not True:
        errs.append("p705 long must be liquidated")
    if p705.get("fill_engine") != "tick":
        errs.append("p705 not tick")
    if p705.get("range_mode") != "usdt":
        errs.append("p705 range_mode")

    # daily CSV must reproduce return / days / extrema
    lines = P705_CSV.read_text().strip().splitlines()
    if len(lines) - 1 != 58:
        errs.append(f"p705 csv rows {len(lines)-1}")
    last = lines[-1].split(",")
    # date,equity,daily_pnl,daily_ret,cum_ret
    if abs(float(last[1]) - 8722.234395247577) > 1e-9:
        errs.append(f"p705 csv end equity {last[1]}")
    if abs(float(last[4]) - (-0.12777656047524233)) > 1e-12:
        errs.append(f"p705 csv cum_ret {last[4]}")
    pnls = [float(row.split(",")[2]) for row in lines[1:]]
    if abs(max(pnls) - 4606.532998124249) > 1e-9:
        errs.append("p705 csv best_day")
    if abs(min(pnls) - (-5543.7182427782245)) > 1e-9:
        errs.append("p705 csv worst_day")
    if sum(1 for x in pnls if x > 0) != 28:
        errs.append("p705 csv win_days")

    pct = json.loads(P705_PCT_JSON.read_text())
    expect_pct = {
        "return": -0.18650635696806295,
        "max_dd": -0.7716279958553999,
        "end_equity": 8134.936430319371,
        "n_days": 58,
        "win_days": 29,
        "best_day": 4033.8665681258103,
        "worst_day": -4854.544554822065,
    }
    for k, exp in expect_pct.items():
        got = pct[k]
        if isinstance(exp, float):
            if abs(float(got) - exp) > 1e-12:
                errs.append(f"p705pct.{k} {got} != {exp}")
        elif got != exp:
            errs.append(f"p705pct.{k} {got} != {exp}")
    if pct.get("liquidated_long") is not True:
        errs.append("p705pct long must be liquidated")
    if pct.get("fill_engine") != "tick" or pct.get("range_mode") != "pct":
        errs.append("p705pct engine/mode")
    pct_lines = P705_PCT_CSV.read_text().strip().splitlines()
    if len(pct_lines) - 1 != 58:
        errs.append(f"p705pct csv rows {len(pct_lines)-1}")
    pct_last = pct_lines[-1].split(",")
    if abs(float(pct_last[1]) - 8134.936430319371) > 1e-9:
        errs.append(f"p705pct csv end equity {pct_last[1]}")
    if abs(float(pct_last[4]) - (-0.18650635696806295)) > 1e-12:
        errs.append(f"p705pct csv cum_ret {pct_last[4]}")
    pct_pnls = [float(row.split(",")[2]) for row in pct_lines[1:]]
    if abs(max(pct_pnls) - 4033.8665681258103) > 1e-9:
        errs.append("p705pct csv best_day")
    if abs(min(pct_pnls) - (-4854.544554822065)) > 1e-9:
        errs.append("p705pct csv worst_day")
    if sum(1 for x in pct_pnls if x > 0) != 29:
        errs.append("p705pct csv win_days")

    if REVIEW.exists():
        log = REVIEW.read_text()
        for s in ("−6.0%", "−20.1%", "+12.3%", "−17.7%", "1392/1392"):
            if s not in log and s.replace("−", "-") not in log:
                if s not in log:
                    errs.append(f"review log missing {s}")
    return errs


def one_run() -> dict:
    results = {
        "pass1_data": pass1_data(),
        "pass2_params": pass2_params(),
        "pass3_results": pass3_results(),
    }
    ok = all(len(v) == 0 for v in results.values())
    return {"ok": ok, "errors": results}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--times", type=int, default=1)
    args = ap.parse_args()
    audit_dir = ROOT / "results" / "audit"
    audit_dir.mkdir(parents=True, exist_ok=True)
    all_ok = True
    bundle = []
    for i in range(1, args.times + 1):
        rec = one_run()
        rec["pass_index"] = i
        bundle.append(rec)
        (audit_dir / f"run_{i}.json").write_text(json.dumps(rec, indent=2) + "\n")
        print(json.dumps(rec, indent=2))
        all_ok = all_ok and rec["ok"]
    (audit_dir / "three_passes.json").write_text(json.dumps({"ok": all_ok, "runs": bundle}, indent=2) + "\n")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
