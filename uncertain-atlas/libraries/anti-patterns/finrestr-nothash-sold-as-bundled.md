# 反模式：把 FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量） 写成已经 已经是 ProcessProposalRequest.hash / 已经跑过 Process / 已经交差

**层次**：实现 / FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finrestr-nothash-vs-bundled.md`](../tracks/implementation/worked-example-finrestr-nothash-vs-bundled.md)。

把 FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量） 写成已经 已经是 ProcessProposalRequest.hash / 已经跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 hash 正式三事（428 余量），必须分开 not already process-hash、not already processed、not already settled 三件事，不要和 428 / 419 / 410 / 1062 / 1063 糊成一句。

也不是：

- [procend-notprelim-sold-as-bundled](procend-notprelim-sold-as-bundled.md) 是 Prepare 回包 txs 仍未是初步列表边界（427/1060），不是本页 Finalize hash 仍未是 Process hash 边界。
- ProcessProposalRequest.hash 就已经跑过 Process 是不变量 419，不是本页能指已决块仍未 Process 边界。
