# 反模式：把 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事卖成 Verify When 正式流程 / 写进 last_commit / 已经 Verify 过迟到扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ACCEPT keep or REJECT discard ≠ bundled](../../tracks/implementation/worked-example-verifywhen-keepdiscard-vs-bundled.md)。

## 卖法

- 「看见 ACCEPT 就已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable。」
- 「看见 populate ExtendedCommitInfo 就已经进了块 interchangeable / 已经 Prepare 带了扩展 interchangeable。」
- 「看见 REJECT 丢掉 Precommit 就已经 step 1 discard interchangeable / 已经当成块非法 interchangeable。」

## 为什么错

官方把 ACCEPT keep、h+1 Prepare populate、REJECT discard 写成三件独立的实现事。把它们卖成 Verify When 正式流程、写进 last_commit、已经 Verify 过迟到扩展，会把 keep、用途、discard 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事，必须分开 ACCEPT keep、populate ExtendedCommitInfo in h+1 Prepare、REJECT discard 三个名字，不要把它们卖成 Verify When 正式流程 / 写进 last_commit / 已经 Verify 过迟到扩展。

## 和相邻反模式

- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是 Verify When 正式流程三事 bundled，不是本页 step 4 keep/discard 单句专用边界。
- [verifywhen-status-sold-as-bundled](verifywhen-status-sold-as-bundled.md) 是 step 3 return 单句，不是本页 step 4 keep/discard 单句边界。
- [verifywhen-discard-sold-as-bundled](verifywhen-discard-sold-as-bundled.md) 是 step 1 discard 单句，不是本页 REJECT discard 单句边界。
