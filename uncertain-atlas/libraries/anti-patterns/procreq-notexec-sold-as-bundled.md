# 反模式：把 ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事（419 余量） 写成已经 已经执行那些交易 / 已经整块跑了 / 已经交差

**层次**：实现 / ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事（419 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procreq-notexec-vs-bundled.md`](../tracks/implementation/worked-example-procreq-notexec-vs-bundled.md)。

把 ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事（419 余量） 写成已经 已经执行那些交易 / 已经整块跑了 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.txs 正式三事（419 余量），必须分开 not already executed、not already whole-block、not already settled 三件事，不要和 419 / 411 / 410 / 1026 / 1027 糊成一句。

也不是：

- [extreqhash-notts-sold-as-bundled](extreqhash-notts-sold-as-bundled.md) 是 ExtendVoteRequest.time 仍未验过票上时间边界（410/1024），不是本页 txs 仍未执行边界。
- ExtendVoteRequest.txs 就已经执行那些交易是不变量 411，不是本页有交易列表仍未整块跑边界。
