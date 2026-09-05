"""Live module must hard-force DRY_RUN."""

from __future__ import annotations

import pytest

from qtb.live.broker import (
    DryRunViolation,
    LiveBroker,
    LiveStubError,
    assert_live_allowed,
    is_dry_run_forced,
)


def test_default_dry_run_forced(monkeypatch):
    monkeypatch.delenv("ALLOW_LIVE", raising=False)
    cfg = {"live": {"dry_run": True}}
    assert is_dry_run_forced(cfg) is True
    assert is_dry_run_forced({}) is True
    broker = LiveBroker(config=cfg)
    assert broker.dry_run is True
    rec = broker.send_order({"side": "buy", "size": 1})
    assert rec["status"] == "dry_run"
    assert rec["filled"] is False


def test_dry_run_false_without_env_still_forced(monkeypatch):
    monkeypatch.delenv("ALLOW_LIVE", raising=False)
    cfg = {"live": {"dry_run": False}}
    assert is_dry_run_forced(cfg) is True
    with pytest.raises(DryRunViolation):
        assert_live_allowed(cfg)
    broker = LiveBroker(config=cfg)
    rec = broker.send_order({"side": "sell"})
    assert rec["status"] == "dry_run"


def test_allow_live_with_dry_run_true_still_forced(monkeypatch):
    monkeypatch.setenv("ALLOW_LIVE", "1")
    cfg = {"live": {"dry_run": True}}
    assert is_dry_run_forced(cfg) is True
    with pytest.raises(DryRunViolation):
        assert_live_allowed(cfg)


def test_dangerous_override_still_stub(monkeypatch):
    monkeypatch.setenv("ALLOW_LIVE", "1")
    cfg = {"live": {"dry_run": False}}
    assert is_dry_run_forced(cfg) is False
    with pytest.raises(LiveStubError):
        assert_live_allowed(cfg)
    # Broker still refuses to mark dry_run False path as a live fill
    broker = LiveBroker(config=cfg)
    assert broker.dry_run is False
    with pytest.raises(LiveStubError):
        broker.send_order({"side": "buy"})
