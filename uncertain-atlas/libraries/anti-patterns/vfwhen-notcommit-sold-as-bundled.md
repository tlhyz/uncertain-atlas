# 反模式：把 ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量） 写成已经 已经写进 last_commit / 已经 Verify 过迟到扩展 / 已经当成块非法

**层次**：实现 / ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-vfwhen-notcommit-vs-bundled.md`](../tracks/implementation/worked-example-vfwhen-notcommit-vs-bundled.md)。

把 ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量） 写成已经 已经写进 last_commit / 已经 Verify 过迟到扩展 / 已经当成块非法，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT/REJECT 正式三事（435 余量），必须分开 not already last-commit、not already late-verified、not already block-invalid 三件事，不要和 435 / 352 / 409 / 1085 / 1086 糊成一句。

也不是：

- [vfwhen-notverif-sold-as-bundled](vfwhen-notverif-sold-as-bundled.md) 是会叫 Verify 仍未验过扩展单句边界（1086 item 2），不是本页 ACCEPT/REJECT 仍未写进 last_commit 边界。
- +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过是不变量 352，不是本页留给下一高仍未迟到已验边界。
