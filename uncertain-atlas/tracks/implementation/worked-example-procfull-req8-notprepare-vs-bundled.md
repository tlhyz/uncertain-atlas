# 例：看见 `ProcessProposalRequest` 有 `txs` + `proposed_last_commit` + `misbehavior` + `hash` + `height` + `time` + `next_validators_hash` + `proposer_address` / 看见 Request 八栏齐 is not only `PrepareProposalResponse.txs` / raw proposal 不是已经 ProcessProposal 含执行所需全部信息 bundled interchangeable / 已经 Prepare 回包就已经齐 interchangeable / 已经只有 raw proposal interchangeable

**层次**：实现 / ProcessProposal Request 八栏齐 not only Prepare txs 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Request 八栏齐 not only Prepare txs 不是 ProcessProposal 含执行所需全部信息 bundled interchangeable / 不是已经 Prepare 回包就已经齐 interchangeable / 不是已经只有 raw proposal interchangeable」，不是 ProcessProposal 含执行所需全部信息 bundled（453），也不是 Prepare raw proposal bundled（503），也不是 Process 请求栏单栏定义（419–420 / 427）。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 官方三件事

规范把 ProcessProposalRequest 八栏齐和只有 PrepareProposalResponse.txs、只有 raw proposal、只有 ProcessProposalRequest.txs 单栏分开写成三件独立的实现事，不是「看见 Process 八栏齐就已经只有 Prepare 回包 interchangeable、已经只有 raw proposal interchangeable、已经只有 txs 就够 interchangeable」一件事：

1. **看见 `ProcessProposalRequest` 有 `txs` + `proposed_last_commit` + `misbehavior` + `hash` + `height` + `time` + `next_validators_hash` + `proposer_address` / 看见 Request 八栏齐 is not only `PrepareProposalResponse.txs` / 看见八栏齐不是已经只有 Prepare 回包 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经只有 PrepareProposalResponse.txs interchangeable / 已经 Prepare 回包就已经齐 interchangeable，也不是已经 PrepareProposal When return / use-as-proposal bundled（506 余量） interchangeable / 已经 includes tx list in return interchangeable / 已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经不用再 Process interchangeable，也不是已经 PrepareProposalResponse.txs 是可能改过的列表 Response栏（427） interchangeable / 已经保证是这一次 Prepare interchangeable / 已经 Prepare 改列表 interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 第三件事 / 548 余量） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable。**  
   官方 Request 表写八栏：`txs`、`proposed_last_commit`、`misbehavior`、`hash`、`height`、`time`、`next_validators_hash`、`proposer_address`。`PrepareProposalResponse` 只有 `txs`。看见八栏齐，不是已经 Prepare 回包就已经齐——453 bundled 常被写成「看见 Process 含全部信息就已经只有 PrepareProposalResponse.txs」，本页钉 Request 八栏齐 not only Prepare txs 单句。看见有八栏，不是已经 Prepare When return / use-as-proposal（506 余量） interchangeable——506 钉 includes tx list in return，本页钉 Process Request 八栏边界。看见 Request 八栏齐，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 ProcessProposalRequest.txs equals PrepareProposalResponse.txs，本页钉八栏齐 not only Prepare resp 单句。
2. **看见 Request 八栏齐 is not only raw proposal / preliminary txs / 看见八栏齐不是已经只有 raw proposal 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经只有 raw proposal interchangeable / 已经 PrepareProposalRequest.txs 是初步交易列表 interchangeable，也不是已经 PrepareProposal Usage raw proposal bundled（503 余量） interchangeable / 已经 can modify this set interchangeable / 已经只有 raw proposal interchangeable，也不是已经 `PrepareProposalRequest` contains preliminary txs called raw proposal Request栏（423） interchangeable / 已经跑过 Process interchangeable / 已经只有 raw proposal interchangeable，也不是已经 ProcessProposalRequest.txs 是拟议块的交易列表 Request栏（419） interchangeable / 已经执行那些交易 interchangeable / 已经只有 txs 就够 interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经 Contains all information interchangeable / 已经 only txs enough interchangeable。**  
   官方把 Process 请求八栏和 Prepare 请求里的 raw proposal 分开——453 bundled 常与 503 混成「八栏齐 = 只有 raw proposal = 只有 txs」，本页钉 Request 八栏齐 not only raw proposal 单句。看见八栏齐，不是已经 Prepare raw proposal bundled（503 余量） interchangeable——503 钉 preliminary txs / can modify this set，本页钉 Process Request 八栏边界。看见有 `txs`，不是已经 ProcessProposalRequest.txs 是拟议块的交易列表（419） interchangeable——419 钉单栏 txs 不是已经执行那些交易，本页钉八栏齐 not only txs 单句。
