# 例：看见填了 TimeoutPropose / 看见同步期 / 看见钟一响就 prevote nil is not already already fits-execution interchangeable / already clock-silent interchangeable / already propose-bound interchangeable

**层次**：实现 / 填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量）/ not 738 preparetimeout-notfit interchangeable / not 327 preparetimeout bundled interchangeable」，不是 PrepareProposal 及时性 bundled（327），也不是立刻整块执行不是已经离开关键路径（737 item 1 余量）或又开一轮不是已经丢了活性（739 item 3 余量）。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。

## 官方三件事

规范把 Requirements 里同步期 *q* 的 `TimeoutPropose` 必须装得下 *p* 这次 Prepare 执行、让 *q* 的提议钟不响 和「已经是填了 TimeoutPropose 就已经装得下 interchangeable / 已经是同步期就已经钟不响 interchangeable / 已经是钟一响就 prevote nil 就已经把提议绑死 interchangeable / 已经是 PrepareProposal 及时性 bundled interchangeable」分开写成三件独立的实现事，不是「看见填了 TimeoutPropose 就已经装得下 interchangeable / 就已经钟不响 interchangeable / 就已经把提议绑死 interchangeable」一件事：

1. **看见填了 TimeoutPropose / 看见填了这个值 / 看见有 TimeoutPropose 初值 is not already 已经装得下这次 Prepare 执行 interchangeable / 已经 fits-execution interchangeable / 已经装得下交差 interchangeable / 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 738 preparetimeout-notfit interchangeable / 327 preparetimeout item 2 interchangeable，也不是已经填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事 bundled（327 item 2 余量） interchangeable / 327 preparetimeout item 2 interchangeable，也不是已经立刻整块执行不是已经离开关键路径（737） interchangeable / 739 preparetimeout-notlivenesslost interchangeable / 47 local-timeout interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：若 *p* 的应用在 Prepare 里立刻整块执行，且 *p*、*q* 同在一轮、网络处在同步期，则 *q* 的 `TimeoutPropose` **必须**装得下这次执行。看见填了 TimeoutPropose，不是已经 fits-execution interchangeable——327 钉 bundled 三事，本页从 item 2 侧钉 not already fits-execution 单句。看见填了这个值，不是已经 PrepareProposal 及时性 bundled（327） interchangeable——327 钉 bundled，本页钉 item 2 第一件事。看见有 TimeoutPropose 初值，不是已经立刻整块执行不是已经离开关键路径（737） interchangeable——737 另钉 item 1。327 preparetimeout vs liveness bundled unbundling 在本页 item 2 续。

2. **看见同步期 / 看见 p、q 同在一轮 / 看见网络处在同步期 is not already 已经 q 的提议钟不会响 interchangeable / 已经 clock-silent interchangeable / 已经钟不响交差 interchangeable / 327 preparetimeout bundled interchangeable / 47 local-timeout interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 738 preparetimeout-notfit interchangeable / 327 preparetimeout item 1 关键路径 interchangeable / 327 preparetimeout item 3 又开一轮 interchangeable，也不是已经填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事 bundled（327 item 2 余量） interchangeable / 327 preparetimeout item 2 interchangeable，也不是已经装得下（本页第一件事） interchangeable。**  
   官方把同步期和已经钟不响分开——同在一轮、处在同步期，不等于 *q* 的提议钟已经不会响。看见同步期，不是已经 clock-silent interchangeable——本页钉 not already clock-silent 单句。看见 *p*、*q* 同在一轮，不是已经本地超时已经是最终性（47） interchangeable——47 另钉本地超时。看见网络处在同步期，不是已经装得下（本页第一件事） interchangeable——三件事分开钉。327 preparetimeout vs liveness bundled unbundling 在本页 item 2 续。

3. **看见钟一响就 prevote nil / 看见提议钟挂钩 / 看见钟响走 nil is not already 已经把这一轮提议绑成必成 interchangeable / 已经 propose-bound interchangeable / 已经提议绑死交差 interchangeable / 327 preparetimeout bundled interchangeable / 416 proposetimeout interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 738 preparetimeout-notfit interchangeable / 327 preparetimeout item 1 / 327 preparetimeout item 3，也不是已经填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事 bundled（327 item 2 余量） interchangeable / 327 preparetimeout item 2 interchangeable，也不是已经装得下（本页第一件事） interchangeable / 已经钟不响（本页第二件事） interchangeable。**  
   官方写：钟一响，*q* 在这一轮 prevote `nil`。看见钟一响就 prevote nil，不是已经 propose-bound interchangeable——挂钩不等于这一轮提议已经绑成必成。看见提议钟挂钩，不是已经进了这一轮会先设 ProposeTimeout（416） interchangeable——416 另钉 ProposeTimeout。看见钟响走 nil，不是已经钟不响（本页第二件事） interchangeable——三件事分开钉。327 preparetimeout vs liveness bundled unbundling 在本页 item 2 完成。

怎样设 TimeoutPropose、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。PrepareProposal 及时性 bundled（327）、立刻整块执行不是已经离开关键路径（327 item 1 余量 / 737）、又开一轮不是已经丢了活性（327 item 3 余量 / 739）、四门已经结算（33）、本地超时已经是最终性（47）、进了这一轮会先设 ProposeTimeout（416）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了 TimeoutPropose not already fits-execution ≠ 327 / 33 interchangeable：** 官方把填了初值和已经装得下这次 Prepare 执行分开。
- **同步期 not already clock-silent ≠ 已经钟不响 interchangeable：** 官方把同步期和 *q* 的提议钟已经不会响分开。
- **钟一响就 prevote nil not already propose-bound ≠ 已经把提议绑成必成 interchangeable：** 官方把钟响走 nil 和这一轮提议已经绑成必成分开；327 preparetimeout vs liveness bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 TimeoutPropose | 不是 already fits-execution | 不是关键路径 alone（737） |
| 同步期 | 不是 already clock-silent | 不是本地超时 alone（47） |
| 钟一响就 prevote nil | 不是 already propose-bound | 不是 ProposeTimeout alone（416） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量），必须分开填了 TimeoutPropose 是不是 already fits-execution interchangeable / 327 preparetimeout bundled interchangeable / preparetimeout-sold-as-liveness interchangeable、同步期 是不是 already clock-silent interchangeable、钟一响就 prevote nil 是不是 already propose-bound interchangeable。可以跳过「看见填了 TimeoutPropose 就已经装得下 interchangeable / 就已经钟不响 interchangeable / 就已经把提议绑死 interchangeable」。不要另写怎样设 TimeoutPropose。327 preparetimeout vs liveness bundled unbundling 在本页 item 2 续（737 + 738）；续 [`worked-example-preparetimeout-notlivenesslost-vs-bundled.md`](worked-example-preparetimeout-notlivenesslost-vs-bundled.md)（不变量 739 item 3）已写；完成见 739。

## 本页不抄

- 怎样设 TimeoutPropose、默认秒数、怎样写立刻执行。
- PrepareProposal 及时性 bundled。那是不变量 327。
- 立刻整块执行不是已经离开关键路径。那是不变量 327 item 1 余量 / 737。
- 又开一轮不是已经丢了活性。那是不变量 327 item 3 余量 / 739。
- 四门已经结算。那是不变量 33。
- 本地超时已经是最终性。那是不变量 47。
- 进了这一轮会先设 ProposeTimeout。那是不变量 416。
