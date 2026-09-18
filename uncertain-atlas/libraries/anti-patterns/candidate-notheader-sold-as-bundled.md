# 反模式：把 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量）说成已经有本头哈希 / Prepare 当时已经有 / 已经是决定块身份

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Prepare 没有头哈希 not already have header hash ≠ bundled（311）](../../tracks/implementation/worked-example-candidate-notheader-vs-bundled.md)。

## 卖法

把 PrepareProposal 披露了提案 / Prepare 来了 / 两门给的字段差不多 写成已经有本头哈希 interchangeable / 已经 have header hash interchangeable / 已经知道本头 interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable；把 Process 有哈希 / Process 交了块头哈希 写成 Prepare 当时已经有 interchangeable / 已经 Prepare already had hash interchangeable；把字段齐了 / 交易列表 LastCommit 时间等都有了 写成已经能当决定块的身份 interchangeable / 已经 decided block identity interchangeable，或已经和 311 candidate bundled / candidate-sold-as-execute interchangeable / 692 candidate-notheader interchangeable。

## 为什么错

官方把 Prepare 披露单句、already have header hash、Prepare already had hash、already decided block identity 写成三件独立的实现事。把它们卖成 already have header hash interchangeable / Prepare already had hash interchangeable / already decided block identity interchangeable，会把 not already have header hash、not Prepare already had hash、not already decided block identity 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量），必须分开 not already have header hash、not Prepare already had hash、not already decided block identity 三件事，不要和 311 / 33 / 693 / 694 / 310 / 5 糊成一句。

## 和相邻反模式

- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选 ≠ ExecuteTxState bundled 全段，不是本页 Prepare 没有头哈希 item 1 单句边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是默认锁 ≠ 已经 RPC 安全（310），不是本页头哈希边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页 Prepare 披露 vs 本头哈希边界。
