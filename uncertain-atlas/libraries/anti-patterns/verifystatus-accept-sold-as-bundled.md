# 反模式：把 VerifyStatus ACCEPT accepts vote 正式三事卖成 VerifyStatus bundled / 已经当成块非法 / 已经 correct process must Accept

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[VerifyStatus ACCEPT ≠ bundled](../../tracks/implementation/worked-example-verifystatus-accept-vs-bundled.md)。

## 卖法

- 「看见 VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票 / 看见回了 ACCEPT 就已经当成块非法 interchangeable / 已经 VerifyStatus bundled interchangeable。」
- 「看见会收下这张票 就已经 correct process must Accept interchangeable / 已经 Requirement 6 已经测过 interchangeable。」
- 「看见 VerifyStatus ACCEPT 就已经 ProposalStatus ACCEPT interchangeable / 已经会发 Prevote interchangeable。」

## 为什么错

官方把 ACCEPT accepts vote not block invalid、ACCEPT not Req 6 must Accept、VerifyStatus ACCEPT not ProposalStatus ACCEPT 写成三件独立的实现事。把它们卖成 VerifyStatus bundled、已经当成块非法、已经 correct process must Accept，会把 block invalid、Req 6 must Accept、ProposalStatus ACCEPT 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus ACCEPT accepts vote 正式三事，必须分开 ACCEPT accepts vote not block invalid、ACCEPT not Req 6 must Accept、VerifyStatus ACCEPT not ProposalStatus ACCEPT 三个名字，不要把它们卖成 VerifyStatus bundled / 已经当成块非法 / 已经 correct process must Accept。

## 和相邻反模式

- [verifystatus-sold-as-vote](verifystatus-sold-as-vote.md) 是 434 bundled 三事专用；本页是 ACCEPT accepts vote 单句边界。
- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus ACCEPT 会发 Prevote，不是本页 VerifyStatus ACCEPT not ProposalStatus ACCEPT 边界。
- [verifyaccept-shouldaccept-sold-as-bundled](verifyaccept-shouldaccept-sold-as-bundled.md) 是 Verify SHOULD always set ACCEPT 专用，不是本页 VerifyStatus ACCEPT 边界。
