# 例：看见四门里有 Snapshot Connection 不是已经必须实现快照；看见用来给人快照或给自己装回不是已经必须两头都做；看见应用选择不实现不是已经没有 state sync 这条对象

**层次**：实现 / Snapshot Connection。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「四门里有 Snapshot Connection 不是已经必须实现快照 / 给人快照或给自己装回不是已经必须两头都做 / 应用选择不实现不是已经没有 state sync 这条对象」，不是 ListSnapshots 已经齐，也不是只有 AppHash 可信任。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

规范把快照连接写成三件独立的实现事，不是「看见四门里有 Snapshot Connection 就必须实现快照、必须两头都做、已经没有这条对象」一件事：

1. **看见四门里有 Snapshot Connection / 看见四条连接 不是已经必须实现快照管理，也不是已经拍过快照。**  
   官方写：CometBFT 维持四条并发 ABCI 连接，其中一条是 Snapshot Connection。快照管理**可选**：应用可以不实现。看见门在，不是已经必须实现。看见四门齐了，不是已经有快照。看见连接名在，不是已经拍过或装过。
2. **看见这条连接用来给人快照 / 看见这条连接用来给自己装回 不是已经必须两头都做，也不是已经装完。**  
   官方写：Snapshot Connection 用来给别的节点提供 state sync 快照，**和 / 或** 给正在引导的本节点装回。看见能给人，不是已经必须给自己装。看见能装回，不是已经必须对外提供。看见写了「和 / 或」，不是已经两头都做了。
3. **看见应用选择不实现 / 看见快照管理可选 不是已经没有 state sync 这条对象，也不是已经从创世是唯一合法路径，也不是已经 ListSnapshots 齐了。**  
   官方写：应用可以不实现。这不是已经删掉 state sync 这个对象。也不是已经等于从创世。也不是已经问过邻居、已经齐了快照清单。看见可选，不是已经是 Query 那种「实现了也不是正常运转必须有」。

怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync 是规范里的做法，本页不抄。只有 AppHash 可信任是不变量 38，本页不抄。

## 官方为什么这样拆

- **四门里有 Snapshot Connection ≠ 已经必须实现快照：** 官方把门的存在和必须实现分开。
- **给人快照或给自己装回 ≠ 已经必须两头都做：** 官方把「和 / 或」写成可以只做一头。
- **应用选择不实现 ≠ 已经没有 state sync 这条对象：** 官方把可选实现和这条对象还在、从创世、清单齐了分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 四门里有 Snapshot Connection | 不是已经必须实现快照 | 不是 ListSnapshots 回了已经齐（322） |
| 给人快照或给自己装回 | 不是已经必须两头都做 | 不是 Offer 收下已经装完（321） |
| 应用选择不实现 | 不是已经没有 state sync 这条对象 | 不是只有 AppHash 可信任（38），也不是 Query 回了已经是正常运转必须有（329） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「四门里有 Snapshot Connection 就必须实现快照、必须两头都做、已经没有这条对象」，必须分开门在是不是已经必须实现、给人快照或给自己装回是不是已经必须两头都做、选择不实现是不是已经没有 state sync 这条对象。可以跳过「看见四门就已经必须做快照」。第一版默认可从创世。不要另写怎样实现快照方法或怎样配 state sync。334 snapshot-conn vs required bundled unbundling 完成（932 item 1 / 933 item 2 / 934 item 3）；精读 [`worked-example-snapshot-conn-notmust-vs-bundled.md`](worked-example-snapshot-conn-notmust-vs-bundled.md)（不变量 932 item 1）。

## 本页不抄

- 怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync。
- ListSnapshots 回了已经齐。那是不变量 322。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任、提供 state sync 必须轻验。那是不变量 38。
- Query 回了已经是正常运转必须有。那是不变量 329。
