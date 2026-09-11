"""Tick-accurate spot moving grid + official deals helpers (no network)."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from qtb.config import load_config
from qtb.data.gatedata import (
    audit_deals_tape,
    deals_url,
    generate_sample_deals,
    month_range,
    parse_deals_csv,
)
from qtb.engine.backtest import run_backtest
from qtb.engine.spot_grid import run_spot_moving_grid
from qtb.strategies.moving_grid import (
    DEFAULT_ETF_3X,
    bar_touch_path,
    build_moving_levels,
    count_pct_crosses,
    remap_lots_shift_down,
    remap_lots_shift_up,
    resolve_etf_markets,
    shift_levels,
)


def _cfg(**overrides):
    cfg = load_config("configs/backtest_etf_moving_grid.yaml")
    cfg["prefer_sample"] = True
    cfg["feed"] = "deals"
    strat = cfg.setdefault("strategy", {})
    strat["grid_count"] = 8
    strat["spacing_pct"] = 0.01
    strat["range_up_pct"] = None
    strat["range_down_pct"] = None
    strat["spacing_mode"] = "geometric"
    strat["quote_capital"] = 800.0
    strat["order_size_quote"] = 100.0
    cfg.setdefault("risk", {})["investment_sl_pct"] = None
    cfg["risk"]["max_drawdown_stop_pct"] = None
    cfg.update(overrides)
    return cfg


def _tape(prices, start=1_720_000_000.0):
    rows = []
    for i, px in enumerate(prices):
        rows.append(
            {
                "timestamp": pd.to_datetime(start + i, unit="s", utc=True),
                "dealid": i + 1,
                "price": float(px),
                "amount": 20.0,
                "side": "buy" if i % 2 == 0 else "sell",
            }
        )
    df = pd.DataFrame(rows)
    df.attrs["feed"] = "deals"
    return df


def test_resolve_etf_markets_families_and_raw_pairs():
    soxl_snxx = resolve_etf_markets("soxl,snxx")
    assert soxl_snxx[0] == "SOXL3L_USDT"
    assert soxl_snxx[1] == "SOXL3S_USDT"
    assert "SNXX3L_USDT" in soxl_snxx
    assert "SNXX3S_USDT" in soxl_snxx
    assert "ETH3L_USDT" in resolve_etf_markets("eth")
    assert resolve_etf_markets("SOXL3L_USDT") == ["SOXL3L_USDT"]
    assert DEFAULT_ETF_3X == (
        "SOXL3L_USDT",
        "SOXL3S_USDT",
        "SNXX3L_USDT",
        "SNXX3S_USDT",
    )


def test_month_range_and_deals_url():
    assert month_range("2026-06", "2026-08") == ["202606", "202607", "202608"]
    assert deals_url("ETH3L_USDT", "202608").endswith("/spot/deals/202608/ETH3L_USDT-202608.csv.gz")


def test_parse_deals_csv_gate_layout():
    text = "1782378219.672023,1,1.00644,33.68,2\n1782378277.5,2,1.01032,1.01,1\n"
    df = parse_deals_csv(text)
    assert len(df) == 2
    assert df.iloc[0]["side"] == "buy"
    assert df.iloc[1]["side"] == "sell"
    assert float(df.iloc[0]["price"]) == pytest.approx(1.00644)


def test_parse_official_announcement_sample_row():
    # Gate announcement: timestamp, dealid, price, amount, side
    text = "1577830575.771538,215782675,0.032900,500.000000,1\n"
    df = parse_deals_csv(text)
    assert float(df.iloc[0]["price"]) == pytest.approx(0.0329)
    assert float(df.iloc[0]["amount"]) == pytest.approx(500.0)
    assert int(df.iloc[0]["dealid"]) == 215782675
    assert df.iloc[0]["side"] == "sell"
    audit = audit_deals_tape(df)
    assert audit["tape_ok"] is True
    assert audit["n_prints"] == 1


def test_count_pct_crosses_up_and_down():
    # 0.5% geometric stairs: 100 → 100.5 → 101.0025 is two up-crosses.
    ups = [100.0 * (1.005**k) for k in range(0, 6)]
    got = count_pct_crosses(ups, 0.005)
    assert got["up_crosses"] == 5
    assert got["down_crosses"] == 0
    downs = [100.0 / (1.005**k) for k in range(0, 6)]
    got = count_pct_crosses(downs, 0.005)
    assert got["down_crosses"] == 5
    assert got["up_crosses"] == 0


def test_plus_minus_5pct_twenty_arithmetic_grids():
    lv = build_moving_levels(
        100.0, 20, mode="arithmetic", range_up_pct=0.05, range_down_pct=0.05
    )
    assert len(lv) == 21
    assert lv[0] == pytest.approx(95.0)
    assert lv[-1] == pytest.approx(105.0)
    assert float(lv[1] - lv[0]) == pytest.approx(0.5)


def test_levels_shift_and_lot_remap():
    lv = build_moving_levels(100.0, 4, 0.01, "geometric")
    assert len(lv) == 5
    up = shift_levels(lv, "up", 0.01, "geometric")
    assert up[0] == pytest.approx(lv[0] * 1.01)
    lots, left = remap_lots_shift_up({0: 2.0, 2: 3.0})
    assert left == pytest.approx(2.0)
    assert lots == {1: 3.0}
    lots, left = remap_lots_shift_down({0: 1.0, 3: 4.0}, max_buy_idx=3)
    assert left == pytest.approx(4.0)
    assert lots == {1: 1.0}


def test_grid_harvest_uses_rung_cost_not_portfolio_average():
    """A completed grid must credit sell − that buy, even if another lot is cheaper."""
    cfg = _cfg()
    cfg["strategy"]["grid_count"] = 8
    cfg["strategy"]["spacing_pct"] = 0.01
    cfg["strategy"]["order_size_quote"] = 100.0
    # Stay inside the 8×1% band (~96.06–104.06): 98 fills, 99.1 sells that rung.
    tape = _tape([100.0, 98.0, 99.1])
    result = run_spot_moving_grid(cfg, tape)
    sells = [t for t in result.trades if t.reason == "grid_sell_tp"]
    assert sells, "expected at least one completed grid rung"
    assert result.metrics["grid_harvest"] == pytest.approx(
        sum(t.realized_pnl for t in sells), abs=1e-3
    )
    # Harvest must be positive on a +1% geometric rung after tiny maker fees.
    assert result.metrics["grid_harvest"] > 0
    assert result.metrics.get("halted") is False


def test_no_drawdown_halt_by_default():
    cfg = _cfg()
    # Crash then grind — without a stop the robot keeps shifting.
    prices = [100.0] + [70.0] * 5 + [70.0 + i * 2.0 for i in range(20)]
    result = run_spot_moving_grid(cfg, _tape(prices))
    assert result.metrics.get("halted") is False
    assert result.metrics.get("stop_outs", 0) == 0


def test_tick_tape_buy_then_sell_round_trip():
    # 8 geometric 1% grids around 100. A print at 96 fills a lower buy;
    # a later print at 104 fills the +1 grid sell.
    tape = _tape([100.0, 96.0, 96.0, 104.0, 104.0])
    result = run_spot_moving_grid(_cfg(), tape)
    sides = [t.side for t in result.trades]
    assert "buy" in sides
    assert "sell" in sides
    assert result.metrics["num_trades"] >= 2
    assert result.metrics["feed"] == "deals"


def test_band_recenters_on_exit_and_leftover_tp_is_percent():
    cfg = _cfg()
    cfg["strategy"]["grid_count"] = 20
    cfg["strategy"]["range_up_pct"] = 0.05
    cfg["strategy"]["range_down_pct"] = 0.05
    cfg["strategy"]["spacing_mode"] = "arithmetic"
    cfg["strategy"]["spacing_pct"] = None
    cfg["strategy"]["quote_capital"] = 2000.0
    cfg["strategy"]["order_size_quote"] = 100.0
    # Dip fills 97, then 94 leaves the 95–105 band. Frozen opening step is +0.5;
    # percent TP for the 97 lot is 97*1.005=97.485. A print at 97.49 sells only the latter.
    prices = [100.0, 97.0, 94.0, 97.49]
    result = run_spot_moving_grid(cfg, _tape(prices))
    assert result.metrics["grid_shifts"] >= 1
    sells = [t for t in result.trades if t.side == "sell"]
    assert sells
    assert any(96.9 < t.price < 98.0 for t in sells)


def test_uptrend_shifts_window_without_wick_invention():
    # Monotone up prints: no dip, so few/no buys; window must slide up.
    prices = [100.0 + i * 1.2 for i in range(40)]
    result = run_spot_moving_grid(_cfg(), _tape(prices))
    assert result.metrics["grid_shifts"] >= 1


def test_same_print_does_not_fill_orders_hung_after_shift():
    cfg = _cfg()
    cfg["strategy"]["grid_count"] = 4
    cfg["strategy"]["spacing_pct"] = 0.01
    # Jump from mid to far above the top in one print: shift happens after fills.
    tape = _tape([100.0, 130.0])
    result = run_spot_moving_grid(cfg, tape)
    # The 130 print may fill existing sells (none yet) then shift; no buy at 130.
    assert all(t.reason != "grid_buy" or t.price < 120 for t in result.trades)


def test_ohlc_wick_path_invents_a_touch_the_tape_never_printed():
    """Document why feed=deals is required: candle paths invent fills."""
    o, h, l, c = 100.0, 102.0, 98.0, 101.0
    path = bar_touch_path(o, h, l, c)
    assert 98.0 in path  # wick
    tape = _tape([100.0, 101.0, 102.0, 101.0])  # never printed 98
    assert 98.0 not in set(tape["price"])
    result = run_spot_moving_grid(_cfg(), tape)
    assert all(t.price != pytest.approx(98.0) for t in result.trades)


def test_run_backtest_rejects_candles_for_moving_grid():
    cfg = _cfg()
    candles = pd.DataFrame(
        {
            "timestamp": pd.date_range("2026-01-01", periods=8, freq="h", tz="UTC"),
            "open": 100.0,
            "high": 101.0,
            "low": 99.0,
            "close": 100.5,
        }
    )
    with pytest.raises(ValueError, match="tick-accurate"):
        run_backtest(cfg, candles)


def test_generate_sample_deals_roundtrip(tmp_path: Path):
    path = tmp_path / "sample.csv"
    df = generate_sample_deals(path, n=50, mid=1.2)
    assert path.exists()
    assert len(df) == 50
    assert df.attrs.get("feed") == "deals"


def test_opening_print_does_not_buy_through_the_market():
    cfg = _cfg()
    cfg["strategy"]["grid_count"] = 20
    cfg["strategy"]["range_up_pct"] = 0.05
    cfg["strategy"]["range_down_pct"] = 0.05
    cfg["strategy"]["spacing_mode"] = "arithmetic"
    cfg["strategy"]["spacing_pct"] = None
    result = run_spot_moving_grid(cfg, _tape([100.0, 100.0, 100.01, 99.99]))
    assert result.trades == []
    assert result.metrics["grid_harvest"] == 0
    assert abs(result.metrics["pnl_identity_gap"]) < 1e-6


def test_dip_fills_only_buy_levels_at_or_below_print():
    cfg = _cfg()
    cfg["strategy"]["grid_count"] = 20
    cfg["strategy"]["range_up_pct"] = 0.05
    cfg["strategy"]["range_down_pct"] = 0.05
    cfg["strategy"]["spacing_mode"] = "arithmetic"
    cfg["strategy"]["spacing_pct"] = None
    cfg["strategy"]["quote_capital"] = 2000.0
    cfg["strategy"]["order_size_quote"] = 100.0
    result = run_spot_moving_grid(cfg, _tape([100.0, 97.0]))
    buys = [t for t in result.trades if t.side == "buy"]
    assert buys
    assert all(t.price < 100.0 for t in buys)
    assert all(t.price >= 97.0 - 1e-9 for t in buys)
    assert all(t.price <= 99.5 + 1e-9 for t in buys)


def test_harvest_identity_matches_equity_on_sample_tape():
    cfg = _cfg()
    tape = generate_sample_deals(n=240, mid=1.0, amp=0.02)
    result = run_spot_moving_grid(cfg, tape)
    assert result.metrics["tape_ok"] is True
    assert abs(result.metrics["pnl_identity_gap"]) < 0.05
    rounds = int(result.metrics["grid_rounds_tp"]) + int(result.metrics["grid_rounds_leftover"])
    if rounds:
        assert result.metrics["avg_harvest_per_round"] == pytest.approx(
            result.metrics["grid_income"] / rounds, rel=1e-4
        )


def test_yaml_defaults_are_spot_tick_grid():
    cfg = load_config("configs/backtest_etf_moving_grid.yaml")
    assert cfg["feed"] == "deals"
    assert cfg["market"] == "spot"
    assert cfg["strategy"]["name"] == "moving_grid"
    assert int(cfg["strategy"]["grid_count"]) == 20
    assert float(cfg["strategy"]["range_up_pct"]) == pytest.approx(0.05)
    assert float(cfg["strategy"]["range_down_pct"]) == pytest.approx(0.05)
    assert cfg["strategy"]["spacing_mode"] == "arithmetic"
    assert cfg["strategy"]["shift_on_exit"] is True
    assert cfg["risk"]["stop_if_price_breaks_range"] is False
    assert cfg["risk"]["max_drawdown_stop_pct"] in (None, 0, 0.0)
    assert cfg["risk"]["investment_sl_pct"] in (None, 0, 0.0)
