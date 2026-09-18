# 反模式：把 Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量） 写成已经 已经跳过 Verify / 已经验过扩展 / 已经 Accept

**层次**：实现 / Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-vfwhen-notskip-vs-bundled.md`](../tracks/implementation/worked-example-vfwhen-notskip-vs-bundled.md)。

把 Precommit unsigned discard not already skip-verify / not already verified / not already accept 正式三事（435 余量） 写成已经 已经跳过 Verify / 已经验过扩展 / 已经 Accept，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 unsigned discard 正式三事（435 余量），必须分开 not already skip-verify、not already verified、not already accept 三件事，不要和 435 / 353 / 409 / 1086 / 1087 糊成一句。

也不是：

- [eresp-nottable-sold-as-bundled](eresp-nottable-sold-as-bundled.md) 是 Verify non_rp 仍未是 vote_extension 表边界（418/1084），不是本页 unsigned discard 仍未跳过 Verify 边界。
- 空扩展仍会调 Verify 就已经跳过 Verify 是不变量 353，不是本页没调 Verify 仍未验过扩展边界。
