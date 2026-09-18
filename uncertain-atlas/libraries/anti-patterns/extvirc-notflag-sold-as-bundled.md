# 反模式：把 ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量） 写成已经 已经罚没 / 已经是 VoteInfo 的 block_id_flag / 已经交差

**层次**：实现 / ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvirc-notflag-vs-bundled.md`](../tracks/implementation/worked-example-extvirc-notflag-vs-bundled.md)。

把 ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量） 写成已经 已经罚没 / 已经是 VoteInfo 的 block_id_flag / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_id_flag 正式三事（425 余量），必须分开 not already slashed、not already voteinfo-flag、not already settled 三件事，不要和 425 / 365 / 424 / 1052 / 1054 糊成一句。

也不是：

- [extvirc-notkey-sold-as-bundled](extvirc-notkey-sold-as-bundled.md) 是 validator 仍未带公钥单句边界（1052 item 1），不是本页 block_id_flag 仍未罚没边界。
- VoteInfo 能按到场定奖惩就已经罚没是不变量 365，不是本页能指没收到仍未是 VoteInfo flag 边界。
