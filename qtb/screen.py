"""
Gate USDT-perp screener: high volatility + low one-sided trend (low path efficiency).

Research note (aggressive dual Martingale):
- Extreme one-way trenders (BULLA / AKE) and pure sideways jitter (BTW / TUT) underperform.
- Prefer 牛来 / HYPE-like choppy mid-high vol: wide intra-bar range, but path is not a straight line.
- Score = vol * amp / (trend + 0.05), not raw 24h (high-low)/last.
"""

from __future__ import annotations

import json
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

import pandas as pd

from qtb.data.candles import (
    ROOT,
    api_stats,
    fetch_candles_cached,
    fetch_gate_futures_tickers,
    normalize_contract,
    reset_api_stats,
)

TREND_EPS = 0.05
DEFAULT_MIN_VOLUME = 5_000_000.0
DEFAULT_MIN_RANGE = 0.12
DEFAULT_MAX_TREND = 0.28
DEFAULT_PREFILTER = 40
DEFAULT_TOP = 20
DEFAULT_PICKS = 3
DEFAULT_INTERVAL = "1h"
DEFAULT_DAYS = 7
DEFAULT_CONFIG = ROOT / "configs" / "optimize_niulai_aggressive_sl50.yaml"

RESEARCH_NOTE = (
    "极端单边趋势币（如 BULLA / AKE）和纯横盘碎抖（如 BTW / TUT）回测表现较差；"
    "更偏好 牛来 / HYPE 一类「中高波动 + 低路径效率（来回震荡）」的品种。"
    "评分 score = vol × amp / (trend + 0.05)，不是单纯看 24h 振幅。"
)


def add_screen_flags(p: Any, *, batch_default: bool) -> None:
    """Shared flags for `screen` / `batch-screen` (qtb CLI and legacy cli.py)."""
    import argparse

    if not isinstance(p, argparse.ArgumentParser):
        raise TypeError("add_screen_flags expects an ArgumentParser")
    p.add_argument(
        "--min-volume",
        type=float,
        default=DEFAULT_MIN_VOLUME,
        help="Min 24h quote volume in USDT (default 5000000)",
    )
    p.add_argument(
        "--min-range",
        type=float,
        default=DEFAULT_MIN_RANGE,
        help="Min 24h (high-low)/last prefilter (default 0.12)",
    )
    p.add_argument(
        "--max-trend",
        type=float,
        default=DEFAULT_MAX_TREND,
        help="Keep symbols with path efficiency < this (default 0.28; <0 disables)",
    )
    p.add_argument("--top", type=int, default=DEFAULT_TOP, help="How many scored symbols to print / write (default 20)")
    p.add_argument(
        "--prefilter",
        type=int,
        default=DEFAULT_PREFILTER,
        help="After volume+range filter, fetch candles for top N by 24h range (default 40)",
    )
    p.add_argument("--interval", default=DEFAULT_INTERVAL, help="Path-efficiency candle interval (default 1h)")
    p.add_argument(
        "--days",
        type=int,
        default=DEFAULT_DAYS,
        help="Path-efficiency lookback days (default 7, ~168 hourly bars)",
    )
    p.add_argument("--cache-only", action="store_true", help="Never hit network; use disk cache only")
    p.add_argument("--out", default="", help="Output prefix for JSON/markdown (default outputs/screen_TIMESTAMP)")
    p.add_argument("--picks", type=int, default=DEFAULT_PICKS, help="Top K ranked symbols for --batch-backtest (default 3)")
    p.add_argument(
        "-c",
        "--config",
        default=str(DEFAULT_CONFIG),
        help="YAML for batch optimize/backtest (default configs/optimize_niulai_aggressive_sl50.yaml)",
    )
    p.add_argument(
        "--batch-mode",
        default="backtest",
        choices=["backtest", "optimize"],
        help="batch uses qtb runner: backtest (fixed params) or optimize (compact search)",
    )
    if batch_default:
        p.set_defaults(batch_backtest=True)
    else:
        p.add_argument(
            "--batch-backtest",
            action="store_true",
            help="After ranking, run aggressive dual backtest/optimize on top --picks",
        )


def close_returns(closes: Sequence[float]) -> list[float]:
    """Simple close-to-close returns. Skips a bar if the previous close is 0."""
    out: list[float] = []
    prev: float | None = None
    for raw in closes:
        c = float(raw)
        if prev is not None and prev != 0.0:
            out.append((c - prev) / prev)
        prev = c
    return out


