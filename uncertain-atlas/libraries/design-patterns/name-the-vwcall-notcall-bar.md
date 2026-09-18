# 模式：点名 vwcall-notcall 杠

**层次**：实现 / VerifyCall call not already Verify-When / not already verified / not already Accept 正式三事（515 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应**：[`../tracks/implementation/worked-example-vwcall-notcall-vs-bundled.md`](../tracks/implementation/worked-example-vwcall-notcall-vs-bundled.md)。

- **带有效签就会调 VerifyVoteExtension 不是已经 Verify When 正式流程 bundled：看见带有效签就会调 VerifyVoteExtension，不是已经 Verify When 正式流程 bundled interchangeable / 1328 vwcall-notcall interchangeable。**
- **calls VerifyVoteExtension 不是已经验过扩展：看见calls VerifyVoteExtension，不是已经验过扩展 interchangeable / 1328 vwcall-notcall interchangeable。**
- **带有效签就会调 VerifyVoteExtension 不是已经 Accept：看见带有效签就会调 VerifyVoteExtension，不是已经 Accept interchangeable / 1328 vwcall-notcall interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事（515 余量），必须分开 not already Verify-When-bundled、not already local-also-Verify、not already Accept 三件事。
