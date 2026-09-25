# 模式：把引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[有码 not already used ≠ bundled（373）](../../tracks/implementation/worked-example-checktxopt-notused-vs-bundled.md)。

## 三个名字

1. **有码 不是 already used：** 看见有码 / 引擎对回包码不再赋予别的含义 / 有回包码，不是已经被引擎用了 Data interchangeable / 已经 used interchangeable / 已经被引擎用了 Data 交差 interchangeable，不是 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable。

2. **码在 不是 already consensus：** 看见码在 / 回包码在 / 码列在，不是已经是共识顺序 interchangeable / 已经 consensus interchangeable / 已经是共识顺序交差 interchangeable，不是 317 Priority interchangeable / 866 checktxopt-notfourgates interchangeable。

3. **拒了 不是 already fork：** 看见拒了 / 回包码拒了 / 码拒了，不是已经分叉 interchangeable / 已经 fork interchangeable / 已经分叉交差 interchangeable，不是 867 checktxopt-notexcluded interchangeable / 711 CheckTx notfork interchangeable。

官方把有码、不是已经是共识顺序、不是已经分叉写成三个名字。把它们叫成一个「看见有码就已经被引擎用了 Data interchangeable / 就已经是共识顺序 interchangeable / 就已经分叉 interchangeable」，会把 not already used、not already consensus、not already fork 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量），先数清问的是有码 是不是 already used / 373 / checktxopt-sold-as-block，是不是码在 是不是 already consensus，还是拒了 是不是 already fork，再决定要不要同一次发布。373 checktxopt-vs-block bundled unbundling 在本页 item 3 完成。
