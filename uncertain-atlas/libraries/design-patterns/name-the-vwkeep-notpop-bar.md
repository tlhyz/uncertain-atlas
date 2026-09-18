# 模式：点名 vwkeep-notpop 杠

**层次**：实现 / VerifyKeep h+1-Prepare not already last_commit / not already in-block / not already same-path 正式三事（517 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应**：[`../tracks/implementation/worked-example-vwkeep-notpop-vs-bundled.md`](../tracks/implementation/worked-example-vwkeep-notpop-vs-bundled.md)。

- **用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify When 正式流程 bundled：看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo，不是已经 Verify When 正式流程 bundled interchangeable / 1335 vwkeep-notpop interchangeable。**
- **populate ExtendedCommitInfo in h+1 Prepare 不是已经写进 last_commit：看见populate ExtendedCommitInfo in h+1 Prepare，不是已经写进 last_commit interchangeable / 1335 vwkeep-notpop interchangeable。**
- **用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 ExtendedCommitInfo 就已经进了块：看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo，不是已经 ExtendedCommitInfo 就已经进了块 interchangeable / 1335 vwkeep-notpop interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事（517 余量），必须分开 not already Verify-When-bundled、not already last_commit、not already step-1-discard 三件事。
