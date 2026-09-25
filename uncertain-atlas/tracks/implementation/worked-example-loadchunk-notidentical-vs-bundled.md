# 例：看见填了三列 / 看见从 0 起 / 看见有 format is not already already identical interchangeable / already complete interchangeable / already selected interchangeable

**层次**：实现 / 请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量）/ not 873 loadchunk-notidentical interchangeable / not 375 loadchunk bundled interchangeable」，不是 loadchunk bundled（375），也不是 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐（872 item 1 余量）或回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB（375 item 3 余量）。不要另写怎样写 LoadSnapshotChunk。

## 官方三件事

规范把 Methods 里请求用 height / format / chunk（从 0 起）认这块 和「已经是填了三列就已经是同一份 interchangeable / 已经是从 0 起就已经齐 interchangeable / 已经是有 format 就已经选型 interchangeable / 已经是 loadchunk bundled interchangeable」分开写成三件独立的实现事，不是「看见填了三列就已经是同一份 interchangeable / 就已经齐 interchangeable / 就已经选型 interchangeable」一件事：

1. **看见填了三列 / 看见请求用 height / format / chunk（从 0 起）认这块 / 看见填了 height·format·chunk is not already 已经是同一份 interchangeable / 已经 identical interchangeable / 已经是同一份交差 interchangeable / 375 loadchunk bundled interchangeable / 368 Snapshot identical interchangeable / loadchunk-sold-as-retrieved interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 873 loadchunk-notidentical interchangeable / 375 loadchunk item 2 interchangeable，也不是已经请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事 bundled（375 item 2 余量） interchangeable / 375 loadchunk item 2 interchangeable，也不是已经在拉就已经齐（872） interchangeable / 322 ListSnapshots interchangeable / 有上限就已经是 4 MB（375 item 3） interchangeable，也不是已经全字段（含 Metadata）对上就已经装完（368） interchangeable。**  
   官方写：请求用这份快照的 `height`、应用自己的 `format`、从 `0` 起的块下标认这块。看见填了三列，不是五个字段都对上。看见填了三列，不是已经 identical interchangeable——375 钉 bundled 三事，本页从 item 2 侧钉 not already identical 单句。看见请求用 height / format / chunk（从 0 起）认这块，不是已经 loadchunk bundled（375） interchangeable——375 钉 bundled，本页钉 item 2 第一件事。看见填了三列，不是已经全字段（含 Metadata）对上就已经装完（368） interchangeable——368 另钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 2 续。

2. **看见从 0 起 / 看见块下标从 0 起 / 看见从 0 起认块 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 375 loadchunk bundled interchangeable / 872 loadchunk-notcomplete interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 873 loadchunk-notidentical interchangeable / 375 loadchunk item 1 在拉 interchangeable / 375 loadchunk item 3 有上限 interchangeable，也不是已经请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事 bundled（375 item 2 余量） interchangeable / 375 loadchunk item 2 interchangeable，也不是已经是同一份（本页第一件事） interchangeable。**  
   官方写：看见从 0 起，不是已经齐。看见块下标从 0 起，不是已经 complete interchangeable——本页钉 not already complete 单句。看见从 0 起认块，不是已经是同一份（本页第一件事） interchangeable——三件事分开钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 2 续。

3. **看见有 format / 看见应用自己的 format / 看见填了 format is not already 已经选型 interchangeable / 已经 selected interchangeable / 已经选型交差 interchangeable / 375 loadchunk bundled interchangeable / 376 format interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 873 loadchunk-notidentical interchangeable / 375 loadchunk item 1 / 375 loadchunk item 3，也不是已经请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事 bundled（375 item 2 余量） interchangeable / 375 loadchunk item 2 interchangeable，也不是已经是同一份（本页第一件事） interchangeable / 已经齐（本页第二件事） interchangeable。**  
   官方写：看见有 `format`，不是已经选型。看见应用自己的 format，不是已经 selected interchangeable——本页钉 not already selected 单句。看见填了 format，不是已经齐（本页第二件事） interchangeable——三件事分开钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 2 续。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。loadchunk bundled（375）、LoadSnapshotChunk 用来从邻居拉快照块不是已经齐（375 item 1 余量 / 872）、回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB（375 item 3 余量）、ListSnapshots 回了就已经齐（322）、全字段（含 Metadata）对上就已经装完（368）、Offer 收下就已经装完（321）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了三列 not already identical ≠ 375 / 368 interchangeable：** 官方把认这块和全字段对上已经是同一份分开。
- **从 0 起 not already complete ≠ 已经齐 interchangeable：** 官方把从 0 起和已经齐分开。
- **有 format not already selected ≠ 已经选型 interchangeable：** 官方把有 format 和已经选型分开；375 loadchunk-vs-retrieved bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了三列 | 不是 already identical | 不是全字段对上就已经装完 alone（368） |
| 从 0 起 | 不是 already complete | 不是在拉 already complete alone（872） |
| 有 format | 不是 already selected | 不是 Offer 收下就已经装完 alone（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量），必须分开填了三列 是不是 already identical interchangeable / 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable、从 0 起 是不是 already complete interchangeable、有 format 是不是 already selected interchangeable。可以跳过「看见填了三列就已经是同一份 interchangeable / 就已经齐 interchangeable / 就已经选型 interchangeable」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 2 续（872 + 873）。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- loadchunk bundled。那是不变量 375。
- LoadSnapshotChunk 用来从邻居拉快照块不是已经齐。那是不变量 375 item 1 余量 / 872。
- 回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB。那是不变量 375 item 3 余量。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 全字段（含 Metadata）对上就已经装完。那是不变量 368。
- Offer 收下就已经装完。那是不变量 321。
