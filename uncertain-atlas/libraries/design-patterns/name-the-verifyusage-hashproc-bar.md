# 模式：把 VerifyVoteExtension Usage hash does not guarantee Process 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage hash 句。  
**例**：[hash does not guarantee Process ≠ bundled](../../tracks/implementation/worked-example-verifyusage-hashproc-vs-bundled.md)。

## 三个名字

1. **hash points to a block 不是 already Process'd：** 看见 hash in request，不是 353 bundled interchangeable / 422 table hash interchangeable / 394 Finalize hash interchangeable。
2. **does not guarantee exposed via ProcessProposal 不是 proposer also Process：** 看见 not guarantee，不是 351 proposer Process interchangeable / 351 txs matched interchangeable / 515 Verify call interchangeable。
3. **hash does not guarantee Process 不是 Verify Usage bundled：** 看见 not already Process'd，不是 353 bundled interchangeable / 521 empty ext interchangeable / 522 local process interchangeable。

## 为什么要分开叫

官方把 hash points to a block、does not guarantee ProcessProposal exposure、not already Process'd、Verify Usage bundled（353）、Process 也会在提议者那边叫（351）写成三个名字。把它们叫成一个「看见请求里的 hash 就已经对该块跑过 Process interchangeable、已经 Process 过 interchangeable」，会把有 hash、不保证 Process、不是已经 Process 过三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage hash does not guarantee Process 正式三事，先数清问的是 hash points to a block 是不是 already Process'd、does not guarantee ProcessProposal 是不是 proposer also Process、hash does not guarantee Process 是不是 Verify Usage bundled，再决定要不要同一次发布。
