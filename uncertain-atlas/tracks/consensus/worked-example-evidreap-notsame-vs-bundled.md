# 例：看见两条收交易上限 is not already same-cap interchangeable / not already pool-fits interchangeable / not already settled interchangeable

**层次**：共识 / 两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量）/ not 990 evidreap-notsame interchangeable / not 299 evidence-vs-reap bundled interchangeable」，不是造提案 bundled（299），也不是仓库默认 MaxBytes 已经是活性 SLA（63），也不是证据 MaxBytes 就已经落在块上限下面（331）。不要另写怎样算扣减或怎样从池里收割。

## 官方三件事

1. **看见提案按扣掉头、上次 commit、证据之后的上限收交易 / 看见内存池按假定没有证据的上限收 这份上限 is not already 已经同一条上限 interchangeable，也不是已经造提案 bundled（299） interchangeable / 990 evidreap-notsame interchangeable / 989 evidreap-notfull interchangeable / 299 evidence item 1 先装证据 interchangeable，也不是已经两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事 bundled（299 item 2 余量） interchangeable / 299 evidence item 2 interchangeable。**  
   官方写：从内存池收交易时，先扣掉头、整块开销、上次 commit 和证据，再谈还能装多少交易。进池之前的体积检查用同一套扣法，但假定没有证据。看见提案这边的交易上限，不是内存池已经按同一条收 interchangeable——本页从 299 item 2 侧钉 not already same-cap 单句。299 evidence vs reap bundled unbundling 在本页 item 2 续。

2. **看见内存池收得下 / 看见提案上限 / 这份上限 is not already 已经扣掉证据之后还收得下 interchangeable，也不是已经造提案 bundled（299） interchangeable / 990 evidreap-notsame interchangeable / 299 evidence item 3 -1 interchangeable / 991 evidreap-notunlim interchangeable，也不是已经仓库默认 MaxBytes 已经是活性 SLA interchangeable / 63 MaxBytes SLA interchangeable。**  
   官方把内存池收得下和提案扣掉证据之后还收得下分开。看见内存池收得下，不是提案扣掉证据之后还收得下 interchangeable。本页钉 not already pool-fits 单句。

3. **看见两套扣法 / 看见提案上限 / 这份上限 is not already 已经交差 interchangeable，也不是已经造提案 bundled（299） interchangeable / 990 evidreap-notsame interchangeable / 989 evidreap-notfull interchangeable，也不是已经证据 MaxBytes 就已经落在块上限下面 interchangeable / 331 evidence-maxbytes interchangeable。**  
   官方把两套扣法和已经交差分开。看见两套扣法，不是已经交差 interchangeable。299 evidence vs reap bundled unbundling 在本页 item 2 续。

扣减公式、整块体积取值、怎样收割是规范里的做法，本页不抄。

## 官方为什么这样拆

- **两条收交易上限 not already same-cap ≠ 已经同一条 interchangeable：** 官方把提案扣掉证据和内存池假定没有证据写成两套上限。
- **看见内存池收得下 not already pool-fits ≠ 提案扣掉证据之后还收得下 interchangeable：** 官方把内存池收得下和提案扣掉证据之后还收得下分开。
- **看见两套扣法 not already settled ≠ 已经交差 interchangeable：** 官方把两套扣法和已经交差分开；299 evidence vs reap bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两条收交易上限 | 不是已经同一条 | 不是仓库默认 MaxBytes 已经是活性 SLA（63） |
| 看见内存池收得下 | 不是提案扣掉证据之后还收得下 | 不是证据 MaxBytes 就已经落在块上限下面（331） |
| 看见两套扣法 | 不是已经交差 | 不是 -1 就已经没有上限（991） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量），必须分开是不是已经同一条、是不是提案扣掉证据之后还收得下、是不是已经交差。可以跳过「看见先装证据就已经装满交易」。不要另写怎样算扣减或怎样从池里收割。299 evidence vs reap bundled unbundling 在本页 item 2 续；续 [`worked-example-evidreap-notunlim-vs-bundled.md`](worked-example-evidreap-notunlim-vs-bundled.md)（不变量 991 item 3）。

## 本页不抄

- 扣减公式、整块体积取值、protobuf 开销数字。
- 造提案 bundled。那是不变量 299。
- 仓库默认 MaxBytes 已经是活性 SLA。那是不变量 63。
- 证据 MaxBytes 就已经落在块上限下面。那是不变量 331。
