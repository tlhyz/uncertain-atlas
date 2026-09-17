# 模式：把 Finalize 回包栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[FinalizeBlockResponse.events 是给索引用的类型键值事件 ≠ 已经印进本头](../../tracks/implementation/worked-example-finrespbar-vs-header.md)。

## 三个名字

1. **FinalizeBlockResponse.events 是给索引用的类型键值事件不是已经印进本头：** 看见回了 events 不是已经像 Code/Data 那样必须确定。
2. **FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表不是已经是 CheckTx 回包：** 看见回了 tx_results 不是已经同一顺序就是已经印进 LastResultsHash。
3. **FinalizeBlockResponse.validator_updates 是对验证者集合的改动不是已经在 H+1 换人：** 看见回了 validator_updates 不是已经是 ValidatorUpdate 用公钥认人就已经改了集合。

## 为什么要分开叫

官方把 FinalizeBlock Response 表上 `events` 是给索引用的类型键值事件、`tx_results` 是执行这块各笔交易得到的结果列表、`validator_updates` 是对验证者集合的改动写成三件事。把它们叫成一个「看见回了 Finalize 回包栏就已经印进本头」，会把已经印进本头、已经是 CheckTx 回包和已经在 H+1 换人一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 回包栏就已经印进本头」，先数清问的是 FinalizeBlockResponse.events 是给索引用的类型键值事件不是已经印进本头、FinalizeBlockResponse.tx_results 是执行这块各笔交易得到的结果列表不是已经是 CheckTx 回包，还是 FinalizeBlockResponse.validator_updates 是对验证者集合的改动不是已经在 H+1 换人，再决定要不要同一次发布。
