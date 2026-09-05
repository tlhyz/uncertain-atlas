"""Config-driven parameter search ranked by composite + anti-overfit score."""

from __future__ import annotations

import copy
from itertools import product
from typing import Any

import pandas as pd

from qtb.engine.backtest import run_backtest

from .antifit import anti_overfit_report, neighbor_stability
from .score import composite_score


def _grid_for(style: str, size: str) -> dict[str, list]:
    if style in {"dual_martingale", "martingale", "aggressive_dual", "aggressive-dual"}:
        if size == "full":
            return {
                "multiplier": [1.3, 1.5, 1.8, 2.0],
                "add_drop_pct": [0.010, 0.015, 0.025],
                "take_profit_pct": [0.006, 0.010, 0.012],
                "max_adds": [20, 40],
                "base_order_quote": [15.0, 25.0],
            }
        if size == "medium":
            return {
                "multiplier": [1.3, 1.5, 2.0],
                "add_drop_pct": [0.010, 0.015],
                "take_profit_pct": [0.006, 0.010],
                "max_adds": [40],
                "base_order_quote": [20.0],
            }
        return {
            "multiplier": [1.3, 1.5],
            "add_drop_pct": [0.010, 0.015],
            "take_profit_pct": [0.008, 0.012],
            "max_adds": [40],
            "base_order_quote": [20.0],
        }
    # grids
    if size == "full":
        return {
            "spacing_pct": [0.005, 0.008, 0.012],
            "grid_count": [16, 24, 32],
            "order_size_quote": [30.0, 50.0],
        }
    if size == "medium":
        return {
            "spacing_pct": [0.006, 0.010],
            "grid_count": [20, 28],
            "order_size_quote": [40.0],
        }
    return {
        "spacing_pct": [0.008, 0.012],
        "grid_count": [20, 28],
        "order_size_quote": [40.0],
    }


def _apply_params(cfg: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
    out = copy.deepcopy(cfg)
    strat = out.setdefault("strategy", {})
    strat.update(params)
    return out


def _cycle_pnls(result) -> list[float]:
    return [p for b in result.books.values() for p in b.cycle_pnls]


def run_optimize(
    cfg: dict[str, Any],
    df: pd.DataFrame,
    progress: bool = True,
) -> dict[str, Any]:
    opt = cfg.get("optimize") or {}
    size = str(opt.get("grid") or "compact")
    top_k = int(opt.get("top_k") or 8)
    weights = opt.get("weights") or {}
    style = str((cfg.get("strategy") or {}).get("name") or "dual_martingale")
    grid = _grid_for(style, size)
    keys = list(grid.keys())
    combos = list(product(*[grid[k] for k in keys]))

    rows: list[dict[str, Any]] = []
    for i, values in enumerate(combos):
        params = dict(zip(keys, values))
        trial_cfg = _apply_params(cfg, params)
        result = run_backtest(trial_cfg, df)
        m = dict(result.metrics)
        raw_score = composite_score(m, weights, stability=0.0)
        row = {
            "params": params,
            "metrics": m,
            "raw_score": raw_score,
            "score": raw_score,
            "liquidated": m.get("liquidated"),
        }
        rows.append(row)
        if progress and (i + 1) % 8 == 0:
            print(f"  [optimize] {i+1}/{len(combos)}", flush=True)

    # Stability on top raw candidates (cheap neighbor eval)
    rows.sort(key=lambda r: r["raw_score"], reverse=True)
    preview = rows[: max(top_k * 2, 6)]

    def _score_neighbor(nb: dict[str, Any], base: dict[str, Any]) -> float:
        merged = {**base, **nb}
        trial_cfg = _apply_params(cfg, merged)
        r = run_backtest(trial_cfg, df)
        return composite_score(r.metrics, weights)

    for row in preview:
        base = row["params"]
        stab = neighbor_stability(lambda nb, b=base: _score_neighbor(nb, b), base)
        row["stability"] = stab
        row["score"] = composite_score(row["metrics"], weights, stability=stab)

    rows.sort(key=lambda r: r["score"], reverse=True)
    top = rows[:top_k]
    best = top[0] if top else None

    antifit: dict[str, Any] = {}
    if best is not None:
        best_cfg = _apply_params(cfg, best["params"])

        def _run_m(part: pd.DataFrame, c=best_cfg) -> dict[str, Any]:
            return run_backtest(c, part).metrics

        best_res = run_backtest(best_cfg, df)
        antifit = anti_overfit_report(
            df,
            _run_m,
            opt,
            _cycle_pnls(best_res),
            float(best["metrics"].get("initial_capital") or 1.0),
            weights=weights,
        )
        best["anti_overfit"] = {
            "train_test": antifit.get("train_test"),
            "walk_forward": antifit.get("walk_forward"),
            "monte_carlo": antifit.get("monte_carlo"),
            "regimes": {k: v.get("score") for k, v in (antifit.get("regimes") or {}).items()},
        }

    heatmap = _heatmap_rows(rows, str(opt.get("heatmap_x") or "add_drop_pct"), str(opt.get("heatmap_y") or "take_profit_pct"))

    return {
        "n_combos": len(combos),
        "grid": grid,
        "top": top,
        "all_scores": [
            {"params": r["params"], "score": r["score"], "metrics": r["metrics"]} for r in rows
        ],
        "best": best,
        "anti_overfit": antifit,
        "heatmap": heatmap,
    }


def _heatmap_rows(rows: list[dict[str, Any]], xkey: str, ykey: str) -> dict[str, Any]:
    cells: list[dict[str, Any]] = []
    for r in rows:
        p = r["params"]
        if xkey in p and ykey in p:
            cells.append({"x": p[xkey], "y": p[ykey], "score": r["score"]})
    return {"x": xkey, "y": ykey, "cells": cells}
