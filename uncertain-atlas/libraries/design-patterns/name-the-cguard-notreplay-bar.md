# 模式：点名 cguard-notreplay 杠

**层次**：实现 / CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-cguard-notreplay-vs-bundled.md`](../tracks/implementation/worked-example-cguard-notreplay-vs-bundled.md)。

- **来源 不是已经保证不重放：** 看见送来了，不是已经保证不重放 interchangeable / 1104 cguard-notreplay interchangeable。
- **看见能来自邻居 不是已经过了 CheckTx 就有应用级保护：** 看见能来自邻居，不是已经过了 CheckTx 就有应用级保护 interchangeable。
- **看见能来自用户 不是已经交差：** 看见能来自用户，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看来源 正式三事（405 余量），先数清问的是是不是已经保证不重放、是不是已经过了 CheckTx 就有应用级保护、还是看见能来自用户是不是已经交差，再决定要不要同一次发布。405 checktxguard vs optional bundled unbundling 在本页 item 2 续。
