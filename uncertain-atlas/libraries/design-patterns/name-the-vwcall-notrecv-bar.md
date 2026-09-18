# 模式：点名 vwcall-notrecv 杠

**层次**：实现 / VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事（515 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应**：[`../tracks/implementation/worked-example-vwcall-notrecv-vs-bundled.md`](../tracks/implementation/worked-example-vwcall-notrecv-vs-bundled.md)。

- **收到他人 Precommit 不是已经 Verify 不对 local process 调用 bundled：看见收到他人 Precommit，不是已经 Verify 不对 local process 调用 bundled interchangeable / 1329 vwcall-notrecv interchangeable。**
- **received from q≠p 不是已经本地票也 Verify：看见received from q≠p，不是已经本地票也 Verify interchangeable / 1329 vwcall-notrecv interchangeable。**
- **收到他人 Precommit 不是已经 round 0 height h MAY add without calling Verify：看见收到他人 Precommit，不是已经 round 0 height h MAY add without calling Verify interchangeable / 1329 vwcall-notrecv interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事（515 余量），必须分开 not already Verify-When-bundled、not already local-also-Verify、not already Accept 三件事。
