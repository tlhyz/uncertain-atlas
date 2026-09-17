# 模式：点名 snapshot-restore-notchunk 杠

**层次**：实现 / 一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应**：[`../tracks/implementation/worked-example-snapshot-restore-notchunk-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-restore-notchunk-vs-bundled.md)。

- **一块 chunk 收下 不是已经齐：** 看见收下一块，不是已经齐 interchangeable / 960 snapshot-restore-notchunk interchangeable。
- **看见回了再拉 不是已经封禁：** 看见回了再拉，不是已经封禁 interchangeable。
- **看见能回指令 不是已经交差：** 看见能回指令，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一块 chunk 收下 正式三事（321 余量），先数清问的是是不是已经齐、是不是已经封禁、还是看见能回指令是不是已经交差，再决定要不要同一次发布。321 snapshot-restore vs offer bundled unbundling 在本页 item 2 续。
