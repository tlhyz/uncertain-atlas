# 反模式：看见内存池会挡重复就当成已经保证不重放 / 看见过了 CheckTx 就当成已经有应用级保护 / 看见通常不受欢迎就当成已经没有幂等例外

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**例**：[索引器去重 ≠ 已经保证不重放](../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md)。

## 塌法

1. 看见旧交易又被送来 / 看见内存池有去重机制，就当成已经保证不会重复。
2. 看见过了 CheckTx / 看见索引器滤过，就当成已经有应用自己写的、带强保证的重放保护。
3. 看见多数交易再发一次通常不受欢迎，就当成已经没有幂等例外，或当成已经能把所有交易当必须唯一。

## 为什么会出事

官方写：内存池挡重复只是尽力（目前靠索引器），不提供任何不重复保证。应用必须自己在 CheckTx 里写带强保证的重放保护。旧交易再送来对绝大多数通常不受欢迎，除了一般很小的那一类幂等交易。

## 和相邻反模式

- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState，不是本页这种重放保护。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页。
