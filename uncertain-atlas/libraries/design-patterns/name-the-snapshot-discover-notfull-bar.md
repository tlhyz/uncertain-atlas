# 模式：点名 snapshot-discover-notfull 杠

**层次**：实现 / ListSnapshots 回了 not already all-snapshots / not already unbounded / not already settled 正式三事（322 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应**：[`../tracks/implementation/worked-example-snapshot-discover-notfull-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-discover-notfull-vs-bundled.md)。

- **ListSnapshots 回了 不是已经有了全部快照：** 看见问了，不是已经齐 interchangeable / 956 snapshot-discover-notfull interchangeable。
- **看见回了 不是已经没有上限：** 看见回了，不是已经没有上限 interchangeable。
- **看见 10 不是已经交差：** 看见 10，不是已经是不确定默认 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 回了 正式三事（322 余量），先数清问的是是不是已经齐、是不是已经没有上限、还是看见 10 是不是已经交差，再决定要不要同一次发布。322 snapshot-discover vs offer bundled unbundling 在本页 item 1 启动。
