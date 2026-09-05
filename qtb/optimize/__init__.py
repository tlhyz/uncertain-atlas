"""Parameter search, composite scoring, and anti-overfit diagnostics."""

from .antifit import anti_overfit_report
from .score import composite_score, score_metrics
from .search import run_optimize

__all__ = ["composite_score", "score_metrics", "run_optimize", "anti_overfit_report"]
