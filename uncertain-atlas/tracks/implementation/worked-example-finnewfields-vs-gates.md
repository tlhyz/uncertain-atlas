# 例：看见 FinalizeBlock Contains the fields of the newly decided block 不是已经是四门已经结算；看见 newly decided block 的字段不是已经是 ProcessProposal 含提案块上执行所需的全部信息；看见 CometBFT 会把 FinalizeBlockRequest 全部字段填齐、即使 Prepare/Process 已经传过不是已经 decided_last_commit 和 proposed_last_commit 就可以混用

**层次**：实现 / FinalizeBlock 含刚决定那块字段正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Contains the fields of the newly decided block 不是已经是四门已经结算 / newly decided block 的字段不是已经是 ProcessProposal 含执行所需全部信息 / 全部字段填齐即使 Prepare/Process 已经传过不是已经 decided 和 proposed 就可以混用」，不是 Finalize 字段余量 bundled 三事，也不是 Finalize 请求栏 decided vs proposed 单栏定义，也不是 ProcessProposal 含执行所需全部信息那套。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock 含刚决定那块的字段、newly decided block 的字段对象、CometBFT 会把全部字段填齐即使 Prepare/Process 已经传过写成三件独立的实现事，不是「看见填了 Finalize 含刚决定那块的字段就已经是四门已经结算、已经是 Process 含全部信息、decided 和 proposed 字段 interchangeable」一件事：

1. **看见 FinalizeBlock Contains the fields of the newly decided block / 看见含刚决定那块的字段 不是已经是四门已经结算，也不是已经跑过 Process。**  
   官方写：Contains the fields of the newly decided block。看见有刚决定那块的字段，不是已经 Finalize 等价于 ABCI 1.0 那三步（363）那种四门已经结算。看见能填字段，不是已经 Prepare / Process 同一套字段就已经跑过 Process。看见 newly decided block，不是已经 Process 回了 Accept 就已经换工作状态。
2. **看见 newly decided block 的字段 / 看见有刚决定那块 不是已经是 ProcessProposal Contains all information on the proposed block needed to fully execute it，也不是已经是 ProcessProposalRequest 拟议块字段 interchangeable。**  
   官方把 newly decided block 的字段和 proposed block 上执行所需全部信息分开写。看见刚决定那块的字段，不是已经 ProcessProposal 含提案块上执行所需的全部信息（453）就已经是同一句 interchangeable。看见 decided block，不是已经 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息那种 proposed 对象 interchangeable。看见有字段，不是已经只有 `PrepareProposalResponse.txs` 那种 raw proposal 就够。
3. **看见 CometBFT 会把 FinalizeBlockRequest 全部字段填齐、即使 Prepare/Process 已经传过 / 看见又填一遍 不是已经 decided_last_commit 和 proposed_last_commit 就可以混用，也不是已经 Prepare/Process 同一套字段就已经是刚决定那块的字段。**  
   官方写：Currently, CometBFT will fill up all fields in `FinalizeBlockRequest`, even if they were already passed on to the Application via `PrepareProposalRequest` or `ProcessProposalRequest`。看见又填一遍，不是已经 `FinalizeBlockRequest.decided_last_commit` 和 `ProcessProposalRequest.proposed_last_commit` 就可以混用（422）。看见全部字段齐，不是已经 Prepare/Process 传过就意味着 newly decided block 的字段和 proposed block 字段 interchangeable。看见引擎填齐，不是已经跑过 Process 就不需要 Finalize 那种已经交差。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐是规范里的做法，本页不抄。Finalize 字段余量 bundled（407）是含刚决定那块的字段 + 实现必须确定 + Info 回应用状态信息那套另一切片，Finalize 请求栏 decided vs proposed（422）是 decided_last_commit / height / txs 单栏定义，ProcessProposal 含执行所需全部信息（453）是 Contains all information needed to fully execute / 八栏齐 / 不是已经是 Finalize 字段那套另一切片，本页不抄。

## 官方为什么这样拆

- **Contains the fields of the newly decided block ≠ 已经是四门已经结算 / 已经跑过 Process：** 官方把刚决定那块的字段和收成一门的三步、和 Process 跑过分开。
- **newly decided block 的字段 ≠ 已经是 ProcessProposal 含执行所需全部信息 / 拟议块字段 interchangeable：** 官方把已决块字段和拟议块上执行所需信息分开。
- **全部字段填齐即使 Prepare/Process 已经传过 ≠ decided 和 proposed 就可以混用：** 官方把引擎再填一遍和 decided_last_commit vs proposed_last_commit 语义分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Contains the fields of the newly decided block | 不是已经是四门已经结算 | 不是 Finalize 字段余量 bundled 三事（407） |
| newly decided block 的字段 | 不是已经是 ProcessProposal 含执行所需全部信息 | 不是 ProcessProposal 含执行所需全部信息正式三事（453） |
| 全部字段填齐即使 Prepare/Process 已经传过 | 不是已经 decided 和 proposed 就可以混用 | 不是 Finalize 请求栏 decided vs proposed（422） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 含刚决定那块的字段就已经是四门已经结算、已经是 Process 含全部信息、decided 和 proposed 字段 interchangeable」，必须分开 Contains the fields of the newly decided block 是不是已经是四门已经结算、newly decided block 的字段是不是已经是 ProcessProposal 含执行所需全部信息、全部字段填齐即使 Prepare/Process 已经传过是不是已经 decided 和 proposed 就可以混用。可以跳过「看见填了 Finalize 字段就已经是四门已经结算」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐。
- Finalize 字段余量 bundled 三事。那是不变量 407。
- Finalize 请求栏 decided vs proposed 单栏定义。那是不变量 422。
- ProcessProposal 含执行所需全部信息正式三事。那是不变量 453。
- Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算。那是不变量 363。
