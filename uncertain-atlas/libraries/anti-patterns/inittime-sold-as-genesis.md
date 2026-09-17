# 反模式：看见 InitChain 请求 time 是创世时间就当成已经过了 genesis_time / 看见 InitChain 请求 chain_id 是链的 ID 就当成已经有了 ChainID / 看见 InitChain 请求 initial_height 是起步块高度就当成已经能跳步

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain 请求 time 是创世时间 ≠ 已经过了 genesis_time](../../tracks/implementation/worked-example-inittime-vs-genesis.md)。

## 塌法

1. 看见 InitChain 请求 `time` 是创世时间 / 看见填了 time，就当成已经过了 genesis_time，或当成已经开出块。
2. 看见 InitChain 请求 `chain_id` 是链的 ID / 看见填了 chain_id，就当成已经有了 ChainID，或当成已经有完整历史。
3. 看见 InitChain 请求 `initial_height` 是起步块高度 / 看见填了起步高，就当成已经能跳步，或当成已经过了崩溃三步。

## 为什么会出事

官方写：`time` 是创世时间。`chain_id` 是这条链的 ID。`initial_height` 是起步块的高度，通常是 1。

## 和相邻反模式

- [appstate-sold-as-validated](appstate-sold-as-validated.md) 是进程起来就已经过了 genesis_time，不是本页这种 InitChain 请求 time 是创世时间不是已经过了 genesis_time。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是快照装完就已经有了 ChainID，不是本页这种 InitChain 请求 chain_id 是链的 ID 不是已经有了 ChainID。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是启动 Info 对上就已经能跳步，不是本页这种 InitChain 请求 initial_height 是起步块高度不是已经能跳步。
