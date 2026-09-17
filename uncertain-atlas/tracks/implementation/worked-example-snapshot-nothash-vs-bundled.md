# 例：看见引擎不解释 format / hash is not already light-verified AppHash interchangeable / not already genesis replay interchangeable / not already selected interchangeable

**层次**：实现 / 引擎不解释 format/hash not already light-verified AppHash / not already genesis replay / not already selected 正式三事（368 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎不解释 format/hash not already light-verified AppHash / not already genesis replay / not already selected 正式三事（368 余量）/ not 822 snapshot-nothash interchangeable / not 368 snapshot-vs-identical bundled interchangeable」，不是 Snapshot 类型 bundled（368），也不是应用快照就已经从创世重放（38），也不是本头 AppHash 就已经轻验（325），也不是 Offer 收下就已经装完（321）。不要另写怎样写 Snapshot 类型。

## 官方三件事

1. **看见 `format` 是应用自己的版本、引擎不解释 `format` / `hash`、只比较 `hash` / 看见有哈希 / 这份比较 is not already 已经轻验 AppHash interchangeable / 325 queryproof interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 822 snapshot-nothash interchangeable / 821 snapshot-notrestored interchangeable / 368 snapshot item 1 对上 interchangeable，也不是已经引擎不解释 format/hash not already light-verified AppHash / not already genesis replay / not already selected 正式三事 bundled（368 item 2 余量） interchangeable / 368 snapshot item 2 interchangeable。**  
   官方写：`hash` 是任意快照哈希，只在各节点同一份时相等。CometBFT 不解释哈希，只比较。看见有哈希，不是已经轻验 AppHash interchangeable——本页从 368 item 2 侧钉 not already light-verified AppHash 单句。368 snapshot vs identical bundled unbundling 在本页 item 2 续。

2. **看见有哈希 / 看见比过了 / 这份比较 is not already 已经从创世重放 interchangeable / 38 snapshotreplay interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 822 snapshot-nothash interchangeable / 368 snapshot item 3 至少 1 块 interchangeable / 823 snapshot-notcomplete interchangeable，也不是已经应用快照就已经从创世重放 interchangeable / 38 snapshotreplay interchangeable。**  
   官方把比过了和已经从创世重放分开——368 bundled 第二件事常与 325 / 38 混成「看见有哈希就已经轻验 AppHash 或已经从创世重放 interchangeable」，本页钉 not already genesis replay 单句。

3. **看见有哈希 / 看见有 format / 这份比较 is not already 已经选型 interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 822 snapshot-nothash interchangeable / 821 snapshot-notrestored interchangeable。**  
   官方把有 format 和已经选型分开。看见有 format，不是已经选型 interchangeable。368 snapshot vs identical bundled unbundling 在本页 item 2 续。

怎样编 Snapshot、怎样切块、怎样比较哈希是规范里的做法，本页不抄。

## 官方为什么这样拆

- **引擎不解释 format/hash not already light-verified ≠ 325 interchangeable：** 官方把比较哈希和轻验 AppHash 分开。
- **看见比过了 not already genesis replay ≠ 38 interchangeable：** 官方把比较哈希和从创世重放分开。
- **看见有 format not already selected ≠ 已经选型 interchangeable：** 官方把有 format 和已经选型分开；368 snapshot vs identical bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 引擎不解释 format / hash | 不是已经轻验 AppHash（325） | 不是全字段对上（821/368 item 1） |
| 看见比过了 | 不是已经从创世重放（38） | 不是至少 1 块（823/368 item 3） |
| 看见有 format | 不是已经选型 | 不是 Offer 收下就已经装完（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不解释 format/hash not already light-verified AppHash / not already genesis replay / not already selected 正式三事（368 余量），必须分开是不是已经轻验 AppHash interchangeable / 325、是不是已经从创世重放 interchangeable / 38、是不是已经选型。可以跳过「看见有哈希就已经轻验 AppHash」。不要另写怎样写 Snapshot 类型。368 snapshot vs identical bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-notcomplete-vs-bundled.md`](worked-example-snapshot-notcomplete-vs-bundled.md)（不变量 823 item 3）。

## 本页不抄

- 怎样编 Snapshot、怎样切块、怎样比较哈希。
- Snapshot 类型 bundled。那是不变量 368。
- 全字段对上。那是不变量 368 item 1 余量 / 821。
- 应用快照就已经从创世重放。那是不变量 38。
- 本头 AppHash 就已经轻验。那是不变量 325。
