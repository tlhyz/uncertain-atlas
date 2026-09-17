# 反模式：把 ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量） 写成已经 已经交差 local_last_commit / 已经字段名对上就已经跑过 Process / 已经是本头 LastCommit

**层次**：实现 / ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extrest-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-extrest-notlocal-vs-bundled.md)。

把 ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量） 写成已经 已经交差 local_last_commit / 已经字段名对上就已经跑过 Process / 已经是本头 LastCommit，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposed_last_commit 正式三事（411 余量），必须分开 not already local-settled、not already processed、not already this-header 三件事，不要和 411 / 359 / 420 / 1034 / 1036 糊成一句。

也不是：

- [extrest-notexec-sold-as-bundled](extrest-notexec-sold-as-bundled.md) 是 txs 仍未执行单句边界（1034 item 1），不是本页 proposed_last_commit 仍未交差 local 边界。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process 是不变量 359，不是本页有上一份 last commit 仍未 Process 边界。
