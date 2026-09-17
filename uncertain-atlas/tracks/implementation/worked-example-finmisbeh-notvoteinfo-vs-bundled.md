# 例：看见 FinalizeBlockRequest.misbehavior 是过错验证者信息列表 / misbehavior fault list is not already VoteInfo / ExtendedVoteInfo Usage allowing for rewards based on validator availability / misbehavior fault list is not already ProcessProposalRequest.misbehavior 已经定奖惩 不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable / 已经 VoteInfo 按到场定奖惩 interchangeable / 已经 Misbehavior.type 就已经罚没 interchangeable

**层次**：实现 / FinalizeBlock misbehavior not VoteInfo availability 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 Misbehavior 枚举那页已有边界时对照，本页不另写 mempool 正文。本页是「misbehavior fault list not VoteInfo availability rewards 不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable / 不是已经 VoteInfo 按到场定奖惩 interchangeable / 不是已经 Misbehavior.type 就已经罚没 interchangeable」，不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463），也不是 VoteInfo 按到场定奖惩（365），也不是 Misbehavior.type 只是过错枚举（372 / 447）。不要另写怎样算奖惩、怎样 slashing。

## 官方三件事

规范把 FinalizeBlock Request 表上 `misbehavior` 是过错验证者信息列表、VoteInfo / ExtendedVoteInfo Usage 里 allowing for rewards based on validator availability、ProcessProposalRequest.misbehavior 是过错验证者信息列表、Misbehavior.type 只是过错枚举分开写成三件独立的实现事，不是「看见 misbehavior 过错列表 就已经 VoteInfo 按到场定奖惩 interchangeable、已经 ProcessProposalRequest.misbehavior 已经定奖惩 interchangeable、已经 Misbehavior.type 就已经 slashed interchangeable」一件事：

1. **看见 FinalizeBlockRequest.misbehavior 是过错验证者信息列表 / 看见 misbehavior fault list is not already VoteInfo / ExtendedVoteInfo Usage allowing for rewards based on validator availability / 看见过错列表 is not already FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463） interchangeable / 已经 VoteInfo 按到场定奖惩 interchangeable / 已经 block_id_flag interchangeable，也不是已经 VoteInfo 按到场定奖惩 bundled（365 余量） interchangeable / 已经从拟议块或已决块抽出 interchangeable / 已经按投票权降序排 interchangeable，也不是已经 ExtendedVoteInfo Usage 暴露签 bundled（440 余量） interchangeable / 已经 extension_signature interchangeable / 已经应用验完 interchangeable，也不是已经 CommitInfo Fields 栏 bundled（444 余量） interchangeable / 已经 votes 列表 interchangeable / 已经 round interchangeable，也不是已经 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed bundled（463 第一件事 / 567） interchangeable / 已经 slashed interchangeable / 已经 determine rewards and punishments interchangeable，也不是已经 FinalizeBlock decided_last_commit from decided block not proposed_last_commit bundled（463 第二件事 / 568） interchangeable / 已经 proposed_last_commit interchangeable / 已经 local_last_commit interchangeable。**  
   官方 Request 表写：`misbehavior` 是过错验证者信息列表。VoteInfo / ExtendedVoteInfo Usage 写 allowing for rewards based on validator availability。看见过错列表，不是已经 VoteInfo 的 block_id_flag 那种按到场定奖惩（365）就已经是同一句 interchangeable——463 bundled 第三件事常被写成「看见 misbehavior 就已经 VoteInfo 按到场定奖惩 interchangeable」，本页钉 misbehavior fault list not VoteInfo availability rewards 单句。看见 misbehavior，不是已经 VoteInfo 按到场定奖惩 bundled（365 余量） interchangeable——365 钉 block_id_flag / 从拟议块或已决块抽出 / 按投票权降序排，本页钉 misbehavior 过错列表边界。看见过错验证者信息列表，不是已经 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed（567） interchangeable——558 钉 can use 定奖惩 not slashed，本页钉 misbehavior vs VoteInfo 按到场定奖惩 单句。
2. **看见 misbehavior fault list is not already ProcessProposalRequest.misbehavior 已经定奖惩 / 看见填了 misbehavior is not already Process 请求余栏 bundled（420 余量） interchangeable / 已经定奖惩 interchangeable / 已经 ProcessProposalRequest.misbehavior 是过错验证者信息列表 interchangeable 不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463） interchangeable / 已经 ProcessProposalRequest.misbehavior interchangeable / 已经 ExtendVoteRequest.misbehavior interchangeable，也不是已经 Finalize 请求余栏 bundled（428 余量） interchangeable / 已经 FinalizeBlockRequest.misbehavior interchangeable / 已经 ProcessProposalRequest.misbehavior interchangeable，也不是已经 Prepare 请求余栏 bundled（424 余量） interchangeable / 已经 PrepareProposalRequest.misbehavior interchangeable / 已经 ProcessProposalRequest.misbehavior interchangeable，也不是已经 ProcessProposalRequest.misbehavior 是过错验证者信息列表 Request栏（420 余量） interchangeable / 已经 ExtendVoteRequest.misbehavior interchangeable / 已经 proposed_last_commit interchangeable，也不是已经 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed bundled（463 第一件事 / 567） interchangeable / 已经 slashed interchangeable / 已经 determine rewards and punishments interchangeable。**  
   官方把 Finalize 请求表上这份过错列表和 Process 请求表上那份过错列表分开——463 bundled 常与 420 混成「Finalize misbehavior 就已经 ProcessProposalRequest.misbehavior 已经定奖惩 interchangeable」，本页钉 misbehavior fault list not ProcessProposal misbehavior already定奖惩 单句。看见 misbehavior，不是已经 Process 请求余栏 bundled（420 余量） interchangeable——420 钉 proposed_last_commit / time / misbehavior 三栏，本页钉 misbehavior 过错列表 vs 已经定奖惩 边界。看见过错列表，不是已经 Finalize 请求余栏 bundled（428 余量） interchangeable——428 钉 hash / misbehavior / next_validators_hash，本页钉 Finalize misbehavior not Process misbehavior already定奖惩 单句。
