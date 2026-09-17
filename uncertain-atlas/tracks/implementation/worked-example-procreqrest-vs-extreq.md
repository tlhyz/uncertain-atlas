# 例：看见 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息不是已经交差 local_last_commit；看见 ProcessProposalRequest.time 是拟议块的时间戳不是已经验过票上时间；看见 ProcessProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩

**层次**：实现 / Process 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息不是已经交差 local_last_commit / ProcessProposalRequest.time 是拟议块的时间戳不是已经验过票上时间 / ProcessProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩」，不是 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息就已经交差 local_last_commit，也不是 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩。不要另写怎样写 Process 请求余栏。

## 官方三件事

规范把 ProcessProposal Request 表上 `proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息、`time` 是拟议块的时间戳、`misbehavior` 是过错验证者信息列表写成三件独立的实现事，不是「看见填了 Process 请求余栏就已经交差 local_last_commit、已经验过票上时间、已经定奖惩」一件事：

1. **看见 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息 / 看见填了 proposed_last_commit 不是已经交差 local_last_commit，也不是已经是 ExtendVoteRequest.proposed_last_commit。**  
   官方写：`proposed_last_commit` 是上一份提交信息，从拟议块里的信息拿到。看见填了 proposed_last_commit，不是已经 `ExtendVoteRequest.proposed_last_commit` 是上一份拟议块的 last commit 信息那种已经交差 local_last_commit。看见从拟议块拿到，不是已经交差。看见能指上一份提交，不是已经跑过 Process。
2. **看见 `ProcessProposalRequest.time` 是拟议块的时间戳 / 看见填了 time 不是已经验过票上时间，也不是已经是 ExtendVoteRequest.time。**  
   官方写：`time` 是拟议块的时间戳。看见填了 time，不是已经 `ExtendVoteRequest.time` 是扩展要指的那份拟议块时间戳那种已经验过票上时间。看见有拟议块时间戳，不是已经 Process 的 height / time 对上拟议块头那种已经验过块头。看见能指时间，不是已经交差。
3. **看见 `ProcessProposalRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior 不是已经定奖惩，也不是已经是 ExtendVoteRequest.misbehavior。**  
   官方写：`misbehavior` 是过错验证者信息列表。看见填了 misbehavior，不是已经 `ExtendVoteRequest.misbehavior` 是拟议块里那些过错信息那种已经定奖惩。看见有过错列表，不是已经罚没。看见能指过错，不是已经交差。

怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time 是规范里的做法，本页不抄。ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息就已经交差 local_last_commit 是不变量 411，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 ≠ 已经交差 local_last_commit：** 官方把 Process 请求表上这份从拟议块拿到的上一份提交和 ExtendVote 请求表上那份上一份拟议块的 last commit 分开。
- **ProcessProposalRequest.time 是拟议块的时间戳 ≠ 已经验过票上时间：** 官方把 Process 请求表上这份拟议块时间戳和 ExtendVote 请求表上那份扩展要指的时间戳分开。
- **ProcessProposalRequest.misbehavior 是过错验证者信息列表 ≠ 已经定奖惩：** 官方把 Process 请求表上这份过错列表和 ExtendVote 请求表上那份拟议块里的过错信息分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 | 不是已经交差 local_last_commit | 不是 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息就已经交差 local_last_commit（411） |
| ProcessProposalRequest.time 是拟议块的时间戳 | 不是已经验过票上时间 | 不是 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳就已经验过票上时间（410） |
| ProcessProposalRequest.misbehavior 是过错验证者信息列表 | 不是已经定奖惩 | 不是 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩（413） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Process 请求余栏就已经交差 local_last_commit、已经验过票上时间、已经定奖惩」，必须分开 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息是不是已经交差 local_last_commit、ProcessProposalRequest.time 是拟议块的时间戳是不是已经验过票上时间、ProcessProposalRequest.misbehavior 是过错验证者信息列表是不是已经定奖惩。可以跳过「看见填了 Process 请求余栏就已经交差 local_last_commit」。不要另写怎样写 Process 请求余栏。

## 本页不抄

- 怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time。
- ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息就已经交差 local_last_commit。那是不变量 411。
- ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳就已经验过票上时间。那是不变量 410。
- ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩。那是不变量 413。
