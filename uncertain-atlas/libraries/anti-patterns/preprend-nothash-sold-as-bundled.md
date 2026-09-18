# 反模式：把 PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事（426 余量） 写成已经 已经是 Finalize 请求栏的 next_validators_hash / 已经换了人 / 已经交差

**层次**：实现 / PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事（426 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-preprend-nothash-vs-bundled.md`](../tracks/implementation/worked-example-preprend-nothash-vs-bundled.md)。

把 PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事（426 余量） 写成已经 已经是 Finalize 请求栏的 next_validators_hash / 已经换了人 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（426 余量），必须分开 not already finalize-hash、not already rotated、not already settled 三件事，不要和 426 / 394 / 411 / 1056 / 1057 糊成一句。

也不是：

- [extvirc-notgive-sold-as-bundled](extvirc-notgive-sold-as-bundled.md) 是 non_rp 签仍未交给应用边界（425/1054），不是本页 next_validators_hash 仍未是 Finalize 栏边界。
- Finalize 请求 next_validators_hash 就已经是同一套字段是不变量 394，不是本页能指下一份集合仍未换人边界。
