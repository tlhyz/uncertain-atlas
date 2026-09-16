"""Copy to a name that does not start with _ , then it auto-loads.

    from src.analysis.grid_ext import register_sizer, register_yaml_keys

    def edge_heavy(*, capital, leverage, n_grids, level_idx, extras, direction, **_):
        base = capital * leverage / max(n_grids, 1)
        tilt = float(extras.get("edge_tilt", 1.0))
        # 两端更重：离中间越远越大
        mid = (n_grids - 1) / 2.0
        dist = abs(level_idx - mid) / max(mid, 1.0)
        return max(base * (1.0 + tilt * dist), 1.0)

    register_yaml_keys("edge_tilt")
    register_sizer("edge_heavy", edge_heavy)
"""
