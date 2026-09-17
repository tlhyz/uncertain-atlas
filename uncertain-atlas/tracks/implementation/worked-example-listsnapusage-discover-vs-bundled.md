# 例：看见 Used during state sync to discover available snapshots on peers 不是已经 ListSnapshots 空请求 bundled（395） interchangeable；看见 See Snapshot data type for details 不是已经 Snapshot 类型 bundled（368） interchangeable

**层次**：实现 / ListSnapshots Usage discover / Snapshot type 正式二事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Used during state sync to discover on peers 不是 ListSnapshots 空请求 bundled interchangeable / See Snapshot data type 不是 Snapshot 类型 bundled interchangeable」，不是 ListSnapshots 空请求 bundled（395），也不是 Snapshot Discovery 已经齐（322）。不要另写怎样写 ListSnapshots、怎样列 Snapshot 类型。

## 官方两件事

规范把 ListSnapshots Methods Usage 写成两件独立的实现事，不是「看见 ListSnapshots Usage 了就已经空请求 bundled interchangeable、已经 five fields 对上 interchangeable」一件事：

1. **看见 Used during state sync to discover available snapshots on peers / 看见在 state sync 时用来发现邻居上有哪些快照 不是已经 ListSnapshots 请求是空请求、向应用要一份快照清单 bundled（395） interchangeable，也不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 bundled（395） interchangeable，也不是已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable。**  
   官方 Usage 写：Used during state sync to discover available snapshots on peers。看见 discover on peers during state sync，不是已经 ListSnapshots 空请求 bundled（395） interchangeable——395 钉 Request/Response 栏和 Usage 发现句 bundled 三事，本页钉 Methods Usage discover on peers 单句。看见 discover available snapshots on peers，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable——395 钉本地清单栏，本页钉 Usage 侧发现邻居快照语义。看见 during state sync，不是已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable——322 钉 app requirements Snapshot Discovery，本页钉 Methods ListSnapshots Usage 单句。
2. **看见 See `Snapshot` data type for details / 看见要看 Snapshot 数据类型细节 不是已经 Snapshot 全字段（含 Metadata）对上就已经装完（368） interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable，也不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单就已经是同一份（395 bundled 第二件事） interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable。**  
   官方 Usage 写：See `Snapshot` data type for details。看见 See Snapshot data type，不是已经 Snapshot 类型 five fields / format / hash / chunks bundled（368） interchangeable——368 钉 Data Types Snapshot 栏，本页钉 Methods Usage 交叉引用句。看见 for details，不是已经五个字段都对上就已经装完 interchangeable——368 钉同一份快照，本页钉 Usage 侧「要看类型细节」语义。看见 Snapshot data type，不是已经 ListSnapshots 回了本地清单就可信 interchangeable——395 钉本地清单，本页钉 Usage 指向 Snapshot 类型。

怎样做 ListSnapshots、怎样列 Snapshot 类型、怎样切块是规范里的做法，本页不抄。ListSnapshots 空请求 bundled（395）、Snapshot Discovery 已经齐（322）、Snapshot 类型 five fields（368）、Offer 收下就已经装完（321）是另外那套，本页不抄。

## 官方为什么这样拆

- **discover on peers during state sync ≠ ListSnapshots 空请求 bundled interchangeable：** 官方把 Methods Usage discover 单句和 Request/Response bundled 分开。
- **See Snapshot data type for details ≠ Snapshot 类型 bundled interchangeable：** 官方把 Usage 交叉引用句和 Data Types Snapshot 栏 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| discover on peers during state sync | 不是 ListSnapshots 空请求 bundled（395） | 不是 Snapshot Discovery 已经齐（322） |
| See Snapshot data type for details | 不是 Snapshot 类型 bundled（368） | 不是 ListSnapshots 本地清单就已经是同一份（395） |
| ListSnapshots Usage | 不是已经在拉块 | 不是 LoadSnapshotChunk 已经齐（375） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage discover / Snapshot type 正式二事，必须分开 Used during state sync to discover on peers 是不是 ListSnapshots 空请求 bundled interchangeable / 已经本地清单 / 已经问了邻居就齐、See Snapshot data type for details 是不是 Snapshot 类型 bundled interchangeable / 已经 five fields 对上 / 已经装完。可以跳过「看见 ListSnapshots Usage 了就已经空请求 bundled interchangeable、已经 five fields 对上 interchangeable」。不要另写怎样写 ListSnapshots、怎样列 Snapshot 类型。 500 listsnapusage discover unbundling 在本页 item 1 启动；精读 [`worked-example-listsnapusage-notdiscover-vs-bundled.md`](worked-example-listsnapusage-notdiscover-vs-bundled.md)（不变量 661 item 1）；续 [`worked-example-listsnapusage-notsnaptype-vs-bundled.md`](worked-example-listsnapusage-notsnaptype-vs-bundled.md)（不变量 662 item 2）。500 listsnapusage discover unbundling 完成（661→662）。

## 本页不抄

- 怎样写 ListSnapshots、怎样列 Snapshot 类型、怎样切块。
- ListSnapshots 空请求 bundled。那是不变量 395。
- Snapshot Discovery 已经齐。那是不变量 322。
- Snapshot 类型 five fields。那是不变量 368。
- Offer 收下就已经装完。那是不变量 321。
- LoadSnapshotChunk 已经齐。那是不变量 375。
