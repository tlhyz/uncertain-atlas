# 例：看见应用选择不实现 is not already no-state-sync-object interchangeable / not already genesis-only interchangeable / not already settled interchangeable

**层次**：实现 / 应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事（334 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事（334 余量）/ not 934 snapshot-conn-notgone interchangeable / not 334 snapshot-conn-vs-required bundled interchangeable」，不是快照连接 bundled（334），也不是只有 AppHash 可信任（38），也不是 Query 回了已经是正常运转必须有（329）。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

1. **看见应用选择不实现 / 看见快照管理可选 这份选择 is not already 已经没有 state sync 这条对象 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 934 snapshot-conn-notgone interchangeable / 932 snapshot-conn-notmust interchangeable / 334 snapshot-conn item 1 四门 interchangeable，也不是已经应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事 bundled（334 item 3 余量） interchangeable / 334 snapshot-conn item 3 interchangeable。**  
   官方写：应用可以不实现。这不是已经删掉 state sync 这个对象。看见可选，不是已经没有这条对象 interchangeable——本页从 334 item 3 侧钉 not already no-state-sync-object 单句。334 snapshot-conn vs required bundled unbundling 在本页 item 3 完成。

2. **看见可选 / 看见应用可以不实现 / 这份选择 is not already 已经从创世是唯一合法路径 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 934 snapshot-conn-notgone interchangeable / 334 snapshot-conn item 2 给人快照 interchangeable / 933 snapshot-conn-notboth interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-trust interchangeable。**  
   官方把可选和已经等于从创世分开——334 bundled 第三件事常与 38 / 329 混成「看见不实现就已经没有 state sync 或已经是 Query 那种实现了也不是必须有 interchangeable」，本页钉 not already genesis-only 单句。

3. **看见可选 / 看见应用可以不实现 / 这份选择 is not already 已经交差 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 934 snapshot-conn-notgone interchangeable / 932 snapshot-conn-notmust interchangeable，也不是已经 Query 回了已经是正常运转必须有 interchangeable / 329 query-replicated interchangeable。**  
   官方把可选和已经问过邻居、已经齐了快照清单 / 已经交差分开。看见可选，不是已经交差 interchangeable。334 snapshot-conn vs required bundled unbundling 在本页 item 3 完成。

怎样实现 ListSnapshots / OfferSnapshot / LoadSnapshotChunk / ApplySnapshotChunk、怎样配 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **应用选择不实现 not already no-state-sync-object ≠ 已经没有 state sync 这条对象 interchangeable：** 官方把可选实现和这条对象还在分开。
- **看见可选 not already genesis-only ≠ 已经从创世是唯一合法路径 interchangeable：** 官方把可选和已经等于从创世分开。
- **看见可选 not already settled ≠ 已经交差 interchangeable：** 官方把可选和已经清单齐了 / 已经交差分开；334 snapshot-conn vs required bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用选择不实现 | 不是已经没有 state sync 这条对象 | 不是只有 AppHash 可信任（38） |
| 看见快照管理可选 | 不是已经从创世是唯一合法路径 | 不是 Query 回了已经是正常运转必须有（329） |
| 看见可选 | 不是已经交差 | 不是四门就已经必须实现（932） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用选择不实现 not already no-state-sync-object / not already genesis-only / not already settled 正式三事（334 余量），必须分开是不是已经没有 state sync 这条对象、是不是已经从创世是唯一合法路径、是不是已经交差。可以跳过「看见可选就已经没有这条对象」。第一版默认可从创世。不要另写怎样实现快照方法或怎样配 state sync。334 snapshot-conn vs required bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现 ListSnapshots / OfferSnapshot / LoadSnapshotChunk / ApplySnapshotChunk、怎样配 state sync。
- 快照连接 bundled。那是不变量 334。
- 四门就已经必须实现。那是不变量 334 item 1 余量 / 932。
- 只有 AppHash 可信任。那是不变量 38。
- Query 回了已经是正常运转必须有。那是不变量 329。
