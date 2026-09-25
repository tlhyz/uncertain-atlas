# 例：看见在拉 / 看见问了邻居 / 看见能拉 is not already already complete interchangeable / already all interchangeable / already restored interchangeable

**层次**：实现 / LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量）/ not 872 loadchunk-notcomplete interchangeable / not 375 loadchunk bundled interchangeable」，不是 loadchunk bundled（375），也不是请求用 height / format / chunk（从 0 起）认这块不是已经是同一份（375 item 2 余量）或回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB（375 item 3 余量）。不要另写怎样写 LoadSnapshotChunk。

## 官方三件事

规范把 Methods 里 LoadSnapshotChunk 用来从邻居拉快照块 和「已经是在拉就已经齐 interchangeable / 已经是问了邻居就已经有了全部快照 interchangeable / 已经是能拉就已经装完 interchangeable / 已经是 loadchunk bundled interchangeable」分开写成三件独立的实现事，不是「看见在拉就已经齐 interchangeable / 就已经有了全部快照 interchangeable / 就已经装完 interchangeable」一件事：

1. **看见在拉 / 看见 LoadSnapshotChunk 用来从邻居拉快照块 / 看见在拉块 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 375 loadchunk bundled interchangeable / 322 ListSnapshots interchangeable / loadchunk-sold-as-retrieved interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 872 loadchunk-notcomplete interchangeable / 375 loadchunk item 1 interchangeable，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事 bundled（375 item 1 余量） interchangeable / 375 loadchunk item 1 interchangeable，也不是已经填了三列就已经是同一份（375 item 2） interchangeable / 有上限就已经是 4 MB（375 item 3） interchangeable / 368 Snapshot identical interchangeable，也不是已经 ListSnapshots 回了就已经齐（322） interchangeable。**  
   官方写：LoadSnapshotChunk 用在 state sync 里，从邻居拉快照块。看见在拉，不是已经齐。看见在拉，不是已经 complete interchangeable——375 钉 bundled 三事，本页从 item 1 侧钉 not already complete 单句。看见 LoadSnapshotChunk 用来从邻居拉快照块，不是已经 loadchunk bundled（375） interchangeable——375 钉 bundled，本页钉 item 1 第一件事。看见在拉，不是已经 ListSnapshots 回了就已经齐（322） interchangeable——322 另钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 1 启动。

2. **看见问了邻居 / 看见从邻居拉 / 看见问邻居 is not already 已经有了全部快照 interchangeable / 已经 all interchangeable / 已经有了全部快照交差 interchangeable / 375 loadchunk bundled interchangeable / 322 ListSnapshots interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 872 loadchunk-notcomplete interchangeable / 375 loadchunk item 2 填了三列 interchangeable / 375 loadchunk item 3 有上限 interchangeable，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事 bundled（375 item 1 余量） interchangeable / 375 loadchunk item 1 interchangeable，也不是已经齐（本页第一件事） interchangeable。**  
   官方写：看见问了邻居，不是已经有了全部快照。看见从邻居拉，不是已经 all interchangeable——本页钉 not already all 单句。看见问邻居，不是已经齐（本页第一件事） interchangeable——三件事分开钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 1 启动。

3. **看见能拉 / 看见能拉快照块 / 看见能拉块 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable / 375 loadchunk bundled interchangeable / 321 Offer restored interchangeable，也不是已经 loadchunk bundled（375） interchangeable / 872 loadchunk-notcomplete interchangeable / 375 loadchunk item 2 / 375 loadchunk item 3，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事 bundled（375 item 1 余量） interchangeable / 375 loadchunk item 1 interchangeable，也不是已经齐（本页第一件事） interchangeable / 已经有了全部快照（本页第二件事） interchangeable。**  
   官方写：看见能拉，不是已经装完。看见能拉快照块，不是已经 restored interchangeable——本页钉 not already restored 单句。看见能拉块，不是已经有了全部快照（本页第二件事） interchangeable——三件事分开钉。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 1 启动。

怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB 是规范里的做法，本页不抄。loadchunk bundled（375）、请求用 height / format / chunk（从 0 起）认这块不是已经是同一份（375 item 2 余量）、回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB（375 item 3 余量）、ListSnapshots 回了就已经齐（322）、全字段（含 Metadata）对上就已经装完（368）、Offer 收下就已经装完（321）是另外那套，本页不抄。

## 官方为什么这样拆

- **在拉 not already complete ≠ 375 / 322 interchangeable：** 官方把在拉和已经齐分开。
- **问了邻居 not already all ≠ 已经有了全部快照 interchangeable：** 官方把问了邻居和已经有了全部快照分开。
- **能拉 not already restored ≠ 已经装完 interchangeable：** 官方把能拉和已经装完分开；375 loadchunk-vs-retrieved bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 在拉 | 不是 already complete | 不是 ListSnapshots 回了就已经齐 alone（322） |
| 问了邻居 | 不是 already all | 不是全字段对上就已经装完 alone（368） |
| 能拉 | 不是 already restored | 不是 Offer 收下就已经装完 alone（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量），必须分开在拉 是不是 already complete interchangeable / 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable、问了邻居 是不是 already all interchangeable、能拉 是不是 already restored interchangeable。可以跳过「看见在拉就已经齐 interchangeable / 就已经有了全部快照 interchangeable / 就已经装完 interchangeable」。不要另写怎样写 LoadSnapshotChunk。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 1 启动（872）。

## 本页不抄

- 怎样写 LoadSnapshotChunk、怎样切块、怎样挑 10 MB。
- loadchunk bundled。那是不变量 375。
- 请求用 height / format / chunk（从 0 起）认这块不是已经是同一份。那是不变量 375 item 2 余量。
- 回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB。那是不变量 375 item 3 余量。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 全字段（含 Metadata）对上就已经装完。那是不变量 368。
- Offer 收下就已经装完。那是不变量 321。
