# 例：看见 CheckTx 的 Data 不是已经被引擎用了；看见各节点 Data 不一样不是已经分叉；看见 Priority 不是已经是共识顺序

**层次**：实现 / CheckTxResponse。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「CheckTx 的 Data 不是已经被引擎用了 / 各节点 Data 不一样不是已经分叉 / Priority 不是已经是共识顺序」，不是 CheckTxState 已经是 ExecuteTxState，也不是 Finalize 的 Data 已经印进下一头。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

规范把 `CheckTxResponse` 写成三件独立的实现事，不是「看见回了 Data 就已经被引擎用了、已经必须确定、已经按 Priority 排进共识」一件事：

1. **看见 CheckTxResponse.Data / 看见回了结果字节 不是已经被 CometBFT 用了，也不是已经是 ExecTxResult.Data。**  
   官方写：`Data` 装着 CheckTx 执行的结果（如果有）。**CometBFT 忽略** `CheckTxResponse` 里这个值。看见回了字节，不是已经被引擎用了。看见字段名也叫 Data，不是已经和 Finalize 那份同一把尺。看见有结果，不是已经进了下一头的 `LastResultsHash`。
2. **看见 Data 不确定 / 看见各节点 Data 不一样 不是已经分叉，也不是已经和 Finalize 的 Data 同一把确定性尺子。**  
   官方写：这个字段**不必确定**。同一笔交易，各节点的应用收到它、用 CheckTx 验的时候，*CheckTxState* 可以不一样。看见各节点 Data 不一样，不是已经分叉。看见不确定，不是已经违规。看见 CheckTxState 不同，不是已经和 ExecuteTxState 同一份。
3. **看见 Priority / 看见排进提案优先 不是已经是共识顺序，也不是已经进了块。**  
   官方写：从 v0.34.x 起，`CheckTxResponse` 有 `Priority` 字段，用来在内存池里**显式**给交易排优先，好进一块提案。看见有 Priority，不是已经是共识顺序。看见排在前面，不是已经进了块。看见能优先，不是已经从池里删掉。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **CheckTx 的 Data ≠ 已经被引擎用了：** 官方把忽略这份 Data 和 Finalize 必须确定的 Data 分开。
- **各节点 Data 不一样 ≠ 已经分叉：** 官方把 CheckTxState 可以不同和共识 Agreement 分开。
- **Priority ≠ 已经是共识顺序：** 官方把池里显式优先和已经进块分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 的 Data 被忽略 | 不是已经被引擎用了 | 不是 Finalize 的 Data 已经印进下一头（316） |
| Data 不必确定 | 不是已经分叉 | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| Priority | 不是已经是共识顺序 | 不是提案收了已经从池里删掉（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「CheckTx 已经回了 Data」，必须分开这份 Data 是不是已经被引擎用了、各节点不一样是不是已经分叉、Priority 是不是已经是共识顺序。可以跳过「看见回了就已经被引擎用了」。不要另写怎样实现 Priority 或怎样编 Data。317 checktxresponse vs exec bundled unbundling 完成（710 + 711 + 712）；精读 [`worked-example-checktxresponse-notused-vs-bundled.md`](worked-example-checktxresponse-notused-vs-bundled.md)（不变量 710 item 1）；[`worked-example-checktxresponse-notfork-vs-bundled.md`](worked-example-checktxresponse-notfork-vs-bundled.md)（不变量 711 item 2）；[`worked-example-checktxresponse-notpriority-vs-bundled.md`](worked-example-checktxresponse-notpriority-vs-bundled.md)（不变量 712 item 3）。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- 怎样写四门。那是不变量 33。
- ValidatorUpdate。那是另一对象。
