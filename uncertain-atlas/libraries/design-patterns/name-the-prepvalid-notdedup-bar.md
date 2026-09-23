# 模式：把引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[引擎没有再验重复交易 not already dedup-checked ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notdedup-vs-bundled.md)。

## 三个名字

1. **回了提案 不是 already dedup-checked：** 看见引擎没有再验重复交易 / 回了提案 / 没有再做额外有效性检查，不是已经验过重复 interchangeable / 已经 dedup-checked interchangeable / 已经验过重复交差 interchangeable，不是 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable。

2. **能提 不是 already app-replay：** 看见能提 / 回了提案 / 没有再验，不是已经有应用级重放保护 interchangeable / 已经 app-replay interchangeable / 已经有应用级重放保护交差 interchangeable，不是 313 indexer interchangeable / 825 prepvalid-notreject interchangeable。

3. **没有再验 不是 already settled：** 看见没有再验 / 引擎没有再验 / 没有再做额外检查，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 826 prepvalid-notfinalize interchangeable / 33 fourgates interchangeable。

官方把回了提案、不是已经有应用级重放保护、不是已经交差写成三个名字。把它们叫成一个「看见回了提案就已经验过重复 interchangeable / 就已经有应用级重放保护 interchangeable / 就已经交差 interchangeable」，会把 not already dedup-checked、not already app-replay、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量），先数清问的是回了提案 是不是 already dedup-checked / 357 / preparevalid-sold-as-checked，是不是能提 是不是 already app-replay，还是没有再验 是不是 already settled，再决定要不要同一次发布。357 prepare-valid vs checked bundled unbundling 在本页 item 1 启动。
