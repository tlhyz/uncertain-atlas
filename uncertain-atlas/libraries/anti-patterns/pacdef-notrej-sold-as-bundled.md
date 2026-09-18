# 反模式：把 ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事（532 余量） 写成已经 已经 Process SHOULD Accept bundled / 已经 ProcessProposalResponse.status bundled / 已经 Process REJECT consensus assume bundled

**层次**：实现 / ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事（532 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应**：[`../tracks/implementation/worked-example-pacdef-notrej-vs-bundled.md`](../tracks/implementation/worked-example-pacdef-notrej-vs-bundled.md)。

把 ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事（532 余量） 写成已经 已经 Process SHOULD Accept bundled / 已经 ProcessProposalResponse.status bundled / 已经 Process REJECT consensus assume bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（532 余量），必须分开 not already can't-Reject、not already 456-bundled、not already 340-general 三件事，不要和 532 / 430 / 455 / 1340 / 1342 糊成一句。

也不是：

- [pacdef-notcant-sold-as-bundled](pacdef-notcant-sold-as-bundled.md) 是 notcant 单句边界（1340），不是本页边界。
- [pacdef-not340-sold-as-bundled](pacdef-not340-sold-as-bundled.md) 是 not340 单句边界（1342），不是本页边界。
- [vacdef-not341-sold-as-bundled](vacdef-not341-sold-as-bundled.md) 是 VerifyAcceptDef 默认不是 341 通则边界（529/1339），不是本页 Process SHOULD Accept 默认策略边界。
