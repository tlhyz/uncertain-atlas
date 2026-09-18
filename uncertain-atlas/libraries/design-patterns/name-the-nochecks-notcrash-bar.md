# 模式：点名 nochecks-notcrash 杠

**层次**：实现 / PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事（504 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-nochecks-notcrash-vs-bundled.md`](../tracks/implementation/worked-example-nochecks-notcrash-vs-bundled.md)。

- **Prepare 回包验不过引擎崩溃 不是已经是 Process REJECT：看见Prepare 回包验不过引擎崩溃，不是已经是 Process REJECT interchangeable / 1308 nochecks-notcrash interchangeable。**
- **当应用坏了并崩溃 不是已经是正确提议者必须被 Accept：看见当应用坏了并崩溃，不是已经是正确提议者必须被 Accept interchangeable / 1308 nochecks-notcrash interchangeable。**
- **Prepare 回包验不过引擎崩溃 不是已经 ProposalStatus REJECT：看见Prepare 回包验不过引擎崩溃，不是已经 ProposalStatus REJECT interchangeable / 1308 nochecks-notcrash interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事（504 余量），必须分开 not already checked-dup、not already Process-REJECT、not already must-deterministic 三件事。
