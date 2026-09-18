# 模式：点名 sheight-notmeta 杠

**层次**：实现 / Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-sheight-notmeta-vs-bundled.md`](../tracks/implementation/worked-example-sheight-notmeta-vs-bundled.md)。

- **Snapshot.metadata 不是已经全字段对上：** 看见填了 metadata，不是已经全字段对上 interchangeable / 1107 sheight-notmeta interchangeable。
- **看见有块哈希 不是已经在装回当中增量验过：** 看见有块哈希，不是已经在装回当中增量验过 interchangeable。
- **看见能填 不是已经交差：** 看见能填，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Snapshot.metadata 正式三事（406 余量），先数清问的是是不是已经全字段对上、是不是已经在装回当中增量验过、还是看见能填是不是已经交差，再决定要不要同一次发布。406 snapheight vs queryh bundled unbundling 在本页 item 2 续。
