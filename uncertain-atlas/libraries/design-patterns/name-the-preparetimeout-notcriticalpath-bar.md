# 模式：把立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**例**：[立刻执行 not already left-critical-path ≠ bundled（327）](../../tracks/implementation/worked-example-preparetimeout-notcriticalpath-vs-bundled.md)。

## 三个名字

1. **立刻执行了 不是 already left-critical-path：** 看见立刻执行了 / Prepare 里立刻整块执行 / 整块执行跑了，不是已经离开提议超时的关键路径 interchangeable / 已经离开关键路径交差 interchangeable，不是 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable。

2. **执行回了 不是 already unblocks-propose-clock：** 看见执行回了 / Prepare 执行回了 / 整块执行返回了，不是已经不挡 q 的提议钟 interchangeable / 已经不挡提议钟交差 interchangeable，不是 47 local-timeout interchangeable / 327 preparetimeout item 2 interchangeable。

3. **候选写进内存 不是 already candidate-settled：** 看见候选写进内存 / 候选在内存里 / Prepare 写了候选，不是已经交差 interchangeable / 已经候选交差 interchangeable，不是 311 candidate interchangeable / 327 preparetimeout item 3 interchangeable。

官方把立刻执行了单句、already left-critical-path、already unblocks-propose-clock、already candidate-settled 写成三个名字。把它们叫成一个「看见 Prepare 里立刻整块执行就已经离开关键路径 interchangeable / 就已经不挡提议钟 interchangeable / 就已经交差 interchangeable」，会把 not already left-critical-path、not already unblocks-propose-clock、not already candidate-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量），先数清问的是立刻执行了 是不是 already left-critical-path / 327 / preparetimeout-sold-as-liveness，是不是执行回了 是不是 already unblocks-propose-clock，还是候选写进内存 是不是 already candidate-settled，再决定要不要同一次发布。327 preparetimeout vs liveness bundled unbundling 在本页 item 1 启动。
