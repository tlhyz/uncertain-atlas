# 模式：点名 finbar-notchktx 杠

**层次**：实现 / FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-finbar-notchktx-vs-bundled.md`](../tracks/implementation/worked-example-finbar-notchktx-vs-bundled.md)。

- **tx_results 不是已经是 CheckTx 回包：** 看见回了 tx_results，不是已经是 CheckTx 回包 interchangeable / 1071 finbar-notchktx interchangeable。
- **看见有执行结果 不是已经印进 LastResultsHash：** 看见有执行结果，不是已经印进 LastResultsHash interchangeable。
- **看见 Deterministic 是 Yes 不是已经只是记日志：** 看见 Deterministic 是 Yes，不是已经只是记日志 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 tx_results 正式三事（431 余量），先数清问的是是不是已经是 CheckTx 回包、是不是已经印进 LastResultsHash、还是看见 Deterministic 是 Yes 是不是已经只是记日志，再决定要不要同一次发布。431 finrespbar vs header bundled unbundling 在本页 item 2 续。