3. **看见 Request 八栏齐 is not only ProcessProposalRequest.txs is enough / 看见八栏齐不是已经只有 txs 字段就够 fully execute 不是已经 ProcessProposal 含执行所需全部信息 bundled（453） interchangeable / 已经只有 txs 就够 interchangeable / 已经 ProcessProposalRequest.txs 是拟议块的交易列表 interchangeable，也不是已经 ProcessProposalRequest.txs 是拟议块的交易列表 Request栏（419） interchangeable / 已经执行那些交易 interchangeable / 已经只有 txs interchangeable，也不是已经 Process 请求余栏 / 请求末栏 bundled（420 / 427 余量） interchangeable / 已经 proposed_last_commit interchangeable / 已经 hash height time interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经 Contains all information interchangeable / 已经 only txs enough interchangeable，也不是已经 ProcessProposal 含执行所需全部信息 bundled（453 第三件事 / 548 余量） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 decided_last_commit interchangeable。**  
   官方把 Process 请求八栏和「只有 txs 字段就够 fully execute」分开——453 bundled 第三件事常与 419 混成「看见 txs 栏就已经 only txs enough」，本页钉 Request 八栏齐 not only txs enough 单句。看见八栏齐，不是已经 Process 请求栏 bundled（419） interchangeable——419 钉单栏定义，本页钉八栏齐边界。看见有 `txs`，不是已经 Process 请求余栏 / 末栏（420 / 427 余量） interchangeable——420 / 427 钉 proposed_last_commit / hash / height / time 单栏，本页钉八栏齐 not only txs 单句。

怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐 是规范里的做法，本页不抄。ProcessProposal 含执行所需全部信息 bundled（453）、Prepare raw proposal bundled（503）、Process 请求栏单栏定义（419–420 / 427）是另外那套，本页不抄。

## 官方为什么这样拆

- **Request 八栏齐 not only Prepare txs ≠ ProcessProposal 含执行所需全部信息 bundled interchangeable：** 官方把 Process 请求八栏和 PrepareProposalResponse 只有 txs 分开。
- **Request 八栏齐 not only raw proposal ≠ Prepare raw proposal interchangeable：** 官方把 Process 八栏齐和 Prepare 请求 preliminary txs 分开。
- **Request 八栏齐 not only txs enough ≠ Process req txs column interchangeable：** 官方把八栏齐和只有 txs 字段就够 fully execute 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Request 八栏齐 | 不是 only PrepareProposalResponse.txs | 不是 Prepare return bundled（506） |
| Request 八栏齐 | 不是 only raw proposal | 不是 Prepare raw proposal bundled（503） |
| Request 八栏齐 | 不是 only txs enough | 不是 Process req txs 单栏（419） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Request 八栏齐 not only Prepare txs 正式三事，必须分开 Request 八栏齐 是不是 only PrepareProposalResponse.txs interchangeable / Prepare 回包就已经齐 interchangeable、Request 八栏齐 是不是 only raw proposal interchangeable / 503 raw proposal interchangeable、Request 八栏齐 是不是 only txs enough interchangeable / 419 Process req txs interchangeable。可以跳过「看见 Process 八栏齐就已经只有 Prepare 回包 interchangeable」。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 本页不抄

- 怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐。
- Contains all information not already executed。那是不变量 546（453 item 1 余量）。
- 含执行所需全部信息 ≠ 已经是 FinalizeBlockRequest 刚决定那块的字段。那是不变量 548（453 item 3 余量）。
- Process 请求栏 / 请求余栏 / 请求末栏单栏定义。那是不变量 419–420 / 427。
