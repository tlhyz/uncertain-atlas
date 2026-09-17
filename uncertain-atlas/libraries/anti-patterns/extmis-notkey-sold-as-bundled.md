# 反模式：把 VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量） 写成已经 已经带了公钥 / 已经能验签 / 已经交差

**层次**：实现 / VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-extmis-notkey-vs-bundled.md`](../tracks/implementation/worked-example-extmis-notkey-vs-bundled.md)。

把 VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量） 写成已经 已经带了公钥 / 已经能验签 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_address 正式三事（413 余量），必须分开 not already has-key、not already can-verify、not already settled 三件事，不要和 413 / 364 / 353 / 1037 / 1038 糊成一句。

也不是：

- [extmis-notheader-sold-as-bundled](extmis-notheader-sold-as-bundled.md) 是 proposer_address 仍未知道本头哈希单句边界（1038 item 2），不是本页 validator_address 仍未带公钥边界。
- Validator 用 address 认人就已经带了公钥是不变量 364，不是本页能指签扩展的人仍未能验签边界。
