# 反模式：把 PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量） 写成已经 已经交差 proposed_last_commit / 已经是本高度刚签的扩展 / 已经交差

**层次**：实现 / PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-preprestr-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-preprestr-notlocal-vs-bundled.md)。

把 PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量） 写成已经 已经交差 proposed_last_commit / 已经是本高度刚签的扩展 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 正式三事（424 余量），必须分开 not already proposed、not already last-ext、not already settled 三件事，不要和 424 / 420 / 359 / 1050 / 1051 糊成一句。

也不是：

- [prepreqcol-nothead-sold-as-bundled](prepreqcol-nothead-sold-as-bundled.md) 是 Prepare height 仍未对上头边界（423/1048），不是本页 local_last_commit 仍未交差 proposed 边界。
- ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit 是不变量 420，不是本页从本进程拿到仍未是本高度刚签扩展边界。
