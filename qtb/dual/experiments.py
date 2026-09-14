"""Experiment matrix, benchmarks, parameter sweeps."""

from __future__ import annotations

import itertools
from typing import Any

import numpy as np

from .crypto_fsm import CryptoParams
from .data import DualDataset, slice_window
from .metrics import regime_cross_stats, summarize_portfolio
from .portfolio import run_dual_portfolio
from .tech_fsm import TechParams
from .universe import (
    BENCHMARKS,
    CRYPTO_BOOK,
    GLOBAL_RESERVE,
    DualParams,
    GRID_ATR_RANGES,
    GRID_ATR_STEPS,
    GRID_MIXES,
    STRESS_LEVERAGE,
    TECH_BOOK,
    default_sweep,
    plan_presets,
)


def portfolio_kwargs_from_config(cfg: dict[str, Any] | None = None, *, tick_precise: bool = False) -> dict[str, Any]:
    """Map dual job config to run_dual_portfolio keyword args."""
    cfg = cfg or {}
    tech_tick_only = bool(cfg.get("tech_tick_only", True))
    crypto_tick_fills = bool(cfg.get("crypto_tick_fills", False))
    return {
        "fill_mode": str(cfg.get("fill_mode") or "base"),
        "tick_precise": tick_precise,
        "tech_tick_only": tech_tick_only,
        "crypto_tick_fills": crypto_tick_fills,
        "tech_tick_fills": bool(cfg.get("tech_tick_fills", True)),
    }


