# 反模式：把 VerifyVoteExtension When late-arriving MAY add without Verify 正式三事卖成迟到扩展 bundled / 已经 Verify 过 / 已经又叫了 Verify

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[late-arriving MAY add without Verify ≠ bundled](../../tracks/implementation/worked-example-verifywhen-latemay-vs-bundled.md)。

## 卖法

- 「看见 last_commit 里有扩展 就已经 Verify 过 interchangeable / 已经 Accept interchangeable。」
- 「看见写进 ExtendedCommitInfo 就已经又叫了 Verify interchangeable / 已经是引擎会再 Verify interchangeable。」
- 「看见 MAY add 就已经 Verify When 正式流程 interchangeable / 已经 step 2 call interchangeable。」

## 为什么错

官方把 MAY add without Verify、round 0 h-1 CommitRound 前提、without calling VerifyVoteExtension 写成三件独立的实现事。把它们卖成迟到扩展 bundled、已经 Verify 过、已经又叫了 Verify，会把 MAY 路径、前提、不调 Verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When late-arriving MAY add without Verify 正式三事，必须分开 MAY add without Verify、round 0 h-1 CommitRound、without calling VerifyVoteExtension 三个名字，不要把它们卖成迟到扩展 bundled / 已经 Verify 过 / 已经又叫了 Verify。

## 和相邻反模式

- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是 352 bundled 专用；本页是 When late-arriving MAY 单句边界。
- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是 Verify When 正式流程 bundled，不是本页 MAY 不调 Verify 单句边界。
- [verifywhen-call-sold-as-bundled](verifywhen-call-sold-as-bundled.md) 是正常 When step 2 call，不是本页迟到 MAY 不调 Verify 单句边界。
