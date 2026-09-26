# 例：看见拒了人 / 看见丢掉排队 / 看见已装的还在 is not already already proceed interchangeable / already stopped interchangeable / already complete interchangeable

**层次**：实现 / reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量）/ not 883 refetch-notproceed interchangeable / not 378 refetch bundled interchangeable」，不是 refetch bundled（378），也不是应用可以再拉块或封邻居、引擎不自己做不是已经封了（881 item 1 余量）或 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐（378 item 2 余量 / 882）。不要另写怎样写 ApplySnapshotChunk。

## 官方三件事

规范把 Methods 里 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名 和「已经是拒了人就能接着装 interchangeable / 已经是丢掉排队就已经停 interchangeable / 已经是已装的还在就已经齐 interchangeable / 已经是 refetch bundled interchangeable」分开写成三件独立的实现事，不是「看见拒了人就能接着装 interchangeable / 就已经停 interchangeable / 就已经齐 interchangeable」一件事：

1. **看见拒了人 / 看见 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名 / 看见拒了发送者 is not already 已经能接着装 interchangeable / 已经 proceed interchangeable / 已经能接着装交差 interchangeable / 378 refetch bundled interchangeable / 375 loadchunk interchangeable / refetch-sold-as-restored interchangeable，也不是已经 refetch bundled（378） interchangeable / 883 refetch-notproceed interchangeable / 378 refetch item 3 interchangeable，也不是已经 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事 bundled（378 item 3 余量） interchangeable / 378 refetch item 3 interchangeable，也不是已经能再拉就已经封了（881） interchangeable / 列了块号就已经齐（882） interchangeable / 321 Offer restored interchangeable，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable。**  
   官方写：`reject_senders` 不论 `Result` 是什么，都拒这些 P2P 发送者。已经装上的块不会重拉，除非明确点名。这些人排队的块会丢掉，新块或其他快照也会拒。看见拒了人，不是已经能接着装。看见拒了人，不是已经 proceed interchangeable——378 钉 bundled 三事，本页从 item 3 侧钉 not already proceed 单句。看见 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名，不是已经 refetch bundled（378） interchangeable——378 钉 bundled，本页钉 item 3 第一件事。看见拒了发送者，不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable——375 另钉。378 refetch-vs-restored bundled unbundling 在本页 item 3 完成。

2. **看见丢掉排队 / 看见这些人排队的块会丢掉 / 看见丢掉排队块 is not already 已经停 interchangeable / 已经 stopped interchangeable / 已经停交差 interchangeable / 378 refetch bundled interchangeable / 332 snapshotverify interchangeable，也不是已经 refetch bundled（378） interchangeable / 883 refetch-notproceed interchangeable / 378 refetch item 1 能再拉 interchangeable / 378 refetch item 2 列了块号 interchangeable，也不是已经 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事 bundled（378 item 3 余量） interchangeable / 378 refetch item 3 interchangeable，也不是已经能接着装（本页第一件事） interchangeable。**  
   官方写：看见丢掉排队，不是已经停。看见这些人排队的块会丢掉，不是已经 stopped interchangeable——本页钉 not already stopped 单句。看见丢掉排队块，不是已经能接着装（本页第一件事） interchangeable——三件事分开钉。378 refetch-vs-restored bundled unbundling 在本页 item 3 完成。

3. **看见已装的还在 / 看见已经装上的块不会重拉除非点名 / 看见已装的还在字段 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 378 refetch bundled interchangeable / 882 refetch-notcomplete interchangeable，也不是已经 refetch bundled（378） interchangeable / 883 refetch-notproceed interchangeable / 378 refetch item 1 / 378 refetch item 2，也不是已经 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事 bundled（378 item 3 余量） interchangeable / 378 refetch item 3 interchangeable，也不是已经能接着装（本页第一件事） interchangeable / 已经停（本页第二件事） interchangeable。**  
   官方写：看见已装的还在，不是已经齐。看见已经装上的块不会重拉除非点名，不是已经 complete interchangeable——本页钉 not already complete 单句。看见已装的还在字段，不是已经停（本页第二件事） interchangeable——三件事分开钉。378 refetch-vs-restored bundled unbundling 在本页 item 3 完成。

怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居是规范里的做法，本页不抄。refetch bundled（378）、应用可以再拉块或封邻居、引擎不自己做不是已经封了（378 item 1 余量 / 881）、refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐（378 item 2 余量 / 882）、Offer 收下就已经装完（321）、封禁邻居就已经没有快照 DoS（332）、LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375）是另外那套，本页不抄。

## 官方为什么这样拆

- **拒了人 not already proceed ≠ 378 / 375 interchangeable：** 官方把拒发送者和已经能接着装分开。
- **丢掉排队 not already stopped ≠ 已经停 interchangeable：** 官方把丢掉排队和已经停分开。
- **已装的还在 not already complete ≠ 已经齐 interchangeable：** 官方把已装的还在和已经齐分开；378 refetch-vs-restored bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拒了人 | 不是 already proceed | 不是 LoadSnapshotChunk 就已经齐 alone（375） |
| 丢掉排队 | 不是 already stopped | 不是封禁邻居就已经没有快照 DoS alone（332） |
| 已装的还在 | 不是 already complete | 不是列了块号 already complete alone（882） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装 not already proceed / not already stopped / not already complete 正式三事（378 余量），必须分开拒了人 是不是 already proceed interchangeable / 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable、丢掉排队 是不是 already stopped interchangeable、已装的还在 是不是 already complete interchangeable。可以跳过「看见拒了人就能接着装 interchangeable / 就已经停 interchangeable / 就已经齐 interchangeable」。不要另写怎样写 ApplySnapshotChunk。378 refetch-vs-restored bundled unbundling 在本页 item 3 完成（881 + 882 + 883）。

## 本页不抄

- 怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居。
- refetch bundled。那是不变量 378。
- 应用可以再拉块或封邻居、引擎不自己做不是已经封了。那是不变量 378 item 1 余量 / 881。
- refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐。那是不变量 378 item 2 余量 / 882。
- Offer 收下就已经装完。那是不变量 321。
- 封禁邻居就已经没有快照 DoS。那是不变量 332。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
