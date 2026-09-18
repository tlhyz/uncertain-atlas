# 模式：点名 vreqb-notkey 杠

**层次**：实现 / VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应**：[`../tracks/implementation/worked-example-vreqb-notkey-vs-bundled.md`](../tracks/implementation/worked-example-vreqb-notkey-vs-bundled.md)。

- **validator_address 不是已经带了公钥：** 看见填了 validator_address，不是已经带了公钥 interchangeable / 1079 vreqb-notkey interchangeable。
- **看见能指签扩展的人 不是已经是 proposer_address：** 看见能指签扩展的人，不是已经是造这份提案的 proposer_address interchangeable。
- **看见有地址 不是已经能验签：** 看见有地址，不是已经能验签 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_address 正式三事（436 余量），先数清问的是是不是已经带了公钥、是不是已经是 proposer、还是看见有地址是不是已经能验签，再决定要不要同一次发布。436 verifyreqbar vs rest bundled unbundling 在本页 item 1 启动。
