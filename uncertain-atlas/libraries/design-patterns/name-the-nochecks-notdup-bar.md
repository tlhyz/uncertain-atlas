# 模式：点名 nochecks-notdup 杠

**层次**：实现 / PrepareNochecks nocheck not already checked-dup / not already app-replay / not already pool-dedup 正式三事（504 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-nochecks-notdup-vs-bundled.md`](../tracks/implementation/worked-example-nochecks-notdup-vs-bundled.md)。

- **引擎不再做额外有效性检查 不是已经验过重复：看见引擎不再做额外有效性检查，不是已经验过重复 interchangeable / 1307 nochecks-notdup interchangeable。**
- **不再查重复交易 不是已经有应用级重放保护：看见不再查重复交易，不是已经有应用级重放保护 interchangeable / 1307 nochecks-notdup interchangeable。**
- **引擎不再做额外有效性检查 不是已经内存池去重就已经保证不重放：看见引擎不再做额外有效性检查，不是已经内存池去重就已经保证不重放 interchangeable / 1307 nochecks-notdup interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事（504 余量），必须分开 not already checked-dup、not already Process-REJECT、not already must-deterministic 三件事。
