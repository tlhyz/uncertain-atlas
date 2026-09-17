# 模式：点名 snapshot-discover-nothalt 杠

**层次**：实现 / Offer 被拒 not already empty / not already halted / not already settled 正式三事（322 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应**：[`../tracks/implementation/worked-example-snapshot-discover-nothalt-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-discover-nothalt-vs-bundled.md)。

- **Offer 被拒 不是已经没有快照：** 看见被拒，不是已经没有快照 interchangeable / 958 snapshot-discover-nothalt interchangeable。
- **看见拒了邻居 不是已经停：** 看见拒了邻居，不是已经停 interchangeable。
- **看见能中止 不是已经交差：** 看见能中止，不是已经发现完 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 被拒 正式三事（322 余量），先数清问的是是不是已经没有快照、是不是已经停、还是看见能中止是不是已经交差，再决定要不要同一次发布。322 snapshot-discover vs offer bundled unbundling 在本页 item 3 完成。
