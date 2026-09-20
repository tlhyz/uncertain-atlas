# 例：看见立刻整块执行不是已经离开关键路径；看见填了 TimeoutPropose 不是已经装得下；看见又开一轮不是已经丢了活性

**层次**：实现 / PrepareProposal 及时性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「立刻整块执行不是已经离开关键路径 / 填了 TimeoutPropose 不是已经装得下 / 又开一轮不是已经丢了活性」，不是四门已经结算，也不是本地超时已经是最终性。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。 327 preparetimeout vs liveness bundled unbundling 完成（737 + 738 + 739）；精读 [`worked-example-preparetimeout-notcriticalpath-vs-bundled.md`](worked-example-preparetimeout-notcriticalpath-vs-bundled.md)（不变量 737 item 1）；[`worked-example-preparetimeout-notfit-vs-bundled.md`](worked-example-preparetimeout-notfit-vs-bundled.md)（不变量 738 item 2）；[`worked-example-preparetimeout-notlivenesslost-vs-bundled.md`](worked-example-preparetimeout-notlivenesslost-vs-bundled.md)（不变量 739 item 3）。

## 官方三件事

规范把 Prepare 里立刻整块执行和提议超时写成三件独立的实现事，不是「看见立刻执行了就已经离开关键路径、已经装得下、已经丢了活性」一件事：

1. **看见 Prepare 里立刻整块执行 / 看见执行回了 不是已经离开提议超时的关键路径，也不是已经不挡 q 的提议钟。**  
   官方写：在 `PrepareProposal` 时整块执行，站在 CometBFT 的**关键路径**上。看见立刻执行了，不是已经离开这条路径。看见执行回了，不是已经不挡提议钟。看见候选写进内存，不是已经交差。
2. **看见填了 TimeoutPropose / 看见同步期 不是已经装得下这次 Prepare 执行，也不是 q 的提议钟已经不会响。**  
   官方写：若 *p* 的应用在 Prepare 里立刻整块执行，且 *p*、*q* 同在一轮、网络处在同步期，则 *q* 的 `TimeoutPropose` **必须**装得下这次执行，让 *q* 的提议钟**不响**。钟一响，*q* 在这一轮 prevote `nil`。看见填了这个值，不是已经装得下。看见同步期，不是钟已经不会响。
3. **看见又开一轮 / 看见 TimeoutPropose 只是初值 不是已经丢了活性，也不是超时已经不再涨。**  
   官方写：违反 Requirement 1 **可能再开一轮**，**不会**因此丢掉活性。`TimeoutPropose` 只是初值；CometBFT 会动态把超时往上调，直到够完成本次 Prepare。看见又开一轮，不是已经停。看见初值，不是已经是最后那一档。

怎样设 TimeoutPropose、默认秒数、怎样写立刻执行是规范里的取值或做法，本页不抄。本地超时不是最终性是不变量 47，本页不抄。

## 官方为什么这样拆

- **立刻整块执行 ≠ 已经离开关键路径：** 官方把 Prepare 里整块执行写成站在提议钟的关键路径上。
- **填了 TimeoutPropose ≠ 已经装得下：** 官方把同步期里 *q* 的初值必须装得下 *p* 这次执行，和「看见填了」分开。
- **又开一轮 ≠ 已经丢了活性：** 官方把再开一轮和丢掉活性分开；初值会涨，不是已经停。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻整块执行 | 不是已经离开关键路径 | 不是四门已经结算（33） |
| 填了 TimeoutPropose | 不是已经装得下 | 不是本地超时已经是最终性（47） |
| 又开一轮 | 不是已经丢了活性 | 不是候选已经是 ExecuteTxState（311）；不是应用 delay 已经是槽位（52） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「立刻执行就已经来得及、超时已经够、再开一轮就已经停」，必须分开立刻整块执行是不是已经离开关键路径、填了 TimeoutPropose 是不是已经装得下、又开一轮是不是已经丢了活性。可以跳过「看见立刻执行了就已经离开关键路径」。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。 327 preparetimeout vs liveness bundled unbundling 完成（737 + 738 + 739）。

## 本页不抄

- 怎样设 TimeoutPropose、默认秒数、怎样写立刻执行。
- 四门已经结算。那是不变量 33。
- 本地超时已经是最终性。那是不变量 47。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 应用 delay 已经是槽位。那是不变量 52。
