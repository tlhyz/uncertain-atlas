# 模式：点名 chktxresp-notused 杠

**层次**：实现 / CheckTx Data not already engine-used / not already same-scale / not already last-results 正式三事（317 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应**：[`../tracks/implementation/worked-example-chktxresp-notused-vs-bundled.md`](../tracks/implementation/worked-example-chktxresp-notused-vs-bundled.md)。

- **CheckTx Data 不是已经被引擎用了：** 看见回了字节，不是已经被引擎用了 interchangeable / 1016 chktxresp-notused interchangeable。
- **看见字段名也叫 Data 不是已经和 Finalize 那份同一把尺：** 看见字段名也叫 Data，不是已经和 Finalize 那份同一把尺 interchangeable。
- **看见有结果 不是已经进了下一头的 LastResultsHash：** 看见有结果，不是已经进了下一头的 LastResultsHash interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Data 正式三事（317 余量），先数清问的是是不是已经被引擎用了、是不是已经和 Finalize 那份同一把尺、还是看见有结果是不是已经进了下一头的 LastResultsHash，再决定要不要同一次发布。317 checktxresponse vs exec bundled unbundling 在本页 item 1 启动。
