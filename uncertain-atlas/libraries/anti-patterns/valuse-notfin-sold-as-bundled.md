# 反模式：把 ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事（449 余量） 写成已经 已经是 Process proposed_last_commit / 已经交差 / 已经可以拿 Prepare Extended 代替

**层次**：实现 / ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事（449 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应**：[`../tracks/implementation/worked-example-valuse-notfin-vs-bundled.md`](../tracks/implementation/worked-example-valuse-notfin-vs-bundled.md)。

把 ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事（449 余量） 写成已经 已经是 Process proposed_last_commit / 已经交差 / 已经可以拿 Prepare Extended 代替，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（449 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事，不要和 449 / 365 / 364 / 1371 / 1373 糊成一句。

也不是：

- [valuse-notproc-sold-as-bundled](valuse-notproc-sold-as-bundled.md) 是 notproc 单句边界（1371），不是本页边界。
- [valuse-notprep-sold-as-bundled](valuse-notprep-sold-as-bundled.md) 是 notprep 单句边界（1373），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 ProcAcceptDef 默认不是 340 通则边界（532/1342），不是本页 ExtendVote When step 7 广播边界。
