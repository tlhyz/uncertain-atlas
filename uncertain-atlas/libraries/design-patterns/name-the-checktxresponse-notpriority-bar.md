# 模式：把 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**例**：[有 Priority not already consensus order ≠ bundled（317）](../../tracks/implementation/worked-example-checktxresponse-notpriority-vs-bundled.md)。

## 三个名字

1. **有 Priority 不是 already consensus order：** 看见 Priority 字段 / 排进提案优先，不是已经是共识顺序 interchangeable / 已经进了 Agreement 顺序 interchangeable，不是 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable。

2. **排在前面 不是 already in block：** 看见优先排进提案 / 池里靠前，不是已经进了块 interchangeable / 已经进了决定块 interchangeable，不是 317 checktxresponse item 1 interchangeable / 710 checktxresponse-notused interchangeable。

3. **能优先 不是 already removed from mempool：** 看见显式优先 / Priority 能排，不是已经从池里删掉 interchangeable / 已经出池 interchangeable，不是 317 checktxresponse item 2 interchangeable / 711 checktxresponse-notfork interchangeable。

官方把有 Priority 单句、already consensus order、already in block、already removed from mempool 写成三个名字。把它们叫成一个「看见 Priority 就已经是共识顺序 interchangeable / 就已经进了块 interchangeable / 就已经从池里删掉 interchangeable」，会把 not already consensus order、not already in block、not already removed from mempool 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Priority 不是已经是共识顺序 not already consensus order / not already in block / not already removed from mempool 正式三事（317 余量），先数清问的是有 Priority 是不是 already consensus order / 317 / checktxresponse-sold-as-exec，是不是排在前面 是不是 already in block，还是能优先 是不是 already removed from mempool，再决定要不要同一次发布。317 checktxresponse vs exec bundled unbundling 在本页 item 3 完成。
