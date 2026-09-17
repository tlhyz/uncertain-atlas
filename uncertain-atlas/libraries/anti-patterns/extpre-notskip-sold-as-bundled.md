# 反模式：把 Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量） 写成已经 已经跳过 Verify / 已经没有签 / 已经自己验过

**层次**：实现 / Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-extpre-notskip-vs-bundled.md`](../tracks/implementation/worked-example-extpre-notskip-vs-bundled.md)。

把 Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量） 写成已经 已经跳过 Verify / 已经没有签 / 已经自己验过，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉无有效签扩展 正式三事（409 余量），必须分开 not already skip-verify、not already unsigned、not already self-verified 三件事，不要和 409 / 353 / 352 / 1031 / 1033 糊成一句。

也不是：

- [extpre-notcall-sold-as-bundled](extpre-notcall-sold-as-bundled.md) 是请求对应仍未会调单句边界（1031 item 1），不是本页丢掉仍未跳过 Verify 边界。
- 空扩展仍会调 Verify 就已经跳过 Verify 是不变量 353，不是本页空扩展仍未没有签边界。
