# 反模式：把下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量）说成已经又叫了 Verify / 已经必须再叫 / 已经是本轮那次 Verify

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[下一高度 round 0 写进 ExtendedCommitInfo not already called-again ≠ bundled（352）](../../tracks/implementation/worked-example-lateext-notrecall-vs-bundled.md)。

## 卖法

把下一高度 round 0 收到上一高度 `CommitRound` 的 Precommit / 写进 `ExtendedCommitInfo` / 写进去了 写成已经又叫了 Verify interchangeable / 已经 called-again interchangeable / 已经又 Verify 交差 interchangeable / 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable；把规范允许 / MAY 写进 / 可以不叫 写成已经必须再叫 interchangeable / 已经 must-recall interchangeable / 已经必须再 Verify 交差 interchangeable；把是上一高度 / *h-1* / 上一高度 `CommitRound` *r* 写成已经是本轮那次 Verify interchangeable / 已经 this-round-verify interchangeable / 已经本轮 Verify 交差 interchangeable，或已经和 352 lateext bundled / lateext-sold-as-verified interchangeable / 811 lateext-notrecall interchangeable。

## 为什么错

官方把写进去了、不是已经必须再叫、不是已经是本轮那次 Verify 写成三件独立的实现事。把它们卖成 already called-again interchangeable / already must-recall interchangeable / already this-round-verify interchangeable，会把 not already called-again、not already must-recall、not already this-round-verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量），必须分开 not already called-again、not already must-recall、not already this-round-verify 三件事，不要和 352 / 34 / 348 / 809 / 810 糊成一句。

## 和相邻反模式

- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是迟到扩展 bundled 全段，不是本页写进去了 item 3 单句边界。
- [lateext-notreverify-sold-as-bundled](lateext-notreverify-sold-as-bundled.md) 是建议按 Verify 同款逻辑再看一遍 not already engine-reverify（352 item 2），不是本页 not already called-again 边界。
- [lateext-notverified-sold-as-bundled](lateext-notverified-sold-as-bundled.md) 是 +2/3 之后才进来的扩展写进了 commit info not already verified（352 item 1），不是本页 not already this-round-verify 边界。
