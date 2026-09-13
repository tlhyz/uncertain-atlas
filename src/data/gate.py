"""Gate.io market data for OOS calibration and execution modeling.

See docs/DATA_POLICY.md. If history insufficient → INSUFFICIENT_GATE_HISTORY.
"""

from qtb.data.candles import fetch_candles, load_cache  # noqa: F401
from qtb.data.funding import fetch_funding_cached  # noqa: F401
from qtb.data.contracts import fetch_contract_spec  # noqa: F401

RAW_ROOT = "data/raw/gate"


class InsufficientGateHistory(Exception):
    """Raised when Gate cannot supply required history for execution claims."""
