# 反模式：把 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量） 写成已经 已经是 vote_extension / 已经跳过 Verify / 已经同一对象

**层次**：实现 / VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应**：[`../tracks/implementation/worked-example-vreqb-notext-vs-bundled.md`](../tracks/implementation/worked-example-vreqb-notext-vs-bundled.md)。

把 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量） 写成已经 已经是 vote_extension / 已经跳过 Verify / 已经同一对象，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp 正式三事（436 余量），必须分开 not already vote-extension、not already skip-verify、not already same-object 三件事，不要和 436 / 415 / 353 / 1079 / 1081 糊成一句。

也不是：

- [vreqb-notkey-sold-as-bundled](vreqb-notkey-sold-as-bundled.md) 是 validator_address 仍未带了公钥单句边界（1079 item 1），不是本页 non_rp 仍未是 vote_extension 边界。
- VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify 是不变量 415，不是本页能空仍未跳过 Verify 边界。
