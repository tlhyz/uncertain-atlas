# 例：看见 Validator 装在 CommitInfo 里用于 ProcessProposal 不是已经 PrepareProposal 里的 ExtendedCommitInfo；看见 Validator 装在 CommitInfo 里用于 FinalizeBlock 不是已经 Process 里的 proposed_last_commit 同一路；看见 Validator 装在 ExtendedCommitInfo 里用于 PrepareProposal 不是已经 Process/Finalize 里的 CommitInfo 同一路

**层次**：实现 / Validator Usage 四门映射正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Validator 装在 CommitInfo 里用于 ProcessProposal 不是已经 PrepareProposal 里的 ExtendedCommitInfo / Validator 装在 CommitInfo 里用于 FinalizeBlock 不是已经 Process 里的 proposed_last_commit 同一路 / Validator 装在 ExtendedCommitInfo 里用于 PrepareProposal 不是已经 Process/Finalize 里的 CommitInfo 同一路」，不是 Validator 用 address 认人就已经带了公钥，也不是 VoteInfo 通常从拟议块或已决块抽出就已经从本进程抽出。不要另写怎样写 Validator Usage 四门映射正式三事。

## 官方三件事

规范把 `Validator` 装在 `VoteInfo`/`CommitInfo` 给 Process 和 Finalize、装在 `ExtendedCommitInfo` 给 Prepare 写成三件独立的实现事，不是「看见 Prepare / Process / Finalize 里都有验证者就已经同一门、同一路、可以互换」一件事：

1. **看见 Validator 作为 `VoteInfo` 的一部分装在 `CommitInfo` 里、用于 `ProcessProposal` / 看见 Process 路径 不是已经 `PrepareProposal` 里的 `ExtendedCommitInfo`，也不是已经 `local_last_commit` 同一份。**  
   官方写：Used as part of `VoteInfo` within `CommitInfo` (used in `ProcessProposal` and `FinalizeBlock`). 看见 Process 收到的是 `proposed_last_commit` 里的 `CommitInfo`，不是已经是 Prepare 里的 `ExtendedCommitInfo`。看见 `VoteInfo` 里的 `Validator` 只有 address 和 power，不是已经 Prepare 路径。看见 Process 门，不是已经 local 结构那一路。
2. **看见 Validator 作为 `VoteInfo` 的一部分装在 `CommitInfo` 里、用于 `FinalizeBlock` / 看见 Finalize 路径 不是已经 Process 里的 `proposed_last_commit` 同一路，也不是看见 `decided_last_commit` 就已经交差。**  
   官方写：`CommitInfo` 也用于 `FinalizeBlock`。Finalize 收到的是 `decided_last_commit` 里的 `CommitInfo`，从刚决定那块拿到上一份提交信息。看见 Finalize 路径，不是已经 Process 拟议块里的 `proposed_last_commit` 同一份对象。看见 decided，不是已经交差。看见 `VoteInfo` 里的 `Validator`，不是已经可以拿 Prepare 的 `ExtendedCommitInfo` 代替。
3. **看见 Validator 作为 `ExtendedVoteInfo` 的一部分装在 `ExtendedCommitInfo` 里、用于 `PrepareProposal` / 看见 Prepare 路径 不是已经 Process/Finalize 里的 `CommitInfo` 同一路，也不是已经可以拿 `CommitInfo` 代替 `ExtendedCommitInfo`。**  
   官方写：Used as part of `ExtendedCommitInfo` (used in `PrepareProposal`). Prepare 收到的是 `local_last_commit` 里的 `ExtendedCommitInfo`，从本进程 CometBFT 数据结构拿到。看见 Prepare 路径，不是已经 Process 里的 `CommitInfo`。看见 Extended 结构，不是已经 VoteInfo 从拟议块或已决块抽出那种路径。看见可以带扩展，不是已经和 `CommitInfo`  interchangeable。

怎样写 Validator Usage 四门映射正式三事、怎样填 `proposed_last_commit` / `decided_last_commit` / `local_last_commit` 是规范里的做法，本页不抄。Validator 用 address 认人就已经带了公钥是不变量 364，VoteInfo 通常从拟议块或已决块抽出就已经从本进程抽出是不变量 442，本页不抄。

## 官方为什么这样拆

- **Process 的 CommitInfo ≠ Prepare 的 ExtendedCommitInfo：** 官方把 Process 拟议路径和 Prepare 本地路径分开。
- **Finalize 的 decided_last_commit ≠ Process 的 proposed_last_commit：** 官方把已决块路径和拟议块路径分开。
- **Prepare 的 ExtendedCommitInfo ≠ Process/Finalize 的 CommitInfo：** 官方把 Extended 结构和 VoteInfo/CommitInfo 结构分开写进不同门。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 的 CommitInfo | 不是已经 Prepare 的 ExtendedCommitInfo | 不是 Validator 用 address 认人就已经带了公钥（364） |
| Finalize 的 decided_last_commit | 不是已经 Process 的 proposed_last_commit | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |
| Prepare 的 ExtendedCommitInfo | 不是已经 Process/Finalize 的 CommitInfo | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare / Process / Finalize 里都有验证者就已经同一门、同一路」，必须分开 Validator 装在 CommitInfo 里用于 ProcessProposal 是不是已经 PrepareProposal 里的 ExtendedCommitInfo / 已经是 local_last_commit 同一份、Validator 装在 CommitInfo 里用于 FinalizeBlock 是不是已经 Process 里的 proposed_last_commit 同一路 / 已经是 decided_last_commit 就已经交差、Validator 装在 ExtendedCommitInfo 里用于 PrepareProposal 是不是已经 Process/Finalize 里的 CommitInfo 同一路 / 已经可以拿 CommitInfo 代替 ExtendedCommitInfo。可以跳过「看见四门里都有 Validator 就已经同一门」。449 Validator Usage four-gate mapping bundled unbundling 完成（1371 item 1 / 1372 item 2 / 1373 item 3）；精读 [`worked-example-valuse-notproc-vs-bundled.md`](worked-example-valuse-notproc-vs-bundled.md)（不变量 1371 item 1）、[`worked-example-valuse-notfin-vs-bundled.md`](worked-example-valuse-notfin-vs-bundled.md)（不变量 1372 item 2）、[`worked-example-valuse-notprep-vs-bundled.md`](worked-example-valuse-notprep-vs-bundled.md)（不变量 1373 item 3）。不要另写怎样写 Validator Usage 四门映射正式三事。

## 本页不抄

- 怎样写 Validator Usage 四门映射正式三事、怎样填 `proposed_last_commit` / `decided_last_commit` / `local_last_commit`。
- Validator 用 address 认人、不带 PubKey、ValidatorUpdate 用公钥认人。那是不变量 364。
- VoteInfo 能按到场定奖惩、从拟议块或已决块抽出、按投票权降序排。那是不变量 365。
- ExtendedVoteInfo 从本进程抽出、availability 同句、两条 Usage 抽取异路。那是不变量 369 / 442。
