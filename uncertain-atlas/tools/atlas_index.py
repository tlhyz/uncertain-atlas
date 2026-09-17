#!/usr/bin/env python3
"""Local Markdown catalog for Uncertain Atlas (P3-1).

Walks uncertain-atlas/**/*.md (skips generated REVIEW_REPORT.md by default
when --skip-generated). Writes JSON directory to tools/atlas_index.json.

Usage:
  python tools/atlas_index.py
  python tools/atlas_index.py --out /tmp/atlas_index.json
  python tools/atlas_index.py --stats
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "tools" / "atlas_index.json"

HEADING_RE = re.compile(r"^#\s+(.+?)\s*$")
SKIP_NAMES = {"REVIEW_REPORT.md"}


def first_heading(text: str) -> str | None:
    for line in text.splitlines()[:40]:
        m = HEADING_RE.match(line)
        if m:
            return m.group(1).strip()
    return None


def track_of(rel: str) -> str:
    parts = Path(rel).parts
    if not parts:
        return "root"
    if parts[0] in {
        "index",
        "courses",
        "protocols",
        "tracks",
        "libraries",
        "tools",
        "exams",
    }:
        if parts[0] == "tracks" and len(parts) > 1:
            return f"tracks/{parts[1]}"
        if parts[0] == "libraries" and len(parts) > 1:
            return f"libraries/{parts[1]}"
        if parts[0] == "courses" and len(parts) > 1:
            return f"courses/{parts[1]}"
        if parts[0] == "protocols" and len(parts) > 1:
            return f"protocols/{parts[1]}"
        return parts[0]
    return "root"


def collect(skip_generated: bool) -> list[dict]:
    rows: list[dict] = []
    for path in sorted(ROOT.rglob("*.md")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if skip_generated and path.name in SKIP_NAMES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        title = first_heading(text) or path.stem
        rows.append(
            {
                "path": rel,
                "title": title,
                "track": track_of(rel),
                "bytes": path.stat().st_size,
            }
        )
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description="Build Uncertain Atlas Markdown index")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--skip-generated", action="store_true", default=True)
    args = ap.parse_args()

    rows = collect(skip_generated=args.skip_generated)
    payload = {
        "root": "uncertain-atlas",
        "count": len(rows),
        "files": rows,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if args.stats:
        tracks: dict[str, int] = {}
        for r in rows:
            tracks[r["track"]] = tracks.get(r["track"], 0) + 1
        print(f"files={len(rows)}")
        print(f"out={args.out}")
        for k in sorted(tracks):
            print(f"  {k}: {tracks[k]}")
    else:
        print(args.out)
        print(f"files={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
