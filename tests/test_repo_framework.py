"""Test src package imports and config load."""

from pathlib import Path

import yaml


def test_configs_load():
    for name in ("portfolio.yaml", "fees.yaml", "risk.yaml", "universe.yaml"):
        p = Path("configs") / name
        assert p.exists()
        yaml.safe_load(p.read_text())


def test_src_binance_public_import():
    from src.data import binance_public
    assert "BTCUSDT" in binance_public.SYMBOLS_CRYPTO


def test_research_history_exists():
    assert Path("docs/RESEARCH_HISTORY.md").exists()
    text = Path("docs/RESEARCH_HISTORY.md").read_text()
    assert "FAILED" in text
    assert "ETF" in text


def test_review_log_policy_exists():
    assert Path("docs/REVIEW_AND_OPTIMIZATION.md").exists()
    assert Path("outputs/review_logs/TEMPLATE.md").exists()
    assert Path("outputs/review_logs/INDEX.md").exists()
    assert Path(".cursor/rules/review-optimize-log.mdc").exists()
