# 反模式：把拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量）说成已经被池子挡住 / 已经进不了共识 / 已经同一把尺

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[拜占庭能提案无效块 not already pool-blocked ≠ bundled（339）](../../tracks/implementation/worked-example-checktx-notblocked-vs-bundled.md)。

## 卖法

把拜占庭可以不在乎 CheckTx / 池子会挡 / 弱过滤器在挡 写成已经被池子挡住 interchangeable / 已经 pool-blocked interchangeable / 已经拜占庭被挡住交差 interchangeable / 339 checktxweak bundled interchangeable / 33 four gates interchangeable / checktxweak-sold-as-consensus interchangeable；把能提案一满块无效交易 / 想的话就能提案无效块 / 能提案无效交易 写成已经进不了共识 interchangeable / 已经 consensus-barred interchangeable；把诚实节点过了 CheckTx / 诚实节点弱过滤器绿了 / 诚实过了 写成已经对手守同一把尺 interchangeable / 已经 same-ruler interchangeable，或已经和 339 checktxweak bundled / checktxweak-sold-as-consensus interchangeable / 771 checktx-notblocked interchangeable。

## 为什么错

官方把拜占庭可以不在乎单句、already pool-blocked、already consensus-barred、already same-ruler 写成三件独立的实现事。把它们卖成 already pool-blocked interchangeable / already consensus-barred interchangeable / already same-ruler interchangeable，会把 not already pool-blocked、not already consensus-barred、not already same-ruler 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拜占庭能提案一满块无效交易不是已经被池子挡住 not already pool-blocked / not already consensus-barred / not already same-ruler 正式三事（339 余量），必须分开 not already pool-blocked、not already consensus-barred、not already same-ruler 三件事，不要和 339 / 312 / 33 / 313 / 770 / 772 糊成一句。

## 和相邻反模式

- [checktx-notprocess-sold-as-bundled](checktx-notprocess-sold-as-bundled.md) 是有 ProcessProposal ≠ 已经是 CheckTx（339 item 3），不是本页拜占庭能提案无效块 item 2 单句边界。
- [checktxweak-sold-as-consensus](checktxweak-sold-as-consensus.md) 是 CheckTx 弱过滤器 bundled 全段，不是本页拜占庭能提案无效块 item 2 单句边界。
- [checktx-notordering-sold-as-bundled](checktx-notordering-sold-as-bundled.md) 是不该验排序相关有效性 ≠ 已经该在 CheckTx 里验（339 item 1），不是本页拜占庭能提案无效块 ≠ 已经被池子挡住 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页能提案无效交易 ≠ 已经进不了共识 边界。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是索引器 ≠ 已经保证不重放（313），不是本页诚实过了 ≠ 已经同一把尺 边界。
