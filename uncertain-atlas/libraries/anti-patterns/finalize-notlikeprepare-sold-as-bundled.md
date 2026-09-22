# 反模式：把 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（342 余量）说成已经可以像 Prepare 那样 / 已经和 Prepare nondet 同一句 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[必须确定 not already like-prepare ≠ bundled（342）](../../tracks/implementation/worked-example-finalize-notlikeprepare-vs-bundled.md)。

## 卖法

把 FinalizeBlock 算出的状态必须只依赖 *s_{h-1}* 和 *v* / 必须确定 / 造出 *s_h* 写成已经可以像 Prepare 那样依赖其它值 interchangeable / 已经 like-prepare interchangeable / 已经可以依赖其它值交差 interchangeable / 342 finalizedet bundled interchangeable / 338 preparenondet interchangeable / finalizedet-sold-as-prepare interchangeable；把只依赖上一份状态和决定块 / 只依赖 *s_{h-1}* 和 *v* / 不能另依赖其它值 写成已经和 Prepare 没有确定性要求同一句 interchangeable / 已经 same-as-nondet interchangeable；把 Finalize 回了 / FinalizeBlock 回了 / 造出了 *s_h* 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 342 finalizedet bundled / finalizedet-sold-as-prepare interchangeable / 779 finalize-notlikeprepare interchangeable。

## 为什么错

官方把必须确定单句、already like-prepare、already same-as-nondet、already settled 写成三件独立的实现事。把它们卖成 already like-prepare interchangeable / already same-as-nondet interchangeable / already settled interchangeable，会把 not already like-prepare、not already same-as-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（342 余量），必须分开 not already like-prepare、not already same-as-nondet、not already settled 三件事，不要和 342 / 338 / 316 / 340 / 780 / 781 糊成一句。

## 和相邻反模式

- [finalize-notprinted-sold-as-bundled](finalize-notprinted-sold-as-bundled.md) 是结果必须确定 ≠ 已经印进本头（342 item 2），不是本页必须确定 item 1 单句边界。
- [finalizedet-sold-as-prepare](finalizedet-sold-as-prepare.md) 是 FinalizeBlock 确定性 bundled 全段，不是本页必须确定 item 1 单句边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求 bundled（338），不是本页必须确定 ≠ 已经可以像 Prepare 那样 边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表已经同一顺序（316），不是本页 Finalize 回了 ≠ 已经交差 边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 ProcessProposal 确定性（340），不是本页只依赖上一份状态和决定块边界。
