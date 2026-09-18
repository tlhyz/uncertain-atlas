# 模式：把丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[丢掉候选 not already can unboundedly accumulate ≠ bundled（311）](../../tracks/implementation/worked-example-candidate-notdiscarded-vs-bundled.md)。

## 三个名字

1. **还没 Finalize 不是 already can unboundedly accumulate：** 看见候选很多 / 一轮高度披露很多提案，不是已经能无界攒着 interchangeable / 已经能一直攒 interchangeable，不是 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable。

2. **丢掉了 不是 already never need re-execute：** 看见 Finalize 之前丢掉候选 / 丢了内存里那份，不是已经永远不用再跑 interchangeable / 已经永远不用再执行 interchangeable，不是 311 candidate item 2 interchangeable / 693 candidate-notexecute interchangeable。

3. **看见有上界 不是 already bound by spec：** 看见自己限制了内存 / 开发者设了候选上限，不是规范已经写死条数 interchangeable / 已经协议写死上界 interchangeable，不是 5 half-write atomic interchangeable / 692 candidate-notheader interchangeable。

官方把候选很多单句、already can unboundedly accumulate、already never need re-execute、already bound by spec 写成三个名字。把它们叫成一个「看见还没 Finalize 就已经能一直攒 interchangeable / 就已经永远不用再跑 interchangeable / 就已经规范写死条数 interchangeable」，会把 not already can unboundedly accumulate、not already never need re-execute、not already bound by spec 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量），先数清问的是还没 Finalize 是不是 already can unboundedly accumulate / 311 / 33，是不是丢掉了 是不是 already never need re-execute，还是看见有上界 是不是 already bound by spec，再决定要不要同一次发布。311 candidate vs execute bundled unbundling 在本页 item 3 完成。
