"""Pre-experiment data quality gate — blocks runs on corrupt or incomplete data."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from src.data.manifest import DatasetManifest, sha256_file


class DataQualityError(RuntimeError):
    """Raised when data quality checks fail and the experiment must not run."""

    def __init__(self, message: str, report: DataQualityReport | None = None):
        super().__init__(message)
        self.report = report


@dataclass
class DataQualityThresholds:
    min_rows: int = 1
    max_missing_rate: float = 0.05
    max_gap_fraction: float = 0.10
    max_duplicate_rate: float = 0.001
    max_time_disorder_rate: float = 0.0
    min_file_bytes: int = 64
    require_manifest_rows_match: bool = False  # if True, manifest.rows must match recount


@dataclass
class FileQualityCheck:
    path: str
    exists: bool
    bytes: int
    rows: int
    missing_rate: float
    duplicate_rate: float
    time_disorder_rate: float
    gap_count: int
    passed: bool
    issues: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ManifestQualityCheck:
    path: str
    symbol: str
    manifest_rows: int
    recounted_rows: int
    file_checks: list[FileQualityCheck]
    passed: bool
    issues: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["file_checks"] = [fc.as_dict() if hasattr(fc, "as_dict") else fc for fc in self.file_checks]
        return d


@dataclass
class DataQualityReport:
    passed: bool
    created_at: str
    manifest_checks: list[ManifestQualityCheck]
    failures: list[str]
    thresholds: dict[str, Any]

    def as_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "created_at": self.created_at,
            "failures": self.failures,
            "thresholds": self.thresholds,
            "manifest_checks": [m.as_dict() for m in self.manifest_checks],
        }

    def save(self, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.as_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
        return path


def _time_series_from_csv(path: Path) -> pd.Series | None:
    """Return monotonic time series from aggTrades CSV (ts_ms or timestamp column)."""
    try:
        sample = pd.read_csv(path, nrows=5)
    except Exception:
        return None
    if sample.empty:
        return None
    if "ts_ms" in sample.columns:
        full = pd.read_csv(path, usecols=["ts_ms"])
        ts = pd.to_numeric(full["ts_ms"], errors="coerce")
        return pd.to_datetime(ts, unit="ms", utc=True, errors="coerce")
    if "timestamp" in sample.columns:
        full = pd.read_csv(path, usecols=["timestamp"])
        return pd.to_datetime(full["timestamp"], utc=True, errors="coerce")
    return None


def count_csv_rows(path: Path) -> int:
    """Count data rows in aggTrades CSV using ts_ms or timestamp column."""
    try:
        sample = pd.read_csv(path, nrows=1)
    except Exception:
        return 0
    if sample.empty:
        return 0
    col = "ts_ms" if "ts_ms" in sample.columns else "timestamp" if "timestamp" in sample.columns else None
    if col is None:
        return max(0, sum(1 for _ in open(path, encoding="utf-8", errors="replace")) - 1)
    try:
        return len(pd.read_csv(path, usecols=[col]))
    except Exception:
        return 0


def inspect_csv_file(path: Path, thresholds: DataQualityThresholds) -> FileQualityCheck:
    issues: list[str] = []
    p = Path(path)
    if not p.is_absolute():
        p = Path.cwd() / p
    exists = p.exists()
    nbytes = p.stat().st_size if exists else 0
    rows = count_csv_rows(p) if exists else 0
    missing_rate = 0.0
    duplicate_rate = 0.0
    time_disorder_rate = 0.0
    gap_count = 0

    if not exists:
        issues.append("file_missing")
    elif nbytes < thresholds.min_file_bytes:
        issues.append(f"file_too_small:{nbytes}")
    elif rows < thresholds.min_rows:
        issues.append(f"rows_below_min:{rows}<{thresholds.min_rows}")

    if exists and rows > 0:
        ts = _time_series_from_csv(p)
        if ts is not None and len(ts) > 0:
            missing_rate = float(ts.isna().mean())
            if missing_rate > thresholds.max_missing_rate:
                issues.append(f"missing_rate:{missing_rate:.4f}>{thresholds.max_missing_rate}")
            valid = ts.dropna()
            if len(valid) > 1:
                # aggTrades: many rows share the same ms — dedupe on agg_id if present
                try:
                    sample_cols = pd.read_csv(p, nrows=1).columns
                    if "agg_id" in sample_cols:
                        ids = pd.read_csv(p, usecols=["agg_id"])
                        duplicate_rate = float(ids.duplicated(subset=["agg_id"]).mean())
                    else:
                        duplicate_rate = float(valid.duplicated().mean())
                except Exception:
                    duplicate_rate = 0.0
                if duplicate_rate > thresholds.max_duplicate_rate:
                    issues.append(f"duplicate_rate:{duplicate_rate:.4f}>{thresholds.max_duplicate_rate}")
                diffs = valid.sort_values().diff().dropna()
                if len(diffs) > 0:
                    neg = diffs < pd.Timedelta(0)
                    time_disorder_rate = float(neg.mean())
                    if time_disorder_rate > thresholds.max_time_disorder_rate:
                        issues.append(f"time_disorder:{time_disorder_rate:.4f}")
                    # Large gaps (> 1 hour for tick data) as fraction of intervals
                    big_gaps = diffs > pd.Timedelta(hours=1)
                    gap_count = int(big_gaps.sum())
                    gap_frac = float(big_gaps.mean()) if len(big_gaps) else 0.0
                    if gap_frac > thresholds.max_gap_fraction:
                        issues.append(f"gap_fraction:{gap_frac:.4f}>{thresholds.max_gap_fraction}")
        else:
            issues.append("no_parseable_time_column")

    passed = len(issues) == 0
    return FileQualityCheck(
        path=str(p),
        exists=exists,
        bytes=nbytes,
        rows=rows,
        missing_rate=missing_rate,
        duplicate_rate=duplicate_rate,
        time_disorder_rate=time_disorder_rate,
        gap_count=gap_count,
        passed=passed,
        issues=issues,
    )


def load_manifest_json(path: Path) -> DatasetManifest:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return DatasetManifest(**{k: raw[k] for k in raw if k in DatasetManifest.__dataclass_fields__})


def find_manifests_for_symbols(
    symbols: list[str],
    manifest_dir: Path | None = None,
) -> list[Path]:
    """Find latest manifest per symbol in data/manifests/."""
    root = manifest_dir or Path("data/manifests")
    if not root.exists():
        return []
    out: list[Path] = []
    for sym in symbols:
        s = sym.upper().replace("/", "").replace("_", "")
        if not s.endswith("USDT"):
            s = s + "USDT"
        matches = sorted(root.glob(f"binance_{s}_aggTrades_*.json"), reverse=True)
        if matches:
            out.append(matches[0])
    return out


def check_manifest(path: Path, thresholds: DataQualityThresholds) -> ManifestQualityCheck:
    issues: list[str] = []
    m = load_manifest_json(path)
    file_checks: list[FileQualityCheck] = []
    recounted = 0
    for fe in m.files:
        fp = Path(fe["path"])
        fc = inspect_csv_file(fp, thresholds)
        file_checks.append(fc)
        recounted += fc.rows
        if "sha256" in fe and fp.exists():
            expected = str(fe["sha256"])
            if len(expected) == 64 and all(c in "0123456789abcdef" for c in expected.lower()):
                actual = sha256_file(fp)
                if actual != expected:
                    issues.append(f"sha256_mismatch:{fp.name}")
        if not fc.passed:
            issues.extend([f"{fp.name}:{x}" for x in fc.issues])

    if m.rows > 0 and recounted == 0:
        issues.append(f"manifest_rows={m.rows}_but_recount=0")
    if m.rows == 0 and recounted > 0:
        issues.append(f"manifest_rows_zero_but_recount={recounted}")
    if thresholds.require_manifest_rows_match and m.rows > 0 and recounted != m.rows:
        issues.append(f"row_count_mismatch:manifest={m.rows}_files={recounted}")

    passed = len(issues) == 0 and all(fc.passed for fc in file_checks)
    return ManifestQualityCheck(
        path=str(path),
        symbol=m.symbol,
        manifest_rows=m.rows,
        recounted_rows=recounted,
        file_checks=file_checks,
        passed=passed,
        issues=issues,
    )


def generate_data_quality_report(
    manifest_paths: list[Path | str],
    thresholds: DataQualityThresholds | None = None,
    output_path: Path | str | None = None,
) -> DataQualityReport:
    th = thresholds or DataQualityThresholds()
    checks: list[ManifestQualityCheck] = []
    failures: list[str] = []
    for mp in manifest_paths:
        p = Path(mp)
        if not p.exists():
            failures.append(f"manifest_missing:{p}")
            checks.append(
                ManifestQualityCheck(
                    path=str(p),
                    symbol="?",
                    manifest_rows=0,
                    recounted_rows=0,
                    file_checks=[],
                    passed=False,
                    issues=["manifest_missing"],
                )
            )
            continue
        mc = check_manifest(p, th)
        checks.append(mc)
        if not mc.passed:
            failures.extend([f"{p.name}:{x}" for x in mc.issues])

    report = DataQualityReport(
        passed=len(failures) == 0,
        created_at=datetime.now(timezone.utc).isoformat(),
        manifest_checks=checks,
        failures=failures,
        thresholds=asdict(th),
    )
    if output_path:
        report.save(Path(output_path))
    return report


def assert_data_quality_or_raise(
    manifest_paths: list[Path | str],
    thresholds: DataQualityThresholds | None = None,
    output_path: Path | str | None = None,
) -> DataQualityReport:
    report = generate_data_quality_report(manifest_paths, thresholds, output_path)
    if not report.passed:
        msg = "DATA_QUALITY_REPORT FAILED — experiment blocked:\n" + "\n".join(report.failures[:20])
        raise DataQualityError(msg, report)
    return report


def gate_binance_symbols(
    symbols: list[str],
    output_dir: Path | str,
    thresholds: DataQualityThresholds | None = None,
    required: bool = True,
) -> DataQualityReport | None:
    """Run quality gate for Binance aggTrades manifests; write DATA_QUALITY_REPORT.json."""
    manifests = find_manifests_for_symbols(symbols)
    out = Path(output_dir) / "DATA_QUALITY_REPORT.json"
    if not manifests:
        if required:
            report = DataQualityReport(
                passed=False,
                created_at=datetime.now(timezone.utc).isoformat(),
                manifest_checks=[],
                failures=[f"no_manifests_for_symbols:{symbols}"],
                thresholds=asdict(thresholds or DataQualityThresholds()),
            )
            report.save(out)
            raise DataQualityError(
                f"No data manifests found for symbols {symbols}. Run build_manifest.py first.",
                report,
            )
        return None
    return assert_data_quality_or_raise(manifests, thresholds, out)
