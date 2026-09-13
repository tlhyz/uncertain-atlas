#!/usr/bin/env python3
"""Build data/manifests/*.json from downloaded raw files."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.data.manifest import DatasetManifest, sha256_file, MANIFEST_DIR


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--raw-dir", default="data/raw/binance")
    args = p.parse_args()
    raw = Path(args.raw_dir)
    if not raw.exists():
        print(f"[warn] {raw} missing — run scripts/download_binance.py first")
        return 1
    count = 0
    for f in sorted(raw.rglob("*.csv"))[:50]:
        m = DatasetManifest(
            venue="binance",
            symbol=f.stem.split("_")[0] if "_" in f.stem else f.stem,
            market="futures_um",
            start="unknown",
            end="unknown",
            source="binance_vision",
            files=[{"path": str(f), "sha256": sha256_file(f), "bytes": f.stat().st_size}],
            rows=0,
        )
        m.save()
        count += 1
    print(f"[manifest] wrote {count} manifests to {MANIFEST_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
