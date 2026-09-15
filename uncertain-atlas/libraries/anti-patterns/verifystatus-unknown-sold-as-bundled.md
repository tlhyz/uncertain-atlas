# 反模式：把 VerifyStatus UNKNOWN always wrong 正式三事卖成 VerifyStatus bundled / 已经验过扩展 / 已经扩展启用

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[VerifyStatus UNKNOWN ≠ bundled](../../tracks/implementation/worked-example-verifystatus-unknown-vs-bundled.md)。

## 卖法

- 「看见 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩 / 看见回了 UNKNOWN 就已经验过扩展 interchangeable / 已经 VerifyStatus bundled interchangeable。」
- 「看见崩了 就已经扩展启用 interchangeable / 已经 ExtendVote 已经启用 interchangeable。」
- 「看见 VerifyStatus UNKNOWN 就已经 ProposalStatus UNKNOWN interchangeable / 已经四门已经结算 interchangeable。」

## 为什么错

官方把 UNKNOWN always wrong not already verified、UNKNOWN crash not extension enabled、VerifyStatus UNKNOWN not ProposalStatus UNKNOWN 写成三件独立的实现事。把它们卖成 VerifyStatus bundled、已经验过扩展、已经扩展启用，会把 already verified、extension enabled、ProposalStatus UNKNOWN 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus UNKNOWN always wrong 正式三事，必须分开 UNKNOWN always wrong、UNKNOWN crash not extension enabled、VerifyStatus UNKNOWN not ProposalStatus UNKNOWN 三个名字，不要把它们卖成 VerifyStatus bundled / 已经验过扩展 / 已经扩展启用。

## 和相邻反模式

- [verifystatus-sold-as-vote](verifystatus-sold-as-vote.md) 是 434 bundled 三事专用；本页是 UNKNOWN always wrong 单句边界。
- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus ACCEPT 会发 Prevote，不是本页 VerifyStatus UNKNOWN not ProposalStatus UNKNOWN 边界。
- [verifyrespstatus-validinvalid-sold-as-bundled](verifyrespstatus-validinvalid-sold-as-bundled.md) 是 Response status valid/invalid 专用，不是本页 VerifyStatus UNKNOWN 边界。
