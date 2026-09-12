"""Full hang-parameter sweep for Gate spot grid on official ETF deals."""

from __future__ import annotations

import json
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import product
from pathlib import Path
from typing import Any

import pandas as pd

from qtb.config import load_config
from qtb.data.gatedata import DEFAULT_ETF_3X, load_cached_deals
from qtb.engine.spot_grid import run_spot_moving_grid

SYMBOLS = list(DEFAULT_ETF_3X)
RANGE_DOWN = (0.0, 0.02, 0.05)
RANGE_UP = (0.05, 0.10, 0.15, 0.20)
GRID_COUNT = (10, 20)
MOVE = ("none", "up", "both")
SELLS_ONLY = (False, True)
WINDOWS = ("full", "late")


def generate_combos() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for down, up, n, move, sells_only in product(
        RANGE_DOWN, RANGE_UP, GRID_COUNT, MOVE, SELLS_ONLY
    ):
        rows.append(
            {
                "range_down_pct": float(down),
                "range_up_pct": float(up),
                "grid_count": int(n),
                "move": move,
                "sells_only": bool(sells_only),
                "allow_move_up": move in {"up", "both"},
                "allow_move_down": move == "both",
                "shift_on_exit": move != "none",
            }
        )
    return rows


# Official-tape V shapes: drop then rally. `from_high` opens before the dump;
# `from_trough` opens after the dump, on the way back up.
V_WINDOWS: list[dict[str, str]] = [
    # SOXL3L 0.81 → 0.34 → 0.88
    {"id": "SOXL3L_jun_high", "scenario": "from_high", "symbol": "SOXL3L_USDT",
     "start": "2026-06-26", "end": "2026-07-01"},
    {"id": "SOXL3L_jun_trough", "scenario": "from_trough", "symbol": "SOXL3L_USDT",
     "start": "2026-06-28", "end": "2026-07-01"},
    # SOXL3S 1.12 → 0.71 → 1.84
    {"id": "SOXL3S_jun_high", "scenario": "from_high", "symbol": "SOXL3S_USDT",
     "start": "2026-06-30", "end": "2026-07-03"},
    {"id": "SOXL3S_jun_trough", "scenario": "from_trough", "symbol": "SOXL3S_USDT",
     "start": "2026-07-01", "end": "2026-07-03"},
    # SNXX3L first day 1.00 → 0.46 → 2.35
    {"id": "SNXX3L_open_high", "scenario": "from_high", "symbol": "SNXX3L_USDT",
     "start": "2026-07-29", "end": "2026-07-31"},
    {"id": "SNXX3L_open_trough", "scenario": "from_trough", "symbol": "SNXX3L_USDT",
     "start": "2026-07-30", "end": "2026-07-31"},
    # SNXX3L 2.17 → 0.47 → 4.05
    {"id": "SNXX3L_aug_high", "scenario": "from_high", "symbol": "SNXX3L_USDT",
     "start": "2026-08-05", "end": "2026-08-18"},
    {"id": "SNXX3L_aug_trough", "scenario": "from_trough", "symbol": "SNXX3L_USDT",
     "start": "2026-08-08", "end": "2026-08-18"},
    # SOXL3S 0.57 → 0.43 → 0.96
    {"id": "SOXL3S_aug_high", "scenario": "from_high", "symbol": "SOXL3S_USDT",
     "start": "2026-08-17", "end": "2026-08-25"},
    {"id": "SOXL3S_aug_trough", "scenario": "from_trough", "symbol": "SOXL3S_USDT",
     "start": "2026-08-18", "end": "2026-08-25"},
]


def _slice_tape(
    tape: pd.DataFrame,
    window: str,
    start: str | None = None,
    end: str | None = None,
) -> pd.DataFrame:
    if start or end:
        ts = pd.to_datetime(tape["timestamp"], utc=True)
        mask = pd.Series(True, index=tape.index)
        if start:
            mask &= ts >= pd.Timestamp(start, tz="UTC")
        if end:
            mask &= ts < pd.Timestamp(end, tz="UTC")
        out = tape.loc[mask].copy()
    elif window == "full" or tape.empty:
        out = tape
    elif window == "late":
        ts = pd.to_datetime(tape["timestamp"], utc=True)
        cut = ts.min() + (ts.max() - ts.min()) / 2
        out = tape.loc[ts >= cut].copy()
    else:
        raise ValueError(f"unknown window {window}")
    if out.empty:
        raise ValueError(f"empty tape for window={window} start={start} end={end}")
    out.attrs.update(tape.attrs)
    return out.reset_index(drop=True)


