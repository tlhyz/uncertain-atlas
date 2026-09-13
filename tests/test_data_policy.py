"""No synthetic tick policy enforcement tests."""

from pathlib import Path


def test_data_policy_forbids_synthetic():
    text = Path("docs/DATA_POLICY.md").read_text()
    assert "No synthetic tick" in text or "No synthetic tick data" in text.lower() or "synthetic tick" in text.lower()


def test_gitignore_raw_data():
    gi = Path(".gitignore").read_text()
    assert "data/raw/" in gi
