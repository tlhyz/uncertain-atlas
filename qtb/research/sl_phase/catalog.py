"""Product catalog, listing dates, contamination rules, research windows.

Primary feed is official Gate spot deals (tick/trade tape).
Yahoo / Stooq / any daily OHLC is forbidden as a trading or matching feed.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Literal

from qtb.costs.fees import VIP7_SPOT_NO_REBATE

PRIMARY_FEED = "gate_spot_deals"
FORBIDDEN_PRIMARY_FEEDS = frozenset(
    {
        "yahoo_daily",
        "yahoo_chart",
        "stooq_daily",
        "daily_ohlc",
        "adjclose",
    }
)

# External fee table already in qtb.costs.fees — do not invent new rates.
# VIP7 spot maker 0.0008 / taker 0.00085 (public schedule in _SPOT_VIP_TABLE).
MAKER_FEE = VIP7_SPOT_NO_REBATE.maker_rate
TAKER_FEE = VIP7_SPOT_NO_REBATE.taker_rate
FEE_SOURCE = "qtb.costs.fees._SPOT_VIP_TABLE[7] (external config, not guessed)"
ETF_MGMT_FEE_DAILY = 0.001  # 0.1% NAV / day, charged at UTC+8 00:00
REBATE_SCENARIOS = (0.0, 0.50, 0.70)

UTC8 = timezone.utc  # timestamps on tape are UTC; UTC+8 day = UTC date + 8h


@dataclass(frozen=True)
class Product:
    gate_market: str
    kind: Literal["etf_3l", "etf_3s", "tokenized_underlying", "crypto_spot", "us_etf"]
    listed: date | None
    underlying_gate: str | None
    notes: str
    # If set, strategy must drop prints before this UTC date (contamination / rename).
    strategy_from: date | None = None
    # Prints before this date may exist on disk but must not be merged into the live ticker.
    contaminated_before: date | None = None


PRODUCTS: dict[str, Product] = {
    "SOXL3L_USDT": Product(
        "SOXL3L_USDT",
        "etf_3l",
        date(2026, 6, 25),
        "SOXLG_USDT",
        "Gate 3x on SOXL (already a 3x US ETF). NOT SOX 9x.",
    ),
    "SOXL3S_USDT": Product(
        "SOXL3S_USDT",
        "etf_3s",
        date(2026, 6, 25),
        "SOXLG_USDT",
        "Gate -3x on SOXL. NOT SOX -9x.",
    ),
    "SOXLG_USDT": Product(
        "SOXLG_USDT",
        "tokenized_underlying",
        date(2026, 7, 1),
        None,
        "Gate tokenized SOXL. Proxy for SOXL spot on Gate after listing. Not NYSE SOXL.",
    ),
    "SNXX3L_USDT": Product(
        "SNXX3L_USDT",
        "etf_3l",
        date(2026, 7, 29),
        "SNXXG_USDT",
        "Gate 3x on SNXX (SNXX itself is 2x SNDK). NOT SNDK 6x. SNXX 8-for-1 split was 2026-06; post-listing tape is post-split.",
    ),
    "SNXX3S_USDT": Product(
        "SNXX3S_USDT",
        "etf_3s",
        date(2026, 7, 29),
        "SNXXG_USDT",
        "Gate -3x on SNXX. NOT SNDK -6x.",
    ),
    "SNXXG_USDT": Product(
        "SNXXG_USDT",
        "tokenized_underlying",
        date(2026, 7, 1),
        None,
        "Gate tokenized SNXX. SNXX listed 2026-01-26; 8-for-1 split 2026-06. Do not treat the split as a crash.",
    ),
    "AAOI3L_USDT": Product(
        "AAOI3L_USDT",
        "etf_3l",
        date(2026, 9, 9),
        None,
        "Gate listed 2026-09-09. No official deals file published as of 2026-09. Pre-listing AAOI3L history does not exist on Gate.",
    ),
    "BTC3L_USDT": Product("BTC3L_USDT", "etf_3l", None, "BTC_USDT", "Gate BTC 3x. Model C = official deals."),
    "ETH3L_USDT": Product("ETH3L_USDT", "etf_3l", None, "ETH_USDT", "Gate ETH 3x. Model C = official deals."),
    "SOL3L_USDT": Product("SOL3L_USDT", "etf_3l", None, "SOL_USDT", "Gate SOL 3x. Model C = official deals."),
    "PENGU3L_USDT": Product(
        "PENGU3L_USDT",
        "etf_3l",
        date(2025, 7, 18),
        "PENGU_USDT",
        "Current PENGU3L from 2025-07-18. Official deals start 2025-07.",
        strategy_from=date(2025, 7, 18),
    ),
    "PUMP3L_USDT": Product(
        "PUMP3L_USDT",
        "etf_3l",
        date(2025, 7, 18),
        "PUMP_USDT",
        "Current pump.fun PUMP3L from 2025-07-18. "
        "2025-04..2025-06 PUMP3L deals exist but belong to the old PumpBTC era — do not merge.",
        strategy_from=date(2025, 7, 18),
        contaminated_before=date(2025, 7, 18),
    ),
    "PUMPBTC_USDT": Product(
        "PUMPBTC_USDT",
        "crypto_spot",
        date(2025, 6, 1),
        None,
        "Renamed old PumpBTC spot. Not pump.fun PUMP. Deals from 2025-06.",
    ),
}

# Baseline geometric grids (C = ETF last at hang time). Levels are ETF prices, never underlying.
BASELINE_GRIDS: dict[str, dict[str, float | int]] = {
    "SOXL3L_USDT": {"lower_mult": 0.60, "upper_mult": 1.45, "grid_n": 56, "capital": 1500},
    "AAOI3L_USDT": {"lower_mult": 0.50, "upper_mult": 1.60, "grid_n": 64, "capital": 600},
    "SNXX3L_USDT": {"lower_mult": 0.50, "upper_mult": 1.65, "grid_n": 64, "capital": 600},
    "BTC3L_USDT": {"lower_mult": 0.70, "upper_mult": 1.35, "grid_n": 40, "capital": 300},
    "ETH3L_USDT": {"lower_mult": 0.60, "upper_mult": 1.45, "grid_n": 56, "capital": 750},
    "SOL3L_USDT": {"lower_mult": 0.55, "upper_mult": 1.55, "grid_n": 64, "capital": 1050},
    "PENGU3L_USDT": {"lower_mult": 0.40, "upper_mult": 1.80, "grid_n": 80, "capital": 600},
    "PUMP3L_USDT": {"lower_mult": 0.35, "upper_mult": 1.90, "grid_n": 80, "capital": 300},
}

TARGET_LONG: dict[str, dict[str, float]] = {
    "SOXL3L_USDT": {"max": 3000, "directional": 1500, "grid": 1500},
    "AAOI3L_USDT": {"max": 1000, "directional": 400, "grid": 600},
    "SNXX3L_USDT": {"max": 1000, "directional": 400, "grid": 600},
    "SOL3L_USDT": {"max": 1050, "directional": 0, "grid": 1050},
    "ETH3L_USDT": {"max": 750, "directional": 0, "grid": 750},
    "PENGU3L_USDT": {"max": 600, "directional": 0, "grid": 600},
    "BTC3L_USDT": {"max": 300, "directional": 0, "grid": 300},
    "PUMP3L_USDT": {"max": 300, "directional": 0, "grid": 300},
}

PHASE0 = {
    "equity": 10_000.0,
    "SOXL3S_USDT": 1400.0,
    "SNXX3S_USDT": 600.0,
    "cash": 8000.0,
    "s_hard_cap": 2500.0,
    "early_l_trial_cap": 500.0,
    "reserve_usdt": 2000.0,
}

S_TO_L_PLANS = {
    "A": (-0.05, -0.10, -0.15, -0.20),  # SYSTEM U (underlying)
    "B": (-0.075, -0.125, -0.175, -0.225),
    "C": None,
}

# SYSTEM E: ETF-native triggers on 3L drawdown from L0 (or 3S rally from S0).
ETF_NATIVE_TRIGGERS = {
    "A": (-0.15, -0.30, -0.45, -0.60),
    "B": (-0.20, -0.35, -0.50, -0.65),
    "C": None,
}

DEPLOY_STAGES = {
    "30_30_40": (0.30, 0.30, 0.40),
    "25_25_50": (0.25, 0.25, 0.50),
    "50_25_25": (0.50, 0.25, 0.25),
}

S_REDUCE_REMAINING = (0.15, 0.25, 0.30, 1.0)  # of remaining S
S_REDUCE_INITIAL = (0.15, 0.25, 0.30, 0.30)  # of initial S (last step = leftover)


@dataclass(frozen=True)
class Window:
    id: str
    asset: str
    start: date
    end: date
    role: Literal["main", "stress"]
    trade_markets: tuple[str, ...]
    anchor_market: str | None
    notes: str


# Human calendars on underlyings — candidates only, never final ETF windows.
WINDOWS: tuple[Window, ...] = (
    Window("S1", "SOXL", date(2024, 7, 1), date(2024, 9, 6), "main", (), None, "No Gate SOXL3L/SOXLG deals (listed 2026-06-25). DATA_MISSING."),
    Window("S2", "SOXL", date(2025, 2, 3), date(2025, 6, 30), "main", (), None, "No Gate SOXL3L/SOXLG deals. DATA_MISSING."),
    Window("S3", "SOXL", date(2026, 6, 25), date(2026, 9, 11), "main", ("SOXL3L_USDT", "SOXL3S_USDT", "SOXLG_USDT", "ETH3L_USDT", "SOL3L_USDT", "SNXX3L_USDT", "SNXX3S_USDT"), "SOXLG_USDT", "Real SOXL3L/S ticks. SOXLG from 2026-07. Sept 2026 monthly deals not published."),
    Window("N1", "SNXX", date(2026, 6, 22), date(2026, 9, 4), "main", ("SNXX3L_USDT", "SNXX3S_USDT", "SNXXG_USDT"), "SNXXG_USDT", "Gate SNXX3L/S from 2026-07-29. Pre-listing slice has no 3x tape."),
    Window("A1", "AAOI", date(2024, 2, 1), date(2024, 11, 30), "main", (), None, "AAOI3L listed 2026-09-09. No official deals. DATA_MISSING."),
    Window("A2", "AAOI", date(2026, 5, 13), date(2026, 8, 31), "main", (), None, "Pre-listing. No AAOI3L deals. DATA_MISSING."),
    Window("B1", "BTC", date(2024, 7, 29), date(2024, 9, 30), "main", ("BTC3L_USDT",), None, "Official BTC3L deals."),
    Window("B2", "BTC", date(2025, 1, 20), date(2025, 5, 31), "main", ("BTC3L_USDT",), None, "Official BTC3L deals."),
    Window("E1", "ETH", date(2025, 3, 24), date(2025, 5, 13), "main", ("ETH3L_USDT",), None, "Official ETH3L deals."),
    Window("L1", "SOL", date(2024, 7, 29), date(2024, 8, 24), "main", ("SOL3L_USDT",), None, "Official SOL3L deals."),
    Window("L2", "SOL", date(2025, 3, 24), date(2025, 5, 31), "main", ("SOL3L_USDT",), None, "Official SOL3L deals."),
    Window("PG1", "PENGU", date(2025, 1, 1), date(2025, 7, 31), "main", ("PENGU3L_USDT",), None, "PENGU3L deals from 2025-07 only. Jan–mid-Jul DATA_MISSING."),
    Window("PG2", "PENGU", date(2026, 1, 1), date(2026, 8, 31), "main", ("PENGU3L_USDT",), None, "Official PENGU3L deals."),
    Window("PP1", "PUMP", date(2026, 2, 1), date(2026, 8, 31), "main", ("PUMP3L_USDT",), None, "pump.fun PUMP3L only (strategy_from 2025-07-18)."),
    Window("SX_FAIL", "SOXL", date(2026, 4, 1), date(2026, 7, 31), "stress", ("SOXL3L_USDT", "SOXL3S_USDT", "SOXLG_USDT"), "SOXLG_USDT", "Pre-listing Apr–Jun 24 DATA_MISSING. Jun 25–Jul 31 has ticks."),
    Window("NX_FAIL", "SNXX", date(2026, 3, 30), date(2026, 7, 29), "stress", ("SNXX3L_USDT", "SNXX3S_USDT"), "SNXXG_USDT", "Almost entirely pre-listing. Only 2026-07-29 has 3x ticks."),
    Window("AX_FAIL", "AAOI", date(2024, 8, 1), date(2025, 4, 30), "stress", (), None, "No AAOI3L deals. DATA_MISSING."),
    Window("BX_FAIL", "BTC", date(2024, 9, 6), date(2025, 4, 7), "stress", ("BTC3L_USDT",), None, "Official BTC3L deals."),
    Window("EX_FAIL", "ETH", date(2024, 9, 1), date(2025, 4, 9), "stress", ("ETH3L_USDT",), None, "Official ETH3L deals."),
    Window("LX_FAIL", "SOL", date(2024, 8, 5), date(2025, 4, 9), "stress", ("SOL3L_USDT",), None, "Official SOL3L deals."),
    Window("PGX_FAIL", "PENGU", date(2025, 4, 1), date(2025, 12, 31), "stress", ("PENGU3L_USDT",), None, "Ticks from 2025-07-18 only."),
    Window("PPX_FAIL", "PUMP", date(2025, 9, 14), date(2025, 12, 31), "stress", ("PUMP3L_USDT",), None, "pump.fun PUMP3L ticks."),
    Window("E_V2024", "ETH", date(2024, 7, 29), date(2024, 9, 30), "main", ("ETH3L_USDT",), None, "Auto-added 2024-07..09 ETH V-like window (same calendar as B1)."),
)

CANDIDATE_REGIMES: tuple[Window, ...] = WINDOWS

SCAN_GRID_N = (32, 48, 64, 80)
SCAN_RANGE = (0.75, 1.0, 1.25)
SCAN_REANCHOR = ("off", "7_day", "14_day", "volatility_triggered")
SCAN_S_INITIAL = (1500.0, 2000.0, 2500.0)
FILL_MODELS = ("optimistic", "base", "conservative")
SIZING_MODES = ("fixed_quote", "fixed_qty", "vol_adjusted")
REANCHOR_VOL_PCT = 0.25
GRID_SPACINGS_FOR_SCAN = (0.003, 0.005, 0.008, 0.01, 0.015, 0.02)

# Leverage bands (Gate-like Model A).
LEV_3L = (2.25, 4.125)
LEV_3S = (1.50, 5.25)
TARGET_LEV_3L = 3.0
TARGET_LEV_3S = -3.0


def utc_bounds(start: date, end: date) -> tuple[datetime, datetime]:
    """Inclusive calendar dates → UTC [start 00:00, end+1day 00:00)."""
    a = datetime(start.year, start.month, start.day, tzinfo=timezone.utc)
    b = datetime(end.year, end.month, end.day, tzinfo=timezone.utc)
    from datetime import timedelta

    return a, b + timedelta(days=1)


def window_by_id(wid: str) -> Window:
    for w in WINDOWS:
        if w.id == wid:
            return w
    raise KeyError(wid)
