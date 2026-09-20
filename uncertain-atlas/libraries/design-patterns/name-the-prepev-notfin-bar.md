# 模式：点名 prepev-notfin 杠

**层次**：实现 / PrepEv pass via FinalizeBlockResponse not already CheckTx events / not already ExecTxResult events / not already LastResultsHash 正式三事（448 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应**：[`../tracks/implementation/worked-example-prepev-notfin-vs-bundled.md`](../tracks/implementation/worked-example-prepev-notfin-vs-bundled.md)。

- **经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events 不是已经是 CheckTxResponse.events：看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events，不是已经是 CheckTxResponse.events interchangeable / 1370 prepev-notfin interchangeable。**
- **pass via FinalizeBlockResponse is not already CheckTx or ExecTx events 不是已经是 ExecTxResult.events：看见pass via FinalizeBlockResponse is not already CheckTx or ExecTx events，不是已经是 ExecTxResult.events interchangeable / 1370 prepev-notfin interchangeable。**
- **经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events 不是已经印进 LastResultsHash：看见经 FinalizeBlockResponse 交回不是已经是 CheckTx/ExecTx events，不是已经印进 LastResultsHash interchangeable / 1370 prepev-notfin interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（448 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
