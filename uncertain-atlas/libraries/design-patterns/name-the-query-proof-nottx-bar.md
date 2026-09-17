# 模式：点名 query-proof-nottx 杠

**层次**：实现 / 头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应**：[`../tracks/implementation/worked-example-query-proof-nottx-vs-bundled.md`](../tracks/implementation/worked-example-query-proof-nottx-vs-bundled.md)。

- **头上有 AppHash 不是已经是交易默克尔：** 看见头上有 AppHash，不是已经是 DataHash interchangeable / 947 query-proof-nottx interchangeable。
- **看见和另外两份并列 不是已经同一种锚：** 看见和另外两份并列，不是已经同一种锚 interchangeable。
- **看见交易在 不是已经交差：** 看见交易在，不是已经有这份分开的应用状态 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上有 AppHash 正式三事（325 余量），先数清问的是是不是已经是交易默克尔、是不是已经同一种锚、还是看见交易在是不是已经交差，再决定要不要同一次发布。325 query-proof vs apphash bundled unbundling 在本页 item 1 启动。
