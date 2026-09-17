# 模式：把创世三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md)。  
**例**：[创世 app_state ≠ 已经验过](../../tracks/implementation/worked-example-genesis-vs-app.md)。

## 三个名字

1. **应用段：** 看见创世里的 app_state 不是已经验过应用状态。
2. **空坐：** 看见节点已经启动不是已经过了 genesis_time 开始出块。
3. **起步可空：** 看见创世 validators 空不是已经没有集合，看见 app_hash 空不是已经没有根。

## 为什么要分开叫

官方把引擎验不了应用段、起来后空坐到指定时刻、名单和根可以留给 InitChain，写成三件事。把它们叫成一个「看见创世就已经开链」，会把快照重放和本头 AppHash 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「创世已经齐」，先数清问的是应用段、空坐，还是起步可空，再决定要不要同一次发布。
