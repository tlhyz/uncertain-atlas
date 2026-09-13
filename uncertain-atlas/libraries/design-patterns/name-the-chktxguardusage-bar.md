# 模式：把 CheckTx Usage Guardian 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[Guardian of the mempool ≠ Technically optional](../../tracks/implementation/worked-example-chktxguardusage-vs-optional.md)。

## 三个名字

1. **Guardian of the mempool 不是 Technically optional / 四门已经结算：** 看见 Methods Usage 侧内存池守卫，不是 optional / 可以不跑 CheckTx interchangeable。
2. **every node runs CheckTx before letting into local mempool 不是已经流言 / Check 通过就是已进提案：** 看见每条节点先跑 CheckTx 才让进本地池，不是广播或四门结算 interchangeable。
3. **before letting into its local mempool 不是已经保证不重放 / tx source bundled interchangeable：** 看见本地池入口守卫，不是 tx source 或 Replay Protection bundled interchangeable。

## 为什么要分开叫

官方把 CheckTx Usage 里 Guardian of the mempool、every node runs CheckTx before letting into its local mempool、before letting into its local mempool 和 Technically optional（373）、四门结算（33）、tx source（488）、Replay Protection（313）写成三个名字。把它们叫成一个「看见每条节点先跑 CheckTx 就已经是 optional、已经四门已经结算、已经保证不重放」，会把 Guardian 语义、本地池入口守卫、来源/重放三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Guardian，先数清问的是 Guardian of the mempool 是不是 Technically optional / 四门已经结算、every node runs CheckTx before letting into local mempool 是不是已经流言 / Check 通过就是已进提案、before letting into its local mempool 是不是已经保证不重放 / tx source bundled interchangeable，再决定要不要同一次发布。
