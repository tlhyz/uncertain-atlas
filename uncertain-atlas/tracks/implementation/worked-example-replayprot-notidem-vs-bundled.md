# 例：看见多数交易再发一次通常不受欢迎 is not already no-exception interchangeable / not already pool-guaranteed interchangeable / not already settled interchangeable

**层次**：实现 / 通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量）/ not 967 replayprot-notidem interchangeable / not 313 mempool-indexer-vs-replay bundled interchangeable」，不是重放 bundled（313），也不是 JSON chainId 已经编进签名哈希（161），也不是 QueryState 已经是 ExecuteTxState（314/962）。不要另写怎样实现重放保护或怎样做索引器。

## 官方三件事

1. **看见多数交易再发一次通常不受欢迎 / 看见官方说 undesirable 这份说法 is not already 已经没有幂等例外 interchangeable，也不是已经重放 bundled（313） interchangeable / 967 replayprot-notidem interchangeable / 965 replayprot-notguar interchangeable / 966 replayprot-notapp interchangeable / 313 replayprot item 1 内存池去重 interchangeable，也不是已经通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事 bundled（313 item 3 余量） interchangeable / 313 replayprot item 3 interchangeable。**  
   官方写：旧交易再送来，对绝大多数交易通常不受欢迎，除了一般很小的那一类幂等交易。看见通常不受欢迎，不是已经没有例外 interchangeable——本页从 313 item 3 侧钉 not already no-exception 单句。313 replayprot vs replay bundled unbundling 在本页 item 3 完成。

2. **看见幂等 / 看见通常不受欢迎 / 这份说法 is not already 已经由内存池保证 interchangeable，也不是已经重放 bundled（313） interchangeable / 967 replayprot-notidem interchangeable / 313 replayprot item 2 过了 CheckTx interchangeable / 966 replayprot-notapp interchangeable，也不是已经 JSON chainId 已经编进签名哈希 interchangeable / 161 chainid interchangeable。**  
   官方把幂等和已经由内存池保证分开。看见幂等，不是已经由内存池保证 interchangeable。本页钉 not already pool-guaranteed 单句。

3. **看见官方点名 undesirable / 看见通常不受欢迎 / 这份说法 is not already 已经交差 interchangeable，也不是已经重放 bundled（313） interchangeable / 967 replayprot-notidem interchangeable / 965 replayprot-notguar interchangeable，也不是已经 QueryState 已经是 ExecuteTxState interchangeable / 314/962 querystate-notexec interchangeable。**  
   官方把点名 undesirable 和已经规定不确定必须怎样写幂等分开。看见官方点名 undesirable，不是已经交差 interchangeable。313 replayprot vs replay bundled unbundling 在本页 item 3 完成。

怎样实现重放保护、怎样做索引器、nonce 公式是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **通常不受欢迎 not already no-exception ≠ 已经没有幂等例外 interchangeable：** 官方把绝大多数交易和那一小类幂等交易分开。
- **看见幂等 not already pool-guaranteed ≠ 已经由内存池保证 interchangeable：** 官方把幂等和已经由内存池保证分开。
- **看见官方点名 undesirable not already settled ≠ 已经交差 interchangeable：** 官方把点名 undesirable 和已经规定不确定必须怎样写幂等分开；313 replayprot vs replay bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 通常不受欢迎 | 不是已经没有幂等例外 | 不是 JSON chainId 已经编进签名哈希（161） |
| 看见幂等 | 不是已经由内存池保证 | 不是 QueryState 已经是 ExecuteTxState（314/962） |
| 看见官方点名 undesirable | 不是已经交差 | 不是内存池去重就已经保证不重复（965） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量），必须分开是不是已经没有例外、是不是已经由内存池保证、是不是已经交差。可以跳过「看见池子挡过就已经保证不重放」。不要另写怎样实现重放保护或怎样做索引器。313 replayprot vs replay bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现重放保护、怎样做索引器、nonce 公式。
- 重放 bundled。那是不变量 313。
- JSON chainId 已经编进签名哈希。那是不变量 161。
- QueryState 已经是 ExecuteTxState。那是不变量 314/962。
