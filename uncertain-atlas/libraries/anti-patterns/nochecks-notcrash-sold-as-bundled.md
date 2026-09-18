# 反模式：把 PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事（504 余量） 写成已经 已经是 Process REJECT / 已经是正确提议者必须被 Accept / 已经 ProposalStatus REJECT

**层次**：实现 / PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事（504 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-nochecks-notcrash-vs-bundled.md`](../tracks/implementation/worked-example-nochecks-notcrash-vs-bundled.md)。

把 PrepareNochecks crash not already Process-REJECT / not already must-Accept / not already ProposalStatus-REJECT 正式三事（504 余量） 写成已经 已经是 Process REJECT / 已经是正确提议者必须被 Accept / 已经 ProposalStatus REJECT，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事（504 余量），必须分开 not already checked-dup、not already Process-REJECT、not already must-deterministic 三件事，不要和 504 / 455 / 347 / 1307 / 1309 糊成一句。

也不是：

- [nochecks-notdup-sold-as-bundled](nochecks-notdup-sold-as-bundled.md) 是 notdup 单句边界（1307），不是本页边界。
- [nochecks-notdet-sold-as-bundled](nochecks-notdet-sold-as-bundled.md) 是 notdet 单句边界（1309），不是本页边界。
- [prepusage-notmust-sold-as-bundled](prepusage-notmust-sold-as-bundled.md) 是 PrepareUsage MUST remove 仍未是引擎会帮你裁边界（503/1306），不是本页 PrepareNochecks 边界。
