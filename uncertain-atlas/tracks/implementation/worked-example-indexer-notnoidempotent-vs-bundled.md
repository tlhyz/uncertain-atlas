# 例：看见通常不受欢迎 / 看见幂等 / 官方说 undesirable is not already already no exceptions interchangeable / already mempool-guaranteed interchangeable / already prescribed interchangeable

**层次**：实现 / 通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量）/ not 700 indexer-notnoidempotent interchangeable / not 313 mempool-indexer bundled interchangeable」，不是 Replay Protection bundled（313），也不是索引器去重不是已经保证不重复（698 item 1 余量）或过了 CheckTx 不是已经有应用级保护（699 item 2 余量）。不要另写怎样实现重放保护或怎样写幂等。

## 官方三件事

规范把 Requirements 里旧交易再送来对**绝大多数**交易通常不受欢迎、**除了**一般很小的那一类幂等交易 和「已经是通常不受欢迎就已经没有幂等例外 interchangeable / 已经是看见幂等就已经由内存池保证 interchangeable / 已经是官方说 undesirable 就已经规定不确定必须怎样写幂等 interchangeable / 已经是 Replay Protection bundled interchangeable」分开写成三件独立的实现事，不是「看见通常不受欢迎 就已经没有例外 interchangeable / 就已经由内存池保证 interchangeable / 就已经规定怎样写幂等 interchangeable」一件事：

1. **看见多数交易再发一次通常不受欢迎 / 看见通常不受欢迎 / 看见 undesirable for most is not already 已经没有幂等例外 interchangeable / 已经 no exceptions interchangeable / 已经没有那一小类 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 700 indexer-notnoidempotent interchangeable / 313 mempool-indexer item 3 interchangeable，也不是已经通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事 bundled（313 item 3 余量） interchangeable / 313 mempool-indexer item 3 interchangeable，也不是已经索引器去重不是已经保证不重复（698） interchangeable / 699 indexer-notappprotect interchangeable / 161 chainId interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：旧交易再送来，对**绝大多数**交易通常不受欢迎，**除了**一般很小的那一类幂等交易。看见通常不受欢迎，不是已经没有例外 interchangeable——313 钉 bundled 三事，本页从 item 3 侧钉 not already no exceptions 单句。看见多数交易再发一次通常不受欢迎，不是已经 Replay Protection bundled（313） interchangeable——313 钉 bundled，本页钉 item 3 第一件事。看见 undesirable for most，不是已经索引器去重不是已经保证不重复（698） interchangeable——698 另钉 item 1，本页钉 item 3 第一件事。313 mempool-indexer vs replay bundled unbundling 在本页 item 3 启动。

2. **看见幂等 / 看见那一小类幂等交易 / 看见 idempotent txs is not already 已经由内存池保证 interchangeable / 已经 mempool-guaranteed interchangeable / 已经池子保证幂等 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 700 indexer-notnoidempotent interchangeable / 313 mempool-indexer item 1 保证不重复 interchangeable / 313 mempool-indexer item 2 应用级保护 interchangeable，也不是已经通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事 bundled（313 item 3 余量） interchangeable / 313 mempool-indexer item 3 interchangeable，也不是已经没有幂等例外（本页第一件事） interchangeable。**  
   官方把那一小类幂等交易和已经由内存池保证幂等路径分开——看见幂等，不等于已经由内存池保证。看见幂等，不是已经由内存池保证 interchangeable——本页钉 not already mempool-guaranteed 单句。看见那一小类幂等交易，不是已经过了 CheckTx 不是已经有应用级保护（699） interchangeable——699 另钉 item 2，本页钉 item 3 第二件事。看见 idempotent txs，不是已经索引器去重不是已经保证不重复（698） interchangeable——698 另钉 item 1，本页钉 item 3 第二件事。313 mempool-indexer vs replay bundled unbundling 在本页 item 3 启动。

