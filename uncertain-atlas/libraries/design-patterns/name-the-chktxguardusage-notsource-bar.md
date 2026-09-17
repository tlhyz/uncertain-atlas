# 模式：把 CheckTx Usage before letting into its local mempool not tx source bundled / not mempool dedup / not Code≠0 rejected bundled 正式三事（490 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[before letting in not tx source bundled ≠ bundled（490）](../../tracks/implementation/worked-example-chktxguardusage-notsource-vs-bundled.md)。

## 三个名字

1. **before letting into its local mempool 不是 tx source bundled：** 看见 Methods Usage 才让进本地池，不是已经来源验完 interchangeable，不是 488 chktxsource interchangeable / 691 chktxguardusage-notsource interchangeable。
2. **看见才让进本地池 不是内存池去重就保证不重放：** 看见 local mempool，不是已经 Replay Protection interchangeable，不是 313 replay interchangeable。
3. **看见 Usage 这句 不是 Code≠0 rejected bundled：** 看见 Guardian 语境下的 before letting in，不是已经 Code≠0 bundled 就代表 Guardian 交差 interchangeable，不是 489 chktxcodereject interchangeable。

官方把 CheckTx Usage 本地池入口、tx source、去重保证、Code≠0 bundled 写成三个名字。把它们叫成一个「看见才让进本地池就已经保证不重放」，会把 not tx source bundled、not mempool dedup、not Code≠0 rejected bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage before letting into local mempool 正式三事（490 余量），先数清问的是才让进本地池 是不是 tx source bundled / 488、是不是去重就保证不重放 / 313、还是看见 Usage 是不是 Code≠0 bundled / 489，再决定要不要同一次发布。490 chktxguardusage vs optional bundled unbundling 在本页 item 3 完成。
