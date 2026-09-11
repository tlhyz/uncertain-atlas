"""Resolve OHLCV (+ optional funding) from a config dict."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from .candles import fetch_candles_cached, fetch_ohlcv, load_csv, normalize_contract
from .funding import align_funding_to_bars, fetch_funding_cached
from .gatedata import default_deals_window, ensure_spot_deals, generate_sample_deals, load_deals_csv


SPOT_MOVING_NAMES = {"moving_grid", "spot_moving_grid", "etf_grid"}
SAMPLE_DEALS = Path("data_sample/etf_deals_sample.csv")


def wants_deals_feed(cfg: dict[str, Any]) -> bool:
    name = str((cfg.get("strategy") or {}).get("name") or "").strip().lower()
    feed = str(cfg.get("feed") or "").strip().lower()
    return feed == "deals" or name in SPOT_MOVING_NAMES


def load_deals_market(cfg: dict[str, Any]) -> pd.DataFrame:
    """Load the official (or sample) spot deals tape. Never falls back to OHLCV."""
    symbol = normalize_contract(str(cfg.get("symbol") or "ETH3L_USDT"))
    prefer_sample = bool(cfg.get("prefer_sample"))
    sample_path = Path(cfg.get("sample_path") or SAMPLE_DEALS)
    if prefer_sample or str(cfg.get("prefer") or "") == "sample":
        if sample_path.exists():
            df = load_deals_csv(sample_path)
        else:
            df = generate_sample_deals(sample_path)
        df.attrs["symbol"] = symbol
        df.attrs["market"] = "spot"
        df.attrs["feed"] = "deals"
        df.attrs["source"] = f"sample:{sample_path}"
        return df

    start = str(cfg.get("deals_from") or "").strip()
    end = str(cfg.get("deals_to") or "").strip()
    if not start or not end:
        start, end = default_deals_window()
    df = ensure_spot_deals(
        symbol,
        start,
        end,
        cache_only=bool(cfg.get("cache_only")),
    )
    df.attrs["symbol"] = symbol
    return df


def load_market(cfg: dict[str, Any]) -> pd.DataFrame:
    symbol = normalize_contract(str(cfg.get("symbol") or "BTC_USDT"))
    interval = str(cfg.get("interval") or "1h")
    days = int(cfg.get("days") or 90)
    market = str(cfg.get("market") or "futures")
    cache_only = bool(cfg.get("cache_only"))
    prefer_sample = bool(cfg.get("prefer_sample"))
    sample_path = Path(cfg.get("sample_path") or "data_sample/BTCUSDT_1h_sample.csv")

    if prefer_sample or str(cfg.get("prefer") or "") == "sample":
        if sample_path.exists():
            df = load_csv(sample_path)
        else:
            df = fetch_ohlcv(symbol=symbol, interval=interval, days=days, prefer="sample")
        df.attrs["symbol"] = symbol
        df.attrs["interval"] = interval
        df.attrs["market"] = market
    else:
        try:
            df = fetch_candles_cached(
                symbol,
                interval=interval,
                days=days,
                market=market if market in {"futures", "spot"} else "futures",
                cache_only=cache_only,
            )
        except Exception:
            if sample_path.exists():
                df = load_csv(sample_path)
                df.attrs["symbol"] = symbol
                df.attrs["interval"] = interval
                df.attrs["fallback"] = "sample_csv"
            else:
                raise

    apply_funding = bool((cfg.get("costs") or {}).get("apply_funding", True))
    if apply_funding and market == "futures":
        funding = None
        if not prefer_sample:
            try:
                funding = fetch_funding_cached(symbol, cache_only=cache_only)
            except Exception:
                funding = None
        df = align_funding_to_bars(df, funding)
    elif "funding_rate" not in df.columns:
        df = df.copy()
        df["funding_rate"] = 0.0
    df.attrs["symbol"] = df.attrs.get("symbol") or symbol
    return df
