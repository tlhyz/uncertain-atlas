# 反模式：把 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量）说成已经可以像 ExtendVote 那样 / 已经和 ExtendVote nondet 同一句 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[必须确定 not already like-extend ≠ bundled（341）](../../tracks/implementation/worked-example-verify-notlikeextend-vs-bundled.md)。

## 卖法

把 VerifyVoteExtension 必须只依赖扩展、这块和 *s_{h-1}* / 必须确定 / 是确定函数 写成已经可以像 ExtendVote 那样依赖其它值 interchangeable / 已经 like-extend interchangeable / 已经可以依赖其它值交差 interchangeable / 341 verifydet bundled interchangeable / 338 preparenondet interchangeable / verifydet-sold-as-extend interchangeable；把只依赖扩展、这块和上一份状态 / 只依赖 *e*、*w* 和 *s_{h-1}* / 不能另依赖其它值 写成已经和 ExtendVote 没有确定性要求同一句 interchangeable / 已经 same-as-nondet interchangeable；把 Verify 回了 / VerifyVoteExtension 回了 / Accept 或 Reject 回来了 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 341 verifydet bundled / verifydet-sold-as-extend interchangeable / 776 verify-notlikeextend interchangeable。

## 为什么错

官方把必须确定单句、already like-extend、already same-as-nondet、already settled 写成三件独立的实现事。把它们卖成 already like-extend interchangeable / already same-as-nondet interchangeable / already settled interchangeable，会把 not already like-extend、not already same-as-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量），必须分开 not already like-extend、not already same-as-nondet、not already settled 三件事，不要和 341 / 338 / 34 / 340 / 777 / 778 糊成一句。

## 和相邻反模式

- [verify-notlostsafety-sold-as-bundled](verify-notlostsafety-sold-as-bundled.md) 是活性会被伤 ≠ 已经丢了安全性（341 item 3），不是本页必须确定 item 1 单句边界。
- [verify-nothonestonly-sold-as-bundled](verify-nothonestonly-sold-as-bundled.md) 是两边同判 ≠ 已经只对诚实扩展（341 item 2），不是本页必须确定 item 1 单句边界。
- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 VerifyVoteExtension 确定性 bundled 全段，不是本页必须确定 item 1 单句边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare/ExtendVote 没有确定性要求 bundled（338），不是本页必须确定 ≠ 已经可以像 ExtendVote 那样 边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交（34），不是本页 Verify 回了 ≠ 已经交差 边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 ProcessProposal 确定性（340），不是本页只依赖扩展边界。
