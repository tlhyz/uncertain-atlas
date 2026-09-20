# 反模式：把又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量）说成已经丢了活性 / 已经超时不再涨 / 已经是最后那一档

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[又开一轮 not already liveness-lost ≠ bundled（327）](../../tracks/implementation/worked-example-preparetimeout-notlivenesslost-vs-bundled.md)。

## 卖法

把又开一轮 / 再开一轮 / 违反后可能再开一轮 写成已经丢了活性 interchangeable / 已经 liveness-lost interchangeable / 已经活性丢掉交差 interchangeable / 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable；把 TimeoutPropose 只是初值 / 超时还会涨 / 动态往上调 写成已经超时不再涨 interchangeable / 已经 timeout-frozen interchangeable；把看见初值 / 不是最后那一档 / 还会再调 写成已经是最后那一档 interchangeable / 已经 final-tier interchangeable，或已经和 327 preparetimeout bundled / preparetimeout-sold-as-liveness interchangeable / 739 preparetimeout-notlivenesslost interchangeable。

## 为什么错

官方把又开一轮单句、already liveness-lost、already timeout-frozen、already final-tier 写成三件独立的实现事。把它们卖成 already liveness-lost interchangeable / already timeout-frozen interchangeable / already final-tier interchangeable，会把 not already liveness-lost、not already timeout-frozen、not already final-tier 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量），必须分开 not already liveness-lost、not already timeout-frozen、not already final-tier 三件事，不要和 327 / 33 / 47 / 416 / 52 / 737 / 738 糊成一句。

## 和相邻反模式

- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是 PrepareProposal 及时性 bundled 全段，不是本页又开一轮 item 3 单句边界。
- [preparetimeout-notfit-sold-as-bundled](preparetimeout-notfit-sold-as-bundled.md) 是装得下 item 2，不是本页又开一轮与丢掉活性边界。
- [preparetimeout-notcriticalpath-sold-as-bundled](preparetimeout-notcriticalpath-sold-as-bundled.md) 是关键路径 item 1，不是本页初值与末档边界。
