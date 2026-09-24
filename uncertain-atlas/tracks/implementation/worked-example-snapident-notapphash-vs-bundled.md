# 例：看见有哈希 / 看见有 format / 看见比过了 is not already already apphash-light interchangeable / already algo interchangeable / already genesis-replay interchangeable

**层次**：实现 / 引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量）/ not 852 snapident-notapphash interchangeable / not 368 snapident bundled interchangeable」，不是 snapident bundled（368），也不是快照全字段含 Metadata 对上不是已经装完（851 item 1 余量）或空快照也至少 1 块不是已经齐（853 item 3 余量）。不要另写怎样写 Snapshot 类型。

## 官方三件事

规范把 Methods 里 `format` 是应用自己的版本、引擎不解释 `format` / `hash`、只比较 `hash` 和「已经是有哈希就已经轻验 AppHash interchangeable / 已经是有 format 就已经选型 interchangeable / 已经是比过了就已经从创世重放 interchangeable / 已经是 snapident bundled interchangeable」分开写成三件独立的实现事，不是「看见有哈希就已经轻验 AppHash interchangeable / 就已经选型 interchangeable / 就已经从创世重放 interchangeable」一件事：

1. **看见有哈希 / 看见 `hash` 是任意快照哈希、只在各节点同一份时相等、引擎不解释哈希只比较 / 看见有 hash 字段 is not already 已经轻验 AppHash interchangeable / 已经 apphash-light interchangeable / 已经轻验 AppHash 交差 interchangeable / 368 snapident bundled interchangeable / 322 listsnap interchangeable / snapshot-sold-as-identical interchangeable，也不是已经 snapident bundled（368） interchangeable / 852 snapident-notapphash interchangeable / 368 snapident item 2 interchangeable，也不是已经引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事 bundled（368 item 2 余量） interchangeable / 368 snapident item 2 interchangeable，也不是已经对上了就已经装完（851） interchangeable / 853 snapident-notcomplete interchangeable / 38 genesis-replay interchangeable，也不是已经 ListSnapshots 回了就已经齐（322） interchangeable。**  
   官方写：`hash` 是任意快照哈希，只在各节点同一份时相等。CometBFT 不解释哈希，只比较。看见有哈希，不是已经轻验 AppHash。看见有哈希，不是已经 apphash-light interchangeable——368 钉 bundled 三事，本页从 item 2 侧钉 not already apphash-light 单句。看见 `hash` 是任意快照哈希、引擎不解释只比较，不是已经 snapident bundled（368） interchangeable——368 钉 bundled，本页钉 item 2 第一件事。看见有哈希，不是已经对上了就已经装完（851） interchangeable——851 另钉 item 1。看见有哈希，不是已经至少 1 块就已经齐（853） interchangeable——853 另钉 item 3。368 snapshot-vs-identical bundled unbundling 在本页 item 2 续。

2. **看见有 format / 看见 `format` 是应用自己的快照格式、用来给数据格式做版本 / 看见有 format 字段 is not already 已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 368 snapident bundled interchangeable / 321 offer interchangeable，也不是已经 snapident bundled（368） interchangeable / 852 snapident-notapphash interchangeable / 368 snapident item 1 对上 interchangeable / 368 snapident item 3 至少 1 块 interchangeable，也不是已经引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事 bundled（368 item 2 余量） interchangeable / 368 snapident item 2 interchangeable，也不是已经轻验 AppHash（本页第一件事） interchangeable。**  
   官方写：看见有 format，不是已经选型。看见 `format` 是应用自己的快照格式，不是已经 algo interchangeable——本页钉 not already algo 单句。看见有 format 字段，不是已经轻验 AppHash（本页第一件事） interchangeable——三件事分开钉。368 snapshot-vs-identical bundled unbundling 在本页 item 2 续。

3. **看见比过了 / 看见引擎只比较 hash、比过了同一份 / 看见比较过 is not already 已经从创世重放 interchangeable / 已经 genesis-replay interchangeable / 已经从创世重放交差 interchangeable / 368 snapident bundled interchangeable / 38 genesis-replay interchangeable，也不是已经 snapident bundled（368） interchangeable / 852 snapident-notapphash interchangeable / 368 snapident item 1 / 368 snapident item 3，也不是已经引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事 bundled（368 item 2 余量） interchangeable / 368 snapident item 2 interchangeable，也不是已经轻验 AppHash（本页第一件事） interchangeable / 已经选型（本页第二件事） interchangeable。**  
   官方写：看见比过了，不是已经从创世重放。看见引擎只比较 hash、比过了同一份，不是已经 genesis-replay interchangeable——本页钉 not already genesis-replay 单句。看见比较过，不是已经选型（本页第二件事） interchangeable——三件事分开钉。368 snapshot-vs-identical bundled unbundling 在本页 item 2 续。

怎样编 `Snapshot`、怎样切块、怎样比较哈希是规范里的做法，本页不抄。snapident bundled（368）、快照全字段含 Metadata 对上不是已经装完（368 item 1 余量 / 851）、空快照也至少 1 块不是已经齐（368 item 3 余量 / 853）、Offer 收下就已经装完（321）、ListSnapshots 回了就已经齐（322）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **有哈希 not already apphash-light ≠ 368 / 322 interchangeable：** 官方把比较哈希和轻验 AppHash 分开。
- **有 format not already algo ≠ 已经选型 interchangeable：** 官方把有 format 和已经选型分开。
- **比过了 not already genesis-replay ≠ 已经从创世重放 interchangeable：** 官方把比过了和已经从创世重放分开；368 snapshot-vs-identical bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有哈希 | 不是 already apphash-light | 不是 ListSnapshots 回了就已经齐 alone（322） |
| 有 format | 不是 already algo | 不是对上了 already restored alone（851） |
| 比过了 | 不是 already genesis-replay | 不是至少 1 块 already complete alone（853） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量），必须分开有哈希 是不是 already apphash-light interchangeable / 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable、有 format 是不是 already algo interchangeable、比过了 是不是 already genesis-replay interchangeable。可以跳过「看见有哈希就已经轻验 AppHash interchangeable / 就已经选型 interchangeable / 就已经从创世重放 interchangeable」。不要另写怎样写 Snapshot 类型。368 snapshot-vs-identical bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样编 `Snapshot`、怎样切块、怎样比较哈希。
- snapident bundled。那是不变量 368。
- 快照全字段含 Metadata 对上不是已经装完。那是不变量 368 item 1 余量 / 851。
- 空快照也至少 1 块不是已经齐。那是不变量 368 item 3 余量 / 853。
- Offer 收下就已经装完。那是不变量 321。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 应用快照就已经从创世重放。那是不变量 38。
