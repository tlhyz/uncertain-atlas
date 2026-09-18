# 反模式：把 VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事（514 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经验过扩展 / 已经写进 last_commit

**层次**：实现 / VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事（514 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应**：[`../tracks/implementation/worked-example-vwdisc-notstep-vs-bundled.md`](../tracks/implementation/worked-example-vwdisc-notstep-vs-bundled.md)。

把 VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事（514 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经验过扩展 / 已经写进 last_commit，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事（514 余量），必须分开 not already Verify-When-bundled、not already still-calls-Verify、not already verified 三件事，不要和 514 / 435 / 352 / 1325 / 1326 糊成一句。

也不是：

- [vwdisc-notsig-sold-as-bundled](vwdisc-notsig-sold-as-bundled.md) 是 notsig 单句边界（1325），不是本页边界。
- [vwdisc-notzero-sold-as-bundled](vwdisc-notzero-sold-as-bundled.md) 是 notzero 单句边界（1326），不是本页边界。
- [latemay-notcall-sold-as-bundled](latemay-notcall-sold-as-bundled.md) 是 LateMay 不再叫 Verify 仍未是已经 Verify 过边界（518/1324），不是本页 step 1 discard 边界。
