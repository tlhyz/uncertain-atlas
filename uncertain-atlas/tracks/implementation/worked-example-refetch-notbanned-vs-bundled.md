# 例：看见能再拉 / 看见能封 / 看见有指令 is not already already banned interchangeable / already complete interchangeable / already settled interchangeable

**层次**：实现 / 应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量）/ not 881 refetch-notbanned interchangeable / not 378 refetch bundled interchangeable」，不是 refetch bundled（378），也不是 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐（378 item 2 余量）或 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装（378 item 3 余量）。不要另写怎样写 ApplySnapshotChunk。

## 官方三件事

规范把 Methods 里应用可以再拉块或封邻居、引擎不自己做 和「已经是能再拉就已经封了 interchangeable / 已经是能封就已经齐 interchangeable / 已经是有指令就已经交差 interchangeable / 已经是 refetch bundled interchangeable」分开写成三件独立的实现事，不是「看见能再拉就已经封了 interchangeable / 就已经齐 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见能再拉 / 看见应用可以再拉块或封邻居、引擎不自己做 / 看见能再拉块 is not already 已经封了 interchangeable / 已经 banned interchangeable / 已经封了交差 interchangeable / 378 refetch bundled interchangeable / 321 Offer restored interchangeable / refetch-sold-as-restored interchangeable，也不是已经 refetch bundled（378） interchangeable / 881 refetch-notbanned interchangeable / 378 refetch item 1 interchangeable，也不是已经应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事 bundled（378 item 1 余量） interchangeable / 378 refetch item 1 interchangeable，也不是已经列了块号就已经齐（378 item 2） interchangeable / 拒了人就能接着装（378 item 3） interchangeable / 332 snapshotverify interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable。**  
   官方写：应用可以再拉块，也可以封 P2P 邻居。CometBFT 不会自己做这些，除非应用下了指令。看见能再拉，不是已经封了。看见能再拉，不是已经 banned interchangeable——378 钉 bundled 三事，本页从 item 1 侧钉 not already banned 单句。看见应用可以再拉块或封邻居、引擎不自己做，不是已经 refetch bundled（378） interchangeable——378 钉 bundled，本页钉 item 1 第一件事。看见能再拉块，不是已经 Offer 收下就已经装完（321） interchangeable——321 另钉。378 refetch-vs-restored bundled unbundling 在本页 item 1 启动。

2. **看见能封 / 看见能封邻居 / 看见能封 P2P is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 378 refetch bundled interchangeable / 332 snapshotverify interchangeable，也不是已经 refetch bundled（378） interchangeable / 881 refetch-notbanned interchangeable / 378 refetch item 2 列了块号 interchangeable / 378 refetch item 3 拒了人 interchangeable，也不是已经应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事 bundled（378 item 1 余量） interchangeable / 378 refetch item 1 interchangeable，也不是已经封了（本页第一件事） interchangeable。**  
   官方写：看见能封，不是已经齐。看见能封邻居，不是已经 complete interchangeable——本页钉 not already complete 单句。看见能封 P2P，不是已经封了（本页第一件事） interchangeable——三件事分开钉。378 refetch-vs-restored bundled unbundling 在本页 item 1 启动。

3. **看见有指令 / 看见应用下了指令 / 看见有下指令 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 378 refetch bundled interchangeable / 375 loadchunk interchangeable，也不是已经 refetch bundled（378） interchangeable / 881 refetch-notbanned interchangeable / 378 refetch item 2 / 378 refetch item 3，也不是已经应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事 bundled（378 item 1 余量） interchangeable / 378 refetch item 1 interchangeable，也不是已经封了（本页第一件事） interchangeable / 已经齐（本页第二件事） interchangeable。**  
   官方写：看见有指令，不是已经交差。看见应用下了指令，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有下指令，不是已经齐（本页第二件事） interchangeable——三件事分开钉。378 refetch-vs-restored bundled unbundling 在本页 item 1 启动。

怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居是规范里的做法，本页不抄。refetch bundled（378）、refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐（378 item 2 余量）、reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装（378 item 3 余量）、Offer 收下就已经装完（321）、封禁邻居就已经没有快照 DoS（332）、LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375）是另外那套，本页不抄。

## 官方为什么这样拆

- **能再拉 not already banned ≠ 378 / 321 interchangeable：** 官方把应用下指令和引擎已经封了分开。
- **能封 not already complete ≠ 已经齐 interchangeable：** 官方把能封和已经齐分开。
- **有指令 not already settled ≠ 已经交差 interchangeable：** 官方把有指令和已经交差分开；378 refetch-vs-restored bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能再拉 | 不是 already banned | 不是 Offer 收下就已经装完 alone（321） |
| 能封 | 不是 already complete | 不是 refetch_chunks already complete alone（378 item 2） |
| 有指令 | 不是 already settled | 不是 LoadSnapshotChunk 就已经齐 alone（375） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用可以再拉块或封邻居、引擎不自己做不是已经封了 not already banned / not already complete / not already settled 正式三事（378 余量），必须分开能再拉 是不是 already banned interchangeable / 378 refetch bundled interchangeable / refetch-sold-as-restored interchangeable、能封 是不是 already complete interchangeable、有指令 是不是 already settled interchangeable。可以跳过「看见能再拉就已经封了 interchangeable / 就已经齐 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 ApplySnapshotChunk。378 refetch-vs-restored bundled unbundling 在本页 item 1 启动（881）。

## 本页不抄

- 怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居。
- refetch bundled。那是不变量 378。
- refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐。那是不变量 378 item 2 余量。
- reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装。那是不变量 378 item 3 余量。
- Offer 收下就已经装完。那是不变量 321。
- 封禁邻居就已经没有快照 DoS。那是不变量 332。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
