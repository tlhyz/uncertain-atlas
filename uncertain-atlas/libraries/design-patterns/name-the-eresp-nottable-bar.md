# 模式：点名 eresp-nottable 杠

**层次**：实现 / VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-eresp-nottable-vs-bundled.md`](../tracks/implementation/worked-example-eresp-nottable-vs-bundled.md)。

- **non_rp_vote_extension 不是已经是 vote_extension 表：** 看见能空，不是已经是 vote_extension 表 interchangeable / 1084 eresp-nottable interchangeable。
- **看见由 CometBFT 签 不是已经跳过 Verify：** 看见由 CometBFT 签，不是已经跳过 Verify interchangeable。
- **看见是应用自己的信息 不是已经同一份：** 看见是应用自己的信息，不是已经和 vote_extension 同一份 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify non_rp 正式三事（418 余量），先数清问的是是不是已经是 vote_extension 表、是不是已经跳过 Verify、还是看见是应用自己的信息是不是已经同一份，再决定要不要同一次发布。418 extresp vs wrap bundled unbundling 在本页 item 3 完成。
