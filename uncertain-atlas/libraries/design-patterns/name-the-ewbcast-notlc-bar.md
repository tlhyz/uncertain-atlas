# 模式：点名 ewbcast-notlc 杠

**层次**：实现 / ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事（513 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应**：[`../tracks/implementation/worked-example-ewbcast-notlc-vs-bundled.md`](../tracks/implementation/worked-example-ewbcast-notlc-vs-bundled.md)。

- **广播了不是已经写进 last_commit 不是已经写进 last_commit：看见广播了不是已经写进 last_commit，不是已经写进 last_commit interchangeable / 1345 ewbcast-notlc interchangeable。**
- **broadcasts is not write into last_commit 不是已经 Verify 过迟到扩展：看见broadcasts is not write into last_commit，不是已经 Verify 过迟到扩展 interchangeable / 1345 ewbcast-notlc interchangeable。**
- **广播了不是已经写进 last_commit 不是已经 ExtendVote When 正式流程 bundled：看见广播了不是已经写进 last_commit，不是已经 ExtendVote When 正式流程 bundled interchangeable / 1345 ewbcast-notlc interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（513 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
