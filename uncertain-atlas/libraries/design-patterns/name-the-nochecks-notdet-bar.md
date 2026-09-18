# 模式：点名 nochecks-notdet 杠

**层次**：实现 / PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事（504 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-nochecks-notdet-vs-bundled.md`](../tracks/implementation/worked-example-nochecks-notdet-vs-bundled.md)。

- **Prepare 实现可以非确定 不是已经必须确定：看见Prepare 实现可以非确定，不是已经必须确定 interchangeable / 1309 nochecks-notdet interchangeable。**
- **MAY be non-deterministic 不是已经和 Process / Finalize 同一把尺：看见MAY be non-deterministic，不是已经和 Process / Finalize 同一把尺 interchangeable / 1309 nochecks-notdet interchangeable。**
- **Prepare 实现可以非确定 不是已经 Process MUST deterministic：看见Prepare 实现可以非确定，不是已经 Process MUST deterministic interchangeable / 1309 nochecks-notdet interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事（504 余量），必须分开 not already checked-dup、not already Process-REJECT、not already must-deterministic 三件事。
