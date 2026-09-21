# 模式：把拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**例**：[拜占庭能提案无效块 not already pool-blocked ≠ bundled（339）](../../tracks/implementation/worked-example-checktx-notblocked-vs-bundled.md)。

## 三个名字

1. **拜占庭可以不在乎 / 池子会挡 不是 already pool-blocked：** 看见拜占庭可以不在乎 CheckTx / 池子会挡 / 弱过滤器在挡，不是已经被池子挡住 interchangeable / 已经拜占庭被挡住交差 interchangeable，不是 339 checktxweak bundled interchangeable / 33 four gates interchangeable / checktxweak-sold-as-consensus interchangeable。

2. **能提案无效交易 不是 already consensus-barred：** 看见能提案一满块无效交易 / 想的话就能提案无效块 / 能提案无效交易，不是已经进不了共识 interchangeable / 已经进不了块交差 interchangeable，不是 33 four gates interchangeable / 339 checktxweak item 1 interchangeable。

3. **诚实节点过了 CheckTx 不是 already same-ruler：** 看见诚实节点过了 CheckTx / 诚实节点弱过滤器绿了 / 诚实过了，不是已经对手守同一把尺 interchangeable / 已经同一把尺交差 interchangeable，不是 313 indexer interchangeable / 339 checktxweak item 3 interchangeable。

官方把拜占庭可以不在乎单句、already pool-blocked、already consensus-barred、already same-ruler 写成三个名字。把它们叫成一个「看见拜占庭能提案无效块就已经被池子挡住 interchangeable / 就已经进不了共识 interchangeable / 就已经同一把尺 interchangeable」，会把 not already pool-blocked、not already consensus-barred、not already same-ruler 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量），先数清问的是拜占庭可以不在乎 / 池子会挡 是不是 already pool-blocked / 339 / checktxweak-sold-as-consensus，是不是能提案无效交易 是不是 already consensus-barred，还是诚实节点过了 CheckTx 是不是 already same-ruler，再决定要不要同一次发布。339 checktxweak vs process bundled unbundling 在本页 item 2 续。