def path_vol(rets: Sequence[float]) -> float:
    """Population stdev of returns (statistics.pstdev)."""
    if len(rets) < 2:
        return 0.0
    return float(statistics.pstdev(rets))


def path_amp(
    highs: Sequence[float],
    lows: Sequence[float],
    closes: Sequence[float],
) -> float:
    """Mean intra-bar amplitude (high-low)/close."""
    vals: list[float] = []
    for h, l, c in zip(highs, lows, closes, strict=False):
        cf = float(c)
        if cf > 0.0:
            vals.append((float(h) - float(l)) / cf)
    if not vals:
        return 0.0
    return float(statistics.fmean(vals))


def path_efficiency(rets: Sequence[float]) -> float:
    """
    Path efficiency / one-sided trend: |net return| / sum(|rets|).

    1.0 = perfectly one-sided; 0.0 = perfectly round-trip chop.
    """
    if not rets:
        return 0.0
    denom = sum(abs(float(r)) for r in rets)
    if denom <= 0.0:
        return 0.0
    return abs(sum(float(r) for r in rets)) / denom


def screen_score(vol: float, amp: float, trend: float, eps: float = TREND_EPS) -> float:
    """vol * amp / (trend + eps). Higher = choppy mid-high vol (preferred)."""
    return float(vol) * float(amp) / (float(trend) + float(eps))


def metrics_from_ohlcv(df: pd.DataFrame) -> dict[str, float | int]:
    closes = df["close"].astype(float).tolist()
    highs = df["high"].astype(float).tolist()
    lows = df["low"].astype(float).tolist()
    rets = close_returns(closes)
    vol = path_vol(rets)
    amp = path_amp(highs, lows, closes)
    trend = path_efficiency(rets)
    net = (closes[-1] / closes[0] - 1.0) if closes and closes[0] else 0.0
    return {
        "vol": vol,
        "amp": amp,
        "trend": trend,
        "score": screen_score(vol, amp, trend),
        "bars": int(len(df)),
        "net_return": net,
        "sum_abs_rets": sum(abs(r) for r in rets),
    }


def is_usdt_perp(name: str) -> bool:
    """USDT-M perpetual-style names; skip dated delivery (BTC_USDT_20260327)."""
    if not name or not name.endswith("_USDT"):
        return False
    parts = name.split("_")
    if len(parts) >= 3 and parts[-1].isdigit() and len(parts[-1]) >= 6:
        return False
    return True


def ticker_quote_volume(row: dict[str, Any]) -> float:
    for key in ("volume_24h_quote", "volume_24h_settle", "volume_24h_usd"):
        val = row.get(key)
        if val in (None, ""):
            continue
        try:
            return float(val)
        except (TypeError, ValueError):
            continue
    return 0.0


def ticker_range_24h(row: dict[str, Any]) -> float | None:
    """(high_24h - low_24h) / last. None if unusable."""
    try:
        last = float(row["last"])
        high = float(row["high_24h"])
        low = float(row["low_24h"])
    except (KeyError, TypeError, ValueError):
        return None
    if last <= 0.0:
        return None
    return (high - low) / last


def parse_ticker_row(row: dict[str, Any]) -> dict[str, Any] | None:
    name = str(row.get("contract") or "").strip()
    if not is_usdt_perp(name):
        return None
    last = None
    try:
        last = float(row.get("last") or 0)
    except (TypeError, ValueError):
        return None
    if last <= 0:
        return None
    rng = ticker_range_24h(row)
    if rng is None:
        return None
    try:
        high = float(row.get("high_24h") or 0)
        low = float(row.get("low_24h") or 0)
    except (TypeError, ValueError):
        high, low = 0.0, 0.0
    chg = row.get("change_percentage")
    try:
        change_pct = float(chg) / 100.0 if chg not in (None, "") else None
    except (TypeError, ValueError):
        change_pct = None
    return {
        "symbol": normalize_contract(name),
        "last": last,
        "high_24h": high,
        "low_24h": low,
        "range_24h": rng,
        "volume_24h": ticker_quote_volume(row),
        "change_pct": change_pct,
    }


def prefilter_tickers(
    tickers: Iterable[dict[str, Any]],
    min_volume: float = DEFAULT_MIN_VOLUME,
    min_range: float = DEFAULT_MIN_RANGE,
    prefilter: int = DEFAULT_PREFILTER,
) -> list[dict[str, Any]]:
    """Volume + 24h-range filter, then top N by 24h range (not by score)."""
    rows: list[dict[str, Any]] = []
    for raw in tickers:
        parsed = parse_ticker_row(raw)
        if parsed is None:
            continue
        if parsed["volume_24h"] < min_volume:
            continue
        if parsed["range_24h"] < min_range:
            continue
        rows.append(parsed)
    rows.sort(key=lambda r: r["range_24h"], reverse=True)
    n = max(0, int(prefilter))
    return rows[:n] if n else rows


