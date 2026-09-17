# 例：看见 ApplySnapshotChunk Result REJECT_SNAPSHOT is not already this-chunk result interchangeable / not already rejected senders interchangeable / not already Offer REJECT_FORMAT interchangeable

**层次**：实现 / ApplySnapshotChunk Result REJECT_SNAPSHOT not this-chunk result / not rejected senders / not Offer REJECT_FORMAT 正式三事（398 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Result REJECT_SNAPSHOT not this-chunk result / not rejected senders / not Offer REJECT_FORMAT 正式三事（398 余量）/ not 721 applyretry-notchunkresult interchangeable / not 398 applyretry-vs-refetch bundled interchangeable」，不是 ApplySnapshotChunk 结果枚举 bundled（398），也不是 ApplySnapshotChunk 回包 result 是装这块的结果就已经是 Offer 的结果（397）或 Offer REJECT_FORMAT（400）。不要另写怎样写 ApplySnapshotChunk 结果枚举。

## 官方三件事

1. **看见 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 是拒掉这份、换一份 / 看见回了 REJECT_SNAPSHOT / REJECT_SNAPSHOT is not already 已经是 ApplySnapshotChunk 回包 result 那份装这块的结果 interchangeable / 397 applyresult interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 721 applyretry-notchunkresult interchangeable / 719 applyretry-notrefetch interchangeable / 398 applyretry item 1 RETRY interchangeable，也不是已经 REJECT_SNAPSHOT not this-chunk result / not rejected senders / not Offer REJECT_FORMAT 正式三事 bundled（398 item 3 余量） interchangeable / 398 applyretry item 3 interchangeable。**  
   官方 Data Types 写：REJECT_SNAPSHOT 是拒掉这份，换一份。看见回了 REJECT_SNAPSHOT，不是已经是装这块的结果 interchangeable——本页从 398 item 3 侧钉 not this-chunk result 单句。398 applyretry vs refetch bundled unbundling 在本页 item 3 完成。

2. **看见回了 REJECT_SNAPSHOT / 看见能换一份 / REJECT_SNAPSHOT is not already 已经 reject_senders 拒了人 interchangeable / 378 refetch interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 721 applyretry-notchunkresult interchangeable / 398 applyretry item 2 RETRY_SNAPSHOT interchangeable / 720 applyretry-notswitch interchangeable。**  
   官方把拒掉这份和拒了人分开——398 bundled 第三件事常与「看见换一份就已经拒了人 interchangeable」糊成一句，本页钉 not rejected senders 单句。

3. **看见回了 REJECT_SNAPSHOT / 看见 Usage 这句 / REJECT_SNAPSHOT is not already 已经 OfferSnapshot Result REJECT_FORMAT 那种拒掉这种 format（400） interchangeable / 400 offerfmt interchangeable，也不是已经 ApplySnapshotChunk 结果枚举 bundled（398） interchangeable / 721 applyretry-notchunkresult interchangeable / 719 applyretry-notrefetch interchangeable。**  
   官方把 Apply REJECT_SNAPSHOT 拒掉这份和 Offer REJECT_FORMAT 拒掉这种 format 分开。看见能换一份，不是已经 400 交差 interchangeable。398 applyretry vs refetch bundled unbundling 在本页 item 3 完成。

怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **REJECT_SNAPSHOT not this-chunk result ≠ 397 interchangeable：** 官方把拒掉这份和装这块的结果分开。
- **REJECT_SNAPSHOT not rejected senders ≠ 378 interchangeable：** 官方把拒掉这份和拒了人分开。
- **REJECT_SNAPSHOT not Offer REJECT_FORMAT ≠ 400 interchangeable：** 官方把 Apply 拒掉这份和 Offer 拒掉这种 format 分开；398 applyretry vs refetch bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT_SNAPSHOT 是拒掉这份、换一份 | 不是已经是装这块的结果（397） | 不是 RETRY 再装这块（719/398 item 1） |
| 看见回了 REJECT_SNAPSHOT | 不是已经拒了人（378） | 不是 ApplySnapshotChunk 结果枚举 bundled（398） |
| 看见能换一份 | 不是 Offer REJECT_FORMAT（400） | 不是 RETRY_SNAPSHOT 重来这份（720/398 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result REJECT_SNAPSHOT not this-chunk result / not rejected senders / not Offer REJECT_FORMAT 正式三事（398 余量），必须分开 REJECT_SNAPSHOT 是不是已经是装这块的结果 interchangeable / 397、是不是已经拒了人 interchangeable / 378、是不是 Offer REJECT_FORMAT interchangeable / 400。可以跳过「看见回了 REJECT_SNAPSHOT 就已经是装这块的结果」。不要另写怎样写 ApplySnapshotChunk 结果枚举。398 applyretry vs refetch bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT。
- ApplySnapshotChunk 结果枚举 bundled。那是不变量 398。
- RETRY 再装这块。那是不变量 398 item 1 余量 / 719。
- RETRY_SNAPSHOT 从 OfferSnapshot 重来这份。那是不变量 398 item 2 余量 / 720。
- ApplySnapshotChunk 回包 result 是装这块的结果就已经是 Offer 的结果。那是不变量 397。
- OfferSnapshot Result REJECT_FORMAT。那是不变量 400。
