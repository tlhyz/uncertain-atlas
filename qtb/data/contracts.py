"""Gate USDT-M contract metadata (quanto, min size, maintenance)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .candles import _http_get_json, normalize_contract


@dataclass(frozen=True)
class ContractSpec:
    name: str
    quanto: float = 0.0001
    min_order_size: float = 1.0  # contracts
    min_notional: float = 1.0
    maintenance_rate: float = 0.005
    order_price_round: float = 0.1
    raw: dict[str, Any] | None = None


# Conservative fallbacks when the public contract list is unavailable.
_FALLBACKS: dict[str, ContractSpec] = {
    "BTC_USDT": ContractSpec("BTC_USDT", quanto=0.0001, maintenance_rate=0.004),
    "ETH_USDT": ContractSpec("ETH_USDT", quanto=0.01, maintenance_rate=0.005),
}


def fetch_contract_spec(contract: str, timeout: float = 20.0) -> ContractSpec:
    pair = normalize_contract(contract)
    url = f"https://api.gateio.ws/api/v4/futures/usdt/contracts/{pair}"
    try:
        raw = _http_get_json(url, {})
    except Exception:
        return _FALLBACKS.get(pair, ContractSpec(name=pair))
    if not isinstance(raw, dict):
        return _FALLBACKS.get(pair, ContractSpec(name=pair))
    quanto = float(raw.get("quanto_multiplier") or raw.get("quanto") or 0.0001)
    min_size = float(raw.get("order_size_min") or 1.0)
    maint = raw.get("maintenance_rate")
    try:
        maint_f = float(maint) if maint is not None else 0.005
    except (TypeError, ValueError):
        maint_f = 0.005
    # Gate sometimes returns maintenance_rate as percent string
    if maint_f > 1:
        maint_f = maint_f / 100.0
    return ContractSpec(
        name=pair,
        quanto=quanto if quanto > 0 else 0.0001,
        min_order_size=max(min_size, 1.0),
        maintenance_rate=maint_f if maint_f > 0 else 0.005,
        order_price_round=float(raw.get("order_price_round") or 0.1),
        raw=raw,
    )
