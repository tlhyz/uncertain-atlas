#!/usr/bin/env python3
"""Compare committed tick manifests to files still on disk. Does not download."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / "data" / "manifests"
CACHE = ROOT / "cache"


def _cache_tick_inventory() -> dict[str, dict]:
    by_sym: dict[str, list[str]] = defaultdict(list)
    pat = re.compile(r"binance_futures_([A-Z0-9]+)_aggTrades_(\d{4}-\d{2}-\d{2})\.csv$")
    if CACHE.is_dir():
        for p in CACHE.iterdir():
            m = pat.match(p.name)
            if not m or p.stat().st_size <= 0:
                continue
            by_sym[m.group(1)].append(m.group(2))
    return {
        sym: {
            "days": len(days),
            "start": min(days) if days else None,
            "end": max(days) if days else None,
        }
        for sym, days in sorted(by_sym.items())
    }


def _audit_manifest(path: Path) -> dict:
    man = json.loads(path.read_text())
    files = man.get("files") or []
    present = 0
    missing: list[str] = []
    bytes_ok = 0
    bytes_mismatch: list[str] = []
    for rec in files:
        p = ROOT / rec["path"]
        if p.exists() and p.stat().st_size > 0:
            present += 1
            if rec.get("bytes") is None or p.stat().st_size == rec.get("bytes"):
                bytes_ok += 1
            else:
                bytes_mismatch.append(rec["path"])
        else:
            missing.append(rec["path"])
    claimed = len(files)
    if claimed == 0:
        status = "empty_manifest"
    elif present == 0:
        status = "evicted"
    elif present < claimed:
        status = "partial"
    elif bytes_mismatch:
        status = "bytes_mismatch"
    else:
        status = "on_disk"
    return {
        "manifest": path.name,
        "symbol": man.get("symbol"),
        "start": man.get("start"),
        "end": man.get("end"),
        "claimed_files": claimed,
        "present": present,
        "missing": len(missing),
        "missing_head": missing[:5],
        "bytes_match": bytes_ok,
        "bytes_mismatch": len(bytes_mismatch),
        "status": status,
        "on_disk": status == "on_disk",
    }


def main() -> int:
    rows = [_audit_manifest(p) for p in sorted(MAN.glob("binance_*_aggTrades_*.json"))]
    cache = _cache_tick_inventory()
    claimed_syms = sorted({r["symbol"] for r in rows if r.get("symbol")})
    evicted = sorted(
        {
            r["symbol"]
            for r in rows
            if r["status"] == "evicted" and r["symbol"] not in cache
        }
    )
    on_disk_syms = [s for s in claimed_syms if s in cache]
    out = {
        "n_manifests": len(rows),
        "rows": rows,
        "cache_tick_symbols": cache,
        "claimed_symbols": claimed_syms,
        "on_disk_symbols": on_disk_syms,
        "evicted_symbols": evicted,
        "note": "audit only; does not re-download. ticks stay gitignored.",
    }
    dest = ROOT / "outputs" / "experiments" / "cache_vs_manifests"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "p1_15_audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print(
        json.dumps(
            {
                "cache": cache,
                "manifests": {
                    r["manifest"]: {
                        "symbol": r["symbol"],
                        "present": r["present"],
                        "claimed": r["claimed_files"],
                        "status": r["status"],
                    }
                    for r in rows
                },
                "evicted": evicted,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
