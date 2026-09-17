# 例：看见应用可以再拉块或封邻居、引擎不自己做 is not already banned interchangeable / not already complete interchangeable / not already settled interchangeable

**层次**：实现 / 引擎不自己做 not already banned / not already complete / not already settled 正式三事（378 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎不自己做 not already banned / not already complete / not already settled 正式三事（378 余量）/ not 794 refetch-notbanned interchangeable / not 378 refetch-vs-restored bundled interchangeable」，不是 ApplySnapshotChunk 再拉 bundled（378），也不是 Offer 收下就已经装完（321），也不是 Usage can choose refetch/ban 就已经是 refetch_chunks（502/656），也不是 RETRY 就已经 refetch 不论 result（398/719）。不要另写怎样写 ApplySnapshotChunk。

## 官方三件事

1. **看见应用可以再拉块或封邻居、引擎不自己做 / 看见能再拉 / 这份指令 is not already 已经封了 interchangeable / 321 restored interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 794 refetch-notbanned interchangeable / 795 refetch-notcomplete interchangeable / 378 refetch item 2 refetch_chunks interchangeable，也不是已经引擎不自己做 not already banned / not already complete / not already settled 正式三事 bundled（378 item 1 余量） interchangeable / 378 refetch item 1 interchangeable。**  
   官方写：应用可以再拉块，也可以封 P2P 邻居。CometBFT 不会自己做这些，除非应用下了指令。看见能再拉，不是已经封了 interchangeable——本页从 378 item 1 侧钉 not already banned 单句。378 refetch vs restored bundled unbundling 在本页 item 1 启动。

2. **看见能再拉 / 看见能封 / 这份指令 is not already 已经齐 interchangeable / 321 restored interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 794 refetch-notbanned interchangeable / 378 refetch item 3 reject_senders interchangeable / 796 refetch-notcontinue interchangeable，也不是已经 Usage can choose refetch/ban 就已经是 refetch_chunks interchangeable / 502 applysnapusage / 656 applysnapusage-notchoose interchangeable，也不是已经 RETRY 就已经 refetch 不论 result interchangeable / 398 applyretry / 719 applyretry-notrefetch interchangeable。**  
   官方把能封和已经齐分开——378 bundled 第一件事常与 321 / 502 / 398 混成「看见能再拉就已经封了或已经齐 interchangeable」，本页钉 not already complete 单句。

3. **看见能再拉 / 看见有指令 / 这份指令 is not already 已经交差 interchangeable，也不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable / 794 refetch-notbanned interchangeable / 795 refetch-notcomplete interchangeable。**  
   官方把有指令和已经交差分开。看见有指令，不是已经交差 interchangeable。378 refetch vs restored bundled unbundling 在本页 item 1 启动。

怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居是规范里的做法，本页不抄。

## 官方为什么这样拆

- **引擎不自己做 not already banned ≠ 321 interchangeable：** 官方把应用下指令和引擎已经封了分开。
- **看见能封 not already complete ≠ 已经齐 interchangeable：** 官方把能封和已经齐分开。
- **看见有指令 not already settled ≠ 已经交差 interchangeable：** 官方把有指令和已经交差分开；378 refetch vs restored bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 应用可以再拉块或封邻居、引擎不自己做 | 不是已经封了（321） | 不是 refetch_chunks（795/378 item 2） |
| 看见能再拉 | 不是已经齐 | 不是 Usage can choose（502/656） |
| 看见有指令 | 不是已经交差 | 不是 RETRY 就已经再拉（398/719） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不自己做 not already banned / not already complete / not already settled 正式三事（378 余量），必须分开是不是已经封了 interchangeable / 321、是不是已经齐、是不是已经交差。可以跳过「看见能再拉就已经封了」。不要另写怎样写 ApplySnapshotChunk。378 refetch vs restored bundled unbundling 在本页 item 1 启动；续 [`worked-example-refetch-notcomplete-vs-bundled.md`](worked-example-refetch-notcomplete-vs-bundled.md)（不变量 795 item 2）。

## 本页不抄

- 怎样写 ApplySnapshotChunk、怎样再拉、怎样封邻居。
- ApplySnapshotChunk 再拉 bundled。那是不变量 378。
- refetch_chunks 不论 result。那是不变量 378 item 2 余量 / 795。
- Usage can choose refetch/ban。那是不变量 502 / 656。
- RETRY 就已经 refetch 不论 result。那是不变量 398 / 719。
