# 模式：把 VerifyStatus REJECT rejects whole vote 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**例**：[VerifyStatus REJECT ≠ bundled](../../tracks/implementation/worked-example-verifystatus-reject-vs-bundled.md)。

## 三个名字

1. **REJECT rejects whole vote not Process prevote nil 不是 VerifyStatus bundled：** 看见回了 REJECT 不是已经会发 Prevote nil，不是 434 bundled interchangeable / 430 Process REJECT interchangeable / 533 prevote nil interchangeable。
2. **REJECT rejects whole vote not block invalid 不是 block invalid：** 看见拒掉整张票不是已经当成块非法，不是 434 bundled interchangeable / 34 whole precommit invalid interchangeable / 535 valid/invalid interchangeable。
3. **VerifyStatus REJECT not ProposalStatus REJECT 不是 sends Prevote nil：** 看见 VerifyStatus REJECT 不是 ProposalStatus REJECT 会发 Prevote nil，不是 434 bundled interchangeable / 376 sends Prevote nil interchangeable / 517 When REJECT discard interchangeable。

## 为什么要分开叫

官方把 REJECT rejects whole vote not Process prevote nil、REJECT rejects whole vote not block invalid、VerifyStatus REJECT not ProposalStatus REJECT、VerifyStatus bundled（434）、ProposalStatus REJECT（376）、Process REJECT prevote nil（430/533）写成三个名字。把它们叫成一个「看见回了 VerifyStatus REJECT 就已经会发 Prevote nil interchangeable」，会把 Process prevote nil、block invalid、ProposalStatus REJECT 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus REJECT rejects whole vote 正式三事，先数清问的是 REJECT rejects whole vote 是不是 Process prevote nil、REJECT rejects whole vote 是不是 block invalid / 34 block invalid、VerifyStatus REJECT 是不是 ProposalStatus REJECT / 376 sends Prevote nil，再决定要不要同一次发布。
