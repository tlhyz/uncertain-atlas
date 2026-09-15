# 反模式：把 VerifyVoteExtension Response status valid/invalid 正式三事卖成 Verify 回包栏 bundled / 已经当成块非法 / 已经不能收这张 Precommit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[status valid/invalid ≠ bundled](../../tracks/implementation/worked-example-verifyrespstatus-validinvalid-vs-bundled.md)。

## 卖法

- 「看见 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 就已经 Verify 回包栏 bundled interchangeable / 已经当成块非法 interchangeable。」
- 「看见 REJECT 时共识拒整张票 就已经 Process prevote nil interchangeable / 已经验签拒收整张 Precommit 就已经是块非法 interchangeable。」
- 「看见 REJECT 就已经不能收这张 Precommit interchangeable / 已经 Verify When REJECT discard interchangeable。」

## 为什么错

官方把 status valid/invalid、REJECT rejects whole vote not block invalid、REJECT not can't receive precommit 写成三件独立的实现事。把它们卖成 Verify 回包栏 bundled、已经当成块非法、已经不能收这张 Precommit，会把 status 语义、rejects whole vote、can't receive 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Response status valid/invalid 正式三事，必须分开 status valid/invalid、REJECT rejects whole vote not block invalid、REJECT not can't receive precommit 三个名字，不要把它们卖成 Verify 回包栏 bundled / 已经当成块非法 / 已经不能收这张 Precommit。

## 和相邻反模式

- [verifyrespstatus-sold-as-verifystatus](verifyrespstatus-sold-as-verifystatus.md) 是 433 bundled 三事专用；本页是 status valid/invalid 单句边界。
- [verifystatus-sold-as-vote](verifystatus-sold-as-vote.md) 是验签拒收整张 Precommit 块非法专用，不是本页 Response status 语义边界。
- [verifywhen-discard-sold-as-bundled](verifywhen-discard-sold-as-bundled.md) 是 Verify When REJECT discard 专用，不是本页 Response status 边界。
