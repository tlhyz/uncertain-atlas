# 模式：把 CheckTx Usage every node runs CheckTx before letting into local mempool not broadcast_tx others run / not in-pool gossip / not forever valid 正式三事（490 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[every node runs CheckTx not forever valid ≠ bundled（490）](../../tracks/implementation/worked-example-chktxguardusage-notgates-vs-bundled.md)。

## 三个名字

1. **every node runs CheckTx 不是 broadcast_tx 别人也会跑：** 看见 Methods Usage 每条节点先跑，不是已经 RPC 回了别人也会跑 interchangeable，不是 690 chktxguardusage-notgates interchangeable。
2. **先跑了才让进本地池 不是已经流言 / Check 通过就是已进提案：** 看见 every node，不是已经四门已经结算 interchangeable，不是 33 four gates interchangeable。
3. **看见 every node 不是 forever valid：** 看见本地池入口，不是已经 CheckTx 过了就永远有效 interchangeable，不是 301 forever valid interchangeable。

官方把 CheckTx Usage 本地池入口、别人也会跑、进池流言、forever valid 写成三个名字。把它们叫成一个「看见每条节点先跑 CheckTx 就已经四门已经结算」，会把 not broadcast_tx others run、not in-pool gossip、not forever valid 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage every node runs CheckTx 正式三事（490 余量），先数清问的是 every node 是不是别人也会跑、是不是已经流言 / Check 通过就是已进提案 / 33、还是看见先跑了 是不是 forever valid / 301，再决定要不要同一次发布。490 chktxguardusage vs optional bundled unbundling 在本页 item 2 续。
