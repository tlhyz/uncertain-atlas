"""Compatibility shim — implementation lives in qtb.costs.fees."""

from qtb.costs.fees import *  # noqa: F403
from qtb.costs.fees import (
    VIP7_FUTURES_75,
    VIP7_FUTURES_75_EXACT,
    VIP7_SPOT_70,
    VIP7_SPOT_NO_REBATE,
    FeeConfig,
    compare_fee_drag,
    effective_fee,
    fee_on_notional,
)

__all__ = [
    "FeeConfig",
    "effective_fee",
    "fee_on_notional",
    "compare_fee_drag",
    "VIP7_SPOT_NO_REBATE",
    "VIP7_SPOT_70",
    "VIP7_FUTURES_75",
    "VIP7_FUTURES_75_EXACT",
]
