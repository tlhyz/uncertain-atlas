#!/usr/bin/env python3
"""Adversarial corpus runner v0 — parse, list, validate.

Reads libraries/adversarial-corpus/README.md (pipe table rows C001+).
Future: hook each row to pytest / doc lint / copy-paste scanners.

Usage:
  python tools/adversarial_runner.py list [--limit N]
  python tools/adversarial_runner.py stats
  python tools/advisarial_runner.py validate
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "libraries" / "adversarial-corpus" / "README.md"

ROW_RE = re.compile(
    r"^\|\s*C(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$"
)


@dataclass(frozen=True)
class CorpusEntry:
    cid: int
    invariant: int
    slug: str
    body: str
    line_no: int


def parse_corpus(text: str) -> list[CorpusEntry]:
    entries: list[CorpusEntry] = []
    for i, line in enumerate(text.splitlines(), start=1):
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        cid = int(m.group(1))
        inv = int(m.group(2))
        slug = m.group(3).strip()
        body = m.group(4).strip()
        entries.append(CorpusEntry(cid, inv, slug, body, i))
    return entries


def cmd_list(entries: list[CorpusEntry], limit: int | None) -> None:
    show = entries[:limit] if limit else entries
    for e in show:
        print(f"C{e.cid:03d}  inv={e.invariant}  {e.slug[:60]}")


def cmd_stats(entries: list[CorpusEntry]) -> None:
    if not entries:
        print("No entries parsed.")
        return
    invs = {e.invariant for e in entries}
    print(f"entries={len(entries)}")
    print(f"invariants_referenced={len(invs)}")
    print(f"cid_range=C{entries[-1].cid:03d}..C{entries[0].cid:03d}")
    print(f"invariant_range={min(invs)}..{max(invs)}")


def cmd_validate(entries: list[CorpusEntry]) -> int:
    errors: list[str] = []
    seen_cid: dict[int, int] = {}
    for e in entries:
        if e.cid in seen_cid:
            errors.append(f"duplicate C{e.cid:03d} at lines {seen_cid[e.cid]} and {e.line_no}")
        seen_cid[e.cid] = e.line_no
        if not e.slug:
            errors.append(f"C{e.cid:03d}: empty slug")
        if e.invariant <= 0:
            errors.append(f"C{e.cid:03d}: invalid invariant {e.invariant}")
        if len(e.body) < 20:
            errors.append(f"C{e.cid:03d}: body too short")
    if errors:
        for err in errors[:50]:
            print(err, file=sys.stderr)
        if len(errors) > 50:
            print(f"... and {len(errors) - 50} more", file=sys.stderr)
        return 1
    print(f"OK: {len(entries)} corpus rows validated")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Uncertain Atlas adversarial corpus runner v0")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List corpus entries (newest first in file)")
    p_list.add_argument("--limit", type=int, default=None)

    sub.add_parser("stats", help="Summary statistics")
    sub.add_parser("validate", help="Validate corpus table integrity")

    args = parser.parse_args()
    if not CORPUS.is_file():
        print(f"Missing corpus: {CORPUS}", file=sys.stderr)
        return 2
    entries = parse_corpus(CORPUS.read_text(encoding="utf-8"))
    if args.cmd == "list":
        cmd_list(entries, args.limit)
        return 0
    if args.cmd == "stats":
        cmd_stats(entries)
        return 0
    if args.cmd == "validate":
        return cmd_validate(entries)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
