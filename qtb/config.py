"""Load YAML/TOML configs. Defaults keep mode=backtest and live dry_run=true."""

from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None  # type: ignore


def _deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(base)
    for k, v in overlay.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


DEFAULT_CONFIG: dict[str, Any] = {
    "mode": "backtest",
    "symbol": "BTC_USDT",
    "interval": "1h",
    "days": 90,
    "market": "futures",
    "cache_only": False,
    "prefer_sample": False,
    "sample_path": "data_sample/BTCUSDT_1h_sample.csv",
    "feed": "",
    "deals_from": "",
    "deals_to": "",
    "output_dir": "outputs",
    "run_name": "",
    "costs": {
        "vip_tier": 7,
        "rebate_rate": 0.75,
        "market": "futures",
        "slippage_bps": 1.0,
        "use_maker": False,
        "quanto": 0.0001,
        "min_order_size": 1.0,
        "min_notional": 1.0,
        "apply_funding": True,
        "maintenance_rate": 0.005,
    },
    "strategy": {
        "name": "dual_martingale",
        "leverage": 5.0,
        "long_capital": 950.0,
        "short_capital": 1380.0,
        "initial_margin": 2330.0,
        "multiplier": 1.5,
        "add_drop_pct": 0.015,
        "take_profit_pct": 0.010,
        "max_adds": 40,
        "base_order_quote": 20.0,
        "fee_as_maker": False,
        "cooldown_bars": 0,
        "grid_count": 24,
        "spacing_pct": 0.008,
        "order_size_quote": 40.0,
        "lower": None,
        "upper": None,
        "ema_period": 48,
        "trend_threshold": 0.002,
        "martingale_addon": False,
        "direction": "dual",
    },
    "risk": {
        "per_trade_tp_pct": None,
        "per_trade_sl_pct": None,
        "investment_sl_pct": 0.50,
        "portfolio_tp_pct": None,
        "portfolio_equity_sl_pct": None,
        "max_drawdown_stop_pct": None,
        "stop_adding_float_loss_pct": None,
        "force_exit_before_liq_buffer_pct": 0.20,
        "stop_if_price_breaks_range": True,
        "trailing_tp_pct": None,
        "trailing_activation_pct": None,
        "time_tp_bars": None,
        "scaled_tp": [],
    },
    "optimize": {
        "grid": "compact",
        "train_ratio": 0.70,
        "walk_forward_folds": 3,
        "monte_carlo_paths": 40,
        "regime_splits": 3,
        "top_k": 8,
        "heatmap_x": "add_drop_pct",
        "heatmap_y": "take_profit_pct",
        "weights": {
            "return": 1.0,
            "max_dd": 0.9,
            "sharpe": 0.6,
            "calmar": 0.5,
            "win_rate": 0.25,
            "profit_factor": 0.35,
            "max_float_loss": 0.5,
            "liq_risk": 2.0,
            "fee_ratio": 0.3,
            "stability": 0.4,
        },
    },
    "live": {
        "dry_run": True,
        "note": "Live is a stub. Real orders require ALLOW_LIVE=1 AND dry_run=false, and still have no order path.",
    },
    "batch": {
        "symbols": ["BTC_USDT"],
        "intervals": ["1h"],
    },
}


def default_config() -> dict[str, Any]:
    return copy.deepcopy(DEFAULT_CONFIG)


def load_config(path: str | Path | None = None, overrides: dict[str, Any] | None = None) -> dict[str, Any]:
    cfg = default_config()
    if path is not None:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"config not found: {p}")
        data = _read_file(p)
        if not isinstance(data, dict):
            raise ValueError(f"config root must be a mapping: {p}")
        cfg = _deep_merge(cfg, data)
    if overrides:
        cfg = _deep_merge(cfg, overrides)
    if not cfg.get("mode"):
        cfg["mode"] = "backtest"
    live = cfg.setdefault("live", {})
    if "dry_run" not in live:
        live["dry_run"] = True
    return cfg


def _read_file(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix in {".yaml", ".yml"}:
        try:
            import yaml
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError("PyYAML is required for YAML configs: pip install pyyaml") from exc
        data = yaml.safe_load(text) or {}
        return data
    if suffix == ".toml":
        if tomllib is None:
            raise RuntimeError("tomllib unavailable; use Python 3.11+")
        return tomllib.loads(text)
    raise ValueError(f"unsupported config suffix {suffix}; use .yaml/.yml/.toml")


def dump_yaml(cfg: dict[str, Any], path: Path) -> Path:
    import yaml

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )
    return path
