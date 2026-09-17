# 例：看见 ListSnapshots 请求是空请求、向应用要一份快照清单不是已经齐；看见 ListSnapshots 回包 snapshots 是本地状态快照清单不是已经是同一份；看见 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照不是已经在拉块

**层次**：实现 / ListSnapshots 空请求。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ListSnapshots 请求是空请求、向应用要一份快照清单不是已经齐 / ListSnapshots 回包 snapshots 是本地状态快照清单不是已经是同一份 / ListSnapshots 用来在 state sync 时发现邻居上有哪些快照不是已经在拉块」，不是问了邻居就已经齐，也不是快照对上就已经装完。不要另写怎样写 ListSnapshots 空请求。

## 官方三件事

规范把 ListSnapshots 请求是空请求、向应用要一份快照清单、回包 `snapshots` 是本地状态快照清单、Usage 是在 state sync 时发现邻居上有哪些快照写成三件独立的实现事，不是「看见填了 ListSnapshots 空请求就已经齐、已经是同一份、已经在拉块」一件事：

1. **看见 ListSnapshots 请求是空请求、向应用要一份快照清单 / 看见填了空请求不是已经齐，也不是已经问了邻居。**  
   官方写：请求是空请求，向应用要一份快照清单。看见填了空请求，不是已经问过邻居、已经齐了。看见能问，不是已经有了全部快照。看见能填，不是已经交差。
2. **看见 ListSnapshots 回包 `snapshots` 是本地状态快照清单 / 看见回了清单不是已经是同一份，也不是已经装完。**  
   官方写：`snapshots` 是本地状态快照清单。看见回了清单，不是已经五个字段都对上、已经是同一份。看见有本地清单，不是已经装完。看见能回，不是已经交差。
3. **看见 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 / 看见用来发现不是已经在拉块，也不是已经齐。**  
   官方写：用来在 state sync 时发现邻居上有哪些快照。看见用来发现，不是已经在从邻居拉快照块。看见能发现，不是已经齐。看见能填，不是已经交差。

怎样写 ListSnapshots 空请求、怎样填空请求、怎样填本地清单是规范里的做法，本页不抄。问了邻居就已经齐是不变量 322，本页不抄。

## 官方为什么这样拆

- **ListSnapshots 请求是空请求、向应用要一份快照清单 ≠ 已经齐：** 官方把空请求和问了邻居就已经齐分开。
- **ListSnapshots 回包 snapshots 是本地状态快照清单 ≠ 已经是同一份：** 官方把本地清单和全字段对上就已经是同一份分开。
- **ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 ≠ 已经在拉块：** 官方把发现清单和拉块分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ListSnapshots 请求是空请求、向应用要一份快照清单 | 不是已经齐 | 不是问了邻居就已经齐（322） |
| ListSnapshots 回包 snapshots 是本地状态快照清单 | 不是已经是同一份 | 不是全字段（含 Metadata）对上就已经装完（368） |
| ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 | 不是已经在拉块 | 不是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ListSnapshots 空请求就已经齐、已经是同一份、已经在拉块」，必须分开 ListSnapshots 请求是空请求、向应用要一份快照清单是不是已经齐、ListSnapshots 回包 snapshots 是本地状态快照清单是不是已经是同一份、ListSnapshots 用来在 state sync 时发现邻居上有哪些快照是不是已经在拉块。可以跳过「看见填了 ListSnapshots 空请求就已经齐」。不要另写怎样写 ListSnapshots 空请求。395 listsnapempty vs discovery bundled unbundling 完成（734 item 1 / 735 item 2 / 736 item 3）；精读 [`worked-example-listsnapempty-notcomplete-vs-bundled.md`](worked-example-listsnapempty-notcomplete-vs-bundled.md)（不变量 734 item 1）。

## 本页不抄

- 怎样写 ListSnapshots 空请求、怎样填空请求、怎样填本地清单。
- 问了邻居就已经齐。那是不变量 322。
- 全字段（含 Metadata）对上就已经装完。那是不变量 368。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
