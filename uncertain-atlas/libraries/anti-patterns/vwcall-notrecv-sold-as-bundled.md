# 反模式：把 VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事（515 余量） 写成已经 已经 Verify 不对 local process 调用 bundled / 已经本地票也 Verify / 已经 round 0 height h MAY add without calling Verify

**层次**：实现 / VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事（515 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应**：[`../tracks/implementation/worked-example-vwcall-notrecv-vs-bundled.md`](../tracks/implementation/worked-example-vwcall-notrecv-vs-bundled.md)。

把 VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事（515 余量） 写成已经 已经 Verify 不对 local process 调用 bundled / 已经本地票也 Verify / 已经 round 0 height h MAY add without calling Verify，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事（515 余量），必须分开 not already Verify-When-bundled、not already local-also-Verify、not already Accept 三件事，不要和 515 / 353 / 352 / 1328 / 1330 糊成一句。

也不是：

- [vwcall-notcall-sold-as-bundled](vwcall-notcall-sold-as-bundled.md) 是 notcall 单句边界（1328），不是本页边界。
- [vwcall-notbefore-sold-as-bundled](vwcall-notbefore-sold-as-bundled.md) 是 notbefore 单句边界（1330），不是本页边界。
- [vwdisc-notstep-sold-as-bundled](vwdisc-notstep-sold-as-bundled.md) 是 VerifyDiscard step 1 在 call 前仍未是已经验过边界（514/1327），不是本页 step 2 call 边界。
