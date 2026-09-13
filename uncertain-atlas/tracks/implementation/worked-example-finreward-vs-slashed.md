# 例：看见应用可以用 FinalizeBlockRequest.decided_last_commit 和 misbehavior 定验证者奖惩不是已经罚没；看见 decided_last_commit 是从刚决定那块拿到的上一份提交信息不是已经 proposed_last_commit / 已经交差 local_last_commit；看见 misbehavior 是过错验证者信息列表不是已经 VoteInfo 按到场定奖惩 / 已经 Misbehavior.type 就已经罚没

**层次**：实现 / FinalizeBlock decided_last_commit + misbehavior 定奖惩正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 Misbehavior 枚举那页已有边界时对照，本页不另写 mempool 正文。本页是「可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没 / decided_last_commit 从刚决定那块拿到不是已经 proposed_last_commit / misbehavior 是过错列表不是已经 VoteInfo 按到场定奖惩」，不是 Finalize 回包义务 bundled 三事，也不是 Finalize 请求栏 decided vs proposed 单栏定义，也不是 VoteInfo 按到场定奖惩那套。不要另写怎样算奖惩、怎样 slashing。

## 官方三件事

规范把应用可以用 `decided_last_commit` 和 `misbehavior` 定验证者奖惩、`decided_last_commit` 从刚决定那块拿到、`misbehavior` 是过错验证者信息列表写成三件独立的实现事，不是「看见 Finalize 里有 decided_last_commit 和 misbehavior 就已经罚没、已经定奖惩完、已经交差」一件事：

1. **看见应用可以用 `FinalizeBlockRequest.decided_last_commit` 和 `FinalizeBlockRequest.misbehavior` 定验证者奖惩 / 看见能定奖惩 不是已经罚没，也不是已经交差。**  
   官方写：The Application can use `FinalizeBlockRequest.decided_last_commit` and `FinalizeBlockRequest.misbehavior` to determine rewards and punishments for the validators。看见 can use 定奖惩，不是已经 slashed。看见 rewards and punishments，不是已经 VoteInfo 的 block_id_flag 那种按到场定奖惩（365）就已经是同一句 interchangeable。看见能定，不是已经 Finalize + Commit 那种已经交差。
2. **看见 `FinalizeBlockRequest.decided_last_commit` 是从刚决定那块拿到的上一份提交信息 / 看见填了 decided_last_commit 不是已经 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息，也不是已经交差 local_last_commit。**  
   官方 Request 表写：`decided_last_commit` 是上一份提交信息，从刚决定那块拿到。Usage 写可以用它和 misbehavior 定奖惩。看见从刚决定那块拿到，不是已经 proposed_last_commit 那种从拟议块里的信息拿到 interchangeable。看见有上一份 commit，不是已经 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到那种已经交差 local_last_commit。看见能指 decided block 的 commit，不是已经可以用这两列定奖惩那种已经罚没。
3. **看见 `FinalizeBlockRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior 不是已经 VoteInfo / ExtendedVoteInfo Usage 里 allowing for rewards based on validator availability 那种按到场定奖惩，也不是已经 Misbehavior.type 只是过错枚举那种已经罚没。**  
   官方 Request 表写：`misbehavior` 是过错验证者信息列表。Usage 写可以和 decided_last_commit 一起定奖惩。看见有过错列表，不是已经 `ProcessProposalRequest.misbehavior` 是过错验证者信息列表那种已经定奖惩（420）就已经是同一句 interchangeable。看见 Misbehavior 结构，不是已经 MisbehaviorType 枚举（447）就已经 slashed。看见能指过错，不是已经证据上链（21）就已经罚没。

怎样算奖惩、怎样 slashing、怎样填 decided_last_commit / misbehavior 是规范里的做法，本页不抄。Finalize 回包义务 bundled（363）是等价 ABCI 1.0 三步 + 可以用 decided_last_commit 和 misbehavior 定奖惩 + 必须回四列那套另一切片，Finalize 请求栏 decided vs proposed（422）是 decided_last_commit / height / txs 单栏定义，VoteInfo 按到场定奖惩（365）是 block_id_flag / 从拟议块或已决块抽出 / 按投票权降序排那套另一切片，本页不抄。

## 官方为什么这样拆

- **can use decided_last_commit and misbehavior to determine rewards and punishments ≠ 已经罚没 / 已经交差：** 官方把 can use 定奖惩和已经 slashed 分开。
- **decided_last_commit 从刚决定那块拿到 ≠ 已经 proposed_last_commit / 已经交差 local_last_commit：** 官方把 decided block 的 commit 和 proposed / local commit 分开。
- **misbehavior 过错列表 ≠ 已经 VoteInfo 按到场定奖惩 / 已经 Misbehavior.type 就已经罚没：** 官方把过错列表定奖惩和 VoteInfo 到场、Misbehavior 枚举分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| can use decided_last_commit + misbehavior 定奖惩 | 不是已经罚没 | 不是 Finalize 回包义务 bundled（363） |
| decided_last_commit 从刚决定那块拿到 | 不是已经 proposed_last_commit | 不是 Finalize 请求栏 decided vs proposed（422） |
| misbehavior 过错列表 | 不是已经 VoteInfo 按到场定奖惩 | 不是 VoteInfo 按到场定奖惩（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 里有 decided_last_commit 和 misbehavior 就已经罚没、已经定奖惩完」，必须分开 can use decided_last_commit 和 misbehavior 定奖惩是不是已经罚没、decided_last_commit 从刚决定那块拿到是不是已经 proposed_last_commit、misbehavior 过错列表是不是已经 VoteInfo 按到场定奖惩。可以跳过「看见有 misbehavior 就已经罚没」。不要另写怎样算奖惩。

## 本页不抄

- 怎样算奖惩、怎样 slashing、怎样填 decided_last_commit / misbehavior。
- Finalize 回包义务 bundled 三事。那是不变量 363。
- Finalize 请求栏 decided vs proposed 单栏定义。那是不变量 422。
- VoteInfo 按到场定奖惩。那是不变量 365。
- Misbehavior 类型 / 枚举。那是不变量 372 / 447。
- 证据上链就已经罚没。那是不变量 21。
