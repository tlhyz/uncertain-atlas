# 反模式：把 ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事（420 余量） 写成已经 已经定奖惩 / 已经罚没 / 已经交差

**层次**：实现 / ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事（420 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procrestr-notpunish-vs-bundled.md`](../tracks/implementation/worked-example-procrestr-notpunish-vs-bundled.md)。

把 ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事（420 余量） 写成已经 已经定奖惩 / 已经罚没 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 misbehavior 正式三事（420 余量），必须分开 not already rewarded、not already slashed、not already settled 三件事，不要和 420 / 413 / 372 / 1028 / 1029 糊成一句。

也不是：

- [procrestr-notts-sold-as-bundled](procrestr-notts-sold-as-bundled.md) 是 time 仍未验过票上时间单句边界（1029 item 2），不是本页 misbehavior 仍未定奖惩边界。
- ExtendVoteRequest.misbehavior 就已经定奖惩是不变量 413，不是本页有过错列表仍未罚没边界。
