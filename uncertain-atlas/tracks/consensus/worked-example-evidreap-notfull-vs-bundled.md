# 例：看见先装证据 is not already full-of-txs interchangeable / not already executed interchangeable / not already settled interchangeable

**层次**：共识 / 先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量）/ not 989 evidreap-notfull interchangeable / not 299 evidence-vs-reap bundled interchangeable」，不是造提案 bundled（299），也不是四门已经结算（33），也不是创世 app_state 就已经验过（303/986）。不要另写怎样算扣减或怎样从池里收割。

## 官方三件事

1. **看见未处理的证据优先于内存池交易 / 看见先装证据 这份顺序 is not already 已经装满交易 interchangeable，也不是已经造提案 bundled（299） interchangeable / 989 evidreap-notfull interchangeable / 990 evidreap-notsame interchangeable / 299 evidence item 2 两条上限 interchangeable，也不是已经先装证据 not already full-of-txs / not already executed / not already settled 正式三事 bundled（299 item 1 余量） interchangeable / 299 evidence item 1 interchangeable。**  
   官方写：未处理的证据比内存池里未处理的交易优先。看见先装证据，不是这块已经装满交易 interchangeable——本页从 299 item 1 侧钉 not already full-of-txs 单句。299 evidence vs reap bundled unbundling 在本页 item 1 启动。

2. **看见证据进了提案 / 看见先装证据 / 这份顺序 is not already 已经执行 interchangeable，也不是已经造提案 bundled（299） interchangeable / 989 evidreap-notfull interchangeable / 299 evidence item 3 -1 无上限 interchangeable / 991 evidreap-notunlim interchangeable，也不是已经四门已经结算 interchangeable / 33 four-gates interchangeable。**  
   官方把证据进了提案和这些证据已经执行分开。看见证据进了提案，不是已经执行 interchangeable。本页钉 not already executed 单句。

3. **看见证据占了位置 / 看见先装证据 / 这份顺序 is not already 已经交差 interchangeable，也不是已经造提案 bundled（299） interchangeable / 989 evidreap-notfull interchangeable / 990 evidreap-notsame interchangeable，也不是已经创世 app_state 就已经验过 interchangeable / 303/986 genesis-notapp interchangeable。**  
   官方把证据占了位置和已经过了验收分开。看见证据占了位置，不是已经交差 interchangeable。299 evidence vs reap bundled unbundling 在本页 item 1 启动。

扣减公式、整块体积取值、怎样收割是规范里的做法，本页不抄。

## 官方为什么这样拆

- **先装证据 not already full-of-txs ≠ 已经装满交易 interchangeable：** 官方把证据优先写成装块顺序，不是执行，也不是验收。
- **看见证据进了提案 not already executed ≠ 已经执行 interchangeable：** 官方把证据进了提案和这些证据已经执行分开。
- **看见证据占了位置 not already settled ≠ 已经交差 interchangeable：** 官方把证据占了位置和已经过了验收分开；299 evidence vs reap bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 先装证据 | 不是已经装满交易 | 不是四门已经结算（33） |
| 看见证据进了提案 | 不是已经执行 | 不是创世 app_state 就已经验过（303/986） |
| 看见证据占了位置 | 不是已经交差 | 不是两条上限就已经同一条（990） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量），必须分开是不是已经装满交易、是不是已经执行、是不是已经交差。可以跳过「看见先装证据就已经装满交易」。不要另写怎样算扣减或怎样从池里收割。299 evidence vs reap bundled unbundling 在本页 item 1 启动；续 [`worked-example-evidreap-notsame-vs-bundled.md`](worked-example-evidreap-notsame-vs-bundled.md)（不变量 990 item 2）。

## 本页不抄

- 扣减公式、整块体积取值、protobuf 开销数字。
- 造提案 bundled。那是不变量 299。
- 四门已经结算。那是不变量 33。
- 创世 app_state 就已经验过。那是不变量 303/986。
