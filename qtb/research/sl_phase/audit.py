"""Tape integrity and PUMP contamination checks. Deals only."""

from __future__ import annotations

from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from qtb.data.candles import CACHE_DIR
from qtb.data.gatedata import audit_deals_tape, deals_cache_path, load_cached_deals, month_range
from qtb.research.sl_phase.catalog import PRODUCTS, WINDOWS, utc_bounds


def _exists(market: str, yyyymm: str) -> bool:
    p = deals_cache_path(market, yyyymm)
    return p.exists() and p.stat().st_size > 0


def inventory_months(market: str) -> list[str]:
    base = CACHE_DIR / "spot_deals" / market
    if not base.exists():
        return []
    out = []
    for p in sorted(base.glob(f"{market}-*.csv")):
        ym = p.stem.split("-")[-1]
        if len(ym) == 6 and ym.isdigit():
            out.append(ym)
    return out


def load_strategy_tape(
    market: str,
    start: date | None = None,
    end: date | None = None,
) -> pd.DataFrame:
    """Load official deals, apply listing / contamination filters. Never merges tickers."""
    prod = PRODUCTS.get(market)
    months_start = start.strftime("%Y-%m") if start else None
    months_end = end.strftime("%Y-%m") if end else None
    try:
        df = load_cached_deals(market, start=months_start, end=months_end)
    except FileNotFoundError:
        empty = pd.DataFrame(
            {
                "timestamp": pd.DatetimeIndex([], tz="UTC"),
                "dealid": pd.Series(dtype="int64"),
                "price": pd.Series(dtype="float64"),
                "amount": pd.Series(dtype="float64"),
                "side": pd.Series(dtype="object"),
            }
        )
        empty.attrs["symbol"] = market
        empty.attrs["data_status"] = "DATA_MISSING"
        return empty
    if prod is not None:
        if prod.listed is not None:
            listed_ts = datetime(prod.listed.year, prod.listed.month, prod.listed.day, tzinfo=timezone.utc)
            df = df.loc[df["timestamp"] >= listed_ts]
        if prod.strategy_from is not None:
            sf = datetime(
                prod.strategy_from.year,
                prod.strategy_from.month,
                prod.strategy_from.day,
                tzinfo=timezone.utc,
            )
            df = df.loc[df["timestamp"] >= sf]
    if start is not None and end is not None:
        a, b = utc_bounds(start, end)
        df = df.loc[(df["timestamp"] >= a) & (df["timestamp"] < b)]
    df = df.reset_index(drop=True)
    df.attrs["symbol"] = market
    df.attrs["data_status"] = "ok" if len(df) else "EMPTY_AFTER_FILTER"
    df.attrs["feed"] = "gate_spot_deals"
    return df


def pump_contamination_report() -> dict[str, Any]:
    """Split old PumpBTC-era PUMP3L from pump.fun PUMP3L. Do not concatenate."""
    legacy_months = [ym for ym in inventory_months("PUMP3L_USDT") if ym <= "202506"]
    live_months = [ym for ym in inventory_months("PUMP3L_USDT") if ym >= "202507"]
    pumpbtc_months = inventory_months("PUMPBTC_USDT")
    out: dict[str, Any] = {
        "rule": "PUMP3L before 2025-07-18 is old PumpBTC-era; do not merge with pump.fun PUMP3L",
        "legacy_PUMP3L_months": legacy_months,
        "live_PUMP3L_months": live_months,
        "PUMPBTC_USDT_months": pumpbtc_months,
        "merged": False,
    }
    try:
        legacy = load_cached_deals("PUMP3L_USDT", start="2025-04", end="2025-06")
        live = load_cached_deals("PUMP3L_USDT", start="2025-07", end="2025-07")
    except FileNotFoundError as exc:
        out["error"] = str(exc)
        return out
    cut = datetime(2025, 7, 18, tzinfo=timezone.utc)
    live = live.loc[live["timestamp"] >= cut]
    if legacy.empty or live.empty:
        out["legacy_empty"] = bool(legacy.empty)
        out["live_empty"] = bool(live.empty)
        return out
    out["legacy"] = {
        **audit_deals_tape(legacy),
        "first_ts": str(legacy["timestamp"].iloc[0]),
        "last_ts": str(legacy["timestamp"].iloc[-1]),
    }
    out["live_from_2025_07_18"] = {
        **audit_deals_tape(live),
        "first_ts": str(live["timestamp"].iloc[0]),
        "last_ts": str(live["timestamp"].iloc[-1]),
    }
    gap = float(live["price"].iloc[0] / legacy["price"].iloc[-1] - 1.0) if legacy["price"].iloc[-1] else None
    out["price_gap_legacy_last_to_live_first"] = gap
    out["contiguous_same_instrument"] = False
    out["reason"] = (
        "Same filename PUMP3L_USDT spans PumpBTC-era months (202504-202506) and pump.fun months "
        "(202507+). Cut at 2025-07-18. Strategy loader drops pre-cut prints."
    )
    return out


