# 模式：点名 replayprot-notapp 杠

**层次**：实现 / 过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应**：[`../tracks/implementation/worked-example-replayprot-notapp-vs-bundled.md`](../tracks/implementation/worked-example-replayprot-notapp-vs-bundled.md)。

- **过了 CheckTx 不是已经有应用级保护：** 看见过了 CheckTx，不是已经有这套保护 interchangeable / 966 replayprot-notapp interchangeable。
- **看见索引器滤过 不是已经是应用谓词：** 看见索引器滤过，不是已经是应用谓词 interchangeable。
- **看见引擎会挡 不是已经交差：** 看见引擎会挡，不是已经把保证交给了应用 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看过了 CheckTx 正式三事（313 余量），先数清问的是是不是已经有应用级保护、是不是已经是应用谓词、还是看见引擎会挡是不是已经交差，再决定要不要同一次发布。313 replayprot vs replay bundled unbundling 在本页 item 2 续。
