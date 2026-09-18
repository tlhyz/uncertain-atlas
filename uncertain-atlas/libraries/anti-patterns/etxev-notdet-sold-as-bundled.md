# 反模式：把 ExecTxEv tx events marked non-deterministic not already consensus-field / not already hashed / not already 316-det 正式三事（446 余量） 写成已经 已经是共识字段 / 已经编进结构再哈希 / 已经必须确定

**层次**：实现 / ExecTxEv tx events marked non-deterministic not already consensus-field / not already hashed / not already 316-det 正式三事（446 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields events 句。  
**对应**：[`../tracks/implementation/worked-example-etxev-notdet-vs-bundled.md`](../tracks/implementation/worked-example-etxev-notdet-vs-bundled.md)。

把 ExecTxEv tx events marked non-deterministic not already consensus-field / not already hashed / not already 316-det 正式三事（446 余量） 写成已经 已经是共识字段 / 已经编进结构再哈希 / 已经必须确定，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（446 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 446 / 431 / 316 / 1362 / 1364 糊成一句。

也不是：

- [etxev-notidx-sold-as-bundled](etxev-notidx-sold-as-bundled.md) 是 notidx 单句边界（1362），不是本页边界。
- [etxev-notlvl-sold-as-bundled](etxev-notlvl-sold-as-bundled.md) 是 notlvl 单句边界（1364），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
