# 例：看见 ApplySnapshotChunk Result RETRY is not already refetch_chunks regardless interchangeable / not already complete interchangeable / not already applysnapusage refetch bundled interchangeable

**层次**：实现 / ApplySnapshotChunk Result RETRY not refetch regardless / not already complete / not applysnapusage refetch 正式三事（398 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Result RETRY not refetch regardless / not already complete / not applysnapusage refetch 正式三事（398 余量）/ not 719 applyretry-notrefetch interchangeable / not 398 applyretry-vs-refetch bundled interchangeable」，不是 ApplySnapshotChunk 结果枚举 bundled（398），也不是 refetch_chunks 不论 result 都再拉再装就已经齐（378）或 Apply Usage refetch/ban（502）。不要另写怎样写 ApplySnapshotChunk 结果枚举。

## 官方三件事

1. **看见 ApplySnapshotChunk Result `RETRY` 是再装这块、按需配合 RefetchChunks 和 RejectSenders / 看见回了 RETRY / RETRY is not already 已经 refetch_chunks 不论 result 都再拉再装 interchangeable / 378 refetch interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 719 applyretry-notrefetch interchangeable / 720 applyretry-notswitch interchangeable / 398 applyretry item 2 RETRY_SNAPSHOT interchangeable，也不是已经 RETRY not refetch regardless / not already complete / not applysnapusage refetch 正式三事 bundled（398 item 1 余量） interchangeable / 398 applyretry item 1 interchangeable。**  
   官方 Data Types 写：RETRY 是再装这块，按需配合 RefetchChunks 和 RejectSenders。看见回了 RETRY，不是已经 refetch_chunks 不论 result 都再拉再装 interchangeable——本页从 398 item 1 侧钉 not refetch regardless 单句。398 applyretry vs refetch bundled unbundling 在本页 item 1 启动。

2. **看见回了 RETRY / 看见能再装 / RETRY is not already 已经齐 interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 719 applyretry-notrefetch interchangeable / 398 applyretry item 3 REJECT_SNAPSHOT interchangeable / 721 applyretry-notchunkresult interchangeable。**  
   官方把 RETRY 再装这块和已经齐分开——398 bundled 第一件事常与「看见回了 RETRY 就已经齐 interchangeable」糊成一句，本页钉 not already complete 单句。

3. **看见回了 RETRY / 看见 Usage 这句 / RETRY is not already 已经 Apply Usage refetch/ban bundled（502） interchangeable / 502 applysnapusage interchangeable / 656 applysnapusage-notchoose interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 719 applyretry-notrefetch interchangeable / 720 applyretry-notswitch interchangeable。**  
   官方把 Result RETRY 枚举和 Usage refetch/ban 指令分开。看见回了 RETRY，不是已经 502 交差 interchangeable。398 applyretry vs refetch bundled unbundling 在本页 item 1 启动。

怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **RETRY not refetch regardless ≠ 378 interchangeable：** 官方把 RETRY 再装这块和 refetch_chunks 不论 result 都再拉分开。
- **RETRY not already complete ≠ 已经齐 interchangeable：** 官方把能再装和已经齐分开。
- **RETRY not applysnapusage refetch ≠ 502 interchangeable：** 官方把 Result RETRY 和 Usage refetch/ban 分开；398 applyretry vs refetch bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders | 不是已经 refetch 不论 result（378） | 不是 RETRY_SNAPSHOT 重来这份（720/398 item 2） |
| 看见回了 RETRY | 不是已经齐 | 不是 ApplySnapshotChunk 结果枚举 bundled（398） |
| 看见能再装 | 不是 Apply Usage refetch/ban（502） | 不是 REJECT_SNAPSHOT 拒掉这份（721/398 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result RETRY not refetch regardless / not already complete / not applysnapusage refetch 正式三事（398 余量），必须分开 RETRY 是不是已经 refetch 不论 result interchangeable / 378、是不是已经齐、是不是 Usage refetch/ban interchangeable / 502。可以跳过「看见回了 RETRY 就已经再拉」。不要另写怎样写 ApplySnapshotChunk 结果枚举。398 applyretry vs refetch bundled unbundling 在本页 item 1 启动；续 [`worked-example-applyretry-notswitch-vs-bundled.md`](worked-example-applyretry-notswitch-vs-bundled.md)（不变量 720 item 2）。

## 本页不抄

- 怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT。
- ApplySnapshotChunk 结果枚举 bundled。那是不变量 398。
- RETRY_SNAPSHOT 从 OfferSnapshot 重来这份。那是不变量 398 item 2 余量 / 720。
- REJECT_SNAPSHOT 拒掉这份、换一份。那是不变量 398 item 3 余量 / 721。
- refetch_chunks 不论 result 都再拉再装就已经齐。那是不变量 378。
- Apply Usage refetch/ban bundled。那是不变量 502。
