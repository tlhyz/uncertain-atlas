"""Market data: candles (disk cache + incremental), funding, contract specs."""

from .candles import (
    CACHE_DIR,
    SAMPLE_CSV,
    WS_FUTURES_TRADES_DOC,
    api_stats,
    cache_path,
    encode_contract_for_url,
    fetch_candles_cached,
    fetch_gate_futures_candles,
    fetch_gate_futures_tickers,
    fetch_gate_futures_trades,
    fetch_ohlcv,
    generate_sample_ohlcv,
    load_csv,
    normalize_contract,
    reset_api_stats,
    resolve_gate_futures_contract,
)
from .contracts import ContractSpec, fetch_contract_spec
from .funding import fetch_funding_cached, load_funding_csv, synthetic_funding

__all__ = [
    "CACHE_DIR",
    "SAMPLE_CSV",
    "WS_FUTURES_TRADES_DOC",
    "api_stats",
    "cache_path",
    "encode_contract_for_url",
    "fetch_candles_cached",
    "fetch_gate_futures_candles",
    "fetch_gate_futures_tickers",
    "fetch_gate_futures_trades",
    "fetch_ohlcv",
    "generate_sample_ohlcv",
    "load_csv",
    "normalize_contract",
    "reset_api_stats",
    "resolve_gate_futures_contract",
    "ContractSpec",
    "fetch_contract_spec",
    "fetch_funding_cached",
    "load_funding_csv",
    "synthetic_funding",
]
