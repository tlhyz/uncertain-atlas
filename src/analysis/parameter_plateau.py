"""Parameter plateau detection — STEP 9 (P5-02)."""

from __future__ import annotations

from typing import Any

import numpy as np


def _metric_values(results: list[dict[str, Any]], param_key: str, metric: str) -> tuple[list[float], list[float]]:
    rows = [r for r in results if param_key in r and metric in r]
    rows.sort(key=lambda r: float(r[param_key]))
    params = [float(r[param_key]) for r in rows]
    metrics = [float(r[metric]) for r in rows]
    return params, metrics


def overfit_flag(vals: list[float]) -> dict[str, Any]:
    """
    Classify a 1-D metric sweep as plateau, sensitive, or OVERFIT (god-param).

    Matches ``qtb.ab.experiments._overfit_flag`` semantics.
    """
    if len(vals) < 3:
        return {"flag": "insufficient", "values": list(vals)}
    mid = vals[len(vals) // 2]
    neighbors = [vals[0], vals[-1]]
    if mid > 0.05 and all(v < 0 for v in neighbors):
        return {"flag": "OVERFIT", "values": list(vals), "spread": max(vals) - min(vals)}
    spread = max(vals) - min(vals)
    return {"flag": "plateau" if spread < 0.15 else "sensitive", "values": list(vals), "spread": spread}


def is_plateau(
    results: list[dict[str, Any]],
    param_key: str,
    metric: str = "calmar",
    tol: float = 0.15,
) -> bool:
    """True when metric spread across sweep is within *tol* (legacy API)."""
    _, metrics = _metric_values(results, param_key, metric)
    if len(metrics) < 3:
        return False
    mx = max(abs(v) for v in metrics)
    return (max(metrics) - min(metrics)) / max(mx, 1e-9) <= tol


def robust_pick(
    results: list[dict[str, Any]],
    param_key: str,
    metric: str = "calmar",
) -> float | None:
    """Pick parameter at median metric rank (robust to single sharp peak)."""
    params, metrics = _metric_values(results, param_key, metric)
    if len(params) < 3:
        return None
    order = np.argsort(metrics)
    pick = int(order[len(metrics) // 2])
    return float(params[pick])


def detect_plateau(
    results: list[dict[str, Any]],
    param_key: str,
    metric: str = "calmar",
    *,
    tol: float = 0.15,
    reference_param: float | None = None,
    inert_return_threshold: float = -0.5,
    inert_return_spread: float = 0.05,
) -> dict[str, Any]:
    """
    Analyze a parameter sweep for plateau / sensitivity / overfit.

    Returns structured verdict including ``actionable`` (False for flat failure bands).
    """
    params, metrics = _metric_values(results, param_key, metric)
    n = len(params)
    out: dict[str, Any] = {
        "param_key": param_key,
        "metric": metric,
        "n": n,
        "params": params,
        "metrics": metrics,
        "tol": tol,
    }
    if n < 3:
        out["flag"] = "insufficient"
        out["actionable"] = False
        return out

    of = overfit_flag(metrics)
    spread = float(of.get("spread", 0.0))
    rel_spread = spread / max(max(abs(v) for v in metrics), 1e-9)
    out.update({"spread": spread, "relative_spread": rel_spread, "overfit": of})

    returns = [float(r.get("total_return", 0)) for r in sorted(results, key=lambda r: float(r[param_key])) if param_key in r]
    ret_spread = max(returns) - min(returns) if returns else 0.0
    inert = bool(returns) and all(r <= inert_return_threshold for r in returns) and ret_spread <= inert_return_spread
    out["return_spread"] = ret_spread
    out["inert_failure_band"] = inert

    best_idx = int(np.argmax(metrics))
    out["best_param"] = params[best_idx]
    out["best_metric"] = metrics[best_idx]
    out["robust_pick"] = robust_pick(results, param_key, metric)

    metrics_arr = np.asarray(metrics)
    ranks = metrics_arr.argsort().argsort() + 1  # 1 = worst for ascending sort on calmar negatives
    if metric in ("calmar", "sharpe", "sortino", "total_return"):
        ranks = (-metrics_arr).argsort().argsort() + 1  # 1 = best

    if reference_param is not None:
        ref_idx = min(range(n), key=lambda i: abs(params[i] - reference_param))
        out["reference_param"] = params[ref_idx]
        out["reference_rank"] = int(ranks[ref_idx])
        out["reference_metric"] = metrics[ref_idx]
        out["reference_is_best"] = ref_idx == best_idx

    flag = str(of["flag"])
    if flag == "plateau" and inert:
        out["flag"] = "PLATEAU_INERT"
        out["actionable"] = False
    elif flag == "plateau":
        out["flag"] = "PLATEAU_ACTIONABLE"
        out["actionable"] = True
    elif flag == "OVERFIT":
        out["flag"] = "OVERFIT"
        out["actionable"] = False
    elif flag == "sensitive":
        out["flag"] = "SENSITIVE"
        out["actionable"] = False
    else:
        out["flag"] = flag
        out["actionable"] = False

    out["is_plateau"] = flag == "plateau"
    return out


def analyze_sweep(
    results: list[dict[str, Any]],
    param_key: str,
    metrics: tuple[str, ...] = ("calmar", "total_return"),
    **kwargs: Any,
) -> dict[str, Any]:
    """Run ``detect_plateau`` for each metric."""
    return {m: detect_plateau(results, param_key, metric=m, **kwargs) for m in metrics}
