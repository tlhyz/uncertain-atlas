# 例：看见 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息不是已经交差 proposed_last_commit；看见 PrepareProposalRequest.time 是将要提议那块的时间戳不是已经对上了拟议块头；看见 PrepareProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩

**层次**：实现 / Prepare 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息不是已经交差 proposed_last_commit / PrepareProposalRequest.time 是将要提议那块的时间戳不是已经对上了拟议块头 / PrepareProposalRequest.misbehavior 是过错验证者信息列表不是已经定奖惩」，不是 local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展，也不是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit。不要另写怎样写 Prepare 请求余栏。

## 官方三件事

规范把 PrepareProposal Request 表上 `local_last_commit` 是从本进程 CometBFT 数据结构拿到的上一份提交信息、`time` 是将要提议那块的时间戳、`misbehavior` 是过错验证者信息列表写成三件独立的实现事，不是「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit、已经对上了拟议块头、已经定奖惩」一件事：

1. **看见 `PrepareProposalRequest.local_last_commit` 是从本进程 CometBFT 数据结构拿到的上一份提交信息 / 看见填了 local_last_commit 不是已经交差 proposed_last_commit，也不是已经是上一高度的预提交带扩展。**  
   官方写：`local_last_commit` 是上一份提交信息，从本进程 CometBFT 数据结构拿到。看见填了 local_last_commit，不是已经 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息那种已经交差 local_last_commit。看见从本进程拿到，不是已经 `local_last_commit` 是上一高度的预提交带扩展那种已经是本高度刚签的扩展。看见能指上一份提交，不是已经交差。
2. **看见 `PrepareProposalRequest.time` 是将要提议那块的时间戳 / 看见填了 time 不是已经对上了拟议块头，也不是已经是 ProcessProposalRequest.time。**  
   官方写：`time` 是将要提议那块的时间戳。看见填了 time，不是已经 `ProcessProposalRequest.time` 是拟议块的时间戳那种已经验过票上时间。看见有将要提议的时间戳，不是已经 Prepare 的 `height` / `time` / `proposer_address` 对上拟议头那种已经知道本头哈希。看见能指时间，不是已经交差。
3. **看见 `PrepareProposalRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior 不是已经定奖惩，也不是已经是 ProcessProposalRequest.misbehavior。**  
   官方写：`misbehavior` 是过错验证者信息列表。看见填了 misbehavior，不是已经 `ProcessProposalRequest.misbehavior` 是过错验证者信息列表那种已经定奖惩。看见有过错列表，不是已经 `ExtendVoteRequest.misbehavior` 是拟议块里那些过错信息那种已经罚没。看见能指过错，不是已经交差。

怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time 是规范里的做法，本页不抄。local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展是不变量 359，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息 ≠ 已经交差 proposed_last_commit：** 官方把 Prepare 请求表上这份从本进程拿到的上一份提交和 Process 请求表上那份从拟议块拿到的上一份提交分开。
- **PrepareProposalRequest.time 是将要提议那块的时间戳 ≠ 已经对上了拟议块头：** 官方把 Prepare 请求表上这份将要提议那块的时间戳和 Process 请求表上那份拟议块时间戳分开。
- **PrepareProposalRequest.misbehavior 是过错验证者信息列表 ≠ 已经定奖惩：** 官方把 Prepare 请求表上这份过错列表和 Process 请求表上那份过错列表分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息 | 不是已经交差 proposed_last_commit | 不是 local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展（359） |
| PrepareProposalRequest.time 是将要提议那块的时间戳 | 不是已经对上了拟议块头 | 不是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit（420） |
| PrepareProposalRequest.misbehavior 是过错验证者信息列表 | 不是已经定奖惩 | 不是 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩（413） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit、已经对上了拟议块头、已经定奖惩」，必须分开 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息是不是已经交差 proposed_last_commit、PrepareProposalRequest.time 是将要提议那块的时间戳是不是已经对上了拟议块头、PrepareProposalRequest.misbehavior 是过错验证者信息列表是不是已经定奖惩。可以跳过「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit」。不要另写怎样写 Prepare 请求余栏。

## 本页不抄

- 怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time。
- local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展。那是不变量 359。
- ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit。那是不变量 420。
- ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就已经定奖惩。那是不变量 413。
