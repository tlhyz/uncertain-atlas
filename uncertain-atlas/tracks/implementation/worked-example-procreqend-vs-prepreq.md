# 例：看见 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Prepare 请求末栏的 next_validators_hash；看见 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案；看见 PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表不是已经是初步交易列表

**层次**：实现 / Process 请求末栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根不是已经是 Prepare 请求末栏的 next_validators_hash / ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案 / PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表不是已经是初步交易列表」，不是 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Finalize 请求栏的 next_validators_hash，也不是 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希。不要另写怎样写 Process 请求末栏。

## 官方三件事

规范把 ProcessProposal Request 表上 `next_validators_hash` 是下一验证者集合默克尔根、`proposer_address` 是造了这份提案的验证者地址、PrepareProposal Response 表上 `txs` 是可能改过的、挑进拟议块的交易列表写成三件独立的实现事，不是「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash、已经正在造这份提案、已经是初步交易列表」一件事：

1. **看见 `ProcessProposalRequest.next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash 不是已经是 Prepare 请求末栏的 next_validators_hash，也不是已经是 Finalize 请求栏的 next_validators_hash。**  
   官方写：`next_validators_hash` 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经 `PrepareProposalRequest.next_validators_hash` 是下一验证者集合默克尔根那种已经是 Finalize 请求栏的 next_validators_hash。看见能指下一份集合，不是已经 Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根那种已经是同一套字段。看见字段名对得上，不是已经交差。
2. **看见 `ProcessProposalRequest.proposer_address` 是造了这份提案的验证者地址 / 看见填了 proposer_address 不是已经正在造这份提案，也不是已经知道本头哈希。**  
   官方写：`proposer_address` 是造了这份提案的验证者地址。看见填了 proposer_address，不是已经 `PrepareProposalRequest.proposer_address` 是正在造这份提案的验证者地址那种已经正在造。看见造了，不是已经 `ExtendVoteRequest.proposer_address` 是造这份提案的验证者地址那种已经知道本头哈希。看见能指造了的人，不是已经交差。
3. **看见 `PrepareProposalResponse.txs` 是可能改过的、挑进拟议块的交易列表 / 看见回了 txs 不是已经是初步交易列表，也不是已经保证是这一次。**  
   官方写：`txs` 是可能改过的、挑进拟议块的交易列表。看见回了 txs，不是已经 `PrepareProposalRequest.txs` 是挑进拟议块的初步交易列表那种已经跑过 Process。看见可能改过，不是已经通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` 那种已经保证是这一次。看见能指回包列表，不是已经交差。

怎样写 Process 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Finalize 请求栏的 next_validators_hash 是不变量 426，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是 Prepare 请求末栏的 next_validators_hash：** 官方把 Process 请求表上这份下一验证者集合默克尔根和 Prepare 请求表上那份下一验证者集合默克尔根分开。
- **ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址 ≠ 已经正在造这份提案：** 官方把 Process 请求表上这份造了这份提案的验证者地址和 Prepare 请求表上那份正在造这份提案的验证者地址分开。
- **PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表 ≠ 已经是初步交易列表：** 官方把 Prepare 回包表上这份可能改过的列表和 Prepare 请求表上那份初步列表分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根 | 不是已经是 Prepare 请求末栏的 next_validators_hash | 不是 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Finalize 请求栏的 next_validators_hash（426） |
| ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址 | 不是已经正在造这份提案 | 不是 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希（413） |
| PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表 | 不是已经是初步交易列表 | 不是 PrepareProposalRequest.txs 是挑进拟议块的初步交易列表就已经跑过 Process（423） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash、已经正在造这份提案、已经是初步交易列表」，必须分开 ProcessProposalRequest.next_validators_hash 是下一验证者集合默克尔根是不是已经是 Prepare 请求末栏的 next_validators_hash、ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址是不是已经正在造这份提案、PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表是不是已经是初步交易列表。可以跳过「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash」。不要另写怎样写 Process 请求末栏。

## 本页不抄

- 怎样写 Process 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根就已经是 Finalize 请求栏的 next_validators_hash。那是不变量 426。
- ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就已经知道本头哈希。那是不变量 413。
- PrepareProposalRequest.txs 是挑进拟议块的初步交易列表就已经跑过 Process。那是不变量 423。
