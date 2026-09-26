# 模式：把 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[填了目标 not already history ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-nothistory-vs-bundled.md)。

## 三个名字

1. **填了目标 不是 already history：** 看见填了目标 / syncing_to_height 同步或重放时是目标高、否则等于本高 / 填了 syncing_to_height，不是已经有完整历史 interchangeable / 已经 history interchangeable / 已经有从创世的完整历史交差 interchangeable，不是 382 syncingheight bundled interchangeable / syncingheight-sold-as-history interchangeable。

2. **在同步 不是 already restored：** 看见在同步 / 在同步或重放 / 正在追目标高，不是已经是快照重放 interchangeable / 已经 restored interchangeable / 已经是快照重放交差 interchangeable，不是 323 transition interchangeable / 321 offerrestored interchangeable。

3. **等于本高 不是 already settled：** 看见等于本高 / syncing_to_height 等于本高 / 目标就是本高，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 316 txresults interchangeable / 382 syncingheight item 2 interchangeable。

官方把填了目标、不是已经是快照重放、不是已经交差写成三个名字。把它们叫成一个「看见填了目标就已经有完整历史 interchangeable / 就已经是快照重放 interchangeable / 就已经交差 interchangeable」，会把 not already history、not already restored、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 余量），先数清问的是填了目标 是不是 already history / 382 / syncingheight-sold-as-history，是不是在同步 是不是 already restored，还是等于本高 是不是 already settled，再决定要不要同一次发布。382 syncingheight-vs-history bundled unbundling 在本页 item 1 启动。
