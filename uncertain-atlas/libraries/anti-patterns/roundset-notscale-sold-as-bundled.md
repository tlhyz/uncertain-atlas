# 反模式：把 优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事（302 余量） 写成已经 已经按人头轮 / 已经没有优先级 / 已经每人一轮

**层次**：共识 / 优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事（302 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应**：[`../tracks/consensus/worked-example-roundset-notscale-vs-bundled.md`](../tracks/consensus/worked-example-roundset-notscale-vs-bundled.md)。

把 优先级差被缩放 not already per-head / not already no-priority / not already equal 正式三事（302 余量） 写成已经 已经按人头轮 / 已经没有优先级 / 已经每人一轮，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级差被缩放 正式三事（302 余量），必须分开 not already per-head、not already no-priority、not already equal 三件事，不要和 302 / 129 / 318 / 995 / 996 糊成一句。

也不是：

- [roundset-notjump-sold-as-bundled](roundset-notjump-sold-as-bundled.md) 是新加入仍未能跳队头单句边界（996 item 2），不是本页缩放仍未按人头轮边界。
- NPoS 当选已经按质押计票是不变量 129，不是本页范围被压住仍未没有优先级边界。
