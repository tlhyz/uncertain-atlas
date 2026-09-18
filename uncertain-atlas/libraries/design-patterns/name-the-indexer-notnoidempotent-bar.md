# 模式：把通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**例**：[通常不受欢迎 not already no exceptions ≠ bundled（313）](../../tracks/implementation/worked-example-indexer-notnoidempotent-vs-bundled.md)。

## 三个名字

1. **通常不受欢迎 不是 already no exceptions：** 看见多数交易再发一次通常不受欢迎 / undesirable for most，不是已经没有幂等例外 interchangeable / 已经没有那一小类 interchangeable，不是 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable。

2. **看见幂等 不是 already mempool-guaranteed：** 看见那一小类幂等交易 / idempotent txs，不是已经由内存池保证 interchangeable / 已经池子保证幂等 interchangeable，不是 313 mempool-indexer item 2 interchangeable / 699 indexer-notappprotect interchangeable。

3. **官方说 undesirable 不是 already prescribed：** 看见规范点名通常不受欢迎 / 官方写下 undesirable，不是已经规定不确定必须怎样写幂等 interchangeable / 已经不确定幂等公式已定 interchangeable，不是 313 mempool-indexer item 1 interchangeable / 161 chainId interchangeable。

官方把通常不受欢迎单句、already no exceptions、already mempool-guaranteed、already prescribed 写成三个名字。把它们叫成一个「看见通常不受欢迎就已经没有例外 interchangeable / 就已经由内存池保证 interchangeable / 就已经规定怎样写幂等 interchangeable」，会把 not already no exceptions、not already mempool-guaranteed、not already prescribed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量），先数清问的是通常不受欢迎 是不是 already no exceptions / 313 / indexer-sold-as-replay，是不是看见幂等 是不是 already mempool-guaranteed，还是官方说 undesirable 是不是 already prescribed，再决定要不要同一次发布。313 mempool-indexer vs replay bundled unbundling 在本页 item 3 完成。
