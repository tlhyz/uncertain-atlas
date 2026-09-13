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


def test_research_goals_and_backlog():
    assert Path("docs/RESEARCH_GOALS.md").exists()
    assert Path("docs/RESEARCH_BACKLOG.md").exists()
    assert Path("docs/WORK_CADENCE.md").exists()
    assert Path(".cursor/rules/continuous-work-goals.mdc").exists()
    text = Path("docs/RESEARCH_BACKLOG.md").read_text()
    assert "pending" in text
    assert "P1-" in text


def test_check_backlog_script():
    import subprocess
    r = subprocess.run(["python3", "scripts/check_backlog.py", "--next", "2"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "pending" in r.stdout.lower() or "P0" in r.stdout or "P1" in r.stdout
