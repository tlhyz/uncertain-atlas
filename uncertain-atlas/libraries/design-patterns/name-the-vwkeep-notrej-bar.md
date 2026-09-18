# 模式：点名 vwkeep-notrej 杠

**层次**：实现 / VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事（517 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应**：[`../tracks/implementation/worked-example-vwkeep-notrej-vs-bundled.md`](../tracks/implementation/worked-example-vwkeep-notrej-vs-bundled.md)。

- **REJECT 会把 Precommit 当非法丢掉 不是已经 Verify When 正式流程 bundled：看见REJECT 会把 Precommit 当非法丢掉，不是已经 Verify When 正式流程 bundled interchangeable / 1336 vwkeep-notrej interchangeable。**
- **REJECT discard Precommit 不是已经 step 1 discard bundled：看见REJECT discard Precommit，不是已经 step 1 discard bundled interchangeable / 1336 vwkeep-notrej interchangeable。**
- **REJECT 会把 Precommit 当非法丢掉 不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法：看见REJECT 会把 Precommit 当非法丢掉，不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法 interchangeable / 1336 vwkeep-notrej interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事（517 余量），必须分开 not already Verify-When-bundled、not already last_commit、not already step-1-discard 三件事。
