# 模式：点名 ptime-notcfg 杠

**层次**：实现 / ProposeTimeout set-on-enter not already timeout-propose / not already left-critical / not already will-call 正式三事（416 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应**：[`../tracks/implementation/worked-example-ptime-notcfg-vs-bundled.md`](../tracks/implementation/worked-example-ptime-notcfg-vs-bundled.md)。

- **ProposeTimeout 不是已经填了 TimeoutPropose：** 看见设了定时，不是已经填了 TimeoutPropose interchangeable / 1094 ptime-notcfg interchangeable。
- **看见进了这一轮 不是已经离开关键路径：** 看见进了这一轮，不是已经离开关键路径 interchangeable。
- **看见有定时器 不是已经会调 Process：** 看见有定时器，不是已经会调 Process interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposeTimeout 正式三事（416 余量），先数清问的是是不是已经填了 TimeoutPropose、是不是已经离开关键路径、还是看见有定时器是不是已经会调 Process，再决定要不要同一次发布。416 proposetimeout vs process bundled unbundling 在本页 item 1 启动。
