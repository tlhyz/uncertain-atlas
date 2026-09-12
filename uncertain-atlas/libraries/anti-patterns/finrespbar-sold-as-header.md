# 反模式：看见 FinalizeBlockResponse.events 是给索引用的类型键值事件就当成已经印进本头 / 看见 FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表就当成已经是 CheckTx 回包 / 看见 FinalizeBlockResponse.validator_updates 是对验证者集合的改动就当成已经在 H+1 换人

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[FinalizeBlockResponse.events 是给索引用的类型键值事件 ≠ 已经印进本头](../../tracks/implementation/worked-example-finrespbar-vs-header.md)。

## 塌法

1. 看见 `FinalizeBlockResponse.events` 是给索引用的类型键值事件 / 看见回了 events，就当成已经印进本头，或当成已经像 Code/Data 那样必须确定。
2. 看见 `FinalizeBlockResponse.tx_results` 是执行这块各笔交易得到的结果列表 / 看见回了 tx_results，就当成已经是 CheckTx 回包，或当成已经同一顺序就是已经印进 LastResultsHash。
3. 看见 `FinalizeBlockResponse.validator_updates` 是对验证者集合的改动 / 看见回了 validator_updates，就当成已经在 H+1 换人，或当成已经是 ValidatorUpdate 用公钥认人就已经改了集合。

## 为什么会出事

官方写：`events` 是 Type & Key-Value events for indexing，Deterministic 是 No。`tx_results` 是 executing the transactions 的结果列表，Deterministic 是 Yes。块 H 触发的 `validator_updates` 影响 H+1、H+2、H+3。看见回了 Finalize 回包栏，不是已经印进本头，也不是已经是 CheckTx 回包，也不是已经在 H+1 换人。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 里产出了事件就已经交给引擎，不是本页这种 FinalizeBlockResponse.events 是给索引用的类型键值事件不是已经印进本头。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code / Data 就已经印进本头，不是本页这种 FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表不是已经是 CheckTx 回包。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 ValidatorUpdate 用公钥认人就已经改了集合，不是本页这种 FinalizeBlockResponse.validator_updates 是对验证者集合的改动不是已经在 H+1 换人。
