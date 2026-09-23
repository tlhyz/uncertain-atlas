# 反模式：把不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量）说成已经自己验过 / 已经 Accept / 已经过了 Req 6

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[不对本进程自己发出的 Precommit 调用 not already self-verified ≠ bundled（353）](../../tracks/implementation/worked-example-empty-notlocal-vs-bundled.md)。

## 卖法

把 `VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用 / 不调本地票 / 是本地票 写成已经自己验过 interchangeable / 已经 self-verified interchangeable / 已经自己验过交差 interchangeable / 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable；把是自己签的 / 本地签的 Precommit 写成已经 Accept interchangeable / 已经 accept interchangeable / 已经 Accept 交差 interchangeable；把跳过本地 / 不调本地 / 本地票被跳过 写成已经过了 Req 6 interchangeable / 已经 req6-done interchangeable / 已经 Req 6 交差 interchangeable，或已经和 353 verifywhen bundled / verifywhen-sold-as-skipped interchangeable / 813 empty-notlocal interchangeable。

## 为什么错

官方把不调本地票、不是已经 Accept、不是已经过了 Req 6 写成三件独立的实现事。把它们卖成 already self-verified interchangeable / already accept interchangeable / already req6-done interchangeable，会把 not already self-verified、not already accept、not already req6-done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量），必须分开 not already self-verified、not already accept、not already req6-done 三件事，不要和 353 / 34 / 348 / 812 / 814 糊成一句。

## 和相邻反模式

- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是 Verify 何时调用 bundled 全段，不是本页不调本地票 item 2 单句边界。
- [empty-notskip-sold-as-bundled](empty-notskip-sold-as-bundled.md) 是空扩展仍会调 Verify not already skip-verify（353 item 1），不是本页 not already self-verified 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept（348），不是本页 not already accept 边界。
