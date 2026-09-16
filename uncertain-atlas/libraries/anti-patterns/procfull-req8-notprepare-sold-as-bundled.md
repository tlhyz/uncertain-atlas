# 反模式：把 ProcessProposal Request 八栏齐 not only Prepare txs 正式三事卖成 ProcessProposal 含执行所需全部信息 bundled / 已经只有 PrepareProposalResponse.txs / 已经只有 raw proposal

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal Request 八栏齐 not only Prepare txs ≠ bundled](../../tracks/implementation/worked-example-procfull-req8-notprepare-vs-bundled.md)。

## 卖法

- 「看见 `ProcessProposalRequest` 八栏齐 / 看见有 txs + proposed_last_commit + misbehavior + hash + height + time + next_validators_hash + proposer_address 就已经只有 `PrepareProposalResponse.txs` interchangeable / 已经 Prepare 回包就已经齐 interchangeable。」
- 「看见 Process 八栏齐 就已经只有 raw proposal interchangeable / 已经 PrepareProposalRequest.txs 是初步交易列表 interchangeable。」
- 「看见 Process 八栏齐 就已经只有 txs 字段就够 fully execute interchangeable / 已经 ProcessProposalRequest.txs 是拟议块的交易列表 interchangeable。」

## 为什么错

官方 Request 表写八栏，而 `PrepareProposalResponse` 只有 `txs`。Process 八栏齐不是只有 raw proposal，也不是只有 txs 单栏就够 fully execute。把它们卖成 ProcessProposal 含执行所需全部信息 bundled、已经只有 PrepareProposalResponse.txs、已经只有 raw proposal，会把 Prepare resp only txs、raw proposal only、txs column enough 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Request 八栏齐 not only Prepare txs 正式三事，必须分开 Request 八栏齐 not only Prepare txs、Request 八栏齐 not only raw proposal、Request 八栏齐 not only txs enough 三个名字，不要把它们卖成 ProcessProposal 含执行所需全部信息 bundled / 已经只有 PrepareProposalResponse.txs / 已经只有 raw proposal。

## 和相邻反模式

- [procfull-sold-as-execute](procfull-sold-as-execute.md) 是 453 bundled 三事专用，不是本页 Request 八栏齐 not only Prepare txs 单句边界。
- [procfull-notexecuted-sold-as-bundled](procfull-notexecuted-sold-as-bundled.md) 是 Contains all information not already executed 单句边界，不是本页 Request 八栏齐边界。
- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 Process 请求栏单栏 bundled，不是本页 Request 八栏齐 vs Prepare 回包只有 txs。
