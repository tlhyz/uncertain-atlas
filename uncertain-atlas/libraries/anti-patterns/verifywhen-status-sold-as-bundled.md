# 反模式：把 VerifyVoteExtension When return status 正式三事卖成 Verify When 正式流程 / 已经 Accept / 已经写进 last_commit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[return status ≠ bundled](../../tracks/implementation/worked-example-verifywhen-status-vs-bundled.md)。

## 卖法

- 「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable / 已经 REJECT 丢掉 Precommit interchangeable。」
- 「看见 Application returns status 就已经 Verify When 正式流程 interchangeable / 已经验过扩展 interchangeable。」
- 「看见 step 3 就已经 ACCEPT 留给 h+1 Prepare interchangeable / 已经写进 last_commit interchangeable。」

## 为什么错

官方把 Application returns status、step 3 after call、step 3 before keep/discard 写成三件独立的实现事。把它们卖成 Verify When 正式流程、已经 Accept、已经写进 last_commit，会把 return、顺序、后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事，必须分开 Application returns ACCEPT/REJECT、step 3 after call、step 3 before keep/discard 三个名字，不要把它们卖成 Verify When 正式流程 / 已经 Accept / 已经写进 last_commit。

## 和相邻反模式

- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是 Verify When 正式流程三事 bundled，不是本页 step 3 return 单句专用边界。
- [verifywhen-call-sold-as-bundled](verifywhen-call-sold-as-bundled.md) 是 step 2 call 单句，不是本页 step 3 return 单句边界。
- [verifyrespstatus-sold-as-verifystatus](verifyrespstatus-sold-as-verifystatus.md) 是 433 回包栏专用；本页是 When step 3 return 单句边界。
