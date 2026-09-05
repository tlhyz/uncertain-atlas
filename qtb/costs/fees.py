"""Fee and rebate math for Gate.io VIP levels (spot + USDT-M futures)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeeConfig:
    """Exchange fee configuration with optional rebate."""

    maker_rate: float = 0.00008  # VIP7 USDT-M maker 0.008%
    taker_rate: float = 0.0002  # VIP7 USDT-M taker 0.02%
    rebate_rate: float = 0.75  # futures rebate 75%
    label: str = "VIP7 futures + 75% rebate"
    vip_tier: int = 7
    market: str = "futures"

    @property
    def effective_maker(self) -> float:
        return effective_fee(self.maker_rate, self.rebate_rate)

    @property
    def effective_taker(self) -> float:
        return effective_fee(self.taker_rate, self.rebate_rate)

    def with_rebate(self, rebate_rate: float, label: str | None = None) -> FeeConfig:
        return FeeConfig(
            maker_rate=self.maker_rate,
            taker_rate=self.taker_rate,
            rebate_rate=rebate_rate,
            label=label or f"rebate={rebate_rate:.0%}",
            vip_tier=self.vip_tier,
            market=self.market,
        )


def effective_fee(base_fee: float, rebate_rate: float) -> float:
    """effective_fee = base_fee * (1 - rebate_rate)."""
    if not 0.0 <= rebate_rate <= 1.0:
        raise ValueError(f"rebate_rate must be in [0, 1], got {rebate_rate}")
    if base_fee < 0:
        raise ValueError(f"base_fee must be >= 0, got {base_fee}")
    return base_fee * (1.0 - rebate_rate)


VIP7_SPOT_NO_REBATE = FeeConfig(
    maker_rate=0.0008,
    taker_rate=0.00085,
    rebate_rate=0.0,
    label="VIP7 no rebate",
    vip_tier=7,
    market="spot",
)

VIP7_SPOT_70 = FeeConfig(
    maker_rate=0.0008,
    taker_rate=0.00085,
    rebate_rate=0.70,
    label="VIP7 + 70% spot rebate",
    vip_tier=7,
    market="spot",
)

VIP7_FUTURES_75 = FeeConfig(
    maker_rate=0.00008,
    taker_rate=0.0002,
    rebate_rate=0.75,
    label="VIP7 futures + 75% rebate (eff ~0.002%/0.005%)",
    vip_tier=7,
    market="futures",
)

VIP7_FUTURES_75_EXACT = VIP7_FUTURES_75


def fee_on_notional(notional: float, fee_rate: float) -> float:
    """Absolute fee charged on a trade notional."""
    return abs(notional) * fee_rate


def compare_fee_drag(
    notional: float,
    base_fee: float,
    rebate_rate: float,
) -> dict[str, float]:
    """Compare fee paid with vs without rebate on a given notional."""
    no_rebate = fee_on_notional(notional, base_fee)
    with_rebate = fee_on_notional(notional, effective_fee(base_fee, rebate_rate))
    return {
        "notional": notional,
        "fee_no_rebate": no_rebate,
        "fee_with_rebate": with_rebate,
        "fee_saved": no_rebate - with_rebate,
        "effective_rate": effective_fee(base_fee, rebate_rate),
        "base_rate": base_fee,
    }


# Approximate Gate USDT-M VIP maker/taker (public schedule; rebate applied separately).
_FUTURES_VIP_TABLE: dict[int, tuple[float, float]] = {
    0: (0.0002, 0.0005),
    1: (0.00018, 0.00045),
    2: (0.00016, 0.0004),
    3: (0.00014, 0.00035),
    4: (0.00012, 0.0003),
    5: (0.0001, 0.00025),
    6: (0.00009, 0.00022),
    7: (0.00008, 0.0002),
}

_SPOT_VIP_TABLE: dict[int, tuple[float, float]] = {
    0: (0.002, 0.002),
    7: (0.0008, 0.00085),
}


def fee_preset(
    market: str = "futures",
    vip_tier: int = 7,
    rebate_rate: float | None = None,
) -> FeeConfig:
    """Build a FeeConfig from VIP tier + market. Defaults match the user's VIP7 + rebate."""
    market = market.lower()
    if market == "futures":
        maker, taker = _FUTURES_VIP_TABLE.get(int(vip_tier), _FUTURES_VIP_TABLE[7])
        rebate = 0.75 if rebate_rate is None else float(rebate_rate)
        return FeeConfig(
            maker_rate=maker,
            taker_rate=taker,
            rebate_rate=rebate,
            label=f"VIP{vip_tier} futures + {rebate:.0%} rebate",
            vip_tier=int(vip_tier),
            market="futures",
        )
    maker, taker = _SPOT_VIP_TABLE.get(int(vip_tier), _SPOT_VIP_TABLE[7])
    rebate = 0.70 if rebate_rate is None else float(rebate_rate)
    return FeeConfig(
        maker_rate=maker,
        taker_rate=taker,
        rebate_rate=rebate,
        label=f"VIP{vip_tier} spot + {rebate:.0%} rebate",
        vip_tier=int(vip_tier),
        market="spot",
    )
