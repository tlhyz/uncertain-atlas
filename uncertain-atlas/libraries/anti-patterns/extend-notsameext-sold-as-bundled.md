# 反模式：把 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量）说成已经是同一份扩展 / 已经必须同一份 / 已经和 Verify 同一把尺

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[同一块 not already same-extension ≠ bundled（338）](../../tracks/implementation/worked-example-extend-notsameext-vs-bundled.md)。

## 卖法

把同一块 / *w^r_p = w^r_q* / 同一份块 写成已经是同一份扩展 interchangeable / 已经 same-extension interchangeable / 已经同一份扩展交差 interchangeable / 338 preparenondet bundled interchangeable / 34 vote-extension interchangeable / preparenondet-sold-as-deterministic interchangeable；把 ExtendVote 没有确定性要求 / ExtendVote 也可以不确定 / 没有这道要求 写成已经必须同一份 interchangeable / 已经 must-same-e interchangeable；把能签扩展 / 扩展可以依赖其它值或操作 / 能签 写成已经和 VerifyVoteExtension 必须确定同一把尺 interchangeable / 已经 same-as-verify interchangeable，或已经和 338 preparenondet bundled / preparenondet-sold-as-deterministic interchangeable / 769 extend-notsameext interchangeable。

## 为什么错

官方把同一块单句、already same-extension、already must-same-e、already same-as-verify 写成三件独立的实现事。把它们卖成 already same-extension interchangeable / already must-same-e interchangeable / already same-as-verify interchangeable，会把 not already same-extension、not already must-same-e、not already same-as-verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量），必须分开 not already same-extension、not already must-same-e、not already same-as-verify 三件事，不要和 338 / 33 / 327 / 34 / 767 / 768 糊成一句。

## 和相邻反模式

- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare nondet bundled 全段，不是本页同一块 item 3 单句边界。
- [prepare-notmustdet-sold-as-bundled](prepare-notmustdet-sold-as-bundled.md) 是 Prepare 没有确定性要求 ≠ 已经必须确定（338 item 1），不是本页同一块 ≠ 已经是同一份扩展 边界。
- [prepare-notrawsame-sold-as-bundled](prepare-notrawsame-sold-as-bundled.md) 是两边 raw 一样 ≠ 已经是同一份提案（338 item 2），不是本页没有确定性要求 ≠ 已经必须同一份 边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交（34），不是本页能签扩展 ≠ 已经和 Verify 同一把尺 边界。
