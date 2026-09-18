# 模式：点名 vwdisc-notstep 杠

**层次**：实现 / VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事（514 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应**：[`../tracks/implementation/worked-example-vwdisc-notstep-vs-bundled.md`](../tracks/implementation/worked-example-vwdisc-notstep-vs-bundled.md)。

- **step 1 在调 VerifyVoteExtension 之前 不是已经 Verify When 正式流程 bundled：看见step 1 在调 VerifyVoteExtension 之前，不是已经 Verify When 正式流程 bundled interchangeable / 1327 vwdisc-notstep interchangeable。**
- **step 1 before call 不是已经验过扩展：看见step 1 before call，不是已经验过扩展 interchangeable / 1327 vwdisc-notstep interchangeable。**
- **step 1 在调 VerifyVoteExtension 之前 不是已经写进 last_commit：看见step 1 在调 VerifyVoteExtension 之前，不是已经写进 last_commit interchangeable / 1327 vwdisc-notstep interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事（514 余量），必须分开 not already Verify-When-bundled、not already still-calls-Verify、not already verified 三件事。
