# 反模式：把 ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量） 写成已经 已经交差 local_last_commit / 已经交差 / 已经跑过 Process

**层次**：实现 / ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procrestr-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-procrestr-notlocal-vs-bundled.md)。

把 ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量） 写成已经 已经交差 local_last_commit / 已经交差 / 已经跑过 Process，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposed_last_commit 正式三事（420 余量），必须分开 not already local-settled、not already ext-commit、not already processed 三件事，不要和 420 / 411 / 419 / 1029 / 1030 糊成一句。

也不是：

- [procreq-nothead-sold-as-bundled](procreq-nothead-sold-as-bundled.md) 是 ProcessProposalRequest.height 仍未对上拟议块头边界（419/1027），不是本页 proposed_last_commit 仍未交差 local 边界。
- ExtendVoteRequest.proposed_last_commit 就已经交差 local_last_commit 是不变量 411，不是本页从拟议块拿到仍未交差边界。
