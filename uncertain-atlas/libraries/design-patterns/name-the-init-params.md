# 模式：把 InitChain 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain 请求 consensus_params 是起步共识参数 ≠ 已经没有参数](../../tracks/implementation/worked-example-initparams-vs-empty.md)。

## 三个名字

1. **InitChain 请求 consensus_params 是起步共识参数不是已经没有参数：** 看见填了起步参数不是已经用了回包空参数。
2. **InitChain 请求 validators 是起步验证者名单不是已经没有集合：** 看见填了起步名单不是已经用了回包空名单。
3. **InitChain 请求 app_state_bytes 是序列化起步应用状态不是已经验过应用状态：** 看见填了 JSON 字节不是已经懂余额。

## 为什么要分开叫

官方把 InitChain 请求 `consensus_params` 是起步共识参数、`validators` 是起步验证者名单、`app_state_bytes` 是序列化起步应用状态写成三件事。把它们叫成一个「看见填了 InitChain 请求余栏就已经没有参数」，会把起步参数、起步名单和验过应用状态一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 InitChain 请求余栏就已经没有参数」，先数清问的是 InitChain 请求 consensus_params 是起步共识参数不是已经没有参数、InitChain 请求 validators 是起步验证者名单不是已经没有集合，还是 InitChain 请求 app_state_bytes 是序列化起步应用状态不是已经验过应用状态，再决定要不要同一次发布。
