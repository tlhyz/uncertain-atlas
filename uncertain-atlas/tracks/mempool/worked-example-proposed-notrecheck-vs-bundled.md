# 例：看见本块已 commit is not already skip-recheck interchangeable / not already empty interchangeable / not already forever interchangeable

**层次**：共识 / 本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量）/ not 993 proposed-notrecheck interchangeable / not 301 proposed-vs-removed bundled interchangeable」，不是内存池交接 bundled（301），也不是单笔 CheckTx 绿已经整包可提案（69），也不是 CheckTx 状态就已经是 ExecuteTxState（312）。不要另写怎样加锁、怎样 flush、怎样再验。

## 官方三件事

1. **看见块已经 commit / 看见本块交易从池里去掉 这份交接 is not already 已经不用再验剩下的 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 993 proposed-notrecheck interchangeable / 992 proposed-notdel interchangeable / 301 proposed item 1 提案收了 interchangeable，也不是已经本块已 commit not already skip-recheck / not already empty / not already forever 正式三事 bundled（301 item 2 余量） interchangeable / 301 proposed item 2 interchangeable。**  
   官方写：块决定之后，本块里的交易才从池里去掉。还留在池里的，要按应用的新状态再验一遍。看见 commit 了，不是剩下的已经不用再验 interchangeable——本页从 301 item 2 侧钉 not already skip-recheck 单句。301 proposed vs removed bundled unbundling 在本页 item 2 续。

2. **看见本块交易没了 / 看见 commit / 这份交接 is not already 池已经空了 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 993 proposed-notrecheck interchangeable / 301 proposed item 3 CheckTx 绿 interchangeable / 994 proposed-notforever interchangeable，也不是已经单笔 CheckTx 绿已经整包可提案 interchangeable / 69 package interchangeable。**  
   官方把本块交易从池里去掉和池已经空了分开。看见本块交易没了，不是池已经空了 interchangeable。本页钉 not already empty 单句。

3. **看见再验开始了 / 看见 commit / 这份交接 is not already 剩下的已经永远有效 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 993 proposed-notrecheck interchangeable / 992 proposed-notdel interchangeable，也不是已经 CheckTx 状态就已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把再验开始了和剩下的已经永远有效分开。看见再验开始了，不是剩下的已经永远有效 interchangeable。301 proposed vs removed bundled unbundling 在本页 item 2 续。

实现名单、加锁、flush、再验次数是规范里的做法或取值，本页不抄。

## 官方为什么这样拆

- **本块已 commit not already skip-recheck ≠ 已经不用再验剩下的 interchangeable：** 官方把去掉本块交易和按新状态再验剩下的分开。
- **看见本块交易没了 not already empty ≠ 池已经空了 interchangeable：** 官方把本块交易从池里去掉和池已经空了分开。
- **看见再验开始了 not already forever ≠ 剩下的已经永远有效 interchangeable：** 官方把再验开始了和剩下的已经永远有效分开；301 proposed vs removed bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 本块已 commit | 不是已经不用再验剩下的 | 不是单笔 CheckTx 绿已经整包可提案（69） |
| 看见本块交易没了 | 不是池已经空了 | 不是 CheckTx 状态就已经是 ExecuteTxState（312） |
| 看见再验开始了 | 不是剩下的已经永远有效 | 不是曾经绿过就已经永远有效（994） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本块已 commit not already skip-recheck / not already empty / not already forever 正式三事（301 余量），必须分开是不是已经不用再验剩下的、是不是池已经空了、是不是剩下的已经永远有效。可以跳过「看见提案收了就已经从池里拿走」。不要另写怎样加锁、怎样 flush、怎样再验。301 proposed vs removed bundled unbundling 在本页 item 2 续；续 [`worked-example-proposed-notforever-vs-bundled.md`](worked-example-proposed-notforever-vs-bundled.md)（不变量 994 item 3）。

## 本页不抄

- 实现名单、加锁、flush、再验次数。
- 内存池交接 bundled。那是不变量 301。
- 单笔 CheckTx 绿已经整包可提案。那是不变量 69。
- CheckTx 状态就已经是 ExecuteTxState。那是不变量 312。
