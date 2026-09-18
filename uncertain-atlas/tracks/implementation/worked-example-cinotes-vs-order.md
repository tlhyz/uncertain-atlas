# 例：看见 CommitInfo.votes 里的 VoteInfo 按投票权降序排不是已经进了块；看见 CometBFT 通过更新验证者集合的逻辑保证这个顺序、集合写入 store 时顺序也落盘不是已经由应用排过；看见造 CommitInfo 时从 store 再装集合不是已经从拟议块或已决块抽出

**层次**：实现 / CommitInfo Notes 票序正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Notes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CommitInfo.votes 里的 VoteInfo 按投票权降序排不是已经进了块 / CometBFT 通过更新验证者集合的逻辑保证这个顺序、集合写入 store 时顺序也落盘不是已经由应用排过 / 造 CommitInfo 时从 store 再装集合不是已经从拟议块或已决块抽出」，不是 VoteInfo 能按到场定奖惩就已经罚没，也不是 ExtendedCommitInfo Notes 那套话就已经是同一句。不要另写怎样写 CommitInfo Notes 票序正式三事。

## 官方三件事

规范把 CommitInfo Notes 里 votes 按投票权降序排、引擎保证并落盘、造 CommitInfo 时从 store 再装写成三件独立的实现事，不是「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好、已经进了块、已经从块里抽出」一件事：

1. **看见 `CommitInfo.votes` 里的 `VoteInfo` 按投票权降序排 / 看见顺序在 不是已经进了块，也不是已经交差。**  
   官方写：The `VoteInfo` in `votes` are ordered by the voting power of the validators (descending order, highest to lowest voting power). 看见按投票权降序排，不是已经进了块。看见顺序在，不是已经交差。看见 Process / Finalize 里有 `CommitInfo`，不是已经写进 last_commit。
2. **看见 CometBFT 通过更新验证者集合的逻辑保证这个顺序 / 看见集合写入 store 时顺序也落盘 不是已经由应用排过，也不是已经是收到票时的顺序。**  
   官方写：CometBFT guarantees the `votes` ordering through its logic to update the validator set in which, in the end, the validators are sorted (descending) by their voting power. The ordering is also persisted when a validator set is saved in the store. 看见引擎保证，不是已经由应用排过。看见落盘，不是已经是收到 Precommit 时的顺序。看见集合更新后会排序，不是已经由 Process 回包决定。
3. **看见造 `CommitInfo` 时从 store 再装集合、好保住这份顺序 / 看见从 store 装回 不是已经从拟议块或已决块抽出，也不是已经是 ExtendedCommitInfo Notes 那套话就已经是同一句。**  
   官方写：The validator set is loaded from the store when building the `CommitInfo`, ensuring order is maintained from the persisted validator set. 看见从 store 装回，不是已经从拟议块或已决块抽出。看见保住顺序，不是已经是 VoteInfo Usage 里 typically extracted from proposed or decided block 那种路径就代替本页 Notes。看见 Notes 文字和 ExtendedCommitInfo 很像，不是已经可以用不变量 441 代替本页。

怎样写 CommitInfo Notes 票序正式三事、怎样从 store 再装、怎样排 votes 是规范里的做法，本页不抄。VoteInfo 能按到场定奖惩就已经罚没是不变量 365 的 Usage 路径，ExtendedCommitInfo Notes 票序正式三事是不变量 441，本页不抄。

## 官方为什么这样拆

- **VoteInfo 按投票权降序排 ≠ 已经进了块 / 已经交差：** 官方把顺序和已经进规范分开。
- **引擎保证并落盘 ≠ 已经由应用排过 / 已经是收到票时的顺序：** 官方把 CometBFT 保证和应用自己排序分开。
- **从 store 再装 ≠ 已经从拟议块或已决块抽出 / 已经是 ExtendedCommitInfo Notes 同一句：** 官方把 store 路径和块里抽出路径分开，也把 CommitInfo Notes 和 ExtendedCommitInfo Notes 分开写。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VoteInfo 按投票权降序排 | 不是已经进了块 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| 引擎保证并落盘 | 不是已经由应用排过 | 不是 ExtendedCommitInfo.votes 按投票权降序排就已经进了块（441） |
| 从 store 再装 | 不是已经从拟议块或已决块抽出 | 不是 CommitInfo.round 是提交轮就已经按投票权排过（392） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好、已经进了块、已经从块里抽出」，必须分开 CommitInfo.votes 里的 VoteInfo 按投票权降序排是不是已经进了块 / 已经交差、CometBFT 通过更新验证者集合的逻辑保证这个顺序、集合写入 store 时顺序也落盘是不是已经由应用排过 / 已经是收到票时的顺序、造 CommitInfo 时从 store 再装集合是不是已经从拟议块或已决块抽出 / 已经是 ExtendedCommitInfo Notes 那套话就已经是同一句。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经按投票权排好」。444 CommitInfo Notes vote-power order bundled unbundling 完成（1353 item 1 / 1354 item 2 / 1355 item 3）；精读 [`worked-example-cinotes-notblk-vs-bundled.md`](worked-example-cinotes-notblk-vs-bundled.md)（不变量 1353 item 1）、[`worked-example-cinotes-notapp-vs-bundled.md`](worked-example-cinotes-notapp-vs-bundled.md)（不变量 1354 item 2）、[`worked-example-cinotes-notstore-vs-bundled.md`](worked-example-cinotes-notstore-vs-bundled.md)（不变量 1355 item 3）。不要另写怎样写 CommitInfo Notes 票序正式三事。

## 本页不抄

- 怎样写 CommitInfo Notes 票序正式三事、怎样从 store 再装、怎样排 votes。
- VoteInfo 能按到场定奖惩、从拟议块或已决块抽出。那是不变量 365。
- ExtendedCommitInfo.votes 按投票权降序排、从 store 装 ExtendedCommitInfo。那是不变量 441。
- CommitInfo.round 是提交轮。那是不变量 392 的轮次栏，不是本页 Notes 票序。
