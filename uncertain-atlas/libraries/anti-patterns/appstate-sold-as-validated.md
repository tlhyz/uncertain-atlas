# 反模式：看见创世 app_state 就当成已经验过应用状态 / 看见节点起来就当成已经过了 genesis_time / 看见创世 validators 空就当成已经没有集合

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md)。  
**例**：[创世 app_state ≠ 已经验过](../../tracks/implementation/worked-example-genesis-vs-app.md)。

## 塌法

1. 看见创世里的 app_state / 看见引擎收下这份创世，就当成已经验过应用状态。
2. 看见节点已经启动 / 看见进程起来了，就当成已经过了 genesis_time 开始出块。
3. 看见创世 validators 空 / 看见 app_hash 空，就当成已经没有集合，或当成已经没有根。
4. 看见 InitChain 被叫了，就当成已经过了四门。
5. 看见创世文件齐了，就当成快照已经从创世重放。

## 为什么会出事

官方写：引擎不知道应用状态由什么组成，所以验不了 `app_state`。节点可以在 `genesis_time` 之前起来并空坐。名单和根起步可以空，留给 `InitChain`。

## 和相邻反模式

- [state-sold-as-block](state-sold-as-block.md) 是本地 State ≠ 已经进了块，不是本页这种创世文件。
- [statesync-sold-as-genesis](statesync-sold-as-genesis.md) 是快照 ≠ 已经从创世重放，不是本页。
