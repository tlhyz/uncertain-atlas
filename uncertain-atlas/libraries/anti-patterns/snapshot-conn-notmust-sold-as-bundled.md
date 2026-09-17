# 反模式：把 四门里有 Snapshot Connection not already must implement snapshots / not already snapshotted / not already settled 正式三事（334 余量） 卖成 已经必须实现快照 / 已经拍过快照 / 已经交差

**层次**：实现 / Snapshot Connection。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-conn-notmust-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-conn-notmust-vs-bundled.md)。

官方把四门里有 Snapshot Connection / 给人快照或给自己装回 / 应用选择不实现 三条核心句写成三件独立的实现事。把它们卖成已经必须实现快照 / 已经拍过快照 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看四门里有 Snapshot Connection 正式三事（334 余量），必须分开 not already must implement snapshots、not already snapshotted、not already settled 三件事，不要和 334 / 322 / 321 / 933 / 934 糊成一句。

## 和相邻反模式

- [checktx-weak-notproc-sold-as-bundled](checktx-weak-notproc-sold-as-bundled.md) 是 ProcessProposal 还不是 CheckTx 边界（339/931），不是本页四门还不是必须做快照边界。
- ListSnapshots 回了已经齐是不变量 322，不是本页门在仍可选实现边界。
