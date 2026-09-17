# 模式：把 CheckTx 回包 info not already Query info / not already CheckTx log / not already settled 正式三事（391 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**例**：[CheckTx ≠ bundled（391）](../../tracks/implementation/worked-example-checktxtx-notqueryinfo-vs-bundled.md)。

## 三个名字

1. **info 不是已经是 Query 附加信息：** 看见回了信息，不是已经 384 interchangeable / 754 checktxtx-notqueryinfo interchangeable。
2. **看见回了信息 不是已经是 CheckTx 日志：** 看见有附加字段，不是已经 390 / 745 interchangeable。
3. **看见能回 不是已经交差：** 看见 CheckTx 回包 info，不是已经交差 interchangeable。

官方把 CheckTx 请求 tx / 对照当前状态验 / 回包 info 三条核心句拆成三个名字。把它们叫成一个「看见填了 CheckTx 请求余栏就已经是 Recheck」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 info 正式三事（391 余量），先数清问的是 info 是不是已经是 Query 附加信息 / 384、是不是已经是 CheckTx 日志 / 390、还是看见能回是不是已经交差，再决定要不要同一次发布。391 checktxtx vs recheck bundled unbundling 在本页 item 3 完成。
