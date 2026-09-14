# 模式：把 VerifyStatus UNKNOWN always wrong 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**例**：[VerifyStatus UNKNOWN ≠ bundled](../../tracks/implementation/worked-example-verifystatus-unknown-vs-bundled.md)。

## 三个名字

1. **UNKNOWN always wrong not already verified 不是 VerifyStatus bundled：** 看见回了 UNKNOWN 不是已经验过扩展，不是 434 bundled interchangeable / 535 valid/invalid interchangeable / 516 When return interchangeable。
2. **UNKNOWN crash not extension enabled 不是 extension enabled：** 看见崩了不是已经扩展启用，不是 434 bundled interchangeable / 437 precommit nil won't call ExtendVote interchangeable / 376 ProposalStatus UNKNOWN interchangeable。
3. **VerifyStatus UNKNOWN not ProposalStatus UNKNOWN 不是 four gates settled：** 看见 VerifyStatus UNKNOWN 不是 ProposalStatus UNKNOWN，不是 434 bundled interchangeable / 376 four gates settled interchangeable / 433 Response bundled interchangeable。

## 为什么要分开叫

官方把 UNKNOWN always wrong、UNKNOWN crash not extension enabled、VerifyStatus UNKNOWN not ProposalStatus UNKNOWN、VerifyStatus bundled（434）、ProposalStatus UNKNOWN（376）、status valid/invalid（535）写成三个名字。把它们叫成一个「看见回了 VerifyStatus UNKNOWN 就已经验过扩展 interchangeable」，会把 already verified、extension enabled、ProposalStatus UNKNOWN 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus UNKNOWN always wrong 正式三事，先数清问的是 UNKNOWN always wrong 是不是 already verified、UNKNOWN crash 是不是 extension enabled、VerifyStatus UNKNOWN 是不是 ProposalStatus UNKNOWN / 376 four gates settled，再决定要不要同一次发布。
