"""Config / CLI overlay tests — no tick download."""

from __future__ import annotations

from pathlib import Path

from src.analysis.soxl_grid_cli import GridSpec, apply_cli, build_parser, spec_from_yaml


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
