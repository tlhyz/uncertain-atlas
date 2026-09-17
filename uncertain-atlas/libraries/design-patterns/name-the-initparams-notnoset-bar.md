# 模式：把 InitChain 请求 validators not already no set / not already empty list / not already settled 正式三事（388 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain ≠ bundled（388）](../../tracks/implementation/worked-example-initparams-notnoset-vs-bundled.md)。

## 三个名字

1. **validators 不是已经没有集合：** 看见填了起步名单，不是已经 318 interchangeable / 765 initparams-notnoset interchangeable。
2. **看见填了起步名单 不是已经用了回包空名单：** 看见有这份请求栏，不是已经 318 interchangeable。
3. **看见能回 不是已经交差：** 看见 InitChain 请求 validators，不是已经交差 interchangeable。

官方把 InitChain 请求 consensus_params / validators / app_state_bytes 三条核心句拆成三个名字。把它们叫成一个「看见填了 InitChain 请求余栏就已经没有参数」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 validators 正式三事（388 余量），先数清问的是是不是已经没有集合 / 318、是不是已经用了回包空名单、还是看见能回是不是已经交差，再决定要不要同一次发布。388 initparams vs empty bundled unbundling 在本页 item 2 续。
