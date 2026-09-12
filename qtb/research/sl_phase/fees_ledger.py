"""Explicit fee ledger. Rebate is never netted into a hidden maker/taker rate."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FeeLedger:
    maker_rate: float
    taker_rate: float
    rebate_rate: float
    mgmt_fee_daily: float
    gross_fee: float = 0.0
    rebate_income: float = 0.0
    etf_management_fee: float = 0.0
    maker_fill_count: int = 0
    taker_fill_count: int = 0
    turnover_usdt: float = 0.0

    def charge(self, notional: float, *, maker: bool) -> float:
        """Charge exchange fee; accrue rebate separately. Returns cash fee paid now."""
        rate = self.maker_rate if maker else self.taker_rate
        fee = abs(notional) * rate
        rebate = fee * self.rebate_rate
        self.gross_fee += fee
        self.rebate_income += rebate
        self.turnover_usdt += abs(notional)
        if maker:
            self.maker_fill_count += 1
        else:
            self.taker_fill_count += 1
        return fee

    def charge_mgmt(self, nav: float) -> float:
        fee = max(0.0, nav) * self.mgmt_fee_daily
        self.etf_management_fee += fee
        return fee

    @property
    def net_trading_fee(self) -> float:
        return self.gross_fee - self.rebate_income

    def snapshot(self) -> dict[str, float | int]:
        return {
            "gross_fee": self.gross_fee,
            "rebate_income": self.rebate_income,
            "net_trading_fee": self.net_trading_fee,
            "ETF_management_fee": self.etf_management_fee,
            "maker_fill_count": self.maker_fill_count,
            "taker_fill_count": self.taker_fill_count,
            "total_turnover_USDT": self.turnover_usdt,
            "maker_rate": self.maker_rate,
            "taker_rate": self.taker_rate,
            "rebate_rate": self.rebate_rate,
            "fee_source": 1,
        }


def assert_identity(led: FeeLedger) -> None:
    if abs(led.net_trading_fee - (led.gross_fee - led.rebate_income)) > 1e-9:
        raise AssertionError("fee identity broken")