def run_benchmarks(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> list[dict[str, Any]]:
    base = DualParams()
    rows: list[dict[str, Any]] = []
    for b in BENCHMARKS:
        if b == "B10_independent_books":
            r = run_dual_portfolio(data, base, name=b, fill_mode=fill_mode, tick_precise=tick_precise)
        elif b == "B9_unified_signal":
            p = DualParams(unified_signal=True)
            r = run_dual_portfolio(data, p, name=b, fill_mode=fill_mode, tick_precise=tick_precise)
        else:
            r = run_dual_portfolio(data, base, name=b, fill_mode=fill_mode, benchmark=b, tick_precise=tick_precise)
        m = summarize_portfolio(r)
        m["benchmark"] = b
        rows.append(m)
    return rows


def run_fill_modes(data: DualDataset, params: DualParams | None = None, tick_precise: bool = False) -> dict[str, dict[str, Any]]:
    p = params or DualParams()
    out: dict[str, dict[str, Any]] = {}
    for mode in ("optimistic", "base", "conservative"):
        r = run_dual_portfolio(data, p, name=f"dual_{mode}", fill_mode=mode, tick_precise=tick_precise)
        out[mode] = summarize_portfolio(r)
    return out


def run_parameter_sweep(
    data: DualDataset,
    *,
    max_runs: int = 48,
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Representative sweep — not full Cartesian product."""
    candidates: list[TechParams] = default_sweep()[:max_runs]
    rows: list[dict[str, Any]] = []
    for tp in candidates:
        dp = DualParams(tech=tp, fill_mode=fill_mode)
        for mode in ("base", "conservative"):
            r = run_dual_portfolio(data, dp, name=dp.label(), fill_mode=mode, tick_precise=tick_precise)
            m = summarize_portfolio(r)
            m["params"] = tp.label()
            m["fill"] = mode
            m["tech"] = {
                "drawdown_set": tp.drawdown_set,
                "short_init_pct": tp.short_init_pct,
                "short_structure": tp.short_structure,
                "leverage": tp.leverage,
                "grid_mix": tp.grid_mix,
                "reversal": tp.reversal,
                "soxl_weight": tp.soxl_weight,
                "snxx_weight": tp.snxx_weight,
                "grid_atr_step": tp.grid_atr_step,
                "grid_atr_range": tp.grid_atr_range,
            }
            rows.append(m)
    rows.sort(key=lambda x: (x.get("calmar", 0), x.get("total_return", 0)), reverse=True)
    return rows


def run_stress_leverage(data: DualDataset, fill_mode: str = "conservative", tick_precise: bool = False) -> dict[str, Any]:
    tp = TechParams(leverage=STRESS_LEVERAGE)
    dp = DualParams(tech=tp)
    r = run_dual_portfolio(data, dp, name="stress_3x", fill_mode=fill_mode, tick_precise=tick_precise)
    return summarize_portfolio(r)


def run_seed_windows(
    data: DualDataset,
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Run dual strategy on executable seed windows only."""
    from .universe import SEED_WINDOWS

    rows: list[dict[str, Any]] = []
    dp = DualParams()
    for sw in SEED_WINDOWS:
        cov = next((c for c in data.seed_coverage if c.window.id == sw.id), None)
        if cov and not cov.executable and cov.status == "STRUCTURAL_SEED_ONLY":
            rows.append({
                "seed_id": sw.id,
                "status": "STRUCTURAL_SEED_ONLY",
                "pattern": sw.pattern,
            })
            continue
        try:
            sub = slice_window(data, sw.start, sw.end)
            if len(sub.tech["SOXL"].bars) < 24:
                rows.append({"seed_id": sw.id, "status": "SKIP", "bars": len(sub.tech["SOXL"].bars)})
                continue
            r = run_dual_portfolio(sub, dp, name=sw.id, fill_mode=fill_mode, tick_precise=tick_precise)
            m = summarize_portfolio(r)
            m["seed_id"] = sw.id
            m["pattern"] = sw.pattern
            m["status"] = cov.status if cov else "UNKNOWN"
            rows.append(m)
        except Exception as exc:  # noqa: BLE001
            rows.append({"seed_id": sw.id, "error": str(exc)})
    return rows


def run_plans(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for name, spec in plan_presets().items():
        tp = spec["tech"]
        cp = spec.get("crypto") or CryptoParams()
        dp = DualParams(
            tech=tp,
            crypto=cp,
            unified_signal=bool(spec.get("unified_signal")),
        )
        r_base = run_dual_portfolio(data, dp, name=name, fill_mode="base", tick_precise=tick_precise)
        r_cons = run_dual_portfolio(data, dp, name=name, fill_mode="conservative", tick_precise=tick_precise)
        out[name] = {
            "base": summarize_portfolio(r_base),
            "conservative": summarize_portfolio(r_cons),
            "regime_stats": regime_cross_stats(r_base.tech_equity, r_base.crypto_equity, r_base.timestamps),
        }
    return out


def compare_independent_vs_unified(
    data: DualDataset,
    fill_mode: str = "base",
    tick_precise: bool = False,
    *,
    tech_tick_only: bool = True,
    crypto_tick_fills: bool = False,
    tech_tick_fills: bool = True,
) -> dict[str, Any]:
    kwargs = {
        "fill_mode": fill_mode,
        "tick_precise": tick_precise,
        "tech_tick_only": tech_tick_only,
        "crypto_tick_fills": crypto_tick_fills,
        "tech_tick_fills": tech_tick_fills,
    }
    ind = run_dual_portfolio(data, DualParams(unified_signal=False), name="independent", **kwargs)
    uni = run_dual_portfolio(data, DualParams(unified_signal=True), name="unified", **kwargs)
    ind_m = summarize_portfolio(ind)
    uni_m = summarize_portfolio(uni)
    return {
        "independent": ind_m,
        "unified": uni_m,
        "delta_return": ind_m["total_return"] - uni_m["total_return"],
        "delta_dd": ind_m["max_dd_pct"] - uni_m["max_dd_pct"],
        "regime_independent": regime_cross_stats(ind.tech_equity, ind.crypto_equity, ind.timestamps),
        "regime_unified": regime_cross_stats(uni.tech_equity, uni.crypto_equity, uni.timestamps),
        "portfolio_kwargs": kwargs,
    }


def rank_short_structures(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> list[dict[str, Any]]:
    """Sweep short-phase structure mix (Q-tech / P3-03)."""
    rows: list[dict[str, Any]] = []
    for ss in ("directional", "grid", "70_30", "50_50"):
        print(f"[run] short_structure {ss}...")
        tp = TechParams(short_structure=ss)  # type: ignore[arg-type]
        r = run_dual_portfolio(data, DualParams(tech=tp), name=ss, fill_mode=fill_mode, tick_precise=tick_precise)
        m = summarize_portfolio(r)
        m["short_structure"] = ss
        print(
            f"[run] short_structure {ss} done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def rank_short_init(
    data: DualDataset,
    *,
    levels: tuple[float, ...] = (0.10, 0.15, 0.20),
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Sweep initial short fraction (Q-tech-2 / P3-02)."""
    rows: list[dict[str, Any]] = []
    for sp in levels:
        pct = int(round(sp * 100))
        print(f"[run] short_init {pct}%...")
        tp = TechParams(short_init_pct=sp)
        r = run_dual_portfolio(
            data, DualParams(tech=tp), name=f"short_init_{pct}", fill_mode=fill_mode, tick_precise=tick_precise,
        )
        m = summarize_portfolio(r)
        m["short_init_pct"] = sp
        print(
            f"[run] short_init {pct}% done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def rank_drawdown_sets(
    data: DualDataset,
    *,
    sets: tuple[str, ...] = ("A", "B", "C"),
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Sweep drawdown tier thresholds A/B/C (Q-tech-1 partial / P3-04)."""
    rows: list[dict[str, Any]] = []
    for dd in sets:
        print(f"[run] drawdown_set {dd}...")
        tp = TechParams(drawdown_set=dd)  # type: ignore[arg-type]
        r = run_dual_portfolio(
            data, DualParams(tech=tp), name=f"drawdown_set_{dd}", fill_mode=fill_mode, tick_precise=tick_precise,
        )
        m = summarize_portfolio(r)
        m["drawdown_set"] = dd
        print(
            f"[run] drawdown_set {dd} done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def rank_right_side_reserve(
    data: DualDataset,
    *,
    levels: tuple[float, ...] = (0.25, 0.30, 0.35),
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Sweep reversal-confirm long deployment fraction (P3-06)."""
    rows: list[dict[str, Any]] = []
    for frac in levels:
        pct = int(round(frac * 100))
        print(f"[run] right_side_reserve {pct}%...")
        tp = TechParams(right_side_reserve_frac=frac)
        r = run_dual_portfolio(
            data,
            DualParams(tech=tp),
            name=f"right_side_reserve_{pct}",
            fill_mode=fill_mode,
            tick_precise=tick_precise,
        )
        m = summarize_portfolio(r)
        m["right_side_reserve_frac"] = frac
        print(
            f"[run] right_side_reserve {pct}% done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def rank_margin_reserve(
    data: DualDataset,
    *,
    margin_fracs: tuple[float, ...] = (0.80, 0.70, 0.60),
    fill_mode: str = "base",
    tick_precise: bool = False,
    portfolio_kwargs: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Sweep margin/reserve split within each book (P4-07). margin_frac = deployed fraction."""
    pk = dict(portfolio_kwargs or {})
    pk.pop("fill_mode", None)
    pk.pop("tick_precise", None)
    rows: list[dict[str, Any]] = []
    for mf in margin_fracs:
        res_pct = int(round((1.0 - mf) * 100))
        dep_pct = int(round(mf * 100))
        label = f"{dep_pct}_{res_pct}"
        print(f"[run] margin_reserve {dep_pct}/{res_pct}...")
        r = run_dual_portfolio(
            data,
            DualParams(margin_frac=mf),
            name=f"margin_{label}",
            fill_mode=fill_mode,
            tick_precise=tick_precise,
            **pk,
        )
        m = summarize_portfolio(r)
        m["margin_frac"] = mf
        m["reserve_frac"] = round(1.0 - mf, 4)
        print(
            f"[run] margin_reserve {dep_pct}/{res_pct} done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"max_dd={100 * float(m.get('max_dd_pct', 0)):.2f}% calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def test_funding_stress_deleverage(
    data: DualDataset,
    *,
    thresholds: tuple[float | None, ...] = (None, 0.01, 0.015, 0.02),
    fill_mode: str = "base",
    tick_precise: bool = False,
    portfolio_kwargs: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Baseline vs rolling-7d funding stress deleverage thresholds (P4-08)."""
    pk = dict(portfolio_kwargs or {})
    pk.pop("fill_mode", None)
    pk.pop("tick_precise", None)
    rows: list[dict[str, Any]] = []
    for th in thresholds:
        label = "baseline" if th is None else f"stress_{int(th * 10000)}bp"
        print(f"[run] funding_stress {label}...")
        dp = DualParams(funding_stress_threshold=th)
        r = run_dual_portfolio(
            data, dp, name=label, fill_mode=fill_mode, tick_precise=tick_precise, **pk,
        )
        m = summarize_portfolio(r)
        m["funding_stress_threshold"] = th
        m["stress_triggers_tech"] = r.components.get("funding_stress_triggers_tech", 0)
        m["stress_triggers_crypto"] = r.components.get("funding_stress_triggers_crypto", 0)
        m["max_rolling_stress_tech"] = r.components.get("max_rolling_funding_stress_tech", 0)
        m["max_rolling_stress_crypto"] = r.components.get("max_rolling_funding_stress_crypto", 0)
        print(
            f"[run] funding_stress {label} done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"triggers tech={m['stress_triggers_tech']} crypto={m['stress_triggers_crypto']}"
        )
        rows.append(m)
    return rows


def rank_soxl_snxx_weights(
    data: DualDataset,
    *,
    soxl_weights: tuple[float, ...] = (0.75, 0.70, 0.65),
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Sweep SOXL/SNXX book split (P3-07)."""
    rows: list[dict[str, Any]] = []
    for sw in soxl_weights:
        snw = round(1.0 - sw, 2)
        label = f"{int(sw * 100)}_{int(snw * 100)}"
        print(f"[run] soxl_snxx_weight {label}...")
        tp = TechParams(soxl_weight=sw, snxx_weight=snw)
        r = run_dual_portfolio(
            data,
            DualParams(tech=tp),
            name=f"soxl_snxx_{label}",
            fill_mode=fill_mode,
            tick_precise=tick_precise,
        )
        m = summarize_portfolio(r)
        m["soxl_weight"] = sw
        m["snxx_weight"] = snw
        print(
            f"[run] soxl_snxx_weight {label} done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def rank_grid_mix(
    data: DualDataset,
    *,
    mixes: tuple[str, ...] = GRID_MIXES,
    fill_mode: str = "base",
    tick_precise: bool = False,
) -> list[dict[str, Any]]:
    """Sweep grid→directional mix presets (P3-08)."""
    rows: list[dict[str, Any]] = []
    for gm in mixes:
        print(f"[run] grid_mix {gm}...")
        tp = TechParams(grid_mix=gm)  # type: ignore[arg-type]
        r = run_dual_portfolio(
            data,
            DualParams(tech=tp),
            name=f"grid_mix_{gm}",
            fill_mode=fill_mode,
            tick_precise=tick_precise,
        )
        m = summarize_portfolio(r)
        m["grid_mix"] = gm
        print(
            f"[run] grid_mix {gm} done return={100 * float(m.get('total_return', 0)):.2f}% "
            f"calmar={float(m.get('calmar', 0)):.2f}"
        )
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def run_binance_crypto_c1(
    *,
    start: str = "2024-09-01",
    end: str = "2024-11-30",
    cache_only: bool = False,
    fill_mode: str = "base",
    skip_tick_validation: bool = False,
) -> dict[str, Any]:
    """CRYPTO_C1: BTC/ETH/SOL independent book on Binance aggTrades + klines."""
    from .data import load_binance_crypto_dataset

    data = load_binance_crypto_dataset(
        start, end, download_trades=True, cache_only=cache_only,
        skip_tick_validation=skip_tick_validation,
    )
    dp = DualParams(unified_signal=False)
    print("[run] C1 independent crypto ticks (BTC/ETH/SOL)...")
    r_ind = run_dual_portfolio(
        data, dp, name="C1_independent_ticks", fill_mode=fill_mode,
        crypto_tick_fills=True, tech_disabled=True, tick_precise=True,
    )
    m_ind = summarize_portfolio(r_ind, initial=CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
    print(
        f"[run] C1 independent done return={100 * float(m_ind.get('total_return', 0)):.2f}% "
        f"calmar={float(m_ind.get('calmar', 0)):.2f}"
    )
    # Tech book uses placeholder bars on C1 — bar fills for tech, tick fills for crypto.
    print("[run] C1 unified-signal crypto ticks + tech bar fills...")
    r_uni = run_dual_portfolio(
        data, DualParams(unified_signal=True), name="C1_unified_crypto_ticks", fill_mode=fill_mode,
        crypto_tick_fills=True, tech_tick_fills=False, tech_disabled=False, tick_precise=True,
    )
    # Tech disabled vs unified with synthetic tech drawdown when unified
    m_uni = summarize_portfolio(r_uni, initial=CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
    print(
        f"[run] C1 unified done return={100 * float(m_uni.get('total_return', 0)):.2f}% "
        f"calmar={float(m_uni.get('calmar', 0)):.2f} delta={100 * float(m_ind.get('total_return', 0) - m_uni.get('total_return', 0)):.2f}pp"
    )
    return {
        "window": "CRYPTO_C1",
        "start": start,
        "end": end,
        "data_source": "binance_futures_aggTrades",
        "aggTrades_cached_rows": data.provenance.get("aggTrades_cached_rows"),
        "independent": m_ind,
        "unified": m_uni,
        "delta_return": m_ind.get("total_return", 0) - m_uni.get("total_return", 0),
        "regime_stats": regime_cross_stats(r_ind.crypto_equity, r_ind.tech_equity, r_ind.timestamps),
    }


def rank_leverage(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for lev in (1.25, 1.5, 1.75, 2.0):
        tp = TechParams(leverage=lev)
        r = run_dual_portfolio(data, DualParams(tech=tp), name=f"lev{lev}", fill_mode=fill_mode, tick_precise=tick_precise)
        m = summarize_portfolio(r)
        m["leverage"] = lev
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def rank_grid_atr(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> list[dict[str, Any]]:
    """Sweep grid ATR step × range for Q9/Q10 — measured, not template."""
    rows: list[dict[str, Any]] = []
    for step in GRID_ATR_STEPS:
        for rng in GRID_ATR_RANGES:
            tp = TechParams(grid_atr_step=step, grid_atr_range=rng)
            r = run_dual_portfolio(
                data, DualParams(tech=tp), name=f"atr{step}_r{rng}", fill_mode=fill_mode, tick_precise=tick_precise,
            )
            m = summarize_portfolio(r)
            m["grid_atr_step"] = step
            m["grid_atr_range"] = rng
            rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def _best_by_group(rows: list[dict], group_key: str, metric: str = "calmar") -> dict[str, dict]:
    """Return best row per group_key value (from row[group_key] or row['tech'][group_key])."""
    out: dict[str, dict] = {}
    for r in rows:
        if "error" in r:
            continue
        val = r.get(group_key)
        if val is None and isinstance(r.get("tech"), dict):
            val = r["tech"].get(group_key)
        if val is None:
            continue
        key = str(val)
        if key not in out or r.get(metric, -1e9) > out[key].get(metric, -1e9):
            out[key] = r
    return out
