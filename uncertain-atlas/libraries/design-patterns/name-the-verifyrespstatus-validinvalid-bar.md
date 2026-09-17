# 模式：把 VerifyVoteExtension Response status valid/invalid 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response status 句。  
**例**：[status valid/invalid ≠ bundled](../../tracks/implementation/worked-example-verifyrespstatus-validinvalid-vs-bundled.md)。

## 三个名字

1. **status is valid/invalid judgment 不是 block invalid：** 看见 application considers valid or invalid，不是 433 bundled interchangeable / 34 whole precommit invalid interchangeable / 516 When return interchangeable。
2. **REJECT rejects whole vote not block invalid 不是 Process prevote nil：** 看见 rejects whole vote，不是 433 bundled interchangeable / 537 prevote nil interchangeable / 34 block invalid interchangeable。
3. **REJECT not can't receive precommit 不是 When REJECT discard：** 看见 not can't receive，不是 433 bundled interchangeable / 517 When REJECT discard interchangeable / 529 can't Reject interchangeable。

## 为什么要分开叫

官方把 status valid/invalid、REJECT rejects whole vote not block invalid、REJECT not can't receive precommit、Verify 回包栏 bundled（433）、status must exclusively depend（540 余量）、Verify When REJECT discard（517）写成三个名字。把它们叫成一个「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法 interchangeable」，会把 status 语义、rejects whole vote、cannot receive 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Response status valid/invalid 正式三事，先数清问的是 status valid/invalid 是不是 block invalid、REJECT rejects whole vote 是不是 Process prevote nil / 34 block invalid、REJECT 是不是 can't receive precommit，再决定要不要同一次发布。
