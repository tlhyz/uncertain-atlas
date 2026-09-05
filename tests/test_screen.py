"""Unit tests for screener score / trend helpers (no network)."""

from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from qtb.config import load_config
from qtb.screen import (
    close_returns,
    is_usdt_perp,
    metrics_from_ohlcv,
    parse_ticker_row,
    path_amp,
    path_efficiency,
    path_vol,
    prefilter_tickers,
    screen_score,
)


def test_path_efficiency_one_sided_is_one():
    rets = [0.01] * 20
    assert path_efficiency(rets) == pytest.approx(1.0)


def test_path_efficiency_roundtrip_chop_is_zero():
    rets = [0.02, -0.02] * 16
    assert path_efficiency(rets) == pytest.approx(0.0)


def test_path_efficiency_empty_and_flat():
    assert path_efficiency([]) == 0.0
    assert path_efficiency([0.0, 0.0, 0.0]) == 0.0


def test_close_returns_and_pstdev():
    closes = [100.0, 110.0, 99.0]
    rets = close_returns(closes)
    assert rets[0] == pytest.approx(0.10)
    assert rets[1] == pytest.approx((99.0 - 110.0) / 110.0)
    # two returns → pstdev is defined
    assert path_vol(rets) > 0
    assert path_vol([0.01]) == 0.0


def test_path_amp_mean_hl_over_close():
    highs = [102.0, 110.0]
    lows = [98.0, 100.0]
    closes = [100.0, 105.0]
    expected = ((4.0 / 100.0) + (10.0 / 105.0)) / 2.0
    assert path_amp(highs, lows, closes) == pytest.approx(expected)


def test_screen_score_formula():
    vol, amp, trend = 0.02, 0.01, 0.15
    assert screen_score(vol, amp, trend) == pytest.approx(vol * amp / (trend + 0.05))


