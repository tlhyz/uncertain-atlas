# 模式：点名 crashrec-notahead 杠

**层次**：实现 / 应用比引擎高 not already allowed / not already recover-alone / not already same-as-atomic 正式三事（320 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Crash Recovery。  
**对应**：[`../tracks/implementation/worked-example-crashrec-notahead-vs-bundled.md`](../tracks/implementation/worked-example-crashrec-notahead-vs-bundled.md)。

- **应用比引擎高 不是已经允许：** 看见应用先写完，不是已经合法 interchangeable / 1019 crashrec-notahead interchangeable。
- **看见两边高度不一样 不是已经能各醒各的：** 看见两边高度不一样，不是已经能各醒各的 interchangeable。
- **看见能单独重启应用 不是已经和半写已经原子同一句：** 看见能单独重启应用，不是已经和半写已经原子同一句 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用比引擎高 正式三事（320 余量），先数清问的是是不是已经允许、是不是已经能各醒各的、还是看见能单独重启应用是不是已经和半写已经原子同一句，再决定要不要同一次发布。320 crash-steps vs commit bundled unbundling 在本页 item 1 启动。
