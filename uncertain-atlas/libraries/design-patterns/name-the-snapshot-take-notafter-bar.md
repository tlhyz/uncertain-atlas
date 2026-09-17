# 模式：点名 snapshot-take-notafter 杠

**层次**：实现 / 拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应**：[`../tracks/implementation/worked-example-snapshot-take-notafter-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-take-notafter-vs-bundled.md)。

- **拍了这个高度 不是已经交差之后拍的：** 看见标了高度，不是已经交差之后拍 interchangeable / 950 snapshot-take-notafter interchangeable。
- **看见拍了 不是已经没有更高高度的数据：** 看见拍了，不是已经没有后面高度 interchangeable。
- **看见字段在 不是已经交差：** 看见字段在，不是已经隔离在这一高度 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拍了这个高度 正式三事（324 余量），先数清问的是是不是已经交差之后拍的、是不是已经没有更高高度、还是看见字段在是不是已经交差，再决定要不要同一次发布。324 snapshot-take vs commit bundled unbundling 在本页 item 1 启动。
