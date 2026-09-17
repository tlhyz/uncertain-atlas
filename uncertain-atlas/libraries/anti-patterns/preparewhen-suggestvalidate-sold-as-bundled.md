# 反模式：把 PrepareProposal When suggested validate like Verify 正式三事卖成迟到扩展 bundled / 引擎会再 Verify / 已经 Accept

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[suggested validate like Verify ≠ bundled](../../tracks/implementation/worked-example-preparewhen-suggestvalidate-vs-bundled.md)。

## 卖法

- 「看见建议按 Verify 同款逻辑再看一遍 就已经是引擎会再 Verify interchangeable / 已经 CometBFT 会叫 interchangeable。」
- 「看见 it is suggested 就已经 Accept interchangeable / 已经 Req 6 已经测过 interchangeable。」
- 「看见 same manner as VerifyVoteExtension 就已经 step 2 call bundled interchangeable / 已经 Verify 过 interchangeable。」

## 为什么错

官方把 it is suggested、same manner as VerifyVoteExtension、not CometBFT calling VerifyVoteExtension again 写成三件独立的实现事。把它们卖成迟到扩展 bundled、引擎会再 Verify、已经 Accept，会把 suggested、应用自验、引擎再 call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When suggested validate like Verify 正式三事，必须分开 it is suggested、same manner as VerifyVoteExtension、not engine re-Verify 三个名字，不要把它们卖成迟到扩展 bundled / 引擎会再 Verify / 已经 Accept。

## 和相邻反模式

- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是 352 bundled 专用；本页是 PrepareProposal When suggested validate 单句边界。
- [preparewhen-lateext-unverified-sold-as-bundled](preparewhen-lateext-unverified-sold-as-bundled.md) 是 +2/3 not verified 三事 bundled，不是本页 suggested validate 单句边界。
- [verifywhen-call-sold-as-bundled](verifywhen-call-sold-as-bundled.md) 是 Verify When step 2 call，不是本页 Prepare 侧 suggested 自验边界。
