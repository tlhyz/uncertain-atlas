# 例：看见 newly decided block 的字段 / 看见有刚决定那块 is not already ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见 decided block is not already ProcessProposalRequest 拟议块字段 interchangeable 不是已经 FinalizeBlock 含刚决定那块字段 bundled interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable / 已经 proposed block 字段 interchangeable

**层次**：实现 / FinalizeBlock newly decided block fields not ProcessProposal contains all information 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「newly decided block fields not ProcessProposal contains all information 不是 FinalizeBlock 含刚决定那块字段 bundled interchangeable / 不是已经 ProcessProposal 含执行所需全部信息 interchangeable / 不是已经 proposed block 字段 interchangeable」，不是 FinalizeBlock 含刚决定那块字段 bundled（461），也不是 ProcessProposal Contains all information not Finalize newly decided fields（548），也不是 FinalizeBlock Contains newly decided block fields not already settled（555）。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 里 newly decided block 的字段对象、ProcessProposal Contains all information on the proposed block needed to fully execute it、ProcessProposalRequest 拟议块字段分开写成三件独立的实现事，不是「看见 newly decided block 的字段就已经 ProcessProposal 含执行所需全部信息 interchangeable、proposed_last_commit interchangeable、只有 raw proposal 就够 interchangeable」一件事：

1. **看见 newly decided block 的字段 / 看见有刚决定那块 is not already ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见 decided block is not already FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable / 已经 proposed block 字段 interchangeable，也不是已经 ProcessProposal Contains all information not Finalize newly decided fields bundled（548 余量） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 decided_last_commit interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经四门已经结算 interchangeable / 已经跑过 Process interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（474 余量） interchangeable / 已经 newly decided vs proposed 对象 interchangeable / 已经 height/time match header 就代表对象已经分清 interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 余量） interchangeable / 已经八栏齐 interchangeable / 已经 only txs enough interchangeable，也不是已经 FinalizeBlock 含刚决定那块字段 bundled（461 第三件事 / 557 余量） interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable / 已经 fill all fields interchangeable。**  
   官方把 newly decided block 的字段和 proposed block 上执行所需全部信息分开写。看见刚决定那块的字段，不是已经 ProcessProposal 含提案块上执行所需的全部信息（453）就已经是同一句 interchangeable——461 bundled 第二件事常被写成「看见 newly decided 字段就已经 Process 含全部信息」，本页钉 newly decided block fields not ProcessProposal contains all information 单句。看见 decided block，不是已经 ProcessProposal Contains all information not Finalize newly decided fields（548 余量） interchangeable——548 钉 Process Usage 拟议块执行所需 vs Finalize 字段，本页钉 Finalize newly decided 对象边界。看见有字段，不是已经 FinalizeBlock Contains newly decided block fields not already settled（555 余量） interchangeable——555 钉 Contains newly decided not settled，本页钉 newly decided vs proposed 单句。
2. **看见 newly decided block fields is not proposed_last_commit vs decided_last_commit interchangeable / 看见 decided block is not already ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 interchangeable 不是已经 FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 proposed_last_commit 和 decided_last_commit 就可以混用 interchangeable / 已经 proposed 对象 interchangeable，也不是已经 Process 请求余栏 bundled（420 余量） interchangeable / 已经 ProcessProposalRequest.proposed_last_commit interchangeable / 已经 ProcessProposalRequest.hash 是拟议块的哈希 Request栏（419 余量） interchangeable，也不是已经 Finalize 请求余栏 bundled（428 余量） interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable / 已经 ProcessProposalRequest.hash interchangeable，也不是已经 Prepare 请求余栏 bundled（424 余量） interchangeable / 已经 local_last_commit interchangeable / 已经 proposed_last_commit interchangeable，也不是已经 ProcessProposal Contains all information not proposed/decided bundled（548 余量） interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable / 已经 proposed/decided interchangeable，也不是已经 FinalizeBlock 含刚决定那块字段 bundled（461 第三件事 / 557 余量） interchangeable / 已经 fill all fields interchangeable / 已经 Prepare/Process 传过 interchangeable。**  
   官方把 newly decided block 的字段和 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息分开——461 bundled 常与 422 混成「decided_last_commit 和 proposed_last_commit 就可以混用」，本页钉 newly decided block fields not proposed/decided interchangeable 单句。看见 decided block，不是已经 Process 请求余栏 proposed_last_commit（420 余量） interchangeable——420 钉 proposed_last_commit 单栏，本页钉 newly decided vs proposed 边界。看见有字段，不是已经 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息那种 decided 对象（422 余量） interchangeable——422 钉 decided_last_commit 单栏，本页钉 newly decided fields not proposed 对象 单句。