3. **看见 misbehavior fault list is not already Misbehavior.type 只是过错枚举 / 看见填了 misbehavior is not already MisbehaviorType enum already slashed 不是已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463） interchangeable / 已经 Misbehavior.type 就已经罚没 interchangeable / 已经过错枚举 interchangeable，也不是已经 Misbehavior.type 只是过错枚举 bundled（372 余量） interchangeable / 已经 slashed interchangeable / 已经 height/time 栏 interchangeable，也不是已经 MisbehaviorType 枚举 bundled（447 余量） interchangeable / 已经 UNKNOWN / DUPLICATE_VOTE / LIGHT_CLIENT_ATTACK interchangeable / 已经 slashed interchangeable，也不是已经证据上链就已经罚没 bundled（21 余量） interchangeable / 已经 notify application interchangeable / 已经罚没 interchangeable，也不是已经 FinalizeBlock can use decided_last_commit + misbehavior to determine rewards not already slashed bundled（463 第一件事 / 567） interchangeable / 已经 determine rewards and punishments interchangeable / 已经 slashed interchangeable，也不是已经 Misbehavior height/time 栏 bundled（449 余量） interchangeable / 已经定了奖惩 interchangeable / 已经 slashed interchangeable。**  
   官方把 Finalize 请求表上 misbehavior 过错列表和 Misbehavior.type 只是过错枚举分开——463 bundled 常与 372 / 447 混成「看见 misbehavior 就已经 Misbehavior.type 就已经 slashed interchangeable」，本页钉 misbehavior fault list not Misbehavior.type already slashed 单句。看见过错列表，不是已经 Misbehavior.type 只是过错枚举（372 余量） interchangeable——372 钉 type 枚举不是已经罚没，本页钉 misbehavior 列表边界。看见 misbehavior，不是已经证据上链（21 余量） interchangeable——21 钉 notify application，本页钉 misbehavior 过错列表 vs 已经 slashed 单句。

怎样算奖惩、怎样 slashing、怎样填 misbehavior 是规范里的做法，本页不抄。FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled（463）、VoteInfo 按到场定奖惩（365）、Misbehavior.type 只是过错枚举（372 / 447）是另外那套，本页不抄。

## 官方为什么这样拆

- **misbehavior fault list not VoteInfo availability rewards ≠ FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable：** 官方把过错列表定奖惩和 VoteInfo block_id_flag 按到场定奖惩分开。
- **misbehavior fault list not ProcessProposal misbehavior already定奖惩 ≠ 420 Process 请求余栏 interchangeable：** 官方把 Finalize misbehavior 过错列表和 Process 请求表上 misbehavior 已经定奖惩分开。
- **misbehavior fault list not Misbehavior.type already slashed ≠ 372 / 447 枚举 interchangeable：** 官方把过错列表和 Misbehavior 枚举就已经 slashed 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| misbehavior fault list | 不是 VoteInfo availability rewards | 不是 VoteInfo 按到场定奖惩（365） |
| misbehavior fault list | 不是 ProcessProposal misbehavior already定奖惩 | 不是 ProcessProposalRequest.misbehavior（420） |
| misbehavior fault list | 不是 Misbehavior.type already slashed | 不是 Misbehavior.type 只是过错枚举（372 / 447） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock misbehavior not VoteInfo availability 正式三事，必须分开 misbehavior fault list 是不是 VoteInfo availability rewards interchangeable / 365 VoteInfo 按到场定奖惩 interchangeable / 567 can use not slashed interchangeable、misbehavior fault list 是不是 ProcessProposal misbehavior already定奖惩 interchangeable / 420 Process 请求余栏 interchangeable / 428 Finalize 请求余栏 interchangeable、misbehavior fault list 是不是 Misbehavior.type already slashed interchangeable / 372 枚举 interchangeable / 21 证据上链 interchangeable。可以跳过「看见 misbehavior 过错列表 就已经 VoteInfo 按到场定奖惩 interchangeable」。不要另写怎样算奖惩。

## 本页不抄

- 怎样算奖惩、怎样 slashing、怎样填 misbehavior。
- can use decided_last_commit + misbehavior to determine rewards not already slashed。那是不变量 567（463 item 1 余量）。
- decided_last_commit from decided block not proposed_last_commit。那是不变量 568（463 item 2 余量）。
- VoteInfo 按到场定奖惩 bundled 三事。那是不变量 365。
- Misbehavior 类型 / 枚举。那是不变量 372 / 447。
- 证据上链就已经罚没。那是不变量 21。
