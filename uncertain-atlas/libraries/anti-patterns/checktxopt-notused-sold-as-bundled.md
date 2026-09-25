# 反模式：把引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量）说成已经被引擎用了 Data / 已经是共识顺序 / 已经分叉

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有码 not already used ≠ bundled（373）](../../tracks/implementation/worked-example-checktxopt-notused-vs-bundled.md)。

## 卖法

把有码 / 引擎对回包码不再赋予别的含义 / 有回包码 写成已经被引擎用了 Data interchangeable / 已经 used interchangeable / 已经被引擎用了 Data 交差 interchangeable / 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable；把码在 / 回包码在 / 码列在 写成已经是共识顺序 interchangeable / 已经 consensus interchangeable / 已经是共识顺序交差 interchangeable；把拒了 / 回包码拒了 / 码拒了 写成已经分叉 interchangeable / 已经 fork interchangeable / 已经分叉交差 interchangeable，或已经和 373 checktxopt bundled / checktxopt-sold-as-block interchangeable / 868 checktxopt-notused interchangeable。

## 为什么错

官方把有码、不是已经是共识顺序、不是已经分叉写成三件独立的实现事。把它们卖成 already used interchangeable / already consensus interchangeable / already fork interchangeable，会把 not already used、not already consensus、not already fork 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎对回包码不再赋予别的含义不是已经被引擎用了 Data not already used / not already consensus / not already fork 正式三事（373 余量），必须分开 not already used、not already consensus、not already fork 三件事，不要和 373 / 317 / 866 / 867 糊成一句。

## 和相邻反模式

- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 checktxopt bundled 全段，不是本页有码 item 3 单句边界。
- [checktxopt-notfourgates-sold-as-bundled](checktxopt-notfourgates-sold-as-bundled.md) 是能回 not already fourgates（373 item 1），不是本页 not already used 边界。
- [checktxopt-notexcluded-sold-as-bundled](checktxopt-notexcluded-sold-as-bundled.md) 是拒了 not already excluded（373 item 2），不是本页 not already fork 边界。
- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTx 的 Data 就已经被引擎用了（317），不是本页 not already used 单句。