def load_simple_config(path: str | Path) -> dict[str, Any]:
    """Load a flat YAML config. Uses PyYAML if present; otherwise a comment-safe line parser."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        if isinstance(data, dict):
            return data
    except Exception:  # noqa: BLE001
        pass
    out: dict[str, Any] = {}
    for line in text.splitlines():
        raw = line.split("#", 1)[0].strip()
        if not raw or ":" not in raw:
            continue
        key, val = raw.split(":", 1)
        key = key.strip()
        val = val.strip().strip("'\"")
        if not key:
            continue
        low = val.lower()
        if low in ("true", "false"):
            out[key] = low == "true"
        elif low in ("null", "none", "~", ""):
            out[key] = None
        else:
            try:
                if val.lstrip("+-").isdigit():
                    out[key] = int(val, 10)
                else:
                    out[key] = float(val)
            except ValueError:
                out[key] = val
    return out


def default_opt_config() -> dict[str, Any]:
    return {
        "name": "optimize_niulai_aggressive_sl50",
        "style": "aggressive-dual",
        "mode": "backtest",
        "symbol": "牛来_USDT",
        "stop_loss": 0.5,
        "interval": "5m",
        "days": 14,
        "market": "futures",
        "grid": "compact",
        "long_cap": 950.0,
        "short_cap": 1380.0,
        "leverage": 5.0,
        "multiplier": 1.5,
        "add_drop_pct": 0.012,
        "take_profit_pct": 0.006,
        "max_adds": 90,
    }


def resolve_out_prefix(out: str, kind: str = "screen") -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    if out:
        p = Path(out)
        if p.suffix.lower() in {".json", ".md", ".markdown"}:
            p = p.with_suffix("")
        return p
    return ROOT / "outputs" / f"{kind}_{stamp}"


def _fmt_qty(x: float | None) -> str:
    if x is None:
        return "-"
    ax = abs(float(x))
    if ax >= 1e9:
        return f"{x / 1e9:.2f}B"
    if ax >= 1e6:
        return f"{x / 1e6:.2f}M"
    if ax >= 1e3:
        return f"{x / 1e3:.1f}k"
    return f"{x:.4f}"


def format_screen_table(rows: Sequence[dict[str, Any]]) -> str:
    if not rows:
        return "(no symbols passed filters)"
    headers = ("rank", "symbol", "score", "vol", "amp", "trend", "range24", "vol24h", "net7d")
    body: list[tuple[str, ...]] = []
    for i, r in enumerate(rows, 1):
        body.append(
            (
                str(i),
                str(r.get("symbol", "")),
                f"{float(r.get('score', 0)):.6f}",
                f"{float(r.get('vol', 0)):.6f}",
                f"{float(r.get('amp', 0)):.6f}",
                f"{float(r.get('trend', 0)):.4f}",
                f"{float(r.get('range_24h', 0)):.4f}",
                _fmt_qty(float(r.get("volume_24h", 0))),
                f"{float(r.get('net_return', 0)):.2%}",
            )
        )
    widths = [len(h) for h in headers]
    for row in body:
        for j, cell in enumerate(row):
            widths[j] = max(widths[j], len(cell))
    sep = "  "
    lines = [sep.join(h.ljust(widths[j]) for j, h in enumerate(headers))]
    lines.append(sep.join("-" * w for w in widths))
    for row in body:
        lines.append(sep.join(cell.ljust(widths[j]) for j, cell in enumerate(row)))
    return "\n".join(lines)


def format_screen_markdown(payload: dict[str, Any]) -> str:
    meta = payload.get("meta") or {}
    rows = payload.get("ranked") or []
    lines = [
        "# Gate USDT 永续选币（高波动 + 低路径效率）",
        "",
        f"> 生成时间（UTC）：{meta.get('generated_utc')} | 研究筛选，非投资建议，无实盘下单。",
        "",
        "## 研究备注",
        "",
        RESEARCH_NOTE,
        "",
        "## 规则",
        "",
        f"- min 24h quote volume ≥ **{meta.get('min_volume')}** USDT",
        f"- 24h range (high-low)/last ≥ **{meta.get('min_range')}**（仅预筛，不是最终排名）",
        f"- 路径 K 线：`{meta.get('interval')}` × {meta.get('days')}d（约 {meta.get('candle_limit')} 根）",
        f"- 预筛取 24h range 前 **{meta.get('prefilter')}** 再拉 K 线",
        f"- trend < **{meta.get('max_trend')}**" if meta.get("max_trend") is not None else "- 未启用 max_trend 过滤",
        f"- score = vol × amp / (trend + {TREND_EPS})",
        f"- vol = pstdev(1h returns)；amp = mean((h-l)/c)；trend = |Σ r| / Σ|r|",
        "",
        f"ticker 合约数={meta.get('ticker_count')} → 成交额+振幅预筛={meta.get('liquid_range_count')} "
        f"→ 拉 K={meta.get('prefilter_count')} → 打分={meta.get('scored_count')} → 入榜={len(rows)}",
        "",
        "## 排名",
        "",
        "| rank | symbol | score | vol | amp | trend | range_24h | volume_24h | net | bars |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for i, r in enumerate(rows, 1):
        lines.append(
            f"| {i} | `{r.get('symbol')}` | {float(r.get('score', 0)):.6f} | "
            f"{float(r.get('vol', 0)):.6f} | {float(r.get('amp', 0)):.6f} | "
            f"{float(r.get('trend', 0)):.4f} | {float(r.get('range_24h', 0)):.4f} | "
            f"{_fmt_qty(float(r.get('volume_24h', 0)))} | {float(r.get('net_return', 0)):.2%} | "
            f"{r.get('bars', '')} |"
        )
    lines += [
        "",
        f"api_calls={meta.get('api_calls')} retries_429={meta.get('retries_429')}",
        "",
    ]
    return "\n".join(lines)


def format_batch_markdown(payload: dict[str, Any]) -> str:
    meta = payload.get("meta") or {}
    rows = payload.get("results") or []
    lines = [
        "# 选币批量回测对比（激进双开马丁）",
        "",
        f"> 生成时间（UTC）：{meta.get('generated_utc')} | config=`{meta.get('config')}` | mode=`{meta.get('mode')}`",
        "",
        "## 研究备注",
        "",
        RESEARCH_NOTE,
        "",
        f"- 取选币榜前 **{meta.get('picks')}**；`--symbol` 覆盖配置里的默认合约",
        f"- 回测/优化：interval=`{meta.get('bt_interval')}` days={meta.get('bt_days')} "
        f"SL={meta.get('stop_loss')} grid=`{meta.get('grid')}`",
        "",
        "| symbol | screen_score | trend | net_pnl | cycles | stop_outs | liq | max_dd_pct | sharpe | score |",
        "|---|---:|---:|---:|---:|---:|---|---:|---:|---:|",
    ]
    for r in rows:
        err = r.get("error")
        if err:
            lines.append(
                f"| `{r.get('symbol')}` | {float(r.get('screen_score', 0)):.6f} | "
                f"{float(r.get('trend', 0)):.4f} | — | — | — | error | — | — | {err} |"
            )
            continue
        lines.append(
            f"| `{r.get('symbol')}` | {float(r.get('screen_score', 0)):.6f} | "
            f"{float(r.get('trend', 0)):.4f} | {r.get('net_pnl')} | "
            f"{r.get('cycles')} | {r.get('stop_outs')} | {r.get('liquidated')} | "
            f"{r.get('max_dd_pct')} | {r.get('sharpe')} | {r.get('opt_score', '')} |"
        )
    lines += ["", f"api_calls={meta.get('api_calls')} retries_429={meta.get('retries_429')}", ""]
    return "\n".join(lines)


def score_universe(
    prefiltered: Sequence[dict[str, Any]],
    *,
    interval: str = DEFAULT_INTERVAL,
    days: int = DEFAULT_DAYS,
    cache_only: bool = False,
    max_trend: float | None = DEFAULT_MAX_TREND,
    min_bars: int = 24,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fetch path candles for prefiltered tickers and score them. Returns (kept, all_scored)."""
    scored: list[dict[str, Any]] = []
    for i, t in enumerate(prefiltered, 1):
        symbol = t["symbol"]
        print(f"[screen] candles {i}/{len(prefiltered)} {symbol} {interval} {days}d")
        try:
            df = fetch_candles_cached(
                symbol,
                interval=interval,
                days=days,
                market="futures",
                cache_only=cache_only,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] skip {symbol}: {exc}")
            continue
        if df is None or len(df) < min_bars:
            print(f"[warn] skip {symbol}: not enough bars ({0 if df is None else len(df)})")
            continue
        m = metrics_from_ohlcv(df)
        row = {
            **t,
            **m,
            "filtered": bool(max_trend is not None and float(m["trend"]) >= float(max_trend)),
            "source": df.attrs.get("source"),
            "cache_hit": df.attrs.get("cache_hit"),
        }
        scored.append(row)
    scored.sort(key=lambda r: float(r.get("score") or 0.0), reverse=True)
    kept = [r for r in scored if not r.get("filtered")]
    return kept, scored


