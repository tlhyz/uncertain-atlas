# 例：看见 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Finalize 请求栏的 next_validators_hash；看见 PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址不是已经造了这份提案；看见 FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头

**层次**：实现 / Prepare 请求末栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Finalize 请求栏的 next_validators_hash / PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址不是已经造了这份提案 / FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头」，不是 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根就已经是同一套字段，也不是 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希。不要另写怎样写 Prepare 请求末栏。

## 官方三件事

规范把 PrepareProposal Request 表上 `next_validators_hash` 是下一验证者集合默克尔根、`proposer_address` 是正在造这份提案的验证者地址、FinalizeBlock Request 表上 `time` 是已决块的时间戳写成三件独立的实现事，不是「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash、已经造了这份提案、已经对上了拟议块头」一件事：

1. **看见 `PrepareProposalRequest.next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash 不是已经是 Finalize 请求栏的 next_validators_hash，也不是已经换了人。**  
   官方写：`next_validators_hash` 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经 Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根那种已经是同一套字段。看见能指下一份集合，不是已经 `ExtendVoteRequest.next_validators_hash` 是下一份验证者集合的哈希那种已经换了人。看见字段名对得上，不是已经交差。
2. **看见 `PrepareProposalRequest.proposer_address` 是正在造这份提案的验证者地址 / 看见填了 proposer_address 不是已经造了这份提案，也不是已经知道本头哈希。**  
   官方写：`proposer_address` 是正在造这份提案的验证者地址。看见填了 proposer_address，不是已经 `ExtendVoteRequest.proposer_address` 是造这份提案的验证者地址那种已经知道本头哈希。看见正在造，不是已经造完。看见能指正在造的人，不是已经 Prepare 的 `height` / `time` / `proposer_address` 对上拟议头那种已经知道本头哈希。
3. **看见 `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 time 不是已经对上了拟议块头，也不是已经是 PrepareProposalRequest.time。**  
   官方写：`time` 是已决块的时间戳。看见填了 time，不是已经 `PrepareProposalRequest.time` 是将要提议那块的时间戳那种已经对上了拟议块头。看见有已决块时间戳，不是已经 `ProcessProposalRequest.time` 是拟议块的时间戳那种已经验过票上时间。看见能指已决时间，不是已经交差。

怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。Finalize 请求 next_validators_hash 是下一验证者集合默克尔根就已经是同一套字段是不变量 394，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Finalize 请求栏的 next_validators_hash：** 官方把 Prepare 请求表上这份下一验证者集合默克尔根和 Finalize 请求表上那份下一验证者集合默克尔根分开。
- **PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址 ≠ 已经造了这份提案：** 官方把 Prepare 请求表上这份正在造这份提案的验证者地址和 ExtendVote 请求表上那份造了这份提案的验证者地址分开。
- **FinalizeBlockRequest.time 是已决块的时间戳 ≠ 已经对上了拟议块头：** 官方把 Finalize 请求表上这份已决块时间戳和 Prepare 请求表上那份将要提议那块的时间戳分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根 | 不是已经是 Finalize 请求栏的 next_validators_hash | 不是 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根就已经是同一套字段（394） |
| PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址 | 不是已经造了这份提案 | 不是 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希（413） |
| FinalizeBlockRequest.time 是已决块的时间戳 | 不是已经对上了拟议块头 | 不是 PrepareProposalRequest.time 是将要提议那块的时间戳就已经对上了拟议块头（424） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash、已经造了这份提案、已经对上了拟议块头」，必须分开 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根是不是已经是 Finalize 请求栏的 next_validators_hash、PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址是不是已经造了这份提案、FinalizeBlockRequest.time 是已决块的时间戳是不是已经对上了拟议块头。可以跳过「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash」。不要另写怎样写 Prepare 请求末栏。

## 本页不抄

- 怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- Finalize 请求 next_validators_hash 是下一验证者集合默克尔根就已经是同一套字段。那是不变量 394。
- ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希。那是不变量 413。
- PrepareProposalRequest.time 是将要提议那块的时间戳就已经对上了拟议块头。那是不变量 424。
