#!/usr/bin/env python3
"""P1-14: sha256 manifest for SOXL listing-length cache (does not touch 07-15 audit file)."""

from __future__ import annotations

import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data.manifest import DatasetManifest, sha256_file
from src.data.quality_gate import count_csv_rows


def main() -> int:
    start, end = date(2026, 5, 15), date(2026, 9, 11)
    cache = ROOT / "cache"
    files: list[Path] = []
    miss: list[str] = []
    d = start
    while d <= end:
        p = cache / f"binance_futures_SOXLUSDT_aggTrades_{d.isoformat()}.csv"
        if p.exists() and p.stat().st_size > 0:
            files.append(p)
        else:
            miss.append(d.isoformat())
        d += timedelta(days=1)
    entries = []
    rows = 0
    for f in files:
        entries.append(
            {
                "path": str(f.relative_to(ROOT)),
                "sha256": sha256_file(f),
                "bytes": f.stat().st_size,
            }
        )
        rows += count_csv_rows(f)
    man = DatasetManifest(
        venue="binance",
        symbol="SOXLUSDT",
        market="futures_um_aggTrades",
        start=start.isoformat(),
        end=end.isoformat(),
        source="binance_vision_daily",
        files=entries,
        rows=rows,
        missing_periods=miss,
        notes=["listing_length", f"day_files={len(files)}", "tech_perp_tradfi"],
    )
    out = ROOT / "data" / "manifests" / f"binance_SOXLUSDT_aggTrades_{start}_{end}.json"
    man.save(out)
    lab = ROOT / "soxl-lab" / "data" / "manifests" / out.name
    lab.write_text(out.read_text(encoding="utf-8"), encoding="utf-8")
    print(
        json.dumps(
            {
                "path": str(out),
                "days": len(files),
                "gaps": miss,
                "rows": rows,
                "bytes": sum(e["bytes"] for e in entries),
            },
            indent=2,
        )
    )
    return 0 if not miss else 1


if __name__ == "__main__":
    raise SystemExit(main())
