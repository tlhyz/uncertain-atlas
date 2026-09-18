# 例：看见引擎保证并落盘顺序不是已经由应用排过不是已经由应用排过；看见engine guarantees and persists order is not already sorted by the app不是已经是收到票时的顺序；看见引擎保证并落盘顺序不是已经由应用排过不是已经由 Process 回包决定

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CiNotes engine guarantees and persists order not already app-sorted / not already recv-order / not already Process-decided 正式三事（444 余量）/ not 1354 cinotes-notapp interchangeable / not 444 cinotes-vs-order bundled interchangeable」，不是 cinotes vs order bundled（444），也不是已经 VoteInfo 按投票权降序就已经进了块（365），也不是已经 CommitInfo Fields 栏（445）。不要另写 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。

## 官方三件事

1. **看见引擎保证并落盘顺序不是已经由应用排过 / 看见引擎保证并落盘顺序不是已经由应用排过 这份对象 is not already 已经由应用排过 interchangeable，也不是已经 cinotes vs order bundled（444） interchangeable / 1354 cinotes-notapp interchangeable / 1353 cinotes-notblk interchangeable，也不是已经 CiNotes engine guarantees and persists order not already app-sorted / not already recv-order / not already Process-decided 正式三事 bundled（444 item 2 余量） interchangeable / 444 cinotes item 2 interchangeable。**  
   官方把引擎保证并落盘顺序不是已经由应用排过和已经由应用排过写成两件。看见引擎保证并落盘顺序不是已经由应用排过，不是已经由应用排过。

2. **看见engine guarantees and persists order is not already sorted by the app / 看见引擎保证并落盘顺序不是已经由应用排过 / 这份对象 is not already 已经是收到票时的顺序 interchangeable，也不是已经 cinotes vs order bundled（444） interchangeable / 1354 cinotes-notapp interchangeable / 1355 cinotes-notstore interchangeable，也不是已经 VoteInfo 按投票权降序就已经进了块 interchangeable / 365 VoteInfo 按投票权降序就已经进了块 interchangeable。**  
   官方把engine guarantees and persists order is not already sorted by the app和已经是收到票时的顺序写成两件。看见engine guarantees and persists order is not already sorted by the app，不是已经是收到票时的顺序。

3. **看见引擎保证并落盘顺序不是已经由应用排过 / 看见engine guarantees and persists order is not already sorted by the app / 这份对象 is not already 已经由 Process 回包决定 interchangeable，也不是已经 cinotes vs order bundled（444） interchangeable / 1354 cinotes-notapp interchangeable / 1353 cinotes-notblk interchangeable，也不是已经 CommitInfo Fields 栏 interchangeable / 445 CommitInfo Fields 栏 interchangeable。**  
   官方把引擎保证并落盘顺序不是已经由应用排过和已经由 Process 回包决定写成两件。看见引擎保证并落盘顺序不是已经由应用排过，不是已经由 Process 回包决定。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。

## 官方为什么这样拆

- **引擎保证并落盘 不是已经由应用排过 interchangeable：官方把 CometBFT 保证和应用自己排序分开。**
- **看见落盘 不是已经是收到 Precommit 时的顺序。**
- **看见集合更新后会排序 不是已经由 Process 回包决定。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经由应用排过 | 不是已经由应用排过 | 不是已经VoteInfo 按投票权降序就已经进了块（365） |
| 已经是收到票时的顺序 | 不是已经是收到票时的顺序 | 不是已经CommitInfo Fields 栏（445） |
| 已经由 Process 回包决定 | 不是已经由 Process 回包决定 | 不是已经1353 cinotes-notblk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CiNotes engine guarantees and persists order not already app-sorted / not already recv-order / not already Process-decided 正式三事（444 余量），必须分开是不是已经由应用排过、是不是已经是收到票时的顺序、是不是已经由 Process 回包决定。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好」。不要另写 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。444 CommitInfo Notes vote-power order bundled unbundling 在本页 item 2 续；续 [`worked-example-cinotes-notstore-vs-bundled.md`](worked-example-cinotes-notstore-vs-bundled.md)（不变量 1355 item 3）。

## 本页不抄

- 怎样写 CommitInfo Notes 票序正式三事、怎样从 store 再装、怎样排 votes。
- 怎样排 VoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 CommitInfo。
