# 模式：点名 vwstat-notret 杠

**层次**：实现 / VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事（516 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应**：[`../tracks/implementation/worked-example-vwstat-notret-vs-bundled.md`](../tracks/implementation/worked-example-vwstat-notret-vs-bundled.md)。

- **应用回 status 不是已经 Verify When 正式流程 bundled：看见应用回 status，不是已经 Verify When 正式流程 bundled interchangeable / 1331 vwstat-notret interchangeable。**
- **returns ACCEPT or REJECT 不是已经验过扩展：看见returns ACCEPT or REJECT，不是已经验过扩展 interchangeable / 1331 vwstat-notret interchangeable。**
- **应用回 status 不是已经 VerifyVoteExtensionResponse.status bundled：看见应用回 status，不是已经 VerifyVoteExtensionResponse.status bundled interchangeable / 1331 vwstat-notret interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事（516 余量），必须分开 not already Verify-When-bundled、not already step-2-call、not already keep-discard 三件事。
