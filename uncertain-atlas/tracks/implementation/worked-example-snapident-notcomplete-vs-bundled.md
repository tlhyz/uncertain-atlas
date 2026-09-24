# 例：看见写成 1 / 看见有上限 / 看见能发 is not already already complete interchangeable / already consensus-const interchangeable / already restored interchangeable

**层次**：实现 / 空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量）/ not 853 snapident-notcomplete interchangeable / not 368 snapident bundled interchangeable」，不是 snapident bundled（368），也不是快照全字段含 Metadata 对上不是已经装完（851 item 1 余量）或引擎不解释 format / hash 不是已经轻验 AppHash（852 item 2 余量）。不要另写怎样写 Snapshot 类型。

## 官方三件事

规范把 Methods 里 `chunks` 是快照里的块数、至少是 1（哪怕是空快照）、网上一份快照报文最多 4 MB 和「已经是写成 1 就已经齐 interchangeable / 已经是有上限就已经是共识常数 interchangeable / 已经是能发就已经装完 interchangeable / 已经是 snapident bundled interchangeable」分开写成三件独立的实现事，不是「看见写成 1 就已经齐 interchangeable / 就已经是共识常数 interchangeable / 就已经装完 interchangeable」一件事：

1. **看见写成 1 / 看见 `chunks` 至少是 1、哪怕是空快照 / 看见有块数 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 368 snapident bundled interchangeable / 322 listsnap interchangeable / snapshot-sold-as-identical interchangeable，也不是已经 snapident bundled（368） interchangeable / 853 snapident-notcomplete interchangeable / 368 snapident item 3 interchangeable，也不是已经空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事 bundled（368 item 3 余量） interchangeable / 368 snapident item 3 interchangeable，也不是已经对上了就已经装完（851） interchangeable / 852 snapident-notapphash interchangeable / 321 offer interchangeable，也不是已经 ListSnapshots 回了就已经齐（322） interchangeable。**  
   官方写：`chunks` 是快照里的块数，至少是 1，哪怕是空快照。看见写成 1，不是已经齐。看见写成 1，不是已经 complete interchangeable——368 钉 bundled 三事，本页从 item 3 侧钉 not already complete 单句。看见 `chunks` 至少是 1、哪怕是空快照，不是已经 snapident bundled（368） interchangeable——368 钉 bundled，本页钉 item 3 第一件事。看见写成 1，不是已经对上了就已经装完（851） interchangeable——851 另钉 item 1。看见写成 1，不是已经引擎不解释就已经轻验 AppHash（852） interchangeable——852 另钉 item 2。368 snapshot-vs-identical bundled unbundling 在本页 item 3 完成。

2. **看见有上限 / 看见网上一份快照报文最多 4 MB / 看见有 4 MB 上限 is not already 已经是共识常数 interchangeable / 已经 consensus-const interchangeable / 已经是共识常数交差 interchangeable / 368 snapident bundled interchangeable / 299 maxbytes interchangeable，也不是已经 snapident bundled（368） interchangeable / 853 snapident-notcomplete interchangeable / 368 snapident item 1 对上 interchangeable / 368 snapident item 2 不解释 interchangeable，也不是已经空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事 bundled（368 item 3 余量） interchangeable / 368 snapident item 3 interchangeable，也不是已经齐（本页第一件事） interchangeable。**  
   官方写：看见有上限，不是已经是共识常数。看见网上一份快照报文最多 4 MB，不是已经 consensus-const interchangeable——本页钉 not already consensus-const 单句。看见有 4 MB 上限，不是已经齐（本页第一件事） interchangeable——三件事分开钉。368 snapshot-vs-identical bundled unbundling 在本页 item 3 完成。

3. **看见能发 / 看见能发这份快照报文 / 看见报文能上网上 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable / 368 snapident bundled interchangeable / 321 offer interchangeable，也不是已经 snapident bundled（368） interchangeable / 853 snapident-notcomplete interchangeable / 368 snapident item 1 / 368 snapident item 2，也不是已经空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事 bundled（368 item 3 余量） interchangeable / 368 snapident item 3 interchangeable，也不是已经齐（本页第一件事） interchangeable / 已经是共识常数（本页第二件事） interchangeable。**  
   官方写：看见能发，不是已经装完。看见能发这份快照报文，不是已经 restored interchangeable——本页钉 not already restored 单句。看见报文能上网上，不是已经是共识常数（本页第二件事） interchangeable——三件事分开钉。368 snapshot-vs-identical bundled unbundling 在本页 item 3 完成。

怎样编 `Snapshot`、怎样切块、怎样比较哈希是规范里的做法，本页不抄。snapident bundled（368）、快照全字段含 Metadata 对上不是已经装完（368 item 1 余量 / 851）、引擎不解释 format / hash 不是已经轻验 AppHash（368 item 2 余量 / 852）、Offer 收下就已经装完（321）、ListSnapshots 回了就已经齐（322）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **写成 1 not already complete ≠ 368 / 322 interchangeable：** 官方把至少 1 块和已经齐分开。
- **有上限 not already consensus-const ≠ 已经是共识常数 interchangeable：** 官方把 4 MB 上限和已经是共识常数分开。
- **能发 not already restored ≠ 已经装完 interchangeable：** 官方把能发和已经装完分开；368 snapshot-vs-identical bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写成 1 | 不是 already complete | 不是 ListSnapshots 回了就已经齐 alone（322） |
| 有上限 | 不是 already consensus-const | 不是对上了 already restored alone（851） |
| 能发 | 不是 already restored | 不是有哈希 already apphash-light alone（852） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量），必须分开写成 1 是不是 already complete interchangeable / 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable、有上限 是不是 already consensus-const interchangeable、能发 是不是 already restored interchangeable。可以跳过「看见写成 1 就已经齐 interchangeable / 就已经是共识常数 interchangeable / 就已经装完 interchangeable」。不要另写怎样写 Snapshot 类型。368 snapshot-vs-identical bundled unbundling 在本页 item 3 完成（851 + 852 + 853）。

## 本页不抄

- 怎样编 `Snapshot`、怎样切块、怎样比较哈希。
- snapident bundled。那是不变量 368。
- 快照全字段含 Metadata 对上不是已经装完。那是不变量 368 item 1 余量 / 851。
- 引擎不解释 format / hash 不是已经轻验 AppHash。那是不变量 368 item 2 余量 / 852。
- Offer 收下就已经装完。那是不变量 321。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 应用快照就已经从创世重放。那是不变量 38。
