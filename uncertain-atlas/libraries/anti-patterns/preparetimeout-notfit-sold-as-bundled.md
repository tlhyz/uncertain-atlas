# 反模式：把填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量）说成已经装得下 / 已经钟不响 / 已经把提议绑死

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了 TimeoutPropose not already fits-execution ≠ bundled（327）](../../tracks/implementation/worked-example-preparetimeout-notfit-vs-bundled.md)。

## 卖法

把填了 TimeoutPropose / 填了这个值 / 有 TimeoutPropose 初值 写成已经装得下这次 Prepare 执行 interchangeable / 已经 fits-execution interchangeable / 已经装得下交差 interchangeable / 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable；把同步期 / *p*、*q* 同在一轮 / 网络处在同步期 写成已经 *q* 的提议钟不会响 interchangeable / 已经 clock-silent interchangeable；把钟一响就 prevote nil / 提议钟挂钩 / 钟响走 nil 写成已经把这一轮提议绑成必成 interchangeable / 已经 propose-bound interchangeable，或已经和 327 preparetimeout bundled / preparetimeout-sold-as-liveness interchangeable / 738 preparetimeout-notfit interchangeable。

## 为什么错

官方把填了 TimeoutPropose 单句、already fits-execution、already clock-silent、already propose-bound 写成三件独立的实现事。把它们卖成 already fits-execution interchangeable / already clock-silent interchangeable / already propose-bound interchangeable，会把 not already fits-execution、not already clock-silent、not already propose-bound 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量），必须分开 not already fits-execution、not already clock-silent、not already propose-bound 三件事，不要和 327 / 33 / 47 / 416 / 737 / 739 糊成一句。

## 和相邻反模式

- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是 PrepareProposal 及时性 bundled 全段，不是本页装得下 item 2 单句边界。
- [preparetimeout-notcriticalpath-sold-as-bundled](preparetimeout-notcriticalpath-sold-as-bundled.md) 是关键路径 item 1，不是本页填了 TimeoutPropose 与装得下边界。
- [preparetimeout-notlivenesslost-sold-as-bundled](preparetimeout-notlivenesslost-sold-as-bundled.md) 是又开一轮丢掉活性（327 item 3），不是本页装得下 item 2 单句边界。
- [proposetimeout-sold-as-process](proposetimeout-sold-as-process.md) 是进了这一轮会先设 ProposeTimeout（416），不是本页钟一响就 prevote nil 边界。
