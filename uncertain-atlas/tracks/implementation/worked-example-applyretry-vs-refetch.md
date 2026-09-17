# 例：看见 ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 不是已经再拉；看见 ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块不是已经换一份；看见 ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份不是已经是装这块的结果

**层次**：实现 / ApplySnapshotChunk 结果枚举。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 不是已经再拉 / ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块不是已经换一份 / ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份不是已经是装这块的结果」，不是 refetch_chunks 不论 result 都再拉再装就已经齐，也不是 Offer 收下就已经装完。不要另写怎样写 ApplySnapshotChunk 结果枚举。

## 官方三件事

规范把 ApplySnapshotChunk Result `RETRY` 是再装这块、按需配合 RefetchChunks 和 RejectSenders、`RETRY_SNAPSHOT` 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块、`REJECT_SNAPSHOT` 是拒掉这份、换一份写成三件独立的实现事，不是「看见回了 ApplySnapshotChunk 结果枚举就已经再拉、已经换一份、已经是装这块的结果」一件事：

1. **看见 ApplySnapshotChunk Result `RETRY` 是再装这块、按需配合 RefetchChunks 和 RejectSenders / 看见回了 RETRY 不是已经再拉，也不是已经齐。**  
   官方写：`RETRY` 是再装这块，按需配合 `RefetchChunks` 和 `RejectSenders`。看见回了 RETRY，不是已经 `refetch_chunks` 不论 result 都再拉再装。看见能再装，不是已经齐。看见能回，不是已经交差。
2. **看见 ApplySnapshotChunk Result `RETRY_SNAPSHOT` 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块 / 看见回了 RETRY_SNAPSHOT 不是已经换一份，也不是已经装完。**  
   官方写：`RETRY_SNAPSHOT` 是从 `OfferSnapshot` 重来这份，除非另有指令否则复用已拉块。看见回了 RETRY_SNAPSHOT，不是已经拉失败换一份就已经能接着装。看见能重来这份，不是已经装完。看见能回，不是已经交差。
3. **看见 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 是拒掉这份、换一份 / 看见回了 REJECT_SNAPSHOT 不是已经是装这块的结果，也不是已经拒了人。**  
   官方写：`REJECT_SNAPSHOT` 是拒掉这份，换一份。看见回了 REJECT_SNAPSHOT，不是已经是 ApplySnapshotChunk 回包 result 那份装这块的结果。看见能换一份，不是已经 `reject_senders` 拒了人。看见能回，不是已经交差。

怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT 是规范里的做法，本页不抄。refetch_chunks 不论 result 都再拉再装就已经齐是不变量 378，本页不抄。

## 官方为什么这样拆

- **ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders ≠ 已经再拉：** 官方把再装这块和不论 result 都再拉分开。
- **ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块 ≠ 已经换一份：** 官方把重来这份和拉失败换一份分开。
- **ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份 ≠ 已经是装这块的结果：** 官方把拒掉这份和装这块的结果字段分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders | 不是已经再拉 | 不是 refetch_chunks 不论 result 都再拉再装就已经齐（378） |
| ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块 | 不是已经换一份 | 不是拉失败换一份就已经能接着装（321） |
| ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份 | 不是已经是装这块的结果 | 不是 ApplySnapshotChunk 回包 result 是装这块的结果就已经是 Offer 的结果（397） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 ApplySnapshotChunk 结果枚举就已经再拉、已经换一份、已经是装这块的结果」，必须分开 ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 是不是已经再拉、ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块是不是已经换一份、ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份是不是已经是装这块的结果。可以跳过「看见回了 ApplySnapshotChunk 结果枚举就已经再拉」。不要另写怎样写 ApplySnapshotChunk 结果枚举。398 applyretry vs refetch bundled unbundling 完成（719 item 1 / 720 item 2 / 721 item 3）；精读 [`worked-example-applyretry-notrefetch-vs-bundled.md`](worked-example-applyretry-notrefetch-vs-bundled.md)（不变量 719 item 1）。

## 本页不抄

- 怎样写 ApplySnapshotChunk 结果枚举、怎样挑 RETRY、怎样挑 RETRY_SNAPSHOT。
- refetch_chunks 不论 result 都再拉再装就已经齐。那是不变量 378。
- 拉失败换一份就已经能接着装。那是不变量 321。
- ApplySnapshotChunk 回包 result 是装这块的结果就已经是 Offer 的结果。那是不变量 397。
