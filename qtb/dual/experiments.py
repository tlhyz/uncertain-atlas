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
    STRESS_LEVERAGE,
    TECH_BOOK,
    default_sweep,
    plan_presets,
)


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


def compare_independent_vs_unified(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> dict[str, Any]:
    ind = run_dual_portfolio(data, DualParams(unified_signal=False), name="independent", fill_mode=fill_mode, tick_precise=tick_precise)
    uni = run_dual_portfolio(data, DualParams(unified_signal=True), name="unified", fill_mode=fill_mode, tick_precise=tick_precise)
    return {
        "independent": summarize_portfolio(ind),
        "unified": summarize_portfolio(uni),
        "delta_return": summarize_portfolio(ind)["total_return"] - summarize_portfolio(uni)["total_return"],
        "delta_dd": summarize_portfolio(ind)["max_dd_pct"] - summarize_portfolio(uni)["max_dd_pct"],
        "regime_independent": regime_cross_stats(ind.tech_equity, ind.crypto_equity, ind.timestamps),
    }


def rank_short_structures(data: DualDataset, fill_mode: str = "base", tick_precise: bool = False) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for ss in ("directional", "grid", "70_30", "50_50"):
        tp = TechParams(short_structure=ss)  # type: ignore[arg-type]
        r = run_dual_portfolio(data, DualParams(tech=tp), name=ss, fill_mode=fill_mode, tick_precise=tick_precise)
        m = summarize_portfolio(r)
        m["short_structure"] = ss
        rows.append(m)
    rows.sort(key=lambda x: x.get("calmar", 0), reverse=True)
    return rows


def run_binance_crypto_c1(
    *,
    start: str = "2024-09-01",
    end: str = "2024-11-30",
    cache_only: bool = False,
    fill_mode: str = "base",
) -> dict[str, Any]:
    """CRYPTO_C1: BTC independent long on Binance aggTrades + klines."""
    from .data import load_binance_crypto_dataset

    data = load_binance_crypto_dataset(start, end, download_trades=True, cache_only=cache_only)
    dp = DualParams(unified_signal=False)
    r_ind = run_dual_portfolio(
        data, dp, name="C1_independent_ticks", fill_mode=fill_mode,
        crypto_tick_fills=True, tech_disabled=True, tick_precise=True,
    )
    r_uni = run_dual_portfolio(
        data, DualParams(unified_signal=True), name="C1_unified_ticks", fill_mode=fill_mode,
        crypto_tick_fills=True, tech_disabled=False, tick_precise=True,
    )
    # Tech disabled vs unified with synthetic tech drawdown when unified
    m_ind = summarize_portfolio(r_ind, initial=CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
    m_uni = summarize_portfolio(r_uni, initial=CRYPTO_BOOK + GLOBAL_RESERVE + TECH_BOOK)
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
    return rows
