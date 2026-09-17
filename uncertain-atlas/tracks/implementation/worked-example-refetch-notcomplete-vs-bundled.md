# 例：看见 refetch_chunks 不论 result 都再拉再装 is not already complete interchangeable / not already settled interchangeable / not already same snapshot interchangeable

**层次**：实现 / refetch_chunks not already complete / not already settled / not already same snapshot 正式三事（378 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「refetch_chunks not already complete / not already settled / not already same snapshot 正式三事（378 余量）/ not 795 refetch-notcomplete interchangeable / not 378 refetch-vs-restored bundled interchangeable」，不是 ApplySnapshotChunk 再拉 bundled（378），也不是封禁邻居就已经没有快照 DoS（332），也不是 RETRY 就已经 refetch 不论 result（398/719），也不是 LoadSnapshotChunk 就已经齐（375）。不要另写怎样写 ApplySnapshotChunk。

## 官方三件事

1. **看见 `refetch_chunks` 不论 `result` 都再拉再装、按顺序 / 看见列了块号 / 这份再拉 is not already 已经齐 interchangeable / 332 snapshotverify interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 795 refetch-notcomplete interchangeable / 794 refetch-notbanned interchangeable / 378 refetch item 1 引擎不自己做 interchangeable，也不是已经 refetch_chunks not already complete / not already settled / not already same snapshot 正式三事 bundled（378 item 2 余量） interchangeable / 378 refetch item 2 interchangeable。**  
   官方写：`refetch_chunks` 不论 `result` 是什么，都会再拉并列出来的那些块，再按顺序装回去。只拉列出来的那些。看见列了块号，不是已经齐 interchangeable——本页从 378 item 2 侧钉 not already complete 单句。378 refetch vs restored bundled unbundling 在本页 item 2 续。

2. **看见列了块号 / 看见再装 / 这份再拉 is not already 已经交差 interchangeable / 332 snapshotverify interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 795 refetch-notcomplete interchangeable / 378 refetch item 3 reject_senders interchangeable / 796 refetch-notcontinue interchangeable，也不是已经 RETRY 就已经 refetch 不论 result interchangeable / 398 applyretry / 719 applyretry-notrefetch interchangeable，也不是已经 LoadSnapshotChunk 就已经齐 interchangeable / 375 loadchunk interchangeable。**  
   官方把再装和已经交差分开——378 bundled 第二件事常与 332 / 398 / 375 混成「看见列了块号就已经齐或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见列了块号 / 看见按顺序 / 这份再拉 is not already 已经是同一份 interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 795 refetch-notcomplete interchangeable / 794 refetch-notbanned interchangeable。**  
   官方把按顺序和已经是同一份分开。看见按顺序，不是已经是同一份 interchangeable。378 refetch vs restored bundled unbundling 在本页 item 2 续。

怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居是规范里的做法，本页不抄。

## 官方为什么这样拆

- **refetch_chunks not already complete ≠ 332 interchangeable：** 官方把再拉并列块和已经齐分开。
- **看见再装 not already settled ≠ 已经交差 interchangeable：** 官方把再装和已经交差分开。
- **看见按顺序 not already same snapshot ≠ 已经是同一份 interchangeable：** 官方把按顺序和已经是同一份分开；378 refetch vs restored bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| refetch_chunks 不论 result 都再拉再装 | 不是已经齐（332） | 不是引擎不自己做（794/378 item 1） |
| 看见列了块号 | 不是已经交差 | 不是 RETRY（398/719） |
| 看见按顺序 | 不是已经是同一份 | 不是 LoadSnapshotChunk 就已经齐（375） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 refetch_chunks not already complete / not already settled / not already same snapshot 正式三事（378 余量），必须分开是不是已经齐 interchangeable / 332、是不是已经交差、是不是已经是同一份。可以跳过「看见列了块号就已经齐」。不要另写怎样写 ApplySnapshotChunk。378 refetch vs restored bundled unbundling 在本页 item 2 续；续 [`worked-example-refetch-notcontinue-vs-bundled.md`](worked-example-refetch-notcontinue-vs-bundled.md)（不变量 796 item 3）。

## 本页不抄

- 怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居。
- ApplySnapshotChunk 再拉 bundled。那是不变量 378。
- 引擎不自己做。那是不变量 378 item 1 余量 / 794。
- RETRY 就已经 refetch 不论 result。那是不变量 398 / 719。
- LoadSnapshotChunk 就已经齐。那是不变量 375。