def run_screen(
    *,
    min_volume: float = DEFAULT_MIN_VOLUME,
    min_range: float = DEFAULT_MIN_RANGE,
    max_trend: float | None = DEFAULT_MAX_TREND,
    top: int = DEFAULT_TOP,
    prefilter: int = DEFAULT_PREFILTER,
    interval: str = DEFAULT_INTERVAL,
    days: int = DEFAULT_DAYS,
    cache_only: bool = False,
    out: str = "",
) -> dict[str, Any]:
    reset_api_stats()
    tickers = fetch_gate_futures_tickers(cache_only=cache_only)
    parsed_all = [p for p in (parse_ticker_row(t) for t in tickers) if p is not None]
    liquid_range = [
        p
        for p in parsed_all
        if p["volume_24h"] >= min_volume and p["range_24h"] >= min_range
    ]
    pre = prefilter_tickers(
        tickers, min_volume=min_volume, min_range=min_range, prefilter=prefilter
    )
    kept, scored = score_universe(
        pre,
        interval=interval,
        days=days,
        cache_only=cache_only,
        max_trend=max_trend,
    )
    ranked = kept[: max(0, int(top))]
    stats = api_stats()
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    payload = {
        "meta": {
            "generated_utc": generated,
            "min_volume": min_volume,
            "min_range": min_range,
            "max_trend": max_trend,
            "top": top,
            "prefilter": prefilter,
            "interval": interval,
            "days": days,
            "candle_limit": int(days) * (24 if interval.endswith("h") else 1),
            "ticker_count": len(tickers),
            "liquid_range_count": len(liquid_range),
            "prefilter_count": len(pre),
            "scored_count": len(scored),
            "api_calls": stats.get("calls"),
            "retries_429": stats.get("retries_429"),
            "research_note": RESEARCH_NOTE,
        },
        "ranked": ranked,
        "scored_all": scored,
    }
    prefix = resolve_out_prefix(out, kind="screen")
    prefix.parent.mkdir(parents=True, exist_ok=True)
    json_path = Path(str(prefix) + ".json")
    md_path = Path(str(prefix) + ".md")
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    md_path.write_text(format_screen_markdown(payload), encoding="utf-8")
    payload["meta"]["json_path"] = str(json_path)
    payload["meta"]["md_path"] = str(md_path)
    print(format_screen_table(ranked))
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"api_calls={stats.get('calls')} retries_429={stats.get('retries_429')}")
    return payload


