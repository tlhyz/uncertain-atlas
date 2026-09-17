# 模式：点名 snapshot-discover-nottake 杠

**层次**：实现 / 挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应**：[`../tracks/implementation/worked-example-snapshot-discover-nottake-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-discover-nottake-vs-bundled.md)。

- **挑了最高 不是已经收下：** 看见挑了，不是已经收下 interchangeable / 957 snapshot-discover-nottake interchangeable。
- **看见最高 不是已经装完：** 看见最高，不是已经装完 interchangeable。
- **看见排过了 不是已经交差：** 看见排过了，不是已经是应用要的格式 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看挑了最高 正式三事（322 余量），先数清问的是是不是已经收下、是不是已经装完、还是看见排过了是不是已经交差，再决定要不要同一次发布。322 snapshot-discover vs offer bundled unbundling 在本页 item 2 续。
