"""Atlas tooling: corpus runner + review audit (no network, no qtb)."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "uncertain-atlas"

# P1-4: at least 10 Cxx rows have a parseable placeholder hook.
CXX_HOOKS = (650, 651, 652, 653, 655, 656, 657, 658, 659, 660)


def _load(name: str, rel: str):
    path = ATLAS / rel
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _corpus_by_cid() -> dict[int, object]:
    runner = _load("adversarial_runner", "tools/adversarial_runner.py")
    entries = runner.parse_corpus(
        (ATLAS / "libraries/adversarial-corpus/README.md").read_text(encoding="utf-8")
    )
    return {e.cid: e for e in entries}


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


@pytest.mark.parametrize("cid", CXX_HOOKS)
def test_corpus_cxx_placeholder(cid):
    """P1-4: Cxx row parses and names an invariant (placeholder, no network)."""
    by_cid = _corpus_by_cid()
    assert cid in by_cid, f"missing C{cid}"
    entry = by_cid[cid]
    assert entry.invariant > 0
    assert entry.slug
    assert len(entry.body) >= 20


def test_invariant_corpus_links_gate():
    p = subprocess.run(
        [sys.executable, str(ATLAS / "tools" / "invariant_corpus_links.py")],
        cwd=ATLAS,
        capture_output=True,
        text=True,
    )
    assert p.returncode == 0, p.stdout + p.stderr
    assert "OK:" in p.stdout
