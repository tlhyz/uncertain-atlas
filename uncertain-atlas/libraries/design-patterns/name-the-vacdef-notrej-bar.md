# 模式：点名 vacdef-notrej 杠

**层次**：实现 / VerifyAcceptDef REJECT-path not already can't-Reject / not already 433-bundled / not already 517-discard 正式三事（529 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD Accept default strategy 句。  
**对应**：[`../tracks/implementation/worked-example-vacdef-notrej-vs-bundled.md`](../tracks/implementation/worked-example-vacdef-notrej-vs-bundled.md)。

- **REJECT 时共识拒整张票不是已经不能 Reject 不是已经 Verify SHOULD Accept bundled：看见REJECT 时共识拒整张票不是已经不能 Reject，不是已经 Verify SHOULD Accept bundled interchangeable / 1338 vacdef-notrej interchangeable。**
- **REJECT rejects whole vote 不是已经 VerifyVoteExtensionResponse.status bundled：看见REJECT rejects whole vote，不是已经 VerifyVoteExtensionResponse.status bundled interchangeable / 1338 vacdef-notrej interchangeable。**
- **REJECT 时共识拒整张票不是已经不能 Reject 不是已经 Verify When REJECT discard bundled：看见REJECT 时共识拒整张票不是已经不能 Reject，不是已经 Verify When REJECT discard bundled interchangeable / 1338 vacdef-notrej interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事（529 余量），必须分开 not already can't-Reject、not already 457-bundled、not already 341-general 三件事。