3. **看见 newly decided block fields is not only PrepareProposalResponse.txs raw proposal enough / 看见有刚决定那块 is not already only raw proposal / preliminary txs is enough 不是已经 FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 only raw proposal interchangeable / 已经 PrepareProposalResponse.txs interchangeable，也不是已经 ProcessProposal Request 八栏齐 not only Prepare txs bundled（547 余量） interchangeable / 已经 only PrepareProposalResponse.txs interchangeable / 已经 Request 八栏齐 interchangeable，也不是已经 ProcessProposal Contains all information not only txs enough bundled（548 余量） interchangeable / 已经 only txs field is enough interchangeable / 已经 ProcessProposalRequest.txs 是拟议块的交易列表 interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经 Contains all information interchangeable / 已经 only txs enough interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 余量） interchangeable / 已经八栏齐 interchangeable / 已经 only txs enough interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable。**  
   官方把 newly decided block 的字段和只有 `PrepareProposalResponse.txs` 那种 raw proposal 就够分开——461 bundled 常与 547 混成「看见有字段 = 只有 raw proposal 就够」，本页钉 newly decided block fields not only raw proposal enough 单句。看见 decided block，不是已经 ProcessProposal Request 八栏齐 not only Prepare txs（547 余量） interchangeable——547 钉八栏齐 not only Prepare txs，本页钉 newly decided vs raw proposal 边界。看见有字段，不是已经 ProcessProposal Contains all information not only txs enough（548 余量） interchangeable——548 钉 Usage 拟议块执行所需 vs only txs，本页钉 Finalize newly decided 对象 单句。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐 是规范里的做法，本页不抄。FinalizeBlock 含刚决定那块字段 bundled（461）、ProcessProposal Contains all information not Finalize newly decided fields（548）、FinalizeBlock Contains newly decided block fields not already settled（555）是另外那套，本页不抄。

## 官方为什么这样拆

- **newly decided block fields not ProcessProposal contains all information ≠ FinalizeBlock 含刚决定那块字段 bundled interchangeable：** 官方把已决块字段和拟议块上执行所需信息分开。
- **newly decided block fields not proposed/decided interchangeable ≠ proposed_last_commit vs decided_last_commit interchangeable：** 官方把 newly decided 对象和 Process/Finalize 请求栏 proposed vs decided 分开。
- **newly decided block fields not only raw proposal enough ≠ Request 八栏齐 only Prepare txs interchangeable：** 官方把 newly decided block 字段和只有 raw proposal / txs 就够分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| newly decided block fields | 不是 ProcessProposal contains all information | 不是 ProcessProposal 含执行所需全部信息（453） |
| newly decided block fields | 不是 proposed/decided interchangeable | 不是 Finalize 请求栏 decided vs proposed（422） |
| newly decided block fields | 不是 only raw proposal enough | 不是 Request 八栏齐 only Prepare txs（547） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock newly decided block fields not ProcessProposal contains all information 正式三事，必须分开 newly decided block fields 是不是 ProcessProposal contains all information interchangeable / 453 bundled interchangeable / 548 not Finalize fields interchangeable、newly decided block fields 是不是 proposed/decided interchangeable / 422 decided vs proposed interchangeable、newly decided block fields 是不是 only raw proposal enough interchangeable / 547 Request 八栏齐 interchangeable。可以跳过「看见 newly decided 字段就已经 Process 含全部信息 interchangeable」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐。
- Contains newly decided block fields not already settled。那是不变量 555（461 item 1 余量）。
- fill all fields even if Prepare/Process passed ≠ decided/proposed interchangeable。那是不变量 557（461 item 3 余量）。
- ProcessProposal Contains all information not Finalize newly decided fields。那是不变量 548。
