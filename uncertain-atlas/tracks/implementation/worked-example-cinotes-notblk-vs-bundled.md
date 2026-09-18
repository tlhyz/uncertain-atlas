# 例：看见CommitInfo.votes 按投票权降序排不是已经进了块不是已经进了块；看见CommitInfo.votes ordered by voting power is not already in the block不是已经交差；看见CommitInfo.votes 按投票权降序排不是已经进了块不是已经写进 last_commit

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CiNotes votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（444 余量）/ not 1353 cinotes-notblk interchangeable / not 444 cinotes-vs-order bundled interchangeable」，不是 cinotes vs order bundled（444），也不是已经 VoteInfo 能按到场定奖惩就已经罚没（365），也不是已经 CommitInfo.round 是提交轮（392）。不要另写 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。

## 官方三件事

1. **看见CommitInfo.votes 按投票权降序排不是已经进了块 / 看见CommitInfo.votes 按投票权降序排不是已经进了块 这份对象 is not already 已经进了块 interchangeable，也不是已经 cinotes vs order bundled（444） interchangeable / 1353 cinotes-notblk interchangeable / 1354 cinotes-notapp interchangeable，也不是已经 CiNotes votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事 bundled（444 item 1 余量） interchangeable / 444 cinotes item 1 interchangeable。**  
   官方把CommitInfo.votes 按投票权降序排不是已经进了块和已经进了块写成两件。看见CommitInfo.votes 按投票权降序排不是已经进了块，不是已经进了块。

2. **看见CommitInfo.votes ordered by voting power is not already in the block / 看见CommitInfo.votes 按投票权降序排不是已经进了块 / 这份对象 is not already 已经交差 interchangeable，也不是已经 cinotes vs order bundled（444） interchangeable / 1353 cinotes-notblk interchangeable / 1355 cinotes-notstore interchangeable，也不是已经 VoteInfo 能按到场定奖惩就已经罚没 interchangeable / 365 VoteInfo 能按到场定奖惩就已经罚没 interchangeable。**  
   官方把CommitInfo.votes ordered by voting power is not already in the block和已经交差写成两件。看见CommitInfo.votes ordered by voting power is not already in the block，不是已经交差。

3. **看见CommitInfo.votes 按投票权降序排不是已经进了块 / 看见CommitInfo.votes ordered by voting power is not already in the block / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 cinotes vs order bundled（444） interchangeable / 1353 cinotes-notblk interchangeable / 1354 cinotes-notapp interchangeable，也不是已经 CommitInfo.round 是提交轮 interchangeable / 392 CommitInfo.round 是提交轮 interchangeable。**  
   官方把CommitInfo.votes 按投票权降序排不是已经进了块和已经写进 last_commit写成两件。看见CommitInfo.votes 按投票权降序排不是已经进了块，不是已经写进 last_commit。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。

## 官方为什么这样拆

- **按投票权降序排 不是已经进了块 interchangeable：官方把顺序和已经进规范分开。**
- **看见顺序在 不是已经交差：Notes 写顺序，不是 last_commit。**
- **看见 Process/Finalize 有 CommitInfo 不是已经写进 last_commit。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经进了块 | 不是已经进了块 | 不是已经VoteInfo 能按到场定奖惩就已经罚没（365） |
| 已经交差 | 不是已经交差 | 不是已经CommitInfo.round 是提交轮（392） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经1354 cinotes-notapp |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CiNotes votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（444 余量），必须分开是不是已经进了块、是不是已经交差、是不是已经写进 last_commit。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好」。不要另写 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。444 CommitInfo Notes vote-power order bundled unbundling 在本页 item 1 启动；续 [`worked-example-cinotes-notapp-vs-bundled.md`](worked-example-cinotes-notapp-vs-bundled.md)（不变量 1354 item 2）。

## 本页不抄

- 怎样写 CommitInfo Notes 票序正式三事、怎样从 store 再装、怎样排 votes。
- 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。
