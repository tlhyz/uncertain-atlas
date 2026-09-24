# 模式：把没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[没填表 not already prioritized ≠ bundled（367）](../../tracks/implementation/worked-example-lane-notpriority-vs-bundled.md)。

## 三个名字

1. **没填表 不是 already prioritized：** 看见没填表 / 应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 / 没定义，不是已经排了优先 interchangeable / 已经 prioritized interchangeable / 已经排了优先交差 interchangeable，不是 367 lane bundled interchangeable / lane-sold-as-priority interchangeable。

2. **并成一条道 不是 already checktx-priority：** 看见并成一条道 / 这时引擎把交易都放进一条道 / 没定义就并道，不是已经是 `CheckTxResponse.Priority` interchangeable / 已经 checktx-priority interchangeable / 已经是 CheckTx Priority 交差 interchangeable，不是 317 checktx-priority interchangeable / 849 lane-notalgo interchangeable。

3. **Info 回了 不是 already settled：** 看见 Info 回了 / Info 回了车道 / 回了车道字段，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 850 lane-notinblock interchangeable / 33 fourgates interchangeable。

官方把没填表、不是已经是 CheckTx Priority、不是已经交差写成三个名字。把它们叫成一个「看见没填表就已经排了优先 interchangeable / 就已经是 CheckTx Priority interchangeable / 就已经交差 interchangeable」，会把 not already prioritized、not already checktx-priority、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没定义 lane_priorities 不是已经排了优先 not already prioritized / not already checktx-priority / not already settled 正式三事（367 余量），先数清问的是没填表 是不是 already prioritized / 367 / lane-sold-as-priority，是不是并成一条道 是不是 already checktx-priority，还是 Info 回了 是不是 already settled，再决定要不要同一次发布。367 lane-vs-priority bundled unbundling 在本页 item 1 启动。
