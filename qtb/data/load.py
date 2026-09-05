"""Resolve OHLCV (+ optional funding) from a config dict."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from .candles import fetch_candles_cached, fetch_ohlcv, load_csv, normalize_contract
from .funding import align_funding_to_bars, fetch_funding_cached


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
