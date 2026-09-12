# 模式：把 InitChain 请求三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain 请求 time 是创世时间 ≠ 已经过了 genesis_time](../../tracks/implementation/worked-example-inittime-vs-genesis.md)。

## 三个名字

1. **InitChain 请求 time 是创世时间不是已经过了 genesis_time：** 看见填了 time 不是已经开出块。
2. **InitChain 请求 chain_id 是链的 ID 不是已经有了 ChainID：** 看见填了 chain_id 不是已经有完整历史。
3. **InitChain 请求 initial_height 是起步块高度不是已经能跳步：** 看见填了起步高不是已经过了崩溃三步。

## 为什么要分开叫

官方把 InitChain 请求 `time` 是创世时间、`chain_id` 是链的 ID、`initial_height` 是起步块高度写成三件事。把它们叫成一个「看见叫了 InitChain 就已经过了 genesis_time」，会把创世时间、ChainID 和能跳步一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 InitChain 就已经过了 genesis_time」，先数清问的是 InitChain 请求 time 是创世时间不是已经过了 genesis_time、InitChain 请求 chain_id 是链的 ID 不是已经有了 ChainID，还是 InitChain 请求 initial_height 是起步块高度不是已经能跳步，再决定要不要同一次发布。
