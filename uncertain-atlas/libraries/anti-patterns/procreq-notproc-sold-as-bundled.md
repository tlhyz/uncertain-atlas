# 反模式：把 ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量） 写成已经 已经跑过 Process / 已经请求里的 hash 那种不保证已经对该块跑过 Process / 已经交差

**层次**：实现 / ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procreq-notproc-vs-bundled.md`](../tracks/implementation/worked-example-procreq-notproc-vs-bundled.md)。

把 ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量） 写成已经 已经跑过 Process / 已经请求里的 hash 那种不保证已经对该块跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.hash 正式三事（419 余量），必须分开 not already processed、not already ext-hash、not already settled 三件事，不要和 419 / 410 / 353 / 1025 / 1027 糊成一句。

也不是：

- [procreq-notexec-sold-as-bundled](procreq-notexec-sold-as-bundled.md) 是 txs 仍未执行单句边界（1025 item 1），不是本页 hash 仍未 Process 边界。
- ExtendVoteRequest.hash 就已经跑过 Process 是不变量 410，不是本页有拟议块哈希仍未 ext-hash 边界。
