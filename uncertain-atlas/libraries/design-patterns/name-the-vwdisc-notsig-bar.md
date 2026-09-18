# 模式：点名 vwdisc-notsig 杠

**层次**：实现 / VerifyDiscard discard not already Verify-When / not already skip-Verify / not already verified 正式三事（514 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应**：[`../tracks/implementation/worked-example-vwdisc-notsig-vs-bundled.md`](../tracks/implementation/worked-example-vwdisc-notsig-vs-bundled.md)。

- **Precommit 没有带有效签的扩展就会当非法丢掉 不是已经 Verify When 正式流程 bundled：看见Precommit 没有带有效签的扩展就会当非法丢掉，不是已经 Verify When 正式流程 bundled interchangeable / 1325 vwdisc-notsig interchangeable。**
- **discards as invalid 不是已经跳过 Verify：看见discards as invalid，不是已经跳过 Verify interchangeable / 1325 vwdisc-notsig interchangeable。**
- **Precommit 没有带有效签的扩展就会当非法丢掉 不是已经验过扩展：看见Precommit 没有带有效签的扩展就会当非法丢掉，不是已经验过扩展 interchangeable / 1325 vwdisc-notsig interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事（514 余量），必须分开 not already Verify-When-bundled、not already still-calls-Verify、not already verified 三件事。
