# 反模式：把 ProcessProposal REJECT consensus assumes not valid not block invalid 正式三事卖成 Process REJECT consensus assume bundled / 已经当成块非法 / 已经永久标成非法块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal REJECT assumes not valid not block invalid ≠ bundled](../../tracks/implementation/worked-example-procreject-assume-notblockinvalid-vs-bundled.md)。

## 卖法

- 「看见 `ProcessProposalResponse.status` 是 `REJECT` 时共识假设收到的提案不合法 / 看见 consensus assumes not valid 就已经当成块非法 interchangeable / 已经 Process REJECT consensus assume bundled interchangeable。」
- 「看见 assumes not valid 就已经永久标成非法块 interchangeable / 已经 Process 回包栏 bundled interchangeable / 已经 block invalid interchangeable。」
- 「看见 Process REJECT 就已经 ProposalStatus REJECT 会发 Prevote nil interchangeable / 已经 Verify REJECT whole vote interchangeable。」

## 为什么错

官方把 consensus assumes not valid not block invalid、assumes not valid not permanently blacklisted、Process REJECT assumes not valid not ProposalStatus REJECT 写成三件独立的实现事。把它们卖成 Process REJECT consensus assume bundled、已经当成块非法、已经永久标成非法块，会把 block invalid、永久拉黑、ProposalStatus REJECT 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT consensus assumes not valid not block invalid 正式三事，必须分开 consensus assumes not valid not block invalid、assumes not valid not permanently blacklisted、Process REJECT assumes not valid not ProposalStatus REJECT 三个名字，不要把它们卖成 Process REJECT consensus assume bundled / 已经当成块非法 / 已经永久标成非法块。

## 和相邻反模式

- [procreject-sold-as-invalid](procreject-sold-as-invalid.md) 是 455 bundled 三事专用；本页是 assumes not valid not block invalid 单句边界。
- [procrespstatus-validinvalid-sold-as-bundled](procrespstatus-validinvalid-sold-as-bundled.md) 是 ProcessProposal Response status valid/invalid 专用，不是本页 Usage assumes not valid 边界。
- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus REJECT 会发 Prevote nil，不是本页 Process REJECT assumes not valid not ProposalStatus REJECT 边界。
