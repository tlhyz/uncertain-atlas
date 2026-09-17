#!/usr/bin/env python3
"""P3-2: bidirectional invariant ↔ corpus link check.

Corpus rows name an invariant ID. Recent unbundling pages (inv >= 650)
must have both a corpus row and a markdown mention of 不变量 N.

Historical gaps (inv < 650 missing a numbered README entry) are listed
as warnings and do not fail the default gate.

Usage:
  python tools/invariant_corpus_links.py
  python tools/invariant_corpus_links.py --min-inv 650
  python tools/invariant_corpus_links.py --strict-all
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "libraries" / "adversarial-corpus" / "README.md"
INV_README = ROOT / "libraries" / "invariants" / "README.md"

ROW_RE = re.compile(r"^\|\s*C(\d+)\s*\|\s*(\d+)\s*\|")
INV_MENTION_RE = re.compile(r"不变量\s*(\d+)")
INV_HEAD_RE = re.compile(r"^(\d+)\.\s+\*\*", re.M)


def corpus_invariants() -> dict[int, list[int]]:
    """invariant -> list of Cxx ids."""
    mapping: dict[int, list[int]] = {}
    if not CORPUS.is_file():
        return mapping
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line.strip())
        if not m:
            continue
        cid, inv = int(m.group(1)), int(m.group(2))
        mapping.setdefault(inv, []).append(cid)
    return mapping


def numbered_heads() -> set[int]:
    """Invariant IDs that have a numbered entry in invariants/README.md."""
    if not INV_README.is_file():
        return set()
    return {int(n) for n in INV_HEAD_RE.findall(INV_README.read_text(encoding="utf-8"))}


def mentioned_invariants() -> set[int]:
    """Any markdown mention of 不变量 N, plus numbered README heads.

    Used only to prove a corpus row is referenced somewhere.
    The reverse gate (mentioned → corpus) uses numbered_heads so
    cross-references to older IDs do not fail the ≥650 check.
    """
    found = set(numbered_heads())
    if INV_README.is_file():
        found.update(int(n) for n in INV_MENTION_RE.findall(INV_README.read_text(encoding="utf-8")))
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("tools/") or path.name == "REVIEW_REPORT.md":
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "不变量" not in text:
            continue
        found.update(int(n) for n in INV_MENTION_RE.findall(text))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description="Check invariant ↔ corpus links")
    ap.add_argument("--min-inv", type=int, default=650, help="Fail gate starts at this inv")
    ap.add_argument("--strict-all", action="store_true", help="Fail on any missing link")
    args = ap.parse_args()

    corpus = corpus_invariants()
    mentioned = mentioned_invariants()
    heads = numbered_heads()
    corpus_invs = set(corpus)

    missing_mention = sorted(
        i for i in corpus_invs if i >= (1 if args.strict_all else args.min_inv) and i not in mentioned
    )
    # Reverse gate: a numbered README head ≥ gate must have a corpus row.
    missing_corpus = sorted(
        i for i in heads if i >= args.min_inv and i not in corpus_invs
    )

    print(f"corpus_invariants={len(corpus_invs)}")
    print(f"mentioned_invariants={len(mentioned)}")
    print(f"numbered_heads={len(heads)}")
    print(f"gate_min_inv={1 if args.strict_all else args.min_inv}")

    warn_old = sorted(i for i in corpus_invs if i < args.min_inv and i not in mentioned)
    if warn_old and not args.strict_all:
        print(f"warn_corpus_without_mention_below_gate={len(warn_old)}")

    errors = 0
    if missing_mention:
        print("FAIL corpus row has no markdown mention:", ", ".join(f"{i}" for i in missing_mention[:40]))
        errors += 1
    if missing_corpus:
        print("FAIL mentioned inv >= gate has no corpus row:", ", ".join(f"{i}" for i in missing_corpus[:40]))
        errors += 1
    if errors:
        return 1
    print("OK: invariant ↔ corpus links hold for gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
