# 模式：把 InitChain 请求 app_state_bytes not already verified / not already balances / not already settled 正式三事（388 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain ≠ bundled（388）](../../tracks/implementation/worked-example-initparams-notverified-vs-bundled.md)。

## 三个名字

1. **app_state_bytes 不是已经验过应用状态：** 看见填了 JSON 字节，不是已经 303 interchangeable / 766 initparams-notverified interchangeable。
2. **看见填了 JSON 字节 不是已经懂余额：** 看见有字节，不是已经 303 interchangeable。
3. **看见能填 不是已经交差：** 看见 InitChain 请求 app_state_bytes，不是已经交差 interchangeable。

官方把 InitChain 请求 consensus_params / validators / app_state_bytes 三条核心句拆成三个名字。把它们叫成一个「看见填了 InitChain 请求余栏就已经没有参数」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 app_state_bytes 正式三事（388 余量），先数清问的是是不是已经验过应用状态 / 303、是不是已经懂余额、还是看见能填是不是已经交差，再决定要不要同一次发布。388 initparams vs empty bundled unbundling 在本页 item 3 完成。
