# 反模式：把 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量）说成已经必须确定 / 已经和 Process 同一把尺 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[没有确定性要求 not already must-deterministic ≠ bundled（338）](../../tracks/implementation/worked-example-prepare-notmustdet-vs-bundled.md)。

## 卖法

把 PrepareProposal 没有确定性要求 / Prepare 不被要求确定 / 没有这道要求 写成已经必须确定 interchangeable / 已经 must-deterministic interchangeable / 已经必须确定交差 interchangeable / 338 preparenondet bundled interchangeable / 33 four gates interchangeable / preparenondet-sold-as-deterministic interchangeable；把可以依赖其它值或操作 / 准备好的提案可以依赖其它值 / 可以不止 raw 和已提交状态 写成已经和 Process / Finalize 同一把尺 interchangeable / 已经 same-as-process interchangeable；把 Prepare 回了 / PrepareProposal 回了 / 准备好的提案回来了 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 338 preparenondet bundled / preparenondet-sold-as-deterministic interchangeable / 767 prepare-notmustdet interchangeable。

## 为什么错

官方把没有确定性要求单句、already must-deterministic、already same-as-process、already settled 写成三件独立的实现事。把它们卖成 already must-deterministic interchangeable / already same-as-process interchangeable / already settled interchangeable，会把 not already must-deterministic、not already same-as-process、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量），必须分开 not already must-deterministic、not already same-as-process、not already settled 三件事，不要和 338 / 33 / 327 / 34 / 768 / 769 糊成一句。

## 和相邻反模式

- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare nondet bundled 全段，不是本页没有确定性要求 item 1 单句边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页没有确定性要求 ≠ 已经必须确定 边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径（327），不是本页可以依赖其它值边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交（34），不是本页 Prepare 回了边界。
