# 反模式：把 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量）说成已经可以像 Prepare 那样 / 已经和 Prepare nondet 同一句 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[必须确定 not already like-prepare ≠ bundled（340）](../../tracks/implementation/worked-example-process-notlikeprepare-vs-bundled.md)。

## 卖法

把 ProcessProposal 必须只依赖本次请求和 *s_{h-1}* / 必须确定 / 是确定函数 写成已经可以像 Prepare 那样依赖其它值 interchangeable / 已经 like-prepare interchangeable / 已经可以依赖其它值交差 interchangeable / 340 processdet bundled interchangeable / 338 preparenondet interchangeable / processdet-sold-as-prepare interchangeable；把只依赖请求和上一份状态 / 只依赖 *u* 和 *s_{h-1}* / 不能另依赖其它值 写成已经和 Prepare 没有确定性要求同一句 interchangeable / 已经 same-as-nondet interchangeable；把 Process 回了 / ProcessProposal 回了 / Accept 或 Reject 回来了 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 340 processdet bundled / processdet-sold-as-prepare interchangeable / 773 process-notlikeprepare interchangeable。

## 为什么错

官方把必须确定单句、already like-prepare、already same-as-nondet、already settled 写成三件独立的实现事。把它们卖成 already like-prepare interchangeable / already same-as-nondet interchangeable / already settled interchangeable，会把 not already like-prepare、not already same-as-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量），必须分开 not already like-prepare、not already same-as-nondet、not already settled 三件事，不要和 340 / 338 / 33 / 327 / 774 / 775 糊成一句。

## 和相邻反模式

- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 ProcessProposal 确定性 bundled 全段，不是本页必须确定 item 1 单句边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求 bundled（338），不是本页必须确定 ≠ 已经可以像 Prepare 那样 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 Process 回了 ≠ 已经交差 边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径（327），不是本页只依赖请求边界。
