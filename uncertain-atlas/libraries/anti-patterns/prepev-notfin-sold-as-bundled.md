# 反模式：把 PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事（448 余量） 写成已经 已经是 CheckTxResponse.events / 已经是 ExecTxResult.events / 已经印进 LastResultsHash

**层次**：实现 / PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事（448 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应**：[`../tracks/implementation/worked-example-prepev-notfin-vs-bundled.md`](../tracks/implementation/worked-example-prepev-notfin-vs-bundled.md)。

把 PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事（448 余量） 写成已经 已经是 CheckTxResponse.events / 已经是 ExecTxResult.events / 已经印进 LastResultsHash，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（448 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 448 / 431 / 381 / 1368 / 1369 糊成一句。

也不是：

- [prepev-notret-sold-as-bundled](prepev-notret-sold-as-bundled.md) 是 notret 单句边界（1368），不是本页边界。
- [prepev-notkeep-sold-as-bundled](prepev-notkeep-sold-as-bundled.md) 是 notkeep 单句边界（1369），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
