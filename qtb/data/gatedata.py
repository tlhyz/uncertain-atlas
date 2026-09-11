"""Official Gate historical quotation dumps (tick / deals).

REST `/spot/trades` only returns a recent 1000-print window and cannot
rebuild history. Tick-accurate research uses the monthly gzip files:

    https://download.gatedata.org/spot/deals/{YYYYMM}/{MARKET}-{YYYYMM}.csv.gz

CSV has no header: timestamp, dealid, price, amount, side
  side 1 = sell, 2 = buy (Gate spot deals convention).
"""

from __future__ import annotations

import gzip
import shutil
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Literal

import numpy as np
import pandas as pd

from .candles import CACHE_DIR

# Gate listings. *3L/*3S = 3x long/short tokens (can trend to ~0).
# SOXLG / SNXXG = tokenized spot SOXL / SNXX (kept in the family, not the default batch).
ETF_FAMILIES: dict[str, tuple[str, ...]] = {
    "soxl": ("SOXL3L_USDT", "SOXL3S_USDT", "SOXLG_USDT"),
    "snxx": ("SNXX3L_USDT", "SNXX3S_USDT", "SNXXG_USDT"),
    "eth": ("ETH3L_USDT", "ETH3S_USDT", "ETH5L_USDT", "ETH5S_USDT"),
    "sol": ("SOL3L_USDT", "SOL3S_USDT", "SOL5L_USDT", "SOL5S_USDT"),
}

DEFAULT_ETF_3X: tuple[str, ...] = (
    "SOXL3L_USDT",
    "SOXL3S_USDT",
    "SNXX3L_USDT",
    "SNXX3S_USDT",
)
DEFAULT_ETF_LONGS = DEFAULT_ETF_3X

BASE_URL = "https://download.gatedata.org"
DEALS_CACHE = CACHE_DIR / "spot_deals"
DEAL_COLUMNS = ["timestamp_unix", "dealid", "price", "amount", "side_code"]
SIDE_MAP = {1: "sell", 2: "buy", "1": "sell", "2": "buy"}
USER_AGENT = "qtb-research/0.3 (gatedata deals)"


def resolve_etf_markets(hints: list[str] | tuple[str, ...] | str) -> list[str]:
    """Map soxl/snxx/eth/sol (or a raw pair) to Gate ETF spot markets."""
    if isinstance(hints, str):
        raw = [p.strip() for p in hints.replace(";", ",").split(",") if p.strip()]
    else:
        raw = [str(x).strip() for x in hints if str(x).strip()]
    out: list[str] = []
    seen: set[str] = set()
    for h in raw:
        key = h.lower().replace("-", "_")
        if key.endswith("_usdt"):
            pair = h.upper().replace("-", "_")
            if pair not in seen:
                seen.add(pair)
                out.append(pair)
            continue
        fam = ETF_FAMILIES.get(key)
        if fam is None:
            pair = h.upper().replace("-", "_")
            if not pair.endswith("_USDT"):
                pair = f"{pair}_USDT"
            if pair not in seen:
                seen.add(pair)
                out.append(pair)
            continue
        for pair in fam:
            if pair not in seen:
                seen.add(pair)
                out.append(pair)
    return out


def parse_year_month(value: str | int) -> tuple[int, int]:
    """Accept 2026-06, 202606, or datetime-like."""
    if isinstance(value, int):
        text = str(value)
    else:
        text = str(value).strip().replace("/", "-")
    digits = "".join(ch for ch in text if ch.isdigit())
    if len(digits) < 6:
        raise ValueError(f"expected YYYY-MM, got {value!r}")
    year, month = int(digits[:4]), int(digits[4:6])
    if not 1 <= month <= 12:
        raise ValueError(f"invalid month in {value!r}")
    return year, month


def month_range(start: str | int, end: str | int) -> list[str]:
    y0, m0 = parse_year_month(start)
    y1, m1 = parse_year_month(end)
    if (y0, m0) > (y1, m1):
        raise ValueError(f"start {start} is after end {end}")
    out: list[str] = []
    y, m = y0, m0
    while (y, m) <= (y1, m1):
        out.append(f"{y:04d}{m:02d}")
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def deals_url(market: str, yyyymm: str) -> str:
    pair = market.strip().replace("-", "_")
    return f"{BASE_URL}/spot/deals/{yyyymm}/{pair}-{yyyymm}.csv.gz"


def deals_cache_path(market: str, yyyymm: str, root: Path | None = None) -> Path:
    base = Path(root) if root is not None else DEALS_CACHE
    pair = market.strip().replace("-", "_")
    return base / pair / f"{pair}-{yyyymm}.csv"


