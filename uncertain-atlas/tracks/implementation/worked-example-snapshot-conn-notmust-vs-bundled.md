# 例：看见四门里有 Snapshot Connection is not already must implement snapshots interchangeable / not already snapshotted interchangeable / not already settled interchangeable

**层次**：实现 / 四门里有 Snapshot Connection not already must implement snapshots / not already snapshotted / not already settled 正式三事（334 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「四门里有 Snapshot Connection not already must implement snapshots / not already snapshotted / not already settled 正式三事（334 余量）/ not 932 snapshot-conn-notmust interchangeable / not 334 snapshot-conn-vs-required bundled interchangeable」，不是快照连接 bundled（334），也不是 ListSnapshots 回了已经齐（322），也不是 Offer 收下已经装完（321）。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

1. **看见四门里有 Snapshot Connection / 看见四条连接 这份门 is not already 已经必须实现快照管理 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 932 snapshot-conn-notmust interchangeable / 933 snapshot-conn-notboth interchangeable / 334 snapshot-conn item 2 给人快照 interchangeable，也不是已经四门里有 Snapshot Connection not already must implement snapshots / not already snapshotted / not already settled 正式三事 bundled（334 item 1 余量） interchangeable / 334 snapshot-conn item 1 interchangeable。**  
   官方写：CometBFT 维持四条并发 ABCI 连接，其中一条是 Snapshot Connection。快照管理可选：应用可以不实现。看见门在，不是已经必须实现 interchangeable——本页从 334 item 1 侧钉 not already must implement snapshots 单句。334 snapshot-conn vs required bundled unbundling 在本页 item 1 启动。

2. **看见四门齐了 / 看见连接名在 / 这份门 is not already 已经拍过快照 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 932 snapshot-conn-notmust interchangeable / 334 snapshot-conn item 3 选择不实现 interchangeable / 934 snapshot-conn-notgone interchangeable，也不是已经 ListSnapshots 回了已经齐 interchangeable / 322 listsnap interchangeable。**  
   官方把四门齐了和已经有快照分开——334 bundled 第一件事常与 322 混成「看见四门就已经必须实现或已经清单齐了 interchangeable」，本页钉 not already snapshotted 单句。

3. **看见连接名在 / 看见门在 / 这份门 is not already 已经交差 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 932 snapshot-conn-notmust interchangeable / 933 snapshot-conn-notboth interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 offersnap interchangeable。**  
   官方把连接名在和已经拍过或装过 / 已经交差分开。看见连接名在，不是已经交差 interchangeable。334 snapshot-conn vs required bundled unbundling 在本页 item 1 启动。

怎样实现 ListSnapshots / OfferSnapshot / LoadSnapshotChunk / ApplySnapshotChunk、怎样配 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **四门里有 Snapshot Connection not already must implement snapshots ≠ 已经必须实现快照 interchangeable：** 官方把门的存在和必须实现分开。
- **看见四门齐了 not already snapshotted ≠ 已经拍过快照 interchangeable：** 官方把四门齐了和已经有快照分开。
- **看见连接名在 not already settled ≠ 已经交差 interchangeable：** 官方把连接名在和已经交差分开；334 snapshot-conn vs required bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 四门里有 Snapshot Connection | 不是已经必须实现快照 | 不是 ListSnapshots 回了已经齐（322） |
| 看见四门齐了 | 不是已经拍过快照 | 不是 Offer 收下已经装完（321） |
| 看见连接名在 | 不是已经交差 | 不是给人快照就已经必须两头都做（933） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看四门里有 Snapshot Connection not already must implement snapshots / not already snapshotted / not already settled 正式三事（334 余量），必须分开是不是已经必须实现、是不是已经拍过快照、是不是已经交差。可以跳过「看见四门就已经必须做快照」。第一版默认可从创世。不要另写怎样实现快照方法或怎样配 state sync。334 snapshot-conn vs required bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-conn-notboth-vs-bundled.md`](worked-example-snapshot-conn-notboth-vs-bundled.md)（不变量 933 item 2）。

## 本页不抄

- 怎样实现 ListSnapshots / OfferSnapshot / LoadSnapshotChunk / ApplySnapshotChunk、怎样配 state sync。
- 快照连接 bundled。那是不变量 334。
- 给人快照就已经必须两头都做。那是不变量 334 item 2 余量 / 933。
- ListSnapshots 回了已经齐。那是不变量 322。
