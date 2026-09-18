# 模式：点名 extvirc-notflag 杠

**层次**：实现 / ExtendedVoteInfo.block_id_flag not already slashed / not already voteinfo-flag / not already settled 正式三事（425 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvirc-notflag-vs-bundled.md`](../tracks/implementation/worked-example-extvirc-notflag-vs-bundled.md)。

- **block_id_flag 不是已经罚没：** 看见填了 block_id_flag，不是已经罚没 interchangeable / 1053 extvirc-notflag interchangeable。
- **看见能指没收到 不是已经是 VoteInfo 的 block_id_flag：** 看见能指没收到，不是已经是 VoteInfo 的 block_id_flag interchangeable。
- **看见能指 nil 不是已经交差：** 看见能指 nil，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_id_flag 正式三事（425 余量），先数清问的是是不是已经罚没、是不是已经是 VoteInfo 的 block_id_flag、还是看见能指 nil 是不是已经交差，再决定要不要同一次发布。425 extvirest vs voteinfo bundled unbundling 在本页 item 2 续。
