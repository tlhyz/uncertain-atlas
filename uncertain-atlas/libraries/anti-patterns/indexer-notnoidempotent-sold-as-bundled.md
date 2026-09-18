# 反模式：把通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量）说成已经没有例外 / 已经由内存池保证 / 已经规定怎样写幂等

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[通常不受欢迎 not already no exceptions ≠ bundled（313）](../../tracks/implementation/worked-example-indexer-notnoidempotent-vs-bundled.md)。

## 卖法

把多数交易再发一次通常不受欢迎 / 通常不受欢迎 / undesirable for most 写成已经没有幂等例外 interchangeable / 已经 no exceptions interchangeable / 已经没有那一小类 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable；把看见幂等 / 那一小类幂等交易 / idempotent txs 写成已经由内存池保证 interchangeable / 已经 mempool-guaranteed interchangeable；把官方说 undesirable / 规范点名通常不受欢迎 写成已经规定不确定必须怎样写幂等 interchangeable / 已经 prescribed interchangeable，或已经和 313 mempool-indexer bundled / indexer-sold-as-replay interchangeable / 700 indexer-notnoidempotent interchangeable。

## 为什么错

官方把通常不受欢迎单句、already no exceptions、already mempool-guaranteed、already prescribed 写成三件独立的实现事。把它们卖成 already no exceptions interchangeable / already mempool-guaranteed interchangeable / already prescribed interchangeable，会把 not already no exceptions、not already mempool-guaranteed、not already prescribed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量），必须分开 not already no exceptions、not already mempool-guaranteed、not already prescribed 三件事，不要和 313 / 312 / 698 / 699 / 161 / 33 糊成一句。

## 和相邻反模式

- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是 Replay Protection bundled 全段，不是本页通常不受欢迎 item 3 单句边界。
- [indexer-notappprotect-sold-as-bundled](indexer-notappprotect-sold-as-bundled.md) 是过了 CheckTx item 2，不是本页幂等例外边界。
- [indexer-notguarantee-sold-as-bundled](indexer-notguarantee-sold-as-bundled.md) 是池子挡过一次 item 1，不是本页官方点名 undesirable 边界。
