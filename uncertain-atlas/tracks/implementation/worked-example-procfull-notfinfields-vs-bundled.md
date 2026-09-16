# 例：看见含提案块上执行所需的全部信息 / 看见 Contains all information on the proposed block is not already FinalizeBlockRequest newly decided block fields / 看见填了信息 is not only txs field is enough 不是已经 ProcessProposal 含执行所需全部信息 bundled interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经只有 txs 字段就够 interchangeable

**层次**：实现 / ProcessProposal Contains all information not Finalize newly decided fields 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Contains all information not Finalize newly decided fields 不是 ProcessProposal 含执行所需全部信息 bundled interchangeable / 不是已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 不是已经只有 txs 字段就够 interchangeable」，不是 ProcessProposal 含执行所需全部信息 bundled（453），也不是 FinalizeBlock 含刚决定那块字段 bundled（461 / 474），也不是 Finalize 执行余量 bundled（408）。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 官方三件事

规范把 ProcessProposal 含提案块上执行所需的全部信息、FinalizeBlockRequest 刚决定那块的字段、只有 txs 字段就够 fully execute 分开写成三件独立的实现事，不是「看见 Process 含全部信息就已经是 Finalize 字段 interchangeable、已经 decided_last_commit interchangeable、已经只有 txs 就够 interchangeable」一件事：

1. **看见含提案块上执行所需的全部信息 / 看见 Contains all information on the proposed block is not already FinalizeBlockRequest newly decided block fields / 看见拟议块上执行所需不是已经是 FinalizeBlockRequest 刚决定那块的字段 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 decided_last_commit interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（461 / 474 余量） interchangeable / 已经 newly decided block 字段 interchangeable / 已经跑过 Process interchangeable，也不是已经 FinalizeBlock 含刚决定那块字段 bundled（474 余量） interchangeable / 已经 proposed block 字段 interchangeable / 已经 ProcessProposal Contains all information interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（547 余量） interchangeable / 已经 Finalize 跑过 interchangeable / 已经执行那些交易 interchangeable，也不是已经 ProcessProposal Request 八栏齐 not only Prepare txs bundled（548 余量） interchangeable / 已经 only txs enough interchangeable。**  
   官方写：Contains all information on the proposed block needed to fully execute it。看见拟议块上执行所需，不是已经是 `FinalizeBlockRequest.decided_last_commit` 从刚决定那块拿到那种已经交差——453 bundled 常被写成「看见 Process 含全部信息就已经是 Finalize 刚决定那块的字段」，本页钉 Contains all information not Finalize newly decided fields 单句。看见全部信息，不是已经 FinalizeBlock Contains newly decided block fields（461 / 474 余量） interchangeable——461 钉 newly decided block 字段，本页钉 Process Usage 拟议块执行所需边界。看见能 fully execute，不是已经 CometBFT fill up all fields even if Prepare/Process passed（363 余量） interchangeable——363 钉 Finalize 又填一遍，本页钉 proposed vs decided 单句。
2. **看见 Contains all information is not proposed_last_commit vs decided_last_commit interchangeable / 看见拟议块执行所需不是已经 FinalizeBlockRequest.hash 是已决块的哈希 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经 proposed_last_commit 和 decided_last_commit 就可以混用 interchangeable / 已经 ProcessProposalRequest.hash 是拟议块的哈希 interchangeable，也不是已经 Process 请求余栏 bundled（420 余量） interchangeable / 已经 proposed_last_commit interchangeable / 已经 ProcessProposalRequest.hash 是拟议块的哈希 Request栏（419 余量） interchangeable，也不是已经 Finalize 请求余栏 bundled（428 余量） interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable / 已经 ProcessProposalRequest.hash interchangeable，也不是已经 Prepare 请求余栏 bundled（424 余量） interchangeable / 已经 local_last_commit interchangeable / 已经 proposed_last_commit interchangeable，也不是已经 FinalizeBlock 含刚决定那块字段 bundled（461 余量） interchangeable / 已经 newly decided block 字段 interchangeable / 已经 proposed block interchangeable。**  
   官方把 Process 拟议块上执行所需信息和 Finalize 已决块 hash / decided_last_commit 分开——453 bundled 常与 420 / 428 混成「proposed_last_commit 和 decided_last_commit 就可以混用」，本页钉 Contains all information not proposed/decided interchangeable 单句。看见拟议块执行所需，不是已经 Process 请求余栏 proposed_last_commit（420 余量） interchangeable——420 钉 proposed_last_commit 单栏，本页钉 proposed vs decided 边界。看见全部信息，不是已经 FinalizeBlockRequest.hash 是已决块的哈希（428 余量） interchangeable——428 钉 Finalize 请求 hash 单栏，本页钉 Process Usage 拟议块执行所需单句。
