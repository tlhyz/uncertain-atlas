# 反模式：把 FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量） 写成已经 已经定奖惩 / 已经是 ProcessProposalRequest.misbehavior / 已经交差

**层次**：实现 / FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finrestr-notpunish-vs-bundled.md`](../tracks/implementation/worked-example-finrestr-notpunish-vs-bundled.md)。

把 FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量） 写成已经 已经定奖惩 / 已经是 ProcessProposalRequest.misbehavior / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 misbehavior 正式三事（428 余量），必须分开 not already rewarded、not already process-mis、not already settled 三件事，不要和 428 / 363 / 420 / 1061 / 1063 糊成一句。

也不是：

- [finrestr-nothash-sold-as-bundled](finrestr-nothash-sold-as-bundled.md) 是 hash 仍未是 Process hash 单句边界（1061 item 1），不是本页 misbehavior 仍未定奖惩边界。
- 可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没是不变量 363，不是本页有过错列表仍未是 Process misbehavior 边界。
