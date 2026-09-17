# 模式：点名 extmis-notkey 杠

**层次**：实现 / VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-extmis-notkey-vs-bundled.md`](../tracks/implementation/worked-example-extmis-notkey-vs-bundled.md)。

- **validator_address 不是已经带了公钥：** 看见填了 validator_address，不是已经带了公钥 interchangeable / 1039 extmis-notkey interchangeable。
- **看见能指签扩展的人 不是已经能验签：** 看见能指签扩展的人，不是已经能验签 interchangeable。
- **看见有地址 不是已经交差：** 看见有地址，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_address 正式三事（413 余量），先数清问的是是不是已经带了公钥、是不是已经能验签、还是看见有地址是不是已经交差，再决定要不要同一次发布。413 extreqmis vs reward bundled unbundling 在本页 item 3 完成。
