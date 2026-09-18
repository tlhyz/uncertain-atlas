# 模式：点名 latemay-notround 杠

**层次**：实现 / LateMay round0-h-1 not already normal-When / not already this-height / not already ExtendVote-When 正式三事（518 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When late-arriving MAY 段。  
**对应**：[`../tracks/implementation/worked-example-latemay-notround-vs-bundled.md`](../tracks/implementation/worked-example-latemay-notround-vs-bundled.md)。

- **round 0 height h 收到上一高度 CommitRound 的 Precommit 不是已经 Verify When 正式流程 bundled：看见round 0 height h 收到上一高度 CommitRound 的 Precommit，不是已经 Verify When 正式流程 bundled interchangeable / 1323 latemay-notround interchangeable。**
- **round 0 / h-1 / CommitRound 不是已经 round r height h：看见round 0 / h-1 / CommitRound，不是已经 round r height h interchangeable / 1323 latemay-notround interchangeable。**
- **round 0 height h 收到上一高度 CommitRound 的 Precommit 不是已经 ExtendVote When 正式流程 bundled：看见round 0 height h 收到上一高度 CommitRound 的 Precommit，不是已经 ExtendVote When 正式流程 bundled interchangeable / 1323 latemay-notround interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When late-arriving MAY add without Verify 正式三事（518 余量），必须分开 not already 352-bundled、not already normal-When、not already called-Verify 三件事。
