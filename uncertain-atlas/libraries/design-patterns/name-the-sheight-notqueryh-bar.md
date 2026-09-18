# 模式：点名 sheight-notqueryh 杠

**层次**：实现 / Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-sheight-notqueryh-vs-bundled.md`](../tracks/implementation/worked-example-sheight-notqueryh-vs-bundled.md)。

- **Snapshot.height 不是已经是 Query 高度：** 看见填了 height，不是已经是 Query 高度 interchangeable / 1106 sheight-notqueryh interchangeable。
- **看见写成 Commit 之后 不是已经装完：** 看见写成 Commit 之后，不是已经装完 interchangeable。
- **看见有高度 不是已经交差：** 看见有高度，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Snapshot.height 正式三事（406 余量），先数清问的是是不是已经是 Query 高度、是不是已经装完、还是看见有高度是不是已经交差，再决定要不要同一次发布。406 snapheight vs queryh bundled unbundling 在本页 item 1 启动。
