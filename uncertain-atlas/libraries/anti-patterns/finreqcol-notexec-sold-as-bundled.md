# 反模式：把 FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量） 写成已经 已经执行那些交易 / 已经是 ProcessProposalRequest.txs / 已经交差

**层次**：实现 / FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finreqcol-notexec-vs-bundled.md`](../tracks/implementation/worked-example-finreqcol-notexec-vs-bundled.md)。

把 FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量） 写成已经 已经执行那些交易 / 已经是 ProcessProposalRequest.txs / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 txs 正式三事（422 余量），必须分开 not already executed、not already process-txs、not already settled 三件事，不要和 422 / 408 / 411 / 419 / 1040 / 1041 糊成一句。

也不是：

- [finreqcol-nothead-sold-as-bundled](finreqcol-nothead-sold-as-bundled.md) 是 height 仍未对上拟议块头单句边界（1041 item 2），不是本页 txs 仍未执行边界。
- Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差是不变量 408，不是本页有交易列表仍未是 Process txs 边界。
