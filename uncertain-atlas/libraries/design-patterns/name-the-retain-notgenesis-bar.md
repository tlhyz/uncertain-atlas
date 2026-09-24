# 模式：把全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[全网都删会永久丢 not already genesis-replay ≠ bundled（366）](../../tracks/implementation/worked-example-retain-notgenesis-vs-bundled.md)。

## 三个名字

1. **全网都删会永久丢 不是 already genesis-replay：** 看见全网都删会永久丢 / 若网上所有节点都删了历史块、这些数据就永久丢了 / 能剪会丢，不是已经能从创世再装 interchangeable / 已经 genesis-replay interchangeable / 已经从创世再装交差 interchangeable，不是 366 retain bundled interchangeable / retain-sold-as-kept interchangeable。

2. **开了 state sync 不是 already light-check：** 看见开了 state sync / 除非链上开了 state sync、否则新节点加不进来 / 能引导，不是已经能给轻客户端验 interchangeable / 已经 light-check interchangeable / 已经轻客户端验交差 interchangeable，不是 323 full-history interchangeable / 845 retain-notpruning interchangeable。

3. **能丢 不是 already settled：** 看见能丢 / 能剪会永久丢 / 审计回放轻客户端还可能要用，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 846 retain-notdeleted interchangeable / 33 fourgates interchangeable。

官方把全网都删会永久丢、不是已经能给轻客户端验、不是已经交差写成三个名字。把它们叫成一个「看见全网都删会永久丢就已经能从创世再装 interchangeable / 就已经能给轻客户端验 interchangeable / 就已经交差 interchangeable」，会把 not already genesis-replay、not already light-check、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量），先数清问的是全网都删会永久丢 是不是 already genesis-replay / 366 / retain-sold-as-kept，是不是开了 state sync 是不是 already light-check，还是能丢 是不是 already settled，再决定要不要同一次发布。366 retain-vs-kept bundled unbundling 在本页 item 3 完成。
