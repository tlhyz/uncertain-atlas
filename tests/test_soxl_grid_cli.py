"""Config / CLI overlay tests — no tick download."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.analysis.soxl_grid_cli import (
    DEFAULT_CONFIG,
    DEFAULT_OUT,
    ROOT,
    GridSpec,
    apply_cli,
    build_parser,
    load_yaml,
    main,
    spec_from_yaml,
    validate_spec,
    window_missing_ticks,
)


def test_yaml_round_defaults():
    spec = spec_from_yaml(
        {
            "symbol": "SOXLUSDT",
            "window": {"start": "2026-07-16", "end": "2026-09-11"},
            "leverage": 5,
            "n_grids": 200,
            "capital_long": 5000,
            "capital_short": 5000,
            "range": {"mode": "usdt", "usdt": 20, "pct": 0.2},
            "hedge": "flatten_survivor",
            "fee": "base",
            "fills": "tick",
        }
    )
    assert spec.leverage == 5
    assert spec.n_grids == 200
    assert spec.range_usdt == 20
    assert spec.hedge == "flatten_survivor"
    assert "usdt20" in spec.folder_name()
    assert "lev5" in spec.folder_name()
    assert "20260716-20260911" in spec.folder_name()


def test_cli_overrides_yaml(tmp_path: Path):
    spec = GridSpec()
    ns = build_parser().parse_args(
        ["--leverage", "3", "--n-grids", "80", "--range-usdt", "15", "--mode", "usdt", "--capital", "2000"]
    )
    got = apply_cli(spec, ns)
    assert got.leverage == 3
    assert got.n_grids == 80
    assert got.range_usdt == 15
    assert got.capital_long == 2000
    assert got.capital_short == 2000


def test_default_run_yaml_exists():
    assert Path("soxl-lab/params/run.yaml").exists()
    assert ROOT.name != "src"
    assert DEFAULT_CONFIG.exists()
    assert DEFAULT_OUT == ROOT / "soxl-lab" / "results" / "runs"


def test_yaml_zero_not_swallowed():
    spec = spec_from_yaml({"leverage": 0, "n_grids": 200})
    assert spec.leverage == 0
    errs = validate_spec(spec)
    assert any("leverage" in e for e in errs)


def test_yours_draft_yaml_loads():
    spec = spec_from_yaml(
        {
            "symbol": "SOXLUSDT",
            "leverage": 5,
            "n_grids": 200,
            "capital_per_side_usdt": 5000,
            "sides": {"long": 5000, "short": 4000},
            "range_modes": {"usdt": {"range_usdt": 20}, "pct": {"range_pct": 0.20}},
            "fee": {"base_bps": 2, "conservative_bps": 4},
            "fills": "tick_precise_aggTrades",
            "window": {"start": "2026-07-16", "end": "2026-09-11"},
        }
    )
    assert spec.capital_long == 5000
    assert spec.capital_short == 4000
    assert spec.range_usdt == 20
    assert spec.range_pct == 0.20
    assert spec.n_grids == 200
    assert spec.fills == "tick"
    assert spec.fee == "base"
    assert validate_spec(spec) == []


def test_real_yours_yaml_file_validates():
    spec = spec_from_yaml(load_yaml(Path("soxl-lab/params/01_yours_moving_grid.yaml")))
    assert spec.symbol == "SOXLUSDT"
    assert spec.fills == "tick"
    assert spec.fee == "base"
    assert spec.n_grids == 200
    assert validate_spec(spec) == []


def test_validate_start_after_end():
    spec = GridSpec(start="2026-09-11", end="2026-07-16")
    assert any("晚于" in e for e in validate_spec(spec))


def test_validate_n_grids():
    spec = GridSpec(n_grids=1)
    assert any("n_grids" in e for e in validate_spec(spec))


def test_help_lists_check_and_cache():
    help_txt = build_parser().format_help()
    assert "--list-cache" in help_txt
    assert "--check" in help_txt
    assert "--sides" in help_txt


def test_check_future_window_reports_missing():
    spec = GridSpec(start="2099-01-01", end="2099-01-03", fills="tick")
    miss = window_missing_ticks(spec)
    assert miss == ["2099-01-01", "2099-01-02", "2099-01-03"]


def test_main_check_json_on_default_window():
    rc = main(["--check", "--json-only", "--start", "2026-07-16", "--end", "2026-07-16"])
    assert rc in (0, 3)  # 0 if that day is cached on this machine


def test_main_check_bar_ignores_missing_ticks():
    rc = main(["--check", "--fills", "bar", "--start", "2099-01-01", "--end", "2099-01-02"])
    assert rc == 0


def test_main_check_tick_rejects_missing():
    rc = main(["--check", "--fills", "tick", "--start", "2099-01-01", "--end", "2099-01-02"])
    assert rc == 3


def test_unknown_yaml_keys_land_in_extras():
    spec = spec_from_yaml({"leverage": 5, "n_grids": 200, "stop_loss_pct": 0.1, "foo": 1})
    assert spec.extras["stop_loss_pct"] == 0.1
    assert spec.extras["foo"] == 1
    assert validate_spec(spec) == []


def test_geometric_and_fee_bps_from_yaml():
    spec = spec_from_yaml(
        {
            "grid_kind": "geometric",
            "fee_bps": 3,
            "reanchor": "flatten",
            "mmr_frac": 0.01,
            "n_grids": 40,
            "leverage": 3,
        }
    )
    assert spec.grid_kind == "geometric"
    assert spec.fee_bps == 3
    assert spec.reanchor == "flatten"
    assert spec.mmr_frac == 0.01
    assert "geo" in spec.folder_name()
    assert validate_spec(spec) == []


def test_numeric_fee_becomes_fee_bps():
    spec = spec_from_yaml({"fee": 2.5, "n_grids": 20})
    assert spec.fee_bps == 2.5
    assert spec.fee == "base"
    assert validate_spec(spec) == []


def test_cli_sides_and_tag():
    spec = GridSpec()
    ns = build_parser().parse_args(["--sides", "long", "--tag", "probe"])
    got = apply_cli(spec, ns)
    assert got.sides == "long"
    assert got.tag == "probe"
    assert "long-only" in got.folder_name()
    assert got.folder_name().startswith("probe_")
