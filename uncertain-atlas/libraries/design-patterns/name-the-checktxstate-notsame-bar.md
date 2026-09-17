# 模式：点名 checktxstate-notsame 杠

**层次**：实现 / 同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应**：[`../tracks/implementation/worked-example-checktxstate-notsame-vs-bundled.md`](../tracks/implementation/worked-example-checktxstate-notsame-vs-bundled.md)。

- **同时在改 不是已经同一份：** 看见两边都在改，不是已经同一份 interchangeable / 969 checktxstate-notsame interchangeable。
- **看见并发 不是已经合并：** 看见并发，不是已经合并 interchangeable。
- **看见都叫 CheckTx / Finalize 不是已经交差：** 看见都叫 CheckTx / Finalize，不是已经共用一份工作状态 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同时在改 正式三事（312 余量），先数清问的是是不是已经同一份、是不是已经合并、还是看见都叫 CheckTx / Finalize 是不是已经交差，再决定要不要同一次发布。312 checktxstate vs execute bundled unbundling 在本页 item 2 续。
