# 模式：把 VerifyStatus ACCEPT accepts vote 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**例**：[VerifyStatus ACCEPT ≠ bundled](../../tracks/implementation/worked-example-verifystatus-accept-vs-bundled.md)。

## 三个名字

1. **ACCEPT accepts vote not block invalid 不是 VerifyStatus bundled：** 看见回了 ACCEPT 不是已经当成块非法，不是 434 bundled interchangeable / 34 whole precommit invalid interchangeable / 535 valid/invalid interchangeable。
2. **ACCEPT not Req 6 must Accept 不是 correct process must Accept：** 看见会收下这张票不是已经 correct process must Accept，不是 434 bundled interchangeable / 348 Req 6 must Accept interchangeable / 527 SHOULD always set ACCEPT interchangeable。
3. **VerifyStatus ACCEPT not ProposalStatus ACCEPT 不是 sends Prevote：** 看见 VerifyStatus ACCEPT 不是 ProposalStatus ACCEPT 会发 Prevote，不是 434 bundled interchangeable / 376 sends Prevote interchangeable / 430 Process ACCEPT interchangeable。

## 为什么要分开叫

官方把 ACCEPT accepts vote not block invalid、ACCEPT not Req 6 must Accept、VerifyStatus ACCEPT not ProposalStatus ACCEPT、VerifyStatus bundled（434）、ProposalStatus ACCEPT（376）、Req 6 must Accept（348）写成三个名字。把它们叫成一个「看见回了 VerifyStatus ACCEPT 就已经当成块非法 interchangeable」，会把 block invalid、correct process must Accept、ProposalStatus ACCEPT 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus ACCEPT accepts vote 正式三事，先数清问的是 ACCEPT accepts vote 是不是 block invalid、ACCEPT 是不是 Req 6 must Accept / 348 correct process must Accept、VerifyStatus ACCEPT 是不是 ProposalStatus ACCEPT / 376 sends Prevote，再决定要不要同一次发布。
