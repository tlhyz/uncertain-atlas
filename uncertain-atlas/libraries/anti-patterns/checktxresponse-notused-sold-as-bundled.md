# 反模式：把 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量）说成已经被引擎用了 / 已经是 ExecTxResult.Data / 已经进了 LastResultsHash

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了字节 not already used by engine ≠ bundled（317）](../../tracks/implementation/worked-example-checktxresponse-notused-vs-bundled.md)。

## 卖法

把回了字节 / CheckTxResponse.Data / 回了结果字节 写成已经被引擎用了 interchangeable / 已经 used by engine interchangeable / 已经进了引擎路径 interchangeable / 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable；把字段名也叫 Data / 也叫 Data / 和 Finalize 同名 写成已经是 ExecTxResult.Data interchangeable / 已经和 Finalize 那份同一把尺 interchangeable；把有结果 / CheckTx 回了结果 写成已经进了下一头的 LastResultsHash interchangeable / 已经 in LastResultsHash interchangeable，或已经和 317 checktxresponse bundled / checktxresponse-sold-as-exec interchangeable / 710 checktxresponse-notused interchangeable。

## 为什么错

官方把回了字节单句、already used by engine、already ExecTxResult.Data、already in LastResultsHash 写成三件独立的实现事。把它们卖成 already used by engine interchangeable / already ExecTxResult.Data interchangeable / already in LastResultsHash interchangeable，会把 not already used by engine、not already ExecTxResult.Data、not already in LastResultsHash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量），必须分开 not already used by engine、not already ExecTxResult.Data、not already in LastResultsHash 三件事，不要和 317 / 33 / 711 / 712 / 316 / 709 糊成一句。

## 和相邻反模式

- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTxResponse vs exec bundled 全段，不是本页回了字节 item 1 单句边界。
- [exectxresult-notheader-sold-as-bundled](exectxresult-notheader-sold-as-bundled.md) 是 Finalize Code/Data 印本头（316），不是本页 CheckTx Data 被忽略边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ ExecuteTxState，不是本页 Data 是否被引擎用边界。
