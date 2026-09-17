# 反模式：把 apply candidate state not ExecuteTxState 正式三事（360 余量）卖成 Finalize 时的 Process 保证 bundled / 已经是 ExecuteTxState / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[apply candidate state not ExecuteTxState ≠ bundled（360）](../../tracks/implementation/worked-example-finprocgua-notcand-vs-bundled.md)。

## 卖法

- 「看见 application may apply a candidate state from previous Prepare or Process 就已经是 ExecuteTxState interchangeable / 已经 previously executed interchangeable。」
- 「看见 execute according to FinalizeBlockRequest.txs / 同一块先跑过 就已经 Process 跑过就不执行 interchangeable / 已经不用再执行 interchangeable。」
- 「看见 can apply candidate / reuse memory state 就已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable。」

## 为什么错

官方把 may apply candidate、execute according to txs、reuse memory state 写成独立的实现事。把它们卖成 Finalize 时的 Process 保证 bundled、已经是 ExecuteTxState、已经交差，会把 not ExecuteTxState、not same block already ran means no need to execute、not already committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 apply candidate state not ExecuteTxState 正式三事（360 余量），必须分开 not ExecuteTxState、not same block already ran means no need to execute、not already committed 三个名字，不要把它们卖成 Finalize 时的 Process 保证 bundled / 已经是 ExecuteTxState / 已经交差。

## 和相邻反模式

- [finalize-sold-as-processed](finalize-sold-as-processed.md) 是 360 bundled 三事专用，不是本页 apply candidate not ExecuteTxState 单句边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是 311 专用，不是本页 may apply candidate 单句边界。
