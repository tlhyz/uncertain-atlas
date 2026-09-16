"""Extension registry for the SOXL moving-grid runner.

YAML/CLI knobs stay in GridSpec. Anything that is not a number — a new hedge
book, a new rung spacing, a new band definition, a new reanchor — registers
here (or drops a file in soxl-lab/extensions/) so the scheduler does not change.
"""

from __future__ import annotations

import importlib.util
import os
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXT_DIR = ROOT / "soxl-lab" / "extensions"

HEDGE_RUNNERS: dict[str, Callable[..., Any]] = {}
HEDGE_LABELS: dict[str, str] = {}
RANGE_BANDS: dict[str, Callable[..., tuple[float, float]]] = {}
GRID_KINDS: dict[str, Callable[[float, float, int], Any]] = {}
REANCHORS: dict[str, Callable[..., None]] = {}
KNOWN_YAML_KEYS: set[str] = {
    "symbol",
    "venue",
    "leverage",
    "n_grids",
    "grid_kind",
    "moving",
    "capital_long",
    "capital_short",
    "capital_per_side",
    "capital_per_side_usdt",
    "sides",
    "side",
    "range",
    "range_mode",
    "range_modes",
    "hedge",
    "fee",
    "fee_bps",
    "fills",
    "tag",
    "window",
    "start",
    "end",
    "reanchor",
    "mmr",
    "mmr_frac",
    "note",
    "notes",
    "extends",
    "base",
    "variants",
}

BUILTIN_REANCHORS = ("remap", "drop_lots", "flatten")

_DEFAULT_LOADED = False
_LOADED_FILES: list[str] = []
_EXT_ERRORS: list[str] = []


def register_hedge(name: str, fn: Callable[..., Any], *, label: str | None = None) -> None:
    key = str(name)
    HEDGE_RUNNERS[key] = fn
    HEDGE_LABELS[key] = label or key


def register_range(name: str, fn: Callable[..., tuple[float, float]]) -> None:
    RANGE_BANDS[str(name)] = fn


def register_grid_kind(name: str, fn: Callable[[float, float, int], Any]) -> None:
    GRID_KINDS[str(name)] = fn


def register_reanchor(name: str, fn: Callable[..., None]) -> None:
    REANCHORS[str(name)] = fn


def register_yaml_keys(*keys: str) -> None:
    KNOWN_YAML_KEYS.update(str(k) for k in keys)


def listed_hedges() -> list[str]:
    return sorted(HEDGE_RUNNERS)


def listed_ranges() -> list[str]:
    return sorted(RANGE_BANDS)


def listed_grid_kinds() -> list[str]:
    return sorted(GRID_KINDS)


def listed_reanchors() -> list[str]:
    return sorted(set(BUILTIN_REANCHORS) | set(REANCHORS))


def resolve_band(
    range_mode: str,
    mid: float,
    *,
    range_usdt: float = 20.0,
    range_pct: float = 0.20,
    extras: dict[str, Any] | None = None,
) -> tuple[float, float]:
    fn = RANGE_BANDS.get(str(range_mode))
    if fn is None:
        raise ValueError(f"unknown range_mode {range_mode}; registered={listed_ranges()}")
    return fn(float(mid), range_usdt=range_usdt, range_pct=range_pct, extras=extras or {})


def resolve_rungs(grid_kind: str, lo: float, hi: float, n: int) -> np.ndarray:
    fn = GRID_KINDS.get(str(grid_kind))
    if fn is None:
        raise ValueError(f"unknown grid_kind {grid_kind}; registered={listed_grid_kinds()}")
    return np.asarray(fn(float(lo), float(hi), int(n)), dtype=float)


def snapshot_registry() -> dict[str, dict]:
    return {
        "hedge": dict(HEDGE_RUNNERS),
        "labels": dict(HEDGE_LABELS),
        "range": dict(RANGE_BANDS),
        "grid_kind": dict(GRID_KINDS),
        "reanchor": dict(REANCHORS),
        "yaml_keys": set(KNOWN_YAML_KEYS),
    }


