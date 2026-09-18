# 反模式：把 InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量） 写成已经 已经是崩溃后再调 / 已经能跳步 / 已经过了 genesis_time

**层次**：实现 / InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应**：[`../tracks/implementation/worked-example-ionce-notcrash-vs-bundled.md`](../tracks/implementation/worked-example-ionce-notcrash-vs-bundled.md)。

把 InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量） 写成已经 已经是崩溃后再调 / 已经能跳步 / 已经过了 genesis_time，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 once-at-genesis 正式三事（412 余量），必须分开 not already crash-recall、not already skip-step、not already past-genesis 三件事，不要和 412 / 320 / 303 / 1092 / 1093 糊成一句。

也不是：

- [vreqh-notskip-sold-as-bundled](vreqh-notskip-sold-as-bundled.md) 是 Verify vote_extension 仍未跳过 Verify 边界（415/1090），不是本页 InitChain 创世只调一次仍未是崩溃后再调边界。
- 崩溃后第一块 Commit 之前再调 InitChain 就已经交差是不变量 320，不是本页调了一次仍未能跳步边界。
