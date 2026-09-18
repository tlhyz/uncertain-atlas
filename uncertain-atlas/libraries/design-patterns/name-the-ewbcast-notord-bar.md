# 模式：点名 ewbcast-notord 杠

**层次**：实现 / ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事（513 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应**：[`../tracks/implementation/worked-example-ewbcast-notord-vs-bundled.md`](../tracks/implementation/worked-example-ewbcast-notord-vs-bundled.md)。

- **step 7 在 step 6 之后不是已经 construct CanonicalVote 不是已经 construct CanonicalVote bundled：看见step 7 在 step 6 之后不是已经 construct CanonicalVote，不是已经 construct CanonicalVote bundled interchangeable / 1344 ewbcast-notord interchangeable。**
- **step 7 after step 6 is not construct CanonicalVote 不是已经 fill CanonicalVoteExtension bundled：看见step 7 after step 6 is not construct CanonicalVote，不是已经 fill CanonicalVoteExtension bundled interchangeable / 1344 ewbcast-notord interchangeable。**
- **step 7 在 step 6 之后不是已经 construct CanonicalVote 不是已经 Verify 过扩展：看见step 7 在 step 6 之后不是已经 construct CanonicalVote，不是已经 Verify 过扩展 interchangeable / 1344 ewbcast-notord interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（513 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
