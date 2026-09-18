# 模式：点名 prepwhen-notmanip 杠

**层次**：实现 / PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事（505 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应**：[`../tracks/implementation/worked-example-prepwhen-notmanip-vs-bundled.md`](../tracks/implementation/worked-example-prepwhen-notmanip-vs-bundled.md)。

- **应用可以改列表 不是已经 Prepare 改列表 bundled：看见应用可以改列表，不是已经 Prepare 改列表 bundled interchangeable / 1312 prepwhen-notmanip interchangeable。**
- **MAY 先整块执行出候选 不是已经候选已经是 ExecuteTxState：看见MAY 先整块执行出候选，不是已经候选已经是 ExecuteTxState interchangeable / 1312 prepwhen-notmanip interchangeable。**
- **应用可以改列表 不是已经 +2/3 之后才进来的扩展：看见应用可以改列表，不是已经 +2/3 之后才进来的扩展 interchangeable / 1312 prepwhen-notmanip interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事（505 余量），必须分开 not already raw-proposal、not already can-change-after-return、not already Prepare-list 三件事。