def _safe_tag(symbol: str) -> str:
    return "".join(ch if (ch.isalnum() or ch in "_-") else "_" for ch in symbol)


def _batch_one(
    pick: dict[str, Any],
    config_path: Path,
    *,
    mode: str,
    cache_only: bool,
) -> dict[str, Any]:
    from qtb.config import load_config
    from qtb.runner import run_backtest_job, run_optimize_job

    symbol = pick["symbol"]
    overrides: dict[str, Any] = {
        "symbol": symbol,
        "prefer_sample": False,
        "cache_only": bool(cache_only),
        "mode": mode,
        "run_name": f"screen_batch_{_safe_tag(symbol)}_{mode}",
    }
    cfg = load_config(config_path, overrides=overrides)
    sl = (cfg.get("risk") or {}).get("investment_sl_pct")
    print(
        f"[batch] {mode} {symbol} {cfg.get('interval')} {cfg.get('days')}d "
        f"SL={sl} (config={config_path.name})"
    )
    opt_score = None
    if mode == "optimize":
        result, opt, written = run_optimize_job(cfg)
        opt_score = (opt.get("best") or {}).get("score")
    else:
        result, written = run_backtest_job(cfg)
    m = result.metrics or {}
    return {
        "symbol": symbol,
        "screen_score": pick.get("score"),
        "trend": pick.get("trend"),
        "vol": pick.get("vol"),
        "amp": pick.get("amp"),
        "range_24h": pick.get("range_24h"),
        "volume_24h": pick.get("volume_24h"),
        "net_pnl": m.get("net_pnl"),
        "cashflow": m.get("cycle_pnl_sum", m.get("net_pnl")),
        "cycles": m.get("cycles"),
        "stop_outs": m.get("stop_outs"),
        "liquidated": m.get("liquidated"),
        "max_dd_pct": m.get("max_dd_pct"),
        "sharpe": m.get("sharpe"),
        "opt_score": opt_score,
        "artifacts": written,
        "mode": mode,
    }


