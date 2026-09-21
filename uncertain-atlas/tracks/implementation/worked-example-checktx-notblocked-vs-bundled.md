# 例：看见拜占庭可以不在乎 CheckTx / 看见能提案一满块无效交易 / 看见诚实节点过了 CheckTx is not already already pool-blocked interchangeable / already consensus-barred interchangeable / already same-ruler interchangeable

**层次**：实现 / 拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 整池已经交差。本页是「拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量）/ not 771 checktx-notblocked interchangeable / not 339 checktxweak bundled interchangeable」，不是 CheckTx 弱过滤器 bundled（339），也不是不该验排序相关有效性不是已经该在 CheckTx 里验（770 item 1 余量）或 ProcessProposal 对付这种行为不是已经是 CheckTx（772 item 3 余量）。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

规范把 Requirements 里拜占庭可以不在乎 CheckTx、能提案一满块无效交易 和「已经是拜占庭不在乎就已经被池子挡住 interchangeable / 已经是能提案无效交易就已经进不了共识 interchangeable / 已经是诚实节点过了 CheckTx 就已经对手守同一把尺 interchangeable / 已经是 checktxweak bundled interchangeable」分开写成三件独立的实现事，不是「看见拜占庭能提案无效块就已经被池子挡住 interchangeable / 就已经进不了共识 interchangeable / 就已经同一把尺 interchangeable」一件事：

1. **看见拜占庭可以不在乎 CheckTx / 看见池子会挡 / 看见弱过滤器在挡 is not already 已经被池子挡住 interchangeable / 已经 pool-blocked interchangeable / 已经拜占庭被挡住交差 interchangeable / 339 checktxweak bundled interchangeable / 33 four gates interchangeable / checktxweak-sold-as-consensus interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 771 checktx-notblocked interchangeable / 339 checktxweak item 2 interchangeable，也不是已经拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事 bundled（339 item 2 余量） interchangeable / 339 checktxweak item 2 interchangeable，也不是已经不该验排序相关有效性不是已经该在 CheckTx 里验（770） interchangeable / 772 checktx-notprocess interchangeable / 312 checktxstate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CheckTx 弱，是因为拜占庭节点可以不在乎 CheckTx。看见池子会挡，不是拜占庭已经被挡住。看见拜占庭可以不在乎 CheckTx，不是已经 pool-blocked interchangeable——339 钉 bundled 三事，本页从 item 2 侧钉 not already pool-blocked 单句。看见弱过滤器在挡，不是已经 CheckTx 弱过滤器 bundled（339） interchangeable——339 钉 bundled，本页钉 item 2 第一件事。看见池子会挡，不是已经四门已经结算（33） interchangeable——33 另钉。339 checktxweak vs process bundled unbundling 在本页 item 2 续。

2. **看见能提案一满块无效交易 / 看见想的话就能提案无效块 / 看见能提案无效交易 is not already 已经进不了共识 interchangeable / 已经 consensus-barred interchangeable / 已经进不了块交差 interchangeable / 339 checktxweak bundled interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 771 checktx-notblocked interchangeable / 339 checktxweak item 1 排序 interchangeable / 339 checktxweak item 3 ProcessProposal interchangeable，也不是已经拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事 bundled（339 item 2 余量） interchangeable / 339 checktxweak item 2 interchangeable，也不是已经被池子挡住（本页第一件事） interchangeable。**  
   官方写：它想的话就能提案一满块无效交易。看见能提案无效交易，不是已经进不了块。看见能提案一满块无效交易，不是已经 consensus-barred interchangeable——本页钉 not already consensus-barred 单句。看见想的话就能提案无效块，不是已经被池子挡住（本页第一件事） interchangeable——三件事分开钉。339 checktxweak vs process bundled unbundling 在本页 item 2 续。

3. **看见诚实节点过了 CheckTx / 看见诚实节点弱过滤器绿了 / 看见诚实过了 is not already 已经对手守同一把尺 interchangeable / 已经 same-ruler interchangeable / 已经同一把尺交差 interchangeable / 339 checktxweak bundled interchangeable / 313 indexer interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339） interchangeable / 771 checktx-notblocked interchangeable / 339 checktxweak item 1 / 339 checktxweak item 3，也不是已经拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事 bundled（339 item 2 余量） interchangeable / 339 checktxweak item 2 interchangeable，也不是已经被池子挡住（本页第一件事） interchangeable / 已经进不了共识（本页第二件事） interchangeable。**  
   官方写：看见诚实节点过了 CheckTx，不是对手已经守同一把尺。看见诚实节点弱过滤器绿了，不是已经 same-ruler interchangeable——本页钉 not already same-ruler 单句。看见诚实过了，不是已经进不了共识（本页第二件事） interchangeable——三件事分开钉。339 checktxweak vs process bundled unbundling 在本页 item 2 续。

怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal` 是规范里的做法，本页不抄。CheckTx 弱过滤器 bundled（339）、不该验排序相关有效性不是已经该在 CheckTx 里验（339 item 1 余量 / 770）、ProcessProposal 对付这种行为不是已经是 CheckTx（339 item 3 余量 / 772）、CheckTxState 已经是 ExecuteTxState（312）、四门已经结算（33）、索引器已经保证不重放（313）是另外那套，本页不抄。

## 官方为什么这样拆

- **拜占庭可以不在乎 / 池子会挡 not already pool-blocked ≠ 339 / 33 interchangeable：** 官方把池子弱过滤器和拜占庭已经被挡住分开。
- **能提案无效交易 not already consensus-barred ≠ 已经进不了共识 interchangeable：** 官方把能提案无效块和已经进不了块分开。
- **诚实节点过了 CheckTx not already same-ruler ≠ 已经同一把尺 interchangeable：** 官方把诚实过了和对手已经守同一把尺分开；339 checktxweak vs process bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拜占庭可以不在乎 / 池子会挡 | 不是 already pool-blocked | 不是四门已经结算 alone（33） |
| 能提案无效交易 | 不是 already consensus-barred | 不是不该验排序就已经该在 CheckTx 里验 alone（770） |
| 诚实节点过了 CheckTx | 不是 already same-ruler | 不是 ProcessProposal 就已经是 CheckTx alone（772） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量），必须分开拜占庭可以不在乎 / 池子会挡 是不是 already pool-blocked interchangeable / 339 checktxweak bundled interchangeable / checktxweak-sold-as-consensus interchangeable、能提案无效交易 是不是 already consensus-barred interchangeable、诚实节点过了 CheckTx 是不是 already same-ruler interchangeable。可以跳过「看见拜占庭能提案无效块就已经被池子挡住 interchangeable / 就已经进不了共识 interchangeable / 就已经同一把尺 interchangeable」。不要把「不验排序」当不确定已经验完。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktxweak vs process bundled unbundling 在本页 item 2 续（770 + 771）；续 [`worked-example-checktx-notprocess-vs-bundled.md`](worked-example-checktx-notprocess-vs-bundled.md)（不变量 772 item 3）已写；完成见 772。

## 本页不抄

- 怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal`。
- CheckTx 弱过滤器 bundled。那是不变量 339。
- 不该验排序相关有效性不是已经该在 CheckTx 里验。那是不变量 339 item 1 余量 / 770。
- ProcessProposal 对付这种行为不是已经是 CheckTx。那是不变量 339 item 3 余量 / 772。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- 四门已经结算。那是不变量 33。
- 索引器已经保证不重放。那是不变量 313。