3. **看见 Contains all information is not only ProcessProposalRequest.txs is enough / 看见含执行所需全部信息不是已经只有 txs 字段就够 fully execute 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经只有 txs 字段就够 interchangeable / 已经 ProcessProposalRequest.txs 是拟议块的交易列表 interchangeable，也不是已经 ProcessProposal Request 八栏齐 not only Prepare txs bundled（548 余量） interchangeable / 已经 only txs enough interchangeable / 已经 Request 八栏齐 interchangeable，也不是已经 ProcessProposalRequest.txs 是拟议块的交易列表 Request栏（419 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 only txs interchangeable，也不是已经 Finalize 执行余量 bundled（408 余量） interchangeable / 已经 Process 含提案块上执行所需的全部信息 interchangeable / 已经 Finalize 执行 bundled interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（547 余量） interchangeable / 已经 Contains all information interchangeable / 已经 only txs enough interchangeable。**  
   官方把 Contains all information needed to fully execute 和只有 txs 字段就够分开——453 bundled 第三件事常与 548 混成「看见含全部信息 = 只有 txs 就够」，本页钉 Contains all information not only txs enough 单句。看见拟议块上执行所需，不是已经 Request 八栏齐 not only txs enough（548 余量） interchangeable——548 钉八栏齐 not only txs，本页钉 Usage 拟议块执行所需 vs Finalize 字段边界。看见全部信息，不是已经 Finalize 执行余量 bundled（408 余量） interchangeable——408 钉 Finalize 执行 bundled 三事之一，本页钉 Process Contains all information not Finalize fields 单句。

怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐 是规范里的做法，本页不抄。ProcessProposal 含执行所需全部信息 bundled（453）、FinalizeBlock 含刚决定那块字段 bundled（461 / 474）、Finalize 执行余量 bundled（408）是另外那套，本页不抄。

## 官方为什么这样拆

- **Contains all information not Finalize newly decided fields ≠ ProcessProposal 含执行所需全部信息 bundled interchangeable：** 官方把拟议块上执行所需信息和 FinalizeBlockRequest 刚决定那块的字段分开。
- **Contains all information not proposed/decided interchangeable ≠ proposed_last_commit vs decided_last_commit interchangeable：** 官方把 Process 拟议块执行所需和 Finalize 已决块 hash / decided_last_commit 分开。
- **Contains all information not only txs enough ≠ Request 八栏齐 only txs interchangeable：** 官方把 Usage 拟议块执行所需和只有 txs 字段就够 fully execute 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Contains all information | 不是 Finalize newly decided fields | 不是 FinalizeBlock Contains newly decided（461） |
| 拟议块执行所需 | 不是 proposed/decided interchangeable | 不是 Process req proposed_last_commit（420） |
| Contains all information | 不是 only txs enough | 不是 Request 八栏齐 only txs（548） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Contains all information not Finalize newly decided fields 正式三事，必须分开 Contains all information 是不是 Finalize newly decided fields interchangeable / 461 newly decided interchangeable、Contains all information 是不是 proposed/decided interchangeable / 428 Finalize hash interchangeable、Contains all information 是不是 only txs enough interchangeable / 548 Request 八栏齐 interchangeable。可以跳过「看见 Process 含全部信息就已经是 Finalize 字段 interchangeable」。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 本页不抄

- 怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐。
- Contains all information not already executed。那是不变量 547（453 item 1 余量）。
- Request 八栏齐 not only Prepare txs。那是不变量 548（453 item 2 余量）。
- Finalize 执行余量 bundled 三事。那是不变量 408。
