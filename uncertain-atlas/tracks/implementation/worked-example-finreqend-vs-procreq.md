# 例：看见 FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案；看见 FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头；看见 FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史

**层次**：实现 / Finalize 请求末栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案 / FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头 / FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史」，不是 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址就已经正在造这份提案，也不是 Finalize 的 height / time 对上拟议块头就已经验过块头。不要另写怎样写 Finalize 请求末栏。

## 官方三件事

规范把 FinalizeBlock Request 表上 `proposer_address` 是造了这份提案的验证者地址、`time` 是已决块的时间戳、`syncing_to_height` 在同步或重放时等于目标高、否则等于本高写成三件独立的实现事，不是「看见填了 Finalize 请求末栏就已经正在造这份提案、已经对上了拟议块头、已经有完整历史」一件事：

1. **看见 `FinalizeBlockRequest.proposer_address` 是造了这份提案的验证者地址 / 看见填了 proposer_address 不是已经正在造这份提案，也不是已经知道本头哈希。**  
   官方写：`proposer_address` 是造了这份提案的验证者地址。看见填了 proposer_address，不是已经 `PrepareProposalRequest.proposer_address` 是正在造这份提案的验证者地址那种已经正在造。看见造了，不是已经 `ProcessProposalRequest.proposer_address` 是造了这份提案的验证者地址那种已经知道本头哈希。看见能指造了的人，不是已经交差。
2. **看见 `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 time 不是已经对上了拟议块头，也不是已经是 PrepareProposalRequest.time。**  
   官方写：`time` 是已决块的时间戳。Usage 也写：height 和 time 值对上拟议块头。看见填了 time，不是已经 `PrepareProposalRequest.time` 是将要提议那块的时间戳那种已经对上了拟议块头。看见有已决块时间戳，不是已经 Finalize 的 height / time 对上拟议块头那种已经验过块头。看见能指时间戳，不是已经交差。
3. **看见 `FinalizeBlockRequest.syncing_to_height` 同步或重放时是目标高、否则等于本高 / 看见填了 syncing_to_height 不是已经有完整历史，也不是已经是快照重放。**  
   官方写：节点在同步或重放块时，`syncing_to_height` 等于目标高度。否则 `syncing_to_height` 等于本高。看见填了目标高，不是已经有从创世的完整历史。看见在同步或重放，不是已经是快照重放。看见能指同步状态，不是已经切进共识。

怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height 是规范里的做法，本页不抄。ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址就已经正在造这份提案是不变量 427，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址 ≠ 已经正在造这份提案：** 官方把 Finalize 请求表上这份造了这份提案的验证者地址和 Prepare 请求表上那份正在造这份提案的验证者地址分开。
- **FinalizeBlockRequest.time 是已决块的时间戳 ≠ 已经对上了拟议块头：** 官方把 Finalize 请求表上这份已决块时间戳和 Prepare 请求表上那份将要提议的时间戳分开；Usage 里的「对上拟议块头」是约束，不是已经验过块头。
- **FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高 ≠ 已经有完整历史：** 官方把 Finalize 请求表上这份同步高度标记和切进共识、快照装回分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址 | 不是已经正在造这份提案 | 不是 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址就已经正在造这份提案（427） |
| FinalizeBlockRequest.time 是已决块的时间戳 | 不是已经对上了拟议块头 | 不是 PrepareProposalRequest.time 是将要提议那块的时间戳就已经对上了拟议块头（426） |
| FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高 | 不是已经有完整历史 | 不是 syncing_to_height 同步或重放时是目标高、否则等于本高就已经有完整历史（382） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 请求末栏就已经正在造这份提案、已经对上了拟议块头、已经有完整历史」，必须分开 FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址是不是已经正在造这份提案、FinalizeBlockRequest.time 是已决块的时间戳是不是已经对上了拟议块头、FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高是不是已经有完整历史。可以跳过「看见填了 Finalize 请求末栏就已经正在造这份提案」。不要另写怎样写 Finalize 请求末栏。

## 本页不抄

- 怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height。
- ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址就已经正在造这份提案。那是不变量 427。
- PrepareProposalRequest.time 是将要提议那块的时间戳就已经对上了拟议块头。那是不变量 426。
- syncing_to_height 同步或重放时是目标高、否则等于本高就已经有完整历史。那是不变量 382。
