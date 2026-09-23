# 模式：把非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[非验证者可以立刻回 ACCEPT not already verified ≠ bundled（354）](../../tracks/implementation/worked-example-nonval-notverified-vs-bundled.md)。

## 三个名字

1. **立刻 ACCEPT 不是 already verified：** 看见非验证者可以立刻回 `ACCEPT` / 立刻 `ACCEPT` / 立刻回了 ACCEPT，不是已经验过这块 interchangeable / 已经 verified interchangeable / 已经验过交差 interchangeable，不是 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable。

2. **不是验证者 不是 already settled：** 看见不是验证者 / *p* 不是验证者 / 非验证者，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 33 fourgates interchangeable / 816 async-notreject interchangeable。

3. **规范允许 不是 already processalso：** 看见规范允许 / 可以立刻回 / 不想让非验证者处理，不是已经是提议者那边也会叫 Process interchangeable / 已经 processalso interchangeable / 已经 processalso 交差 interchangeable，不是 815 sync-notlater interchangeable / 351 processalso interchangeable。

官方把立刻 ACCEPT、不是已经交差、不是已经是提议者那边也会叫 Process 写成三个名字。把它们叫成一个「看见立刻 ACCEPT 就已经验过这块 interchangeable / 就已经交差 interchangeable / 就已经是提议者那边也会叫 Process interchangeable」，会把 not already verified、not already settled、not already processalso 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量），先数清问的是立刻 ACCEPT 是不是 already verified / 354 / processwhen-sold-as-later，是不是不是验证者 是不是 already settled，还是规范允许 是不是 already processalso，再决定要不要同一次发布。354 processwhen vs later bundled unbundling 在本页 item 3 完成。