def run_batch_backtest(
    picks: Sequence[dict[str, Any]],
    *,
    config_path: str | Path | None = None,
    mode: str = "backtest",
    cache_only: bool = False,
    out: str = "",
) -> dict[str, Any]:
    from qtb.config import load_config

    path = Path(config_path) if config_path else DEFAULT_CONFIG
    if not path.exists():
        raise FileNotFoundError(f"batch config not found: {path}")
    mode = (mode or "backtest").strip().lower()
    if mode not in {"backtest", "optimize"}:
        raise ValueError(f"batch mode must be backtest|optimize, got {mode!r}")
    base_cfg = load_config(path)

    results: list[dict[str, Any]] = []
    for pick in picks:
        try:
            results.append(_batch_one(pick, path, mode=mode, cache_only=cache_only))
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] batch failed {pick.get('symbol')}: {exc}")
            results.append(
                {
                    "symbol": pick.get("symbol"),
                    "screen_score": pick.get("score"),
                    "trend": pick.get("trend"),
                    "error": str(exc),
                }
            )

    stats = api_stats()
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    risk = base_cfg.get("risk") or {}
    opt = base_cfg.get("optimize") or {}
    payload = {
        "meta": {
            "generated_utc": generated,
            "config": str(path),
            "mode": mode,
            "picks": len(picks),
            "bt_interval": base_cfg.get("interval"),
            "bt_days": base_cfg.get("days"),
            "stop_loss": risk.get("investment_sl_pct"),
            "grid": opt.get("grid"),
            "api_calls": stats.get("calls"),
            "retries_429": stats.get("retries_429"),
            "research_note": RESEARCH_NOTE,
        },
        "results": results,
    }
    prefix = resolve_out_prefix(out, kind="batch_screen")
    prefix.parent.mkdir(parents=True, exist_ok=True)
    md_path = Path(str(prefix) + ".md")
    json_path = Path(str(prefix) + ".json")
    md_path.write_text(format_batch_markdown(payload), encoding="utf-8")
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    payload["meta"]["md_path"] = str(md_path)
    payload["meta"]["json_path"] = str(json_path)
    print(format_batch_markdown(payload))
    print(f"Wrote {md_path}")
    print(f"Wrote {json_path}")
    return payload


def execute_screen(args: Any) -> int:
    """CLI handler for `screen` / `batch-screen`."""
    max_trend = getattr(args, "max_trend", DEFAULT_MAX_TREND)
    if max_trend is not None and float(max_trend) < 0:
        max_trend = None
    payload = run_screen(
        min_volume=float(getattr(args, "min_volume", DEFAULT_MIN_VOLUME)),
        min_range=float(getattr(args, "min_range", DEFAULT_MIN_RANGE)),
        max_trend=max_trend,
        top=int(getattr(args, "top", DEFAULT_TOP)),
        prefilter=int(getattr(args, "prefilter", DEFAULT_PREFILTER)),
        interval=str(getattr(args, "interval", DEFAULT_INTERVAL)),
        days=int(getattr(args, "days", DEFAULT_DAYS)),
        cache_only=bool(getattr(args, "cache_only", False)),
        out=str(getattr(args, "out", "") or ""),
    )
    do_batch = bool(getattr(args, "batch_backtest", False))
    if do_batch:
        picks_n = int(getattr(args, "picks", DEFAULT_PICKS))
        picks = (payload.get("ranked") or [])[: max(0, picks_n)]
        if not picks:
            print("[batch] no ranked symbols to backtest")
            return 0
        batch_out = str(getattr(args, "out", "") or "")
        if batch_out:
            batch_out = str(Path(batch_out).with_name(Path(batch_out).name + "_batch"))
        run_batch_backtest(
            picks,
            config_path=getattr(args, "config", None) or DEFAULT_CONFIG,
            mode=str(getattr(args, "batch_mode", "backtest")),
            cache_only=bool(getattr(args, "cache_only", False)),
            out=batch_out,
        )
    return 0
