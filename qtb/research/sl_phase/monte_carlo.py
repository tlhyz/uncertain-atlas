"""Block bootstrap on tick-derived daily equity returns. Preserves vol clustering."""

from __future__ import annotations

import numpy as np


def block_bootstrap(
    daily_equity: np.ndarray,
    *,
    block: int = 1,
    n_paths: int = 1000,
    seed: int = 7,
) -> dict[str, float | int]:
    eq = np.asarray(daily_equity, dtype=float)
    if len(eq) < block + 2:
        return {"status": 0, "n": 0}
    rets = np.diff(eq) / np.maximum(eq[:-1], 1e-12)
    n = len(rets)
    rng = np.random.default_rng(seed)
    finals = np.empty(n_paths)
    mdds = np.empty(n_paths)
    for p in range(n_paths):
        chunks = []
        while len(chunks) * block < n:
            i = int(rng.integers(0, max(1, n - block + 1)))
            chunks.append(rets[i : i + block])
        syn = np.concatenate(chunks)[:n]
        path = eq[0] * np.cumprod(1.0 + syn)
        finals[p] = path[-1]
        peak = np.maximum.accumulate(path)
        mdds[p] = float((path / np.maximum(peak, 1e-12) - 1.0).min())
    start = float(eq[0])
    rel = finals / start - 1.0
    return {
        "n_paths": n_paths,
        "block_days": block,
        "p05": float(np.percentile(rel, 5)),
        "p25": float(np.percentile(rel, 25)),
        "p50": float(np.percentile(rel, 50)),
        "p75": float(np.percentile(rel, 75)),
        "p95": float(np.percentile(rel, 95)),
        "p_loss": float(np.mean(rel < 0)),
        "p_loss_10": float(np.mean(rel < -0.10)),
        "p_loss_20": float(np.mean(rel < -0.20)),
        "mdd_p50": float(np.percentile(mdds, 50)),
        "mdd_p05": float(np.percentile(mdds, 5)),
        "mdd_p95": float(np.percentile(mdds, 95)),
    }
