# 反模式：把 ProcessProposal Contains all information not Finalize newly decided fields 正式三事卖成 ProcessProposal 含执行所需全部信息 bundled / 已经是 FinalizeBlockRequest 字段 / 已经只有 txs 就够

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal Contains all information not Finalize newly decided fields ≠ bundled](../../tracks/implementation/worked-example-procfull-notfinfields-vs-bundled.md)。

## 卖法

- 「看见含提案块上执行所需的全部信息 / 看见 Contains all information on the proposed block 就已经是 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 decided_last_commit interchangeable / 已经 ProcessProposal 含执行所需全部信息 bundled interchangeable。」
- 「看见 Process 含全部信息 就已经 proposed_last_commit 和 decided_last_commit 可以混用 interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable。」
- 「看见含执行所需全部信息 就已经只有 txs 字段就够 fully execute interchangeable / 已经 ProcessProposalRequest.txs 是拟议块的交易列表 interchangeable。」

## 为什么错

官方把拟议块上执行所需信息和 FinalizeBlockRequest 刚决定那块的字段分开写。Process 拟议块执行所需不是 proposed/decided interchangeable，也不是只有 txs 字段就够 fully execute。把它们卖成 ProcessProposal 含执行所需全部信息 bundled、已经是 Finalize 字段、已经只有 txs 就够，会把 newly decided fields、proposed/decided 混用、only txs enough 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Contains all information not Finalize newly decided fields 正式三事，必须分开 Contains all information not Finalize newly decided fields、Contains all information not proposed/decided interchangeable、Contains all information not only txs enough 三个名字，不要把它们卖成 ProcessProposal 含执行所需全部信息 bundled / 已经是 FinalizeBlockRequest 字段 / 已经只有 txs 就够。

## 和相邻反模式

- [procfull-sold-as-execute](procfull-sold-as-execute.md) 是 453 bundled 三事专用，不是本页 Contains all information not Finalize fields 单句边界。
- [procfull-notexecuted-sold-as-bundled](procfull-notexecuted-sold-as-bundled.md) 是 Contains all information not already executed 单句边界，不是本页 proposed vs decided 边界。
- [procfull-req8-notprepare-sold-as-bundled](procfull-req8-notprepare-sold-as-bundled.md) 是 Request 八栏齐 not only Prepare txs 单句边界，不是本页 only txs enough vs Finalize fields 边界。
- [finreq-sold-as-procreq](finreq-sold-as-procreq.md) 是 Finalize 请求栏 vs Process 请求栏 bundled，不是本页 Usage 拟议块执行所需 vs Finalize newly decided 边界。
