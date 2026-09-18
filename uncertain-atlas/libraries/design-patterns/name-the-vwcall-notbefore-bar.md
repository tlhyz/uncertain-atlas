# 模式：点名 vwcall-notbefore 杠

**层次**：实现 / VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事（515 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应**：[`../tracks/implementation/worked-example-vwcall-notbefore-vs-bundled.md`](../tracks/implementation/worked-example-vwcall-notbefore-vs-bundled.md)。

- **step 2 在应用回 status 之前 不是已经 Verify When 正式流程 bundled：看见step 2 在应用回 status 之前，不是已经 Verify When 正式流程 bundled interchangeable / 1330 vwcall-notbefore interchangeable。**
- **step 2 before status return 不是已经写进 last_commit：看见step 2 before status return，不是已经写进 last_commit interchangeable / 1330 vwcall-notbefore interchangeable。**
- **step 2 在应用回 status 之前 不是已经 VerifyVoteExtensionResponse.status bundled：看见step 2 在应用回 status 之前，不是已经 VerifyVoteExtensionResponse.status bundled interchangeable / 1330 vwcall-notbefore interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事（515 余量），必须分开 not already Verify-When-bundled、not already local-also-Verify、not already Accept 三件事。
