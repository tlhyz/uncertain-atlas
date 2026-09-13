#!/usr/bin/env python3
"""Build data/manifests/*.json from cache/ or data/raw/binance/."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import pandas as pd

from src.data.manifest import DatasetManifest, sha256_file, MANIFEST_DIR
from src.data.quality_gate import count_csv_rows


def _scan_cache(cache_dir: Path) -> dict[str, list[Path]]:
    pat = re.compile(r"binance_futures_(?P<sym>[A-Z0-9]+)_aggTrades_(?P<day>\d{4}-\d{2}-\d{2})\.csv$")
    groups: dict[str, list[tuple[date, Path]]] = defaultdict(list)
    for f in cache_dir.glob("binance_futures_*_aggTrades_*.csv"):
        m = pat.match(f.name)
        if not m:
            continue
        d = date.fromisoformat(m.group("day"))
        groups[m.group("sym")].append((d, f))
    return {k: [p for _, p in sorted(v)] for k, v in groups.items()}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--cache-dir", default="cache")
    p.add_argument("--raw-dir", default="data/raw/binance")
    args = p.parse_args()

    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    cache = Path(args.cache_dir)
    if cache.exists():
        for sym, files in _scan_cache(cache).items():
            if not files:
                continue
            days = sorted(
                date.fromisoformat(re.search(r"(\d{4}-\d{2}-\d{2})", f.name).group(1))  # type: ignore[union-attr]
                for f in files
            )
            total_rows = 0
            file_entries = []
            for f in files:
                file_entries.append({"path": str(f), "sha256": sha256_file(f), "bytes": f.stat().st_size})
                total_rows += count_csv_rows(f)
            notes = [f"day_files={len(files)}", f"rows_est={total_rows}"]
            if sym in ("SOXLUSDT", "SNXXUSDT"):
                notes.append("tech_perp_tradfi")
            m = DatasetManifest(
                venue="binance",
                symbol=sym,
                market="futures_um_aggTrades",
                start=str(days[0]),
                end=str(days[-1]),
                source="binance_vision_daily",
                files=file_entries,
                rows=total_rows,
                notes=notes,
            )
            out = MANIFEST_DIR / f"binance_{sym}_aggTrades_{days[0]}_{days[-1]}.json"
            m.save(out)
            count += 1
            print(f"[manifest] {sym} {days[0]}->{days[-1]} days={len(files)} rows~{total_rows}")

    raw = Path(args.raw_dir)
    if raw.exists():
        for f in sorted(raw.rglob("*.csv"))[:50]:
            m = DatasetManifest(
                venue="binance",
                symbol=f.stem.split("_")[0],
                market="futures_um",
                start="unknown",
                end="unknown",
                source="binance_vision",
                files=[{"path": str(f), "sha256": sha256_file(f), "bytes": f.stat().st_size}],
            )
            m.save()
            count += 1

    if count == 0:
        print("[warn] no files found — run download first")
        return 1
    print(f"[manifest] wrote {count} manifests to {MANIFEST_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
