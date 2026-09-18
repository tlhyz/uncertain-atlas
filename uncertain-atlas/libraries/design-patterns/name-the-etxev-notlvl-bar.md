# 模式：点名 etxev-notlvl 杠

**层次**：实现 / ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事（446 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields events 句。  
**对应**：[`../tracks/implementation/worked-example-etxev-notlvl-vs-bundled.md`](../tracks/implementation/worked-example-etxev-notlvl-vs-bundled.md)。

- **逐笔 events 不是已经是块级 Finalize events 不是已经是 FinalizeBlockResponse.events：看见逐笔 events 不是已经是块级 Finalize events，不是已经是 FinalizeBlockResponse.events interchangeable / 1364 etxev-notlvl interchangeable。**
- **per-tx events is not already FinalizeBlockResponse.events 不是已经是 CheckTxResponse.events：看见per-tx events is not already FinalizeBlockResponse.events，不是已经是 CheckTxResponse.events interchangeable / 1364 etxev-notlvl interchangeable。**
- **逐笔 events 不是已经是块级 Finalize events 不是已经和池门回包 interchangeable：看见逐笔 events 不是已经是块级 Finalize events，不是已经和池门回包 interchangeable interchangeable / 1364 etxev-notlvl interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（446 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
