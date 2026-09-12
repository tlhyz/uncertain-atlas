"""Crypto book independent regime classifier — never reads SOXL/SNXX."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .signals import grid_mix_fractions
from .universe import CRYPTO_GRID_MIXES, CryptoParams, CryptoRegime


@dataclass
class CryptoExposure:
    long_grid_frac: float = 0.0
    long_dir_frac: float = 0.0
    short_grid_frac: float = 0.0
    cash_frac: float = 1.0
    regime: CryptoRegime = "RANGE_LOW_VOL"
    utilization: float = 0.0


@dataclass
class CryptoAssetFSM:
    symbol: str
    params: CryptoParams
    regime: CryptoRegime = "RANGE_LOW_VOL"
    trend_bars: int = 0

    def classify(self, i: int, close: np.ndarray, high: np.ndarray, low: np.ndarray) -> CryptoRegime:
        if i < 48:
            return "RANGE_LOW_VOL"
        w = close[max(0, i - 24 * 7) : i + 1]
        ret = float(w[-1] / w[0] - 1.0) if len(w) > 1 else 0.0
        r = np.diff(w) / np.maximum(w[:-1], 1e-12)
        rv = float(np.std(r)) if len(r) > 2 else 0.0
        peak = np.maximum.accumulate(w)
        dd = float(((peak - w) / np.maximum(peak, 1e-12)).max())

        if ret >= 0.12 and rv >= 0.015:
            self.regime = "BULL"
        elif ret <= -0.12 and dd >= 0.15:
            self.regime = "BEAR"
        elif rv >= 0.012:
            self.regime = "RANGE_HIGH_VOL"
        else:
            self.regime = "RANGE_LOW_VOL"
        return self.regime

    def exposure(self, regime: CryptoRegime) -> CryptoExposure:
        lev = self.params.leverage
        mix_key = self.params.grid_mix
        if mix_key == "dynamic":
            phase = {"BULL": "strong", "RANGE_HIGH_VOL": "base", "RANGE_LOW_VOL": "base", "BEAR": "base"}.get(
                regime, "base"
            )
            g, d = grid_mix_fractions("dynamic", phase)  # type: ignore[arg-type]
        elif mix_key in CRYPTO_GRID_MIXES:
            g, d = CRYPTO_GRID_MIXES[mix_key]
        else:
            g, d = 0.50, 0.50

        if regime == "BULL":
            util = 0.65
            lg, ld = g * util * lev, d * util * lev
            return CryptoExposure(
                long_grid_frac=lg,
                long_dir_frac=ld,
                cash_frac=max(0.05, 1.0 - util),
                regime=regime,
                utilization=util,
            )
        if regime == "RANGE_HIGH_VOL":
            util = 0.45
            return CryptoExposure(
                long_grid_frac=g * util * lev,
                long_dir_frac=d * util * 0.3 * lev,
                cash_frac=1.0 - util * 0.5,
                regime=regime,
                utilization=util * 0.5,
            )
        if regime == "RANGE_LOW_VOL":
            util = 0.20
            return CryptoExposure(
                long_grid_frac=g * util * lev * 0.5,
                cash_frac=1.0 - util * 0.3,
                regime=regime,
                utilization=util * 0.3,
            )
        # BEAR
        return CryptoExposure(
            short_grid_frac=0.08 * lev,
            cash_frac=0.85,
            regime=regime,
            utilization=0.10,
        )


@dataclass
class CryptoBookFSM:
    params: CryptoParams
    assets: dict[str, CryptoAssetFSM] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.assets:
            for sym in ("BTC", "ETH", "SOL"):
                self.assets[sym] = CryptoAssetFSM(sym, self.params)

    def on_bar(
        self,
        i: int,
        bars: dict[str, dict[str, np.ndarray]],
        tech_signal_dd: float | None = None,
        unified: bool = False,
    ) -> dict[str, CryptoExposure]:
        out: dict[str, CryptoExposure] = {}
        for sym, fsm in self.assets.items():
            b = bars.get(sym)
            if b is None:
                continue
            regime = fsm.classify(i, b["close"], b["high"], b["low"])
            if unified and tech_signal_dd is not None and tech_signal_dd < -0.10:
                # B9 benchmark: force bear when tech is in drawdown
                regime = "BEAR" if regime != "BULL" else "RANGE_LOW_VOL"
            out[sym] = fsm.exposure(regime)
        return out
