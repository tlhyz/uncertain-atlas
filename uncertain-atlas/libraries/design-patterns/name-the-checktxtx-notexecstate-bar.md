# 模式：把 CheckTx 对照当前状态验 not already ExecuteTxState / not already processing block / not already settled 正式三事（391 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**例**：[CheckTx ≠ bundled（391）](../../tracks/implementation/worked-example-checktxtx-notexecstate-vs-bundled.md)。

## 三个名字

1. **validate 不是已经按 ExecuteTxState 验过：** 看见验了，不是已经 312 interchangeable / 753 checktxtx-notexecstate interchangeable。
2. **看见验了 不是已经参与处理块：** 看见没应用改动，不是已经 373 / 486 interchangeable。
3. **看见对照当前状态 不是已经交差：** 看见对照当前状态验，不是已经交差 interchangeable。

官方把 CheckTx 请求 tx / 对照当前状态验 / 回包 info 三条核心句拆成三个名字。把它们叫成一个「看见填了 CheckTx 请求余栏就已经是 Recheck」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 对照当前状态验 正式三事（391 余量），先数清问的是是不是已经按 ExecuteTxState 验过 / 312、是不是已经参与处理块 / 373、还是看见对照当前状态是不是已经交差，再决定要不要同一次发布。391 checktxtx vs recheck bundled unbundling 在本页 item 2 续。
