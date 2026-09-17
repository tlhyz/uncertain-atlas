# 例：看见 CheckTx may come from an external user is not already CheckTx_Recheck interchangeable / not already CheckTx_New bundled interchangeable / not already broadcast_tx once interchangeable

**层次**：实现 / CheckTx Usage may come from an external user not CheckTx_Recheck / not CheckTx_New bundled / not broadcast_tx once 正式三事（488 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage may come from an external user not CheckTx_Recheck / not CheckTx_New bundled / not broadcast_tx once 正式三事（488 余量）/ not 683 chktxsource-notrecheck interchangeable / not 488 chktxsource-vs-recheck bundled interchangeable」，不是 CheckTx Usage tx source 正式三事 bundled（488），也不是 CheckTx Request type 栏 bundled（484）或 Replay Protection（313）。不要另写怎样挑邻居、怎样做索引器。

## 官方三件事

规范把 CheckTx Usage 里 The transaction may come from an external user 和「已经 CheckTx_Recheck 那种内存池正常再验（484） interchangeable / 已经 CheckTx_New default full check（484） bundled 就代表来源已经验完 interchangeable / 已经 RPC broadcast_tx 就代表全网只收一次（313 bundled） interchangeable」分开写成三件独立的实现事，不是「看见能来自外部用户 就已经 Recheck interchangeable / 就已经 New bundled interchangeable / 就已经 broadcast_tx once interchangeable」一件事：

1. **看见 The transaction may come from an external user / 看见能来自外部用户 / external user is not already 已经 `CheckTx_Recheck` 那种内存池正常再验（484） interchangeable / 484 chktxtype Recheck interchangeable / 已经 Type=RECHECK interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 683 chktxsource-notrecheck interchangeable / 684 chktxsource-notremoved interchangeable / 488 chktxsource item 2 another node interchangeable，也不是已经 may come from an external user not CheckTx_Recheck / not CheckTx_New bundled / not broadcast_tx once 正式三事 bundled（488 item 1 余量） interchangeable / 488 chktxsource item 1 interchangeable。**  
   官方 Usage 写：The transaction may come from an external user or another node。看见 may come from an external user，不是已经 CheckTx_Recheck types are used when the mempool is initiating a normal recheck interchangeable——484 钉 Request type 栏 Recheck，本页从 488 item 1 侧钉 not Recheck 单句。488 chktxsource vs recheck bundled unbundling 在本页 item 1 启动。

2. **看见 may come from an external user / 能来自外部用户 / 看见送来了 is not already 已经 `CheckTx_New` default full check（484） bundled 就代表来源已经验完 interchangeable / 484 chktxtype New interchangeable / 已经 tx 栏就知道 New vs Recheck interchangeable / 已经 CheckTx 请求 `tx` 是请求交易字节（391） bundled interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 683 chktxsource-notrecheck interchangeable / 488 chktxsource item 3 replay interchangeable / 685 chktxsource-notreplay interchangeable。**  
   官方把 Usage 外部用户来源单句和 Request type New bundled 路径分开——488 bundled 第一件事常与 484 混成「看见能来自用户 就已经 New bundled 就代表来源验完 interchangeable」，本页钉 not CheckTx_New bundled 单句。看见外部用户送来，不是已经 tx 栏就分清 New vs Recheck interchangeable——391 钉 tx 栏，本页钉 Usage 外部用户来源。

3. **看见 may come from an external user / 看见能来自用户 / 看见外部用户送来 is not already 已经 RPC `broadcast_tx` 就代表全网只收一次（313 bundled） interchangeable / 313 replay interchangeable / 已经内存池索引器滤过 interchangeable / 已经全网只收一次 interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 683 chktxsource-notrecheck interchangeable / 684 chktxsource-notremoved interchangeable。**  
   官方把 Usage 外部用户来源单句和 broadcast_tx 全网只收一次路径分开——488 bundled 第一件事常与 313 混成「看见外部用户送来 就已经全网只收一次 interchangeable」，本页钉 not broadcast_tx once 单句。看见能来自用户，不是已经内存池去重就保证不重放 interchangeable——313 钉 Replay Protection，本页钉 Usage item 1。488 chktxsource vs recheck bundled unbundling 在本页 item 1 启动。

怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx Usage tx source 正式三事 bundled（488）、may come from another node（488 item 2 余量 / 684）、external user or another node not replay（488 item 3 余量 / 685）、CheckTx Request type（484）、Replay Protection（313）是另外那套，本页不抄。

## 官方为什么这样拆

- **may come from external user not CheckTx_Recheck ≠ 484 Recheck interchangeable：** 官方把 Methods Usage 外部用户来源和 Request type Recheck 分开。
- **may come from external user not CheckTx_New bundled ≠ 484 New interchangeable：** 官方把 Usage 外部用户来源单句和 New bundled 就代表来源验完路径分开。
- **may come from external user not broadcast_tx once ≠ 313 bundled interchangeable：** 官方把 Usage 外部用户来源单句和 RPC 全网只收一次路径分开；488 chktxsource vs recheck bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| may come from external user | 不是 CheckTx_Recheck（484） | 不是 another node（684/488 item 2） |
| 能来自外部用户 | 不是 CheckTx_New bundled（484） | 不是 Request type 栏（484） |
| 看见外部用户送来 | 不是 broadcast_tx 全网只收一次（313） | 不是 already 保证不重放（685/488 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from an external user not CheckTx_Recheck / not CheckTx_New bundled / not broadcast_tx once 正式三事（488 余量），必须分开 external user 是不是 Recheck interchangeable / 484、是不是 New bundled 就代表来源验完 interchangeable / 484、是不是 broadcast_tx 全网只收一次 interchangeable / 313。可以跳过「看见送来了就已经是 Recheck」。不要另写怎样挑邻居。488 chktxsource vs recheck bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxsource-notremoved-vs-bundled.md`](worked-example-chktxsource-notremoved-vs-bundled.md)（不变量 684 item 2）。

## 本页不抄

- 怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx Usage tx source 正式三事 bundled。那是不变量 488。
- may come from another node。那是不变量 488 item 2 余量 / 684。
- external user or another node not replay。那是不变量 488 item 3 余量 / 685。
- CheckTx_New / CheckTx_Recheck / Request type 栏。那是不变量 484。
- 内存池去重 / 应用级重放保护。那是不变量 313。
