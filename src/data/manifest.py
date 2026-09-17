"""Dataset manifest I/O — reproducibility audit trail."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MANIFEST_DIR = Path("data/manifests")


@dataclass
class DatasetManifest:
    venue: str
    symbol: str
    market: str
    start: str
    end: str
    source: str
    files: list[dict[str, Any]] = field(default_factory=list)
    rows: int = 0
    missing_periods: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def save(self, path: Path | None = None) -> Path:
        MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
        out = path or MANIFEST_DIR / f"{self.venue}_{self.symbol}_{self.market}_{self.start}_{self.end}.json"
        out.write_text(json.dumps(asdict(self), indent=2, ensure_ascii=False), encoding="utf-8")
        return out


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
