# 例：看见立刻整块执行 is not already left critical path interchangeable / not already not blocking clock interchangeable / not already settled interchangeable

**层次**：实现 / 立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事（327 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事（327 余量）/ not 899 prepare-timeout-notpath interchangeable / not 327 prepare-timeout-vs-liveness bundled interchangeable」，不是 Prepare 及时性 bundled（327），也不是 timeout 必须按满块投递延迟算（344/883），也不是四门已经结算（33）。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。

## 官方三件事

1. **看见 Prepare 里立刻整块执行 / 看见执行回了 这份执行 is not already 已经离开提议超时的关键路径 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 899 prepare-timeout-notpath interchangeable / 900 prepare-timeout-notfit interchangeable / 327 prepare-timeout item 2 装得下 interchangeable，也不是已经立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事 bundled（327 item 1 余量） interchangeable / 327 prepare-timeout item 1 interchangeable。**  
   官方写：在 `PrepareProposal` 时整块执行，站在 CometBFT 的关键路径上。看见立刻执行了，不是已经离开这条路径 interchangeable——本页从 327 item 1 侧钉 not already left critical path 单句。327 prepare-timeout vs liveness bundled unbundling 在本页 item 1 启动。

2. **看见执行回了 / 看见候选写进内存 / 这份执行 is not already 已经不挡 q 的提议钟 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 899 prepare-timeout-notpath interchangeable / 327 prepare-timeout item 3 又开一轮 interchangeable / 901 prepare-timeout-notlost interchangeable，也不是已经 timeout 必须按满块投递延迟算 interchangeable / 344 / 883 maxbytes-overhead-nottimeout interchangeable。**  
   官方把执行回了和已经不挡提议钟分开——327 bundled 第一件事常与 344 混成「看见立刻执行了就已经离开关键路径或已经是满块投递延迟那把尺 interchangeable」，本页钉 not already not blocking clock 单句。

3. **看见候选写进内存 / 看见立刻执行了 / 这份执行 is not already 已经交差 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 899 prepare-timeout-notpath interchangeable / 900 prepare-timeout-notfit interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把候选写进内存和已经交差分开。看见候选写进内存，不是已经交差 interchangeable。327 prepare-timeout vs liveness bundled unbundling 在本页 item 1 启动。

怎样设 `TimeoutPropose`、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **立刻整块执行 not already left critical path ≠ 已经离开关键路径 interchangeable：** 官方把 Prepare 里整块执行写成站在提议钟的关键路径上。
- **看见执行回了 not already not blocking clock ≠ 已经不挡提议钟 interchangeable：** 官方把执行回了和已经不挡 q 的提议钟分开。
- **看见候选写进内存 not already settled ≠ 已经交差 interchangeable：** 官方把候选写进内存和已经交差分开；327 prepare-timeout vs liveness bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻整块执行 | 不是已经离开关键路径 | 不是 timeout 必须按满块投递延迟算（344/883） |
| 看见执行回了 | 不是已经不挡提议钟 | 不是四门已经结算（33） |
| 看见候选写进内存 | 不是已经交差 | 不是填了 TimeoutPropose 就已经装得下（900） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻整块执行 not already left critical path / not already not blocking clock / not already settled 正式三事（327 余量），必须分开是不是已经离开关键路径、是不是已经不挡提议钟、是不是已经交差。可以跳过「看见立刻执行了就已经离开关键路径」。不要把 TimeoutPropose 当不确定常数。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。327 prepare-timeout vs liveness bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-timeout-notfit-vs-bundled.md`](worked-example-prepare-timeout-notfit-vs-bundled.md)（不变量 900 item 2）。

## 本页不抄

- 怎样设 `TimeoutPropose`、默认秒数、怎样写立刻执行。
- Prepare 及时性 bundled。那是不变量 327。
- 填了 TimeoutPropose 就已经装得下。那是不变量 327 item 2 余量 / 900。
- timeout 必须按满块投递延迟算。那是不变量 344 / 883。
- 四门已经结算。那是不变量 33。
