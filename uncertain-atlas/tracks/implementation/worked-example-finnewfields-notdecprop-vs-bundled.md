# 例：看见 CometBFT 会把 FinalizeBlockRequest 全部字段填齐、即使 Prepare/Process 已经传过 / 看见又填一遍 is not already decided_last_commit and proposed_last_commit interchangeable / 看见 all fields is not already Prepare/Process 传过就意味着 newly decided and proposed interchangeable 不是已经 FinalizeBlock 含刚决定那块字段 bundled interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable / 已经 fill all fields interchangeable

**层次**：实现 / FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「fill all fields not decided/proposed interchangeable 不是 FinalizeBlock 含刚决定那块字段 bundled interchangeable / 不是已经 decided 和 proposed 就可以混用 interchangeable / 不是已经 Prepare/Process 传过 interchangeable」，不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473），也不是 FinalizeBlock Contains newly decided block fields not already settled（555），也不是 FinalizeBlock newly decided block fields not ProcessProposal contains all information（556）。不要另写怎样写 FinalizeBlockRequest 各栏。

## 官方三件事

规范把 FinalizeBlock Usage 里 CometBFT will fill up all fields in FinalizeBlockRequest even if passed via Prepare/Process、decided_last_commit vs proposed_last_commit、Prepare/Process 传过和 newly decided vs proposed 对象分开写成三件独立的实现事，不是「看见又填一遍就已经 decided 和 proposed 就可以混用 interchangeable、Prepare/Process 传过 interchangeable、已经跑过 Process 就不需要 Finalize interchangeable」一件事：

1. **看见 CometBFT 会把 FinalizeBlockRequest 全部字段填齐、即使 Prepare/Process 已经传过 / 看见又填一遍 is not already decided_last_commit and proposed_last_commit interchangeable / 看见 all fields is not already FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable / 已经 fill all fields interchangeable，也不是已经 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 Request栏（422 余量） interchangeable / 已经 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 interchangeable / 已经 decided vs proposed 单栏 interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473 余量） interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable / 已经 all fields 又填一遍 interchangeable，也不是已经 Process 请求余栏 bundled（420 余量） interchangeable / 已经 proposed_last_commit interchangeable / 已经 ProcessProposalRequest.hash 是拟议块的哈希 interchangeable，也不是已经 Finalize 请求余栏 bundled（428 余量） interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable / 已经 ProcessProposalRequest.hash interchangeable，也不是已经 FinalizeBlock newly decided block fields not proposed/decided bundled（556 余量） interchangeable / 已经 proposed 对象 interchangeable / 已经 decided 对象 interchangeable。**  
   官方写：Currently, CometBFT will fill up all fields in `FinalizeBlockRequest`, even if they were already passed on via `PrepareProposalRequest` or `ProcessProposalRequest`。看见又填一遍，不是已经 `FinalizeBlockRequest.decided_last_commit` 和 `ProcessProposalRequest.proposed_last_commit` 就可以混用（422）——461 bundled 第三件事常被写成「又填一遍 = decided 和 proposed 就可以混用」，本页钉 fill all fields not decided/proposed interchangeable 单句。看见 all fields，不是已经 Finalize 请求栏 decided vs proposed（422 余量） interchangeable——422 钉 decided_last_commit / height / txs 单栏，本页钉 fill all fields 边界。看见 fill up all fields，不是已经 FinalizeBlock fill all fields even if passed（473 余量） interchangeable——473 钉 fill all fields 专用切片，本页钉 461 bundled item 3 单句。
2. **看见 fill all fields is not Prepare/Process passed means newly decided and proposed interchangeable / 看见即使 Prepare / Process 已经传过 is not already newly decided block 的字段和 proposed block 字段 interchangeable 不是已经 FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经 Prepare/Process 同一套字段 interchangeable / 已经 newly decided and proposed interchangeable，也不是已经 Prepare 请求字段同一套 bundled（359 余量） interchangeable / 已经字段名对得上 interchangeable / 已经 local_last_commit interchangeable，也不是已经 FinalizeBlock newly decided block fields not ProcessProposal contains all information bundled（556 余量） interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable / 已经 proposed block 字段 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经 ran Process interchangeable / 已经四门已经结算 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（473 余量） interchangeable / 已经 even if passed interchangeable / 已经字段名对得上就代表已经跑过 Process interchangeable。**  
   官方把 even if passed 和 newly decided block 的字段 vs proposed block 字段分开——461 bundled 常与 359 混成「Prepare/Process 传过 = newly decided 和 proposed interchangeable」，本页钉 fill all fields not newly decided/proposed interchangeable 单句。看见已经传过，不是已经 Prepare 请求字段同一套（359 余量） interchangeable——359 钉字段名对得上，本页钉 even if passed 边界。看见又填一遍，不是已经 FinalizeBlock newly decided block fields not ProcessProposal contains all information（556 余量） interchangeable——556 钉 newly decided vs Process contains all information，本页钉 fill all fields 单句。