def _run_job(job: dict[str, Any]) -> dict[str, Any]:
    tape = load_cached_deals(job["symbol"], start=job["deals_from"], end=job["deals_to"])
    cut = _slice_tape(
        tape,
        job["window"],
        start=job.get("start"),
        end=job.get("end"),
    )
    cfg = load_config("configs/backtest_etf_moving_grid.yaml")
    cfg["symbol"] = job["symbol"]
    strat = cfg.setdefault("strategy", {})
    combo = job["combo"]
    n = int(combo["grid_count"])
    strat.update(
        {
            "grid_count": n,
            "range_up_pct": combo["range_up_pct"],
            "range_down_pct": combo["range_down_pct"],
            "spacing_mode": "arithmetic",
            "spacing_pct": None,
            "sells_only": combo["sells_only"],
            "allow_move_up": combo["allow_move_up"],
            "allow_move_down": combo["allow_move_down"],
            "shift_on_exit": combo["shift_on_exit"],
            "open_base_inventory": True,
            "quote_capital": 2000.0,
            "order_size_quote": 2000.0 / n,
        }
    )
    result = run_spot_moving_grid(cfg, cut)
    m = result.metrics
    return {
        "symbol": job["symbol"],
        "window": job["window"],
        "range_down_pct": combo["range_down_pct"],
        "range_up_pct": combo["range_up_pct"],
        "grid_count": combo["grid_count"],
        "move": combo["move"],
        "sells_only": combo["sells_only"],
        "n_prints": m.get("n_prints"),
        "first_px": m.get("first_print_px"),
        "last_px": m.get("last_print_px"),
        "arb": m.get("arb_rounds"),
        "n_win": m.get("n_win_sells"),
        "n_loss": m.get("n_loss_sells"),
        "grid_profit": m.get("grid_profit"),
        "mtm": m.get("unrealized_pnl"),
        "net": m.get("net_pnl"),
        "equity": m.get("end_equity"),
        "max_dd_pct": m.get("max_dd_pct"),
        "shifts": m.get("grid_shifts"),
        "n_base": m.get("n_base_buys"),
        "end_quote": m.get("end_quote"),
        "inv": m.get("quote_in_inventory"),
        "gap": m.get("pnl_identity_gap"),
        "scenario": job.get("scenario") or job["window"],
        "seg_id": job.get("seg_id") or job["window"],
    }


def _jobs(symbols: list[str], deals_from: str, deals_to: str) -> list[dict[str, Any]]:
    jobs = []
    for combo in generate_combos():
        for symbol in symbols:
            for window in WINDOWS:
                jobs.append(
                    {
                        "symbol": symbol,
                        "window": window,
                        "deals_from": deals_from,
                        "deals_to": deals_to,
                        "combo": combo,
                    }
                )
    return jobs


def _combo_key(row: pd.Series | dict[str, Any]) -> tuple:
    return (
        float(row["range_down_pct"]),
        float(row["range_up_pct"]),
        int(row["grid_count"]),
        str(row["move"]),
        bool(row["sells_only"]),
    )


