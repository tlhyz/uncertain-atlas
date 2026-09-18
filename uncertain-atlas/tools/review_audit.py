#!/usr/bin/env python3
"""Self-review audit for Uncertain Atlas.

Writes REVIEW_REPORT.md. Exit 0 if no high-severity gaps; 1 if high gaps.
Never touches qtb/.
"""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
REPORT = ROOT / "REVIEW_REPORT.md"


def exists(rel: str) -> bool:
    return (ROOT / rel).is_file()


def read(rel: str) -> str:
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def qtb_dirty() -> list[str]:
    try:
        out = subprocess.check_output(
            ["git", "status", "--short"],
            cwd=REPO,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    hits = []
    for line in out.splitlines():
        path = line[3:].strip()
        if path.startswith(("qtb/", "strategies/", "configs/", "backtest.py")):
            hits.append(path)
    return hits


def corpus_ok() -> tuple[bool, str]:
    runner = ROOT / "tools" / "adversarial_runner.py"
    if not runner.is_file():
        return False, "adversarial_runner.py missing"
    try:
        p = subprocess.run(
            [sys.executable, str(runner), "validate"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    except OSError as e:
        return False, str(e)
    msg = (p.stdout + p.stderr).strip()
    return p.returncode == 0, msg or f"exit {p.returncode}"


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows: list[tuple[str, str, str, str]] = []

    def check(rid: str, sev: str, ok: bool, detail: str) -> None:
        rows.append((rid, sev, "pass" if ok else "FAIL", detail))

    check("R1a", "high", exists("GOAL.md"), "GOAL.md")
    check("R1b", "high", exists("ARCHITECTURE.md"), "ARCHITECTURE.md")
    check("R1c", "high", exists("ROADMAP.md"), "ROADMAP.md")
    check("R1d", "high", exists("REVIEW_LOOP.md"), "REVIEW_LOOP.md")

    consensus = read("libraries/decision-matrix/consensus.md")
    state = read("libraries/decision-matrix/state-model.md")
    check(
        "R2a",
        "high",
        "不确定候选" in consensus and "（空）" not in consensus.split("不确定候选")[-1][:200],
        "consensus 不确定列",
    )
    check(
        "R2b",
        "high",
        "不确定候选" in state and "精简 UTXO" in state,
        "state-model 不确定列",
    )

    ok, msg = corpus_ok()
    check("R3", "high", ok, msg[:240])

    arch = read("ARCHITECTURE.md")
    check("R4", "med", "1430" in arch or "不变量" in arch, "ARCHITECTURE 含进度数字")

    check("R5a", "high", exists("libraries/threat-model/INDEX.md"), "threat-model INDEX")
    check("R5b", "high", exists("libraries/threat-model/actors.md"), "actors.md")
    check("R5c", "high", exists("libraries/threat-model/assets.md"), "assets.md")
    check("R5d", "high", exists("libraries/threat-model/boundaries.md"), "boundaries.md")

    dirty = qtb_dirty()
    check("R7", "high", not dirty, "qtb dirty: " + ", ".join(dirty) if dirty else "trading tree clean")

    high_fail = [r for r in rows if r[1] == "high" and r[2] == "FAIL"]
    next_work = []
    if any(r[0].startswith("R5") and r[2] == "FAIL" for r in rows):
        next_work.append("P1-1 补 threat-model v1（INDEX / actors / assets / boundaries）")
    if any(r[0].startswith("R2") and r[2] == "FAIL" for r in rows):
        next_work.append("P0-4 回填决策矩阵不确定列")
    if any(r[0] == "R3" and r[2] == "FAIL" for r in rows):
        next_work.append("修 adversarial corpus / runner")
    copy = read("libraries/settlement-copy.md")
    check("R8", "med", "commit 高度" in copy and "AppHash" in copy, "settlement-copy 对齐 Y")
    proto = read("protocols/README.md")
    check("R9", "med", "永久过滤器" in proto, "protocols 永久过滤器声明")
    check("R10", "med", exists("tools/atlas_index.py"), "atlas_index.py")
    check("R11", "med", exists("tracks/post-quantum/cpu-measurement-method.md"), "PQ CPU 测量方法")

    link_script = ROOT / "tools" / "invariant_corpus_links.py"
    if link_script.is_file():
        try:
            lp = subprocess.run(
                [sys.executable, str(link_script)],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            link_ok = lp.returncode == 0
            link_msg = (lp.stdout + lp.stderr).strip().splitlines()[-1][:200] if (lp.stdout + lp.stderr).strip() else f"exit {lp.returncode}"
        except OSError as e:
            link_ok, link_msg = False, str(e)
    else:
        link_ok, link_msg = False, "invariant_corpus_links.py missing"
    check("R12", "med", link_ok, link_msg)

    if not next_work:
        next_work.append("P1-3 官方三事 1431+")
        next_work.append("P3-3 merge KB snapshot branches")
        next_work.append("P1-5 按 cpu-measurement-method 补实测数字（无机器则保持空）")

    lines = [
        f"# Review Report · {now}",
        "",
        "由 `tools/review_audit.py` 生成。人工复审仍看 [`REVIEW_LOOP.md`](REVIEW_LOOP.md)。",
        "",
        "| ID | 严重度 | 结果 | 说明 |",
        "|---|---|---|---|",
    ]
    for rid, sev, status, detail in rows:
        lines.append(f"| {rid} | {sev} | {status} | {detail.replace('|', '/')} |")
    lines += [
        "",
        "## 本轮建议执行",
        "",
    ]
    for i, item in enumerate(next_work, 1):
        lines.append(f"{i}. {item}")
    lines += [
        "",
        f"high_fail={len(high_fail)}",
        "",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT)
    print(f"high_fail={len(high_fail)}")
    return 1 if high_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
