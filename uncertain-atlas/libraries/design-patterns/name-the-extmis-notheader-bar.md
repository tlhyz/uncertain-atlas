# 模式：点名 extmis-notheader 杠

**层次**：实现 / ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-extmis-notheader-vs-bundled.md`](../tracks/implementation/worked-example-extmis-notheader-vs-bundled.md)。

- **proposer_address 不是已经知道本头哈希：** 看见填了 proposer_address，不是已经知道本头哈希 interchangeable / 1038 extmis-notheader interchangeable。
- **看见有造提案的人 不是已经字段名对上就已经跑过 Process：** 看见有造提案的人，不是已经字段名对上就已经跑过 Process interchangeable。
- **看见能指提议者 不是已经交差：** 看见能指提议者，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer_address 正式三事（413 余量），先数清问的是是不是已经知道本头哈希、是不是已经字段名对上就已经跑过 Process、还是看见能指提议者是不是已经交差，再决定要不要同一次发布。413 extreqmis vs reward bundled unbundling 在本页 item 2 续。