def rank_combos(frame: pd.DataFrame) -> pd.DataFrame:
    """One row per hang combo: full-tape and late-restart robustness."""
    full = frame[frame["window"] == "full"].copy()
    late = frame[frame["window"] == "late"].copy()
    keys = ["range_down_pct", "range_up_pct", "grid_count", "move", "sells_only"]

    def _agg(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
        g = df.groupby(keys, as_index=False).agg(
            **{
                f"{prefix}_median_eq": ("equity", "median"),
                f"{prefix}_mean_eq": ("equity", "mean"),
                f"{prefix}_min_eq": ("equity", "min"),
                f"{prefix}_max_eq": ("equity", "max"),
                f"{prefix}_median_net": ("net", "median"),
                f"{prefix}_median_profit": ("grid_profit", "median"),
                f"{prefix}_median_mtm": ("mtm", "median"),
                f"{prefix}_median_dd": ("max_dd_pct", "median"),
                f"{prefix}_n_green": ("equity", lambda s: int((s >= 2000.0).sum())),
            }
        )
        return g

    out = _agg(full, "full")
    out = out.merge(_agg(late, "late"), on=keys, how="left")
    # Robust rank: worst symbol on the full tape, then late worst symbol.
    out["score"] = (
        out["full_min_eq"] * 0.50
        + out["full_median_eq"] * 0.30
        + out["late_min_eq"].fillna(0.0) * 0.20
    )
    return out.sort_values(["score", "full_min_eq", "full_median_eq"], ascending=False).reset_index(drop=True)


def write_sweep_report(frame: pd.DataFrame, ranked: pd.DataFrame, out_dir: Path) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "etf_grid_sweep.csv"
    rank_path = out_dir / "etf_grid_sweep_rank.csv"
    json_path = out_dir / "etf_grid_sweep.json"
    md_path = out_dir / "etf_grid_sweep.md"
    frame.to_csv(csv_path, index=False)
    ranked.to_csv(rank_path, index=False)

    best = ranked.iloc[0].to_dict()
    top = ranked.head(10)
    family = (
        frame[frame["window"] == "full"]
        .groupby(["move", "sells_only", "range_down_pct"], as_index=False)
        .agg(median_eq=("equity", "median"), min_eq=("equity", "min"), mean_eq=("equity", "mean"))
        .sort_values("min_eq", ascending=False)
    )

    def _fmt_row(r: pd.Series) -> str:
        sells = "只卖" if r["sells_only"] else "买卖都挂"
        return (
            f"| {r['range_down_pct']:.0%} | {r['range_up_pct']:.0%} | {int(r['grid_count'])} | "
            f"{r['move']} | {sells} | {r['full_min_eq']:.1f} | {r['full_median_eq']:.1f} | "
            f"{r['late_min_eq']:.1f} | {r['score']:.1f} |"
        )

    lines = [
        "# ETF 现货网格全量挂法扫描",
        "",
        "四个 3 倍币官方逐笔（2026-06..08，SNXX 从 7 月起）。2000U，等差，突破移动。",
        f"组合数 {len(generate_combos())}，窗口 `full`（第一笔开到结束）和 `late`（后半段重新开仓）。",
        "",
        "排序看的是钱包，不是网格利润：`score = 0.5×全程最差币 + 0.3×全程中位 + 0.2×后半最差币`。",
        "「最优」必须四个币里最差的那个也不能崩，且后半段重开也还站得住。",
        "",
        "## 最优组合",
        "",
        f"- 下 {best['range_down_pct']:.0%} / 上 {best['range_up_pct']:.0%} / {int(best['grid_count'])} 格 / "
        f"移动 `{best['move']}` / {'只挂卖' if best['sells_only'] else '买卖都挂'}",
        f"- 全程最差币权益 {best['full_min_eq']:.2f}，中位 {best['full_median_eq']:.2f}，"
        f"后半最差 {best['late_min_eq']:.2f}",
        "",
        "## Top 10",
        "",
        "| 下 | 上 | 格 | 移动 | 挂法 | 全程最差 | 全程中位 | 后半最差 | score |",
        "|---:|---:|---:|---|---|---:|---:|---:|---:|",
    ]
    for _, r in top.iterrows():
        lines.append(_fmt_row(r))
    lines.extend(
        [
            "",
            "## 按族汇总（全程）",
            "",
            "| 移动 | 只卖 | 下沿 | 中位权益 | 最差权益 | 平均权益 |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for _, r in family.iterrows():
        lines.append(
            f"| {r['move']} | {r['sells_only']} | {r['range_down_pct']:.0%} | "
            f"{r['median_eq']:.1f} | {r['min_eq']:.1f} | {r['mean_eq']:.1f} |"
        )
    lines.extend(
        [
            "",
            "## 怎么读",
            "",
            "- 只卖 + 不准下移：底仓上方分批止盈，卖完空仓。全程最好看时，往往是第一天就出完货。",
            "- 买卖都挂 + 双边移动：官方默认味道，3 倍币急跌里最差。",
            "- 后半段重开是防过拟合：第一天碰巧冲过上沿的组合，换个开仓日会翻脸。",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")
    payload = {
        "n_combos": len(generate_combos()),
        "n_rows": int(len(frame)),
        "best": {k: (None if pd.isna(v) else v) for k, v in best.items()},
        "top10": top.to_dict(orient="records"),
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    return {
        "csv": str(csv_path),
        "rank": str(rank_path),
        "json": str(json_path),
        "md": str(md_path),
    }


def _run_jobs(jobs: list[dict[str, Any]], workers: int) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    with ProcessPoolExecutor(max_workers=max(int(workers), 1)) as pool:
        futs = [pool.submit(_run_job, job) for job in jobs]
        for i, fut in enumerate(as_completed(futs), start=1):
            rows.append(fut.result())
            if i % 80 == 0 or i == len(futs):
                print(f"[sweep] {i}/{len(futs)}", flush=True)
    return pd.DataFrame(rows)


def rank_v_combos(frame: pd.DataFrame, scenario: str) -> pd.DataFrame:
    keys = ["range_down_pct", "range_up_pct", "grid_count", "move", "sells_only"]
    sub = frame[frame["scenario"] == scenario].copy()
    out = sub.groupby(keys, as_index=False).agg(
        median_eq=("equity", "median"),
        mean_eq=("equity", "mean"),
        min_eq=("equity", "min"),
        max_eq=("equity", "max"),
        median_net=("net", "median"),
        median_profit=("grid_profit", "median"),
        median_mtm=("mtm", "median"),
        n_green=("equity", lambda s: int((s >= 2000.0).sum())),
        n_seg=("seg_id", "nunique"),
    )
    out["score"] = out["min_eq"] * 0.6 + out["median_eq"] * 0.4
    return out.sort_values(["score", "min_eq", "median_eq"], ascending=False).reset_index(drop=True)


def write_v_report(
    frame: pd.DataFrame,
    high_rank: pd.DataFrame,
    trough_rank: pd.DataFrame,
    out_dir: Path,
) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "etf_vshape_sweep.csv"
    frame.to_csv(csv_path, index=False)
    high_rank.to_csv(out_dir / "etf_vshape_rank_from_high.csv", index=False)
    trough_rank.to_csv(out_dir / "etf_vshape_rank_from_trough.csv", index=False)

    def _top_lines(ranked: pd.DataFrame, title: str) -> list[str]:
        lines = [
            f"## {title}",
            "",
            "| 下 | 上 | 格 | 移动 | 挂法 | 最差段 | 中位 | 绿段数 | score |",
            "|---:|---:|---:|---|---|---:|---:|---:|---:|",
        ]
        for _, r in ranked.head(8).iterrows():
            sells = "只卖" if r["sells_only"] else "买卖都挂"
            lines.append(
                f"| {r['range_down_pct']:.0%} | {r['range_up_pct']:.0%} | {int(r['grid_count'])} | "
                f"{r['move']} | {sells} | {r['min_eq']:.1f} | {r['median_eq']:.1f} | "
                f"{int(r['n_green'])}/{int(r['n_seg'])} | {r['score']:.1f} |"
            )
        return lines

    bh = high_rank.iloc[0]
    bt = trough_rank.iloc[0]
    lines = [
        "# 先跌后涨区间：全量挂法扫描",
        "",
        "从官方逐笔里挑了 5 段 V 型（先跌后涨），每段两种开仓：",
        "- `from_high`：下跌前开（对应「现在开、预估先跌后涨」）",
        "- `from_trough`：跌完再开（对应「等低点再买」）",
        "",
        "144 挂法 × 10 段 = 1440 次回测。分数 = 0.6×最差段 + 0.4×中位。",
        "",
        f"- 下跌前开最优：下 {bh['range_down_pct']:.0%} / 上 {bh['range_up_pct']:.0%} / "
        f"{int(bh['grid_count'])} 格 / {bh['move']} / {'只卖' if bh['sells_only'] else '买卖都挂'}；"
        f"最差段 {bh['min_eq']:.1f}，中位 {bh['median_eq']:.1f}",
        f"- 低点再开最优：下 {bt['range_down_pct']:.0%} / 上 {bt['range_up_pct']:.0%} / "
        f"{int(bt['grid_count'])} 格 / {bt['move']} / {'只卖' if bt['sells_only'] else '买卖都挂'}；"
        f"最差段 {bt['min_eq']:.1f}，中位 {bt['median_eq']:.1f}",
        "",
    ]
    lines.extend(_top_lines(high_rank, "下跌前开仓 Top 8"))
    lines.append("")
    lines.extend(_top_lines(trough_rank, "低点再开仓 Top 8"))
    lines.extend(
        [
            "",
            "## 区间",
            "",
            "| id | 开仓 | 合约 | 起 | 止 |",
            "|---|---|---|---|---|",
        ]
    )
    for w in V_WINDOWS:
        lines.append(
            f"| {w['id']} | {w['scenario']} | {w['symbol']} | {w['start']} | {w['end']} |"
        )
    md_path = out_dir / "etf_vshape_sweep.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"csv": str(csv_path), "md": str(md_path)}


def run_v_shape_sweep(
    deals_from: str = "2026-06",
    deals_to: str = "2026-08",
    workers: int = 4,
    out_dir: str | Path = "outputs",
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, str]]:
    jobs = []
    for combo in generate_combos():
        for seg in V_WINDOWS:
            jobs.append(
                {
                    "symbol": seg["symbol"],
                    "window": seg["id"],
                    "start": seg["start"],
                    "end": seg["end"],
                    "scenario": seg["scenario"],
                    "seg_id": seg["id"],
                    "deals_from": deals_from,
                    "deals_to": deals_to,
                    "combo": combo,
                }
            )
    frame = _run_jobs(jobs, workers)
    high_rank = rank_v_combos(frame, "from_high")
    trough_rank = rank_v_combos(frame, "from_trough")
    written = write_v_report(frame, high_rank, trough_rank, Path(out_dir))
    return frame, high_rank, trough_rank, written


def run_etf_sweep(
    symbols: list[str] | None = None,
    deals_from: str = "2026-06",
    deals_to: str = "2026-08",
    workers: int = 4,
    out_dir: str | Path = "outputs",
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, str]]:
    symbols = list(symbols or SYMBOLS)
    jobs = _jobs(symbols, deals_from, deals_to)
    frame = _run_jobs(jobs, workers)
    ranked = rank_combos(frame)
    written = write_sweep_report(frame, ranked, Path(out_dir))
    return frame, ranked, written
