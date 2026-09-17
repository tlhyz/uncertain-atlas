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
GRID_KINDS: dict[str, Callable[..., Any]] = {}
REANCHORS: dict[str, Callable[..., None]] = {}
LOT_SIZERS: dict[str, Callable[..., float]] = {}
SPEC_VALIDATORS: list[Callable[[Any], list[str]]] = []
# Scheduler-owned keys. Plugin keys must NOT go here or they vanish from extras.
ENGINE_YAML_KEYS: set[str] = {
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
    "sizer",
    "lot_sizer",
    "note",
    "notes",
    "extends",
    "base",
    "variants",
}
PLUGIN_YAML_KEYS: set[str] = set()
# Union for --check / docs. register_yaml_keys only adds to PLUGIN_YAML_KEYS.
KNOWN_YAML_KEYS: set[str] = set(ENGINE_YAML_KEYS)
_ENGINE_YAML_KEYS_DEFAULT = frozenset(ENGINE_YAML_KEYS)

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
    """Mark YAML keys as plugin-owned. They stay in extras and --check stops calling them unknown."""
    for k in keys:
        PLUGIN_YAML_KEYS.add(str(k))
        KNOWN_YAML_KEYS.add(str(k))


def register_sizer(name: str, fn: Callable[..., float]) -> None:
    LOT_SIZERS[str(name)] = fn


def register_validator(fn: Callable[[Any], list[str]]) -> None:
    SPEC_VALIDATORS.append(fn)


def listed_hedges() -> list[str]:
    return sorted(HEDGE_RUNNERS)


def listed_ranges() -> list[str]:
    return sorted(RANGE_BANDS)


def listed_grid_kinds() -> list[str]:
    return sorted(GRID_KINDS)


def listed_reanchors() -> list[str]:
    return sorted(set(BUILTIN_REANCHORS) | set(REANCHORS))


def listed_sizers() -> list[str]:
    return sorted(LOT_SIZERS)


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


def resolve_rungs(
    grid_kind: str,
    lo: float,
    hi: float,
    n: int,
    extras: dict[str, Any] | None = None,
) -> np.ndarray:
    fn = GRID_KINDS.get(str(grid_kind))
    if fn is None:
        raise ValueError(f"unknown grid_kind {grid_kind}; registered={listed_grid_kinds()}")
    extras = extras or {}
    try:
        out = fn(float(lo), float(hi), int(n), extras=extras)
    except TypeError:
        out = fn(float(lo), float(hi), int(n))
    return np.asarray(out, dtype=float)


def resolve_notional(
    sizer: str,
    *,
    capital: float,
    leverage: float,
    n_grids: int,
    level_idx: int = 0,
    extras: dict[str, Any] | None = None,
    direction: str = "long",
) -> float:
    fn = LOT_SIZERS.get(str(sizer))
    if fn is None:
        raise ValueError(f"unknown sizer {sizer}; registered={listed_sizers()}")
    out = fn(
        capital=float(capital),
        leverage=float(leverage),
        n_grids=int(n_grids),
        level_idx=int(level_idx),
        extras=extras or {},
        direction=str(direction),
    )
    return max(float(out), 1.0)


def run_validators(spec: Any) -> list[str]:
    errs: list[str] = []
    for fn in SPEC_VALIDATORS:
        try:
            errs.extend(fn(spec) or [])
        except Exception as e:  # plugin validator must not kill --check
            errs.append(f"validator {getattr(fn, '__name__', fn)}: {e}")
    return errs


def snapshot_registry() -> dict[str, Any]:
    return {
        "hedge": dict(HEDGE_RUNNERS),
        "labels": dict(HEDGE_LABELS),
        "range": dict(RANGE_BANDS),
        "grid_kind": dict(GRID_KINDS),
        "reanchor": dict(REANCHORS),
        "sizer": dict(LOT_SIZERS),
        "validators": list(SPEC_VALIDATORS),
        "yaml_keys": set(KNOWN_YAML_KEYS),
        "engine_yaml_keys": set(ENGINE_YAML_KEYS),
        "plugin_yaml_keys": set(PLUGIN_YAML_KEYS),
    }


def restore_registry(snap: dict[str, Any]) -> None:
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
    LOT_SIZERS.clear()
    LOT_SIZERS.update(snap.get("sizer") or {})
    SPEC_VALIDATORS.clear()
    SPEC_VALIDATORS.extend(snap.get("validators") or [])
    KNOWN_YAML_KEYS.clear()
    KNOWN_YAML_KEYS.update(snap["yaml_keys"])
    ENGINE_YAML_KEYS.clear()
    ENGINE_YAML_KEYS.update(snap.get("engine_yaml_keys") or _ENGINE_YAML_KEYS_DEFAULT)
    PLUGIN_YAML_KEYS.clear()
    PLUGIN_YAML_KEYS.update(snap.get("plugin_yaml_keys") or set())


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


def _sizer_equal(
    *,
    capital: float,
    leverage: float,
    n_grids: int,
    level_idx: int = 0,
    extras: dict | None = None,
    **_: Any,
) -> float:
    return max(float(capital) * float(leverage) / max(int(n_grids), 1), 1.0)


def _sizer_fixed(
    *,
    extras: dict | None = None,
    **_: Any,
) -> float:
    extras = extras or {}
    return max(float(extras.get("lot_usdt", extras.get("notional_per_rung", 50.0))), 1.0)


def _sizer_martingale(
    *,
    capital: float,
    leverage: float,
    n_grids: int,
    level_idx: int = 0,
    extras: dict | None = None,
    direction: str = "long",
    **_: Any,
) -> float:
    extras = extras or {}
    ratio = float(extras.get("martingale_ratio", extras.get("lot_ratio", 1.2)))
    if ratio <= 0:
        raise ValueError("martingale_ratio 必须 > 0")
    n = max(int(n_grids), 1)
    base = float(capital) * float(leverage) / n
    if str(direction) == "short":
        k = int(level_idx)
    else:
        k = max(n - 1 - int(level_idx), 0)
    return max(base * (ratio ** k), 1.0)


register_range("usdt", _band_usdt)
register_range("pct", _band_pct)
register_grid_kind("arithmetic", _rungs_arithmetic)
register_grid_kind("geometric", _rungs_geometric)
register_sizer("equal", _sizer_equal)
register_sizer("fixed", _sizer_fixed)
register_sizer("martingale", _sizer_martingale)
register_yaml_keys("martingale_ratio", "lot_ratio", "lot_usdt", "notional_per_rung")


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
        "sizer": listed_sizers(),
        "plugin_yaml_keys": sorted(PLUGIN_YAML_KEYS),
        "plugin_files": loaded_extension_files(),
        "plugin_errors": extension_errors(),
        "ext_dirs": [str(p) for p in extension_dirs()],
    }
