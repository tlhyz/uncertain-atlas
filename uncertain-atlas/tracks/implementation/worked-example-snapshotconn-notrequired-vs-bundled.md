# 例：看见四门里有 Snapshot Connection / 看见四门齐了 / 看见连接名在 is not already already must-implement interchangeable / already snapshot-taken interchangeable / already conn-name-is-snap interchangeable

**层次**：实现 / 四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事（334 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事（334 余量）/ not 758 snapshotconn-notrequired interchangeable / not 334 snapshotconn bundled interchangeable」，不是 Snapshot Connection bundled（334），也不是给人快照或给自己装回不是已经必须两头都做（759 item 2 余量）或应用选择不实现不是已经没有 state sync 这条对象（760 item 3 余量）。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

规范把 Requirements 里四条并发 ABCI 连接中有 Snapshot Connection、快照管理可选 和「已经是四门里有 Snapshot Connection 就必须实现快照 interchangeable / 已经是四门齐了就已经有快照 interchangeable / 已经是连接名在就已经拍过或装过 interchangeable / 已经是 snapshotconn bundled interchangeable」分开写成三件独立的实现事，不是「看见四门里有 Snapshot Connection 就已经必须实现快照 interchangeable / 就已经有快照 interchangeable / 就已经拍过或装过 interchangeable」一件事：

1. **看见四门里有 Snapshot Connection / 看见四条连接 / 看见门在 is not already 已经必须实现快照管理 interchangeable / 已经 must-implement interchangeable / 已经必须实现交差 interchangeable / 334 snapshotconn bundled interchangeable / 33 four gates interchangeable / snapshotconn-sold-as-required interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 758 snapshotconn-notrequired interchangeable / 334 snapshotconn item 1 interchangeable，也不是已经四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事 bundled（334 item 1 余量） interchangeable / 334 snapshotconn item 1 interchangeable，也不是已经给人快照或给自己装回不是已经必须两头都做（759） interchangeable / 760 snapshotconn-notgone interchangeable / 322 snapshotdiscover interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CometBFT 维持四条并发 ABCI 连接，其中一条是 Snapshot Connection。快照管理**可选**：应用可以不实现。看见门在，不是已经 must-implement interchangeable——334 钉 bundled 三事，本页从 item 1 侧钉 not already must-implement 单句。看见四门里有 Snapshot Connection，不是已经 Snapshot Connection bundled（334） interchangeable——334 钉 bundled，本页钉 item 1 第一件事。看见四条连接，不是已经 ListSnapshots 回了已经齐（322） interchangeable——322 另钉。334 snapshotconn vs required bundled unbundling 在本页 item 1 启动。

2. **看见四门齐了 / 看见四条连接都在 / 看见连接表齐了 is not already 已经有快照 interchangeable / 已经 snapshot-taken interchangeable / 已经拍过快照交差 interchangeable / 334 snapshotconn bundled interchangeable / 322 snapshotdiscover interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 758 snapshotconn-notrequired interchangeable / 334 snapshotconn item 2 两头都做 interchangeable / 334 snapshotconn item 3 可选 interchangeable，也不是已经四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事 bundled（334 item 1 余量） interchangeable / 334 snapshotconn item 1 interchangeable，也不是已经必须实现快照管理（本页第一件事） interchangeable。**  
   官方写：看见四门齐了，不是已经有快照。看见四条连接都在，不是已经 snapshot-taken interchangeable——本页钉 not already snapshot-taken 单句。看见连接表齐了，不是已经必须实现快照管理（本页第一件事） interchangeable——三件事分开钉。334 snapshotconn vs required bundled unbundling 在本页 item 1 启动。

3. **看见连接名在 / 看见 Snapshot Connection 这个名 / 看见连接名叫快照 is not already 已经拍过或装过 interchangeable / 已经 conn-name-is-snap interchangeable / 已经名即快照交差 interchangeable / 334 snapshotconn bundled interchangeable / 321 snapshotrestore interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 758 snapshotconn-notrequired interchangeable / 334 snapshotconn item 2 / 334 snapshotconn item 3，也不是已经四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事 bundled（334 item 1 余量） interchangeable / 334 snapshotconn item 1 interchangeable，也不是已经必须实现快照管理（本页第一件事） interchangeable / 已经有快照（本页第二件事） interchangeable。**  
   官方写：看见连接名在，不是已经拍过或装过。看见 Snapshot Connection 这个名，不是已经 conn-name-is-snap interchangeable——本页钉 not already conn-name-is-snap 单句。看见连接名叫快照，不是已经 Offer 收下已经装完（321） interchangeable——321 另钉。看见连接名在，不是已经有快照（本页第二件事） interchangeable——三件事分开钉。334 snapshotconn vs required bundled unbundling 在本页 item 1 启动。

怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync 是规范里的做法，本页不抄。Snapshot Connection bundled（334）、给人快照或给自己装回不是已经必须两头都做（334 item 2 余量 / 759）、应用选择不实现不是已经没有 state sync 这条对象（334 item 3 余量 / 760）、ListSnapshots 回了已经齐（322）、Offer 收下已经装完（321）、只有 AppHash 可信任（38）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **四门里有 Snapshot Connection not already must-implement ≠ 334 / 33 interchangeable：** 官方把门的存在和必须实现分开。
- **四门齐了 not already snapshot-taken ≠ 已经有快照 interchangeable：** 官方把四门齐了和已经有快照分开。
- **连接名在 not already conn-name-is-snap ≠ 已经拍过或装过 interchangeable：** 官方把连接名和已经拍过或装过分开；334 snapshotconn vs required bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 四门里有 Snapshot Connection | 不是 already must-implement | 不是 ListSnapshots 已经齐 alone（322） |
| 四门齐了 | 不是 already snapshot-taken | 不是 Offer 收下已经装完 alone（321） |
| 连接名在 | 不是 already conn-name-is-snap | 不是只有 AppHash 可信任 alone（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事（334 余量），必须分开四门里有 Snapshot Connection 是不是 already must-implement interchangeable / 334 snapshotconn bundled interchangeable / snapshotconn-sold-as-required interchangeable、四门齐了 是不是 already snapshot-taken interchangeable、连接名在 是不是 already conn-name-is-snap interchangeable。可以跳过「看见四门里有 Snapshot Connection 就已经必须实现快照 interchangeable / 就已经有快照 interchangeable / 就已经拍过或装过 interchangeable」。第一版默认可从创世。不要另写怎样实现快照方法。334 snapshotconn vs required bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshotconn-notbothends-vs-bundled.md`](worked-example-snapshotconn-notbothends-vs-bundled.md)（不变量 759 item 2）已写；完成见 760。

## 本页不抄

- 怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync。
- Snapshot Connection bundled。那是不变量 334。
- 给人快照或给自己装回不是已经必须两头都做。那是不变量 334 item 2 余量 / 759。
- 应用选择不实现不是已经没有 state sync 这条对象。那是不变量 334 item 3 余量 / 760。
- ListSnapshots 回了已经齐。那是不变量 322。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 四门已经结算。那是不变量 33。
