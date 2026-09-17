# 反模式：把 ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量） 写成已经 已经定奖惩 / 已经交差 / 已经定了奖惩

**层次**：实现 / ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-extmis-notpunish-vs-bundled.md`](../tracks/implementation/worked-example-extmis-notpunish-vs-bundled.md)。

把 ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量） 写成已经 已经定奖惩 / 已经交差 / 已经定了奖惩，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 misbehavior 正式三事（413 余量），必须分开 not already rewarded、not already settled、not already slashed 三件事，不要和 413 / 363 / 420 / 1038 / 1039 糊成一句。

也不是：

- [extrest-nothash-sold-as-bundled](extrest-nothash-sold-as-bundled.md) 是 next_validators_hash 仍未同一套字段边界（411/1036），不是本页 misbehavior 仍未定奖惩边界。
- 可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没是不变量 363，不是本页拟议块里有过错信息仍未交差边界。
