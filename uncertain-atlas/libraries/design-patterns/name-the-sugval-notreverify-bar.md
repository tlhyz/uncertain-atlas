# 模式：点名 sugval-notreverify 杠

**层次**：实现 / SuggestValidate not-reverify not already verified / not already called-again / not already MAY-add-without-Verify 正式三事（520 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**对应**：[`../tracks/implementation/worked-example-sugval-notreverify-vs-bundled.md`](../tracks/implementation/worked-example-sugval-notreverify-vs-bundled.md)。

- **建议自验不是引擎会再 Verify 不是已经是引擎会再 Verify：看见建议自验不是引擎会再 Verify，不是已经是引擎会再 Verify interchangeable / 1318 sugval-notreverify interchangeable。**
- **not calling VerifyVoteExtension again 不是已经又叫了 Verify：看见not calling VerifyVoteExtension again，不是已经又叫了 Verify interchangeable / 1318 sugval-notreverify interchangeable。**
- **建议自验不是引擎会再 Verify 不是已经 Verify 过：看见建议自验不是引擎会再 Verify，不是已经 Verify 过 interchangeable / 1318 sugval-notreverify interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When suggested validate like Verify 正式三事（520 余量），必须分开 not already must-Accept、not already step-2-call、not already engine-re-Verify 三件事。
