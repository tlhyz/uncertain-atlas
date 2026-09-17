"""Normalize symbols and timestamps across venues."""

from src.data.binance_public import normalize_symbol as normalize_binance


def normalize_gate_symbol(symbol: str) -> str:
    s = symbol.upper().replace("/", "").replace("-", "")
    if s.endswith("_USDT"):
        return s
    if s.endswith("USDT"):
        return s.replace("USDT", "_USDT")
    return f"{s}_USDT"
