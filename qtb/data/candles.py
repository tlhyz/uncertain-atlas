"""
OHLCV / trades data fetchers for Gate.io (public, no API key).

Quota-aware design:
- Prefer REST candlesticks (1m/5m/15m/1h/4h/1d) with **disk cache** + incremental gap fill.
- Do NOT spam REST trades/ticks for multi-day history (quota suicide).
- Optional `--trades` pulls a small recent window only; live ticks → WebSocket.
- Clear sleep/backoff on HTTP 429.
"""

from __future__ import annotations

import json
import time
import urllib.parse
from pathlib import Path
from typing import Any, Literal

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

# Repo root (qtb/data/candles.py → parents[2]) so cache/ and data_sample/ stay top-level.
ROOT = Path(__file__).resolve().parents[2]
SAMPLE_CSV = ROOT / "data_sample" / "BTCUSDT_1h_sample.csv"
CACHE_DIR = ROOT / "cache"

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

# Module-level fetch counters (reset per process) for quota reporting
_API_STATS: dict[str, Any] = {
    "calls": 0,
    "bytes": 0,
    "retries_429": 0,
    "last_remain": None,
}


def api_stats() -> dict[str, Any]:
    return dict(_API_STATS)


def reset_api_stats() -> None:
    _API_STATS.update(calls=0, bytes=0, retries_429=0, last_remain=None)


def _safe_filename(symbol: str) -> str:
    """Filesystem-safe name; keep Chinese, percent-encode only awkward chars."""
    s = symbol.strip().replace("/", "_").replace(" ", "_")
    # Avoid path separators / nulls
    for ch in ("\\", ":", "*", "?", '"', "<", ">", "|", "\0"):
        s = s.replace(ch, "_")
    return s


def cache_path(
    symbol: str,
    interval: str,
    market: str = "futures",
    kind: str = "candles",
) -> Path:
    name = f"{market}_{_safe_filename(symbol)}_{interval}_{kind}.csv"
    return CACHE_DIR / name


def _normalize_pair(symbol: str) -> str:
    s = symbol.upper().replace("/", "_").replace("-", "_")
    if "_" not in s and s.endswith("USDT"):
        s = s[:-4] + "_USDT"
    s = s.replace("__", "_")
    return s


def normalize_contract(symbol: str) -> str:
    """Keep Chinese/unicode intact; normalize ASCII pairs to XXX_USDT."""
    pair = symbol.strip()
    if pair.isascii():
        return _normalize_pair(pair)
    # e.g. 牛来_USDT — leave as-is aside from separator cleanup
    return pair.replace("/", "_").replace("-", "_").replace(" ", "")


def encode_contract_for_url(contract: str) -> str:
    """URL-encode contract (Chinese chars → %XX) for Gate path/query."""
    return urllib.parse.quote(contract, safe="_")


def _http_get_json(
    url: str,
    params: dict,
    timeout: float = 30.0,
    max_retries: int = 6,
    min_interval: float = 0.08,
) -> Any:
    """
    GET JSON with 429 backoff. Sleeps briefly between calls to stay under quota.
    """
    last_err: Exception | None = None
    for attempt in range(max_retries):
        if min_interval > 0:
            time.sleep(min_interval)
        try:
            if httpx is not None:
                r = httpx.get(url, params=params, timeout=timeout)
                remain = r.headers.get("X-Gate-RateLimit-Requests-Remain")
                if remain is not None:
                    _API_STATS["last_remain"] = remain
                if r.status_code == 429:
                    _API_STATS["retries_429"] += 1
                    wait = min(60.0, (2**attempt) * 0.5 + 0.5)
                    # Respect Retry-After if present
                    ra = r.headers.get("Retry-After")
                    if ra:
                        try:
                            wait = max(wait, float(ra))
                        except ValueError:
                            pass
                    print(f"[rate-limit] 429 on {url}; sleep {wait:.1f}s (attempt {attempt+1})")
                    time.sleep(wait)
                    continue
                r.raise_for_status()
                _API_STATS["calls"] += 1
                _API_STATS["bytes"] += len(r.content)
                return r.json()
            if requests is not None:
                r = requests.get(url, params=params, timeout=timeout)
                if r.status_code == 429:
                    _API_STATS["retries_429"] += 1
                    wait = min(60.0, (2**attempt) * 0.5 + 0.5)
                    print(f"[rate-limit] 429 on {url}; sleep {wait:.1f}s (attempt {attempt+1})")
                    time.sleep(wait)
                    continue
                r.raise_for_status()
                _API_STATS["calls"] += 1
                _API_STATS["bytes"] += len(r.content or b"")
                return r.json()
            raise RuntimeError("Need httpx or requests installed to fetch market data")
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            # Retry transient network errors
            msg = str(exc).lower()
            if "429" in msg or "timeout" in msg or "connect" in msg:
                wait = min(30.0, (2**attempt) * 0.4)
                time.sleep(wait)
                continue
            raise
    raise RuntimeError(f"HTTP GET failed after retries: {url} params={params} err={last_err}")


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


