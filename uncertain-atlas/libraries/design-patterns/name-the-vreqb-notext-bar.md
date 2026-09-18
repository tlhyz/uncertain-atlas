# 模式：点名 vreqb-notext 杠

**层次**：实现 / VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应**：[`../tracks/implementation/worked-example-vreqb-notext-vs-bundled.md`](../tracks/implementation/worked-example-vreqb-notext-vs-bundled.md)。

- **non_rp 不是已经是 vote_extension：** 看见能空，不是已经是 vote_extension interchangeable / 1080 vreqb-notext interchangeable。
- **看见能空 不是已经跳过 Verify：** 看见能空，不是已经跳过 Verify interchangeable。
- **看见有第二份 不是已经同一对象：** 看见有第二份，不是已经和 vote_extension 同一对象 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp 正式三事（436 余量），先数清问的是是不是已经是 vote_extension、是不是已经跳过 Verify、还是看见有第二份是不是已经同一对象，再决定要不要同一次发布。436 verifyreqbar vs rest bundled unbundling 在本页 item 2 续。
