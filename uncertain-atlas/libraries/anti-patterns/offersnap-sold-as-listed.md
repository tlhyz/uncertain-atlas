# 反模式：看见 OfferSnapshot 请求 snapshot 是拿来装回的那份快照就当成已经是本地清单 / 看见 OfferSnapshot 回包 result 是这次 Offer 的结果就当成已经装完 / 看见 OfferSnapshot 在用 state sync 引导节点时叫就当成已经必须实现快照连接

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**例**：[OfferSnapshot 请求 snapshot 是拿来装回的那份快照 ≠ 已经是本地清单](../../tracks/implementation/worked-example-offersnap-vs-listed.md)。

## 塌法

1. 看见 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照 / 看见填了 snapshot，就当成已经是本地清单，或当成已经是同一份。
2. 看见 OfferSnapshot 回包 `result` 是这次 Offer 的结果 / 看见回了 result，就当成已经装完，或当成已经收下。
3. 看见 OfferSnapshot 在用 state sync 引导节点时叫 / 看见在引导时叫了，就当成已经必须实现快照连接，或当成已经切进共识。

## 为什么会出事

官方写：`snapshot` 是拿来装回的那份快照。`result` 是这次 Offer 的结果。`OfferSnapshot` 在用 state sync 引导节点时叫。

## 和相邻反模式

- [offersnapusage-bootstrap-sold-as-bundled](offersnapusage-bootstrap-sold-as-bundled.md) 是 OfferSnapshot Usage bootstrap accept/reject 正式三事，不是本页 OfferSnapshot 请求 bundled 三事专用边界。
- [listsnapempty-sold-as-discovery](listsnapempty-sold-as-discovery.md) 是 ListSnapshots 回包 snapshots 是本地状态快照清单就已经是同一份，不是本页这种 OfferSnapshot 请求 snapshot 是拿来装回的那份快照不是已经是本地清单。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完，不是本页这种 OfferSnapshot 回包 result 是这次 Offer 的结果不是已经装完。
- [snapshotconn-sold-as-required](snapshotconn-sold-as-required.md) 是四门里有 Snapshot Connection 就已经必须实现快照，不是本页这种 OfferSnapshot 在用 state sync 引导节点时叫不是已经必须实现快照连接。
