# 反模式：把 VerifyVoteExtension When call VerifyVoteExtension 正式三事卖成 Verify When 正式流程 / 已经验过扩展 / 已经 Accept

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[call VerifyVoteExtension ≠ bundled](../../tracks/implementation/worked-example-verifywhen-call-vs-bundled.md)。

## 卖法

- 「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable / 已经 Accept interchangeable。」
- 「看见 CometBFT 会叫 就已经 Verify When 正式流程 interchangeable / 已经写进 last_commit interchangeable。」
- 「看见 step 2 就已经 Application returns ACCEPT/REJECT interchangeable / 已经 REJECT 丢掉 Precommit interchangeable。」

## 为什么错

官方把 calls VerifyVoteExtension、received from q≠p、step 2 before status return 写成三件独立的实现事。把它们卖成 Verify When 正式流程、已经验过扩展、已经 Accept，会把 call、收到侧前提、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事，必须分开 calls VerifyVoteExtension、received from q≠p、step 2 before status return 三个名字，不要把它们卖成 Verify When 正式流程 / 已经验过扩展 / 已经 Accept。

## 和相邻反模式

- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是 Verify When 正式流程三事 bundled，不是本页 step 2 call 单句专用边界。
- [verifywhen-discard-sold-as-bundled](verifywhen-discard-sold-as-bundled.md) 是 step 1 discard 单句，不是本页 step 2 call 单句边界。
- [verifyrespstatus-sold-as-verifystatus](verifyrespstatus-sold-as-verifystatus.md) 是 433 专用；本页是 When step 2 call 在 status return 之前单句边界。
