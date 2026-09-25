# 例：看见 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐；看见请求用 height / format / chunk（从 0 起）认这块不是已经是同一份；看见回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB

**层次**：实现 / LoadSnapshotChunk。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 / 请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 / 回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB」，不是 ListSnapshots 回了就已经齐，也不是快照全字段对上就已经装完。不要另写怎样写 LoadSnapshotChunk。375 loadchunk-vs-retrieved bundled unbundling 完成（872+873+874）；精读 [`worked-example-loadchunk-notcomplete-vs-bundled.md`](worked-example-loadchunk-notcomplete-vs-bundled.md)（不变量 872 item 1）；精读 [`worked-example-loadchunk-notidentical-vs-bundled.md`](worked-example-loadchunk-notidentical-vs-bundled.md)（不变量 873 item 2）；精读 [`worked-example-loadchunk-not4mb-vs-bundled.md`](worked-example-loadchunk-not4mb-vs-bundled.md)（不变量 874 item 3）。

## 官方三件事

规范把 LoadSnapshotChunk 用来从邻居拉快照块、请求用 height / format / chunk（从 0 起）认这块、回包块含元数据不能超过 16 MB 写成三件独立的实现事，不是「看见叫了 LoadSnapshotChunk 就已经齐、已经是同一份、已经是快照报文 4 MB」一件事：

1. **看见 LoadSnapshotChunk 用来从邻居拉快照块 / 看见在拉 不是已经齐，也不是已经有了全部快照。**  
   官方写：LoadSnapshotChunk 用在 state sync 里，从邻居拉快照块。看见在拉，不是已经齐。看见问了邻居，不是已经有了全部快照。看见能拉，不是已经装完。
2. **看见请求用 `height` / `format` / `chunk`（从 0 起）认这块 / 看见填了三列 不是已经是同一份，也不是已经装完。**  
   官方写：请求用这份快照的 `height`、应用自己的 `format`、从 `0` 起的块下标认这块。看见填了三列，不是五个字段都对上。看见从 0 起，不是已经齐。看见有 `format`，不是已经选型。
3. **看见回包块含元数据不能超过 16 MB / 看见有上限 不是已经是快照报文 4 MB，也不是已经装完。**  
   官方写：回包是任意格式的二进制块。块报文含元数据不能超过 16 MB，所以 10 MB 是个好起点。看见有上限，不是已经是网上一份快照报文最多 4 MB。看见 10 MB，不是已经是共识常数。看见回了字节，不是已经装完。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。ListSnapshots 回了就已经齐是不变量 322，本页不抄。

## 官方为什么这样拆

- **LoadSnapshotChunk 用来从邻居拉快照块 ≠ 已经齐：** 官方把在拉和已经齐分开。
- **请求用 height / format / chunk（从 0 起）认这块 ≠ 已经是同一份：** 官方把认这块和全字段对上已经是同一份分开。
- **回包块含元数据不能超过 16 MB ≠ 已经是快照报文 4 MB：** 官方把块报文上限和快照报文上限分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| LoadSnapshotChunk 用来从邻居拉快照块 | 不是已经齐 | 不是 ListSnapshots 回了就已经齐（322） |
| 请求用 height / format / chunk（从 0 起）认这块 | 不是已经是同一份 | 不是全字段（含 Metadata）对上就已经装完（368） |
| 回包块含元数据不能超过 16 MB | 不是已经是快照报文 4 MB | 不是 Offer 收下就已经装完（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 LoadSnapshotChunk 就已经齐、已经是同一份、已经是快照报文 4 MB」，必须分开 LoadSnapshotChunk 用来从邻居拉快照块是不是已经齐、请求用 height / format / chunk（从 0 起）认这块是不是已经是同一份、回包块含元数据不能超过 16 MB 是不是已经是快照报文 4 MB。可以跳过「看见叫了 LoadSnapshotChunk 就已经齐」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk-vs-retrieved bundled unbundling 完成（872+873+874）。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 全字段（含 Metadata）对上就已经装完。那是不变量 368。
- Offer 收下就已经装完。那是不变量 321。
