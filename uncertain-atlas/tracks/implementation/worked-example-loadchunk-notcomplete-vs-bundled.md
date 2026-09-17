# 例：看见 LoadSnapshotChunk 用来从邻居拉快照块 is not already complete interchangeable / not already all snapshots interchangeable / not already restored interchangeable

**层次**：实现 / LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事（375 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事（375 余量）/ not 800 loadchunk-notcomplete interchangeable / not 375 loadchunk-vs-retrieved bundled interchangeable」，不是 LoadSnapshotChunk bundled（375），也不是 ListSnapshots 回了就已经齐（322），也不是 Usage retrieve 就已经在拉（501/660），也不是 Apply 请求 chunk 就已经在拉（397/740）。不要另写怎样写 LoadSnapshotChunk。

## 官方三件事

1. **看见 LoadSnapshotChunk 用来从邻居拉快照块 / 看见在拉 / 这份拉块 is not already 已经齐 interchangeable / 322 snapcomplete interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 800 loadchunk-notcomplete interchangeable / 801 loadchunk-notsame interchangeable / 375 loadchunk item 2 三列 interchangeable，也不是已经 LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事 bundled（375 item 1 余量） interchangeable / 375 loadchunk item 1 interchangeable。**  
   官方写：LoadSnapshotChunk 用在 state sync 里，从邻居拉快照块。看见在拉，不是已经齐 interchangeable——本页从 375 item 1 侧钉 not already complete 单句。375 loadchunk vs retrieved bundled unbundling 在本页 item 1 启动。

2. **看见在拉 / 看见问了邻居 / 这份拉块 is not already 已经有了全部快照 interchangeable / 322 snapcomplete interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 800 loadchunk-notcomplete interchangeable / 375 loadchunk item 3 16 MB interchangeable / 802 loadchunk-not4mb interchangeable，也不是已经 Usage retrieve 就已经在拉 interchangeable / 501 loadsnapusage / 660 loadsnapusage-notchunks interchangeable，也不是已经 Apply 请求 chunk 就已经在拉 interchangeable / 397 applychunk / 740 applychunk-notload interchangeable。**  
   官方把问了邻居和已经有了全部快照分开——375 bundled 第一件事常与 322 / 501 / 397 混成「看见在拉就已经齐或已经有了全部快照 interchangeable」，本页钉 not already all snapshots 单句。

3. **看见在拉 / 看见能拉 / 这份拉块 is not already 已经装完 interchangeable，也不是已经 LoadSnapshotChunk bundled（375） interchangeable / 800 loadchunk-notcomplete interchangeable / 801 loadchunk-notsame interchangeable。**  
   官方把能拉和已经装完分开。看见能拉，不是已经装完 interchangeable。375 loadchunk vs retrieved bundled unbundling 在本页 item 1 启动。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **LoadSnapshotChunk not already complete ≠ 322 interchangeable：** 官方把从邻居拉块和已经齐分开。
- **看见问了邻居 not already all snapshots ≠ 已经有了全部快照 interchangeable：** 官方把问了邻居和已经有了全部快照分开。
- **看见能拉 not already restored ≠ 已经装完 interchangeable：** 官方把能拉和已经装完分开；375 loadchunk vs retrieved bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| LoadSnapshotChunk 用来从邻居拉快照块 | 不是已经齐（322） | 不是三列认块（801/375 item 2） |
| 看见在拉 | 不是已经有了全部快照 | 不是 Usage retrieve（501/660） |
| 看见能拉 | 不是已经装完 | 不是 Apply 请求 chunk（397/740） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事（375 余量），必须分开是不是已经齐 interchangeable / 322、是不是已经有了全部快照、是不是已经装完。可以跳过「看见在拉就已经齐」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk vs retrieved bundled unbundling 在本页 item 1 启动；续 [`worked-example-loadchunk-notsame-vs-bundled.md`](worked-example-loadchunk-notsame-vs-bundled.md)（不变量 801 item 2）。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- LoadSnapshotChunk bundled。那是不变量 375。
- height / format / chunk 认块。那是不变量 375 item 2 余量 / 801。
- ListSnapshots 回了就已经齐。那是不变量 322。
- Usage retrieve 就已经在拉。那是不变量 501 / 660。