3. **看见 fill all fields is not already ran Process means don't need Finalize / 看见引擎填齐 is not already Prepare / Process 传过就不需要 Finalize / 已经交差 不是已经 FinalizeBlock 含刚决定那块字段 bundled（461） interchangeable / 已经跑过 Process interchangeable / 已经 Prepare/Process 传过 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经字段再填一遍 interchangeable / 已经套用先前 candidate interchangeable，也不是已经 FinalizeBlock fill all fields even if Prepare/Process passed bundled（473 余量） interchangeable / 已经 Prepare/Process 给过就不用再 Finalize interchangeable / 已经交差 interchangeable，也不是已经 FinalizeBlock 确定执行 txs bundled（460 余量） interchangeable / 已经不用再在 Process 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经 ran Process interchangeable / 已经 Process ACCEPT switched working state interchangeable。**  
   官方把 fill up all fields 和 Process 调用之前就已经跑过 Process / 已经交差分开——461 bundled 常与 360 混成「又填一遍 = 已经跑过 Process 就不需要 Finalize」，本页钉 fill all fields not ran Process means don't need Finalize 单句。看见 all fields 齐，不是已经 Finalize 时的 Process 保证（360 余量） interchangeable——360 钉至少一名非拜占庭验证者跑过 Process / 字段再填一遍，本页钉 fill all fields 边界。看见引擎填齐，不是已经 FinalizeBlock fill all fields even if passed（473 余量） interchangeable——473 钉 will fill up / even if passed / all fields 三事，本页钉 461 item 3 not need Finalize 单句。

怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐 是规范里的做法，本页不抄。FinalizeBlock fill all fields even if Prepare/Process passed bundled（473）、FinalizeBlock 含刚决定那块字段 bundled（461）、Finalize 请求栏 decided vs proposed（422）是另外那套，本页不抄。

## 官方为什么这样拆

- **fill all fields not decided/proposed interchangeable ≠ FinalizeBlock 含刚决定那块字段 bundled interchangeable：** 官方把 all fields 填齐和 decided_last_commit vs proposed_last_commit 语义分开。
- **fill all fields not newly decided/proposed interchangeable ≠ Prepare 请求字段同一套 interchangeable：** 官方把 even if passed 和 newly decided vs proposed 对象分开。
- **fill all fields not ran Process means don't need Finalize ≠ Finalize Process guarantee interchangeable：** 官方把 fill up all fields 和 Process 跑过 / 已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| fill all fields | 不是 decided/proposed interchangeable | 不是 Finalize 请求栏 decided vs proposed（422） |
| even if Prepare/Process passed | 不是 newly decided/proposed interchangeable | 不是 Prepare 请求字段同一套（359） |
| fill all fields | 不是 ran Process means don't need Finalize | 不是 Finalize Process guarantee（360） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事，必须分开 fill all fields 是不是 decided/proposed interchangeable / 422 decided vs proposed interchangeable、fill all fields 是不是 newly decided/proposed interchangeable / 359 Prepare 同一套字段 interchangeable、fill all fields 是不是 ran Process means don't need Finalize interchangeable / 360 Process guarantee interchangeable。可以跳过「看见又填一遍就已经 decided 和 proposed 就可以混用 interchangeable」。不要另写怎样写 FinalizeBlockRequest 各栏。

## 本页不抄

- 怎样写 FinalizeBlockRequest 各栏、怎样和 Process 请求栏对齐。
- Contains newly decided block fields not already settled。那是不变量 555（461 item 1 余量）。
- newly decided block fields not ProcessProposal contains all information。那是不变量 556（461 item 2 余量）。
- fill all fields even if Prepare/Process passed bundled 三事。那是不变量 473。
