# 模式：点名 prepwhen-notsync 杠

**层次**：实现 / PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事（505 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应**：[`../tracks/implementation/worked-example-prepwhen-notsync-vs-bundled.md`](../tracks/implementation/worked-example-prepwhen-notsync-vs-bundled.md)。

- **PrepareProposal 调用是同步的 不是已经能在返回之后再改裁决：看见PrepareProposal 调用是同步的，不是已经能在返回之后再改裁决 interchangeable / 1311 prepwhen-notsync interchangeable。**
- **引擎会等到应用返回 不是已经离开关键路径：看见引擎会等到应用返回，不是已经离开关键路径 interchangeable / 1311 prepwhen-notsync interchangeable。**
- **PrepareProposal 调用是同步的 不是已经 Process 调用是同步的：看见PrepareProposal 调用是同步的，不是已经 Process 调用是同步的 interchangeable / 1311 prepwhen-notsync interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事（505 余量），必须分开 not already raw-proposal、not already can-change-after-return、not already Prepare-list 三件事。
