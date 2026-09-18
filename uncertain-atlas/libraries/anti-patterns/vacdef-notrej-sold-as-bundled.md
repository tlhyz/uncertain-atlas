# 反模式：把 VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事（529 余量） 写成已经 已经 Verify SHOULD Accept bundled / 已经 VerifyVoteExtensionResponse.status bundled / 已经 Verify When REJECT discard bundled

**层次**：实现 / VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事（529 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD Accept default strategy 句。  
**对应**：[`../tracks/implementation/worked-example-vacdef-notrej-vs-bundled.md`](../tracks/implementation/worked-example-vacdef-notrej-vs-bundled.md)。

把 VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事（529 余量） 写成已经 已经 Verify SHOULD Accept bundled / 已经 VerifyVoteExtensionResponse.status bundled / 已经 Verify When REJECT discard bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事（529 余量），必须分开 not already can't-Reject、not already 457-bundled、not already 341-general 三件事，不要和 529 / 433 / 517 / 1337 / 1339 糊成一句。

也不是：

- [vacdef-notcant-sold-as-bundled](vacdef-notcant-sold-as-bundled.md) 是 notcant 单句边界（1337），不是本页边界。
- [vacdef-not341-sold-as-bundled](vacdef-not341-sold-as-bundled.md) 是 not341 单句边界（1339），不是本页边界。
- [vwkeep-notrej-sold-as-bundled](vwkeep-notrej-sold-as-bundled.md) 是 VerifyKeep REJECT 丢掉仍未是 step 1 discard 边界（517/1336），不是本页 SHOULD Accept 默认策略边界。
