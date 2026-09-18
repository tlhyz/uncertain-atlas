# 反模式：把 VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量） 写成已经 已经跳过 Verify / 已经按原样签 / 已经交差

**层次**：实现 / VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-vreqh-notskip-vs-bundled.md`](../tracks/implementation/worked-example-vreqh-notskip-vs-bundled.md)。

把 VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量） 写成已经 已经跳过 Verify / 已经按原样签 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 正式三事（415 余量），必须分开 not already skip-verify、not already signed-as-is、not already settled 三件事，不要和 415 / 353 / 358 / 1088 / 1089 糊成一句。

也不是：

- [vreqh-notproc-sold-as-bundled](vreqh-notproc-sold-as-bundled.md) 是 hash 仍未不保证跑过 Process 单句边界（1089 item 2），不是本页 vote_extension 仍未跳过 Verify 边界。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签是不变量 358，不是本页由 CometBFT 签仍未按原样签边界。
