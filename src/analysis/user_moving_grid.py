"""User-spec moving grid: 5x, ±20 USDT, 200 arithmetic levels, isolated perp.

TICK path-exact fills when get_trades is provided. Daily equity is last bar of UTC day.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Literal

import numpy as np
import pandas as pd

BarHook = Callable[[int, pd.Timestamp, float], None]

from qtb.ab.fills import FillConfig, PendingFill
from qtb.dual.tick_fills import resolve_tick_fills

FeePreset = Literal["base", "conservative"]
FEE_BPS = {"base": 2.0, "conservative": 4.0}

USER_LEVERAGE = 5.0
USER_RANGE_USDT = 20.0
USER_RANGE_PCT = 0.20
USER_N_GRIDS = 200
USER_CAPITAL_PER_SIDE = 5_000.0
RangeMode = Literal["usdt", "pct"]
GridKind = Literal["arithmetic", "geometric"]
ReanchorPolicy = Literal["remap", "drop_lots", "flatten"]
USER_GRID_KIND: GridKind = "arithmetic"
USER_REANCHOR: ReanchorPolicy = "remap"
USER_MMR_FRAC = 0.005


def user_levels(
    mid: float,
    *,
    range_mode: str = "usdt",
    range_usdt: float = USER_RANGE_USDT,
    range_pct: float = USER_RANGE_PCT,
    n_grids: int = USER_N_GRIDS,
    grid_kind: str = USER_GRID_KIND,
    extras: dict[str, Any] | None = None,
) -> np.ndarray:
    """Moving-grid rungs. Band + spacing come from grid_ext so both can be plugged in."""
    from src.analysis.grid_ext import resolve_band, resolve_rungs

    n = int(n_grids)
    if n < 2:
        raise ValueError("n_grids must be >= 2")
    lo, hi = resolve_band(
        range_mode,
        float(mid),
        range_usdt=range_usdt,
        range_pct=range_pct,
        extras=extras,
    )
    if lo <= 0:
        lo = max(mid * 0.05, 0.01)
    if hi <= lo:
        raise ValueError(f"grid band inverted lo={lo} hi={hi}")
    return resolve_rungs(grid_kind, lo, hi, n)


def _fee_rate(preset: FeePreset = "base", fee_bps: float | None = None) -> float:
    if fee_bps is not None:
        return float(fee_bps) / 10_000.0
    return FEE_BPS[preset] / 10_000.0


def _step(levels: np.ndarray) -> float:
    if len(levels) < 2:
        return 0.2
    return float(levels[1] - levels[0])


@dataclass
class IsolatedDirBook:
    """One-direction isolated perp book (long XOR short)."""

    capital: float
    leverage: float
    fee: float
    direction: Literal["long", "short"]
    cash: float = 0.0
    im: float = 0.0
    qty: float = 0.0
    avg: float = 0.0
    lots: dict[int, float] = field(default_factory=dict)
    realized: float = 0.0
    turnover: float = 0.0
    fills: int = 0
    liquidated: bool = False
    liq_bars: int = 0
    mmr_frac: float = USER_MMR_FRAC

    def __post_init__(self) -> None:
        self.cash = float(self.capital)

    def equity(self, px: float) -> float:
        if self.direction == "long":
            upnl = self.qty * (px - self.avg) if self.qty else 0.0
        else:
            upnl = self.qty * (self.avg - px) if self.qty else 0.0
        return float(self.cash + self.im + upnl)

    def notional(self, px: float) -> float:
        return abs(self.qty) * px

    def _can_open(self, notion: float, px: float) -> bool:
        if self.liquidated or notion < 1.0:
            return False
        if self.notional(px) + notion > self.capital * self.leverage + 1e-6:
            return False
        need = notion / self.leverage + notion * self.fee
        return self.cash + 1e-9 >= need

    def open_lot(self, q: float, px: float, level_idx: int) -> None:
        notion = q * px
        if not self._can_open(notion, px):
            room = max(self.capital * self.leverage - self.notional(px), 0.0)
            notion = min(notion, room, max(self.cash / (1.0 / self.leverage + self.fee), 0.0))
            if notion < 1.0:
                return
            q = notion / px
        im_add = notion / self.leverage
        fee = notion * self.fee
        self.cash -= im_add + fee
        new_q = self.qty + q
        self.avg = (self.avg * self.qty + px * q) / new_q if new_q > 1e-12 else 0.0
        self.qty = new_q
        self.im += im_add
        self.lots[level_idx] = self.lots.get(level_idx, 0.0) + q
        self.turnover += notion
        self.fills += 1

    def close_lot(self, q: float, px: float, level_idx: int | None) -> None:
        take = min(q, self.qty)
        if take <= 1e-12:
            return
        notion = take * px
        fee = notion * self.fee
        if self.direction == "long":
            pnl = take * (px - self.avg)
        else:
            pnl = take * (self.avg - px)
        im_rel = (take / self.qty) * self.im if self.qty else 0.0
        self.cash += im_rel + pnl - fee
        self.im -= im_rel
        self.qty -= take
        self.realized += pnl - fee
        if self.qty <= 1e-12:
            self.qty = 0.0
            self.avg = 0.0
            self.im = 0.0
            self.lots.clear()
        elif level_idx is not None and level_idx in self.lots:
            left = self.lots[level_idx] - take
            if left <= 1e-12:
                del self.lots[level_idx]
            else:
                self.lots[level_idx] = left
        self.turnover += notion
        self.fills += 1

    def flatten(self, px: float) -> None:
        """Close leftover inventory at mark. Used when the hedge pair stops."""
        if self.liquidated or self.qty <= 1e-12:
            self.lots.clear()
            return
        self.close_lot(self.qty, px, None)

    def check_liq(self, px: float) -> None:
        if self.liquidated:
            return
        eq = self.equity(px)
        notion = self.notional(px)
        # Isolated: wipe if equity cannot cover ~0.5% MMR or equity <= 0
        if eq <= 0.0 or (notion > 0 and eq <= notion * self.mmr_frac):
            self.liquidated = True
            self.liq_bars += 1
            self.cash = 0.0
            self.im = 0.0
            self.qty = 0.0
            self.avg = 0.0
            self.lots.clear()


def remap_lots(book: IsolatedDirBook, old_levels: np.ndarray, new_levels: np.ndarray) -> None:
    """Keep inventory; reattach lot qty to nearest rungs after a band move."""
    if not book.lots:
        return
    if len(new_levels) == 0:
        book.lots = {}
        return
    merged: dict[int, float] = {}
    n_old = len(old_levels)
    for idx, q in book.lots.items():
        if q <= 1e-12:
            continue
        if 0 <= idx < n_old:
            px = float(old_levels[idx])
        else:
            px = float(book.avg) if book.avg else float(new_levels[len(new_levels) // 2])
        j = int(np.argmin(np.abs(new_levels - px)))
        merged[j] = merged.get(j, 0.0) + float(q)
    book.lots = merged


def apply_reanchor(
    book: IsolatedDirBook,
    old_levels: np.ndarray,
    new_levels: np.ndarray,
    px: float,
    policy: ReanchorPolicy = USER_REANCHOR,
) -> None:
    if policy == "remap":
        remap_lots(book, old_levels, new_levels)
    elif policy == "drop_lots":
        book.lots = {}
    elif policy == "flatten":
        book.flatten(px)
    else:
        from src.analysis.grid_ext import REANCHORS

        fn = REANCHORS.get(str(policy))
        if fn is None:
            raise ValueError(f"unknown reanchor {policy}")
        fn(book, old_levels, new_levels, px)


def simulate_user_dir_grid(
    bars: pd.DataFrame,
    *,
    direction: Literal["long", "short"],
    capital: float = USER_CAPITAL_PER_SIDE,
    leverage: float = USER_LEVERAGE,
    range_mode: RangeMode = "usdt",
    range_usdt: float = USER_RANGE_USDT,
    range_pct: float = USER_RANGE_PCT,
    n_grids: int = USER_N_GRIDS,
    fee_preset: FeePreset = "base",
    fill_engine: Literal["bar", "tick"] = "tick",
    get_trades: Callable[[int, pd.Timestamp], pd.DataFrame] | None = None,
    on_bar: BarHook | None = None,
    grid_kind: str = USER_GRID_KIND,
    fee_bps: float | None = None,
    reanchor: ReanchorPolicy | str = USER_REANCHOR,
    mmr_frac: float = USER_MMR_FRAC,
    extras: dict[str, Any] | None = None,
    **_kw: Any,
) -> dict[str, Any]:
    if fill_engine == "tick" and get_trades is None:
        raise ValueError("fill_engine='tick' requires get_trades (refuses silent bar fallback)")
    o = bars["open"].to_numpy(float)
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    ts = pd.to_datetime(bars["timestamp"], utc=True)
    fee = _fee_rate(fee_preset, fee_bps)
    cfg = FillConfig.preset(fee_preset if fee_preset in FEE_BPS else "base")
    book = IsolatedDirBook(capital, leverage, fee, direction, mmr_frac=mmr_frac)
    equity = np.empty(len(c), dtype=float)
    mid0 = float(c[0])
    band = dict(
        range_mode=range_mode,
        range_usdt=range_usdt,
        range_pct=range_pct,
        n_grids=n_grids,
        grid_kind=grid_kind,
        extras=extras or {},
    )
    levels = user_levels(mid0, **band)
    step = _step(levels)
    reanchors = 0

    for i in range(len(c)):
        px = float(c[i])
        if book.liquidated:
            equity[i] = 0.0
            if on_bar is not None:
                on_bar(i, ts.iloc[i], 0.0)
            continue
        if px < float(levels[0]) or px > float(levels[-1]):
            new_levels = user_levels(px, **band)
            apply_reanchor(book, levels, new_levels, px, reanchor)
            levels = new_levels
            step = _step(levels)
            reanchors += 1
        mid = px
        pending: list[PendingFill] = []
        lo_b, hi_b = float(l[i]), float(h[i])
        if direction == "long":
            for idx, lvl in enumerate(levels):
                if idx in book.lots or lvl > mid:
                    continue
                if fill_engine == "tick" and not (lo_b - step <= lvl <= hi_b + step):
                    continue
                pending.append(PendingFill("buy", float(lvl), idx, notional=max(capital * leverage / n_grids, 1.0), reason="grid"))
            for idx, lot_q in list(book.lots.items()):
                tp = float(levels[idx]) + step if idx < len(levels) else book.avg + step
                if idx + 1 < len(levels):
                    tp = float(levels[idx + 1])
                pending.append(PendingFill("sell", tp, idx + 1, qty=lot_q, reduce_only=True, reason="grid_tp"))
        else:
            for idx, lvl in enumerate(levels):
                if idx in book.lots or lvl < mid:
                    continue
                if fill_engine == "tick" and not (lo_b - step <= lvl <= hi_b + step):
                    continue
                pending.append(PendingFill("sell", float(lvl), idx, notional=max(capital * leverage / n_grids, 1.0), reason="grid"))
            for idx, lot_q in list(book.lots.items()):
                tp = float(levels[idx]) - step
                if idx - 1 >= 0:
                    tp = float(levels[idx - 1])
                pending.append(PendingFill("buy", tp, idx - 1, qty=lot_q, reduce_only=True, reason="grid_tp"))

        if fill_engine == "tick":
            trades = get_trades(i, ts.iloc[i])
            if trades is not None and not trades.empty and pending:
                fills = resolve_tick_fills(pending, trades, cfg, bar_open=float(o[i]), bar_close=px)
                for tf in fills:
                    if book.liquidated:
                        break
                    if tf.reduce_only:
                        lot_idx = tf.level_idx - 1 if direction == "long" else tf.level_idx + 1
                        book.close_lot(float(tf.qty), float(tf.price), lot_idx)
                    elif direction == "long" and tf.side == "buy":
                        book.open_lot(float(tf.qty), float(tf.price), tf.level_idx)
                    elif direction == "short" and tf.side == "sell":
                        book.open_lot(float(tf.qty), float(tf.price), tf.level_idx)
        else:
            _apply_bar_pending(book, pending, direction, lo_b, hi_b)
        book.check_liq(px)
        equity[i] = 0.0 if book.liquidated else book.equity(px)
        if on_bar is not None:
            on_bar(i, ts.iloc[i], float(equity[i]))

    out = {
        "label": f"{direction}_user_grid",
        "direction": direction,
        "return": float(equity[-1] / capital - 1.0) if capital else float("nan"),
        "max_dd": _max_dd(equity),
        "end_equity": float(equity[-1]),
        "end_qty": float(book.qty if direction == "long" else -book.qty),
        "end_inventory_notional": float(book.notional(float(c[-1]))),
        "inventory_frac": float(book.notional(float(c[-1])) / capital) if capital else 0.0,
        "turnover": float(book.turnover),
        "fills": int(book.fills),
        "reanchors": int(reanchors),
        "liquidated": bool(book.liquidated),
        "leverage": leverage,
        "range_mode": range_mode,
        "range_usdt": range_usdt,
        "range_pct": range_pct,
        "n_grids": n_grids,
        "fee_preset": fee_preset,
        "fill_engine": fill_engine,
        "equity": equity,
        "timestamps": ts.reset_index(drop=True),
    }
    return out


def _max_dd(equity: np.ndarray) -> float:
    eq = np.asarray(equity, dtype=float)
    peak = np.maximum.accumulate(np.maximum(eq, 1e-12))
    return float((eq / peak - 1.0).min())


def combine_user_ls(long_r: dict[str, Any], short_r: dict[str, Any], capital_total: float) -> dict[str, Any]:
    eq = np.asarray(long_r["equity"]) + np.asarray(short_r["equity"])
    ts = long_r["timestamps"]
    daily = daily_pnl(ts, eq, capital_total)
    return {
        "label": "soxl_user_long_short",
        "return": float(eq[-1] / capital_total - 1.0),
        "max_dd": _max_dd(eq),
        "end_equity": float(eq[-1]),
        "end_inventory_notional": float(long_r["end_inventory_notional"] + short_r["end_inventory_notional"]),
        "inventory_frac": float(
            (long_r["end_inventory_notional"] + short_r["end_inventory_notional"]) / capital_total
        ),
        "net_qty_units": float(long_r["end_qty"] + short_r["end_qty"]),
        "fills": int(long_r["fills"] + short_r["fills"]),
        "turnover": float(long_r["turnover"] + short_r["turnover"]),
        "reanchors": int(long_r["reanchors"] + short_r["reanchors"]),
        "liquidated_long": bool(long_r["liquidated"]),
        "liquidated_short": bool(short_r["liquidated"]),
        "equity": eq,
        "timestamps": ts,
        "daily": daily,
        "long": {k: v for k, v in long_r.items() if k not in ("equity", "timestamps")},
        "short": {k: v for k, v in short_r.items() if k not in ("equity", "timestamps")},
    }


def _dir_pending(
    *,
    direction: Literal["long", "short"],
    levels: np.ndarray,
    step: float,
    mid: float,
    book: IsolatedDirBook,
    capital: float,
    leverage: float,
    n_grids: int,
    fill_engine: str,
    lo_b: float,
    hi_b: float,
) -> list[PendingFill]:
    pending: list[PendingFill] = []
    tag = direction
    if direction == "long":
        for idx, lvl in enumerate(levels):
            if idx in book.lots or lvl > mid:
                continue
            if fill_engine == "tick" and not (lo_b - step <= lvl <= hi_b + step):
                continue
            pending.append(
                PendingFill("buy", float(lvl), idx, notional=max(capital * leverage / n_grids, 1.0), reason=f"{tag}_grid")
            )
        for idx, lot_q in list(book.lots.items()):
            tp = float(levels[idx + 1]) if idx + 1 < len(levels) else float(levels[idx]) + step
            pending.append(PendingFill("sell", tp, idx + 1, qty=lot_q, reduce_only=True, reason=f"{tag}_tp"))
    else:
        for idx, lvl in enumerate(levels):
            if idx in book.lots or lvl < mid:
                continue
            if fill_engine == "tick" and not (lo_b - step <= lvl <= hi_b + step):
                continue
            pending.append(
                PendingFill("sell", float(lvl), idx, notional=max(capital * leverage / n_grids, 1.0), reason=f"{tag}_grid")
            )
        for idx, lot_q in list(book.lots.items()):
            tp = float(levels[idx - 1]) if idx - 1 >= 0 else float(levels[idx]) - step
            pending.append(PendingFill("buy", tp, idx - 1, qty=lot_q, reduce_only=True, reason=f"{tag}_tp"))
    return pending


def _apply_fill(book: IsolatedDirBook, tf: Any, direction: Literal["long", "short"]) -> None:
    if book.liquidated:
        return
    if tf.reduce_only:
        lot_idx = tf.level_idx - 1 if direction == "long" else tf.level_idx + 1
        book.close_lot(float(tf.qty), float(tf.price), lot_idx)
    elif direction == "long" and tf.side == "buy":
        book.open_lot(float(tf.qty), float(tf.price), tf.level_idx)
    elif direction == "short" and tf.side == "sell":
        book.open_lot(float(tf.qty), float(tf.price), tf.level_idx)


def _apply_bar_pending(book: IsolatedDirBook, pending: list[PendingFill], direction: Literal["long", "short"], lo_b: float, hi_b: float) -> None:
    for p in pending:
        if book.liquidated:
            break
        if p.reduce_only:
            hit = (direction == "long" and hi_b >= p.price) or (direction == "short" and lo_b <= p.price)
            if hit:
                book.close_lot(float(p.qty or 0.0), float(p.price), p.level_idx - 1 if direction == "long" else p.level_idx + 1)
        else:
            if lo_b <= p.price <= hi_b:
                notion = float(p.notional or 0.0)
                book.open_lot(notion / p.price, float(p.price), p.level_idx)


def _book_snapshot(book: IsolatedDirBook, equity: np.ndarray, capital: float, last_px: float, *, direction: str, reanchors: int, range_mode: str, range_usdt: float, range_pct: float, n_grids: int, fee_preset: str, fill_engine: str, leverage: float) -> dict[str, Any]:
    return {
        "label": f"{direction}_user_grid",
        "direction": direction,
        "return": float(equity[-1] / capital - 1.0) if capital else float("nan"),
        "max_dd": _max_dd(equity),
        "end_equity": float(equity[-1]),
        "end_qty": float(book.qty if direction == "long" else -book.qty),
        "end_inventory_notional": float(book.notional(last_px)),
        "inventory_frac": float(book.notional(last_px) / capital) if capital else 0.0,
        "turnover": float(book.turnover),
        "fills": int(book.fills),
        "reanchors": int(reanchors),
        "liquidated": bool(book.liquidated),
        "leverage": leverage,
        "range_mode": range_mode,
        "range_usdt": range_usdt,
        "range_pct": range_pct,
        "n_grids": n_grids,
        "fee_preset": fee_preset,
        "fill_engine": fill_engine,
        "equity": equity,
    }


def run_user_hedge_pair(
    bars: pd.DataFrame,
    *,
    range_mode: RangeMode = "usdt",
    capital_per_side: float = USER_CAPITAL_PER_SIDE,
    capital_long: float | None = None,
    capital_short: float | None = None,
    leverage: float = USER_LEVERAGE,
    range_usdt: float = USER_RANGE_USDT,
    range_pct: float = USER_RANGE_PCT,
    n_grids: int = USER_N_GRIDS,
    fee_preset: FeePreset = "base",
    fill_engine: Literal["bar", "tick"] = "tick",
    get_trades: Callable[[int, pd.Timestamp], pd.DataFrame] | None = None,
    on_bar: BarHook | None = None,
    grid_kind: str = USER_GRID_KIND,
    fee_bps: float | None = None,
    reanchor: ReanchorPolicy | str = USER_REANCHOR,
    mmr_frac: float = USER_MMR_FRAC,
    extras: dict[str, Any] | None = None,
    restart: bool = False,
    **_kw: Any,
) -> dict[str, Any]:
    """Moving dual-side hedge: one band, both legs, flatten the survivor if either liquidates.

    restart=True: split remaining equity 50/50 into new isolated books (no new cash).
    """
    if fill_engine == "tick" and get_trades is None:
        raise ValueError("fill_engine='tick' requires get_trades (refuses silent bar fallback)")
    o = bars["open"].to_numpy(float)
    h = bars["high"].to_numpy(float)
    l = bars["low"].to_numpy(float)
    c = bars["close"].to_numpy(float)
    ts = pd.to_datetime(bars["timestamp"], utc=True)
    fee = _fee_rate(fee_preset, fee_bps)
    cfg = FillConfig.preset(fee_preset if fee_preset in FEE_BPS else "base")
    cap_l = float(capital_long if capital_long is not None else capital_per_side)
    cap_s = float(capital_short if capital_short is not None else capital_per_side)
    long_b = IsolatedDirBook(cap_l, leverage, fee, "long", mmr_frac=mmr_frac)
    short_b = IsolatedDirBook(cap_s, leverage, fee, "short", mmr_frac=mmr_frac)
    eq_l = np.empty(len(c), dtype=float)
    eq_s = np.empty(len(c), dtype=float)
    band = dict(
        range_mode=range_mode,
        range_usdt=range_usdt,
        range_pct=range_pct,
        n_grids=n_grids,
        grid_kind=grid_kind,
        extras=extras or {},
    )
    levels = user_levels(float(c[0]), **band)
    step = _step(levels)
    reanchors = 0
    pair_stopped = False
    stop_bar = None
    deaths: list[dict[str, Any]] = []
    n_restarts = 0
    pending_restart = False
    restart_cash = 0.0
    started_long = cap_l
    started_short = cap_s

    for i in range(len(c)):
        px = float(c[i])
        if pending_restart:
            if restart_cash < 200.0:
                pair_stopped = True
                if stop_bar is None:
                    stop_bar = i
                pending_restart = False
            else:
                half = restart_cash / 2.0
                long_b = IsolatedDirBook(half, leverage, fee, "long", mmr_frac=mmr_frac)
                short_b = IsolatedDirBook(half, leverage, fee, "short", mmr_frac=mmr_frac)
                cap_l = half
                cap_s = half
                levels = user_levels(px, **band)
                step = _step(levels)
                n_restarts += 1
                pending_restart = False
        if pair_stopped or ((long_b.liquidated or short_b.liquidated) and not restart and not pending_restart):
            pair_stopped = True
            if stop_bar is None:
                stop_bar = i
            if not long_b.liquidated:
                long_b.flatten(px)
            if not short_b.liquidated:
                short_b.flatten(px)
            eq_l[i] = 0.0 if long_b.liquidated else long_b.equity(px)
            eq_s[i] = 0.0 if short_b.liquidated else short_b.equity(px)
            if on_bar is not None:
                on_bar(i, ts.iloc[i], float(eq_l[i] + eq_s[i]))
            continue

        if px < float(levels[0]) or px > float(levels[-1]):
            new_levels = user_levels(px, **band)
            apply_reanchor(long_b, levels, new_levels, px, reanchor)
            apply_reanchor(short_b, levels, new_levels, px, reanchor)
            levels = new_levels
            step = _step(levels)
            reanchors += 1

        mid = px
        lo_b, hi_b = float(l[i]), float(h[i])
        pend_l = _dir_pending(
            direction="long", levels=levels, step=step, mid=mid, book=long_b,
            capital=cap_l, leverage=leverage, n_grids=n_grids,
            fill_engine=fill_engine, lo_b=lo_b, hi_b=hi_b,
        )
        pend_s = _dir_pending(
            direction="short", levels=levels, step=step, mid=mid, book=short_b,
            capital=cap_s, leverage=leverage, n_grids=n_grids,
            fill_engine=fill_engine, lo_b=lo_b, hi_b=hi_b,
        )
        pending = pend_l + pend_s
        if fill_engine == "tick":
            if pending:
                trades = get_trades(i, ts.iloc[i])
                if trades is not None and not trades.empty:
                    fills = resolve_tick_fills(pending, trades, cfg, bar_open=float(o[i]), bar_close=px)
                    for tf in fills:
                        if str(tf.reason).startswith("long"):
                            _apply_fill(long_b, tf, "long")
                        elif str(tf.reason).startswith("short"):
                            _apply_fill(short_b, tf, "short")
        else:
            _apply_bar_pending(long_b, pend_l, "long", lo_b, hi_b)
            _apply_bar_pending(short_b, pend_s, "short", lo_b, hi_b)

        long_b.check_liq(px)
        short_b.check_liq(px)
        if long_b.liquidated or short_b.liquidated:
            if not long_b.liquidated:
                long_b.flatten(px)
            if not short_b.liquidated:
                short_b.flatten(px)
            live = (0.0 if long_b.liquidated else long_b.equity(px)) + (
                0.0 if short_b.liquidated else short_b.equity(px)
            )
            deaths.append(
                {
                    "bar": i,
                    "ts": str(ts.iloc[i]),
                    "liquidated_long": bool(long_b.liquidated),
                    "liquidated_short": bool(short_b.liquidated),
                    "equity_after_flatten": float(live),
                }
            )
            if restart and live >= 200.0:
                pending_restart = True
                restart_cash = float(live)
            else:
                pair_stopped = True
                if stop_bar is None:
                    stop_bar = i
        eq_l[i] = 0.0 if long_b.liquidated else long_b.equity(px)
        eq_s[i] = 0.0 if short_b.liquidated else short_b.equity(px)
        if on_bar is not None:
            on_bar(i, ts.iloc[i], float(eq_l[i] + eq_s[i]))

    last_px = float(c[-1])
    long_r = _book_snapshot(
        long_b, eq_l, started_long, last_px, direction="long", reanchors=reanchors,
        range_mode=range_mode, range_usdt=range_usdt, range_pct=range_pct, n_grids=n_grids,
        fee_preset=fee_preset, fill_engine=fill_engine, leverage=leverage,
    )
    short_r = _book_snapshot(
        short_b, eq_s, started_short, last_px, direction="short", reanchors=reanchors,
        range_mode=range_mode, range_usdt=range_usdt, range_pct=range_pct, n_grids=n_grids,
        fee_preset=fee_preset, fill_engine=fill_engine, leverage=leverage,
    )
    long_r["timestamps"] = ts.reset_index(drop=True)
    short_r["timestamps"] = ts.reset_index(drop=True)
    comb = combine_user_ls(long_r, short_r, started_long + started_short)
    comb["range_mode"] = range_mode
    comb["fee_preset"] = fee_preset
    comb["fill_engine"] = fill_engine
    comb["hedge_mode"] = "restart_survivor" if restart else "moving_ls_flatten_survivor"
    comb["pair_stopped"] = bool(pair_stopped)
    comb["stop_bar"] = stop_bar
    comb["reanchors"] = int(reanchors)
    comb["n_restarts"] = int(n_restarts)
    comb["deaths"] = deaths
    comb["shared_reanchors"] = int(reanchors)
    return comb


def run_user_hedge_restart(bars: pd.DataFrame, **kwargs: Any) -> dict[str, Any]:
    """Flatten survivor, then re-seed both sides from remaining equity (no new cash)."""
    kwargs.pop("restart", None)
    return run_user_hedge_pair(bars, restart=True, **kwargs)


def run_user_ls_pair(
    bars: pd.DataFrame,
    *,
    range_mode: RangeMode = "usdt",
    capital_per_side: float = USER_CAPITAL_PER_SIDE,
    capital_long: float | None = None,
    capital_short: float | None = None,
    leverage: float = USER_LEVERAGE,
    range_usdt: float = USER_RANGE_USDT,
    range_pct: float = USER_RANGE_PCT,
    n_grids: int = USER_N_GRIDS,
    fee_preset: FeePreset = "base",
    fill_engine: Literal["bar", "tick"] = "tick",
    get_trades=None,
    on_bar: BarHook | None = None,
    grid_kind: str = USER_GRID_KIND,
    fee_bps: float | None = None,
    reanchor: ReanchorPolicy | str = USER_REANCHOR,
    mmr_frac: float = USER_MMR_FRAC,
    extras: dict[str, Any] | None = None,
    **_kw: Any,
) -> dict[str, Any]:
    cap_l = float(capital_long if capital_long is not None else capital_per_side)
    cap_s = float(capital_short if capital_short is not None else capital_per_side)
    shared = dict(
        range_mode=range_mode,
        leverage=leverage,
        range_usdt=range_usdt,
        range_pct=range_pct,
        n_grids=n_grids,
        fee_preset=fee_preset,
        fill_engine=fill_engine,
        get_trades=get_trades,
        grid_kind=grid_kind,
        fee_bps=fee_bps,
        reanchor=reanchor,
        mmr_frac=mmr_frac,
        extras=extras or {},
    )
    # Independent books run sequentially; on_bar reports the side currently simulating.
    long_r = simulate_user_dir_grid(bars, direction="long", capital=cap_l, on_bar=on_bar, **shared)
    short_r = simulate_user_dir_grid(bars, direction="short", capital=cap_s, on_bar=on_bar, **shared)
    comb = combine_user_ls(long_r, short_r, cap_l + cap_s)
    comb["range_mode"] = range_mode
    comb["fee_preset"] = fee_preset
    comb["fill_engine"] = fill_engine
    comb["hedge_mode"] = "independent"
    return comb


def run_user_one_side(
    bars: pd.DataFrame,
    *,
    direction: Literal["long", "short"],
    capital: float = USER_CAPITAL_PER_SIDE,
    leverage: float = USER_LEVERAGE,
    range_mode: RangeMode = "usdt",
    range_usdt: float = USER_RANGE_USDT,
    range_pct: float = USER_RANGE_PCT,
    n_grids: int = USER_N_GRIDS,
    fee_preset: FeePreset = "base",
    fill_engine: Literal["bar", "tick"] = "tick",
    get_trades=None,
    on_bar: BarHook | None = None,
    grid_kind: str = USER_GRID_KIND,
    fee_bps: float | None = None,
    reanchor: ReanchorPolicy | str = USER_REANCHOR,
    mmr_frac: float = USER_MMR_FRAC,
    extras: dict[str, Any] | None = None,
    **_kw: Any,
) -> dict[str, Any]:
    """Single-direction moving grid, same report shape as the pair runners."""
    r = simulate_user_dir_grid(
        bars,
        direction=direction,
        capital=capital,
        leverage=leverage,
        range_mode=range_mode,
        range_usdt=range_usdt,
        range_pct=range_pct,
        n_grids=n_grids,
        fee_preset=fee_preset,
        fill_engine=fill_engine,
        get_trades=get_trades,
        on_bar=on_bar,
        grid_kind=grid_kind,
        fee_bps=fee_bps,
        reanchor=reanchor,
        mmr_frac=mmr_frac,
        extras=extras or {},
    )
    daily = daily_pnl(r["timestamps"], r["equity"], capital)
    slim = {k: v for k, v in r.items() if k not in ("equity", "timestamps")}
    empty = {
        "label": "unused",
        "direction": "short" if direction == "long" else "long",
        "return": 0.0,
        "max_dd": 0.0,
        "end_equity": 0.0,
        "end_qty": 0.0,
        "end_inventory_notional": 0.0,
        "inventory_frac": 0.0,
        "turnover": 0.0,
        "fills": 0,
        "reanchors": 0,
        "liquidated": False,
    }
    return {
        "label": f"soxl_user_{direction}_only",
        "return": r["return"],
        "max_dd": r["max_dd"],
        "end_equity": r["end_equity"],
        "end_inventory_notional": r["end_inventory_notional"],
        "inventory_frac": r["inventory_frac"],
        "net_qty_units": r["end_qty"],
        "fills": r["fills"],
        "turnover": r["turnover"],
        "reanchors": r["reanchors"],
        "liquidated_long": bool(r["liquidated"]) if direction == "long" else False,
        "liquidated_short": bool(r["liquidated"]) if direction == "short" else False,
        "equity": r["equity"],
        "timestamps": r["timestamps"],
        "daily": daily,
        "long": slim if direction == "long" else empty,
        "short": slim if direction == "short" else empty,
        "range_mode": range_mode,
        "fee_preset": fee_preset,
        "fill_engine": fill_engine,
        "hedge_mode": "one_side",
        "pair_stopped": bool(r["liquidated"]),
        "stop_bar": None,
    }


def daily_pnl(ts: pd.Series, equity: np.ndarray, start_capital: float) -> pd.DataFrame:
    s = pd.Series(np.asarray(equity, dtype=float), index=pd.to_datetime(ts, utc=True))
    day = s.resample("1D").last().dropna()
    out = pd.DataFrame({"equity": day})
    out["daily_pnl"] = out["equity"].diff()
    out.iloc[0, out.columns.get_loc("daily_pnl")] = float(out["equity"].iloc[0] - start_capital)
    out["daily_ret"] = out["equity"].pct_change()
    out.iloc[0, out.columns.get_loc("daily_ret")] = float(out["equity"].iloc[0] / start_capital - 1.0)
    out["cum_ret"] = out["equity"] / start_capital - 1.0
    out.index.name = "date"
    return out.reset_index()
