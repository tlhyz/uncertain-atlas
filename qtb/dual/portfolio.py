"""Multi-book portfolio backtest: Tech + Crypto + Global Reserve."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np
import pandas as pd

from qtb.ab.engine import (
    EngineResult,
    FeeSpec,
    TradeRec,
    _PerpState,
    _perp_equity,
    _warmup_bars,
    run_cash,
    run_perp_grid,
)
from qtb.ab.fills import FillConfig, PendingFill, infer_tick, resolve_bar_fills
from qtb.ab.grids import GridSpec, grid_quote_size, native_spec, rolling_atr

from .tick_fills import resolve_tick_fills
from .tick_exec import adjust_notional_via_ticks, perp_close, perp_open
from qtb.costs.model import funding_pnl
from qtb.data.binance_futures import slice_trades_for_bar

from .crypto_fsm import CryptoBookFSM
from .data import DualDataset
from .signals import compute_anchor, drawdown_from_anchor
from .tech_fsm import TechFSM, tech_directional_only, tech_long_grid_only, tech_short_only_exposure
from .universe import (
    CRYPTO_BOOK,
    GLOBAL_RESERVE,
    TECH_BOOK,
    TECH_SYMBOLS,
    TOTAL_CAPITAL,
    DualParams,
    TechParams,
)

FUT_FEE = {"maker": 0.00008, "taker": 0.0002}


def _fee(rebate: float) -> FeeSpec:
    return FeeSpec(FUT_FEE["maker"], FUT_FEE["taker"], rebate)


@dataclass
class LegState:
    name: str
    book: Literal["tech", "crypto", "reserve"]
    symbol: str
    direction: Literal["long", "short"]
    mode: Literal["grid", "directional", "cash"]
    state: _PerpState
    target_notional: float = 0.0
    leverage: float = 1.5
    spec: GridSpec | None = None
    grid_pnl: float = 0.0
    dir_pnl: float = 0.0
    short_pnl: float = 0.0


@dataclass
class PortfolioResult:
    name: str
    params: DualParams
    timestamps: list[Any]
    total_equity: np.ndarray
    tech_equity: np.ndarray
    crypto_equity: np.ndarray
    reserve: np.ndarray
    trades: list[TradeRec]
    liquidated: bool
    liquidation_count: int
    components: dict[str, float]
    regime_log: list[dict[str, Any]] = field(default_factory=list)
    extras: dict[str, Any] = field(default_factory=dict)

    @property
    def final_equity(self) -> float:
        return float(self.total_equity[-1]) if len(self.total_equity) else 0.0


def _leg_equity(leg: LegState, px: float) -> float:
    return _perp_equity(leg.state, px, include_reserve=False, isolated=True)


def _rebalance_leg(
    leg: LegState,
    i: int,
    px: float,
    target_notional: float,
    fee: FeeSpec,
    fill: FillConfig,
) -> None:
    """Move position toward target notional via taker rebalance."""
    st = leg.state
    if st.liquidated:
        return
    sign = 1.0 if leg.direction == "long" else -1.0
    cur_notional = abs(st.qty) * px
    delta = target_notional - cur_notional
    if abs(delta) < px * 0.001:
        return
    qty = abs(delta) / px
    notional = qty * px
    fee_paid, reb = fee.fee_and_rebate(notional, maker=False)
    lev = max(leg.leverage, 1.0)
    margin = notional / lev

    if delta > 0:
        if st.wallet < fee_paid + margin:
            scale = max(st.wallet - fee_paid, 0.0) / max(margin, 1e-12)
            qty *= scale
            notional = qty * px
            fee_paid, reb = fee.fee_and_rebate(notional, maker=False)
            margin = notional / lev
        if qty <= 0 or st.wallet < fee_paid + margin:
            return
        signed = sign * qty
        st.wallet -= fee_paid + margin
        st.locked += margin
        new = abs(st.qty) * st.avg + notional
        st.qty += signed
        st.avg = new / abs(st.qty) if st.qty else 0.0
        st.fees += fee_paid
        st.rebates += reb
        st.turnover += notional
    else:
        close_qty = min(qty, abs(st.qty))
        if close_qty <= 0:
            return
        notional = close_qty * px
        fee_paid, reb = fee.fee_and_rebate(notional, maker=False)
        raw = close_qty * (px - st.avg) * (1.0 if st.qty > 0 else -1.0)
        frac = close_qty / abs(st.qty)
        release = st.locked * frac
        st.wallet += release + raw - fee_paid
        st.locked = max(0.0, st.locked - release)
        st.qty = st.qty - np.sign(st.qty) * close_qty
        if abs(st.qty) < 1e-12:
            st.qty = 0.0
            st.avg = 0.0
            st.locked = 0.0
        st.realized += raw - fee_paid
        st.fees += fee_paid
        st.rebates += reb
        st.turnover += notional
        if leg.direction == "short":
            st.short_pnl = getattr(st, "short_pnl", 0.0) + raw - fee_paid  # type: ignore[attr-defined]


def _process_grid_fills(
    leg: LegState,
    i: int,
    o: float,
    h: float,
    l: float,
    c: float,
    qv: float,
    atr: float,
    atr_step: float,
    atr_range: float,
    fee: FeeSpec,
    fill: FillConfig,
    reanchor: bool,
    bar_trades: pd.DataFrame | None = None,
    tick_precise: bool = False,
) -> bool:
    st = leg.state
    if st.liquidated or leg.mode != "grid" or leg.target_notional <= 0:
        return False
    sign = 1.0 if leg.direction == "long" else -1.0
    if leg.spec is None or (reanchor and leg.spec and (c < leg.spec.lower or c > leg.spec.upper)):
        leg.spec = native_spec(c, max(atr, c * 0.002), atr_step, atr_range, "geometric")
        st.lots = {k: v for k, v in st.lots.items() if 0 <= k < len(leg.spec.levels)}

    spec = leg.spec
    assert spec is not None
    remaining = max(leg.target_notional - abs(st.qty) * c, 0.0)
    empty = max(1, sum(1 for k, lvl in enumerate(spec.levels) if k not in st.lots and (
        (leg.direction == "long" and lvl <= spec.mid) or (leg.direction == "short" and lvl >= spec.mid)
    )))
    baseline = remaining / empty
    pending: list[PendingFill] = []
    if leg.direction == "long":
        for idx, lvl in enumerate(spec.levels):
            if idx in st.lots or lvl > spec.mid:
                continue
            qsz = grid_quote_size(baseline, float(lvl), spec, "fixed_usdt", atr, atr, 1.0)
            if qsz >= 1.0:
                pending.append(PendingFill("buy", float(lvl), idx, notional=qsz, reason="grid"))
        for idx, lot_qty in list(st.lots.items()):
            si = idx + 1
            if si < len(spec.levels):
                pending.append(PendingFill("sell", float(spec.levels[si]), si, qty=lot_qty, reduce_only=True, reason="grid_tp"))
    else:
        for idx, lvl in enumerate(spec.levels):
            if idx in st.lots or lvl < spec.mid:
                continue
            qsz = grid_quote_size(baseline, float(lvl), spec, "fixed_usdt", atr, atr, 1.0)
            if qsz >= 1.0:
                pending.append(PendingFill("sell", float(lvl), idx, notional=qsz, reason="grid"))
        for idx, lot_qty in list(st.lots.items()):
            si = idx - 1
            if si >= 0:
                pending.append(PendingFill("buy", float(spec.levels[si]), si, qty=lot_qty, reduce_only=True, reason="grid_tp"))

    if bar_trades is not None and not bar_trades.empty:
        tick = infer_tick(float(c), fill.tick_size)
        fill_t = FillConfig(fill.mode, fill.participation, fill.extra_ticks, fill.extra_slip_bps, tick)
        fills = resolve_tick_fills(pending, bar_trades, fill_t, bar_open=o, bar_close=c)
        for tf in fills:
            if tf.reduce_only:
                lot_idx = tf.level_idx - 1 if leg.direction == "long" else tf.level_idx + 1
                perp_close(
                    st, leg.direction, tf.qty, tf.price, fee,
                    maker=True, level_idx=lot_idx if lot_idx in st.lots else None, is_grid=True,
                )
            elif tf.side == "buy" and leg.direction == "long":
                perp_open(st, leg.direction, leg.leverage, tf.qty, tf.price, fee, maker=True, level_idx=tf.level_idx)
            elif tf.side == "sell" and leg.direction == "short":
                perp_open(st, leg.direction, leg.leverage, tf.qty, tf.price, fee, maker=True, level_idx=tf.level_idx)
        return True

    if tick_precise:
        raise RuntimeError(
            f"tick_precise: grid leg {leg.name} missing aggTrades — refuse bar OHLC approximation"
        )

    fills = resolve_bar_fills(pending, o, h, l, c, quote_volume=qv, cfg=fill)
    for pf in fills:
        px = pf.price
        if pf.side == "buy" and leg.direction == "long":
            qty = (pf.notional or 0.0) / px if pf.qty is None else pf.qty
            _rebalance_leg(leg, i, px, abs(st.qty) * px + qty * px, fee, fill)
        elif pf.side == "sell" and leg.direction == "long" and pf.reduce_only:
            _rebalance_leg(leg, i, px, max(abs(st.qty) * px - (pf.qty or 0) * px, 0), fee, fill)
    return False


def _load_bar_trades(
    md,
    bar_ts: pd.Timestamp,
    interval: str,
    *,
    tech_tick_fills: bool,
    crypto_tick_fills: bool,
    tick_precise: bool,
) -> pd.DataFrame | None:
    if md is None:
        return None
    use_ticks = (
        (md.data_source == "binance" and getattr(md, "trades_lazy", False))
        and (tech_tick_fills if md.symbol in TECH_SYMBOLS else crypto_tick_fills)
    )
    if not use_ticks:
        return None
    if md.trades is not None and not md.trades.empty:
        return slice_trades_for_bar(md.trades, bar_ts, interval)
    if getattr(md, "trades_lazy", False):
        from qtb.data.binance_futures import fetch_agg_trades_day

        day_df = fetch_agg_trades_day(md.perp, bar_ts.date(), cache_only=True)
        if day_df.empty:
            if tick_precise:
                raise RuntimeError(f"Missing aggTrades cache for {md.perp} on {bar_ts.date()}")
            return None
        return slice_trades_for_bar(day_df, bar_ts, interval)
    return None


def run_dual_portfolio(
    data: DualDataset,
    params: DualParams,
    *,
    name: str = "dual",
    fill_mode: str = "base",
    benchmark: str | None = None,
    crypto_tick_fills: bool = False,
    tech_tick_fills: bool = True,
    tech_disabled: bool = False,
    tick_precise: bool = False,
    tech_tick_only: bool = True,
) -> PortfolioResult:
    """Run dual-engine strategy or named benchmark on aligned dataset."""
    soxl = data.tech["SOXL"].bars
    snxx = data.tech["SNXX"].bars
    n = len(soxl)
    ts = soxl["timestamp"].tolist()
    fill = FillConfig.preset(fill_mode)  # type: ignore[arg-type]
    fee = _fee(params.tech.rebate)

    if benchmark == "B1_cash":
        r = run_cash(soxl, TOTAL_CAPITAL, "B1_cash")
        return _from_engine(r, params, name)

    if benchmark == "B2_buy_hold":
        if tick_precise and data.tech["SOXL"].trades_lazy:
            return _run_tick_tech_benchmark(
                data, params, name, fill_mode, fee, fill, tick_precise,
                mode="hold", benchmark=benchmark,
            )
        r = run_perp_grid(
            soxl, name="B2_buy_hold", symbol="SOXLUSDT", fee=fee, fill=fill,
            initial=TECH_BOOK, hold_only=True, target_notional=TECH_BOOK * params.tech.leverage,
            leverage_hint=params.tech.leverage, interval=data.interval,
        )
        return _from_engine(r, params, name, scale=TECH_BOOK / TOTAL_CAPITAL)

    if benchmark in ("B3_long_grid_only", "B4_directional_long_only"):
        if tick_precise and data.tech["SOXL"].trades_lazy:
            mode = "directional" if benchmark == "B4_directional_long_only" else "grid"
            return _run_tick_tech_benchmark(
                data, params, name, fill_mode, fee, fill, tick_precise,
                mode=mode, benchmark=benchmark,
            )
        hold = benchmark == "B4_directional_long_only"
        r = run_perp_grid(
            soxl,
            name=benchmark,
            symbol="SOXLUSDT",
            fee=fee,
            fill=fill,
            initial=TECH_BOOK,
            dir_frac=0.60 if hold else 0.0,
            hold_only=hold,
            target_notional=TECH_BOOK * params.tech.leverage * 0.6,
            leverage_hint=params.tech.leverage,
            atr_step=params.tech.grid_atr_step,
            atr_range=params.tech.grid_atr_range,
            interval=data.interval,
        )
        return _from_engine(r, params, name, scale=TECH_BOOK / TOTAL_CAPITAL)

    # Dual strategy path
    warm = min(_warmup_bars(data.interval), max(n // 8, 24))
    soxl_c = soxl["close"].to_numpy(float)
    soxl_h = soxl["high"].to_numpy(float)
    soxl_l = soxl["low"].to_numpy(float)
    snxx_c = snxx["close"].to_numpy(float)
    anchor = compute_anchor(soxl_c, params.tech.anchor, rolling_n=20 * 24)
    dd_series = drawdown_from_anchor(soxl_c, anchor)

    atr_s = rolling_atr(soxl_h, soxl_l, soxl_c, 24 if params.tech.atr_tf == "1h" else 96)

    tech_fsm = TechFSM(params.tech)
    crypto_fsm = CryptoBookFSM(params.crypto)

    margin_frac = float(params.margin_frac)
    margin_frac = min(max(margin_frac, 0.05), 0.99)
    reserve_frac = 1.0 - margin_frac
    tech_deploy = TECH_BOOK * margin_frac
    tech_book_reserve = TECH_BOOK * reserve_frac
    crypto_deploy = CRYPTO_BOOK * margin_frac
    crypto_book_reserve = CRYPTO_BOOK * reserve_frac
    reserve_pool = GLOBAL_RESERVE + crypto_book_reserve

    def _mk_leg(nm: str, book: str, sym: str, direction: str, mode: str, cap: float) -> LegState:
        st = _PerpState(wallet=cap, reserve=0.0)
        return LegState(nm, book, sym, direction, mode, st, leverage=params.tech.leverage if book == "tech" else params.crypto.leverage)  # type: ignore[arg-type]

    legs = [
        _mk_leg("soxl_short", "tech", "SOXL", "short", "directional", tech_deploy * 0.4),
        _mk_leg("soxl_long_grid", "tech", "SOXL", "long", "grid", tech_deploy * 0.35),
        _mk_leg("soxl_long_dir", "tech", "SOXL", "long", "directional", tech_deploy * 0.25),
        _mk_leg("snxx_long", "tech", "SNXX", "long", "directional", tech_book_reserve),
    ]
    crypto_symbols = tuple(s for s in ("BTC", "ETH", "SOL") if s in data.crypto)
    crypto_caps = crypto_deploy / max(len(crypto_symbols), 1)
    for sym in crypto_symbols:
        legs.append(_mk_leg(f"{sym.lower()}_long", "crypto", sym, "long", "grid", crypto_caps))

    total_eq = np.full(n, TOTAL_CAPITAL)
    tech_eq = np.full(n, TECH_BOOK)
    crypto_eq = np.full(n, CRYPTO_BOOK)
    res_eq = np.full(n, GLOBAL_RESERVE)
    trades: list[TradeRec] = []
    regime_log: list[dict] = []
    liq_count = 0
    reanchor = params.tech.reanchor != "off"

    crypto_bars = {
        s: {
            "close": data.crypto[s].bars["close"].to_numpy(float),
            "high": data.crypto[s].bars["high"].to_numpy(float),
            "low": data.crypto[s].bars["low"].to_numpy(float),
        }
        for s in crypto_symbols
    }

    def _bar_trades_for(md, bar_ts: pd.Timestamp) -> pd.DataFrame | None:
        return _load_bar_trades(
            md, bar_ts, data.interval,
            tech_tick_fills=tech_tick_fills,
            crypto_tick_fills=crypto_tick_fills,
            tick_precise=tick_precise,
        )

    for i in range(n):
        px = float(soxl_c[i])
        bar_ts_soxl = pd.Timestamp(soxl["timestamp"].iloc[i])
        bar_ts_snxx = pd.Timestamp(snxx["timestamp"].iloc[i])
        soxl_trades = _bar_trades_for(data.tech["SOXL"], bar_ts_soxl)
        snxx_trades = _bar_trades_for(data.tech["SNXX"], bar_ts_snxx)
        if i >= warm:
            tech_exp = tech_fsm.on_bar(i, float(dd_series[i]), soxl_c, soxl_h, soxl_l, snxx_c)
            crypto_exp = crypto_fsm.on_bar(
                i, crypto_bars,
                tech_signal_dd=float(dd_series[i]) if params.unified_signal else None,
                unified=params.unified_signal,
            )

            # Map exposure to legs (scale targets to deployable book capital)
            book_cap = tech_deploy
            short_tgt = tech_exp.short_notional_frac * book_cap
            grid_tgt = tech_exp.long_grid_frac * book_cap
            dir_tgt = tech_exp.long_dir_frac * book_cap
            snxx_tgt = tech_exp.snxx_long_frac * book_cap

            legs[0].target_notional = short_tgt
            legs[1].target_notional = grid_tgt if not tech_exp.pause_long_grid else grid_tgt * 0.3
            legs[2].target_notional = dir_tgt
            legs[3].target_notional = snxx_tgt

            for sym in crypto_symbols:
                leg = next(l for l in legs if l.symbol == sym)
                ce = crypto_exp.get(sym)
                if ce:
                    leg.target_notional = (ce.long_grid_frac + ce.long_dir_frac) * crypto_caps

            if tech_tick_only and tick_precise:
                for leg in legs[4:]:
                    md = data.crypto.get(leg.symbol)
                    if md is None or not getattr(md, "trades_lazy", False):
                        leg.target_notional = 0.0

            if tech_disabled:
                for leg in legs[:4]:
                    leg.target_notional = 0.0

            regime_log.append({
                "ts": str(ts[i]),
                "dd": float(dd_series[i]),
                "phase": tech_exp.phase,
                "tier": tech_exp.dd_tier,
            })

        # Funding
        for leg in legs:
            st = leg.state
            if leg.symbol == "SOXL":
                fr = float(soxl["funding_rate"].iloc[i])
            elif leg.symbol == "SNXX":
                fr = float(snxx["funding_rate"].iloc[i])
            elif leg.symbol in crypto_bars:
                fr = float(data.crypto[leg.symbol].bars["funding_rate"].iloc[i])
            else:
                fr = 0.0
            if st.qty != 0 and abs(fr) > 0:
                pnl = funding_pnl(st.qty, float(soxl["open"].iloc[i]), fr)
                st.wallet += pnl
                if pnl < 0:
                    st.funding_paid += -pnl
                else:
                    st.funding_recv += pnl

        if i >= warm:
            qv = float(soxl["quote_volume"].iloc[i]) if "quote_volume" in soxl.columns else 0.0
            atr = float(atr_s[i])
            if not tech_disabled:
                for leg in legs[:4]:
                    if leg.symbol == "SOXL":
                        bar_trades = soxl_trades
                        mark_px = px
                        o, h, l = float(soxl["open"].iloc[i]), float(soxl["high"].iloc[i]), float(soxl["low"].iloc[i])
                    else:
                        bar_trades = snxx_trades
                        mark_px = float(snxx_c[i])
                        o, h, l = float(snxx["open"].iloc[i]), float(snxx["high"].iloc[i]), float(snxx["low"].iloc[i])
                    if tick_precise and tech_tick_fills and (bar_trades is None or bar_trades.empty):
                        raise RuntimeError(
                            f"tick_precise: no aggTrades in bar {bar_ts_soxl if leg.symbol == 'SOXL' else bar_ts_snxx} "
                            f"for {leg.symbol} — refuse bar approximation"
                        )
                    if leg.mode == "grid":
                        _process_grid_fills(
                            leg, i, o, h, l, mark_px, qv if leg.symbol == "SOXL" else float(snxx["quote_volume"].iloc[i]),
                            atr if leg.symbol == "SOXL" else float(
                                rolling_atr(snxx["high"].to_numpy(float), snxx["low"].to_numpy(float), snxx_c, 24)[i]
                            ),
                            params.tech.grid_atr_step, params.tech.grid_atr_range,
                            fee, fill, reanchor,
                            bar_trades=bar_trades,
                            tick_precise=tick_precise,
                        )
                    if bar_trades is not None and not bar_trades.empty:
                        adjust_notional_via_ticks(
                            leg.state, leg.direction, leg.leverage,
                            leg.target_notional, bar_trades, fee, fill,
                        )
                    elif not tick_precise or not tech_tick_fills:
                        _rebalance_leg(leg, i, mark_px, leg.target_notional, fee, fill)

            for leg in legs[4:]:
                md = data.crypto.get(leg.symbol)
                if tech_tick_only and tick_precise and (md is None or not getattr(md, "trades_lazy", False)):
                    continue
                cpx = float(data.crypto[leg.symbol].bars["close"].iloc[i])
                bar_ts = pd.Timestamp(data.crypto[leg.symbol].bars["timestamp"].iloc[i])
                bar_trades = _bar_trades_for(md, bar_ts)
                if (
                    tick_precise
                    and crypto_tick_fills
                    and getattr(md, "trades_lazy", False)
                    and (bar_trades is None or bar_trades.empty)
                ):
                    raise RuntimeError(
                        f"tick_precise: no aggTrades in bar {bar_ts} for {leg.symbol} — refuse bar approximation"
                    )
                used_ticks = False
                if leg.mode == "grid" and leg.target_notional > 0:
                    atr_c = float(
                        rolling_atr(
                            data.crypto[leg.symbol].bars["high"].to_numpy(float),
                            data.crypto[leg.symbol].bars["low"].to_numpy(float),
                            data.crypto[leg.symbol].bars["close"].to_numpy(float),
                            24,
                        )[i]
                    )
                    qv_c = float(data.crypto[leg.symbol].bars["quote_volume"].iloc[i]) if "quote_volume" in data.crypto[leg.symbol].bars.columns else 0.0
                    crypto_grid_tick = tick_precise and crypto_tick_fills
                    used_ticks = _process_grid_fills(
                        leg, i,
                        float(data.crypto[leg.symbol].bars["open"].iloc[i]),
                        float(data.crypto[leg.symbol].bars["high"].iloc[i]),
                        float(data.crypto[leg.symbol].bars["low"].iloc[i]),
                        cpx, qv_c, atr_c,
                        params.crypto.grid_atr_step, params.crypto.grid_atr_range,
                        fee, fill, reanchor=True,
                        bar_trades=bar_trades,
                        tick_precise=crypto_grid_tick,
                    )
                if bar_trades is not None and not bar_trades.empty:
                    adjust_notional_via_ticks(
                        leg.state, leg.direction, leg.leverage,
                        leg.target_notional, bar_trades, fee, fill,
                    )
                elif not tick_precise or not crypto_tick_fills:
                    _rebalance_leg(leg, i, cpx, leg.target_notional, fee, fill)

        # Liquidation check (isolated, simplified)
        for leg in legs:
            st = leg.state
            if st.qty == 0:
                continue
            mark = px if leg.symbol == "SOXL" else float(
                snxx_c[i] if leg.symbol == "SNXX" else data.crypto[leg.symbol].bars["close"].iloc[i]
            )
            e = _perp_equity(st, mark, include_reserve=False, isolated=True)
            m = abs(st.qty) * mark * 0.005
            if e <= m:
                st.liq_loss += max(e, 0)
                st.qty = 0.0
                st.avg = 0.0
                st.locked = 0.0
                st.liquidated = True
                st.liq_count += 1
                liq_count += 1

        t_e = 0.0
        for l in legs[:4]:
            if l.symbol == "SOXL":
                mark = float(soxl_trades["price"].iloc[-1]) if soxl_trades is not None and not soxl_trades.empty else px
            else:
                mark = float(snxx_trades["price"].iloc[-1]) if snxx_trades is not None and not snxx_trades.empty else float(snxx_c[i])
            t_e += _leg_equity(l, mark)
        c_e = 0.0
        for l in legs[4:]:
            md = data.crypto[l.symbol]
            bt = _bar_trades_for(md, pd.Timestamp(md.bars["timestamp"].iloc[i]))
            mark = float(bt["price"].iloc[-1]) if bt is not None and not bt.empty else float(md.bars["close"].iloc[i])
            c_e += _leg_equity(l, mark)
        total_eq[i] = t_e + c_e + reserve_pool
        tech_eq[i] = t_e
        crypto_eq[i] = c_e
        res_eq[i] = reserve_pool

    components = {
        "futures_fee": sum(l.state.fees for l in legs),
        "rebate": sum(l.state.rebates for l in legs),
        "net_funding": sum(l.state.funding_recv - l.state.funding_paid for l in legs),
        "turnover": sum(l.state.turnover for l in legs),
        "liquidation_loss": sum(l.state.liq_loss for l in legs),
    }
    return PortfolioResult(
        name=name,
        params=params,
        timestamps=ts,
        total_equity=total_eq,
        tech_equity=tech_eq,
        crypto_equity=crypto_eq,
        reserve=res_eq,
        trades=trades,
        liquidated=liq_count > 0,
        liquidation_count=liq_count,
        components=components,
        regime_log=regime_log,
        extras={"benchmark": benchmark, "fill": fill_mode, "execution": "tick_aggTrades" if tick_precise else "bar"},
    )


def _run_tick_tech_benchmark(
    data: DualDataset,
    params: DualParams,
    name: str,
    fill_mode: str,
    fee: FeeSpec,
    fill: FillConfig,
    tick_precise: bool,
    *,
    mode: Literal["hold", "grid", "directional"],
    benchmark: str,
) -> PortfolioResult:
    """SOXL-only benchmark on Binance aggTrades — same tick engine as dual strategy."""
    soxl = data.tech["SOXL"].bars
    n = len(soxl)
    ts = soxl["timestamp"].tolist()
    warm = min(_warmup_bars(data.interval), max(n // 8, 24))
    soxl_c = soxl["close"].to_numpy(float)
    soxl_h = soxl["high"].to_numpy(float)
    soxl_l = soxl["low"].to_numpy(float)
    atr_s = rolling_atr(soxl_h, soxl_l, soxl_c, 24 if params.tech.atr_tf == "1h" else 96)
    reanchor = params.tech.reanchor != "off"
    target = TECH_BOOK * params.tech.leverage * (0.6 if mode != "hold" else 1.0)

    st = _PerpState(wallet=TECH_BOOK, reserve=0.0)
    leg = LegState(
        name, "tech", "SOXL",
        "long", "grid" if mode == "grid" else "directional", st,
        target_notional=target, leverage=params.tech.leverage,
    )
    total_eq = np.full(n, TOTAL_CAPITAL)
    tech_eq = np.full(n, TECH_BOOK)
    liq_count = 0

    for i in range(n):
        px = float(soxl_c[i])
        bar_ts = pd.Timestamp(soxl["timestamp"].iloc[i])
        bar_trades = _load_bar_trades(
            data.tech["SOXL"], bar_ts, data.interval,
            tech_tick_fills=True, crypto_tick_fills=False, tick_precise=tick_precise,
        ) if tick_precise else None
        if tick_precise and (bar_trades is None or bar_trades.empty):
            raise RuntimeError(f"tick_precise benchmark {benchmark}: no aggTrades at {bar_ts}")

        if i >= warm:
            qv = float(soxl["quote_volume"].iloc[i]) if "quote_volume" in soxl.columns else 0.0
            atr = float(atr_s[i])
            if mode == "grid":
                _process_grid_fills(
                    leg, i,
                    float(soxl["open"].iloc[i]), float(soxl["high"].iloc[i]),
                    float(soxl["low"].iloc[i]), px, qv, atr,
                    params.tech.grid_atr_step, params.tech.grid_atr_range,
                    fee, fill, reanchor, bar_trades=bar_trades, tick_precise=tick_precise,
                )
            if bar_trades is not None and not bar_trades.empty:
                adjust_notional_via_ticks(st, leg.direction, leg.leverage, target, bar_trades, fee, fill)
            elif not tick_precise:
                _rebalance_leg(leg, i, px, target, fee, fill)

        mark = float(bar_trades["price"].iloc[-1]) if bar_trades is not None and not bar_trades.empty else px
        te = _leg_equity(leg, mark)
        tech_eq[i] = te
        total_eq[i] = te + CRYPTO_BOOK + GLOBAL_RESERVE

    return PortfolioResult(
        name=name,
        params=params,
        timestamps=ts,
        total_equity=total_eq,
        tech_equity=tech_eq,
        crypto_equity=np.full(n, CRYPTO_BOOK),
        reserve=np.full(n, GLOBAL_RESERVE),
        trades=[],
        liquidated=liq_count > 0,
        liquidation_count=liq_count,
        components={
            "futures_fee": st.fees,
            "rebate": st.rebates,
            "net_funding": st.funding_recv - st.funding_paid,
            "turnover": st.turnover,
            "liquidation_loss": st.liq_loss,
        },
        extras={"benchmark": benchmark, "fill": fill_mode, "execution": "tick_aggTrades"},
    )


def _from_engine(r: EngineResult, params: DualParams, name: str, scale: float = 1.0) -> PortfolioResult:
    tech_eq = np.asarray(r.equity, dtype=float)
    if tech_eq[0] > 0:
        tech_eq = tech_eq / tech_eq[0] * TECH_BOOK
    total_eq = tech_eq + CRYPTO_BOOK + GLOBAL_RESERVE
    return PortfolioResult(
        name=name,
        params=params,
        timestamps=list(r.timestamps),
        total_equity=total_eq,
        tech_equity=tech_eq,
        crypto_equity=np.full(len(r.equity), CRYPTO_BOOK),
        reserve=np.full(len(r.equity), GLOBAL_RESERVE),
        trades=r.trades,
        liquidated=r.liquidated,
        liquidation_count=r.liquidation_count,
        components=dict(r.components),
        extras={"benchmark": name},
    )
