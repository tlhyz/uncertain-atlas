"""Tests for block bootstrap Monte Carlo."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.analysis.monte_carlo import block_bootstrap_mc, block_bootstrap_paths, summarize_bootstrap_paths


def test_block_bootstrap_reproducible():
    daily = np.array([0.01, -0.005, 0.002, 0.003, -0.01, 0.004])
    rng = np.random.default_rng(99)
    p1 = block_bootstrap_paths(daily, block_days=2, n_paths=50, rng=rng)
    rng = np.random.default_rng(99)
    p2 = block_bootstrap_paths(daily, block_days=2, n_paths=50, rng=rng)
    assert np.allclose(p1, p2)


def test_block_bootstrap_mc_1000_paths():
    rng = np.random.default_rng(1)
    daily_rets = rng.normal(0.001, 0.02, 60)
    equity = 10_000.0 * np.cumprod(1.0 + daily_rets)
    equity = np.r_[10_000.0, equity]
    result = block_bootstrap_mc(equity, block_days=(1, 3, 5), n_paths=1000, rng=np.random.default_rng(7))
    assert result["status"] == "OK"
    assert result["n_paths"] == 1000
    for blk in ("1d", "3d", "5d"):
        b = result["blocks"][blk]
        assert b["n_paths"] == 1000
        assert 0 <= b["prob_loss"] <= 1
        assert b["p50_final"] <= b["p75_final"]
