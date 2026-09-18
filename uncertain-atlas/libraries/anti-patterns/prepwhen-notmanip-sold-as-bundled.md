# 反模式：把 PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事（505 余量） 写成已经 已经 Prepare 改列表 bundled / 已经候选已经是 ExecuteTxState / 已经 +2/3 之后才进来的扩展

**层次**：实现 / PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事（505 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应**：[`../tracks/implementation/worked-example-prepwhen-notmanip-vs-bundled.md`](../tracks/implementation/worked-example-prepwhen-notmanip-vs-bundled.md)。

把 PrepareWhen manip not already Prepare-list / not already ExecuteTxState / not already late-ext 正式三事（505 余量） 写成已经 已经 Prepare 改列表 bundled / 已经候选已经是 ExecuteTxState / 已经 +2/3 之后才进来的扩展，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事（505 余量），必须分开 not already raw-proposal、not already can-change-after-return、not already Prepare-list 三件事，不要和 505 / 355 / 311 / 1310 / 1311 糊成一句。

也不是：

- [prepwhen-notprio-sold-as-bundled](prepwhen-notprio-sold-as-bundled.md) 是 notprio 单句边界（1310），不是本页边界。
- [prepwhen-notsync-sold-as-bundled](prepwhen-notsync-sold-as-bundled.md) 是 notsync 单句边界（1311），不是本页边界。
- [nochecks-notdet-sold-as-bundled](nochecks-notdet-sold-as-bundled.md) 是 PrepareNochecks MAY 非确定仍未是必须确定边界（504/1309），不是本页 PrepareWhen 边界。
