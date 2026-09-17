# 模式：把 CheckTx Usage empty lane_id not priority 0 reserved / not deleted from pool / not no-lane means rejected 正式三事（482 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[empty ≠ bundled（482）](../../tracks/implementation/worked-example-chktxlane-notreserved-vs-bundled.md)。

## 三个名字

1. **empty lane_id 不是 priority 0 留给不设道：** 看见空字符串，不是已经 367 interchangeable / 704 chktxlane-notreserved interchangeable。
2. **看见没在回包里设道 不是已经从池里删掉：** 看见 empty，不是已经没进池 interchangeable。
3. **看见 Usage 这句 不是 CheckTx 可选就已经拒了：** 看见 empty 单句，不是已经 373 interchangeable。

官方把 CheckTx Usage lane_id 三条核心句拆成三个名字。把它们叫成一个「看见 CheckTx 回了 lane_id 就已经排了优先」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage empty lane_id 正式三事（482 余量），先数清问的是 empty 是不是 Info 侧 priority 0 不设道 / 367、是不是已经从池里删掉、还是看见 Usage 是不是 CheckTx 可选就已经拒了 / 373，再决定要不要同一次发布。482 chktxlane vs default bundled unbundling 在本页 item 1 启动。
