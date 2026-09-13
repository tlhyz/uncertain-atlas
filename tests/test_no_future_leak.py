"""No future leak tests — signals/features must not change when future bars are perturbed."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from qtb.ab.grids import rolling_atr, rolling_beta
from qtb.ab.regimes import _feat, classify
from qtb.dual.crypto_fsm import CryptoAssetFSM, CryptoBookFSM
from qtb.dual.signals import (
    check_reversal,
    compute_anchor,
    drawdown_from_anchor,
    ema,
    reversal_r1,
    reversal_r2,
    reversal_r3,
    reversal_r4,
    reversal_r5,
    rolling_high,
)
from qtb.dual.tech_fsm import TechFSM
from qtb.dual.universe import CryptoParams, TechParams
from src.features.beta import rolling_realized_beta


def _rng(seed: int = 42) -> np.random.Generator:
    return np.random.default_rng(seed)


def _ohlc(n: int = 300, seed: int = 42) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    r = _rng(seed)
    close = np.cumsum(r.normal(0, 0.5, n)) + 100.0
    high = close + r.uniform(0.1, 1.0, n)
    low = close - r.uniform(0.1, 1.0, n)
    return close, high, low


def assert_no_future_leak_scalar(fn, i: int, *args, **kwargs) -> None:
    """Result at i unchanged if all bars after i are corrupted."""
    base = fn(i, *args, **kwargs)
    mutated = []
    for a in args:
        if isinstance(a, np.ndarray):
            m = a.copy()
            m[i + 1 :] = m[i + 1] * 0.0 + 99999.0
            mutated.append(m)
        else:
            mutated.append(a)
    after = fn(i, *mutated, **kwargs)
    assert base == after, f"future leak at i={i}: {base} != {after}"


def assert_no_future_leak_array(fn, i: int, *args, atol: float = 1e-12, **kwargs) -> None:
    full = fn(*args, **kwargs)
    mutated_args = []
    for a in args:
        if isinstance(a, np.ndarray):
            m = a.copy()
            m[i + 1 :] = np.nan
            mutated_args.append(m)
        else:
            mutated_args.append(a)
    corrupt = fn(*mutated_args, **kwargs)
    assert full[i] == pytest.approx(corrupt[i], abs=atol), f"future leak at i={i}"


class TestSignalArrays:
    def test_ema_causal(self):
        close, _, _ = _ohlc(200)
        assert_no_future_leak_array(ema, 50, close, 12)

    def test_rolling_high_causal(self):
        close, _, _ = _ohlc(200)
        assert_no_future_leak_array(rolling_high, 80, close, 20)

    def test_compute_anchor_rolling_causal(self):
        close, _, _ = _ohlc(500)
        assert_no_future_leak_array(compute_anchor, 120, close, "rolling", rolling_n=48)

    def test_drawdown_from_anchor_causal(self):
        close, _, _ = _ohlc(200)
        anchor = compute_anchor(close, "rolling", rolling_n=24)

        def dd_at(i):
            return drawdown_from_anchor(close[: i + 1], anchor[: i + 1])[-1]

        i = 100
        base = dd_at(i)
        c2 = close.copy()
        c2[i + 1 :] = 1e6
        a2 = compute_anchor(c2, "rolling", rolling_n=24)
        after = drawdown_from_anchor(c2[: i + 1], a2[: i + 1])[-1]
        assert base == pytest.approx(after)


class TestRollingFeatures:
    def test_rolling_atr_causal(self):
        close, high, low = _ohlc(200)
        assert_no_future_leak_array(rolling_atr, 60, high, low, close, 24)

    def test_rolling_beta_causal(self):
        etf, _, _ = _ohlc(200, seed=1)
        und, _, _ = _ohlc(200, seed=2)
        assert_no_future_leak_array(rolling_beta, 80, etf, und, 48)

    def test_rolling_realized_beta_causal(self):
        asset, _, _ = _ohlc(300, seed=3)
        ref, _, _ = _ohlc(300, seed=4)
        assert_no_future_leak_array(rolling_realized_beta, 120, asset, ref, 48)


class TestReversalRules:
    @pytest.fixture
    def bars(self):
        return _ohlc(400, seed=7)

    def test_r1_causal(self, bars):
        close, _, _ = bars
        assert_no_future_leak_scalar(lambda i, c: reversal_r1(c, i), 100, close)

    def test_r2_causal(self, bars):
        close, high, low = bars
        assert_no_future_leak_scalar(lambda i, h, l, c: reversal_r2(h, l, c, i), 150, high, low, close)

    def test_r3_causal(self, bars):
        close, _, _ = bars
        assert_no_future_leak_scalar(lambda i, c: reversal_r3(c, i), 120, close)

    def test_r4_causal(self, bars):
        soxl, _, _ = bars
        snxx, _, _ = _ohlc(400, seed=8)
        assert_no_future_leak_scalar(lambda i, a, b: reversal_r4(a, b, i), 160, soxl, snxx)

    def test_r5_causal(self, bars):
        close, high, low = bars
        snxx, _, _ = _ohlc(400, seed=10)
        assert_no_future_leak_scalar(
            lambda i, c, h, l, s: reversal_r5(c, h, l, s, i), 160, close, high, low, snxx
        )

    @pytest.mark.parametrize("rule", ["R1", "R2", "R3", "R4", "R5"])
    def test_check_reversal_causal(self, bars, rule):
        close, high, low = bars
        snxx = _ohlc(400, seed=9)[0]
        i = 160

        def run(c, h, l, s):
            return check_reversal(rule, i, c, h, l, s)  # type: ignore[arg-type]

        base = run(close, high, low, snxx)
        c2, h2, l2, s2 = [x.copy() for x in (close, high, low, snxx)]
        for arr in (c2, h2, l2, s2):
            arr[i + 1 :] = 99999.0
        assert base == run(c2, h2, l2, s2)


class TestFSM:
    def test_crypto_classify_causal(self):
        close, high, low = _ohlc(300)
        fsm = CryptoAssetFSM("BTC", CryptoParams())
        assert_no_future_leak_scalar(
            lambda i, c, h, l: fsm.classify(i, c, h, l), 120, close, high, low
        )

    def test_crypto_book_independent_of_tech_signal(self):
        close, high, low = _ohlc(200)
        bars = {"BTC": {"close": close, "high": high, "low": low}}
        book = CryptoBookFSM(CryptoParams())
        i = 100
        a = book.on_bar(i, bars, tech_signal_dd=-0.50, unified=False)
        b = book.on_bar(i, bars, tech_signal_dd=0.0, unified=False)
        assert a["BTC"].regime == b["BTC"].regime

    def test_tech_fsm_on_bar_causal(self):
        close, high, low = _ohlc(400, seed=11)
        snxx, _, _ = _ohlc(400, seed=12)
        anchor = compute_anchor(close, "rolling", rolling_n=48)
        dd = drawdown_from_anchor(close, anchor)
        params = TechParams()
        i = 180

        def run(c, h, l, s, d):
            fsm = TechFSM(params)
            return fsm.on_bar(i, float(d[i]), c, h, l, s)

        base = run(close, high, low, snxx, dd)
        c2, h2, l2, s2 = [x.copy() for x in (close, high, low, snxx)]
        for arr in (c2, h2, l2, s2):
            arr[i + 1 :] = 1e6
        d2 = drawdown_from_anchor(c2, compute_anchor(c2, "rolling", rolling_n=48))
        after = run(c2, h2, l2, s2, d2)
        assert base.phase == after.phase
        assert base.short_notional_frac == pytest.approx(after.short_notional_frac)
        assert base.long_grid_frac == pytest.approx(after.long_grid_frac)


class TestRegimeFeatures:
    def test_feat_uses_slice_only(self):
        close, high, low = _ohlc(100)
        vol = np.ones(100)
        f1 = _feat(close[:50], high[:50], low[:50], vol[:50])
        close2 = close.copy()
        close2[50:] = 99999.0
        f2 = _feat(close2[:50], high[:50], low[:50], vol[:50])
        assert f1 == f2

    def test_classify_is_pure_function(self):
        f = {"ret": 0.25, "rv": 0.02, "eff": 0.5, "max_dd": 0.1, "mid_ret": 0.1, "second_half_ret": 0.15, "min_ret": -0.05, "max_ret": 0.3}
        assert classify(f) == classify(f.copy())


class TestDetectLeak:
    """Meta-test: corruption helper must detect intentional leak."""

    def test_detects_obvious_leak(self):
        close, _, _ = _ohlc(100)

        def leaky(i, c):
            return float(c[i + 1]) if i + 1 < len(c) else float(c[i])

        with pytest.raises(AssertionError):
            assert_no_future_leak_scalar(leaky, 50, close)
