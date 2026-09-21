# 反模式：把两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量）说成已经只对诚实扩展同判 / 已经可以各判各的 / 已经是 Req 6

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[两边同判 not already honest-only ≠ bundled（341）](../../tracks/implementation/worked-example-verify-nothonestonly-vs-bundled.md)。

## 卖法

把两边对任意扩展同一裁决 / 两边同判 / 所有正确进程对一份扩展反应相同 写成已经只对诚实扩展同一裁决 interchangeable / 已经 honest-only interchangeable / 已经只对诚实 *e_p* 同判交差 interchangeable / 341 verifydet bundled interchangeable / 348 req6-coherence interchangeable / verifydet-sold-as-extend interchangeable；把扩展来自拜占庭 / 扩展坏了 / 扩展可以不诚实 写成已经可以各判各的 interchangeable / 已经 may-diverge interchangeable；把任意扩展 / 对任意扩展 *e* / 不是只对诚实交出的扩展 写成已经是 Req 6 诚实对诚实 interchangeable / 已经 req6-same interchangeable，或已经和 341 verifydet bundled / verifydet-sold-as-extend interchangeable / 777 verify-nothonestonly interchangeable。

## 为什么错

官方把两边同判单句、already honest-only、already may-diverge、already req6-same 写成三件独立的实现事。把它们卖成 already honest-only interchangeable / already may-diverge interchangeable / already req6-same interchangeable，会把 not already honest-only、not already may-diverge、not already req6-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量），必须分开 not already honest-only、not already may-diverge、not already req6-same 三件事，不要和 341 / 338 / 34 / 348 / 776 / 778 糊成一句。

## 和相邻反模式

- [verify-notlostsafety-sold-as-bundled](verify-notlostsafety-sold-as-bundled.md) 是活性会被伤 ≠ 已经丢了安全性（341 item 3），不是本页两边同判 item 2 单句边界。
- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 VerifyVoteExtension 确定性 bundled 全段，不是本页两边同判 item 2 单句边界。
- [verify-notlikeextend-sold-as-bundled](verify-notlikeextend-sold-as-bundled.md) 是必须确定 ≠ 已经可以像 ExtendVote 那样（341 item 1），不是本页两边同判 ≠ 已经只对诚实扩展 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是诚实扩展必须被诚实 Verify Accept（348），不是本页任意扩展 ≠ 已经是 Req 6 边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交（34），不是本页扩展坏了 ≠ 已经可以各判各的 边界。
