# 反模式：把 ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事（446 余量） 写成已经 已经是 FinalizeBlockResponse.events / 已经是 CheckTxResponse.events / 已经和池门回包 interchangeable

**层次**：实现 / ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事（446 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields events 句。  
**对应**：[`../tracks/implementation/worked-example-etxev-notlvl-vs-bundled.md`](../tracks/implementation/worked-example-etxev-notlvl-vs-bundled.md)。

把 ExecTxEv per-tx events in tx_results not already block-level 431 / not already CheckTx 381 / not already interchangeable 正式三事（446 余量） 写成已经 已经是 FinalizeBlockResponse.events / 已经是 CheckTxResponse.events / 已经和池门回包 interchangeable，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（446 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 446 / 431 / 381 / 1362 / 1363 糊成一句。

也不是：

- [etxev-notidx-sold-as-bundled](etxev-notidx-sold-as-bundled.md) 是 notidx 单句边界（1362），不是本页边界。
- [etxev-notdet-sold-as-bundled](etxev-notdet-sold-as-bundled.md) 是 notdet 单句边界（1363），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
