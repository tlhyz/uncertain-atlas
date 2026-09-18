# 反模式：把 PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事（505 余量） 写成已经 已经能在返回之后再改裁决 / 已经离开关键路径 / 已经 Process 调用是同步的

**层次**：实现 / PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事（505 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应**：[`../tracks/implementation/worked-example-prepwhen-notsync-vs-bundled.md`](../tracks/implementation/worked-example-prepwhen-notsync-vs-bundled.md)。

把 PrepareWhen sync not already can-change-after-return / not already left-critical-path / not already Process-sync 正式三事（505 余量） 写成已经 已经能在返回之后再改裁决 / 已经离开关键路径 / 已经 Process 调用是同步的，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事（505 余量），必须分开 not already raw-proposal、not already can-change-after-return、not already Prepare-list 三件事，不要和 505 / 354 / 327 / 1310 / 1312 糊成一句。

也不是：

- [prepwhen-notprio-sold-as-bundled](prepwhen-notprio-sold-as-bundled.md) 是 notprio 单句边界（1310），不是本页边界。
- [prepwhen-notmanip-sold-as-bundled](prepwhen-notmanip-sold-as-bundled.md) 是 notmanip 单句边界（1312），不是本页边界。
- [nochecks-notdet-sold-as-bundled](nochecks-notdet-sold-as-bundled.md) 是 PrepareNochecks MAY 非确定仍未是必须确定边界（504/1309），不是本页 PrepareWhen 边界。