def _df_from_rows(rows: list[dict], source: str, symbol: str, interval: str, market: str) -> pd.DataFrame:
    if not rows:
        raise RuntimeError(f"No candle rows for {symbol}")
    out = pd.DataFrame(rows).drop_duplicates(subset=["timestamp"]).sort_values("timestamp")
    out = out.reset_index(drop=True)
    out.attrs["source"] = source
    out.attrs["symbol"] = symbol
    out.attrs["interval"] = interval
    out.attrs["market"] = market
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


def save_cache(df: pd.DataFrame, path: Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Persist attrs alongside CSV for provenance
    meta = {
        "source": df.attrs.get("source"),
        "symbol": df.attrs.get("symbol"),
        "interval": df.attrs.get("interval"),
        "market": df.attrs.get("market"),
        "bars": len(df),
    }
    df.to_csv(path, index=False)
    path.with_suffix(".meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def load_cache(path: Path) -> pd.DataFrame | None:
    path = Path(path)
    if not path.exists():
        return None
    df = load_csv(path)
    meta_path = path.with_suffix(".meta.json")
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            for k, v in meta.items():
                if k != "bars":
                    df.attrs[k] = v
        except Exception:  # noqa: BLE001
            pass
    df.attrs["source"] = df.attrs.get("source") or f"cache:{path.name}"
    if "cache" not in str(df.attrs.get("source", "")):
        df.attrs["source"] = f"cache:{path.name}|{df.attrs.get('source')}"
    return df


def _paginate_gate_candles(
    url: str,
    id_key: str,
    contract_or_pair: str,
    interval: str,
    from_ts: int,
    to_ts: int,
    limit_per_call: int = 1000,
    max_pages: int = 80,
) -> list[dict]:
    """Walk backward with `to`+`limit` until covering from_ts."""
    step = _INTERVAL_SEC.get(interval, 300)
    target_bars = max(1, int((to_ts - from_ts) / step) + 2)
    rows: list[dict] = []
    cursor_to = to_ts
    safety = 0
    while len(rows) < target_bars and safety < max_pages:
        safety += 1
        params: dict = {
            id_key: contract_or_pair,
            "interval": interval,
            "to": cursor_to,
            "limit": limit_per_call,
        }
        batch = _http_get_json(url, params)
        if not batch:
            break
        parsed = _parse_gate_rows(batch)
        rows.extend(parsed)
        earliest = min(int(r["timestamp"].timestamp()) for r in parsed)
        if earliest <= from_ts:
            break
        next_to = earliest - step
        if next_to >= cursor_to:
            break
        cursor_to = next_to
    return rows


def fetch_binance_klines(
    symbol: str = "BTCUSDT",
    interval: Interval = "1h",
    days: int = 90,
    limit_per_call: int = 1000,
) -> pd.DataFrame:
    """Fetch OHLCV from Binance public API (no key). Fallback proxy only."""
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
            out.attrs["market"] = "spot"
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
    from_ts: int | None = None,
    to_ts: int | None = None,
) -> pd.DataFrame:
    """Gate.io public spot candles (no key), paginated."""
    pair = _normalize_pair(currency_pair) if currency_pair.isascii() else currency_pair.strip()
    to_ts = int(to_ts or time.time())
    from_ts = int(from_ts if from_ts is not None else to_ts - days * 86400)
    url = "https://api.gateio.ws/api/v4/spot/candlesticks"
    rows = _paginate_gate_candles(
        url, "currency_pair", pair, interval, from_ts, to_ts, limit_per_call=limit_per_call
    )
    if not rows:
        raise RuntimeError("Gate returned no candles")
    out = _df_from_rows(rows, "gate_public_candlesticks", pair, interval, "spot")
    mask = out["timestamp"] >= pd.to_datetime(from_ts, unit="s", utc=True)
    out = out.loc[mask].reset_index(drop=True)
    if out.empty:
        raise RuntimeError("Gate candles empty after window trim")
    return out


def fetch_gate_futures_candles(
    contract: str = "BTC_USDT",
    interval: str = "5m",
    days: int = 30,
    limit_per_call: int = 1000,
    from_ts: int | None = None,
    to_ts: int | None = None,
) -> pd.DataFrame:
    """
    Gate.io public USDT-M futures candlesticks (no key), paginated.
    https://api.gateio.ws/api/v4/futures/usdt/candlesticks
    Contract names may include Chinese (e.g. 牛来_USDT); httpx URL-encodes them.
    """
    pair = normalize_contract(contract)
    to_ts = int(to_ts or time.time())
    from_ts = int(from_ts if from_ts is not None else to_ts - days * 86400)
    url = "https://api.gateio.ws/api/v4/futures/usdt/candlesticks"
    rows = _paginate_gate_candles(
        url, "contract", pair, interval, from_ts, to_ts, limit_per_call=limit_per_call
    )
    if not rows:
        raise RuntimeError(f"Gate futures returned no candles for {pair}")
    out = _df_from_rows(rows, "gate_futures_usdt_candlesticks", pair, interval, "futures")
    mask = out["timestamp"] >= pd.to_datetime(from_ts, unit="s", utc=True)
    out = out.loc[mask].reset_index(drop=True)
    if out.empty:
        raise RuntimeError("Gate futures candles empty after window trim")
    return out


def _merge_candle_frames(parts: list[pd.DataFrame]) -> pd.DataFrame:
    frames = [p for p in parts if p is not None and len(p) > 0]
    if not frames:
        raise RuntimeError("No frames to merge")
    out = pd.concat(frames, ignore_index=True)
    out = out.drop_duplicates(subset=["timestamp"]).sort_values("timestamp").reset_index(drop=True)
    # Preserve attrs from newest non-empty
    for attr in ("source", "symbol", "interval", "market"):
        for f in reversed(frames):
            if f.attrs.get(attr):
                out.attrs[attr] = f.attrs[attr]
                break
    return out


def fetch_candles_cached(
    symbol: str,
    interval: str = "5m",
    days: int = 30,
    market: Literal["futures", "spot"] = "futures",
    cache_only: bool = False,
    force_refresh: bool = False,
    path: Path | None = None,
) -> pd.DataFrame:
    """
    Disk-cached candlesticks with incremental gap fill.

    - Loads local CSV if present.
    - Only fetches missing head/tail ranges (not the full window again).
    - cache_only=True → never hit network (raises if cache missing/insufficient).
    """
    pair = normalize_contract(symbol) if market == "futures" else (
        _normalize_pair(symbol) if symbol.isascii() else symbol.strip()
    )
    path = Path(path) if path else cache_path(pair, interval, market=market, kind="candles")
    now = int(time.time())
    from_ts = now - int(days) * 86400
    step = _INTERVAL_SEC.get(interval, 300)
    # Allow a small lead-in
    from_ts_want = from_ts - step

    cached = None if force_refresh else load_cache(path)
    api_calls_before = _API_STATS["calls"]

    if cache_only:
        if cached is None or cached.empty:
            raise RuntimeError(f"--cache-only but no cache at {path}")
        # Trim to requested window
        mask = cached["timestamp"] >= pd.to_datetime(from_ts_want, unit="s", utc=True)
        out = cached.loc[mask].reset_index(drop=True)
        if out.empty:
            raise RuntimeError(f"--cache-only cache has no bars in last {days}d at {path}")
        out.attrs["cache_hit"] = True
        out.attrs["api_calls"] = 0
        out.attrs["cache_path"] = str(path)
        print(f"[cache-only] {path.name} bars={len(out)} api_calls=0")
        return out

    fetch_fn = fetch_gate_futures_candles if market == "futures" else fetch_gate_candles
    id_kw = "contract" if market == "futures" else "currency_pair"

    if cached is None or cached.empty:
        print(f"[fetch] full {market} {pair} {interval} days={days} ...")
        kwargs = {id_kw: pair, "interval": interval, "days": days}
        fresh = fetch_fn(**kwargs)
        save_cache(fresh, path)
        fresh.attrs["cache_hit"] = False
        fresh.attrs["api_calls"] = _API_STATS["calls"] - api_calls_before
        fresh.attrs["cache_path"] = str(path)
        print(f"[fetch] wrote {path} bars={len(fresh)} api_calls={fresh.attrs['api_calls']}")
        return fresh

    # Incremental: fill left gap (older) and right gap (newer)
    c_start = int(cached["timestamp"].iloc[0].timestamp())
    c_end = int(cached["timestamp"].iloc[-1].timestamp())
    parts: list[pd.DataFrame] = [cached]
    fetched_ranges: list[str] = []

    # Need older data? (ignore gaps smaller than ~2 bars — clock/lead-in noise)
    if c_start > from_ts_want + 2 * step:
        left_to = c_start - step
        left_from = from_ts_want
        if left_to - left_from >= 2 * step:
            print(f"[fetch] left-gap {pair} {interval} {left_from}->{left_to}")
            try:
                left = fetch_fn(
                    **{id_kw: pair},
                    interval=interval,
                    from_ts=left_from,
                    to_ts=left_to,
                    days=max(1, (left_to - left_from) // 86400 + 1),
                )
                parts.append(left)
                fetched_ranges.append("left")
            except Exception as exc:  # noqa: BLE001
                print(f"[warn] left-gap fetch failed: {exc}")

    # Need newer data? (more than ~1.5 intervals stale)
    if c_end < now - int(step * 1.5):
        right_from = c_end + step
        right_to = now
        print(f"[fetch] right-gap {pair} {interval} {right_from}->{right_to}")
        try:
            right = fetch_fn(
                **{id_kw: pair},
                interval=interval,
                from_ts=right_from,
                to_ts=right_to,
                days=max(1, (right_to - right_from) // 86400 + 1),
            )
            parts.append(right)
            fetched_ranges.append("right")
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] right-gap fetch failed: {exc}")

    merged = _merge_candle_frames(parts)
    # Trim to window
    mask = merged["timestamp"] >= pd.to_datetime(from_ts_want, unit="s", utc=True)
    merged = merged.loc[mask].reset_index(drop=True)
    api_delta = _API_STATS["calls"] - api_calls_before
    if fetched_ranges:
        save_cache(merged, path)
        merged.attrs["source"] = f"cache+incremental:{'+'.join(fetched_ranges)}"
        merged.attrs["cache_hit"] = False
        print(f"[fetch] incremental {fetched_ranges} -> {path.name} bars={len(merged)} api_calls={api_delta}")
    else:
        merged.attrs["source"] = f"cache_hit:{path.name}"
        merged.attrs["cache_hit"] = True
        print(f"[cache-hit] {path.name} bars={len(merged)} api_calls=0 (no gaps)")
    merged.attrs["symbol"] = pair
    merged.attrs["interval"] = interval
    merged.attrs["market"] = market
    merged.attrs["api_calls"] = api_delta
    merged.attrs["cache_path"] = str(path)
    return merged


def fetch_gate_futures_trades(
    contract: str,
    limit: int = 1000,
    from_ts: int | None = None,
    to_ts: int | None = None,
) -> pd.DataFrame:
    """
    Sparingly fetch recent futures trades (REST).

    WARNING: Do NOT use this to rebuild 18d history — each call returns ≤1000
    trades and Gate rate-limits hard. For live ticks use WebSocket `futures.trades`.

    Docs:
      REST  GET /api/v4/futures/usdt/trades?contract=BTC_USDT
      WS    wss://fx-ws.gateio.ws/v4/ws/usdt  channel=futures.trades
    """
    pair = normalize_contract(contract)
    url = "https://api.gateio.ws/api/v4/futures/usdt/trades"
    params: dict = {"contract": pair, "limit": min(int(limit), 1000)}
    if from_ts is not None:
        params["from"] = int(from_ts)
    if to_ts is not None:
        params["to"] = int(to_ts)
    print(
        f"[trades] REST pull limit={params['limit']} for {pair} — "
        "prefer candlesticks for history; use WS futures.trades for live"
    )
    raw = _http_get_json(url, params)
    rows = []
    for t in raw or []:
        rows.append(
            {
                "timestamp": pd.to_datetime(int(t.get("create_time", t.get("create_time_ms", 0) // 1000)), unit="s", utc=True)
                if "create_time" in t
                else pd.to_datetime(int(t.get("create_time_ms", 0)), unit="ms", utc=True),
                "id": t.get("id"),
                "price": float(t["price"]),
                "size": float(t.get("size", 0)),
                "contract": pair,
            }
        )
    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values("timestamp").reset_index(drop=True)
    df.attrs["source"] = "gate_futures_usdt_trades_rest"
    df.attrs["symbol"] = pair
    df.attrs["market"] = "futures"
    df.attrs["note"] = (
        "Sparse REST sample only. For live: subscribe WebSocket channel futures.trades. "
        "Do not paginate REST trades across multi-day windows."
    )
    return df


WS_FUTURES_TRADES_DOC = """
# Gate USDT-M futures live trades (WebSocket) — preferred over REST ticks

Endpoint: wss://fx-ws.gateio.ws/v4/ws/usdt

Subscribe:
  {"time": <unix>, "channel": "futures.trades", "event": "subscribe",
   "payload": ["BTC_USDT"]}   # Chinese contracts work URL-encoded in REST; WS uses contract name

Example (python websockets):
  import asyncio, json, time
  import websockets

  async def main():
      uri = "wss://fx-ws.gateio.ws/v4/ws/usdt"
      async with websockets.connect(uri) as ws:
          await ws.send(json.dumps({
              "time": int(time.time()),
              "channel": "futures.trades",
              "event": "subscribe",
              "payload": ["BTC_USDT"],
          }))
          async for msg in ws:
              print(msg)

  asyncio.run(main())

Quota tip: one WS stream ≪ thousands of REST /trades pages for the same live feed.
Backtests should use candlesticks (5m/15m/1h) with disk cache, not tick reconstruction.
"""


def resolve_gate_futures_contract(hint: str) -> str:
    """
    Resolve a user hint (Chinese name / alias) to a Gate USDT-M futures contract name.
    Tries exact match, then substring search on /futures/usdt/contracts.
    """
    hint = hint.strip()
    if hint.endswith("_USDT") or hint.endswith("_USD"):
        return hint
    url = "https://api.gateio.ws/api/v4/futures/usdt/contracts"
    contracts = _http_get_json(url, {})
    names = [c.get("name", "") for c in contracts]
    if hint in names:
        return hint
    norm = _normalize_pair(hint) if hint.isascii() else hint
    if norm in names:
        return norm
    hits = [n for n in names if hint in n or hint.upper() in n.upper()]
    if hits:
        return hits[0]
    chinese = [n for n in names if any("\u4e00" <= ch <= "\u9fff" for ch in n)][:10]
    raise RuntimeError(f"No Gate futures contract matching {hint!r}; sample Chinese: {chinese}")


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
    df.attrs["market"] = "spot"
    if path is not None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
    return df


def fetch_ohlcv(
    symbol: str = "BTCUSDT",
    interval: Interval = "1h",
    days: int = 90,
    prefer: Literal["binance", "gate", "gate_futures", "sample"] = "gate_futures",
    sample_path: Path | None = None,
    cache_only: bool = False,
    use_cache: bool = True,
) -> pd.DataFrame:
    """
    Try live public APIs; on failure fall back to bundled/synthetic CSV.
    Default prefer=gate_futures (USDT-M) with disk cache.
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

    if prefer == "gate_futures":
        try:
            contract = resolve_gate_futures_contract(symbol) if not (
                symbol.endswith("_USDT") or symbol.endswith("_USD")
            ) else normalize_contract(symbol)
            if use_cache:
                return fetch_candles_cached(
                    contract, interval=interval, days=days, market="futures", cache_only=cache_only
                )
            if cache_only:
                raise RuntimeError("cache_only requires use_cache=True")
            return fetch_gate_futures_candles(contract=contract, interval=interval, days=days)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"gate_futures: {exc}")
            if cache_only:
                raise
            prefer = "gate"

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
            if use_cache:
                return fetch_candles_cached(
                    symbol, interval=interval, days=days, market="spot", cache_only=cache_only
                )
            return fetch_gate_candles(currency_pair=symbol, interval=interval, days=days)
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
