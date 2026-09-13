"""Crypto regime runner — config and wiring tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from qtb.dual.crypto_run import load_crypto_config, run_crypto_job


def test_load_crypto_config_defaults():
    cfg = load_crypto_config(None)
    assert cfg["experiment_id"] == "crypto_regime_v1"
    assert cfg["data"]["symbols"] == ["BTC", "ETH", "SOL"]


def test_load_crypto_config_from_file():
    cfg = load_crypto_config("configs/experiments/crypto_regime.yaml")
    assert cfg["enabled"] is True
    assert cfg["data"]["start"] == "2024-09-01"


def test_run_crypto_job_disabled_raises():
    with pytest.raises(RuntimeError, match="enabled=false"):
        run_crypto_job({"enabled": False, "smoke": False})


def test_crypto_cli_smoke(tmp_path, monkeypatch):
    """Smoke path: BTC-only, single leverage — mocked backtest."""
    captured: dict = {}

    def fake_load(*args, **kwargs):
        import numpy as np
        import pandas as pd
        from qtb.ab.data import SeriesMeta
        from qtb.dual.data import DualDataset, MarketData

        ts = pd.date_range("2024-09-01", periods=48, freq="1h", tz="UTC")
        bars = pd.DataFrame({
            "timestamp": ts,
            "open": 100.0,
            "high": 101.0,
            "low": 99.0,
            "close": 100.0,
            "volume": 1.0,
            "funding_rate": 0.0,
        })
        meta = SeriesMeta("BTC", "BTCUSDT", "1h", "test", str(ts[0]), str(ts[-1]), len(ts), 0, "")
        md = MarketData("BTC", "BTCUSDT", "1h", bars, pd.DataFrame(), meta, data_source="binance")
        empty = bars.copy()
        empty["close"] = 1.0
        tech_meta = SeriesMeta("SOXL", "cash", "1h", "test", str(ts[0]), str(ts[-1]), len(ts), 0, "")
        tech = {
            "SOXL": MarketData("SOXL", "SOXLUSDT", "1h", empty, pd.DataFrame(), tech_meta, data_source="binance"),
            "SNXX": MarketData("SNXX", "SNXXUSDT", "1h", empty.copy(), pd.DataFrame(), tech_meta, data_source="binance"),
        }
        return DualDataset(
            interval="1h",
            tech=tech,
            crypto={"BTC": md},
            aligned_index=pd.DatetimeIndex(ts),
            overlap_start=ts[0],
            overlap_end=ts[-1],
            provenance={"bars": len(ts), "source": "test"},
            seed_coverage=[],
        )

    def fake_portfolio(*args, **kwargs):
        captured["called"] = True
        import numpy as np
        from qtb.dual.portfolio import PortfolioResult
        from qtb.dual.universe import DualParams

        n = 48
        return PortfolioResult(
            name="test",
            params=DualParams(),
            timestamps=list(range(n)),
            total_equity=np.full(n, 10000.0),
            tech_equity=np.full(n, 6500.0),
            crypto_equity=np.full(n, 2500.0),
            reserve=np.full(n, 1000.0),
            trades=[],
            liquidated=False,
            liquidation_count=0,
            components={},
        )

    monkeypatch.setattr("qtb.dual.crypto_run.load_binance_crypto_dataset", fake_load)
    monkeypatch.setattr("qtb.dual.crypto_run.run_dual_portfolio", fake_portfolio)

    out = tmp_path / "crypto_smoke"
    cfg = {
        "enabled": True,
        "smoke": True,
        "experiment_id": "test_smoke",
        "data": {"start": "2024-09-01", "end": "2024-09-03", "symbols": ["BTC"]},
        "output": {"dir": str(out)},
        "run_grid_scan": False,
        "run_c1_baseline": False,
    }
    payload = run_crypto_job(cfg)
    assert captured.get("called")
    assert (out / "CRYPTO_REPORT.md").exists()
    assert (out / "crypto_results.json").exists()
    assert payload["leverage_rank"]


def test_run_crypto_grid_mix_scan(tmp_path, monkeypatch):
    calls: list[str] = []

    def fake_load(*args, **kwargs):
        import pandas as pd
        from qtb.ab.data import SeriesMeta
        from qtb.dual.data import DualDataset, MarketData

        ts = pd.date_range("2024-09-01", periods=24, freq="1h", tz="UTC")
        bars = pd.DataFrame({
            "timestamp": ts,
            "open": 100.0,
            "high": 101.0,
            "low": 99.0,
            "close": 100.0,
            "volume": 1.0,
            "funding_rate": 0.0,
        })
        meta = SeriesMeta("BTC", "BTCUSDT", "1h", "test", str(ts[0]), str(ts[-1]), len(ts), 0, "")
        md = MarketData("BTC", "BTCUSDT", "1h", bars, pd.DataFrame(), meta, data_source="binance")
        empty = bars.copy()
        tech_meta = SeriesMeta("SOXL", "cash", "1h", "test", str(ts[0]), str(ts[-1]), len(ts), 0, "")
        tech = {
            "SOXL": MarketData("SOXL", "SOXLUSDT", "1h", empty, pd.DataFrame(), tech_meta, data_source="binance"),
            "SNXX": MarketData("SNXX", "SNXXUSDT", "1h", empty.copy(), pd.DataFrame(), tech_meta, data_source="binance"),
        }
        return DualDataset(
            interval="1h",
            tech=tech,
            crypto={"BTC": md},
            aligned_index=pd.DatetimeIndex(ts),
            overlap_start=ts[0],
            overlap_end=ts[-1],
            provenance={"bars": len(ts), "source": "test"},
            seed_coverage=[],
        )

    def fake_portfolio(data, dp, **kwargs):
        calls.append(dp.crypto.grid_mix)
        import numpy as np
        from qtb.dual.portfolio import PortfolioResult

        n = 24
        return PortfolioResult(
            name=kwargs.get("name", "test"),
            params=dp,
            timestamps=list(range(n)),
            total_equity=np.full(n, 10000.0),
            tech_equity=np.full(n, 6500.0),
            crypto_equity=np.full(n, 2500.0),
            reserve=np.full(n, 1000.0),
            trades=[],
            liquidated=False,
            liquidation_count=0,
            components={},
        )

    monkeypatch.setattr("qtb.dual.crypto_run.load_binance_crypto_dataset", fake_load)
    monkeypatch.setattr("qtb.dual.crypto_run.run_dual_portfolio", fake_portfolio)

    out = tmp_path / "grid_mix"
    cfg = {
        "enabled": True,
        "experiment_id": "test_grid_mix",
        "data": {"start": "2024-09-01", "end": "2024-09-02", "symbols": ["BTC"]},
        "output": {"dir": str(out)},
        "run_leverage_scan": False,
        "run_grid_scan": False,
        "run_grid_mix_scan": True,
        "grid_mix_scan": ["80_20", "20_80"],
        "run_c1_baseline": False,
    }
    payload = run_crypto_job(cfg)
    assert calls == ["80_20", "20_80"]
    assert len(payload["grid_mix_rank"]) == 2
    report = (out / "CRYPTO_REPORT.md").read_text(encoding="utf-8")
    assert "Grid→Trend mix rank" in report
