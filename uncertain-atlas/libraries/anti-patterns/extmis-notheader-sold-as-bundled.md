# 反模式：把 ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量） 写成已经 已经知道本头哈希 / 已经字段名对上就已经跑过 Process / 已经交差

**层次**：实现 / ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-extmis-notheader-vs-bundled.md`](../tracks/implementation/worked-example-extmis-notheader-vs-bundled.md)。

把 ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量） 写成已经 已经知道本头哈希 / 已经字段名对上就已经跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer_address 正式三事（413 余量），必须分开 not already header-known、not already processed、not already settled 三件事，不要和 413 / 359 / 311 / 1037 / 1039 糊成一句。

也不是：

- [extmis-notpunish-sold-as-bundled](extmis-notpunish-sold-as-bundled.md) 是 misbehavior 仍未定奖惩单句边界（1037 item 1），不是本页 proposer_address 仍未知道本头哈希边界。
- Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希是不变量 359，不是本页有造提案的人仍未 Process 边界。
