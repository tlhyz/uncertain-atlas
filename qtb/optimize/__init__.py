"""Parameter search, composite scoring, and anti-overfit diagnostics."""

from .antifit import anti_overfit_report
from .etf_sweep import generate_combos, rank_combos, run_etf_sweep
from .score import composite_score, score_metrics
from .search import run_optimize

__all__ = [
    "anti_overfit_report",
    "composite_score",
    "generate_combos",
    "rank_combos",
    "run_etf_sweep",
    "run_optimize",
    "score_metrics",
]
