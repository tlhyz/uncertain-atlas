# 例：看见应用可以用 FinalizeBlockRequest.decided_last_commit 和 misbehavior 定验证者奖惩 / 看见 can use 定奖惩 is not already slashed / 看见 rewards and punishments is not already committed 不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable / 已经罚没 interchangeable / 已经交差 interchangeable

**层次**：实现 / FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「can use decided_last_commit + misbehavior to determine rewards not already slashed 不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable / 不是已经罚没 interchangeable / 不是已经交差 interchangeable」，不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463），也不是 Finalize 回包义务 bundled（363），也不是 VoteInfo 按到场定奖惩（365）。不要另写怎样算奖惩、怎样 slashing。

## 官方三件事

规范把 FinalizeBlock Usage 里 The Application can use decided_last_commit and misbehavior to determine rewards and punishments、VoteInfo 按到场定奖惩、Finalize + Commit 已经交差分开写成三件独立的实现事，不是「看见 can use 定奖惩就已经 slashed interchangeable、已经 VoteInfo 按到场定奖惩 interchangeable、已经 Finalize + Commit 交差 interchangeable」一件事：

1. **看见应用可以用 `FinalizeBlockRequest.decided_last_commit` 和 `FinalizeBlockRequest.misbehavior` 定验证者奖惩 / 看见 can use 定奖惩 is not already slashed / 看见 rewards and punishments is not already FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463） interchangeable / 已经罚没 interchangeable / 已经 determine rewards and punishments interchangeable，也不是已经 Finalize 回包义务 bundled（363 余量） interchangeable / 已经可以用 decided_last_commit 和 misbehavior 定奖惩 interchangeable / 已经必须回四列 interchangeable，也不是已经 Misbehavior.type 只是过错枚举 bundled（372 余量） interchangeable / 已经过错枚举 interchangeable / 已经 slashed interchangeable，也不是已经证据上链就已经罚没 bundled（21 余量） interchangeable / 已经 notify application interchangeable / 已经罚没 interchangeable，也不是已经 FinalizeBlock decided_last_commit from decided block not proposed_last_commit bundled（463 第二件事 / 568） interchangeable / 已经 proposed_last_commit interchangeable / 已经 local_last_commit interchangeable，也不是已经 FinalizeBlock misbehavior not VoteInfo availability bundled（463 第三件事 / 569） interchangeable / 已经 VoteInfo 按到场定奖惩 interchangeable / 已经 Misbehavior.type 就已经罚没 interchangeable。**  
   官方写：The Application can use `FinalizeBlockRequest.decided_last_commit` and `FinalizeBlockRequest.misbehavior` to determine rewards and punishments for the validators。看见 can use 定奖惩，不是已经 slashed——463 bundled 第一件事常被写成「看见能定奖惩就已经罚没」，本页钉 can use decided_last_commit + misbehavior to determine rewards not already slashed 单句。看见 rewards and punishments，不是已经 Finalize 回包义务 bundled（363 余量） interchangeable——363 钉可以用 decided_last_commit 和 misbehavior 定奖惩 + 必须回四列，本页钉 can use 边界。看见 can use，不是已经证据上链（21 余量） interchangeable——21 钉 notify application，本页钉 Finalize Usage can use 单句。
2. **看见 can use 定奖惩 is not already VoteInfo availability rewards / 看见 rewards and punishments is not already VoteInfo / ExtendedVoteInfo Usage allowing for rewards based on validator availability 不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463） interchangeable / 已经 VoteInfo 按到场定奖惩 interchangeable / 已经 block_id_flag interchangeable，也不是已经 VoteInfo 按到场定奖惩 bundled（365 余量） interchangeable / 已经从拟议块或已决块抽出 interchangeable / 已经按投票权降序排 interchangeable，也不是已经 ExtendedVoteInfo Usage 暴露签 bundled（440 余量） interchangeable / 已经 extension_signature interchangeable / 已经应用验完 interchangeable，也不是已经 CommitInfo Fields 栏 bundled（444 余量） interchangeable / 已经 votes 列表 interchangeable / 已经 round interchangeable，也不是已经 FinalizeBlock decided_last_commit from decided block not proposed_last_commit bundled（463 第二件事 / 568） interchangeable / 已经 decided_last_commit interchangeable / 已经 proposed_last_commit interchangeable，也不是已经 FinalizeBlock misbehavior not VoteInfo availability bundled（463 第三件事 / 569） interchangeable / 已经 Misbehavior.type 就已经罚没 interchangeable / 已经过错列表 interchangeable。**  
   官方把 can use decided_last_commit and misbehavior 定奖惩和 VoteInfo block_id_flag 那种按到场定奖惩分开——463 bundled 常与 365 混成「can use 定奖惩 = VoteInfo 按到场定奖惩 interchangeable」，本页钉 can use not VoteInfo availability rewards 单句。看见 rewards and punishments，不是已经 VoteInfo 按到场定奖惩（365 余量） interchangeable——365 钉 block_id_flag / 从拟议块或已决块抽出，本页钉 can use 边界。看见 can use，不是已经 ExtendedVoteInfo Usage 暴露签（440 余量） interchangeable——440 钉 extension_signature 暴露给应用，本页钉 can use decided_last_commit + misbehavior 单句。
