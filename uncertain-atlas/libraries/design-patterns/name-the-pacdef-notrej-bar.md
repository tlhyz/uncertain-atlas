# 模式：点名 pacdef-notrej 杠

**层次**：实现 / ProcAcceptDef REJECT-path not already can't-Reject / not already 430-bundled / not already 455-assume 正式三事（532 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应**：[`../tracks/implementation/worked-example-pacdef-notrej-vs-bundled.md`](../tracks/implementation/worked-example-pacdef-notrej-vs-bundled.md)。

- **REJECT 时共识 assumes not valid 不是已经不能 Reject 不是已经 Process SHOULD Accept bundled：看见REJECT 时共识 assumes not valid 不是已经不能 Reject，不是已经 Process SHOULD Accept bundled interchangeable / 1341 pacdef-notrej interchangeable。**
- **REJECT assumes not valid 不是已经 ProcessProposalResponse.status bundled：看见REJECT assumes not valid，不是已经 ProcessProposalResponse.status bundled interchangeable / 1341 pacdef-notrej interchangeable。**
- **REJECT 时共识 assumes not valid 不是已经不能 Reject 不是已经 Process REJECT consensus assume bundled：看见REJECT 时共识 assumes not valid 不是已经不能 Reject，不是已经 Process REJECT consensus assume bundled interchangeable / 1341 pacdef-notrej interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事（532 余量），必须分开 not already can't-Reject、not already 456-bundled、not already 340-general 三件事。