def test_score_prefers_choppy_mid_high_vol_over_trender():
    """BULLA/AKE-like one-way trend should score below 牛来/HYPE-like chop."""
    n = 48
    # One-sided trender: small bars, large net drift
    trend_rets = [0.015] * n
    trend_vol = path_vol(trend_rets)
    trend_amp = 0.008
    trend_er = path_efficiency(trend_rets)
    # Choppy mid-high vol: same amp/vol-ish, low path efficiency
    chop_rets = [0.02, -0.018, 0.016, -0.019] * (n // 4)
    chop_vol = path_vol(chop_rets)
    chop_amp = 0.018
    chop_er = path_efficiency(chop_rets)
    assert trend_er > 0.9
    assert chop_er < 0.2
    assert screen_score(chop_vol, chop_amp, chop_er) > screen_score(trend_vol, trend_amp, trend_er)


def test_score_penalizes_pure_sideways_jitter():
    """BTW/TUT-like tiny jitter: low vol*amp even if trend≈0."""
    jitter = [0.0004, -0.00035] * 40
    chop = [0.012, -0.011, 0.010, -0.009] * 20
    jitter_score = screen_score(path_vol(jitter), 0.0012, path_efficiency(jitter))
    chop_score = screen_score(path_vol(chop), 0.016, path_efficiency(chop))
    assert chop_score > jitter_score


def test_metrics_from_ohlcv_synthetic_series():
    # Deterministic up-then-down path (low efficiency, non-zero vol/amp)
    n = 30
    closes = []
    px = 100.0
    for i in range(n):
        px *= 1.01 if i < n // 2 else 0.99
        closes.append(px)
    highs = [c * 1.008 for c in closes]
    lows = [c * 0.992 for c in closes]
    df = pd.DataFrame({"open": closes, "high": highs, "low": lows, "close": closes})
    m = metrics_from_ohlcv(df)
    assert m["bars"] == n
    assert m["vol"] > 0
    assert m["amp"] == pytest.approx(0.016, rel=1e-3)
    assert 0.0 <= m["trend"] < 0.35
    assert m["score"] == pytest.approx(screen_score(m["vol"], m["amp"], m["trend"]))
    assert math.isfinite(m["score"])


def test_is_usdt_perp_filters_dated_delivery():
    assert is_usdt_perp("BTC_USDT")
    assert is_usdt_perp("牛来_USDT")
    assert is_usdt_perp("HYPE_USDT")
    assert not is_usdt_perp("BTC_USDT_20260327")
    assert not is_usdt_perp("BTCUSDT")
    assert not is_usdt_perp("ETH_USD")


def test_prefilter_tickers_volume_range_then_top_n_by_range():
    tickers = [
        {
            "contract": "THIN_USDT",
            "last": "1",
            "high_24h": "1.3",
            "low_24h": "0.9",
            "volume_24h_quote": "1000",
        },
        {
            "contract": "TREND_USDT",
            "last": "10",
            "high_24h": "13",
            "low_24h": "9",
            "volume_24h_quote": "8000000",
        },
        {
            "contract": "CHOP_USDT",
            "last": "5",
            "high_24h": "5.8",
            "low_24h": "4.4",
            "volume_24h_quote": "12000000",
        },
        {
            "contract": "TIGHT_USDT",
            "last": "2",
            "high_24h": "2.1",
            "low_24h": "1.95",
            "volume_24h_quote": "9000000",
        },
        {
            "contract": "BTC_USDT_20260327",
            "last": "1",
            "high_24h": "2",
            "low_24h": "0.5",
            "volume_24h_quote": "99999999",
        },
    ]
    rows = prefilter_tickers(tickers, min_volume=5_000_000, min_range=0.12, prefilter=1)
    assert [r["symbol"] for r in rows] == ["TREND_USDT"]
    assert parse_ticker_row(tickers[1])["range_24h"] == pytest.approx(0.4)
    both = prefilter_tickers(tickers, min_volume=5_000_000, min_range=0.12, prefilter=10)
    assert [r["symbol"] for r in both] == ["TREND_USDT", "CHOP_USDT"]


def test_load_sl50_yaml_config():
    cfg = load_config(ROOT / "configs" / "optimize_niulai_aggressive_sl50.yaml")
    assert cfg["risk"]["investment_sl_pct"] == pytest.approx(0.5)
    assert cfg["strategy"]["long_capital"] == pytest.approx(950.0)
    assert cfg["strategy"]["short_capital"] == pytest.approx(1380.0)
    assert cfg["optimize"]["grid"] == "compact"
    assert cfg["interval"] == "5m"
    assert cfg["symbol"] == "牛来_USDT"


def test_screen_cli_flags_parse():
    from qtb.cli import build_parser

    p = build_parser()
    args = p.parse_args(
        [
            "screen",
            "--min-volume",
            "1000000",
            "--min-range",
            "0.08",
            "--max-trend",
            "0.3",
            "--top",
            "5",
            "--prefilter",
            "12",
            "--interval",
            "1h",
            "--days",
            "7",
            "--cache-only",
            "--out",
            "outputs/demo_screen",
            "--batch-backtest",
            "--picks",
            "2",
            "--batch-mode",
            "optimize",
        ]
    )
    assert args.cmd == "screen"
    assert args.min_volume == 1_000_000
    assert args.min_range == pytest.approx(0.08)
    assert args.max_trend == pytest.approx(0.3)
    assert args.top == 5
    assert args.prefilter == 12
    assert args.interval == "1h"
    assert args.days == 7
    assert args.cache_only is True
    assert args.batch_backtest is True
    assert args.picks == 2
    assert args.batch_mode == "optimize"

    b = p.parse_args(["batch-screen", "--picks", "4"])
    assert b.cmd == "batch-screen"
    assert b.batch_backtest is True
    assert b.picks == 4


def test_qtb_cli_screen_help_subprocess():
    r = subprocess.run(
        [sys.executable, "-m", "qtb.cli", "screen", "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stderr
    assert "--min-volume" in r.stdout
    assert "--min-range" in r.stdout
    assert "--max-trend" in r.stdout
    assert "--prefilter" in r.stdout
    assert "--batch-backtest" in r.stdout
    assert "--cache-only" in r.stdout
