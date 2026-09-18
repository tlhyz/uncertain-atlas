# 例：看见 FinalizeBlockRequest.hash 是已决块的哈希不是已经是 ProcessProposalRequest.hash；看见 FinalizeBlockRequest.misbehavior 是过错验证者信息列表不是已经定奖惩；看见 FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Process 请求末栏的 next_validators_hash

**层次**：实现 / Finalize 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.hash 是已决块的哈希不是已经是 ProcessProposalRequest.hash / FinalizeBlockRequest.misbehavior 是过错验证者信息列表不是已经定奖惩 / FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Process 请求末栏的 next_validators_hash」，不是 ProcessProposalRequest.hash 是拟议块的哈希就已经跑过 Process，也不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没。不要另写怎样写 Finalize 请求余栏。

## 官方三件事

规范把 FinalizeBlock Request 表上 `hash` 是已决块的哈希、`misbehavior` 是过错验证者信息列表、`next_validators_hash` 是下一验证者集合默克尔根写成三件独立的实现事，不是「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash、已经定奖惩、已经是 Process 请求末栏的 next_validators_hash」一件事：

1. **看见 `FinalizeBlockRequest.hash` 是已决块的哈希 / 看见填了 hash 不是已经是 ProcessProposalRequest.hash，也不是已经跑过 Process。**  
   官方写：`hash` 是已决块的哈希。看见填了 hash，不是已经 `ProcessProposalRequest.hash` 是拟议块的哈希那种已经跑过 Process。看见能指已决块，不是已经 `ExtendVoteRequest.hash` 是扩展要指的那份拟议块头哈希那种已经知道本头哈希。看见字段名对得上，不是已经交差。
2. **看见 `FinalizeBlockRequest.misbehavior` 是过错验证者信息列表 / 看见填了 misbehavior 不是已经定奖惩，也不是已经是 ProcessProposalRequest.misbehavior。**  
   官方写：`misbehavior` 是过错验证者信息列表。看见填了 misbehavior，不是已经可以用 `decided_last_commit` 和 `misbehavior` 定奖惩那种已经罚没。看见有过错列表，不是已经 `ProcessProposalRequest.misbehavior` 是过错验证者信息列表那种已经定奖惩。看见能指过错，不是已经交差。
3. **看见 `FinalizeBlockRequest.next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash 不是已经是 Process 请求末栏的 next_validators_hash，也不是已经是 Prepare 请求末栏的 next_validators_hash。**  
   官方写：`next_validators_hash` 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经 `ProcessProposalRequest.next_validators_hash` 是下一验证者集合默克尔根那种已经是 Prepare 请求末栏的 next_validators_hash。看见能指下一份集合，不是已经 `PrepareProposalRequest.next_validators_hash` 是下一验证者集合默克尔根那种已经是 Finalize 请求栏的 next_validators_hash。看见字段名对得上，不是已经换了人。

怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior 是规范里的做法，本页不抄。ProcessProposalRequest.hash 是拟议块的哈希就已经跑过 Process 是不变量 419，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.hash 是已决块的哈希 ≠ 已经是 ProcessProposalRequest.hash：** 官方把 Finalize 请求表上这份已决块哈希和 Process 请求表上那份拟议块哈希分开。
- **FinalizeBlockRequest.misbehavior 是过错验证者信息列表 ≠ 已经定奖惩：** 官方把 Finalize 请求表上这份过错列表和 Usage 里那份可以用 decided_last_commit 和 misbehavior 定奖惩分开。
- **FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Process 请求末栏的 next_validators_hash：** 官方把 Finalize 请求表上这份下一验证者集合默克尔根和 Process 请求表上那份下一验证者集合默克尔根分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.hash 是已决块的哈希 | 不是已经是 ProcessProposalRequest.hash | 不是 ProcessProposalRequest.hash 是拟议块的哈希就已经跑过 Process（419） |
| FinalizeBlockRequest.misbehavior 是过错验证者信息列表 | 不是已经定奖惩 | 不是 ProcessProposalRequest.misbehavior 是过错验证者信息列表就已经定奖惩（420） |
| FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根 | 不是已经是 Process 请求末栏的 next_validators_hash | 不是 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Prepare 请求末栏的 next_validators_hash（427） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash、已经定奖惩、已经是 Process 请求末栏的 next_validators_hash」，必须分开 FinalizeBlockRequest.hash 是已决块的哈希是不是已经是 ProcessProposalRequest.hash、FinalizeBlockRequest.misbehavior 是过错验证者信息列表是不是已经定奖惩、FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根是不是已经是 Process 请求末栏的 next_validators_hash。可以跳过「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash」。不要另写怎样写 Finalize 请求余栏。428 finreqrest vs procreq bundled unbundling 完成（1061 item 1 / 1062 item 2 / 1063 item 3）；精读 [`worked-example-finrestr-nothash-vs-bundled.md`](worked-example-finrestr-nothash-vs-bundled.md)（不变量 1061 item 1）。

## 本页不抄

- 怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior。
- ProcessProposalRequest.hash 是拟议块的哈希就已经跑过 Process。那是不变量 419。
- ProcessProposalRequest.misbehavior 是过错验证者信息列表就已经定奖惩。那是不变量 420。
- ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Prepare 请求末栏的 next_validators_hash。那是不变量 427。
