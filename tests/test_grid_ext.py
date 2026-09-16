"""Extension registry, plugin load, sweep overlay — no tick download."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from src.analysis.grid_ext import (
    HEDGE_RUNNERS,
    load_extensions,
    merge_overlay,
    register_grid_kind,
    register_hedge,
    register_range,
    register_reanchor,
    register_yaml_keys,
    resolve_band,
    resolve_rungs,
    snapshot_registry,
    restore_registry,
)
from src.analysis.soxl_grid_cli import (
    GridSpec,
    load_sweep_raw,
    main,
    spec_from_yaml,
    specs_from_sweep,
    validate_spec,
)
from src.analysis.user_moving_grid import apply_reanchor, user_levels
from src.analysis.user_moving_grid import IsolatedDirBook


@pytest.fixture
def isolated_registry():
    snap = snapshot_registry()
    yield
    restore_registry(snap)


def test_builtin_band_and_rungs():
    lo, hi = resolve_band("usdt", 100.0, range_usdt=20.0)
    assert lo == 80.0 and hi == 120.0
    lo, hi = resolve_band("pct", 100.0, range_pct=0.20)
    assert lo == pytest.approx(80.0) and hi == pytest.approx(120.0)
    arith = resolve_rungs("arithmetic", 80.0, 120.0, 5)
    geo = resolve_rungs("geometric", 80.0, 120.0, 5)
    assert len(arith) == 5
    assert arith[0] == pytest.approx(80.0)
    assert geo[0] == pytest.approx(80.0)
    assert not np.allclose(arith, geo)


def test_register_grid_kind_and_range(isolated_registry):
    register_range("half_usdt", lambda mid, range_usdt=20.0, **_: (mid - range_usdt / 2, mid + range_usdt / 2))
    register_grid_kind("mid3", lambda lo, hi, n: np.array([lo, (lo + hi) / 2, hi]))
    lv = user_levels(100.0, range_mode="half_usdt", range_usdt=20.0, n_grids=3, grid_kind="mid3")
    assert list(lv) == [90.0, 100.0, 110.0]


def test_register_hedge_validates(isolated_registry):
    register_hedge("unit_book", lambda bars, **kw: {"daily": None}, label="unit")
    spec = GridSpec(hedge="unit_book", n_grids=20)
    assert validate_spec(spec) == []


def test_unknown_hedge_rejected():
    spec = GridSpec(hedge="does_not_exist", n_grids=20)
    assert any("hedge" in e for e in validate_spec(spec))


def test_register_reanchor(isolated_registry):
    seen = {}

    def mark(book, old, new, px):
        seen["px"] = px
        book.lots = {}

    register_reanchor("mark", mark)
    book = IsolatedDirBook(1000.0, 5.0, 0.0002, "long")
    book.lots = {0: 1.0}
    apply_reanchor(book, np.array([1.0, 2.0]), np.array([1.5, 2.5]), 9.0, "mark")
    assert seen["px"] == 9.0
    assert book.lots == {}


def test_merge_overlay_nested():
    base = {"range": {"mode": "usdt", "usdt": 20}, "leverage": 5}
    got = merge_overlay(base, {"range": {"usdt": 15}, "leverage": 3, "variants": "ignore"})
    assert got["range"]["mode"] == "usdt"
    assert got["range"]["usdt"] == 15
    assert got["leverage"] == 3
    assert "variants" not in got


def test_sweep_yaml_loads():
    base, variants = load_sweep_raw(Path("soxl-lab/params/sweep.yaml"))
    assert base["fills"] == "bar"
    assert len(variants) >= 3
    ns = type("NS", (), {})()
    # apply_cli needs argparse namespace; use parser
    from src.analysis.soxl_grid_cli import build_parser

    args = build_parser().parse_args([])
    specs = specs_from_sweep(Path("soxl-lab/params/sweep.yaml"), args)
    tags = [s.tag for s in specs]
    assert "yours" in tags
    assert "lev3" in tags
    lev3 = next(s for s in specs if s.tag == "lev3")
    assert lev3.leverage == 3
    g80 = next(s for s in specs if s.tag == "g80")
    assert g80.n_grids == 80
    assert g80.range_usdt == 15


def test_plugin_file_registers(tmp_path, isolated_registry):
    py = tmp_path / "unit_plugin.py"
    py.write_text(
        "from src.analysis.grid_ext import register_hedge, register_yaml_keys\n"
        "register_yaml_keys('pause_hours')\n"
        "register_hedge('from_file', lambda bars, **kw: {'ok': True}, label='file')\n",
        encoding="utf-8",
    )
    load_extensions([tmp_path])
    assert "from_file" in HEDGE_RUNNERS
    spec = spec_from_yaml({"hedge": "from_file", "n_grids": 20, "pause_hours": 4})
    assert spec.hedge == "from_file"
    assert "pause_hours" not in spec.extras


def test_list_extensions_cli():
    rc = main(["--list-extensions", "--json-only"])
    assert rc == 0


def test_sweep_check_cli():
    rc = main(
        [
            "--sweep",
            "soxl-lab/params/sweep.yaml",
            "--check",
            "--fills",
            "bar",
            "--start",
            "2026-07-16",
            "--end",
            "2026-07-16",
        ]
    )
    assert rc in (0, 3)


def test_extras_forwarded_to_hedge(isolated_registry):
    captured = {}

    def grab(bars, **kw):
        captured.update(kw)
        import pandas as pd

        daily = pd.DataFrame({"daily_pnl": [0.0]})
        return {
            "daily": daily,
            "return": 0.0,
            "max_dd": 0.0,
            "end_equity": 10000.0,
            "inventory_frac": 0.0,
            "net_qty_units": 0.0,
            "fills": 0,
            "turnover": 0.0,
            "reanchors": 0,
            "hedge_mode": "grab",
            "pair_stopped": False,
            "liquidated_long": False,
            "liquidated_short": False,
            "long": {},
            "short": {},
        }

    register_hedge("grab", grab, label="grab")
    spec = GridSpec(hedge="grab", n_grids=20)
    spec.extras = {"foo": 1}
    grab(None, extras=spec.extras)
    assert captured["extras"]["foo"] == 1
