# 例：看见CommitInfo.votes 是上一集合投票信息不是已经进了块不是已经进了块；看见CommitInfo.votes is last-set voting info is not already in the block不是已经交差；看见CommitInfo.votes 是上一集合投票信息不是已经进了块不是已经是 Notes 票序

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CiFields votes is last-set voting-info not already in-block / not already settled / not already 444-notes-order 正式三事（445 余量）/ not 1360 cifields-notlst interchangeable / not 445 cifields-vs-notes bundled interchangeable」，不是 cifields vs notes bundled（445），也不是已经 CommitInfo Notes 按投票权降序（444），也不是已经 VoteInfo 能按到场定奖惩（365）。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。

## 官方三件事

1. **看见CommitInfo.votes 是上一集合投票信息不是已经进了块 / 看见CommitInfo.votes 是上一集合投票信息不是已经进了块 这份对象 is not already 已经进了块 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1360 cifields-notlst interchangeable / 1359 cifields-notrnd interchangeable，也不是已经 CiFields votes is last-set voting-info not already in-block / not already settled / not already 444-notes-order 正式三事 bundled（445 item 2 余量） interchangeable / 445 cifields item 2 interchangeable。**  
   官方把CommitInfo.votes 是上一集合投票信息不是已经进了块和已经进了块写成两件。看见CommitInfo.votes 是上一集合投票信息不是已经进了块，不是已经进了块。

2. **看见CommitInfo.votes is last-set voting info is not already in the block / 看见CommitInfo.votes 是上一集合投票信息不是已经进了块 / 这份对象 is not already 已经交差 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1360 cifields-notlst interchangeable / 1361 cifields-notnts interchangeable，也不是已经 CommitInfo Notes 按投票权降序 interchangeable / 444 CommitInfo Notes 按投票权降序 interchangeable。**  
   官方把CommitInfo.votes is last-set voting info is not already in the block和已经交差写成两件。看见CommitInfo.votes is last-set voting info is not already in the block，不是已经交差。

3. **看见CommitInfo.votes 是上一集合投票信息不是已经进了块 / 看见CommitInfo.votes is last-set voting info is not already in the block / 这份对象 is not already 已经是 Notes 票序 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1360 cifields-notlst interchangeable / 1359 cifields-notrnd interchangeable，也不是已经 VoteInfo 能按到场定奖惩 interchangeable / 365 VoteInfo 能按到场定奖惩 interchangeable。**  
   官方把CommitInfo.votes 是上一集合投票信息不是已经进了块和已经是 Notes 票序写成两件。看见CommitInfo.votes 是上一集合投票信息不是已经进了块，不是已经是 Notes 票序。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。

## 官方为什么这样拆

- **Fields 里 votes 列表含义 不是已经进了块 interchangeable：官方把列表内容和已经写进块分开。**
- **看见有投票信息 不是已经 Notes 引擎/store 排序那种已经进了块。**
- **看见 Process/Finalize 有 CommitInfo.votes 不是已经 typically extracted 就已经交差。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经进了块 | 不是已经进了块 | 不是已经CommitInfo Notes 按投票权降序（444） |
| 已经交差 | 不是已经交差 | 不是已经VoteInfo 能按到场定奖惩（365） |
| 已经是 Notes 票序 | 不是已经是 Notes 票序 | 不是已经1359 cifields-notrnd |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CiFields votes is last-set voting-info not already in-block / not already settled / not already 444-notes-order 正式三事（445 余量），必须分开是不是已经进了块、是不是已经交差、是不是已经是 Notes 票序。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮」。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。445 CommitInfo Fields round-and-votes bundled unbundling 在本页 item 2 续；续 [`worked-example-cifields-notnts-vs-bundled.md`](worked-example-cifields-notnts-vs-bundled.md)（不变量 1361 item 3）。

## 本页不抄

- 怎样写 CommitInfo Fields 栏、怎样填 round、怎样读 votes。
- 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。