def restore_registry(snap: dict[str, dict]) -> None:
    HEDGE_RUNNERS.clear()
    HEDGE_RUNNERS.update(snap["hedge"])
    HEDGE_LABELS.clear()
    HEDGE_LABELS.update(snap["labels"])
    RANGE_BANDS.clear()
    RANGE_BANDS.update(snap["range"])
    GRID_KINDS.clear()
    GRID_KINDS.update(snap["grid_kind"])
    REANCHORS.clear()
    REANCHORS.update(snap["reanchor"])
    KNOWN_YAML_KEYS.clear()
    KNOWN_YAML_KEYS.update(snap["yaml_keys"])


def _band_usdt(mid: float, *, range_usdt: float = 20.0, extras: dict | None = None, **_: Any) -> tuple[float, float]:
    half = float(range_usdt)
    return mid - half, mid + half


def _band_pct(mid: float, *, range_pct: float = 0.20, extras: dict | None = None, **_: Any) -> tuple[float, float]:
    p = float(range_pct)
    return mid * (1.0 - p), mid * (1.0 + p)


def _rungs_arithmetic(lo: float, hi: float, n: int) -> np.ndarray:
    return np.linspace(lo, hi, n)


def _rungs_geometric(lo: float, hi: float, n: int) -> np.ndarray:
    return np.geomspace(lo, hi, n)


register_range("usdt", _band_usdt)
register_range("pct", _band_pct)
register_grid_kind("arithmetic", _rungs_arithmetic)
register_grid_kind("geometric", _rungs_geometric)


def merge_overlay(base: dict[str, Any], overlay: dict[str, Any] | None) -> dict[str, Any]:
    """Deep-merge overlay onto base. Overlay wins. Dicts merge; lists replace."""
    out = deepcopy(base or {})
    if not overlay:
        return out
    for k, v in overlay.items():
        if k in ("variants", "extends", "base"):
            continue
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = merge_overlay(out[k], v)
        else:
            out[k] = deepcopy(v)
    return out


def extension_dirs(extra: list[Path] | None = None) -> list[Path]:
    dirs: list[Path] = []
    env = os.environ.get("SOXLLAB_EXTENSIONS", "")
    if env.strip():
        dirs.extend(Path(p).expanduser() for p in env.split(os.pathsep) if p.strip())
    dirs.append(DEFAULT_EXT_DIR)
    if extra:
        dirs.extend(Path(p) for p in extra)
    seen: set[Path] = set()
    uniq: list[Path] = []
    for d in dirs:
        try:
            key = d.resolve()
        except OSError:
            key = d
        if key in seen:
            continue
        seen.add(key)
        uniq.append(d)
    return uniq


def _import_plugin(path: Path) -> None:
    mod_name = f"soxl_lab_ext_{path.stem}"
    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)


def load_extensions(extra_dirs: list[Path] | None = None, *, reload_default: bool = False) -> list[str]:
    """Import soxl-lab/extensions/*.py (skip _*) plus SOXLLAB_EXTENSIONS and extra dirs."""
    global _DEFAULT_LOADED
    if extra_dirs is None and _DEFAULT_LOADED and not reload_default:
        return list(_LOADED_FILES)
    _EXT_ERRORS.clear()
    newly: list[str] = []
    for d in extension_dirs(extra_dirs):
        if not d.is_dir():
            continue
        if d.resolve() == DEFAULT_EXT_DIR.resolve() and _DEFAULT_LOADED and not reload_default and extra_dirs:
            # default already in; still scan extra
            continue
        for py in sorted(d.glob("*.py")):
            if py.name.startswith("_"):
                continue
            key = str(py.resolve())
            if key in _LOADED_FILES and extra_dirs is None:
                continue
            try:
                _import_plugin(py)
            except Exception as e:  # plugin must not kill the runner
                _EXT_ERRORS.append(f"{py}: {e}")
                continue
            if key not in _LOADED_FILES:
                _LOADED_FILES.append(key)
            newly.append(key)
    _DEFAULT_LOADED = True
    return newly


def extension_errors() -> list[str]:
    return list(_EXT_ERRORS)


def loaded_extension_files() -> list[str]:
    return list(_LOADED_FILES)


def describe_extensions() -> dict[str, Any]:
    return {
        "hedge": {k: HEDGE_LABELS.get(k, k) for k in listed_hedges()},
        "range_mode": listed_ranges(),
        "grid_kind": listed_grid_kinds(),
        "reanchor": listed_reanchors(),
        "plugin_files": loaded_extension_files(),
        "plugin_errors": extension_errors(),
        "ext_dirs": [str(p) for p in extension_dirs()],
    }
