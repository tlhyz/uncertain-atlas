# 例：看见应用选择不实现 / 看见快照管理可选 / 看见可选 is not already already no-object interchangeable / already genesis-only interchangeable / already listed interchangeable

**层次**：实现 / 应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量）/ not 760 snapshotconn-notgone interchangeable / not 334 snapshotconn bundled interchangeable」，不是 Snapshot Connection bundled（334），也不是四门里有 Snapshot Connection 不是已经必须实现快照（758 item 1 余量）或给人快照或给自己装回不是已经必须两头都做（759 item 2 余量）。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

规范把 Requirements 里快照管理可选、应用可以不实现 和「已经是选择不实现就已经删掉 state sync 这条对象 interchangeable / 已经是可选就已经等于从创世是唯一合法路径 interchangeable / 已经是可选就已经问过邻居、已经齐了快照清单 interchangeable / 已经是 snapshotconn bundled interchangeable」分开写成三件独立的实现事，不是「看见应用选择不实现就已经没有 state sync 这条对象 interchangeable / 就已经从创世是唯一合法路径 interchangeable / 就已经 ListSnapshots 齐了 interchangeable」一件事：

1. **看见应用选择不实现 / 看见快照管理可选 / 看见可以不实现 is not already 已经删掉 state sync 这个对象 interchangeable / 已经 no-object interchangeable / 已经没有这条对象交差 interchangeable / 334 snapshotconn bundled interchangeable / 33 four gates interchangeable / snapshotconn-sold-as-required interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 760 snapshotconn-notgone interchangeable / 334 snapshotconn item 3 interchangeable，也不是已经应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事 bundled（334 item 3 余量） interchangeable / 334 snapshotconn item 3 interchangeable，也不是已经四门里有 Snapshot Connection 不是已经必须实现（758） interchangeable / 759 snapshotconn-notbothends interchangeable / 329 query-replicated interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：应用可以不实现。这不是已经删掉 state sync 这个对象。看见选择不实现，不是已经 no-object interchangeable——334 钉 bundled 三事，本页从 item 3 侧钉 not already no-object 单句。看见快照管理可选，不是已经 Snapshot Connection bundled（334） interchangeable——334 钉 bundled，本页钉 item 3 第一件事。看见可以不实现，不是已经 Query 回了已经是正常运转必须有（329） interchangeable——329 另钉。334 snapshotconn vs required bundled unbundling 在本页 item 3 完成。

2. **看见从创世的联想 / 看见可选就等于从创世 / 看见不实现就只剩创世 is not already 已经从创世是唯一合法路径 interchangeable / 已经 genesis-only interchangeable / 已经创世唯一交差 interchangeable / 334 snapshotconn bundled interchangeable / 329 query-replicated interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 760 snapshotconn-notgone interchangeable / 334 snapshotconn item 1 必须实现 interchangeable / 334 snapshotconn item 2 两头都做 interchangeable，也不是已经应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事 bundled（334 item 3 余量） interchangeable / 334 snapshotconn item 3 interchangeable，也不是已经没有 state sync 这条对象（本页第一件事） interchangeable。**  
   官方写：也不是已经等于从创世。看见可选就等于从创世，不是已经 genesis-only interchangeable——本页钉 not already genesis-only 单句。看见不实现就只剩创世，不是已经没有 state sync 这条对象（本页第一件事） interchangeable——三件事分开钉。334 snapshotconn vs required bundled unbundling 在本页 item 3 完成。

3. **看见可选就当成清单齐了 / 看见已经问过邻居 / 看见 ListSnapshots 齐了的联想 is not already 已经齐了快照清单 interchangeable / 已经 listed interchangeable / 已经问过邻居交差 interchangeable / 334 snapshotconn bundled interchangeable / 322 snapshotdiscover interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 760 snapshotconn-notgone interchangeable / 334 snapshotconn item 1 / 334 snapshotconn item 2，也不是已经应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事 bundled（334 item 3 余量） interchangeable / 334 snapshotconn item 3 interchangeable，也不是已经没有 state sync 这条对象（本页第一件事） interchangeable / 已经从创世是唯一合法路径（本页第二件事） interchangeable。**  
   官方写：也不是已经问过邻居、已经齐了快照清单。看见可选就当成清单齐了，不是已经 listed interchangeable——本页钉 not already listed 单句。看见已经问过邻居的联想，不是已经 ListSnapshots 回了已经齐（322） interchangeable——322 另钉。看见可选就当成清单齐了，不是已经从创世是唯一合法路径（本页第二件事） interchangeable——三件事分开钉。334 snapshotconn vs required bundled unbundling 在本页 item 3 完成。

怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync 是规范里的做法，本页不抄。Snapshot Connection bundled（334）、四门里有 Snapshot Connection 不是已经必须实现快照（334 item 1 余量 / 758）、给人快照或给自己装回不是已经必须两头都做（334 item 2 余量 / 759）、ListSnapshots 回了已经齐（322）、Query 回了已经是正常运转必须有（329）、只有 AppHash 可信任（38）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **选择不实现 not already no-object ≠ 334 / 33 interchangeable：** 官方把可选实现和这条对象还在分开。
- **可选就等于从创世 not already genesis-only ≠ 已经从创世是唯一合法路径 interchangeable：** 官方把可选和已经等于从创世分开。
- **可选就当成清单齐了 not already listed ≠ 已经齐了快照清单 interchangeable：** 官方把可选和已经问过邻居分开；334 snapshotconn vs required bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 选择不实现 | 不是 already no-object | 不是 Query 必须有 alone（329） |
| 可选就等于从创世 | 不是 already genesis-only | 不是门在必须实现 alone（758） |
| 可选就当成清单齐了 | 不是 already listed | 不是 ListSnapshots 已经齐 alone（322） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量），必须分开选择不实现 是不是 already no-object interchangeable / 334 snapshotconn bundled interchangeable / snapshotconn-sold-as-required interchangeable、可选就等于从创世 是不是 already genesis-only interchangeable、可选就当成清单齐了 是不是 already listed interchangeable。可以跳过「看见应用选择不实现就已经没有 state sync 这条对象 interchangeable / 就已经从创世是唯一合法路径 interchangeable / 就已经 ListSnapshots 齐了 interchangeable」。第一版默认可从创世。不要另写怎样实现快照方法。334 snapshotconn vs required bundled unbundling 在本页 item 3 完成（758 + 759 + 760）。

## 本页不抄

- 怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync。
- Snapshot Connection bundled。那是不变量 334。
- 四门里有 Snapshot Connection 不是已经必须实现快照。那是不变量 334 item 1 余量 / 758。
- 给人快照或给自己装回不是已经必须两头都做。那是不变量 334 item 2 余量 / 759。
- ListSnapshots 回了已经齐。那是不变量 322。
- Query 回了已经是正常运转必须有。那是不变量 329。
- 只有 AppHash 可信任。那是不变量 38。
- 四门已经结算。那是不变量 33。
