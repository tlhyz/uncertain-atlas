# 反模式：把 VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事（415 余量） 写成已经 已经不保证跑过 Process / 已经是 ExtendVoteRequest.hash / 已经交差

**层次**：实现 / VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事（415 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-vreqh-notproc-vs-bundled.md`](../tracks/implementation/worked-example-vreqh-notproc-vs-bundled.md)。

把 VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事（415 余量） 写成已经 已经不保证跑过 Process / 已经是 ExtendVoteRequest.hash / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 hash 正式三事（415 余量），必须分开 not already not-guaranteed-processed、not already ext-hash、not already settled 三件事，不要和 415 / 353 / 410 / 1088 / 1090 糊成一句。

也不是：

- [vreqh-notprop-sold-as-bundled](vreqh-notprop-sold-as-bundled.md) 是 height 仍未是拟议块高度单句边界（1088 item 1），不是本页 hash 仍未不保证跑过 Process 边界。
- 请求里的 hash 就已经对该块跑过 Process 是不变量 353，不是本页有拟议块哈希仍未是 ExtendVote hash 边界。
