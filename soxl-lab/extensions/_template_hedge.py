"""Copy to a name that does not start with _ , then it auto-loads.

Example (do not name this file without the underscore unless you want it live):

    from src.analysis.grid_ext import register_hedge, register_yaml_keys
    from src.analysis.user_moving_grid import run_user_hedge_pair

    def flatten_then_wait(bars, **kw):
        # extras 里是 YAML 里引擎不认识的键
        return run_user_hedge_pair(bars, **kw)

    register_yaml_keys("pause_hours")
    register_hedge("flatten_then_wait", flatten_then_wait, label="爆仓后停，和内置一样的示例")
"""
