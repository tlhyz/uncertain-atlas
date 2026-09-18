# 反模式：把 ProcessProposalRequest.next_validators_hash not already prepare-hash / not already finalize-hash / not already settled 正式三事（427 余量） 写成已经 已经是 Prepare 请求末栏的 next_validators_hash / 已经是 Finalize 请求栏 / 已经交差

**层次**：实现 / ProcessProposalRequest.next_validators_hash not already prepare-hash / not already finalize-hash / not already settled 正式三事（427 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应**：[`../tracks/implementation/worked-example-procend-nothash-vs-bundled.md`](../tracks/implementation/worked-example-procend-nothash-vs-bundled.md)。

把 ProcessProposalRequest.next_validators_hash not already prepare-hash / not already finalize-hash / not already settled 正式三事（427 余量） 写成已经 已经是 Prepare 请求末栏的 next_validators_hash / 已经是 Finalize 请求栏 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（427 余量），必须分开 not already prepare-hash、not already finalize-hash、not already settled 三件事，不要和 427 / 426 / 394 / 1059 / 1060 糊成一句。

也不是：

- [preprend-notts-sold-as-bundled](preprend-notts-sold-as-bundled.md) 是 Finalize time 仍未对上头边界（426/1057），不是本页 Process next_validators_hash 仍未是 Prepare 末栏边界。
- PrepareProposalRequest.next_validators_hash 就已经是 Finalize 请求栏是不变量 426，不是本页能指下一份集合仍未是 Finalize 栏边界。
