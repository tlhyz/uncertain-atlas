"""
Live module — intentionally a stub.

Safety rules (hard):
1. Default DRY_RUN=True always.
2. Real-order attempt requires BOTH:
     - env ALLOW_LIVE=1
     - config live.dry_run == false
3. Even then, there is no Gate private-order implementation. We refuse.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

ALLOW_LIVE_ENV = "ALLOW_LIVE"


class DryRunViolation(RuntimeError):
    """Raised when a live send is blocked by the dry-run guard."""


class LiveStubError(RuntimeError):
    """Raised when someone unlocks the guard — live path still does not exist."""


def is_dry_run_forced(config: dict[str, Any] | None = None) -> bool:
    """True unless ALLOW_LIVE=1 AND config.live.dry_run is explicitly False."""
    cfg = config or {}
    live = cfg.get("live") or {}
    dry = live.get("dry_run", True)
    if dry is not False:
        return True
    if os.environ.get(ALLOW_LIVE_ENV) != "1":
        return True
    return False


def assert_live_allowed(config: dict[str, Any] | None = None) -> None:
    """
    Gate for any function that would place an order.
    Default: refuse (dry-run).
    If unlocked: still refuse because live is a stub.
    """
    if is_dry_run_forced(config):
        raise DryRunViolation(
            "Live orders blocked: DRY_RUN is forced. "
            "To even request live you need ALLOW_LIVE=1 and live.dry_run=false. "
            "Live remains a stub with no private API."
        )
    raise LiveStubError(
        "ALLOW_LIVE=1 and dry_run=false acknowledged, but live trading is a stub: "
        "no order-placement code exists. Refusing to send orders."
    )


@dataclass
class LiveBroker:
    """Paper/dry-run broker. send_order never hits the network."""

    config: dict[str, Any] = field(default_factory=dict)
    dry_run: bool = True
    log: list[dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        # Hard-force dry_run unless the dangerous override is complete.
        self.dry_run = is_dry_run_forced(self.config)

    def send_order(self, order: dict[str, Any]) -> dict[str, Any]:
        if self.dry_run or is_dry_run_forced(self.config):
            rec = {"status": "dry_run", "order": dict(order), "filled": False}
            self.log.append(rec)
            return rec
        assert_live_allowed(self.config)
        raise LiveStubError("unreachable")  # pragma: no cover
