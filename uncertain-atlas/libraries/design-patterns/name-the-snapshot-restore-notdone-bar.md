# 模式：点名 snapshot-restore-notdone 杠

**层次**：实现 / Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应**：[`../tracks/implementation/worked-example-snapshot-restore-notdone-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-restore-notdone-vs-bundled.md)。

- **Offer 收下 不是已经装完：** 看见收下了 Offer，不是已经装完 interchangeable / 959 snapshot-restore-notdone interchangeable。
- **看见选了这份 不是已经有了全部块：** 看见选了这份，不是已经有块 interchangeable。
- **看见元数据对上 不是已经交差：** 看见元数据对上，不是已经验过 AppHash interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下 正式三事（321 余量），先数清问的是是不是已经装完、是不是已经有了全部块、还是看见元数据对上是不是已经交差，再决定要不要同一次发布。321 snapshot-restore vs offer bundled unbundling 在本页 item 1 启动。
