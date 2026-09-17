# 模式：点名 snapshot-take-notcons 杠

**层次**：实现 / 没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应**：[`../tracks/implementation/worked-example-snapshot-take-notcons-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-take-notcons-vs-bundled.md)。

- **没停链 不是已经隔离在单一高度：** 看见没停链，不是已经隔离 interchangeable / 951 snapshot-take-notcons interchangeable。
- **看见在后台拍 不是已经各节点字节相同：** 看见在后台拍，不是已经各节点相同 interchangeable。
- **看见同一高度 不是已经交差：** 看见同一高度，不是已经同一格式 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没停链 正式三事（324 余量），先数清问的是是不是已经隔离、是不是已经各节点相同、还是看见同一高度是不是已经交差，再决定要不要同一次发布。324 snapshot-take vs commit bundled unbundling 在本页 item 2 续。
