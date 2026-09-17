# 反模式：把 Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量） 写成已经 已经 Verify 过迟到扩展 / 已经交差 / 已经必须再 Verify

**层次**：实现 / Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-extpre-notlate-vs-bundled.md`](../tracks/implementation/worked-example-extpre-notlate-vs-bundled.md)。

把 Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量） 写成已经 已经 Verify 过迟到扩展 / 已经交差 / 已经必须再 Verify，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT 留给 h+1 正式三事（409 余量），必须分开 not already late-verified、not already settled、not already must-reverify 三件事，不要和 409 / 352 / 353 / 1031 / 1032 糊成一句。

也不是：

- [extpre-notskip-sold-as-bundled](extpre-notskip-sold-as-bundled.md) 是丢掉仍未跳过 Verify 单句边界（1032 item 2），不是本页 ACCEPT 仍未 Verify 过迟到扩展边界。
- +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过是不变量 352，不是本页留给下一高仍未交差边界。
