# 例：看见 CheckTx 的 Data is not already engine-used interchangeable / not already same-scale interchangeable / not already last-results interchangeable

**层次**：实现 / CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量）/ not 1016 chktxresp-notused interchangeable / not 317 checktxresponse-vs-exec bundled interchangeable」，不是 CheckTxResponse bundled（317），也不是 Finalize 的 Data 已经印进下一头（316/1015），也不是 CheckTxState 已经是 ExecuteTxState（312）。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

1. **看见 CheckTxResponse.Data / 看见回了结果字节 这份回执 is not already 已经被 CometBFT 用了 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1016 chktxresp-notused interchangeable / 1017 chktxresp-notfork interchangeable / 317 checktx item 2 Data 不确定 interchangeable，也不是已经 CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事 bundled（317 item 1 余量） interchangeable / 317 checktx item 1 interchangeable。**  
   官方写：Data 装着 CheckTx 执行的结果（如果有）。CometBFT 忽略 CheckTxResponse 里这个值。看见回了字节，不是已经被引擎用了 interchangeable——本页从 317 item 1 侧钉 not already engine-used 单句。317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动。

2. **看见字段名也叫 Data / 看见回了字节 / 这份回执 is not already 已经和 Finalize 那份同一把尺 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1016 chktxresp-notused interchangeable / 317 checktx item 3 Priority interchangeable / 1018 chktxresp-notprio interchangeable，也不是已经 Finalize 的 Data 已经印进下一头 interchangeable / 316/1015 exectx-notheader interchangeable。**  
   官方把字段名也叫 Data 和已经和 Finalize 那份同一把尺分开。看见字段名也叫 Data，不是已经和 Finalize 那份同一把尺 interchangeable。本页钉 not already same-scale 单句。

3. **看见有结果 / 看见回了字节 / 这份回执 is not already 已经进了下一头的 LastResultsHash interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1016 chktxresp-notused interchangeable / 1017 chktxresp-notfork interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把有结果和已经进了下一头的 LastResultsHash 分开。看见有结果，不是已经进了下一头的 LastResultsHash interchangeable。317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **CheckTx Data not already engine-used ≠ 已经被引擎用了 interchangeable：** 官方把忽略这份 Data 和 Finalize 必须确定的 Data 分开。
- **看见字段名也叫 Data not already same-scale ≠ 已经和 Finalize 那份同一把尺 interchangeable：** 官方把字段名也叫 Data 和已经和 Finalize 那份同一把尺分开。
- **看见有结果 not already last-results ≠ 已经进了下一头的 LastResultsHash interchangeable：** 官方把有结果和已经进了下一头的 LastResultsHash 分开；317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 的 Data 被忽略 | 不是已经被引擎用了 | 不是 Finalize 的 Data 已经印进下一头（316/1015） |
| 看见字段名也叫 Data | 不是已经和 Finalize 那份同一把尺 | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 看见有结果 | 不是已经进了下一头的 LastResultsHash | 不是各节点不一样就已经分叉（1017） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量），必须分开是不是已经被引擎用了、是不是已经和 Finalize 那份同一把尺、是不是已经进了下一头的 LastResultsHash。可以跳过「看见回了就已经被引擎用了」。不要另写怎样实现 Priority 或怎样编 Data。317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxresp-notfork-vs-bundled.md`](worked-example-chktxresp-notfork-vs-bundled.md)（不变量 1017 item 2）。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- CheckTxResponse bundled。那是不变量 317。
- Finalize 的 Data 已经印进下一头。那是不变量 316/1015。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
