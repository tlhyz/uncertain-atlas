# 反模式：把 PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事（504 余量） 写成已经 已经必须确定 / 已经和 Process / Finalize 同一把尺 / 已经 Process MUST deterministic

**层次**：实现 / PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事（504 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-nochecks-notdet-vs-bundled.md`](../tracks/implementation/worked-example-nochecks-notdet-vs-bundled.md)。

把 PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事（504 余量） 写成已经 已经必须确定 / 已经和 Process / Finalize 同一把尺 / 已经 Process MUST deterministic，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事（504 余量），必须分开 not already checked-dup、not already Process-REJECT、not already must-deterministic 三件事，不要和 504 / 338 / 430 / 1307 / 1308 糊成一句。

也不是：

- [nochecks-notdup-sold-as-bundled](nochecks-notdup-sold-as-bundled.md) 是 notdup 单句边界（1307），不是本页边界。
- [nochecks-notcrash-sold-as-bundled](nochecks-notcrash-sold-as-bundled.md) 是 notcrash 单句边界（1308），不是本页边界。
- [prepusage-notmust-sold-as-bundled](prepusage-notmust-sold-as-bundled.md) 是 PrepareUsage MUST remove 仍未是引擎会帮你裁边界（503/1306），不是本页 PrepareNochecks 边界。
