# 模式：点名 vwstat-notafter 杠

**层次**：实现 / VerifyStatusWhen after-call not already step-2-call / not already step-1-discard / not already late-MAY 正式三事（516 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应**：[`../tracks/implementation/worked-example-vwstat-notafter-vs-bundled.md`](../tracks/implementation/worked-example-vwstat-notafter-vs-bundled.md)。

- **step 3 在 call VerifyVoteExtension 之后 不是已经 step 2 call bundled：看见step 3 在 call VerifyVoteExtension 之后，不是已经 step 2 call bundled interchangeable / 1332 vwstat-notafter interchangeable。**
- **step 3 after call 不是已经 CometBFT 会叫：看见step 3 after call，不是已经 CometBFT 会叫 interchangeable / 1332 vwstat-notafter interchangeable。**
- **step 3 在 call VerifyVoteExtension 之后 不是已经 step 1 discard bundled：看见step 3 在 call VerifyVoteExtension 之后，不是已经 step 1 discard bundled interchangeable / 1332 vwstat-notafter interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事（516 余量），必须分开 not already Verify-When-bundled、not already step-2-call、not already keep-discard 三件事。
