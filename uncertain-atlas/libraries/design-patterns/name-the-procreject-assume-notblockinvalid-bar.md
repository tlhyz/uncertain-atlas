# 模式：把 ProcessProposal REJECT consensus assumes not valid not block invalid 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[ProcessProposal REJECT assumes not valid not block invalid ≠ bundled](../../tracks/implementation/worked-example-procreject-assume-notblockinvalid-vs-bundled.md)。

## 三个名字

1. **consensus assumes not valid not block invalid 不是 Process REJECT consensus assume bundled：** 看见 assumes not valid 不是已经当成块非法，不是 455 bundled interchangeable / 34 block invalid interchangeable / 533 valid/invalid interchangeable。
2. **assumes not valid not permanently blacklisted 不是 block invalid：** 看见假设不合法不是已经永久标成非法块，不是 455 bundled interchangeable / 430 block invalid interchangeable / 376 ProposalStatus interchangeable。
3. **Process REJECT assumes not valid not ProposalStatus REJECT 不是 sends Prevote nil：** 看见 Process REJECT assumes not valid 不是 ProposalStatus REJECT 会发 Prevote nil，不是 455 bundled interchangeable / 376 sends Prevote nil interchangeable / 539 VerifyStatus REJECT interchangeable。

## 为什么要分开叫

官方把 ProcessProposal REJECT consensus assumes not valid not block invalid 写成三个名字。把它们叫成一个「看见 Process 回了 REJECT 就已经当成块非法」，会把 assumes not valid、永久拉黑、ProposalStatus REJECT 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT consensus assumes not valid not block invalid 正式三事，先数清问的是 consensus assumes not valid 是不是 block invalid、assumes not valid 是不是 permanently blacklisted、Process REJECT assumes not valid 是不是 ProposalStatus REJECT / 376 sends Prevote nil，再决定要不要同一次发布。