def product_audit(market: str) -> dict[str, Any]:
    prod = PRODUCTS.get(market)
    months = inventory_months(market)
    rec: dict[str, Any] = {
        "market": market,
        "listed": None if prod is None or prod.listed is None else prod.listed.isoformat(),
        "strategy_from": None if prod is None or prod.strategy_from is None else prod.strategy_from.isoformat(),
        "contaminated_before": None
        if prod is None or prod.contaminated_before is None
        else prod.contaminated_before.isoformat(),
        "cached_months": months,
        "notes": None if prod is None else prod.notes,
        "feed": "gate_spot_deals",
    }
    if not months:
        rec["data_status"] = "DATA_MISSING"
        rec["tape"] = {"tape_ok": False, "n_prints": 0}
        return rec
    df = load_strategy_tape(market)
    rec["tape"] = audit_deals_tape(df)
    rec["strategy_prints"] = int(len(df))
    rec["data_status"] = df.attrs.get("data_status", "ok")
    return rec


def window_audit(wid: str | None = None) -> list[dict[str, Any]]:
    rows = []
    wins = WINDOWS if wid is None else [w for w in WINDOWS if w.id == wid]
    for w in wins:
        row: dict[str, Any] = {
            "window": w.id,
            "asset": w.asset,
            "start": w.start.isoformat(),
            "end": w.end.isoformat(),
            "role": w.role,
            "notes": w.notes,
            "markets": {},
        }
        if not w.trade_markets:
            row["data_status"] = "DATA_MISSING"
            rows.append(row)
            continue
        statuses = []
        for m in w.trade_markets:
            df = load_strategy_tape(m, w.start, w.end)
            tap = audit_deals_tape(df)
            row["markets"][m] = {
                "n_prints": tap.get("n_prints", 0),
                "first": tap.get("first_print_ts"),
                "last": tap.get("last_print_ts"),
                "first_px": tap.get("first_print_px"),
                "last_px": tap.get("last_print_px"),
                "ret": tap.get("tape_return_pct"),
                "status": df.attrs.get("data_status"),
            }
            statuses.append(df.attrs.get("data_status"))
        if all(s in {"DATA_MISSING", "EMPTY_AFTER_FILTER"} for s in statuses):
            row["data_status"] = "DATA_MISSING"
        elif any(s == "ok" for s in statuses):
            row["data_status"] = "partial" if any(s != "ok" for s in statuses) else "ok"
        else:
            row["data_status"] = "EMPTY_AFTER_FILTER"
        rows.append(row)
    return rows


def full_audit() -> dict[str, Any]:
    products = [product_audit(m) for m in PRODUCTS]
    return {
        "feed": "gate_spot_deals",
        "forbidden_primary": ["yahoo_daily", "stooq_daily", "daily_ohlc"],
        "products": products,
        "windows": window_audit(),
        "pump_contamination": pump_contamination_report(),
        "soxl_leverage_warning": "SOXL3L is 3x SOXL, not 9x SOX. SNXX3L is 3x SNXX, not 6x SNDK.",
        "aaoi_note": "AAOI3L_USDT official monthly deals: none published.",
    }
