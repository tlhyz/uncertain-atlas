"""Binance USDT-M public historical data — official Vision + REST fallback.

See docs/DATA_POLICY.md. Raw data → data/raw/binance/ (gitignored).
Implementation delegates to qtb.data.binance_futures during migration.
"""

from qtb.data.binance_futures import (  # noqa: F401
    DEFAULT_SYMBOLS,
    download_symbols_range,
    fetch_agg_trades_day,
    fetch_agg_trades_range,
    fetch_binance_klines_range,
    klines_range_cache_path,
    normalize_symbol,
    trades_day_cache_path,
    vision_zip_url,
)

RAW_ROOT = "data/raw/binance"

SYMBOLS_CRYPTO = ("BTCUSDT", "ETHUSDT", "SOLUSDT", "PENGUUSDT", "PUMPUSDT")
SYMBOLS_TECH = ("SOXLUSDT", "SNXXUSDT", "SOXSUSDT")


def detect_earliest_available(symbol: str, *, cache_only: bool = False) -> str | None:
    """Probe Vision daily ZIPs backward from today until first 404 chain."""
    import httpx
    from datetime import date, timedelta

    sym = normalize_symbol(symbol)
    d = date.today()
    earliest: date | None = None
    misses = 0
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        while misses < 14 and d.year >= 2017:
            url = vision_zip_url(sym, d)
            r = client.get(url)
            if r.status_code == 200:
                earliest = d
                misses = 0
            else:
                misses += 1
            d -= timedelta(days=1)
    return str(earliest) if earliest else None
