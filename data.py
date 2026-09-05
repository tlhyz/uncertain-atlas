"""
OHLCV data fetchers.

Primary: Gate.io public spot candlesticks (no API key) — natural fit for this toolkit.
Fallback: Binance public klines / data-api (no key) as a liquidity proxy.
Final fallback: bundled/synthetic CSV so demos always run offline.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import Literal

import pandas as pd

try:
    import httpx
except ImportError:  # pragma: no cover
    httpx = None  # type: ignore

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # type: ignore

Interval = Literal["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "1d"]

SAMPLE_CSV = Path(__file__).resolve().parent / "data_sample" / "BTCUSDT_1h_sample.csv"

_INTERVAL_MS = {
    "1m": 60_000,
    "3m": 180_000,
    "5m": 300_000,
    "15m": 900_000,
    "30m": 1_800_000,
    "1h": 3_600_000,
    "2h": 7_200_000,
    "4h": 14_400_000,
    "1d": 86_400_000,
}

_INTERVAL_SEC = {k: v // 1000 for k, v in _INTERVAL_MS.items()}


def _http_get_json(url: str, params: dict, timeout: float = 30.0):
    if httpx is not None:
        r = httpx.get(url, params=params, timeout=timeout)
        r.raise_for_status()
        return r.json()
    if requests is not None:
        r = requests.get(url, params=params, timeout=timeout)
        r.raise_for_status()
        return r.json()
    raise RuntimeError("Need httpx or requests installed to fetch market data")


def _normalize_pair(symbol: str) -> str:
    s = symbol.upper().replace("/", "_").replace("-", "_")
    if "_" not in s and s.endswith("USDT"):
        s = s[:-4] + "_USDT"
    s = s.replace("__", "_")
    return s


def _parse_gate_rows(raw: list) -> list[dict]:
    rows = []
    for item in raw:
        if isinstance(item, dict):
            rows.append(
                {
                    "timestamp": pd.to_datetime(int(item["t"]), unit="s", utc=True),
                    "open": float(item["o"]),
                    "high": float(item["h"]),
                    "low": float(item["l"]),
                    "close": float(item["c"]),
                    "volume": float(item.get("v", item.get("base_volume", 0))),
                }
            )
        else:
            # [timestamp, quote_volume, close, high, low, open, base_volume, ...]
            rows.append(
                {
                    "timestamp": pd.to_datetime(int(item[0]), unit="s", utc=True),
                    "open": float(item[5]),
                    "high": float(item[3]),
                    "low": float(item[4]),
                    "close": float(item[2]),
                    "volume": float(item[6]) if len(item) > 6 else float(item[1]),
                }
            )
    return rows


def fetch_binance_klines(
    symbol: str = "BTCUSDT",
    interval: Interval = "1h",
    days: int = 90,
    limit_per_call: int = 1000,
) -> pd.DataFrame:
    """
    Fetch OHLCV from Binance public API (no key).
    Tries api.binance.com then data-api.binance.vision.
    """
    symbol = symbol.upper().replace("/", "").replace("_", "")
    ms = _INTERVAL_MS[interval]
    end = int(time.time() * 1000)
    start = end - days * 86_400_000
    urls = [
        "https://api.binance.com/api/v3/klines",
        "https://data-api.binance.vision/api/v3/klines",
    ]
    last_err: Exception | None = None
    for url in urls:
        try:
            rows: list = []
            cursor = start
            while cursor < end:
                batch = _http_get_json(
                    url,
                    {
                        "symbol": symbol,
                        "interval": interval,
                        "startTime": cursor,
                        "endTime": end,
                        "limit": limit_per_call,
                    },
                )
                if not batch:
                    break
                rows.extend(batch)
                last_open = int(batch[-1][0])
                next_cursor = last_open + ms
                if next_cursor <= cursor:
                    break
                cursor = next_cursor
                if len(batch) < limit_per_call:
                    break
                time.sleep(0.05)
            if not rows:
                raise RuntimeError(f"{url} returned no klines")
            df = pd.DataFrame(
                rows,
                columns=[
                    "open_time",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "close_time",
                    "quote_volume",
                    "trades",
                    "taker_buy_base",
                    "taker_buy_quote",
                    "ignore",
                ],
            )
            df = df.drop_duplicates(subset=["open_time"]).sort_values("open_time")
            out = pd.DataFrame(
                {
                    "timestamp": pd.to_datetime(df["open_time"], unit="ms", utc=True),
                    "open": df["open"].astype(float),
                    "high": df["high"].astype(float),
                    "low": df["low"].astype(float),
                    "close": df["close"].astype(float),
                    "volume": df["volume"].astype(float),
                }
            ).reset_index(drop=True)
            out.attrs["source"] = f"binance_public_klines:{url.split('/')[2]}"
            out.attrs["symbol"] = symbol
            out.attrs["interval"] = interval
            return out
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            continue
    raise RuntimeError(f"Binance fetch failed: {last_err}")


def fetch_gate_candles(
    currency_pair: str = "BTC_USDT",
    interval: str = "1h",
    days: int = 90,
    limit_per_call: int = 1000,
) -> pd.DataFrame:
    """
    Gate.io public spot candles (no key), paginated (max 1000 points/request).
    https://api.gateio.ws/api/v4/spot/candlesticks

    Uses `to` + `limit` walking backward (more reliable than broad from/to ranges;
    a from/to span of exactly 1000 intervals is rejected as too broad).
    """
    pair = _normalize_pair(currency_pair)
    gate_interval = interval
    step = _INTERVAL_SEC.get(interval, 3600)
    to_ts = int(time.time())
    from_ts = to_ts - days * 86400
    url = "https://api.gateio.ws/api/v4/spot/candlesticks"
    target_bars = max(1, int(days * 86400 / step) + 2)

    rows: list[dict] = []
    cursor_to = to_ts
    safety = 0
    while len(rows) < target_bars and safety < 50:
        safety += 1
        params: dict = {
            "currency_pair": pair,
            "interval": gate_interval,
            "to": cursor_to,
            "limit": limit_per_call,
        }
        batch = _http_get_json(url, params)
        if not batch:
            break
        parsed = _parse_gate_rows(batch)
        rows.extend(parsed)
        # Earliest timestamp in this page
        earliest = min(int(r["timestamp"].timestamp()) for r in parsed)
        if earliest <= from_ts:
            break
        next_to = earliest - step
        if next_to >= cursor_to:
            break
        cursor_to = next_to
        time.sleep(0.05)

    if not rows:
        raise RuntimeError("Gate returned no candles")

    out = pd.DataFrame(rows).drop_duplicates(subset=["timestamp"]).sort_values("timestamp")
    # Trim to requested window
    ts_sec = out["timestamp"].astype("int64") // 10**9
    # pandas datetime64[ns] -> use .view or convert
    mask = out["timestamp"] >= pd.to_datetime(from_ts, unit="s", utc=True)
    out = out.loc[mask].reset_index(drop=True)
    if out.empty:
        raise RuntimeError("Gate candles empty after window trim")
    out.attrs["source"] = "gate_public_candlesticks"
    out.attrs["symbol"] = pair
    out.attrs["interval"] = interval
    return out


def load_csv(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_csv(path)
    cols = {c.lower(): c for c in df.columns}
    rename = {}
    for need in ("open", "high", "low", "close", "volume", "timestamp"):
        if need in cols:
            rename[cols[need]] = need
    df = df.rename(columns=rename)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
    for c in ("open", "high", "low", "close", "volume"):
        if c in df.columns:
            df[c] = df[c].astype(float)
    df.attrs["source"] = f"csv:{path.name}"
    return df.reset_index(drop=True)


def generate_sample_ohlcv(
    path: Path | None = None,
    bars: int = 90 * 24,
    start_price: float = 65000.0,
    seed: int = 42,
) -> pd.DataFrame:
    """Synthetic GBM-ish OHLCV for offline demos."""
    import numpy as np

    rng = np.random.default_rng(seed)
    rets = rng.normal(0.00005, 0.004, size=bars)
    close = start_price * np.exp(np.cumsum(rets))
    open_ = np.roll(close, 1)
    open_[0] = start_price
    spread = np.abs(rng.normal(0.001, 0.0008, size=bars))
    high = np.maximum(open_, close) * (1 + spread)
    low = np.minimum(open_, close) * (1 - spread)
    vol = rng.lognormal(mean=2.0, sigma=0.5, size=bars)
    idx = pd.date_range(end=pd.Timestamp.utcnow().floor("h"), periods=bars, freq="h", tz="UTC")
    df = pd.DataFrame(
        {
            "timestamp": idx,
            "open": open_,
            "high": high,
            "low": low,
            "close": close,
            "volume": vol,
        }
    )
    df.attrs["source"] = "synthetic_sample"
    df.attrs["symbol"] = "BTCUSDT"
    df.attrs["interval"] = "1h"
    if path is not None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
    return df


def fetch_ohlcv(
    symbol: str = "BTCUSDT",
    interval: Interval = "1h",
    days: int = 90,
    prefer: Literal["binance", "gate", "sample"] = "gate",
    sample_path: Path | None = None,
) -> pd.DataFrame:
    """
    Try live public APIs; on failure fall back to bundled/synthetic CSV.
    Default prefer=gate (Binance may be geo-blocked with HTTP 451).
    """
    sample_path = sample_path or SAMPLE_CSV
    errors: list[str] = []

    if prefer == "sample":
        if sample_path.exists():
            df = load_csv(sample_path)
            df.attrs["symbol"] = symbol
            df.attrs["interval"] = interval
            return df
        return generate_sample_ohlcv(sample_path)

    if prefer == "binance":
        order = ["binance", "gate"]
    elif prefer == "gate":
        order = ["gate", "binance"]
    else:
        order = ["gate", "binance"]

    for src in order:
        try:
            if src == "binance":
                return fetch_binance_klines(symbol=symbol, interval=interval, days=days)
            return fetch_gate_candles(
                currency_pair=symbol,
                interval=interval,
                days=days,
            )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{src}: {exc}")

    if sample_path.exists():
        df = load_csv(sample_path)
        df.attrs["fetch_errors"] = errors
        df.attrs["symbol"] = df.attrs.get("symbol") or symbol
        df.attrs["interval"] = interval
        return df
    df = generate_sample_ohlcv(sample_path)
    df.attrs["fetch_errors"] = errors
    return df
