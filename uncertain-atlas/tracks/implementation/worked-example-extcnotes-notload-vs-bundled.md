# 例：看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出不是已经从拟议块或已决块抽出；看见building ExtendedCommitInfo reloads the set from store is not extracted from the block不是已经是 VoteInfo Usage 抽出路径；看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出不是已经是 CommitInfo Notes 同一句

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedCommitInfo Notes 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtCiNotes rebuild ExtendedCommitInfo from store not already extracted-from-block / not already 365-path / not already 444-cinotes 正式三事（441 余量）/ not 1358 extcnotes-notload interchangeable / not 441 extcinotes-vs-order bundled interchangeable」，不是 extcinotes vs order bundled（441），也不是已经 CommitInfo Notes 从 store 再装（444），也不是已经 VoteInfo typically extracted from proposed or decided block（365）。不要另写 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。

## 官方三件事

1. **看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出 / 看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出 这份对象 is not already 已经从拟议块或已决块抽出 interchangeable，也不是已经 extcinotes vs order bundled（441） interchangeable / 1358 extcnotes-notload interchangeable / 1356 extcnotes-notord interchangeable，也不是已经 ExtCiNotes rebuild ExtendedCommitInfo from store not already extracted-from-block / not already 365-path / not already 444-cinotes 正式三事 bundled（441 item 3 余量） interchangeable / 441 extcnotes item 3 interchangeable。**  
   官方把造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出和已经从拟议块或已决块抽出写成两件。看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出，不是已经从拟议块或已决块抽出。

2. **看见building ExtendedCommitInfo reloads the set from store is not extracted from the block / 看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出 / 这份对象 is not already 已经是 VoteInfo Usage 抽出路径 interchangeable，也不是已经 extcinotes vs order bundled（441） interchangeable / 1358 extcnotes-notload interchangeable / 1357 extcnotes-noteng interchangeable，也不是已经 CommitInfo Notes 从 store 再装 interchangeable / 444 CommitInfo Notes 从 store 再装 interchangeable。**  
   官方把building ExtendedCommitInfo reloads the set from store is not extracted from the block和已经是 VoteInfo Usage 抽出路径写成两件。看见building ExtendedCommitInfo reloads the set from store is not extracted from the block，不是已经是 VoteInfo Usage 抽出路径。

3. **看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出 / 看见building ExtendedCommitInfo reloads the set from store is not extracted from the block / 这份对象 is not already 已经是 CommitInfo Notes 同一句 interchangeable，也不是已经 extcinotes vs order bundled（441） interchangeable / 1358 extcnotes-notload interchangeable / 1356 extcnotes-notord interchangeable，也不是已经 VoteInfo typically extracted from proposed or decided block interchangeable / 365 VoteInfo typically extracted from proposed or decided block interchangeable。**  
   官方把造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出和已经是 CommitInfo Notes 同一句写成两件。看见造 ExtendedCommitInfo 时从 store 再装不是已经从块里抽出，不是已经是 CommitInfo Notes 同一句。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。

## 官方为什么这样拆

- **从 store 再装 ExtendedCommitInfo 不是已经从拟议块或已决块抽出 interchangeable：官方把 local_last_commit 路径和 Process/Finalize 抽出分开。**
- **看见保住顺序 不是已经是 365 Usage typically extracted 那种路径。**
- **看见 Notes 文字和 CommitInfo 很像 不是已经可以用 444 cinotes 代替本页。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经从拟议块或已决块抽出 | 不是已经从拟议块或已决块抽出 | 不是已经CommitInfo Notes 从 store 再装（444） |
| 已经是 VoteInfo Usage 抽出路径 | 不是已经是 VoteInfo Usage 抽出路径 | 不是已经VoteInfo typically extracted from proposed or decided block（365） |
| 已经是 CommitInfo Notes 同一句 | 不是已经是 CommitInfo Notes 同一句 | 不是已经1356 extcnotes-notord |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtCiNotes rebuild ExtendedCommitInfo from store not already extracted-from-block / not already 365-path / not already 444-cinotes 正式三事（441 余量），必须分开是不是已经从拟议块或已决块抽出、是不是已经是 VoteInfo Usage 抽出路径、是不是已经是 CommitInfo Notes 同一句。可以跳过「看见 Prepare 里有 ExtendedCommitInfo 就已经按投票权排好」。不要另写 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。441 ExtendedCommitInfo Notes vote-power order bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样写 ExtendedCommitInfo Notes 票序正式三事、怎样从 store 再装、怎样排 votes。
- 怎样排 ExtendedVoteInfo、怎样从 store 再装验证者集合、怎样从块里抽 ExtendedCommitInfo。
