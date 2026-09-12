"""Fair-lens experiment matrix, walk-forward, Monte Carlo, portfolio, hybrid."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from .data import PairData, attach_funding
from .engine import EngineResult, FeeSpec, run_cash, run_perp_grid, run_spot_grid
from .fills import FillConfig
from .grids import realized_vol
from .metrics import composite_score, path_drag, rebate_value, summarize, value_add
from .regimes import slice_windows, special_masks
from .universe import long_pairs, portfolio_core

SPOT_FEE = {"maker": 0.0008, "taker": 0.00085}
FUT_FEE = {"maker": 0.00008, "taker": 0.0002}


def _fee_spot(rebate: float) -> FeeSpec:
    return FeeSpec(SPOT_FEE["maker"], SPOT_FEE["taker"], rebate)


def _fee_fut(rebate: float) -> FeeSpec:
    return FeeSpec(FUT_FEE["maker"], FUT_FEE["taker"], rebate)


def _slice(df: pd.DataFrame, i0: int, i1: int) -> pd.DataFrame:
    return df.iloc[i0:i1].reset_index(drop=True)


def _exante_beta(data: PairData, warm: int = 24) -> float:
    e = data.etf["close"].to_numpy(float)
    u = data.spot["close"].to_numpy(float)
    from .grids import rolling_beta

    b = rolling_beta(e, u, n=48)
    idx = min(max(warm - 1, 0), len(b) - 1)
    return float(b[idx])


def _exante_vols(data: PairData, warm: int = 24) -> tuple[float, float]:
    ev = realized_vol(data.etf["close"].to_numpy(float), n=24)
    uv = realized_vol(data.perp["close"].to_numpy(float), n=24)
    i = min(max(warm - 1, 0), len(ev) - 1)
    return float(max(ev[i], 1e-8)), float(max(uv[i], 1e-8))


@dataclass
class RunRow:
    pair: str
    lens: str
    side: str
    metrics: dict[str, Any]
    result: EngineResult | None = None


def run_benchmarks(data: PairData, initial: float, fill: FillConfig, interval: str) -> list[RunRow]:
    rows: list[RunRow] = []
    etf = data.etf
    spot = data.spot
    und = data.spot["close"].to_numpy(float)
    a0 = run_cash(etf, initial, "A0_cash")
    a1 = run_spot_grid(
        etf, name="A1_etf_hold", symbol=data.pair.etf_spot, fee=_fee_spot(0.70),
        fill=fill, initial=initial, hold_only=True, interval=interval, und_close=und,
    )
    b1 = run_spot_grid(
        spot, name="B1_spot_hold", symbol=data.pair.underlying_spot, fee=_fee_spot(0.70),
        fill=fill, initial=initial, hold_only=True, interval=interval,
    )
    b2 = run_spot_grid(
        spot, name="B2_spot_grid", symbol=data.pair.underlying_spot, fee=_fee_spot(0.70),
        fill=fill, initial=initial, grid_mode="native_atr", atr_step=0.40, atr_range=5.0,
        interval=interval,
    )
    for r in (a0, a1, b1, b2):
        rows.append(RunRow(data.pair.name, "benchmark", "long", summarize(r, initial), r))
    return rows


def _etf_grid(
    data: PairData,
    *,
    name: str,
    fill: FillConfig,
    rebate: float,
    dir_frac: float,
    grid_mode: str,
    interval: str,
    initial: float,
    atr_step: float = 0.40,
    static_step: float = 0.01,
    und_step: float = 0.005,
    kind: str = "geometric",
    lower_boost: float = 1.0,
    size_mode: str = "fixed_usdt",
) -> EngineResult:
    return run_spot_grid(
        data.etf,
        name=name,
        symbol=data.pair.etf_spot,
        fee=_fee_spot(rebate),
        fill=fill,
        initial=initial,
        dir_frac=dir_frac,
        grid_mode=grid_mode,
        grid_kind=kind,
        atr_step=atr_step,
        atr_range=5.0,
        static_step=static_step,
        static_range=0.18,
        und_step=und_step,
        und_range=0.15,
        und_close=data.spot["close"].to_numpy(float),
        size_mode=size_mode,  # type: ignore[arg-type]
        lower_boost=lower_boost,
        interval=interval,
    )


def _perp_grid(
    data: PairData,
    *,
    name: str,
    fill: FillConfig,
    rebate: float,
    dir_frac: float,
    target_notional: float,
    leverage: float,
    interval: str,
    initial: float,
    margin_mode: str = "isolated",
    reserve_plan: str = "P1",
    add_trigger: float = 0.15,
    grid_mode: str = "native_atr",
    atr_step: float = 0.40,
    static_step: float = 0.005,
    und_step: float = 0.005,
    kind: str = "geometric",
    direction: str = "long",
    hold_only: bool = False,
) -> EngineResult:
    bars = attach_funding(data.perp, data.funding)
    return run_perp_grid(
        bars,
        name=name,
        symbol=data.pair.perp or "",
        fee=_fee_fut(rebate),
        fill=fill,
        initial=initial,
        direction=direction,  # type: ignore[arg-type]
        target_notional=target_notional,
        dir_frac=dir_frac,
        margin_mode=margin_mode,  # type: ignore[arg-type]
        reserve_plan=reserve_plan,  # type: ignore[arg-type]
        add_trigger=add_trigger,
        mm_rate=float(data.contract.maintenance_rate),
        quanto=float(data.contract.quanto),
        min_contracts=float(data.contract.min_order_size),
        grid_mode=grid_mode,
        grid_kind=kind,
        atr_step=atr_step,
        atr_range=5.0,
        static_step=static_step,
        static_range=0.15,
        und_step=und_step,
        und_range=0.15,
        interval=interval,
        hold_only=hold_only,
        leverage_hint=leverage,
    )


def run_long_pair(data: PairData, cfg: dict[str, Any]) -> dict[str, Any]:
    initial = float(cfg.get("initial_capital") or 1000.0)
    interval = data.interval
    spot_reb = float(cfg.get("spot_rebate") or 0.70)
    fut_reb = float(cfg.get("futures_rebate") or 0.75)
    rows: list[RunRow] = []

    for mode in ("base", "conservative"):
        fill = FillConfig.preset(mode)  # type: ignore[arg-type]
        rows.extend(run_benchmarks(data, initial, fill, interval))

        # --- Fairness 1: same wallet ---
        for rebate, tag in ((spot_reb, "reb"), (0.0, "noreb")):
            for dir_f in (0.0, 0.50):
                for gmode, gkw in (
                    ("native_atr", {"atr_step": 0.40}),
                    ("underlying_equiv", {"und_step": 0.005}),
                    ("static_pct", {"static_step": 0.01}),
                ):
                    r = _etf_grid(
                        data, name=f"A2_etf_{gmode}_d{dir_f}_{tag}_{mode}",
                        fill=fill, rebate=rebate, dir_frac=dir_f, grid_mode=gmode,
                        interval=interval, initial=initial, **gkw,
                    )
                    rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))

        for lev in (1.5, 2.0, 2.5, 3.0):
            for rebate, tag in ((fut_reb, "reb"), (0.0, "noreb")):
                for dir_f in (0.0, 0.50):
                    r = _perp_grid(
                        data, name=f"B_perp_{lev}x_iso_P1_d{dir_f}_{tag}_{mode}",
                        fill=fill, rebate=rebate, dir_frac=dir_f,
                        target_notional=initial * lev, leverage=lev,
                        interval=interval, initial=initial,
                    )
                    rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))

        # extras only on base fill to control runtime
        if mode == "base":
            r = _perp_grid(
                data, name="B_perp_3x_iso_P2_reb_base", fill=fill, rebate=fut_reb,
                dir_frac=0.0, target_notional=initial * 3.0 * 0.70, leverage=3.0,
                interval=interval, initial=initial, reserve_plan="P2",
            )
            rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))
            r = _perp_grid(
                data, name="B_perp_3x_iso_P3_reb_base", fill=fill, rebate=fut_reb,
                dir_frac=0.0, target_notional=initial * 3.0 * 0.50, leverage=3.0,
                interval=interval, initial=initial, reserve_plan="P3",
            )
            rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))
            r = _perp_grid(
                data, name="B_perp_3x_cross_P1_reb_base", fill=fill, rebate=fut_reb,
                dir_frac=0.0, target_notional=initial * 3.0, leverage=3.0,
                interval=interval, initial=initial, margin_mode="cross",
            )
            rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))
            for trig in (0.20, 0.10):
                r = _perp_grid(
                    data, name=f"B_perp_3x_iso_P2_trig{trig}_base", fill=fill, rebate=fut_reb,
                    dir_frac=0.0, target_notional=initial * 3.0 * 0.70, leverage=3.0,
                    interval=interval, initial=initial, reserve_plan="P2", add_trigger=trig,
                )
                rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))
            r = _perp_grid(
                data, name="B6_perp_3x_static_base", fill=fill, rebate=fut_reb,
                dir_frac=0.0, target_notional=initial * 3.0, leverage=3.0,
                interval=interval, initial=initial, grid_mode="static_pct", static_step=0.005,
            )
            rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))
            r = _perp_grid(
                data, name="B6_hold_3x_dir", fill=fill, rebate=fut_reb,
                dir_frac=1.0, target_notional=initial * 3.0, leverage=3.0,
                interval=interval, initial=initial, hold_only=True,
            )
            rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))

        # --- Fairness 2: same initial economic exposure ---
        beta = _exante_beta(data)
        expo = initial * beta
        r = _etf_grid(
            data, name=f"A2_same_expo_{mode}", fill=fill, rebate=spot_reb,
            dir_frac=0.0, grid_mode="native_atr", interval=interval, initial=initial,
        )
        rows.append(RunRow(data.pair.name, "same_exposure", "long", {**summarize(r, initial), "exante_beta": beta, "matched_notional": expo}, r))
        r = _perp_grid(
            data, name=f"B_same_expo_{mode}", fill=fill, rebate=fut_reb,
            dir_frac=0.0, target_notional=expo, leverage=max(expo / initial, 1.0),
            interval=interval, initial=initial,
        )
        rows.append(RunRow(data.pair.name, "same_exposure", "long", {**summarize(r, initial), "exante_beta": beta, "matched_notional": expo}, r))

        # --- Fairness 3: same ex-ante vol ---
        ev, uv = _exante_vols(data)
        matched = initial * ev / uv
        r = _etf_grid(
            data, name=f"A2_same_risk_{mode}", fill=fill, rebate=spot_reb,
            dir_frac=0.0, grid_mode="native_atr", interval=interval, initial=initial,
        )
        rows.append(RunRow(data.pair.name, "same_risk", "long", {**summarize(r, initial), "etf_vol": ev, "und_vol": uv, "matched_notional": matched}, r))
        r = _perp_grid(
            data, name=f"B_same_risk_{mode}", fill=fill, rebate=fut_reb,
            dir_frac=0.0, target_notional=matched, leverage=max(matched / initial, 1.0),
            interval=interval, initial=initial,
        )
        rows.append(RunRow(data.pair.name, "same_risk", "long", {**summarize(r, initial), "etf_vol": ev, "und_vol": uv, "matched_notional": matched}, r))

    if data.pair.name == "SOL":
        fill = FillConfig.preset("base")
        r = _etf_grid(
            data, name="A2_etf_arithmetic", fill=fill, rebate=spot_reb, dir_frac=0.0,
            grid_mode="native_atr", interval=interval, initial=initial, kind="arithmetic",
        )
        rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))
        r = _etf_grid(
            data, name="A2_etf_voladj_boost15", fill=fill, rebate=spot_reb, dir_frac=0.0,
            grid_mode="native_atr", interval=interval, initial=initial,
            size_mode="vol_adj", lower_boost=1.5,
        )
        rows.append(RunRow(data.pair.name, "same_wallet", "long", summarize(r, initial), r))

    # value-add + rebate-add vs matched holds
    by_name = {r.metrics["name"]: r for r in rows if r.result is not None}
    a1 = by_name.get("A1_etf_hold")
    bhold = by_name.get("B6_hold_3x_dir")
    extras: dict[str, Any] = {"path_drag": path_drag(data.etf, data.spot), "snapshot": data.snapshot, "window": data.window.as_dict()}
    if a1 and a1.result:
        for r in rows:
            if r.result and r.metrics["name"].startswith("A2_") and r.lens == "same_wallet":
                r.metrics["etf_grid_value_add"] = value_add(r.result, a1.result)
    if bhold and bhold.result:
        for r in rows:
            if r.result and r.metrics["name"].startswith("B_perp_3.0x") and "noreb" not in r.metrics["name"]:
                r.metrics["perp_grid_value_add"] = value_add(r.result, bhold.result)

    # rebate value add on a matched pair of names
    for base_name in (
        "A2_etf_native_atr_d0.0_reb_base",
        "B_perp_3.0x_iso_P1_d0.0_reb_base",
    ):
        reb = by_name.get(base_name)
        zero = by_name.get(base_name.replace("_reb_", "_noreb_"))
        if reb and zero and reb.result and zero.result:
            extras.setdefault("rebate_value_add", {})[base_name] = rebate_value(reb.result, zero.result)

    # robustness across neighboring native ATR steps (plateau, not god-param)
    fill = FillConfig.preset("base")
    plateau = []
    for step in (0.30, 0.40, 0.50):
        r = _etf_grid(
            data, name=f"plateau_etf_{step}", fill=fill, rebate=spot_reb, dir_frac=0.0,
            grid_mode="native_atr", interval=interval, initial=initial, atr_step=step,
        )
        plateau.append({"step": step, "side": "etf", **summarize(r, initial)})
        r = _perp_grid(
            data, name=f"plateau_perp_{step}", fill=fill, rebate=fut_reb, dir_frac=0.0,
            target_notional=initial * 3.0, leverage=3.0, interval=interval, initial=initial,
            atr_step=step,
        )
        plateau.append({"step": step, "side": "perp", **summarize(r, initial)})
    extras["plateau"] = plateau
    etf_rets = [p["total_return"] for p in plateau if p["side"] == "etf"]
    perp_rets = [p["total_return"] for p in plateau if p["side"] == "perp"]
    extras["plateau_overfit"] = {
        "etf": _overfit_flag(etf_rets),
        "perp": _overfit_flag(perp_rets),
    }

    metrics_only = []
    for r in rows:
        m = dict(r.metrics)
        m["score"] = composite_score(m)
        m["lens"] = r.lens
        m["side"] = r.side
        m["pair"] = r.pair
        metrics_only.append(m)

    # keep a few equity curves for the report
    keep_names = {
        "A0_cash", "A1_etf_hold", "B1_spot_hold", "B2_spot_grid",
        "A2_etf_native_atr_d0.0_reb_base", "A2_etf_native_atr_d0.0_noreb_base",
        "A2_etf_native_atr_d0.0_reb_conservative",
        "B_perp_3.0x_iso_P1_d0.0_reb_base", "B_perp_3.0x_iso_P1_d0.0_noreb_base",
        "B_perp_1.5x_iso_P1_d0.0_reb_base", "B_perp_2.0x_iso_P1_d0.0_reb_base",
        "B_perp_2.5x_iso_P1_d0.0_reb_base",
        "B_same_expo_base", "A2_same_expo_base", "B_same_risk_base", "A2_same_risk_base",
        "B6_hold_3x_dir", "B_perp_3x_iso_P2_reb_base", "B_perp_3x_cross_P1_reb_base",
    }
    curves = {}
    for r in rows:
        if r.result and r.metrics["name"] in keep_names:
            curves[r.metrics["name"]] = {
                "equity": [round(float(x), 4) for x in r.result.equity[:: max(1, len(r.result.equity)//400)]],
                "liquidated": r.result.liquidated,
            }

    return {
        "pair": data.pair.name,
        "interval": interval,
        "window": data.window.as_dict(),
        "rows": metrics_only,
        "extras": extras,
        "curves": curves,
    }


def _overfit_flag(vals: list[float]) -> dict[str, Any]:
    if len(vals) < 3:
        return {"flag": "insufficient"}
    mid = vals[len(vals) // 2]
    neighbors = [vals[0], vals[-1]]
    # God-param: middle huge, neighbors lose
    if mid > 0.05 and all(v < 0 for v in neighbors):
        return {"flag": "OVERFIT", "values": vals}
    spread = max(vals) - min(vals)
    return {"flag": "plateau" if spread < 0.15 else "sensitive", "values": vals, "spread": spread}


def run_windows(data: PairData, cfg: dict[str, Any]) -> dict[str, Any]:
    initial = float(cfg.get("initial_capital") or 1000.0)
    horizons = list(cfg.get("horizons") or [7, 14, 30, 60, 90])
    days = (data.window.ab_end - data.window.ab_start).total_seconds() / 86400.0
    horizons = [h for h in horizons if h <= days + 0.5]
    if days >= 170:
        horizons.append(180)
    wins = slice_windows(data.spot, horizons, data.interval, max_per_horizon=6)
    fill = FillConfig.preset("base")
    out = []
    for w in wins:
        etf = _slice(data.etf, w.i0, w.i1)
        perp = _slice(data.perp, w.i0, w.i1)
        spot = _slice(data.spot, w.i0, w.i1)
        sub = PairData(
            pair=data.pair, interval=data.interval, etf=etf, perp=perp, spot=spot,
            funding=data.funding, contract=data.contract, window=data.window, snapshot=data.snapshot,
        )
        a = _etf_grid(sub, name="win_etf", fill=fill, rebate=0.70, dir_frac=0.0, grid_mode="native_atr", interval=data.interval, initial=initial)
        b = _perp_grid(sub, name="win_perp", fill=fill, rebate=0.75, dir_frac=0.0, target_notional=3000.0, leverage=3.0, interval=data.interval, initial=initial)
        sa, sb = summarize(a, initial), summarize(b, initial)
        out.append({
            "horizon_days": w.horizon_days,
            "regime": w.regime,
            "start": str(w.start),
            "end": str(w.end),
            "und_ret": w.features.get("ret"),
            "und_rv": w.features.get("rv"),
            "etf": {k: sa[k] for k in ("final_equity", "total_return", "max_dd_pct", "net_profit_per_1m_turnover", "liquidated", "sharpe")},
            "perp": {k: sb[k] for k in ("final_equity", "total_return", "max_dd_pct", "net_profit_per_1m_turnover", "liquidated", "sharpe")},
        })
    special = {}
    for label, lst in special_masks(data.spot, data.interval).items():
        special[label] = [
            {"start": str(w.start), "end": str(w.end), "ret": w.features.get("ret"), "rv": w.features.get("rv"), "regime": w.regime}
            for w in lst[:4]
        ]
    return {"windows": out, "special_candidates": special}


def walk_forward(data: PairData, cfg: dict[str, Any]) -> dict[str, Any]:
    n = len(data.etf)
    if n < 200:
        return {"skipped": True, "reason": "history_too_short"}
    i_tr = int(n * 0.50)
    i_va = int(n * 0.75)
    initial = float(cfg.get("initial_capital") or 1000.0)
    fill = FillConfig.preset("base")
    plateau_steps = (0.30, 0.40, 0.50)

    def eval_split(i0: int, i1: int, step: float, side: str) -> dict[str, Any]:
        sub = PairData(
            pair=data.pair, interval=data.interval,
            etf=_slice(data.etf, i0, i1), perp=_slice(data.perp, i0, i1), spot=_slice(data.spot, i0, i1),
            funding=data.funding, contract=data.contract, window=data.window, snapshot=data.snapshot,
        )
        if side == "etf":
            r = _etf_grid(sub, name="wf", fill=fill, rebate=0.70, dir_frac=0.0, grid_mode="native_atr", interval=data.interval, initial=initial, atr_step=step)
        else:
            r = _perp_grid(sub, name="wf", fill=fill, rebate=0.75, dir_frac=0.0, target_notional=3000.0, leverage=3.0, interval=data.interval, initial=initial, atr_step=step)
        m = summarize(r, initial)
        m["score"] = composite_score(m)
        return m

    report: dict[str, Any] = {"n": n, "train": i_tr, "val": i_va, "test": n}
    for side in ("etf", "perp"):
        train = [eval_split(0, i_tr, s, side) | {"step": s} for s in plateau_steps]
        # pick robust plateau: median score, not max
        scores = [t["score"] for t in train]
        pick = plateau_steps[int(np.argsort(scores)[len(scores) // 2])]
        val = eval_split(i_tr, i_va, pick, side)
        oos = eval_split(i_va, n, pick, side)
        report[side] = {
            "train": train,
            "picked_step": pick,
            "pick_rule": "median_train_score_plateau",
            "validation": val,
            "oos": oos,
            "oos_stability": float(np.clip(1.0 - abs(val["total_return"] - oos["total_return"]), 0, 1)),
        }
    return report


def block_bootstrap(daily: np.ndarray, block: int, n_paths: int, rng: np.random.Generator) -> np.ndarray:
    if len(daily) == 0:
        return np.ones((n_paths, 1))
    n = len(daily)
    blk = max(int(block), 1)
    starts = rng.integers(0, n, size=(n_paths, int(np.ceil(n / blk)) + 2))
    paths = np.ones(n_paths)
    eq = np.zeros((n_paths, 5))
    for p in range(n_paths):
        seq = []
        for s in starts[p]:
            seq.extend(daily[s : s + blk])
            if len(seq) >= n:
                break
        seq = np.asarray(seq[:n], dtype=float)
        curve = np.cumprod(1.0 + seq)
        paths[p] = float(curve[-1]) if len(curve) else 1.0
        # store unused shape compat
        eq[p, 0] = paths[p]
    return paths


def monte_carlo(data: PairData, cfg: dict[str, Any]) -> dict[str, Any]:
    initial = float(cfg.get("initial_capital") or 1000.0)
    fill = FillConfig.preset("base")
    a = _etf_grid(data, name="mc_etf", fill=fill, rebate=0.70, dir_frac=0.0, grid_mode="native_atr", interval=data.interval, initial=initial)
    b = _perp_grid(data, name="mc_perp", fill=fill, rebate=0.75, dir_frac=0.0, target_notional=3000.0, leverage=3.0, interval=data.interval, initial=initial)
    n_paths = int(cfg.get("mc_paths") or 1000)
    rng = np.random.default_rng(7)

    def daily_from(res: EngineResult) -> np.ndarray:
        s = pd.Series(res.equity, index=pd.to_datetime(res.timestamps, utc=True))
        d = s.resample("1D").last().dropna().pct_change().dropna().to_numpy(float)
        return d

    out: dict[str, Any] = {"paths": n_paths, "etf_liq_prob_in_sample": float(a.liquidated), "perp_liq_in_sample": float(b.liquidated)}
    for side, res in (("etf", a), ("perp", b)):
        daily = daily_from(res)
        side_out = {}
        for blk in (1, 3, 5):
            finals = block_bootstrap(daily, blk, n_paths, rng) * initial
            # reconstruct simple DD proxy from final only is weak; bootstrap daily and rebuild
            # rebuild curves
            curves = []
            n = len(daily)
            if n == 0:
                continue
            starts = rng.integers(0, n, size=(n_paths, int(np.ceil(n / blk)) + 2))
            dds = []
            loss = 0
            dd10 = dd20 = dd30 = 0
            for p in range(n_paths):
                seq = []
                for s in starts[p]:
                    seq.extend(daily[s : s + blk])
                    if len(seq) >= n:
                        break
                seq = np.asarray(seq[:n], dtype=float)
                curve = initial * np.cumprod(1.0 + seq)
                peak = np.maximum.accumulate(curve)
                dd = float(((peak - curve) / np.maximum(peak, 1e-12)).max())
                dds.append(dd)
                if curve[-1] < initial:
                    loss += 1
                if dd > 0.10:
                    dd10 += 1
                if dd > 0.20:
                    dd20 += 1
                if dd > 0.30:
                    dd30 += 1
                curves.append(curve[-1])
            arr = np.asarray(curves)
            side_out[f"block_{blk}d"] = {
                "p5": float(np.percentile(arr, 5)),
                "p25": float(np.percentile(arr, 25)),
                "p50": float(np.percentile(arr, 50)),
                "p75": float(np.percentile(arr, 75)),
                "p95": float(np.percentile(arr, 95)),
                "prob_loss": loss / n_paths,
                "prob_dd_10": dd10 / n_paths,
                "prob_dd_20": dd20 / n_paths,
                "prob_dd_30": dd30 / n_paths,
            }
        if side == "perp":
            side_out["liquidation_probability_in_sample"] = 1.0 if b.liquidated else 0.0
        out[side] = side_out
    return out


def run_short_pair(data: PairData, cfg: dict[str, Any]) -> dict[str, Any] | None:
    if data.etf_short is None or data.etf_short.empty:
        return None
    initial = float(cfg.get("initial_capital") or 1000.0)
    fill = FillConfig.preset("base")
    # overlap short ETF with perp
    etf_s = data.etf_short
    perp = data.perp
    common = etf_s.loc[etf_s["timestamp"].isin(perp["timestamp"])].reset_index(drop=True)
    perp_s = perp.loc[perp["timestamp"].isin(common["timestamp"])].reset_index(drop=True)
    if len(common) < 48:
        return {"skipped": True, "reason": "short_overlap_too_short", "bars": int(len(common))}
    sub_etf = PairData(
        pair=data.pair, interval=data.interval, etf=common, perp=perp_s, spot=data.spot,
        funding=data.funding, contract=data.contract, window=data.window, snapshot=data.snapshot,
    )
    a = run_spot_grid(
        common, name="A_short_3S", symbol=data.pair.etf_short or "", fee=_fee_spot(0.70),
        fill=fill, initial=initial, direction="short", dir_frac=0.50, grid_mode="native_atr",
        interval=data.interval, und_close=None,
    )
    b = _perp_grid(
        sub_etf, name="B_short_perp", fill=fill, rebate=0.75, dir_frac=0.0,
        target_notional=3000.0, leverage=3.0, interval=data.interval, initial=initial, direction="short",
    )
    sa, sb = summarize(a, initial), summarize(b, initial)
    return {
        "pair": data.pair.name,
        "bars": int(len(common)),
        "start": str(common["timestamp"].iloc[0]),
        "end": str(common["timestamp"].iloc[-1]),
        "etf_3s": sa,
        "perp_short": sb,
    }


def _pick(rows: list[dict[str, Any]], name: str) -> dict[str, Any] | None:
    for r in rows:
        if r.get("name") == name:
            return r
    return None


def decide_pair(bundle: dict[str, Any]) -> dict[str, Any]:
    rows = bundle["rows"]
    wf = bundle.get("walk_forward") or {}
    oos_etf = ((wf.get("etf") or {}).get("oos_stability")) if isinstance(wf.get("etf"), dict) else 0.5
    oos_perp = ((wf.get("perp") or {}).get("oos_stability")) if isinstance(wf.get("perp"), dict) else 0.5
    wins = bundle.get("windows") or {}
    wrows = wins.get("windows") or []
    def robust(prefix: str) -> float:
        if not wrows:
            return 0.5
        key = "etf" if prefix == "etf" else "perp"
        rets = [w[key]["total_return"] for w in wrows if key in w]
        if not rets:
            return 0.5
        pos = sum(1 for x in rets if x > 0) / len(rets)
        return float(pos)

    etf = _pick(rows, "A2_etf_native_atr_d0.0_reb_base") or _pick(rows, "A2_same_expo_base")
    perp3 = _pick(rows, "B_perp_3.0x_iso_P1_d0.0_reb_base")
    perp15 = _pick(rows, "B_perp_1.5x_iso_P1_d0.0_reb_base")
    if not etf or not perp3:
        return {"winner": "INCOMPLETE", "reason": "missing_core_rows"}

    etf_s = composite_score(etf, {"robustness": robust("etf"), "oos": float(oos_etf or 0.5)})
    p3_s = composite_score(perp3, {"robustness": robust("perp"), "oos": float(oos_perp or 0.5)})
    p15_s = composite_score(perp15, {"robustness": robust("perp"), "oos": float(oos_perp or 0.5)}) if perp15 else -9

    # Hybrid proxy: 60/20/20 of final equities (independent accounts)
    hyb = 0.60 * etf["final_equity"] + 0.20 * perp3["final_equity"] + 0.20 * 1000.0
    # Hybrid DD approx: weighted (not perfect, conservative)
    hyb_dd = 0.60 * etf["max_dd_pct"] + 0.20 * perp3["max_dd_pct"]
    hyb_row = {
        "total_return": hyb / 1000.0 - 1.0,
        "max_dd_pct": hyb_dd,
        "net_profit_per_1m_turnover": 0.6 * etf.get("net_profit_per_1m_turnover", 0) + 0.2 * perp3.get("net_profit_per_1m_turnover", 0),
        "capital_efficiency": 0.6 * etf.get("capital_efficiency", 0) + 0.2 * perp3.get("capital_efficiency", 0),
        "liquidated": bool(etf.get("liquidated") or perp3.get("liquidated")),
        "liquidation_count": int(etf.get("liquidation_count") or 0) + int(perp3.get("liquidation_count") or 0),
    }
    hyb_s = composite_score(hyb_row, {"robustness": 0.5 * (robust("etf") + robust("perp")), "oos": 0.5})

    scored = [("ETF", etf_s), ("PERP_3x", p3_s), ("PERP_1.5x", p15_s), ("HYBRID", hyb_s)]
    scored.sort(key=lambda x: -x[1])
    winner = scored[0][0]
    second = scored[1][0]
    # Map to user labels
    label = {"ETF": "ETF WIN", "PERP_3x": "PERP WIN", "PERP_1.5x": "PERP WIN", "HYBRID": "HYBRID"}[winner]
    not_rec = scored[-1][0]
    return {
        "winner": label,
        "primary": winner,
        "secondary": second,
        "not_recommended": not_rec,
        "scores": {k: v for k, v in scored},
        "hybrid_final_equity_proxy": hyb,
        "etf_core": etf,
        "perp_3x": perp3,
        "perp_1.5x": perp15,
    }


def run_portfolio(pair_data: dict[str, PairData], cfg: dict[str, Any]) -> dict[str, Any]:
    """10k book. Weights capped. Intersection of real overlap only."""
    wanted = [p.name for p in portfolio_core() if p.name in pair_data]
    if len(wanted) < 3:
        return {"skipped": True, "reason": "not_enough_portfolio_assets"}
    ts_sets = [set(pd.to_datetime(pair_data[n].etf["timestamp"], utc=True)) for n in wanted]
    common = ts_sets[0]
    for s in ts_sets[1:]:
        common &= s
    if len(common) < 48:
        return {"skipped": True, "reason": "portfolio_overlap_too_short", "bars": len(common)}
    common_sorted = sorted(common)
    weights = {"SOL": 0.28, "ETH": 0.28, "SOXL": 0.24, "PENGU": 0.08, "PUMP": 0.08}
    # caps
    weights = {k: min(v, 0.30 if k not in {"PENGU", "PUMP"} else 0.08) for k, v in weights.items() if k in wanted}
    z = sum(weights.values())
    weights = {k: v / z * 0.96 for k, v in weights.items()}  # 4% cash residual after cap
    initial_book = 10_000.0
    fill = FillConfig.preset("base")
    eq_etf = None
    eq_perp = None
    parts = {}
    for name, w in weights.items():
        d = pair_data[name]
        mask = pd.to_datetime(d.etf["timestamp"], utc=True).isin(common)
        sub = PairData(
            pair=d.pair, interval=d.interval,
            etf=d.etf.loc[mask].reset_index(drop=True),
            perp=d.perp.loc[pd.to_datetime(d.perp["timestamp"], utc=True).isin(common)].reset_index(drop=True),
            spot=d.spot.loc[pd.to_datetime(d.spot["timestamp"], utc=True).isin(common)].reset_index(drop=True),
            funding=d.funding, contract=d.contract, window=d.window, snapshot=d.snapshot,
        )
        cap = initial_book * w
        a = _etf_grid(sub, name=f"pf_etf_{name}", fill=fill, rebate=0.70, dir_frac=0.0, grid_mode="native_atr", interval=d.interval, initial=cap)
        b = _perp_grid(sub, name=f"pf_perp_{name}", fill=fill, rebate=0.75, dir_frac=0.0, target_notional=cap * 2.0, leverage=2.0, interval=d.interval, initial=cap)
        parts[name] = {"weight": w, "etf": summarize(a, cap), "perp": summarize(b, cap), "etf_liq": a.liquidated, "perp_liq": b.liquidated}
        if eq_etf is None:
            eq_etf = np.asarray(a.equity, dtype=float)
            eq_perp = np.asarray(b.equity, dtype=float)
        else:
            n = min(len(eq_etf), len(a.equity), len(b.equity))
            eq_etf = eq_etf[:n] + np.asarray(a.equity[:n], dtype=float)
            eq_perp = eq_perp[:n] + np.asarray(b.equity[:n], dtype=float)
    cash = initial_book * (1.0 - sum(weights.values()))
    eq_etf = eq_etf + cash
    eq_perp = eq_perp + cash
    eq_hyb = 0.60 * (eq_etf - cash) + 0.20 * (eq_perp - cash) + 0.20 * initial_book
    eq_hyb2 = 0.70 * (eq_etf - cash) + 0.15 * (eq_perp - cash) + 0.15 * initial_book

    def pack(eq: np.ndarray, name: str) -> dict[str, Any]:
        from .engine import EngineResult

        res = EngineResult(
            name=name, market="portfolio", symbol="BOOK",
            timestamps=list(common_sorted[: len(eq)]),
            equity=eq, cash=np.zeros(len(eq)), inventory_value=eq.copy(),
            position_qty=np.zeros(len(eq)), margin_ratio=np.ones(len(eq)), liq_buffer=np.ones(len(eq)),
            trades=[], liquidated=any(p["perp_liq"] for p in parts.values()) if "perp" in name else False,
            liquidation_count=sum(int(p["perp_liq"]) for p in parts.values()) if "perp" in name else 0,
            margin_additions=[], components={"turnover": 0.0},
        )
        m = summarize(res, initial_book)
        m["score"] = composite_score(m)
        return m

    return {
        "ab_start": str(common_sorted[0]),
        "ab_end": str(common_sorted[-1]),
        "bars": len(common_sorted),
        "weights": weights,
        "cash_frac": 1.0 - sum(weights.values()),
        "parts": parts,
        "pure_etf": pack(eq_etf, "PF_ETF"),
        "pure_perp": pack(eq_perp, "PF_PERP"),
        "hybrid_60_20_20": pack(eq_hyb, "PF_HYB602020"),
        "hybrid_70_15_15": pack(eq_hyb2, "PF_HYB701515"),
    }
