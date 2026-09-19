# 模式：把 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**例**：[回了字节 not already used by engine ≠ bundled（317）](../../tracks/implementation/worked-example-checktxresponse-notused-vs-bundled.md)。

## 三个名字

1. **回了字节 不是 already used by engine：** 看见 CheckTxResponse.Data / 回了结果字节，不是已经被引擎用了 interchangeable / 已经进了引擎路径 interchangeable，不是 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable。

2. **字段名也叫 Data 不是 already ExecTxResult.Data：** 看见也叫 Data / 和 Finalize 同名，不是已经是 ExecTxResult.Data interchangeable / 已经和 Finalize 那份同一把尺 interchangeable，不是 317 checktxresponse item 2 interchangeable / 711 checktxresponse-notfork interchangeable。

3. **有结果 不是 already in LastResultsHash：** 看见 CheckTx 回了结果 / 有结果字节，不是已经进了下一头的 LastResultsHash interchangeable / 已经印进下一头 interchangeable，不是 317 checktxresponse item 3 interchangeable / 712 checktxresponse-notpriority interchangeable。

官方把回了字节单句、already used by engine、already ExecTxResult.Data、already in LastResultsHash 写成三个名字。把它们叫成一个「看见回了就已经被引擎用了 interchangeable / 就已经是 Finalize Data interchangeable / 就已经进了下一头 interchangeable」，会把 not already used by engine、not already ExecTxResult.Data、not already in LastResultsHash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Data 不是已经被引擎用了 not already used by engine / not already ExecTxResult.Data / not already in LastResultsHash 正式三事（317 余量），先数清问的是回了字节 是不是 already used by engine / 317 / checktxresponse-sold-as-exec，是不是字段名也叫 Data 是不是 already ExecTxResult.Data，还是有结果 是不是 already in LastResultsHash，再决定要不要同一次发布。317 checktxresponse vs exec bundled unbundling 在本页 item 1 完成。
