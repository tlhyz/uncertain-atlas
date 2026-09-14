# 反模式：把 VerifyVoteExtension When discard invalid extension 正式三事卖成 Verify When 正式流程 / 跳过 Verify / 已经验过扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[discard invalid extension ≠ bundled](../../tracks/implementation/worked-example-verifywhen-discard-vs-bundled.md)。

## 卖法

- 「看见 Precommit 没有带有效签的扩展就会当非法丢掉 就已经跳过 Verify interchangeable / 已经空扩展仍会调 Verify interchangeable。」
- 「看见 0 长扩展 就已经没有扩展 interchangeable / 已经不会叫 Verify interchangeable。」
- 「看见 step 1 就已经 Verify When 正式流程 interchangeable / 已经验过扩展 interchangeable / 已经写进 last_commit interchangeable。」

## 为什么错

官方把 discards invalid、0-length validity、step 1 before call 写成三件独立的实现事。把它们卖成 Verify When 正式流程、跳过 Verify、已经验过扩展，会把 discard、0 长有效性、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事，必须分开 discards invalid、0-length with valid signature、step 1 before call 三个名字，不要把它们卖成 Verify When 正式流程 / 跳过 Verify / 已经验过扩展。

## 和相邻反模式

- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是 Verify When 正式流程三事，不是本页 step 1 discard 单句专用边界。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是空扩展仍会调 Verify 就已经跳过 Verify，不是本页 When step 1 0 长+有效签仍算有效单句边界。