def audit_deals_tape(df: pd.DataFrame) -> dict[str, Any]:
    """Sanity-check an official deals frame. Does not mutate the tape."""
    if df is None or df.empty:
        return {
            "tape_ok": False,
            "tape_error": "empty",
            "n_prints": 0,
            "source": "download.gatedata.org/spot/deals",
        }
    work = df
    n = int(len(work))
    prices = pd.to_numeric(work["price"], errors="coerce") if "price" in work.columns else pd.Series(dtype="float64")
    ts = work["timestamp"] if "timestamp" in work.columns else None
    first_px = float(prices.iloc[0]) if n else None
    last_px = float(prices.iloc[-1]) if n else None
    ret = None
    if first_px and first_px > 0 and last_px is not None:
        ret = last_px / first_px - 1.0
    ts_mono = True
    if ts is not None and n > 1:
        ts_mono = bool((pd.to_datetime(ts).diff().iloc[1:] >= pd.Timedelta(0)).all())
    keys_unique = True
    if "dealid" in work.columns and ts is not None:
        keys_unique = not bool(work.duplicated(subset=["timestamp", "dealid"]).any())
    bad_px = int((prices <= 0).sum()) if n else 0
    bad_amt = 0
    if "amount" in work.columns and n:
        amt = pd.to_numeric(work["amount"], errors="coerce")
        bad_amt = int((amt <= 0).sum())
    ok = n > 0 and ts_mono and keys_unique and bad_px == 0
    return {
        "tape_ok": ok,
        "tape_source": str(work.attrs.get("source") or "download.gatedata.org/spot/deals"),
        "n_prints": n,
        "first_print_px": None if first_px is None else round(first_px, 8),
        "last_print_px": None if last_px is None else round(last_px, 8),
        "tape_return_pct": None if ret is None else round(ret, 6),
        "first_print_ts": str(ts.iloc[0]) if ts is not None and n else None,
        "last_print_ts": str(ts.iloc[-1]) if ts is not None and n else None,
        "tape_ts_monotonic": ts_mono,
        "tape_keys_unique": keys_unique,
        "tape_nonpositive_price": bad_px,
        "tape_nonpositive_amount": bad_amt,
        "tape_high": None if n == 0 else round(float(prices.max()), 8),
        "tape_low": None if n == 0 else round(float(prices.min()), 8),
    }


def parse_deals_csv(text: str) -> pd.DataFrame:
    """Parse official deals body (no header) into a typed frame."""
    if not text.strip():
        return _empty_deals()
    df = pd.read_csv(
        pd.io.common.StringIO(text),
        header=None,
        names=list(DEAL_COLUMNS),
        engine="python",
    )
    return _normalize_deals(df)


def load_deals_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(path, header=None, names=list(DEAL_COLUMNS), engine="python")
    return _normalize_deals(df)


def _empty_deals() -> pd.DataFrame:
    return _normalize_deals(pd.DataFrame(columns=list(DEAL_COLUMNS)))


