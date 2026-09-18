# 反模式：把 Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量） 写成已经 已经全字段对上 / 已经在装回当中增量验过 / 已经交差

**层次**：实现 / Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-sheight-notmeta-vs-bundled.md`](../tracks/implementation/worked-example-sheight-notmeta-vs-bundled.md)。

把 Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量） 写成已经 已经全字段对上 / 已经在装回当中增量验过 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Snapshot.metadata 正式三事（406 余量），必须分开 not already all-fields-match、not already incrementally-verified、not already settled 三件事，不要和 406 / 368 / 332 / 1106 / 1108 糊成一句。

也不是：

- [sheight-notqueryh-sold-as-bundled](sheight-notqueryh-sold-as-bundled.md) 是拍快照高度仍未是 Query 高度单句边界（1106 item 1），不是本页任意元数据仍未全字段对上边界。
- 快照全字段（含 Metadata）对上就已经装完是不变量 368，不是本页有块哈希仍未增量验过边界。
