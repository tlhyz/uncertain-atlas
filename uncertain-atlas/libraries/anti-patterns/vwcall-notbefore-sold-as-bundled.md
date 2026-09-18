# 反模式：把 VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事（515 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经写进 last_commit / 已经 VerifyVoteExtensionResponse.status bundled

**层次**：实现 / VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事（515 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应**：[`../tracks/implementation/worked-example-vwcall-notbefore-vs-bundled.md`](../tracks/implementation/worked-example-vwcall-notbefore-vs-bundled.md)。

把 VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事（515 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经写进 last_commit / 已经 VerifyVoteExtensionResponse.status bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事（515 余量），必须分开 not already Verify-When-bundled、not already local-also-Verify、not already Accept 三件事，不要和 515 / 435 / 433 / 1328 / 1329 糊成一句。

也不是：

- [vwcall-notcall-sold-as-bundled](vwcall-notcall-sold-as-bundled.md) 是 notcall 单句边界（1328），不是本页边界。
- [vwcall-notrecv-sold-as-bundled](vwcall-notrecv-sold-as-bundled.md) 是 notrecv 单句边界（1329），不是本页边界。
- [vwdisc-notstep-sold-as-bundled](vwdisc-notstep-sold-as-bundled.md) 是 VerifyDiscard step 1 在 call 前仍未是已经验过边界（514/1327），不是本页 step 2 call 边界。
