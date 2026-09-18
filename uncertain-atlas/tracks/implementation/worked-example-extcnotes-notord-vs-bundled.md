# 例：看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块不是已经进了块；看见ExtendedCommitInfo.votes ordered by voting power is not already in the block不是已经交差；看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块不是已经写进 last_commit

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedCommitInfo Notes 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（441 余量）/ not 1356 extcnotes-notord interchangeable / not 441 extcinotes-vs-order bundled interchangeable」，不是 extcinotes vs order bundled（441），也不是已经 VoteInfo 按投票权降序就已经进了块（365），也不是已经 CommitInfo Notes 票序（444）。不要另写 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。

## 官方三件事

1. **看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块 / 看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块 这份对象 is not already 已经进了块 interchangeable，也不是已经 extcinotes vs order bundled（441） interchangeable / 1356 extcnotes-notord interchangeable / 1357 extcnotes-noteng interchangeable，也不是已经 ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事 bundled（441 item 1 余量） interchangeable / 441 extcnotes item 1 interchangeable。**  
   官方把ExtendedCommitInfo.votes 按投票权降序排不是已经进了块和已经进了块写成两件。看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块，不是已经进了块。

2. **看见ExtendedCommitInfo.votes ordered by voting power is not already in the block / 看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块 / 这份对象 is not already 已经交差 interchangeable，也不是已经 extcinotes vs order bundled（441） interchangeable / 1356 extcnotes-notord interchangeable / 1358 extcnotes-notload interchangeable，也不是已经 VoteInfo 按投票权降序就已经进了块 interchangeable / 365 VoteInfo 按投票权降序就已经进了块 interchangeable。**  
   官方把ExtendedCommitInfo.votes ordered by voting power is not already in the block和已经交差写成两件。看见ExtendedCommitInfo.votes ordered by voting power is not already in the block，不是已经交差。

3. **看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块 / 看见ExtendedCommitInfo.votes ordered by voting power is not already in the block / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 extcinotes vs order bundled（441） interchangeable / 1356 extcnotes-notord interchangeable / 1357 extcnotes-noteng interchangeable，也不是已经 CommitInfo Notes 票序 interchangeable / 444 CommitInfo Notes 票序 interchangeable。**  
   官方把ExtendedCommitInfo.votes 按投票权降序排不是已经进了块和已经写进 last_commit写成两件。看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块，不是已经写进 last_commit。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。

## 官方为什么这样拆

- **ExtendedVoteInfo 按投票权降序排 不是已经进了块 interchangeable：官方把 Prepare 路径的顺序和已经进规范分开。**
- **看见顺序在 不是已经交差：Notes 写顺序，不是 last_commit。**
- **看见 Prepare 有 ExtendedCommitInfo 不是已经写进 last_commit。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经进了块 | 不是已经进了块 | 不是已经VoteInfo 按投票权降序就已经进了块（365） |
| 已经交差 | 不是已经交差 | 不是已经CommitInfo Notes 票序（444） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经1357 extcnotes-noteng |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（441 余量），必须分开是不是已经进了块、是不是已经交差、是不是已经写进 last_commit。可以跳过「看见 Prepare 里有 ExtendedCommitInfo 就已经按投票权排好」。不要另写 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。441 ExtendedCommitInfo Notes vote-power order bundled unbundling 在本页 item 1 启动；续 [`worked-example-extcnotes-noteng-vs-bundled.md`](worked-example-extcnotes-noteng-vs-bundled.md)（不变量 1357 item 2）。

## 本页不抄

- 怎样写 ExtendedCommitInfo Notes 票序正式三事、怎样从 store 再装、怎样排 votes。
- 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。