3. **看见 can use 定奖惩 is not already Finalize + Commit committed / 看见 determine rewards and punishments is not already four gates settled / 已经交差 不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463） interchangeable / 已经 Finalize + Commit interchangeable / 已经四门已经结算 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经 ran Process interchangeable / 已经四门已经结算 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 已经收成一门 interchangeable / 已经交差 interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（460 余量） interchangeable / 已经不用再在 Process 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 FinalizeBlock decided_last_commit from decided block not proposed_last_commit bundled（463 第二件事 / 568） interchangeable / 已经 local_last_commit interchangeable / 已经 proposed_last_commit interchangeable，也不是已经 FinalizeBlock misbehavior not VoteInfo availability bundled（463 第三件事 / 569） interchangeable / 已经过错列表 interchangeable / 已经 Misbehavior.type 就已经罚没 interchangeable。**  
   官方把 can use 定奖惩和 Finalize + Commit 已经交差分开——463 bundled 常与 460 混成「can use 定奖惩 = 已经交差 interchangeable」，本页钉 can use not already committed 单句。看见 can use，不是已经 FinalizeBlock Contains newly decided block fields not already settled（555 余量） interchangeable——555 钉 Contains newly decided not settled，本页钉 can use 边界。看见 determine rewards and punishments，不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable——465 钉收成一门 / 四门已经结算，本页钉 can use not committed 单句。

怎样算奖惩、怎样 slashing、怎样填 decided_last_commit / misbehavior 是规范里的做法，本页不抄。FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463）、Finalize 回包义务 bundled（363）、VoteInfo 按到场定奖惩（365）是另外那套，本页不抄。

## 官方为什么这样拆

- **can use decided_last_commit + misbehavior to determine rewards not already slashed ≠ FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable：** 官方把 can use 定奖惩和已经 slashed 分开。
- **can use not VoteInfo availability rewards ≠ 365 VoteInfo 按到场定奖惩 interchangeable：** 官方把 can use 定奖惩和 VoteInfo block_id_flag 按到场定奖惩分开。
- **can use not already committed ≠ Finalize + Commit 交差 interchangeable：** 官方把 can use 定奖惩和四门已经结算 / 已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| can use decided_last_commit + misbehavior | 不是 already slashed | 不是 Misbehavior.type 枚举（372） |
| can use 定奖惩 | 不是 VoteInfo availability rewards | 不是 VoteInfo 按到场定奖惩（365） |
| can use 定奖惩 | 不是 already committed | 不是 Finalize + Commit 交差（452） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed 正式三事，必须分开 can use 定奖惩 是不是 already slashed interchangeable / 363 回包义务 interchangeable、can use 定奖惩 是不是 VoteInfo availability rewards interchangeable / 365 VoteInfo 按到场定奖惩 interchangeable、can use 定奖惩 是不是 already committed interchangeable / 586 ABCI 1.0 equiv interchangeable。可以跳过「看见 can use 定奖惩就已经 slashed interchangeable」。不要另写怎样算奖惩。

## 本页不抄

- 怎样算奖惩、怎样 slashing、怎样填 decided_last_commit / misbehavior。
- decided_last_commit 从刚决定那块拿到 ≠ proposed_last_commit。那是不变量 559（463 item 2 余量）。
- misbehavior 过错列表 ≠ VoteInfo 按到场定奖惩。那是不变量 560（463 item 3 余量）。
- Finalize 回包义务 bundled 三事。那是不变量 363。
