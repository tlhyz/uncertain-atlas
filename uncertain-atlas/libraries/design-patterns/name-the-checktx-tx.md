# 模式：把 CheckTx 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**例**：[CheckTx 请求 tx 是请求交易字节 ≠ 已经是 Recheck](../../tracks/implementation/worked-example-checktxtx-vs-recheck.md)。

## 三个名字

1. **CheckTx 请求 tx 是请求交易字节不是已经是 Recheck：** 看见填了 tx 不是已经是四门已经结算。
2. **CheckTx 对照当前状态验、不应用这笔描述的状态改动不是已经按 ExecuteTxState 验过：** 看见验了不是已经参与处理块。
3. **CheckTx 回包 info 是附加信息不是已经是 Query 附加信息：** 看见回了信息不是已经是 CheckTx 日志。

## 为什么要分开叫

官方把 CheckTx 请求 `tx` 是请求交易字节、对照当前状态验、不应用这笔描述的状态改动、回包 `info` 是附加信息写成三件事。把它们叫成一个「看见填了 CheckTx 请求余栏就已经是 Recheck」，会把 Recheck、ExecuteTxState 和 Query 附加信息一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 CheckTx 请求余栏就已经是 Recheck」，先数清问的是 CheckTx 请求 tx 是请求交易字节不是已经是 Recheck、CheckTx 对照当前状态验、不应用这笔描述的状态改动不是已经按 ExecuteTxState 验过，还是 CheckTx 回包 info 是附加信息不是已经是 Query 附加信息，再决定要不要同一次发布。
