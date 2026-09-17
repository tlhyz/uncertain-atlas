# 例：看见 reject_senders 不论 Result 都拒这些人 is not already can continue interchangeable / not already halted interchangeable / not already complete interchangeable

**层次**：实现 / reject_senders not already can continue / not already halted / not already complete 正式三事（378 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「reject_senders not already can continue / not already halted / not already complete 正式三事（378 余量）/ not 796 refetch-notcontinue interchangeable / not 378 refetch-vs-restored bundled interchangeable」，不是 ApplySnapshotChunk 再拉 bundled（378），也不是 LoadSnapshotChunk 就已经齐（375），也不是 REJECT_SENDER 就已经拒了人（400/723），也不是 Apply 请求 sender 就已经拒了人（397/741）。不要另写怎样写 ApplySnapshotChunk。

## 官方三件事

1. **看见 `reject_senders` 不论 `Result` 都拒这些人、已装的不重拉除非点名 / 看见拒了人 / 这份拒人 is not already 已经能接着装 interchangeable / 375 loadchunk interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 796 refetch-notcontinue interchangeable / 794 refetch-notbanned interchangeable / 378 refetch item 1 引擎不自己做 interchangeable，也不是已经 reject_senders not already can continue / not already halted / not already complete 正式三事 bundled（378 item 3 余量） interchangeable / 378 refetch item 3 interchangeable。**  
   官方写：`reject_senders` 不论 `Result` 是什么，都拒这些 P2P 发送者。已经装上的块不会重拉，除非明确点名。这些人排队的块会丢掉，新块或其他快照也会拒。看见拒了人，不是已经能接着装 interchangeable——本页从 378 item 3 侧钉 not already can continue 单句。378 refetch vs restored bundled unbundling 在本页 item 3 完成。

2. **看见拒了人 / 看见丢掉排队 / 这份拒人 is not already 已经停 interchangeable / 375 loadchunk interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 796 refetch-notcontinue interchangeable / 378 refetch item 2 refetch_chunks interchangeable / 795 refetch-notcomplete interchangeable，也不是已经 REJECT_SENDER 就已经拒了人 interchangeable / 400 offerfmt / 723 offerfmt-notsenders interchangeable，也不是已经 Apply 请求 sender 就已经拒了人 interchangeable / 397 applychunk / 741 applychunk-notsenders interchangeable。**  
   官方把丢掉排队和已经停分开——378 bundled 第三件事常与 375 / 400 / 397 混成「看见拒了人就已经能接着装或已经停 interchangeable」，本页钉 not already halted 单句。

3. **看见拒了人 / 看见已装的还在 / 这份拒人 is not already 已经齐 interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 796 refetch-notcontinue interchangeable / 794 refetch-notbanned interchangeable。**  
   官方把已装的还在和已经齐分开。看见已装的还在，不是已经齐 interchangeable。378 refetch vs restored bundled unbundling 在本页 item 3 完成。

怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居是规范里的做法，本页不抄。

## 官方为什么这样拆

- **reject_senders not already can continue ≠ 375 interchangeable：** 官方把拒发送者和已经能接着装分开。
- **看见丢掉排队 not already halted ≠ 已经停 interchangeable：** 官方把丢掉排队和已经停分开。
- **看见已装的还在 not already complete ≠ 已经齐 interchangeable：** 官方把已装的还在和已经齐分开；378 refetch vs restored bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| reject_senders 不论 Result 都拒这些人 | 不是已经能接着装（375） | 不是引擎不自己做（794/378 item 1） |
| 看见拒了人 | 不是已经停 | 不是 REJECT_SENDER（400/723） |
| 看见已装的还在 | 不是已经齐 | 不是 Apply 请求 sender（397/741） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 reject_senders not already can continue / not already halted / not already complete 正式三事（378 余量），必须分开是不是已经能接着装 interchangeable / 375、是不是已经停、是不是已经齐。可以跳过「看见拒了人就已经能接着装」。不要另写怎样写 ApplySnapshotChunk。378 refetch vs restored bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居。
- ApplySnapshotChunk 再拉 bundled。那是不变量 378。
- 引擎不自己做。那是不变量 378 item 1 余量 / 794。
- REJECT_SENDER 就已经拒了人。那是不变量 400 / 723。
- Apply 请求 sender 就已经拒了人。那是不变量 397 / 741。
