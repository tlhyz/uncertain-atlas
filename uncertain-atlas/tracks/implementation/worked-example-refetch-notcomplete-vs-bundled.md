# 例：看见列了块号 / 看见再装 / 看见按顺序 is not already already complete interchangeable / already settled interchangeable / already identical interchangeable

**层次**：实现 / refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量）/ not 882 refetch-notcomplete interchangeable / not 378 refetch bundled interchangeable」，不是 refetch bundled（378），也不是应用可以再拉块或封邻居、引擎不自己做不是已经封了（881 item 1 余量）或 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装（378 item 3 余量）。不要另写怎样写 ApplySnapshotChunk。

## 官方三件事

规范把 Methods 里 refetch_chunks 不论 result 都再拉再装、按顺序 和「已经是列了块号就已经齐 interchangeable / 已经是再装就已经交差 interchangeable / 已经是按顺序就已经是同一份 interchangeable / 已经是 refetch bundled interchangeable」分开写成三件独立的实现事，不是「看见列了块号就已经齐 interchangeable / 就已经交差 interchangeable / 就已经是同一份 interchangeable」一件事：

1. **看见列了块号 / 看见 refetch_chunks 不论 result 都再拉再装、按顺序 / 看见列了块号字段 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 378 refetch bundled interchangeable / 332 snapshotverify interchangeable / refetch-sold-as-restored interchangeable，也不是已经 refetch bundled（378） interchangeable / 882 refetch-notcomplete interchangeable / 378 refetch item 2 interchangeable，也不是已经 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事 bundled（378 item 2 余量） interchangeable / 378 refetch item 2 interchangeable，也不是已经能再拉就已经封了（881） interchangeable / 321 Offer restored interchangeable / 拒了人就能接着装（378 item 3） interchangeable，也不是已经封禁邻居就已经没有快照 DoS（332） interchangeable。**  
   官方写：`refetch_chunks` 不论 `result` 是什么，都会再拉并列出来的那些块，再按顺序装回去。只拉列出来的那些。看见列了块号，不是已经齐。看见列了块号，不是已经 complete interchangeable——378 钉 bundled 三事，本页从 item 2 侧钉 not already complete 单句。看见 refetch_chunks 不论 result 都再拉再装、按顺序，不是已经 refetch bundled（378） interchangeable——378 钉 bundled，本页钉 item 2 第一件事。看见列了块号字段，不是已经封禁邻居就已经没有快照 DoS（332） interchangeable——332 另钉。378 refetch-vs-restored bundled unbundling 在本页 item 2 续。

2. **看见再装 / 看见再按顺序装回去 / 看见再装块 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 378 refetch bundled interchangeable / 881 refetch-notbanned interchangeable，也不是已经 refetch bundled（378） interchangeable / 882 refetch-notcomplete interchangeable / 378 refetch item 1 能再拉 interchangeable / 378 refetch item 3 拒了人 interchangeable，也不是已经 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事 bundled（378 item 2 余量） interchangeable / 378 refetch item 2 interchangeable，也不是已经齐（本页第一件事） interchangeable。**  
   官方写：看见再装，不是已经交差。看见再按顺序装回去，不是已经 settled interchangeable——本页钉 not already settled 单句。看见再装块，不是已经齐（本页第一件事） interchangeable——三件事分开钉。378 refetch-vs-restored bundled unbundling 在本页 item 2 续。

3. **看见按顺序 / 看见按顺序装回去 / 看见顺序列 is not already 已经是同一份 interchangeable / 已经 identical interchangeable / 已经是同一份交差 interchangeable / 378 refetch bundled interchangeable / 368 Snapshot identical interchangeable，也不是已经 refetch bundled（378） interchangeable / 882 refetch-notcomplete interchangeable / 378 refetch item 1 / 378 refetch item 3，也不是已经 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事 bundled（378 item 2 余量） interchangeable / 378 refetch item 2 interchangeable，也不是已经齐（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见按顺序，不是已经是同一份。看见按顺序装回去，不是已经 identical interchangeable——本页钉 not already identical 单句。看见顺序列，不是已经交差（本页第二件事） interchangeable——三件事分开钉。378 refetch-vs-restored bundled unbundling 在本页 item 2 续。

怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居是规范里的做法，本页不抄。refetch bundled（378）、应用可以再拉块或封邻居、引擎不自己做不是已经封了（378 item 1 余量 / 881）、reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装（378 item 3 余量）、Offer 收下就已经装完（321）、封禁邻居就已经没有快照 DoS（332）、LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375）是另外那套，本页不抄。

## 官方为什么这样拆

- **列了块号 not already complete ≠ 378 / 332 interchangeable：** 官方把再拉并列块和已经齐分开。
- **再装 not already settled ≠ 已经交差 interchangeable：** 官方把再装和已经交差分开。
- **按顺序 not already identical ≠ 已经是同一份 interchangeable：** 官方把按顺序和已经是同一份分开；378 refetch-vs-restored bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 列了块号 | 不是 already complete | 不是封禁邻居就已经没有快照 DoS alone（332） |
| 再装 | 不是 already settled | 不是能再拉 already banned alone（881） |
| 按顺序 | 不是 already identical | 不是全字段对上就已经装完 alone（368） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐 not already complete / not already settled / not already identical 正式三事（378 余量），必须分开列了块号 是不是 already complete interchangeable / 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable、再装 是不是 already settled interchangeable、按顺序 是不是 already identical interchangeable。可以跳过「看见列了块号就已经齐 interchangeable / 就已经交差 interchangeable / 就已经是同一份 interchangeable」。不要另写怎样写 ApplySnapshotChunk。378 refetch-vs-restored bundled unbundling 在本页 item 2 续（881 + 882）。

## 本页不抄

- 怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居。
- refetch bundled。那是不变量 378。
- 应用可以再拉块或封邻居、引擎不自己做不是已经封了。那是不变量 378 item 1 余量 / 881。
- reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装。那是不变量 378 item 3 余量。
- Offer 收下就已经装完。那是不变量 321。
- 封禁邻居就已经没有快照 DoS。那是不变量 332。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
