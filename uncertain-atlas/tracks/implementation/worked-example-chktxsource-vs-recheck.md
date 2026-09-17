# 例：看见 may come from an external user 不是已经 CheckTx_Recheck；看见 may come from another node 不是已经从池里删掉；看见 external user or another node 不是已经保证不重放

**层次**：实现 / CheckTx Usage tx source 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「may come from external user 不是 CheckTx_Recheck / may come from another node 不是已经从池里删掉 / external user or another node 不是已经保证不重放」，不是 CheckTx 守卫余量 bundled（405），也不是 CheckTx Request type 栏 bundled（484）。不要另写怎样挑邻居、怎样做索引器。

## 官方三件事

规范把 CheckTx Usage 里 The transaction may come from an external user or another node 写成三件独立的实现事，不是「看见送来了就已经是 Recheck、已经从池里删掉、已经保证不重放」一件事：

1. **看见 The transaction may come from an external user / 看见能来自外部用户 不是已经 `CheckTx_Recheck` 那种内存池正常再验（484） interchangeable，也不是已经 `CheckTx_New` default full check（484） bundled 就代表来源已经验完，也不是已经 RPC `broadcast_tx` 就代表全网只收一次（313 bundled）。**  
   官方 Usage 写：The transaction may come from an external user or another node。看见 may come from an external user，不是已经 `CheckTx_Recheck` types are used when the mempool is initiating a normal recheck interchangeable——484 钉 Request type 栏 Recheck，本页钉 Methods CheckTx Usage 外部用户来源。看见能来自用户，不是已经 CheckTx 请求 `tx` 是请求交易字节（391） bundled 就代表 New vs Recheck 已经分清 interchangeable。看见外部用户送来，不是已经内存池索引器滤过（313）那种尽力去重 interchangeable。
2. **看见 The transaction may come from another node / 看见能来自另一节点 不是已经流言广播就代表来源已经验过，也不是已经从池里删掉 / 提案收了（301） interchangeable，也不是已经 CheckTx 过了就永远有效（301）。**  
   官方 Usage 写：The transaction may come from an external user or another node。看见 may come from another node，不是已经 P2P 流言就代表全网已经验过 interchangeable。看见能来自邻居，不是已经提案收了就从池里删掉（301） interchangeable——301 钉 mempool 交接，本页钉 Usage 邻居来源。看见邻居送来，不是已经 CheckTx 过了就永远有效（301） interchangeable。看见另一节点，不是已经 CheckTx 是内存池守卫（405） bundled 第一句就代表来源已经交差 interchangeable。
3. **看见 The transaction may come from an external user or another node / 看见送来了 不是已经内存池去重那种保证不重放（313） interchangeable，也不是已经过了 CheckTx 就有应用级重放保护（313），也不是已经 CheckTx 守卫余量（405） bundled 第二句 interchangeable。**  
   官方把 may come from external user or another node 和 mempool replay protection 分开写。App requirements Replay Protection 写：旧交易有可能再被送给应用；内存池去重只是尽力、不提供强保证；应用必须在 CheckTx 里自己实现带强保证的重放保护（313）。看见送来了，不是已经内存池去重就保证不重放 interchangeable。看见能来自用户或邻居，不是已经过了 CheckTx 就有应用级保护 interchangeable。看见 Usage 这句，不是已经 CheckTx 守卫余量（405） bundled 第二件事 interchangeable——405 钉守卫余量语境，本页钉 Usage 侧 tx source 语义。

怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx 守卫余量（405）、CheckTx Request type（484）、Replay Protection（313）是另外那套，本页不抄。

## 官方为什么这样拆

- **may come from external user ≠ CheckTx_Recheck / tx 栏就知道 New：** 官方把 Methods Usage 外部用户来源和 Request type Recheck / tx 栏分开。
- **may come from another node ≠ 已经从池里删掉 / CheckTx 过了就永远有效：** 官方把邻居来源和 mempool 交接、forever valid 分开。
- **may come from external user or another node ≠ 已经保证不重放 / CheckTx 守卫 bundled interchangeable：** 官方把 Usage tx source 和 Replay Protection / 405 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| may come from external user | 不是 CheckTx_Recheck | 不是 CheckTx Request type 栏（484） |
| may come from another node | 不是已经从池里删掉 | 不是提案收了 / CheckTx 过了就永远有效（301） |
| external user or another node | 不是已经保证不重放 | 不是 CheckTx 守卫余量 bundled（405） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见送来了就已经是 Recheck、已经从池里删掉、已经保证不重放」，必须分开 may come from external user 是不是 CheckTx_Recheck、may come from another node 是不是已经从池里删掉 / CheckTx 过了就永远有效、external user or another node 是不是已经保证不重放 / CheckTx 守卫 bundled interchangeable。可以跳过「看见送来了就已经是 Recheck」。不要另写怎样挑邻居。

## 本页不抄

- 怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx 是内存池守卫 / 每条节点先跑 CheckTx。那是不变量 405。
- CheckTx_New / CheckTx_Recheck / Request type 栏。那是不变量 484。
- 内存池去重 / 应用级重放保护。那是不变量 313。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
- CheckTx 请求 tx 栏 bundled。那是不变量 391。
