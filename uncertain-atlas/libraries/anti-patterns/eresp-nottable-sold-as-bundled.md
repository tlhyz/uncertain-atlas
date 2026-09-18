# 反模式：把 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量） 写成已经 已经是 vote_extension 表 / 已经跳过 Verify / 已经同一份

**层次**：实现 / VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-eresp-nottable-vs-bundled.md`](../tracks/implementation/worked-example-eresp-nottable-vs-bundled.md)。

把 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量） 写成已经 已经是 vote_extension 表 / 已经跳过 Verify / 已经同一份，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify non_rp 正式三事（418 余量），必须分开 not already vote-ext-table、not already skip-verify、not already same-copy 三件事，不要和 418 / 415 / 436 / 1082 / 1083 糊成一句。

也不是：

- [eresp-notraw-sold-as-bundled](eresp-notraw-sold-as-bundled.md) 是 ExtendVote non_rp 仍未按原样签单句边界（1083 item 2），不是本页 Verify non_rp 仍未是 vote_extension 表边界。
- VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify 是不变量 415，不是本页由 CometBFT 签仍未跳过 Verify 边界。
