# 反模式：把 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量）说成已经丢了安全性 / 已经有引擎补丁 / 已经必须拒坏扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[活性会被伤 not already lost-safety ≠ bundled（341）](../../tracks/implementation/worked-example-verify-notlostsafety-vs-bundled.md)。

## 卖法

把活性会被伤 / Verify 里有非确定 bug / 打中的进程无法守 Req 7 或 8 写成已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable / 341 verifydet bundled interchangeable / 340 processdet interchangeable / verifydet-sold-as-extend interchangeable；把没有现成解法 / 实现 ExtendVote 和 VerifyVoteExtension 必须非常小心 / 没有协议层补丁 写成已经有引擎补丁 interchangeable / 已经 has-patch interchangeable；把 SHOULD Accept / 通则是一律 Accept / 建议一律 Accept 写成已经必须拒坏扩展 interchangeable / 已经 must-reject interchangeable，或已经和 341 verifydet bundled / verifydet-sold-as-extend interchangeable / 778 verify-notlostsafety interchangeable。

## 为什么错

官方把活性会被伤单句、already lost-safety、already has-patch、already must-reject 写成三件独立的实现事。把它们卖成 already lost-safety interchangeable / already has-patch interchangeable / already must-reject interchangeable，会把 not already lost-safety、not already has-patch、not already must-reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量），必须分开 not already lost-safety、not already has-patch、not already must-reject 三件事，不要和 341 / 338 / 34 / 340 / 776 / 777 糊成一句。

## 和相邻反模式

- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 VerifyVoteExtension 确定性 bundled 全段，不是本页活性会被伤 item 3 单句边界。
- [verify-notlikeextend-sold-as-bundled](verify-notlikeextend-sold-as-bundled.md) 是必须确定 ≠ 已经可以像 ExtendVote 那样（341 item 1），不是本页活性会被伤 ≠ 已经丢了安全性 边界。
- [verify-nothonestonly-sold-as-bundled](verify-nothonestonly-sold-as-bundled.md) 是两边同判 ≠ 已经只对诚实扩展（341 item 2），不是本页 SHOULD Accept ≠ 已经必须拒坏扩展 边界。
- [process-notlostsafety-sold-as-bundled](process-notlostsafety-sold-as-bundled.md) 是 Process 非确定 bug 没有现成解法（340 item 3），不是本页 Verify 活性会被伤边界。
