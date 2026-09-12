"""A/B pair universe. Do not invent a perpetual if Gate does not list one."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ABPair:
    name: str
    etf_spot: str
    perp: str | None
    underlying_spot: str
    etf_short: str | None = None
    priority: int = 10
    meme: bool = False
    notes: tuple[str, ...] = ()

    @property
    def has_perp(self) -> bool:
        return bool(self.perp)

    @property
    def no_direct_perp(self) -> bool:
        return self.perp is None


# Priority: majors first, then memes, then equity-linked tokens.
# SOXL/SNXX/AAOI *do* have Gate USDT-M perps (verified via public API).
# They are compared only on overlapping real history — never on fabricated perps.
PAIRS: tuple[ABPair, ...] = (
    ABPair("BTC", "BTC3L_USDT", "BTC_USDT", "BTC_USDT", "BTC3S_USDT", priority=1),
    ABPair("ETH", "ETH3L_USDT", "ETH_USDT", "ETH_USDT", "ETH3S_USDT", priority=2),
    ABPair("SOL", "SOL3L_USDT", "SOL_USDT", "SOL_USDT", "SOL3S_USDT", priority=3),
    ABPair("PENGU", "PENGU3L_USDT", "PENGU_USDT", "PENGU_USDT", "PENGU3S_USDT", priority=4, meme=True),
    ABPair("PUMP", "PUMP3L_USDT", "PUMP_USDT", "PUMP_USDT", "PUMP3S_USDT", priority=5, meme=True),
    ABPair("SOXL", "SOXL3L_USDT", "SOXL_USDT", "SOXL_USDT", "SOXL3S_USDT", priority=6),
    ABPair("SNXX", "SNXX3L_USDT", "SNXX_USDT", "SNXX_USDT", "SNXX3S_USDT", priority=7),
    ABPair("AAOI", "AAOI3L_USDT", "AAOI_USDT", "AAOI_USDT", "AAOI3S_USDT", priority=8),
)

PAIR_BY_NAME = {p.name: p for p in PAIRS}


def long_pairs(names: list[str] | None = None) -> list[ABPair]:
    if not names:
        return list(PAIRS)
    out = []
    for n in names:
        key = n.strip().upper()
        if key not in PAIR_BY_NAME:
            raise KeyError(f"unknown pair {n!r}; known={sorted(PAIR_BY_NAME)}")
        out.append(PAIR_BY_NAME[key])
    return out


def portfolio_core() -> list[ABPair]:
    """User-specified portfolio core + small meme sleeves."""
    return [PAIR_BY_NAME[n] for n in ("SOL", "ETH", "SOXL", "PENGU", "PUMP")]
