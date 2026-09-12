# 模式：把 Replay Protection 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**例**：[索引器去重 ≠ 已经保证不重放](../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md)。

## 三个名字

1. **内存池去重不是已经保证不重复：** 看见索引器挡过不是已经有强保证。
2. **过了 CheckTx 不是已经有应用级保护：** 看见引擎滤过不是已经写进 CheckTx。
3. **通常不受欢迎不是已经没有幂等例外：** 看见多数交易不该再发不是已经没有那一小类。

## 为什么要分开叫

官方把尽力挡重复、应用必须自写的强保证、幂等例外写成三件事。把它们叫成一个「看见池子挡过就已经保证不重放」，会把 CheckTxState、池交接和链绑定一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经挡了重复」，先数清问的是索引器不是已经保证、CheckTx 不是已经有应用级保护，还是通常不受欢迎不是已经没有幂等例外，再决定要不要同一次发布。
