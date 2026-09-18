# 反模式：把 VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事（517 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经写进 last_commit / 已经 +2/3 之后才进来的扩展写进了 commit info

**层次**：实现 / VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事（517 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应**：[`../tracks/implementation/worked-example-vwkeep-notkeep-vs-bundled.md`](../tracks/implementation/worked-example-vwkeep-notkeep-vs-bundled.md)。

把 VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事（517 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经写进 last_commit / 已经 +2/3 之后才进来的扩展写进了 commit info，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事（517 余量），必须分开 not already Verify-When-bundled、not already last_commit、not already step-1-discard 三件事，不要和 517 / 435 / 352 / 1335 / 1336 糊成一句。

也不是：

- [vwkeep-notpop-sold-as-bundled](vwkeep-notpop-sold-as-bundled.md) 是 notpop 单句边界（1335），不是本页边界。
- [vwkeep-notrej-sold-as-bundled](vwkeep-notrej-sold-as-bundled.md) 是 notrej 单句边界（1336），不是本页边界。
- [vwstat-notkeep-sold-as-bundled](vwstat-notkeep-sold-as-bundled.md) 是 VerifyStatusWhen step 3 在 keep 前仍未是已经写进 last_commit 边界（516/1333），不是本页 step 4 keep/discard 边界。
