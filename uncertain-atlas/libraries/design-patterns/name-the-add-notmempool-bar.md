# 模式：把往提案加了一笔新的不是已经进了内存池 not already in-pool / not already checktx / not already settled 正式三事（355 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[往提案加了一笔新的 not already in-pool ≠ bundled（355）](../../tracks/implementation/worked-example-add-notmempool-vs-bundled.md)。

## 三个名字

1. **回包里有它 不是 already in-pool：** 看见往提案加了一笔新的 / 回包里有它 / 加进了 txs，不是已经进了内存池 interchangeable / 已经 in-pool interchangeable / 已经进池交差 interchangeable，不是 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable。

2. **能提 不是 already checktx：** 看见能提 / 回包里有它 / 能写进提案，不是已经过了 CheckTx interchangeable / 已经 checktx interchangeable / 已经 CheckTx 交差 interchangeable，不是 33 fourgates interchangeable / 818 drop-notmempool interchangeable。

3. **加进去了 不是 already settled：** 看见加进去了 / 加进了回包 / 写进 txs，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 820 retarget-nottraceable interchangeable / 345 preparereturn interchangeable。

官方把回包里有它、不是已经过了 CheckTx、不是已经交差写成三个名字。把它们叫成一个「看见回包里有它就已经进池 interchangeable / 就已经过了 CheckTx interchangeable / 就已经交差 interchangeable」，会把 not already in-pool、not already checktx、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看往提案加了一笔新的不是已经进了内存池 not already in-pool / not already checktx / not already settled 正式三事（355 余量），先数清问的是回包里有它 是不是 already in-pool / 355 / preparedrop-sold-as-evicted，是不是能提 是不是 already checktx，还是加进去了 是不是 already settled，再决定要不要同一次发布。355 preparedrop vs mempool bundled unbundling 在本页 item 2 续。
