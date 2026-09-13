"""Tests for DATA_QUALITY_REPORT pre-experiment gate."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from src.data.manifest import DatasetManifest
from src.data.quality_gate import (
    DataQualityError,
    DataQualityThresholds,
    assert_data_quality_or_raise,
    check_manifest,
    count_csv_rows,
    gate_binance_symbols,
    generate_data_quality_report,
    inspect_csv_file,
)


def test_count_csv_rows_ts_ms(tmp_path: Path):
    p = tmp_path / "t.csv"
    pd.DataFrame({"ts_ms": [1_700_000_000_000, 1_700_000_001_000], "price": [1.0, 2.0]}).to_csv(p, index=False)
    assert count_csv_rows(p) == 2


def test_count_csv_rows_timestamp_column(tmp_path: Path):
    p = tmp_path / "t.csv"
    pd.DataFrame(
        {"timestamp": ["2024-09-01 00:00:00+00:00", "2024-09-01 00:00:01+00:00"], "price": [1.0, 2.0]}
    ).to_csv(p, index=False)
    assert count_csv_rows(p) == 2


def test_inspect_csv_passes_clean_file(tmp_path: Path):
    p = tmp_path / "clean.csv"
    ts = pd.date_range("2024-09-01", periods=100, freq="s", tz="UTC")
    pd.DataFrame({"ts_ms": (ts.view("int64") // 1_000_000), "price": 1.0, "qty": 1.0}).to_csv(p, index=False)
    fc = inspect_csv_file(p, DataQualityThresholds())
    assert fc.passed
    assert fc.rows == 100


def test_inspect_csv_fails_empty(tmp_path: Path):
    p = tmp_path / "empty.csv"
    p.write_text("ts_ms,price\n", encoding="utf-8")
    fc = inspect_csv_file(p, DataQualityThresholds(min_rows=1))
    assert not fc.passed


def test_manifest_blocks_rows_zero_with_data(tmp_path: Path):
    csv = tmp_path / "data.csv"
    pd.DataFrame({"ts_ms": [1_700_000_000_000], "price": [1.0], "qty": [1.0]}).to_csv(csv, index=False)
    manifest = DatasetManifest(
        venue="binance",
        symbol="ETHUSDT",
        market="futures_um_aggTrades",
        start="2024-09-01",
        end="2024-09-01",
        source="test",
        files=[{"path": str(csv), "sha256": "x", "bytes": csv.stat().st_size}],
        rows=0,
    )
    mpath = tmp_path / "m.json"
    manifest.save(mpath)
    mc = check_manifest(mpath, DataQualityThresholds())
    assert not mc.passed
    assert mc.recounted_rows == 1
    assert any("manifest_rows" in x or "rows_below" in x for x in mc.issues)


def test_assert_data_quality_raises_on_bad_manifest(tmp_path: Path):
    csv = tmp_path / "bad.csv"
    csv.write_text("ts_ms,price\n", encoding="utf-8")
    manifest = DatasetManifest(
        venue="binance",
        symbol="TESTUSDT",
        market="futures_um_aggTrades",
        start="2024-01-01",
        end="2024-01-01",
        source="test",
        files=[{"path": str(csv), "sha256": "x", "bytes": csv.stat().st_size}],
        rows=0,
    )
    mpath = tmp_path / "bad.json"
    manifest.save(mpath)
    with pytest.raises(DataQualityError) as exc:
        assert_data_quality_or_raise([mpath], output_path=tmp_path / "report.json")
    assert exc.value.report is not None
    assert not exc.value.report.passed


def test_generate_report_writes_json(tmp_path: Path):
    csv = tmp_path / "ok.csv"
    ts = pd.date_range("2024-09-01", periods=10, freq="s", tz="UTC")
    pd.DataFrame({"ts_ms": (ts.view("int64") // 1_000_000), "price": 1.0, "qty": 1.0}).to_csv(csv, index=False)
    manifest = DatasetManifest(
        venue="binance",
        symbol="OKUSDT",
        market="futures_um_aggTrades",
        start="2024-09-01",
        end="2024-09-01",
        source="test",
        files=[{"path": str(csv), "sha256": "x", "bytes": csv.stat().st_size}],
        rows=10,
    )
    mpath = tmp_path / "ok.json"
    manifest.save(mpath)
    out = tmp_path / "DATA_QUALITY_REPORT.json"
    report = generate_data_quality_report([mpath], output_path=out)
    assert report.passed
    assert out.exists()
    payload = json.loads(out.read_text())
    assert payload["passed"] is True


@pytest.mark.skipif(
    not Path("data/manifests/binance_SOXLUSDT_aggTrades_2026-07-09_2026-09-11.json").exists(),
    reason="SOXL manifest not present",
)
def test_soxl_manifest_passes_if_present():
    mpath = Path("data/manifests/binance_SOXLUSDT_aggTrades_2026-07-09_2026-09-11.json")
    report = generate_data_quality_report([mpath])
    assert report.passed, report.failures


def test_gate_blocks_eth_zero_rows_manifest(tmp_path: Path, monkeypatch):
    """Regression: ETH manifest rows=0 with legacy timestamp CSV must FAIL gate."""
    csv = tmp_path / "eth.csv"
    pd.DataFrame(
        {
            "timestamp": ["2024-09-01 00:00:00+00:00", "2024-09-01 00:00:01+00:00"],
            "price": [2500.0, 2501.0],
            "qty": [1.0, 2.0],
        }
    ).to_csv(csv, index=False)
    manifest = DatasetManifest(
        venue="binance",
        symbol="ETHUSDT",
        market="futures_um_aggTrades",
        start="2024-09-01",
        end="2024-09-01",
        source="test",
        files=[{"path": str(csv), "sha256": "deadbeef", "bytes": csv.stat().st_size}],
        rows=0,
    )
    mdir = tmp_path / "manifests"
    mdir.mkdir()
    mpath = mdir / "binance_ETHUSDT_aggTrades_2024-09-01_2024-09-04.json"
    manifest.save(mpath)

    import src.data.quality_gate as qg

    monkeypatch.setattr(qg, "find_manifests_for_symbols", lambda symbols, manifest_dir=None: [mpath])
    with pytest.raises(DataQualityError):
        gate_binance_symbols(["ETH"], tmp_path / "out")
