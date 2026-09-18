# 例：看见Fields 栏不是已经是 CommitInfo Notes 票序不是已经是 CommitInfo Notes 那套票序话；看见Fields column is not already CommitInfo Notes order不是已经是 444 cinotes bundled；看见Fields 栏不是已经是 CommitInfo Notes 票序不是已经按到场定奖惩

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CiFields Fields column not already Notes order / not already 444-bundled / not already 365-rewards 正式三事（445 余量）/ not 1361 cifields-notnts interchangeable / not 445 cifields-vs-notes bundled interchangeable」，不是 cifields vs notes bundled（445），也不是已经 CommitInfo Notes 票序正式三事（444），也不是已经 VoteInfo 能按到场定奖惩就已经罚没（365）。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。

## 官方三件事

1. **看见Fields 栏不是已经是 CommitInfo Notes 票序 / 看见Fields 栏不是已经是 CommitInfo Notes 票序 这份对象 is not already 已经是 CommitInfo Notes 那套票序话 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1361 cifields-notnts interchangeable / 1359 cifields-notrnd interchangeable，也不是已经 CiFields Fields column not already Notes order / not already 444-bundled / not already 365-rewards 正式三事 bundled（445 item 3 余量） interchangeable / 445 cifields item 3 interchangeable。**  
   官方把Fields 栏不是已经是 CommitInfo Notes 票序和已经是 CommitInfo Notes 那套票序话写成两件。看见Fields 栏不是已经是 CommitInfo Notes 票序，不是已经是 CommitInfo Notes 那套票序话。

2. **看见Fields column is not already CommitInfo Notes order / 看见Fields 栏不是已经是 CommitInfo Notes 票序 / 这份对象 is not already 已经是 444 cinotes bundled interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1361 cifields-notnts interchangeable / 1360 cifields-notlst interchangeable，也不是已经 CommitInfo Notes 票序正式三事 interchangeable / 444 CommitInfo Notes 票序正式三事 interchangeable。**  
   官方把Fields column is not already CommitInfo Notes order和已经是 444 cinotes bundled写成两件。看见Fields column is not already CommitInfo Notes order，不是已经是 444 cinotes bundled。

3. **看见Fields 栏不是已经是 CommitInfo Notes 票序 / 看见Fields column is not already CommitInfo Notes order / 这份对象 is not already 已经按到场定奖惩 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1361 cifields-notnts interchangeable / 1359 cifields-notrnd interchangeable，也不是已经 VoteInfo 能按到场定奖惩就已经罚没 interchangeable / 365 VoteInfo 能按到场定奖惩就已经罚没 interchangeable。**  
   官方把Fields 栏不是已经是 CommitInfo Notes 票序和已经按到场定奖惩写成两件。看见Fields 栏不是已经是 CommitInfo Notes 票序，不是已经按到场定奖惩。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。

## 官方为什么这样拆

- **Fields 栏 不是已经是 Notes 票序 interchangeable：官方把 Fields 表和 Notes 分开写。**
- **看见 round+votes 都在 不是已经可以用 444 代替本页 Fields。**
- **看见 Fields 不是已经按到场定奖惩：365 是 Usage 路径，不是本栏。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 CommitInfo Notes 那套票序话 | 不是已经是 CommitInfo Notes 那套票序话 | 不是已经CommitInfo Notes 票序正式三事（444） |
| 已经是 444 cinotes bundled | 不是已经是 444 cinotes bundled | 不是已经VoteInfo 能按到场定奖惩就已经罚没（365） |
| 已经按到场定奖惩 | 不是已经按到场定奖惩 | 不是已经1359 cifields-notrnd |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CiFields Fields column not already Notes order / not already 444-bundled / not already 365-rewards 正式三事（445 余量），必须分开是不是已经是 CommitInfo Notes 那套票序话、是不是已经是 444 cinotes bundled、是不是已经按到场定奖惩。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮」。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。445 CommitInfo Fields round-and-votes bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样写 CommitInfo Fields 栏、怎样填 round、怎样读 votes。
- 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。