def _normalize_deals(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        out = pd.DataFrame(
            {
                "timestamp": pd.DatetimeIndex([], tz="UTC"),
                "dealid": pd.Series(dtype="int64"),
                "price": pd.Series(dtype="float64"),
                "amount": pd.Series(dtype="float64"),
                "side": pd.Series(dtype="object"),
            }
        )
        out.attrs["feed"] = "deals"
        return out
    work = df.copy()
    work["timestamp"] = pd.to_datetime(work["timestamp_unix"].astype(float), unit="s", utc=True)
    work["dealid"] = pd.to_numeric(work["dealid"], errors="coerce").fillna(0).astype("int64")
    work["price"] = pd.to_numeric(work["price"], errors="coerce")
    work["amount"] = pd.to_numeric(work["amount"], errors="coerce")
    work["side"] = work["side_code"].map(lambda x: SIDE_MAP.get(x, SIDE_MAP.get(int(x), str(x))))
    work = work.dropna(subset=["timestamp", "price"])
    work = work.loc[work["price"] > 0].copy()
    work = work.sort_values(["timestamp", "dealid"], kind="mergesort").reset_index(drop=True)
    out = work[["timestamp", "dealid", "price", "amount", "side"]]
    out.attrs["feed"] = "deals"
    return out


def _http_get(url: str, timeout: float = 120.0, max_retries: int = 5) -> bytes | None:
    """GET bytes. None means 404 (no file that month)."""
    last_err: Exception | None = None
    for attempt in range(max_retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            last_err = exc
            if exc.code in {429, 500, 502, 503, 504} and attempt + 1 < max_retries:
                time.sleep(min(30.0, 0.6 * (2**attempt)))
                continue
            raise
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            time.sleep(min(20.0, 0.4 * (2**attempt)))
    raise RuntimeError(f"download failed: {url} err={last_err}")


def download_deals_month(
    market: str,
    yyyymm: str,
    root: Path | None = None,
    skip_existing: bool = True,
) -> dict[str, Any]:
    dest = deals_cache_path(market, yyyymm, root)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if skip_existing and dest.exists() and dest.stat().st_size > 0:
        return {"market": market, "month": yyyymm, "status": "skip", "path": str(dest), "bytes": dest.stat().st_size}
    url = deals_url(market, yyyymm)
    print(f"[gatedata] GET {url}")
    raw = _http_get(url)
    if raw is None:
        return {"market": market, "month": yyyymm, "status": "missing", "path": None, "bytes": 0}
    tmp = dest.with_suffix(".csv.part")
    with gzip.GzipFile(fileobj=__import__("io").BytesIO(raw)) as gz, tmp.open("wb") as out:
        shutil.copyfileobj(gz, out)
    tmp.replace(dest)
    return {"market": market, "month": yyyymm, "status": "ok", "path": str(dest), "bytes": dest.stat().st_size}


def download_spot_deals(
    markets: Iterable[str],
    start: str,
    end: str,
    root: Path | None = None,
    skip_existing: bool = True,
) -> list[dict[str, Any]]:
    months = month_range(start, end)
    records: list[dict[str, Any]] = []
    for market in markets:
        pair = market.strip().replace("-", "_")
        for ym in months:
            rec = download_deals_month(pair, ym, root=root, skip_existing=skip_existing)
            records.append(rec)
            print(
                f"[gatedata] {pair} {ym} {rec['status']}"
                + (f" bytes={rec['bytes']}" if rec.get("bytes") else "")
            )
    return records


def load_cached_deals(
    market: str,
    start: str | None = None,
    end: str | None = None,
    root: Path | None = None,
) -> pd.DataFrame:
    pair = market.strip().replace("-", "_")
    base = (Path(root) if root is not None else DEALS_CACHE) / pair
    if not base.exists():
        raise FileNotFoundError(f"no deals cache for {pair} under {base}")
    paths = sorted(base.glob(f"{pair}-*.csv"))
    if start or end:
        y0, m0 = parse_year_month(start) if start else (1970, 1)
        y1, m1 = parse_year_month(end) if end else (2100, 12)
        kept = []
        for p in paths:
            ym = p.stem.split("-")[-1]
            try:
                y, m = parse_year_month(ym)
            except ValueError:
                continue
            if (y0, m0) <= (y, m) <= (y1, m1):
                kept.append(p)
        paths = kept
    if not paths:
        raise FileNotFoundError(f"no monthly deals CSVs for {pair} in {base}")
    frames = [load_deals_csv(p) for p in paths]
    out = pd.concat(frames, ignore_index=True)
    out = out.sort_values(["timestamp", "dealid"], kind="mergesort").drop_duplicates(
        subset=["timestamp", "dealid", "price", "amount"], keep="first"
    )
    out = out.reset_index(drop=True)
    out.attrs["feed"] = "deals"
    out.attrs["symbol"] = pair
    out.attrs["market"] = "spot"
    out.attrs["source"] = "download.gatedata.org/spot/deals"
    out.attrs["files"] = [str(p) for p in paths]
    return out


def ensure_spot_deals(
    market: str,
    start: str,
    end: str,
    root: Path | None = None,
    cache_only: bool = False,
) -> pd.DataFrame:
    """Download any missing months (unless cache_only), then load the tape."""
    if not cache_only:
        download_spot_deals([market], start, end, root=root, skip_existing=True)
    return load_cached_deals(market, start=start, end=end, root=root)


def generate_sample_deals(
    path: Path | None = None,
    n: int = 400,
    mid: float = 1.0,
    amp: float = 0.018,
    start_ts: float = 1_720_000_000.0,
) -> pd.DataFrame:
    """Synthetic tape for offline tests: sine around mid so grids actually fill.

    Not a substitute for official deals. Demo / unit tests only.
    """
    idx = np.arange(n, dtype=float)
    prices = mid * (1.0 + amp * np.sin(idx / 8.0))
    # add a one-way burst so shift tests can use a slice
    rows = []
    for i, px in enumerate(prices):
        side = 2 if i % 2 == 0 else 1
        rows.append(f"{start_ts + i * 2.5:.6f},{i + 1},{px:.8f},{10.0 + (i % 5)},{side}")
    text = "\n".join(rows) + "\n"
    if path is not None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return parse_deals_csv(text)


def default_deals_window() -> tuple[str, str]:
    """Last three UTC calendar months, excluding the in-progress month when possible."""
    now = datetime.now(timezone.utc)
    end_y, end_m = now.year, now.month - 1
    if end_m <= 0:
        end_y, end_m = end_y - 1, 12
    # walk back 2 more months → 3 complete months
    y, m = end_y, end_m
    for _ in range(2):
        m -= 1
        if m <= 0:
            y, m = y - 1, 12
    return f"{y:04d}-{m:02d}", f"{end_y:04d}-{end_m:02d}"


FeedKind = Literal["deals", "candles"]
