"""Fee and rebate math for Gate.io VIP levels."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeeConfig:
    """Spot fee configuration with optional rebate."""

    maker_rate: float = 0.0008  # VIP7 spot maker 0.08%
    taker_rate: float = 0.00085  # VIP7 spot taker 0.085%
    rebate_rate: float = 0.70  # spot rebate 70%
    label: str = "VIP7+70% spot rebate"

    @property
    def effective_maker(self) -> float:
        return effective_fee(self.maker_rate, self.rebate_rate)

    @property
    def effective_taker(self) -> float:
        return effective_fee(self.taker_rate, self.rebate_rate)

    def with_rebate(self, rebate_rate: float, label: str | None = None) -> "FeeConfig":
        return FeeConfig(
            maker_rate=self.maker_rate,
            taker_rate=self.taker_rate,
            rebate_rate=rebate_rate,
            label=label or f"rebate={rebate_rate:.0%}",
        )


def effective_fee(base_fee: float, rebate_rate: float) -> float:
    """effective_fee = base_fee * (1 - rebate_rate)."""
    if not 0.0 <= rebate_rate <= 1.0:
        raise ValueError(f"rebate_rate must be in [0, 1], got {rebate_rate}")
    if base_fee < 0:
        raise ValueError(f"base_fee must be >= 0, got {base_fee}")
    return base_fee * (1.0 - rebate_rate)


# Presets
VIP7_SPOT_NO_REBATE = FeeConfig(
    maker_rate=0.0008,
    taker_rate=0.00085,
    rebate_rate=0.0,
    label="VIP7 no rebate",
)

VIP7_SPOT_70 = FeeConfig(
    maker_rate=0.0008,
    taker_rate=0.00085,
    rebate_rate=0.70,
    label="VIP7 + 70% spot rebate",
)

VIP7_FUTURES_75 = FeeConfig(
    maker_rate=0.00008,  # VIP7 futures maker 0.008%
    taker_rate=0.0002,   # VIP7 futures taker 0.02%
    rebate_rate=0.75,    # futures rebate 75%
    label="VIP7 futures + 75% rebate (eff ~0.002%/0.005%)",
)


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

VIP7_FUTURES_75_EXACT = VIP7_FUTURES_75  # alias
