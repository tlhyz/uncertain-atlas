# 反模式：把 PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量） 写成已经 已经造了这份提案 / 已经知道本头哈希 / 已经交差

**层次**：实现 / PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-preprend-notmade-vs-bundled.md`](../tracks/implementation/worked-example-preprend-notmade-vs-bundled.md)。

把 PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量） 写成已经 已经造了这份提案 / 已经知道本头哈希 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer_address 正式三事（426 余量），必须分开 not already made、not already header-known、not already settled 三件事，不要和 426 / 413 / 359 / 1055 / 1057 糊成一句。

也不是：

- [preprend-nothash-sold-as-bundled](preprend-nothash-sold-as-bundled.md) 是 next_validators_hash 仍未是 Finalize 栏单句边界（1055 item 1），不是本页 proposer 仍未造完边界。
- ExtendVoteRequest.proposer_address 就已经知道本头哈希是不变量 413，不是本页正在造仍未知道本头边界。
