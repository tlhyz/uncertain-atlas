# 例：看见又开一轮 / 看见 TimeoutPropose 只是初值 / 看见超时还会涨 is not already already liveness-lost interchangeable / already timeout-frozen interchangeable / already final-tier interchangeable

**层次**：实现 / 又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量）/ not 739 preparetimeout-notlivenesslost interchangeable / not 327 preparetimeout bundled interchangeable」，不是 PrepareProposal 及时性 bundled（327），也不是立刻整块执行不是已经离开关键路径（737 item 1 余量）或填了 TimeoutPropose 不是已经装得下（738 item 2 余量）。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。

## 官方三件事

规范把 Requirements 里违反 Requirement 1 可能再开一轮但不会因此丢掉活性、`TimeoutPropose` 只是初值会动态往上调 和「已经是又开一轮就已经丢了活性 interchangeable / 已经是初值就已经超时不再涨 interchangeable / 已经是看见初值就已经是最后那一档 interchangeable / 已经是 PrepareProposal 及时性 bundled interchangeable」分开写成三件独立的实现事，不是「看见又开一轮就已经丢了活性 interchangeable / 就已经超时不再涨 interchangeable / 就已经是最后那一档 interchangeable」一件事：

1. **看见又开一轮 / 看见再开一轮 / 看见违反后可能再开一轮 is not already 已经丢了活性 interchangeable / 已经 liveness-lost interchangeable / 已经活性丢掉交差 interchangeable / 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 739 preparetimeout-notlivenesslost interchangeable / 327 preparetimeout item 3 interchangeable，也不是已经又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事 bundled（327 item 3 余量） interchangeable / 327 preparetimeout item 3 interchangeable，也不是已经立刻整块执行不是已经离开关键路径（737） interchangeable / 738 preparetimeout-notfit interchangeable / 47 local-timeout interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：违反 Requirement 1 **可能再开一轮**，**不会**因此丢掉活性。看见又开一轮，不是已经 liveness-lost interchangeable——327 钉 bundled 三事，本页从 item 3 侧钉 not already liveness-lost 单句。看见再开一轮，不是已经 PrepareProposal 及时性 bundled（327） interchangeable——327 钉 bundled，本页钉 item 3 第一件事。看见违反后可能再开一轮，不是已经本地超时已经是最终性（47） interchangeable——47 另钉本地超时。327 preparetimeout vs liveness bundled unbundling 在本页 item 3 完成。

2. **看见 TimeoutPropose 只是初值 / 看见超时还会涨 / 看见动态往上调 is not already 已经超时不再涨 interchangeable / 已经 timeout-frozen interchangeable / 已经超时冻住交差 interchangeable / 327 preparetimeout bundled interchangeable / 416 proposetimeout interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 739 preparetimeout-notlivenesslost interchangeable / 327 preparetimeout item 1 关键路径 interchangeable / 327 preparetimeout item 2 装得下 interchangeable，也不是已经又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事 bundled（327 item 3 余量） interchangeable / 327 preparetimeout item 3 interchangeable，也不是已经丢了活性（本页第一件事） interchangeable。**  
   官方写：`TimeoutPropose` 只是初值；CometBFT 会动态把超时往上调，直到够完成本次 Prepare。看见 TimeoutPropose 只是初值，不是已经 timeout-frozen interchangeable——本页钉 not already timeout-frozen 单句。看见超时还会涨，不是已经进了这一轮会先设 ProposeTimeout（416） interchangeable——416 另钉 ProposeTimeout。看见动态往上调，不是已经丢了活性（本页第一件事） interchangeable——三件事分开钉。327 preparetimeout vs liveness bundled unbundling 在本页 item 3 完成。

3. **看见初值 / 看见不是最后那一档 / 看见还会再调 is not already 已经是最后那一档 interchangeable / 已经 final-tier interchangeable / 已经末档交差 interchangeable / 327 preparetimeout bundled interchangeable / 52 next-block-delay interchangeable，也不是已经 PrepareProposal 及时性 bundled（327） interchangeable / 739 preparetimeout-notlivenesslost interchangeable / 327 preparetimeout item 1 / 327 preparetimeout item 2，也不是已经又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事 bundled（327 item 3 余量） interchangeable / 327 preparetimeout item 3 interchangeable，也不是已经丢了活性（本页第一件事） interchangeable / 已经超时不再涨（本页第二件事） interchangeable。**  
   官方把初值和已经是最后那一档分开——看见初值，不等于已经是最后那一档。看见初值，不是已经 final-tier interchangeable——本页钉 not already final-tier 单句。看见不是最后那一档，不是已经应用 delay 已经是槽位（52） interchangeable——52 另钉 delay。看见还会再调，不是已经超时不再涨（本页第二件事） interchangeable——三件事分开钉。327 preparetimeout vs liveness bundled unbundling 在本页 item 3 完成。

怎样设 TimeoutPropose、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。PrepareProposal 及时性 bundled（327）、立刻整块执行不是已经离开关键路径（327 item 1 余量 / 737）、填了 TimeoutPropose 不是已经装得下（327 item 2 余量 / 738）、四门已经结算（33）、本地超时已经是最终性（47）、进了这一轮会先设 ProposeTimeout（416）、应用 delay 已经是槽位（52）是另外那套，本页不抄。

## 官方为什么这样拆

- **又开一轮 not already liveness-lost ≠ 327 / 33 interchangeable：** 官方把再开一轮和丢掉活性分开。
- **TimeoutPropose 只是初值 not already timeout-frozen ≠ 已经超时不再涨 interchangeable：** 官方把初值和动态往上调分开。
- **看见初值 not already final-tier ≠ 已经是最后那一档 interchangeable：** 官方把初值和已经是最后那一档分开；327 preparetimeout vs liveness bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 又开一轮 | 不是 already liveness-lost | 不是本地超时 alone（47） |
| TimeoutPropose 只是初值 | 不是 already timeout-frozen | 不是 ProposeTimeout alone（416） |
| 看见初值 | 不是 already final-tier | 不是应用 delay alone（52） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量），必须分开又开一轮 是不是 already liveness-lost interchangeable / 327 preparetimeout bundled interchangeable / preparetimeout-sold-as-liveness interchangeable、TimeoutPropose 只是初值 是不是 already timeout-frozen interchangeable、看见初值 是不是 already final-tier interchangeable。可以跳过「看见又开一轮就已经丢了活性 interchangeable / 就已经超时不再涨 interchangeable / 就已经是最后那一档 interchangeable」。不要另写怎样设 TimeoutPropose。327 preparetimeout vs liveness bundled unbundling 在本页 item 3 完成（737 + 738 + 739）。

## 本页不抄

- 怎样设 TimeoutPropose、默认秒数、怎样写立刻执行。
- PrepareProposal 及时性 bundled。那是不变量 327。
- 立刻整块执行不是已经离开关键路径。那是不变量 327 item 1 余量 / 737。
- 填了 TimeoutPropose 不是已经装得下。那是不变量 327 item 2 余量 / 738。
- 四门已经结算。那是不变量 33。
- 本地超时已经是最终性。那是不变量 47。
- 进了这一轮会先设 ProposeTimeout。那是不变量 416。
- 应用 delay 已经是槽位。那是不变量 52。
