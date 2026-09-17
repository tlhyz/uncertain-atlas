"""Atlas tooling: corpus runner + review audit (no network, no qtb)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "uncertain-atlas"


def test_adversarial_runner_validate():
    p = subprocess.run(
        [sys.executable, str(ATLAS / "tools" / "adversarial_runner.py"), "validate"],
        cwd=ATLAS,
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr
    assert "OK:" in p.stdout


def test_review_audit_writes_report():
    p = subprocess.run(
        [sys.executable, str(ATLAS / "tools" / "review_audit.py")],
        cwd=ATLAS,
        capture_output=True,
        text=True,
    )
    report = ATLAS / "REVIEW_REPORT.md"
    assert report.is_file()
    text = report.read_text(encoding="utf-8")
    assert "Review Report" in text
    assert p.returncode in (0, 1)
    # v1 pages exist → R5 should pass; high_fail should be 0 after Phase 1
    assert "high_fail=0" in text or p.returncode == 0


def test_atlas_index_writes_json(tmp_path):
    out = tmp_path / "atlas_index.json"
    p = subprocess.run(
        [sys.executable, str(ATLAS / "tools" / "atlas_index.py"), "--out", str(out), "--stats"],
        cwd=ATLAS,
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr
    assert out.is_file()
    data = out.read_text(encoding="utf-8")
    assert '"count"' in data
    assert "GOAL.md" in data
