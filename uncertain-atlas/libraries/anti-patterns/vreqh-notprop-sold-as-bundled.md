# 反模式：把 VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量） 写成已经 已经是拟议块高度 / 已经对上了拟议块 / 已经会调 Verify

**层次**：实现 / VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-vreqh-notprop-vs-bundled.md`](../tracks/implementation/worked-example-vreqh-notprop-vs-bundled.md)。

把 VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量） 写成已经 已经是拟议块高度 / 已经对上了拟议块 / 已经会调 Verify，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 正式三事（415 余量），必须分开 not already proposed-height、not already aligned、not already will-call 三件事，不要和 415 / 410 / 435 / 1089 / 1090 糊成一句。

也不是：

- [vfwhen-notcommit-sold-as-bundled](vfwhen-notcommit-sold-as-bundled.md) 是 ACCEPT/REJECT 仍未写进 last_commit 边界（435/1087），不是本页 Verify height 仍未是拟议块高度边界。
- ExtendVoteRequest.height 就已经对上了拟议块是不变量 410，不是本页能对一下仍未对上边界。
