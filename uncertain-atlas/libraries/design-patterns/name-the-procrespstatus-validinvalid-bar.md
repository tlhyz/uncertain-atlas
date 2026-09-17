# 模式：把 ProcessProposal Response status valid/invalid 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response status 句。  
**例**：[status valid/invalid ≠ bundled](../../tracks/implementation/worked-example-procrespstatus-validinvalid-vs-bundled.md)。

## 三个名字

1. **status is valid/invalid judgment 不是 block invalid：** 看见 application considers valid or invalid，不是 430 bundled interchangeable / 455 assumes not valid interchangeable / 376 ProposalStatus interchangeable。
2. **REJECT assumes not valid not block invalid 不是 Verify whole vote：** 看见 assumes not valid prevote nil，不是 430 bundled interchangeable / 433 REJECT whole vote interchangeable / 33 free filter interchangeable。
3. **REJECT not can't execute candidate 不是 already committed：** 看见 MAY fully execute candidate，不是 430 bundled interchangeable / 452 already committed interchangeable / 455 can't execute interchangeable。

## 为什么要分开叫

官方把 status valid/invalid、REJECT assumes not valid not block invalid、REJECT not can't execute candidate、Process 回包栏 bundled（430）、Process REJECT consensus assume（533）、status must exclusively depend（534）写成三个名字。把它们叫成一个「看见回了 ProcessProposalResponse.status 就已经当成块非法 interchangeable」，会把 status 语义、assumes not valid、candidate 可执行三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Response status valid/invalid 正式三事，先数清问的是 status valid/invalid 是不是 block invalid、REJECT assumes not valid 是不是 Verify whole vote、REJECT 是不是 can't execute candidate，再决定要不要同一次发布。
