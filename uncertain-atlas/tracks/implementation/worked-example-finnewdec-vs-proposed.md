# 例：看见 FinalizeBlock Contains the fields of the newly decided block 不是已经是四门已经结算 / 已经跑过 Process；看见 newly decided block 不是 proposed block / 不是 ProcessProposal 含执行所需全部信息；看见 fields of the newly decided block 不是已经 height/time match proposed block header 就代表对象已经分清

**层次**：实现 / FinalizeBlock Contains newly decided block fields 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Contains the fields of the newly decided block 不是已经是四门已经结算 / 已经跑过 Process / newly decided block 不是 proposed block / ProcessProposal 含执行所需全部信息 / fields of the newly decided block 不是已经 height/time match header 就代表对象已经分清」，不是 FinalizeBlock 含刚决定那块字段 bundled 三事，也不是 Finalize 字段余量 bundled 三事，也不是 fill all fields even if Prepare/Process passed 那套。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 第一句 Contains the fields of the newly decided block、newly decided block 对象、fields of the newly decided block 和 proposed / match header 的边界写成三件独立的实现事，不是「看见填了 Finalize 含刚决定那块的字段就已经是四门已经结算、已经是 Process 含全部信息、height/time 对上了就代表对象已经分清」一件事：

1. **看见 FinalizeBlock Contains the fields of the newly decided block / 看见含刚决定那块的字段 不是已经是四门已经结算，也不是已经跑过 Process / 已经交差。**  
   官方 Usage 第一句写：Contains the fields of the newly decided block。看见有刚决定那块的字段，不是已经 Finalize 等价于 ABCI 1.0 那三步（465）或收成一门（363）那种四门已经结算 interchangeable。看见 Contains the fields，不是已经 Prepare / Process 同一套字段就已经跑过 Process。看见 newly decided block，不是已经 Process 回了 Accept 就已经换工作状态（452）就已经是同一句 interchangeable。
2. **看见 newly decided block / 看见刚决定那块 不是 proposed block，也不是已经是 ProcessProposal Contains all information on the proposed block needed to fully execute it / ProcessProposalRequest 拟议块字段 interchangeable。**  
   官方把 newly decided block 和 proposed block 上执行所需全部信息分开写。看见刚决定那块，不是已经 ProcessProposal 含提案块上执行所需的全部信息（453）就已经是同一句 interchangeable。看见 decided block，不是已经 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息那种 proposed 对象 interchangeable（422）。看见 newly decided，不是已经只有 `PrepareProposalResponse.txs` 那种 raw proposal 就够。
3. **看见 fields of the newly decided block / 看见刚决定那块的字段 不是已经 The height and time values match the values from the header of the proposed block 就代表对象已经分清，也不是已经 fill up all fields even if Prepare/Process passed 就代表 newly decided 和 proposed 语义 interchangeable。**  
   官方另写：The height and time values match the values from the header of the proposed block（462 另钉 height/time match header 三事）。看见 match header，不是已经 Contains the fields of the newly decided block 就已经是同一句 interchangeable——本页钉 newly decided block 对象，462 钉 height/time 对上拟议块头。看见有字段，不是已经 `FinalizeBlockRequest.decided_last_commit` 和 `ProcessProposalRequest.proposed_last_commit` 就可以混用（422）。看见 fields of the newly decided block，不是已经 Currently, CometBFT will fill up all fields even if passed via Prepare/Process（473）那种又填一遍 interchangeable——473 另钉 fill all fields even if passed 专用切片。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐是规范里的做法，本页不抄。FinalizeBlock 含刚决定那块字段 bundled（461）是 Contains newly decided / proposed vs decided / fill all fields 那套另一切片，Finalize 字段余量 bundled（407）是含刚决定那块的字段 + 实现必须确定 + Info 那套另一切片，ProcessProposal 含执行所需全部信息（453）是 Contains all information / 八栏齐那套另一切片，FinalizeBlock height/time 对上拟议块头（462）是 match header / Request height/time 栏那套另一切片，fill all fields even if Prepare/Process passed（473）是 will fill up all fields / even if passed / all fields 那套另一切片，Finalize 等价于 ABCI 1.0（465）是 BeginBlock/DeliverTx/EndBlock 收成一门那套另一切片，本页不抄。

## 官方为什么这样拆

- **Contains the fields of the newly decided block ≠ 已经是四门已经结算 / 已经跑过 Process：** 官方把刚决定那块的字段和收成一门的三步、和 Process 跑过分开。
- **newly decided block ≠ proposed block / ProcessProposal 含执行所需全部信息：** 官方把已决块对象和拟议块上执行所需信息分开。
- **fields of the newly decided block ≠ height/time match header 就代表对象已经分清 / fill all fields 就代表 decided 和 proposed interchangeable：** 官方把 newly decided 对象边界和 match header、又填一遍分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Contains the fields of the newly decided block | 不是已经是四门已经结算 | 不是 Finalize 等价于 ABCI 1.0（465） |
| newly decided block | 不是 proposed block | 不是 ProcessProposal 含执行所需全部信息（453） |
| fields of the newly decided block | 不是 height/time match header 就代表对象已经分清 | 不是 fill all fields even if passed（473） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 含刚决定那块的字段就已经是四门已经结算、已经是 Process 含全部信息、height/time 对上了就代表对象已经分清」，必须分开 Contains the fields of the newly decided block 是不是已经是四门已经结算、newly decided block 是不是 proposed block / ProcessProposal 含执行所需全部信息、fields of the newly decided block 是不是已经 height/time match header 就代表对象已经分清。可以跳过「看见填了 Finalize 字段就已经是四门已经结算」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐。
- FinalizeBlock 含刚决定那块字段 bundled 三事。那是不变量 461。
- Finalize 字段余量 bundled 三事。那是不变量 407。
- ProcessProposal 含执行所需全部信息正式三事。那是不变量 453。
- FinalizeBlock height/time 对上拟议块头。那是不变量 462。
- fill all fields even if Prepare/Process passed。那是不变量 473。
- Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算。那是不变量 465。
