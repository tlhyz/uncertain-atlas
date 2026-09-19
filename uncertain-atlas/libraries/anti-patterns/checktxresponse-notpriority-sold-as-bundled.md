# 反模式：把 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量）说成已经是共识顺序 / 已经进了块 / 已经从池里删掉

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有 Priority not already consensus order ≠ bundled（317）](../../tracks/implementation/worked-example-checktxresponse-notpriority-vs-bundled.md)。

## 卖法

把有 Priority / Priority 字段 / 排进提案优先 写成已经是共识顺序 interchangeable / 已经 consensus order interchangeable / 已经进了 Agreement 顺序 interchangeable / 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable；把排在前面 / 优先排进提案 / 池里靠前 写成已经进了块 interchangeable / 已经 in block interchangeable；把能优先 / 显式优先 / Priority 能排 写成已经从池里删掉 interchangeable / 已经 removed from mempool interchangeable，或已经和 317 checktxresponse bundled / checktxresponse-sold-as-exec interchangeable / 712 checktxresponse-notpriority interchangeable。

## 为什么错

官方把有 Priority 单句、already consensus order、already in block、already removed from mempool 写成三件独立的实现事。把它们卖成 already consensus order interchangeable / already in block interchangeable / already removed from mempool interchangeable，会把 not already consensus order、not already in block、not already removed from mempool 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量），必须分开 not already consensus order、not already in block、not already removed from mempool 三件事，不要和 317 / 33 / 710 / 711 / 301 糊成一句。

## 和相邻反模式

- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTxResponse vs exec bundled 全段，不是本页 Priority item 3 单句边界。
- [checktxresponse-notfork-sold-as-bundled](checktxresponse-notfork-sold-as-bundled.md) 是各节点 Data 分叉 item 2，不是本页 Priority 边界。
- [checktxresponse-notused-sold-as-bundled](checktxresponse-notused-sold-as-bundled.md) 是回了字节被引擎用 item 1，不是本页池优先边界。
