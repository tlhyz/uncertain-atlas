# 例：看见立刻执行了 / 看见执行回了 / 看见候选写进内存 is not already already left-critical-path interchangeable / already unblocks-propose-clock interchangeable / already candidate-settled interchangeable

**层次**：实现 / 立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量）/ not 737 preparetimeout-notcriticalpath interchangeable / not 327 preparetimeout bundled interchangeable」，不是 PrepareProposal 及时性 bundled（327），也不是填了 TimeoutPropose 不是已经装得下（738 item 2 余量）或又开一轮不是已经丢了活性（739 item 3 余量）。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。

## 官方三件事

规范把 Requirements 里在 `PrepareProposal` 时整块执行站在 CometBFT 的关键路径上 和「已经是立刻执行了就已经离开关键路径 interchangeable / 已经是执行回了就已经不挡提议钟 interchangeable / 已经是候选写进内存就已经交差 interchangeable / 已经是 PrepareProposal 及时性 bundled interchangeable」分开写成三件独立的实现事，不是「看见 Prepare 里立刻整块执行就已经离开关键路径 interchangeable / 就已经不挡提议钟 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见立刻执行了 / 看见 Prepare 里立刻整块执行 / 看见整块执行跑了 is not already 已经离开提议超时的关键路径 interchangeable / 已经 left-critical-path interchangeable / 已经离开关键路径交差 interchangeable / 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 737 preparetimeout-notcriticalpath interchangeable / 327 preparetimeout item 1 interchangeable，也不是已经立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事 bundled（327 item 1 余量） interchangeable / 327 preparetimeout item 1 interchangeable，也不是已经填了 TimeoutPropose 不是已经装得下（738） interchangeable / 739 preparetimeout-notlivenesslost interchangeable / 311 candidate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：在 `PrepareProposal` 时整块执行，站在 CometBFT 的**关键路径**上。看见立刻执行了，不是已经 left-critical-path interchangeable——327 钉 bundled 三事，本页从 item 1 侧钉 not already left-critical-path 单句。看见 Prepare 里立刻整块执行，不是已经 PrepareProposal 及时性 bundled（327） interchangeable——327 钉 bundled，本页钉 item 1 第一件事。看见整块执行跑了，不是已经四门已经结算（33） interchangeable——33 另钉四门。327 preparetimeout vs liveness bundled unbundling 在本页 item 1 启动。

2. **看见执行回了 / 看见 Prepare 执行回了 / 看见整块执行返回了 is not already 已经不挡 q 的提议钟 interchangeable / 已经 unblocks-propose-clock interchangeable / 已经不挡提议钟交差 interchangeable / 327 preparetimeout bundled interchangeable / 47 local-timeout interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 737 preparetimeout-notcriticalpath interchangeable / 327 preparetimeout item 2 装得下 interchangeable / 327 preparetimeout item 3 又开一轮 interchangeable，也不是已经立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事 bundled（327 item 1 余量） interchangeable / 327 preparetimeout item 1 interchangeable，也不是已经离开关键路径（本页第一件事） interchangeable。**  
   官方把执行回了和已经不挡提议钟分开——执行回了，不等于已经不挡 q 的提议钟。看见执行回了，不是已经 unblocks-propose-clock interchangeable——本页钉 not already unblocks-propose-clock 单句。看见 Prepare 执行回了，不是已经离开关键路径（本页第一件事） interchangeable——三件事分开钉。看见整块执行返回了，不是已经本地超时已经是最终性（47） interchangeable——47 另钉本地超时。327 preparetimeout vs liveness bundled unbundling 在本页 item 1 启动。

3. **看见候选写进内存 / 看见候选在内存里 / 看见 Prepare 写了候选 is not already 已经交差 interchangeable / 已经 candidate-settled interchangeable / 已经候选交差 interchangeable / 327 preparetimeout bundled interchangeable / 311 candidate interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 737 preparetimeout-notcriticalpath interchangeable / 327 preparetimeout item 2 / 327 preparetimeout item 3，也不是已经立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事 bundled（327 item 1 余量） interchangeable / 327 preparetimeout item 1 interchangeable，也不是已经离开关键路径（本页第一件事） interchangeable / 已经不挡提议钟（本页第二件事） interchangeable。**  
   官方把候选写进内存和已经交差分开——写进内存，不等于已经交差。看见候选写进内存，不是已经 candidate-settled interchangeable——本页钉 not already candidate-settled 单句。看见候选在内存里，不是已经候选已经是 ExecuteTxState（311） interchangeable——311 另钉候选。看见 Prepare 写了候选，不是已经不挡提议钟（本页第二件事） interchangeable——三件事分开钉。327 preparetimeout vs liveness bundled unbundling 在本页 item 1 完成。

怎样设 TimeoutPropose、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。PrepareProposal 及时性 bundled（327）、填了 TimeoutPropose 不是已经装得下（327 item 2 余量 / 738）、又开一轮不是已经丢了活性（327 item 3 余量 / 739）、四门已经结算（33）、本地超时已经是最终性（47）、候选已经是 ExecuteTxState（311）是另外那套，本页不抄。

## 官方为什么这样拆

- **立刻执行 not already left-critical-path ≠ 327 / 33 interchangeable：** 官方把 Prepare 里整块执行写成站在提议钟的关键路径上。
- **执行回了 not already unblocks-propose-clock ≠ 已经不挡提议钟 interchangeable：** 官方把执行回了和已经不挡 q 的提议钟分开。
- **候选写进内存 not already candidate-settled ≠ 已经交差 interchangeable：** 官方把写进内存和已经交差分开；327 preparetimeout vs liveness bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻执行了 | 不是 already left-critical-path | 不是四门 alone（33） |
| 执行回了 | 不是 already unblocks-propose-clock | 不是本地超时 alone（47） |
| 候选写进内存 | 不是 already candidate-settled | 不是候选 ExecuteTxState alone（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻整块执行不是已经离开关键路径 not already left-critical-path / not already unblocks-propose-clock / not already candidate-settled 正式三事（327 余量），必须分开立刻执行了 是不是 already left-critical-path interchangeable / 327 preparetimeout bundled interchangeable / preparetimeout-sold-as-liveness interchangeable、执行回了 是不是 already unblocks-propose-clock interchangeable、候选写进内存 是不是 already candidate-settled interchangeable。可以跳过「看见 Prepare 里立刻整块执行就已经离开关键路径 interchangeable / 就已经不挡提议钟 interchangeable / 就已经交差 interchangeable」。不要另写怎样设 TimeoutPropose。327 preparetimeout vs liveness bundled unbundling 在本页 item 1 启动；续 [`worked-example-preparetimeout-notfit-vs-bundled.md`](worked-example-preparetimeout-notfit-vs-bundled.md)（不变量 738 item 2）。

## 本页不抄

- 怎样设 TimeoutPropose、默认秒数、怎样写立刻执行。
- PrepareProposal 及时性 bundled。那是不变量 327。
- 填了 TimeoutPropose 不是已经装得下。那是不变量 327 item 2 余量 / 738。
- 又开一轮不是已经丢了活性。那是不变量 327 item 3 余量 / 739。
- 四门已经结算。那是不变量 33。
- 本地超时已经是最终性。那是不变量 47。
- 候选已经是 ExecuteTxState。那是不变量 311。
