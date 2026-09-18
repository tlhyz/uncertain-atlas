# 反模式：把 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量）说成已经按 ExecuteTxState 验过 / 已经按将要执行的那份验过 / 已经同一份

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CheckTx 过了 not already checked against ExecuteTxState ≠ bundled（312）](../../tracks/implementation/worked-example-checktxstate-notexecute-vs-bundled.md)。

## 卖法

把 CheckTx 过了 / 没报错 / 按 CheckTxState 顺序验过 写成已经按 ExecuteTxState 验过 interchangeable / 已经 checked against ExecuteTxState interchangeable / 已经按工作状态验 interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable；把进了池并开始流言 / Accepted into the mempool 写成已经按将要执行的那份状态验过 interchangeable / 已经 checked against to-be-executed state interchangeable；把重置了 / Commit 结束时重置成最新已提交 写成已经和 ExecuteTxState 同一份 interchangeable / 已经 same as ExecuteTxState after reset interchangeable，或已经和 312 checktxstate bundled / checktxstate-sold-as-execute interchangeable / 695 checktxstate-notexecute interchangeable。

## 为什么错

官方把 CheckTx 过了单句、already checked against ExecuteTxState、already checked against to-be-executed state、already same as ExecuteTxState after reset 写成三件独立的实现事。把它们卖成 already checked against ExecuteTxState interchangeable / already checked against to-be-executed state interchangeable / already same as ExecuteTxState after reset interchangeable，会把 not already checked against ExecuteTxState、not already checked against to-be-executed state、not already same as ExecuteTxState after reset 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量），必须分开 not already checked against ExecuteTxState、not already checked against to-be-executed state、not already same as ExecuteTxState after reset 三件事，不要和 312 / 33 / 696 / 697 / 311 / 301 糊成一句。

## 和相邻反模式

- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState bundled 全段，不是本页 CheckTx 过了 item 1 单句边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选 ≠ ExecuteTxState（311），不是本页 CheckTxState 验过边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了 ≠ 已经从池里删掉（301），不是本页进池流言边界。
