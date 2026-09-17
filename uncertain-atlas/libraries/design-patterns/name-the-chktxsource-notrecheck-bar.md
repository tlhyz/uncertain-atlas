# 模式：把 CheckTx Usage may come from an external user not CheckTx_Recheck / not CheckTx_New bundled / not broadcast_tx once 正式三事（488 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[may come from an external user not CheckTx_Recheck ≠ bundled（488）](../../tracks/implementation/worked-example-chktxsource-notrecheck-vs-bundled.md)。

## 三个名字

1. **may come from external user 不是 CheckTx_Recheck：** 看见 Methods Usage 能来自外部用户，不是已经 Recheck interchangeable，不是 484 chktxtype Recheck interchangeable / 683 chktxsource-notrecheck interchangeable。
2. **能来自外部用户 不是 CheckTx_New bundled：** 看见送来了，不是已经 New bundled 就代表来源验完 interchangeable，不是 484 chktxtype New interchangeable。
3. **看见外部用户送来 不是 broadcast_tx 全网只收一次：** 看见 Usage 外部用户来源，不是已经 RPC 全网只收一次 interchangeable，不是 313 bundled interchangeable。

官方把 CheckTx Usage 外部用户来源、Recheck、New bundled、broadcast_tx once 写成三个名字。把它们叫成一个「看见送来了就已经是 Recheck」，会把 not Recheck、not New bundled、not broadcast_tx once 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from an external user 正式三事（488 余量），先数清问的是 external user 是不是 Recheck / 484、是不是 New bundled、还是看见送来了 是不是 broadcast_tx once / 313，再决定要不要同一次发布。488 chktxsource vs recheck bundled unbundling 在本页 item 1 启动。
