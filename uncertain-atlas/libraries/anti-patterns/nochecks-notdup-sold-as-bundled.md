# 反模式：把 PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事（504 余量） 写成已经 已经验过重复 / 已经有应用级重放保护 / 已经内存池去重就已经保证不重放

**层次**：实现 / PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事（504 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-nochecks-notdup-vs-bundled.md`](../tracks/implementation/worked-example-nochecks-notdup-vs-bundled.md)。

把 PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事（504 余量） 写成已经 已经验过重复 / 已经有应用级重放保护 / 已经内存池去重就已经保证不重放，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事（504 余量），必须分开 not already checked-dup、not already Process-REJECT、not already must-deterministic 三件事，不要和 504 / 357 / 313 / 1308 / 1309 糊成一句。

也不是：

- [nochecks-notcrash-sold-as-bundled](nochecks-notcrash-sold-as-bundled.md) 是 notcrash 单句边界（1308），不是本页边界。
- [nochecks-notdet-sold-as-bundled](nochecks-notdet-sold-as-bundled.md) 是 notdet 单句边界（1309），不是本页边界。
- [prepusage-notmust-sold-as-bundled](prepusage-notmust-sold-as-bundled.md) 是 PrepareUsage MUST remove 仍未是引擎会帮你裁边界（503/1306），不是本页 PrepareNochecks 边界。
