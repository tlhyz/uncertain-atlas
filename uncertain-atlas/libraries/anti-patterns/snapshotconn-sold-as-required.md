# 反模式：看见四门里有 Snapshot Connection 就当成已经必须实现快照 / 看见用来给人快照或给自己装回就当成已经必须两头都做 / 看见应用选择不实现就当成已经没有 state sync 这条对象

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**例**：[四门里有 Snapshot Connection ≠ 已经必须实现快照](../../tracks/implementation/worked-example-snapshot-conn-vs-required.md)。

## 塌法

1. 看见四门里有 Snapshot Connection / 看见四条连接，就当成已经必须实现快照管理，或当成已经拍过快照。
2. 看见这条连接用来给人快照 / 看见这条连接用来给自己装回，就当成已经必须两头都做，或当成已经装完。
3. 看见应用选择不实现 / 看见快照管理可选，就当成已经没有 state sync 这条对象，或当成已经从创世是唯一合法路径，或当成已经 ListSnapshots 齐了。

## 为什么会出事

官方写：Snapshot Connection 用来给别人快照，和 / 或给正在引导的本节点装回。快照管理可选：应用可以不实现。门在不是必须实现。可选不是已经删掉这条对象，也不是已经问过邻居。

## 和相邻反模式

- [snapshotconn-notrequired-sold-as-bundled](snapshotconn-notrequired-sold-as-bundled.md) 是四门里有 Snapshot Connection 不是已经必须实现快照 item 1 单句边界，不是本页 Snapshot Connection bundled 全段。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了 ≠ 已经齐，不是本页这种门在 ≠ 必须实现。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下 ≠ 已经装完，不是本页。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query 回了 ≠ 已经是正常运转必须有，不是本页这种快照连接可选。
