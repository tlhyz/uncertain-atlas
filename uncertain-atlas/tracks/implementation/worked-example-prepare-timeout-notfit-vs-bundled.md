# 例：看见填了 TimeoutPropose is not already fits interchangeable / not already clock silent interchangeable / not already settled interchangeable

**层次**：实现 / 填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事（327 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事（327 余量）/ not 900 prepare-timeout-notfit interchangeable / not 327 prepare-timeout-vs-liveness bundled interchangeable」，不是 Prepare 及时性 bundled（327），也不是本地超时已经是最终性（47），也不是 timeout 必须按满块投递延迟算（344/883）。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。

## 官方三件事

1. **看见填了 TimeoutPropose / 看见同步期 这份初值 is not already 已经装得下这次 Prepare 执行 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 900 prepare-timeout-notfit interchangeable / 899 prepare-timeout-notpath interchangeable / 327 prepare-timeout item 1 立刻执行 interchangeable，也不是已经填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事 bundled（327 item 2 余量） interchangeable / 327 prepare-timeout item 2 interchangeable。**  
   官方写：若 *p* 的应用在 Prepare 里立刻整块执行，且 *p*、*q* 同在一轮、网络处在同步期，则 *q* 的 `TimeoutPropose` 必须装得下这次执行，让 *q* 的提议钟不响。看见填了这个值，不是已经装得下 interchangeable——本页从 327 item 2 侧钉 not already fits 单句。327 prepare-timeout vs liveness bundled unbundling 在本页 item 2 续。

2. **看见同步期 / 看见填了这个值 / 这份初值 is not already 已经 q 的提议钟不会响 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 900 prepare-timeout-notfit interchangeable / 327 prepare-timeout item 3 又开一轮 interchangeable / 901 prepare-timeout-notlost interchangeable，也不是已经本地超时已经是最终性 interchangeable / 47 local-timeout interchangeable。**  
   官方把同步期和钟已经不会响分开——327 bundled 第二件事常与 344 混成「看见填了 TimeoutPropose 就已经装得下这次 Prepare 或已经是满块投递那句 interchangeable」，本页钉 not already clock silent 单句。

3. **看见填了这个值 / 看见同步期 / 这份初值 is not already 已经交差 interchangeable，也不是已经 Prepare 及时性 bundled（327） interchangeable / 900 prepare-timeout-notfit interchangeable / 899 prepare-timeout-notpath interchangeable，也不是已经 timeout 必须按满块投递延迟算 interchangeable / 344 / 883 maxbytes-overhead-nottimeout interchangeable。**  
   官方把填了这个值和已经交差分开。看见填了这个值，不是已经交差 interchangeable。327 prepare-timeout vs liveness bundled unbundling 在本页 item 2 续。

怎样设 `TimeoutPropose`、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **填了 TimeoutPropose not already fits ≠ 已经装得下 interchangeable：** 官方把同步期里 q 的初值必须装得下 p 这次执行，和「看见填了」分开。
- **看见同步期 not already clock silent ≠ 钟已经不会响 interchangeable：** 官方把同步期和钟已经不会响分开。
- **看见填了这个值 not already settled ≠ 已经交差 interchangeable：** 官方把填了这个值和已经交差分开；327 prepare-timeout vs liveness bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 TimeoutPropose | 不是已经装得下 | 不是本地超时已经是最终性（47） |
| 看见同步期 | 不是钟已经不会响 | 不是 timeout 必须按满块投递延迟算（344/883） |
| 看见填了这个值 | 不是已经交差 | 不是立刻整块执行就已经离开关键路径（899） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 TimeoutPropose not already fits / not already clock silent / not already settled 正式三事（327 余量），必须分开是不是已经装得下、是不是钟已经不会响、是不是已经交差。可以跳过「看见填了 TimeoutPropose 就已经装得下」。不要把 TimeoutPropose 当不确定常数。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。327 prepare-timeout vs liveness bundled unbundling 在本页 item 2 续；续 [`worked-example-prepare-timeout-notlost-vs-bundled.md`](worked-example-prepare-timeout-notlost-vs-bundled.md)（不变量 901 item 3）。

## 本页不抄

- 怎样设 `TimeoutPropose`、默认秒数、怎样写立刻执行。
- Prepare 及时性 bundled。那是不变量 327。
- 立刻整块执行就已经离开关键路径。那是不变量 327 item 1 余量 / 899。
- 本地超时已经是最终性。那是不变量 47。
- timeout 必须按满块投递延迟算。那是不变量 344 / 883。
