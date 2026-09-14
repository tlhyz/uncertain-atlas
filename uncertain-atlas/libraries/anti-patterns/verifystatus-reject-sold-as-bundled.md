# 反模式：把 VerifyStatus REJECT rejects whole vote 正式三事卖成 VerifyStatus bundled / 已经会发 Prevote nil / 已经当成块非法

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[VerifyStatus REJECT ≠ bundled](../../tracks/implementation/worked-example-verifystatus-reject-vs-bundled.md)。

## 卖法

- 「看见 VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票 / 看见回了 REJECT 就已经会发 Prevote nil interchangeable / 已经 VerifyStatus bundled interchangeable。」
- 「看见拒掉整张票 就已经 Process prevote nil interchangeable / 已经 Process REJECT = prevote nil interchangeable。」
- 「看见 VerifyStatus REJECT 就已经当成块非法 interchangeable / 已经验签拒收整张 Precommit 就已经是块非法 interchangeable。」

## 为什么错

官方把 REJECT rejects whole vote not Process prevote nil、REJECT rejects whole vote not block invalid、VerifyStatus REJECT not ProposalStatus REJECT 写成三件独立的实现事。把它们卖成 VerifyStatus bundled、已经会发 Prevote nil、已经当成块非法，会把 Process prevote nil、block invalid、ProposalStatus REJECT 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus REJECT rejects whole vote 正式三事，必须分开 REJECT rejects whole vote not Process prevote nil、REJECT rejects whole vote not block invalid、VerifyStatus REJECT not ProposalStatus REJECT 三个名字，不要把它们卖成 VerifyStatus bundled / 已经会发 Prevote nil / 已经当成块非法。

## 和相邻反模式

- [verifystatus-sold-as-vote](verifystatus-sold-as-vote.md) 是 434 bundled 三事专用；本页是 REJECT rejects whole vote 单句边界。
- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus REJECT 会发 Prevote nil，不是本页 VerifyStatus REJECT not ProposalStatus REJECT 边界。
- [verifyrespstatus-validinvalid-sold-as-bundled](verifyrespstatus-validinvalid-sold-as-bundled.md) 是 VerifyVoteExtensionResponse.status REJECT 专用，不是本页 VerifyStatus REJECT 边界。
