# 例：看见又开一轮 is not already lost liveness interchangeable / not already timeout frozen interchangeable / not already settled interchangeable

**层次**：实现 / 又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事（327 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事（327 余量）/ not 901 prepare-timeout-notlost interchangeable / not 327 prepare-timeout-vs-liveness bundled interchangeable」，不是 Prepare 及时性 bundled（327），也不是 Process 非确定 bug 已经丢了安全性（340/895），也不是应用 delay 已经是槽位（52）。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。

## 官方三件事

1. **看见又开一轮 / 看见 TimeoutPropose 只是初值 这份一轮 is not already 已经丢了活性 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 901 prepare-timeout-notlost interchangeable / 899 prepare-timeout-notpath interchangeable / 327 prepare-timeout item 1 立刻执行 interchangeable，也不是已经又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事 bundled（327 item 3 余量） interchangeable / 327 prepare-timeout item 3 interchangeable。**  
   官方写：违反 Requirement 1 可能再开一轮，不会因此丢掉活性。看见又开一轮，不是已经停 interchangeable——本页从 327 item 3 侧钉 not already lost liveness 单句。327 prepare-timeout vs liveness bundled unbundling 在本页 item 3 完成。

2. **看见 TimeoutPropose 只是初值 / 看见又开一轮 / 这份一轮 is not already 已经超时不再涨 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 901 prepare-timeout-notlost interchangeable / 327 prepare-timeout item 2 装得下 interchangeable / 900 prepare-timeout-notfit interchangeable，也不是已经 Process 非确定 bug 已经丢了安全性 interchangeable / 340 / 895 process-det-notfix interchangeable。**  
   官方把初值和已经是最后那一档分开——327 bundled 第三件事常与 340 混成「看见又开一轮就已经丢了活性或已经丢了安全性 interchangeable」，本页钉 not already timeout frozen 单句。

3. **看见又开一轮 / 看见初值 / 这份一轮 is not already 已经交差 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 901 prepare-timeout-notlost interchangeable / 899 prepare-timeout-notpath interchangeable，也不是已经应用 delay 已经是槽位 interchangeable / 52 next-block-delay interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把又开一轮和已经交差分开。看见又开一轮，不是已经交差 interchangeable。327 prepare-timeout vs liveness bundled unbundling 在本页 item 3 完成。

怎样设 `TimeoutPropose`、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **又开一轮 not already lost liveness ≠ 已经丢了活性 interchangeable：** 官方把再开一轮和丢掉活性分开。
- **看见初值 not already timeout frozen ≠ 超时已经不再涨 interchangeable：** 官方把 TimeoutPropose 只是初值和已经是最后那一档分开；初值会涨，不是已经停。
- **看见又开一轮 not already settled ≠ 已经交差 interchangeable：** 官方把又开一轮和已经交差分开；327 prepare-timeout vs liveness bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 又开一轮 | 不是已经丢了活性 | 不是 Process 非确定 bug 已经丢了安全性（340/895） |
| 看见初值 | 不是超时已经不再涨 | 不是应用 delay 已经是槽位（52） |
| 看见又开一轮 | 不是已经交差 | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看又开一轮 not already lost liveness / not already timeout frozen / not already settled 正式三事（327 余量），必须分开是不是已经丢了活性、是不是超时已经不再涨、是不是已经交差。可以跳过「看见又开一轮就已经丢了活性」。不要把 TimeoutPropose 当不确定常数。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。327 prepare-timeout vs liveness bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 `TimeoutPropose`、默认秒数、怎样写立刻执行。
- Prepare 及时性 bundled。那是不变量 327。
- 立刻整块执行就已经离开关键路径。那是不变量 327 item 1 余量 / 899。
- Process 非确定 bug 已经丢了安全性。那是不变量 340 / 895。
- 应用 delay 已经是槽位。那是不变量 52。
- 候选已经是 ExecuteTxState。那是不变量 311。
