# 反模式：把 ProcAcceptDef default not already 456-bundled / not already 340-general / not already 530-always 正式三事（532 余量） 写成已经 已经 Process SHOULD Accept bundled / 已经 Process 340 SHOULD Accept 通则 / 已经 SHOULD always set ACCEPT bundled

**层次**：实现 / ProcAcceptDef default not already 456-bundled / not already 340-general / not already 530-always 正式三事（532 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应**：[`../tracks/implementation/worked-example-pacdef-not340-vs-bundled.md`](../tracks/implementation/worked-example-pacdef-not340-vs-bundled.md)。

把 ProcAcceptDef default not already 456-bundled / not already 340-general / not already 530-always 正式三事（532 余量） 写成已经 已经 Process SHOULD Accept bundled / 已经 Process 340 SHOULD Accept 通则 / 已经 SHOULD always set ACCEPT bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（532 余量），必须分开 not already can't-Reject、not already 456-bundled、not already 340-general 三件事，不要和 532 / 340 / 531 / 1340 / 1341 糊成一句。

也不是：

- [pacdef-notcant-sold-as-bundled](pacdef-notcant-sold-as-bundled.md) 是 notcant 单句边界（1340），不是本页边界。
- [pacdef-notrej-sold-as-bundled](pacdef-notrej-sold-as-bundled.md) 是 notrej 单句边界（1341），不是本页边界。
- [vacdef-not341-sold-as-bundled](vacdef-not341-sold-as-bundled.md) 是 VerifyAcceptDef 默认不是 341 通则边界（529/1339），不是本页 Process SHOULD Accept 默认策略边界。
