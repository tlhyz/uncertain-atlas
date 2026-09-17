# 例：看见请求用 height / format / chunk（从 0 起）认这块 is not already same snapshot interchangeable / not already complete interchangeable / not already selected format interchangeable

**层次**：实现 / 三列认块 not already same snapshot / not already complete / not already selected format 正式三事（375 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「三列认块 not already same snapshot / not already complete / not already selected format 正式三事（375 余量）/ not 801 loadchunk-notsame interchangeable / not 375 loadchunk-vs-retrieved bundled interchangeable」，不是 LoadSnapshotChunk bundled（375），也不是全字段对上就已经装完（368），也不是 Offer 快照就已经是同一份（396/738），也不是 ListSnapshots 本地列表就已经是同一份（395/735）。不要另写怎样写 LoadSnapshotChunk。

## 官方三件事

1. **看见请求用 `height` / `format` / `chunk`（从 0 起）认这块 / 看见填了三列 / 这份认块 is not already 已经是同一份 interchangeable / 368 snapid interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 801 loadchunk-notsame interchangeable / 800 loadchunk-notcomplete interchangeable / 375 loadchunk item 1 拉块 interchangeable，也不是已经三列认块 not already same snapshot / not already complete / not already selected format 正式三事 bundled（375 item 2 余量） interchangeable / 375 loadchunk item 2 interchangeable。**  
   官方写：请求用这份快照的 `height`、应用自己的 `format`、从 `0` 起的块下标认这块。看见填了三列，不是五个字段都对上 interchangeable——本页从 375 item 2 侧钉 not already same snapshot 单句。375 loadchunk vs retrieved bundled unbundling 在本页 item 2 续。

2. **看见填了三列 / 看见从 0 起 / 这份认块 is not already 已经齐 interchangeable / 368 snapid interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 801 loadchunk-notsame interchangeable / 375 loadchunk item 3 16 MB interchangeable / 802 loadchunk-not4mb interchangeable，也不是已经 Offer 快照就已经是同一份 interchangeable / 396 offersnap / 738 offersnapreq-notrestored interchangeable，也不是已经 ListSnapshots 本地列表就已经是同一份 interchangeable / 395 listsnapempty / 735 listsnapempty-notidentical interchangeable。**  
   官方把从 0 起和已经齐分开——375 bundled 第二件事常与 368 / 396 / 395 混成「看见填了三列就已经是同一份或已经齐 interchangeable」，本页钉 not already complete 单句。

3. **看见填了三列 / 看见有 `format` / 这份认块 is not already 已经选型 interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 801 loadchunk-notsame interchangeable / 800 loadchunk-notcomplete interchangeable。**  
   官方把有 format 和已经选型分开。看见有 `format`，不是已经选型 interchangeable。375 loadchunk vs retrieved bundled unbundling 在本页 item 2 续。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **三列认块 not already same snapshot ≠ 368 interchangeable：** 官方把三列认块和五个字段都对上分开。
- **看见从 0 起 not already complete ≠ 已经齐 interchangeable：** 官方把从 0 起和已经齐分开。
- **看见有 format not already selected format ≠ 已经选型 interchangeable：** 官方把有 format 和已经选型分开；375 loadchunk vs retrieved bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 请求用 height / format / chunk 认这块 | 不是已经是同一份（368） | 不是从邻居拉块（800/375 item 1） |
| 看见填了三列 | 不是已经齐 | 不是 Offer 快照（396/738） |
| 看见有 format | 不是已经选型 | 不是 ListSnapshots 本地列表（395/735） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看三列认块 not already same snapshot / not already complete / not already selected format 正式三事（375 余量），必须分开是不是已经是同一份 interchangeable / 368、是不是已经齐、是不是已经选型。可以跳过「看见填了三列就已经是同一份」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk vs retrieved bundled unbundling 在本页 item 2 续；续 [`worked-example-loadchunk-not4mb-vs-bundled.md`](worked-example-loadchunk-not4mb-vs-bundled.md)（不变量 802 item 3）。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- LoadSnapshotChunk bundled。那是不变量 375。
- 从邻居拉快照块。那是不变量 375 item 1 余量 / 800。
- 全字段对上就已经装完。那是不变量 368。
- Offer 快照就已经是同一份。那是不变量 396 / 738。
