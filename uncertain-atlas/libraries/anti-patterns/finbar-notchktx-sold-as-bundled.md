# 反模式：把 FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量） 写成已经 已经是 CheckTx 回包 / 已经印进 LastResultsHash / 已经只是记日志

**层次**：实现 / FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-finbar-notchktx-vs-bundled.md`](../tracks/implementation/worked-example-finbar-notchktx-vs-bundled.md)。

把 FinalizeBlockResponse.tx_results not already checktx-resp / not already resulthash / not already log-only 正式三事（431 余量） 写成已经 已经是 CheckTx 回包 / 已经印进 LastResultsHash / 已经只是记日志，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 tx_results 正式三事（431 余量），必须分开 not already checktx-resp、not already resulthash、not already log-only 三件事，不要和 431 / 316 / 1070 / 1072 糊成一句。

也不是：

- [finbar-notheader-sold-as-bundled](finbar-notheader-sold-as-bundled.md) 是 events 仍未印进本头单句边界（1070 item 1），不是本页 tx_results 仍未是 CheckTx 回包边界。
- Code / Data 就已经印进本头是不变量 316，不是本页有执行结果仍未印进 LastResultsHash 边界。