3. **看见官方说 undesirable / 看见规范点名通常不受欢迎 / 看见官方写下 undesirable is not already 已经规定不确定必须怎样写幂等 interchangeable / 已经 prescribed interchangeable / 已经不确定幂等公式已定 interchangeable / 313 mempool-indexer bundled interchangeable / 161 chainId interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 700 indexer-notnoidempotent interchangeable / 313 mempool-indexer item 1 / 313 mempool-indexer item 2，也不是已经通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事 bundled（313 item 3 余量） interchangeable / 313 mempool-indexer item 3 interchangeable，也不是已经没有幂等例外（本页第一件事） interchangeable / 已经由内存池保证（本页第二件事） interchangeable。**  
   官方把点名 undesirable 和已经规定不确定必须怎样写幂等路径分开——官方说通常不受欢迎，不等于已经规定不确定必须怎样写幂等。看见官方说 undesirable，不是已经规定不确定必须怎样写幂等 interchangeable——本页钉 not already prescribed 单句。看见规范点名通常不受欢迎，不是已经没有幂等例外（本页第一件事） interchangeable——三件事分开钉。看见官方写下 undesirable，不是已经 JSON chainId 已经编进签名哈希（161） interchangeable——161 另钉。313 mempool-indexer vs replay bundled unbundling 在本页 item 3 完成。

怎样实现重放保护、怎样做索引器、nonce 公式、怎样写幂等是规范里的取值或做法，本页不抄。Replay Protection bundled（313）、索引器去重不是已经保证不重复（313 item 1 余量 / 698）、过了 CheckTx 不是已经有应用级保护（313 item 2 余量 / 699）、CheckTxState vs ExecuteTxState（312）、提案收了已经从池里删掉（301）、JSON chainId（161）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **通常不受欢迎 not already no exceptions ≠ 313 / 312 interchangeable：** 官方把绝大多数通常不受欢迎单句和已经没有幂等例外路径分开。
- **看见幂等 not already mempool-guaranteed ≠ 已经由内存池保证 interchangeable：** 官方把那一小类幂等交易单句和已经由内存池保证路径分开。
- **官方说 undesirable not already prescribed ≠ 已经规定不确定必须怎样写幂等 interchangeable：** 官方把点名 undesirable 单句和已经规定不确定幂等写法路径分开；313 mempool-indexer vs replay bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 通常不受欢迎 | 不是 already no exceptions | 不是保证不重复 alone（698） |
| 看见幂等 | 不是 already mempool-guaranteed | 不是应用级保护 alone（699） |
| 官方说 undesirable | 不是 already prescribed | 不是 chainId alone（161） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常不受欢迎不是已经没有幂等例外 not already no exceptions / not already mempool-guaranteed / not already prescribed 正式三事（313 余量），必须分开通常不受欢迎 是不是 already no exceptions interchangeable / 313 mempool-indexer bundled interchangeable / indexer-sold-as-replay interchangeable、看见幂等 是不是 already mempool-guaranteed interchangeable、官方说 undesirable 是不是 already prescribed interchangeable。可以跳过「看见通常不受欢迎就已经没有例外 interchangeable / 就已经由内存池保证 interchangeable / 就已经规定怎样写幂等 interchangeable」。不要另写怎样写幂等。313 mempool-indexer vs replay bundled unbundling 在本页 item 3 完成（698 + 699 + 700）。

## 本页不抄

- 怎样实现重放保护、怎样做索引器、nonce 公式、怎样写幂等。
- Replay Protection bundled。那是不变量 313。
- 索引器去重不是已经保证不重复。那是不变量 313 item 1 余量 / 698。
- 过了 CheckTx 不是已经有应用级保护。那是不变量 313 item 2 余量 / 699。
- CheckTxState vs ExecuteTxState。那是不变量 312。
- 提案收了已经从池里删掉。那是不变量 301。
- JSON chainId 已经编进签名哈希。那是不变量 161。
- 四门已经结算。那是不变量 33。
