# 模式：点名 vreqh-notskip 杠

**层次**：实现 / VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-vreqh-notskip-vs-bundled.md`](../tracks/implementation/worked-example-vreqh-notskip-vs-bundled.md)。

- **vote_extension 不是已经跳过 Verify：** 看见能空，不是已经跳过 Verify interchangeable / 1090 vreqh-notskip interchangeable。
- **看见由 CometBFT 签 不是已经按原样签：** 看见由 CometBFT 签，不是已经按原样签 interchangeable。
- **看见是应用自己的信息 不是已经交差：** 看见是应用自己的信息，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 正式三事（415 余量），先数清问的是是不是已经跳过 Verify、是不是已经按原样签、还是看见是应用自己的信息是不是已经交差，再决定要不要同一次发布。415 verifyheight vs extheight bundled unbundling 在本页 item 3 完成。
