"""Full cost model: fees, rebate, slippage, funding, quanto / min size."""

from __future__ import annotations

from dataclasses import dataclass, field

from .fees import FeeConfig, VIP7_FUTURES_75, fee_on_notional


def apply_slippage(price: float, side: str, slippage_bps: float) -> float:
    """Shift fill price against the taker. side is 'buy' or 'sell'."""
    if price <= 0:
        raise ValueError(f"price must be > 0, got {price}")
    slip = abs(slippage_bps) / 10_000.0
    if side == "buy":
        return price * (1.0 + slip)
    if side == "sell":
        return price * (1.0 - slip)
    raise ValueError(f"side must be buy|sell, got {side!r}")


def funding_pnl(signed_qty: float, mark_price: float, funding_rate: float) -> float:
    """
    USDT-M funding: longs pay shorts when rate > 0.
    signed_qty > 0 is long. PnL to the position holder = -signed_qty * mark * rate.
    """
    return -signed_qty * mark_price * funding_rate


def round_to_quanto(qty: float, quanto: float) -> float:
    """Round contract quantity down to the nearest quanto multiple (never oversize)."""
    if quanto <= 0:
        return qty
    n = int(abs(qty) / quanto)
    out = n * quanto
    return out if qty >= 0 else -out


@dataclass
class CostModel:
    """Applies exchange + execution costs to intended fills."""

    fee_config: FeeConfig = field(default_factory=lambda: VIP7_FUTURES_75)
    slippage_bps: float = 1.0
    use_maker: bool = False
    quanto: float = 0.0001  # Gate BTC_USDT quanto_multiplier (1 contract ≈ 0.0001 BTC)
    min_order_size: float = 1.0  # contracts (Gate size is integer contracts)
    min_notional: float = 1.0  # USDT
    apply_funding: bool = True

    def fee_rate(self, is_maker: bool | None = None) -> float:
        maker = self.use_maker if is_maker is None else is_maker
        return self.fee_config.effective_maker if maker else self.fee_config.effective_taker

    def fee(self, notional: float, is_maker: bool | None = None) -> float:
        return fee_on_notional(notional, self.fee_rate(is_maker))

    def fill_price(self, raw_price: float, side: str, is_maker: bool | None = None) -> float:
        maker = self.use_maker if is_maker is None else is_maker
        if maker:
            return raw_price  # assume limit rests and fills at the grid/trigger
        return apply_slippage(raw_price, side, self.slippage_bps)

    def size_from_notional(self, notional: float, price: float) -> float:
        """Convert USDT notional to quanto-rounded base quantity."""
        if price <= 0 or notional <= 0:
            return 0.0
        raw_qty = notional / price
        if self.quanto > 0:
            raw_qty = round_to_quanto(raw_qty, self.quanto)
        return raw_qty

    def accept_order(self, qty: float, price: float) -> bool:
        if qty <= 0 or price <= 0:
            return False
        contracts = qty / self.quanto if self.quanto > 0 else qty
        if contracts + 1e-12 < self.min_order_size:
            return False
        if qty * price + 1e-12 < self.min_notional:
            return False
        return True

    def funding(self, signed_qty: float, mark_price: float, rate: float) -> float:
        if not self.apply_funding or abs(rate) < 1e-16 or signed_qty == 0:
            return 0.0
        return funding_pnl(signed_qty, mark_price, rate)
