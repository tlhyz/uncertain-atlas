# 模式：把 CheckTx Usage may come from external user or another node not mempool dedup / not app replay protection / not CheckTx guard bundled 正式三事（488 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[source not mempool dedup ≠ bundled（488）](../../tracks/implementation/worked-example-chktxsource-notreplay-vs-bundled.md)。

## 三个名字

1. **送来了 不是内存池去重就保证不重放：** 看见 Methods Usage 来源，不是已经索引器滤过就保证不重放 interchangeable，不是 313 replay interchangeable / 685 chktxsource-notreplay interchangeable。
2. **能来自用户或邻居 不是已经有应用级重放保护：** 看见送来了，不是已经过了 CheckTx 就有应用级保护 interchangeable，不是 313 app replay interchangeable。
3. **看见 Usage 这句 不是 CheckTx 守卫余量 bundled：** 看见 tx source，不是已经 Guardian 就已经交差 interchangeable，不是 405 checktxguard interchangeable。

官方把 CheckTx Usage 来源、内存池去重、应用级保护、守卫 bundled 写成三个名字。把它们叫成一个「看见送来了就已经保证不重放」，会把 not mempool dedup、not app replay protection、not CheckTx guard bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from external user or another node 正式三事（488 余量），先数清问的是送来了 是不是去重就保证不重放 / 313、是不是已经有应用级保护 / 313、还是看见 Usage 是不是守卫 bundled / 405，再决定要不要同一次发布。488 chktxsource vs recheck bundled unbundling 在本页 item 3 完成。
