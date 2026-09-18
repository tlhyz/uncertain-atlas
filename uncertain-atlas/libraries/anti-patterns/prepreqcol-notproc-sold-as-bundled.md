# 反模式：把 PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量） 写成已经 已经跑过 Process / 已经执行那些交易 / 已经交差

**层次**：实现 / PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-prepreqcol-notproc-vs-bundled.md`](../tracks/implementation/worked-example-prepreqcol-notproc-vs-bundled.md)。

把 PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量） 写成已经 已经跑过 Process / 已经执行那些交易 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 txs 正式三事（423 余量），必须分开 not already processed、not already executed、not already settled 三件事，不要和 423 / 359 / 422 / 419 / 1046 / 1048 糊成一句。

也不是：

- [prepreqcol-notcap-sold-as-bundled](prepreqcol-notcap-sold-as-bundled.md) 是 max_tx_bytes 仍未能回超限列表单句边界（1046 item 1），不是本页 txs 仍未跑过 Process 边界。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process 是不变量 359，不是本页是初步列表仍未执行边界。
