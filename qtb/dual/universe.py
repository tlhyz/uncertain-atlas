"""Capital pools, symbols, seed windows, parameter grids."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

TOTAL_CAPITAL = 10_000.0
TECH_BOOK = 6_500.0
CRYPTO_BOOK = 2_500.0
GLOBAL_RESERVE = 1_000.0

TECH_SYMBOLS = ("SOXL", "SNXX")
CRYPTO_CORE = ("BTC", "ETH", "SOL")
CRYPTO_MEME = ("PENGU", "PUMP")
MEME_MAX_ACCOUNT_FRAC = 0.05

GateSymbol = str

SYMBOL_PERP: dict[str, str] = {
    "SOXL": "SOXL_USDT",
    "SNXX": "SNXX_USDT",
    "BTC": "BTC_USDT",
    "ETH": "ETH_USDT",
    "SOL": "SOL_USDT",
    "PENGU": "PENGU_USDT",
    "PUMP": "PUMP_USDT",
}

BINANCE_SYMBOL: dict[str, str] = {
    "BTC": "BTCUSDT",
    "ETH": "ETHUSDT",
    "SOL": "SOLUSDT",
    "SOXL": "SOXLUSDT",
    "SNXX": "SNXXUSDT",
}

DrawdownSet = Literal["A", "B", "C"]
DRAWDOWN_SETS: dict[str, tuple[float, ...]] = {
    "A": (-0.08, -0.15, -0.25, -0.35),
    "B": (-0.10, -0.20, -0.30, -0.40),
    "C": (-0.125, -0.25, -0.375, -0.50),
}

SHORT_INIT_PCTS = (0.15, 0.20, 0.25, 0.30)
LEVERAGE_LEVELS = (1.25, 1.5, 1.75, 2.0)
STRESS_LEVERAGE = 3.0
SOXL_WEIGHTS = (0.75, 0.70, 0.65)
GRID_ATR_STEPS = (0.30, 0.40, 0.50, 0.60)
GRID_ATR_RANGES = (3.0, 5.0, 7.0)
ATR_TIMEFRAMES = ("1h", "4h")

ShortStructure = Literal["directional", "grid", "70_30", "50_50"]
SHORT_STRUCTURES: tuple[ShortStructure, ...] = ("directional", "grid", "70_30", "50_50")

GridMix = Literal["G100", "G75", "G50", "G25", "dynamic"]
GRID_MIXES: tuple[GridMix, ...] = ("G100", "G75", "G50", "G25", "dynamic")

ReversalRule = Literal["R1", "R2", "R3", "R4"]
REVERSAL_RULES: tuple[ReversalRule, ...] = ("R1", "R2", "R3", "R4")

ReanchorMode = Literal["off", "7d", "dynamic"]
REANCHOR_MODES: tuple[ReanchorMode, ...] = ("off", "7d", "dynamic")

AnchorMode = Literal["start", "rolling20d"]
ANCHOR_MODES: tuple[AnchorMode, ...] = ("start", "rolling20d")

CryptoRegime = Literal["BULL", "RANGE_HIGH_VOL", "RANGE_LOW_VOL", "BEAR"]

CRYPTO_GRID_MIXES: dict[str, tuple[float, float]] = {
    "80_20": (0.80, 0.20),
    "60_40": (0.60, 0.40),
    "50_50": (0.50, 0.50),
    "40_60": (0.40, 0.60),
    "20_80": (0.20, 0.80),
}

BENCHMARKS = (
    "B1_cash",
    "B2_buy_hold",
    "B3_long_grid_only",
    "B4_directional_long_only",
    "B5_short_to_long_grid",
    "B6_short_to_directional",
    "B7_short_grid_to_directional",
    "B8_dynamic_grid_trend",
    "B9_unified_signal",
    "B10_independent_books",
)

FAILURE_PATTERNS = (
    "direct_up",
    "direct_down",
    "crash_v",
    "crash_sideways",
    "false_bottom",
    "double_bottom",
    "long_high_vol_range",
    "low_vol_chop",
)


@dataclass(frozen=True)
class SeedWindow:
    id: str
    symbol: str
    start: str
    end: str
    pattern: str
    priority: int = 0
    structural_only: bool = False


SEED_WINDOWS: tuple[SeedWindow, ...] = (
    SeedWindow("TECH_T1", "SOXL", "2024-07-10", "2024-09-30", "high_crash_v_chop", 2),
    SeedWindow("TECH_T2", "SOXL", "2025-02-01", "2025-06-30", "sustained_drop_panic_recovery", 1),
    SeedWindow("TECH_T3", "SOXL", "2026-06-22", "2026-08-31", "extreme_drop_bounce", 3),
    SeedWindow("TECH_T4", "SNXX", "2026-07-01", "2026-08-31", "high_beta_crash_bounce", 3),
    SeedWindow("FAIL_F1", "SOXL", "2025-09-01", "2025-10-31", "direct_up_short_pain", 4),
    SeedWindow("FAIL_F2", "SOXL", "2024-09-01", "2024-11-30", "drop_no_bounce_inventory", 4),
    SeedWindow("CRYPTO_C1", "BTC", "2024-09-01", "2024-11-30", "btc_up_tech_weak", 2),
)


@dataclass
class TechParams:
    short_init_pct: float = 0.20
    short_structure: ShortStructure = "70_30"
    leverage: float = 1.5
    drawdown_set: DrawdownSet = "B"
    anchor: AnchorMode = "start"
    grid_atr_step: float = 0.40
    grid_atr_range: float = 5.0
    atr_tf: str = "1h"
    grid_mix: GridMix = "dynamic"
    reanchor: ReanchorMode = "dynamic"
    reversal: ReversalRule = "R2"
    soxl_weight: float = 0.70
    snxx_weight: float = 0.30
    rebate: float = 0.75

    def label(self) -> str:
        return (
            f"tech_s{int(self.short_init_pct*100)}_{self.short_structure}_"
            f"lev{self.leverage}_dd{self.drawdown_set}_{self.grid_mix}_{self.reversal}"
        )


@dataclass
class CryptoParams:
    leverage: float = 1.5
    grid_mix: str = "dynamic"
    meme_frac: float = 0.0
    rebate: float = 0.75
    grid_atr_step: float = 0.40
    grid_atr_range: float = 5.0

    def label(self) -> str:
        return f"crypto_lev{self.leverage}_{self.grid_mix}"


@dataclass
class DualParams:
    tech: TechParams = field(default_factory=TechParams)
    crypto: CryptoParams = field(default_factory=CryptoParams)
    unified_signal: bool = False
    use_global_reserve: bool = False
    fill_mode: str = "base"

    def label(self) -> str:
        tag = "unified" if self.unified_signal else "independent"
        return f"{self.tech.label()}_{self.crypto.label()}_{tag}"


def default_sweep() -> list[TechParams]:
    """Representative tech parameter grid (not full Cartesian — run_job expands)."""
    out: list[TechParams] = []
    for sp in (0.20, 0.25):
        for lev in (1.25, 1.5, 1.75, 2.0):
            for dd in ("A", "B", "C"):
                for gm in ("G50", "dynamic"):
                    for rev in ("R1", "R2"):
                        for sw in (0.70, 0.75):
                            out.append(
                                TechParams(
                                    short_init_pct=sp,
                                    leverage=lev,
                                    drawdown_set=dd,  # type: ignore[arg-type]
                                    grid_mix=gm,  # type: ignore[arg-type]
                                    reversal=rev,  # type: ignore[arg-type]
                                    soxl_weight=sw,
                                    snxx_weight=round(1.0 - sw, 2),
                                )
                            )
    return out


def plan_presets() -> dict[str, dict[str, Any]]:
    """稳健 / 平衡 / 激进 execution plans."""
    return {
        "稳健版": {
            "tech": TechParams(
                short_init_pct=0.20,
                short_structure="70_30",
                leverage=1.25,
                drawdown_set="B",
                grid_atr_step=0.40,
                grid_atr_range=5.0,
                grid_mix="G75",
                reanchor="7d",
                reversal="R2",
                soxl_weight=0.70,
            ),
            "crypto": CryptoParams(leverage=1.25, grid_mix="60_40"),
            "unified_signal": False,
        },
        "平衡版": {
            "tech": TechParams(
                short_init_pct=0.25,
                short_structure="70_30",
                leverage=1.5,
                drawdown_set="B",
                grid_atr_step=0.40,
                grid_atr_range=5.0,
                grid_mix="dynamic",
                reanchor="dynamic",
                reversal="R2",
                soxl_weight=0.70,
            ),
            "crypto": CryptoParams(leverage=1.5, grid_mix="dynamic"),
            "unified_signal": False,
        },
        "激进版": {
            "tech": TechParams(
                short_init_pct=0.30,
                short_structure="directional",
                leverage=1.75,
                drawdown_set="A",
                grid_atr_step=0.30,
                grid_atr_range=7.0,
                grid_mix="G25",
                reanchor="dynamic",
                reversal="R3",
                soxl_weight=0.65,
            ),
            "crypto": CryptoParams(leverage=1.75, grid_mix="20_80"),
            "unified_signal": False,
        },
    }
