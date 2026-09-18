# 模式：点名 ffields-notinfo 杠

**层次**：实现 / Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应**：[`../tracks/implementation/worked-example-ffields-notinfo-vs-bundled.md`](../tracks/implementation/worked-example-ffields-notinfo-vs-bundled.md)。

- **Info 回应用状态 不是已经是握手对齐：** 看见能回，不是已经是握手对齐 interchangeable / 1111 ffields-notinfo interchangeable。
- **看见写了应用状态 不是已经是快照重放：** 看见写了应用状态，不是已经是快照重放 interchangeable。
- **看见能查 不是已经交差：** 看见能查，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 回应用状态 正式三事（407 余量），先数清问的是是不是已经是握手对齐、是不是已经是快照重放、还是看见能查是不是已经交差，再决定要不要同一次发布。407 finfields vs equiv bundled unbundling 在本页 item 3 完成。
