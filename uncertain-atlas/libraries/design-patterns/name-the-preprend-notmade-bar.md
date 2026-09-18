# 模式：点名 preprend-notmade 杠

**层次**：实现 / PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-preprend-notmade-vs-bundled.md`](../tracks/implementation/worked-example-preprend-notmade-vs-bundled.md)。

- **proposer_address 不是已经造了这份提案：** 看见填了 proposer_address，不是已经造了这份提案 interchangeable / 1056 preprend-notmade interchangeable。
- **看见正在造 不是已经知道本头哈希：** 看见正在造，不是已经知道本头哈希 interchangeable。
- **看见能指正在造的人 不是已经交差：** 看见能指正在造的人，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer_address 正式三事（426 余量），先数清问的是是不是已经造了这份提案、是不是已经知道本头哈希、还是看见能指正在造的人是不是已经交差，再决定要不要同一次发布。426 prepreqend vs finreq bundled unbundling 在本页 item 2 续。
