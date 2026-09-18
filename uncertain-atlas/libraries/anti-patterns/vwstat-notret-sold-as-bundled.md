# 反模式：把 VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事（516 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经验过扩展 / 已经 VerifyVoteExtensionResponse.status bundled

**层次**：实现 / VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事（516 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应**：[`../tracks/implementation/worked-example-vwstat-notret-vs-bundled.md`](../tracks/implementation/worked-example-vwstat-notret-vs-bundled.md)。

把 VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事（516 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经验过扩展 / 已经 VerifyVoteExtensionResponse.status bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事（516 余量），必须分开 not already Verify-When-bundled、not already step-2-call、not already keep-discard 三件事，不要和 516 / 435 / 433 / 1332 / 1333 糊成一句。

也不是：

- [vwstat-notafter-sold-as-bundled](vwstat-notafter-sold-as-bundled.md) 是 notafter 单句边界（1332），不是本页边界。
- [vwstat-notkeep-sold-as-bundled](vwstat-notkeep-sold-as-bundled.md) 是 notkeep 单句边界（1333），不是本页边界。
- [vwcall-notbefore-sold-as-bundled](vwcall-notbefore-sold-as-bundled.md) 是 VerifyCall step 2 在回 status 前仍未是已经 Accept 边界（515/1330），不是本页 step 3 return 边界。
