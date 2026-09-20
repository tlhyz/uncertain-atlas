# 反模式：把立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量）说成已经离开关键路径 / 已经不挡提议钟 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[立刻执行 not already left-critical-path ≠ bundled（327）](../../tracks/implementation/worked-example-preparetimeout-notcriticalpath-vs-bundled.md)。

## 卖法

把立刻执行了 / Prepare 里立刻整块执行 / 整块执行跑了 写成已经离开提议超时的关键路径 interchangeable / 已经 left-critical-path interchangeable / 已经离开关键路径交差 interchangeable / 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable；把执行回了 / Prepare 执行回了 / 整块执行返回了 写成已经不挡 q 的提议钟 interchangeable / 已经 unblocks-propose-clock interchangeable；把候选写进内存 / 候选在内存里 / Prepare 写了候选 写成已经交差 interchangeable / 已经 candidate-settled interchangeable，或已经和 327 preparetimeout bundled / preparetimeout-sold-as-liveness interchangeable / 737 preparetimeout-notcriticalpath interchangeable。

## 为什么错

官方把立刻执行了单句、already left-critical-path、already unblocks-propose-clock、already candidate-settled 写成三件独立的实现事。把它们卖成 already left-critical-path interchangeable / already unblocks-propose-clock interchangeable / already candidate-settled interchangeable，会把 not already left-critical-path、not already unblocks-propose-clock、not already candidate-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量），必须分开 not already left-critical-path、not already unblocks-propose-clock、not already candidate-settled 三件事，不要和 327 / 33 / 47 / 311 / 738 / 739 糊成一句。

## 和相邻反模式

- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是 PrepareProposal 及时性 bundled 全段，不是本页关键路径 item 1 单句边界。
- [preparetimeout-notfit-sold-as-bundled](preparetimeout-notfit-sold-as-bundled.md) 是填了 TimeoutPropose 装得下（327 item 2），不是本页关键路径 item 1 单句边界。
- [proposetimeout-sold-as-process](proposetimeout-sold-as-process.md) 是提议超时另一边界，不是本页立刻整块执行站在关键路径上。
- [peerfilter-notenginepath-sold-as-bundled](peerfilter-notenginepath-sold-as-bundled.md) 是 /store 路径（326 item 3），不是本页 Prepare 及时性边界。
