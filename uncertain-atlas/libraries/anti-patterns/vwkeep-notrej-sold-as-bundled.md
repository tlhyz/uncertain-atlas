# 反模式：把 VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事（517 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经 step 1 discard bundled / 已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法

**层次**：实现 / VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事（517 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应**：[`../tracks/implementation/worked-example-vwkeep-notrej-vs-bundled.md`](../tracks/implementation/worked-example-vwkeep-notrej-vs-bundled.md)。

把 VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事（517 余量） 写成已经 已经 Verify When 正式流程 bundled / 已经 step 1 discard bundled / 已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事（517 余量），必须分开 not already Verify-When-bundled、not already last_commit、not already step-1-discard 三件事，不要和 517 / 514 / 433 / 1334 / 1335 糊成一句。

也不是：

- [vwkeep-notkeep-sold-as-bundled](vwkeep-notkeep-sold-as-bundled.md) 是 notkeep 单句边界（1334），不是本页边界。
- [vwkeep-notpop-sold-as-bundled](vwkeep-notpop-sold-as-bundled.md) 是 notpop 单句边界（1335），不是本页边界。
- [vwstat-notkeep-sold-as-bundled](vwstat-notkeep-sold-as-bundled.md) 是 VerifyStatusWhen step 3 在 keep 前仍未是已经写进 last_commit 边界（516/1333），不是本页 step 4 keep/discard 边界。
