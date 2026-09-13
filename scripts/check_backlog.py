#!/usr/bin/env python3
"""Print next pending research tasks from RESEARCH_BACKLOG.md."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

BACKLOG = Path("docs/RESEARCH_BACKLOG.md")


def parse_pending(path: Path) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("| ID") or line.startswith("|----"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 3:
            continue
        tid, task, status = parts[0], parts[1], parts[2].lower()
        if status == "pending":
            rows.append((tid, task, status))
    return rows


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--next", type=int, default=5, help="how many pending tasks to show")
    p.add_argument("--phase", default="", help="filter e.g. P1")
    args = p.parse_args()

    if not BACKLOG.exists():
        print(f"[error] missing {BACKLOG}")
        return 1

    pending = parse_pending(BACKLOG)
    if args.phase:
        pending = [(i, t, s) for i, t, s in pending if i.startswith(args.phase)]

    print(f"# Next {args.next} pending tasks (from {BACKLOG})\n")
    for tid, task, _ in pending[: args.next]:
        print(f"  {tid}: {task}")
    if not pending:
        print("  (none — update backlog or advance phase)")
    print(f"\nTotal pending: {len(pending)}")
    print("North star: docs/RESEARCH_GOALS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
