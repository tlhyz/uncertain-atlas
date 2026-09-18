# 模式：点名 vwstat-notkeep 杠

**层次**：实现 / VerifyStatusWhen before-keep not already Verify-When / not already ACCEPT-keep / not already REJECT-discard 正式三事（516 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应**：[`../tracks/implementation/worked-example-vwstat-notkeep-vs-bundled.md`](../tracks/implementation/worked-example-vwstat-notkeep-vs-bundled.md)。

- **step 3 在 keep 或 discard 之前 不是已经 Verify When 正式流程 bundled：看见step 3 在 keep 或 discard 之前，不是已经 Verify When 正式流程 bundled interchangeable / 1333 vwstat-notkeep interchangeable。**
- **step 3 before keep/discard 不是已经写进 last_commit：看见step 3 before keep/discard，不是已经写进 last_commit interchangeable / 1333 vwstat-notkeep interchangeable。**
- **step 3 在 keep 或 discard 之前 不是已经 ACCEPT 留给 h+1 Prepare bundled：看见step 3 在 keep 或 discard 之前，不是已经 ACCEPT 留给 h+1 Prepare bundled interchangeable / 1333 vwstat-notkeep interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事（516 余量），必须分开 not already Verify-When-bundled、not already step-2-call、not already keep-discard 三件事。
