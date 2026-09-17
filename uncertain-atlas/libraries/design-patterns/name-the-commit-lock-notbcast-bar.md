# 模式：点名 commit-lock-notbcast 杠

**层次**：实现 / Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应**：[`../tracks/implementation/worked-example-commit-lock-notbcast-vs-bundled.md`](../tracks/implementation/worked-example-commit-lock-notbcast-vs-bundled.md)。

- **Commit 里等广播 不是已经能往下走：** 看见能调广播，不是已经能继续 interchangeable / 976 commit-lock-notbcast interchangeable。
- **看见能调广播 不是已经允许写进 Commit：** 看见能调广播，不是已经允许 interchangeable。
- **看见同步内存池调用 不是已经交差：** 看见同步内存池调用，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 里等广播 正式三事（310 余量），先数清问的是是不是已经能往下走、是不是已经允许、还是看见同步内存池调用是不是已经交差，再决定要不要同一次发布。310 commit-lock vs rpc bundled unbundling 在本页 item 3 完成。
