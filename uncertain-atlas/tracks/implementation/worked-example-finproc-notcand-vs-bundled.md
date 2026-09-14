# 例：看见 has run ProcessProposal on that block / 看见对这块跑过 Process is not already apply candidate / previously executed means no Process guarantee needed / 看见 has run is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经套用 candidate 就不需要 guarantee interchangeable / 已经 previously executed interchangeable

**层次**：实现 / FinalizeBlock When calling ProcessProposal guarantee not apply candidate 正式三事（472 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「has run ProcessProposal on that block not apply candidate / previously executed / not finproc bundled（472） interchangeable / not Process MAY fully execute（452） interchangeable / not VVE proposed block no guarantee（418） interchangeable」，不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472），也不是 When calling not every validator（570 余量），也不是 at least one not proposer（571 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 has run `ProcessProposal` on that block 和「套用 candidate / previously executed 就不需要 guarantee / Process MAY 整块执行已经交差 / VVE 拟议块无保证 interchangeable」分开写成三件独立的实现事，不是「看见对这块跑过 Process 就已经套用 candidate interchangeable、已经 Process MAY execute interchangeable、已经拟议块无保证 interchangeable」一件事：

1. **看见 has run `ProcessProposal` on that block / 看见对这块跑过 Process is not already apply candidate / previously executed via PrepareProposal or ProcessProposal means no guarantee needed / 看见 has run is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经套用 candidate 就不需要 guarantee interchangeable / 已经 previously executed interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 even if passed not previously executed bundled（473 第三件事 / 568 余量） interchangeable / 已经 even if passed interchangeable / 已经 apply candidate interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not already every validator bundled（570 余量） interchangeable / 已经 When calling interchangeable / 已经 every validator ran Process interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed bundled（571 余量） interchangeable / 已经 proposer Process interchangeable / 已经 local path interchangeable。**  
   官方 Usage 写 has run `ProcessProposal` on **that block**。看见对这块跑过 Process，不是已经 Alternatively apply candidate state（460 余量） interchangeable——472 bundled 第三件事常被写成「看见 previously executed 就不需要 guarantee」，本页钉 has run not apply candidate / previously executed 单句。看见 ran ProcessProposal，不是已经 FinalizeBlock 套用候选（460 余量） interchangeable——460 钉 execute txs / apply candidate / previously executed 三事，本页钉 guarantee 这句。看见 that block，不是已经 even if passed not previously executed（568 余量） interchangeable——568 钉 473 fill all fields even if passed 边界，本页钉 Finalize Usage has run 单句。
2. **看见 has run ProcessProposal on that block is not already ProcessProposal MAY fully execute means guarantee satisfied / 看见对这块跑过 Process is not already Process MAY 整块执行交差 不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经 Process MAY execute interchangeable / 已经 immediate execution 交差 interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 candidate state interchangeable / 已经改了已提交状态 interchangeable，也不是已经 ProcessProposal MAY fully execute not already committed bundled（543 余量） interchangeable / 已经 MAY execute not committed interchangeable / 已经是 ExecuteTxState interchangeable，也不是已经 read-only checks/processes bundled（545 余量） interchangeable / 已经 immediate execution committed interchangeable / 已经 checks/processes 就已经交差 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 ExecuteTxState interchangeable。**  
   官方把 has run ProcessProposal guarantee 和 Process MAY fully execute the block 已经交差分开——472 bundled 常与 452 混成「ran ProcessProposal = MAY execute = guarantee 已满足」，本页钉 has run not MAY execute committed 单句。看见 has run ProcessProposal，不是已经 ProcessProposal 候选执行（452 余量） interchangeable——452 钉 MAY execute / candidate / read-only 三事，本页钉 guarantee 单句。看见 that block，不是已经 Process MAY fully execute not committed（543 余量） interchangeable——543 钉 Usage MAY execute not committed，本页钉 has run 边界。
3. **看见 has run ProcessProposal on that block is not already VerifyVoteExtension proposed block no Process guarantee / 看见对这块跑过 Process is not already VVE hash points to proposed block no guarantee interchangeable 不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经拟议块无保证 interchangeable / 已经 hash 指拟议块 interchangeable，也不是已经 VerifyVoteExtension Usage hash does not guarantee Process bundled（418 余量） interchangeable / 已经对该块跑过 Process interchangeable / 已经 exposed via ProcessProposal interchangeable，也不是已经 VerifyVoteExtension Usage hash points to block bundled（353 余量） interchangeable / 已经 hash 指块 interchangeable / 已经验过扩展 interchangeable，也不是已经 ProcessProposal 也会在提议者那边叫 bundled（351 余量） interchangeable / 已经提议者 Process 过 interchangeable / 已经 proposer path interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed bundled（571 余量） interchangeable / 已经 local path interchangeable / 已经 list matches interchangeable。**  
   官方把 Finalize 对**已决**块的 has run ProcessProposal guarantee 和 VVE 对**拟议**块的 There is no guarantee that this proposed block has previously been exposed via `ProcessProposal` 分开——472 bundled 常与 418 混成「hash 指块 = 已经跑过 Process = guarantee interchangeable」，本页钉 has run on decided block not VVE proposed no guarantee 单句。看见 has run on that block，不是已经 VerifyVoteExtension Usage hash does not guarantee Process（418 余量） interchangeable——418 钉 VVE 拟议块边界，本页钉 Finalize 已决块 guarantee 单句。看见 ran ProcessProposal，不是已经 VerifyVoteExtension Usage hash points to block（353 余量） interchangeable——353 钉 hash points to block 单句，本页钉 472 item 3 边界。

怎样写 Finalize、怎样实现 candidate 缓存、怎样测 VVE 边界 是规范里的做法，本页不抄。FinalizeBlock When calling ProcessProposal guarantee bundled（472）、When calling not every validator（570 余量）、at least one not proposer（571 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **has run not apply candidate / previously executed ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 has run ProcessProposal guarantee 和 apply candidate / previously executed 分开。
- **has run not MAY execute committed ≠ ProcessProposal 候选执行 bundled interchangeable：** 官方把 guarantee 和 Process MAY fully execute 已经交差 分开。
- **has run on decided block not VVE proposed no guarantee ≠ VerifyVoteExtension 拟议块无保证 interchangeable：** 官方把 Finalize 已决块 guarantee 和 VVE 拟议块边界 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| has run ProcessProposal on that block | 不是 already apply candidate / previously executed | 不是 Finalize 套用候选（460） |
| has run ProcessProposal on that block | 不是 already Process MAY fully execute committed | 不是 ProcessProposal 候选执行（452） |
| has run ProcessProposal on that block | 不是 already VVE proposed block no guarantee | 不是 VerifyVoteExtension hash does not guarantee Process（418） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not apply candidate 正式三事（472 余量），必须分开 has run 是不是 already apply candidate / previously executed interchangeable / 472 bundled interchangeable / 460 apply candidate interchangeable、has run 是不是 already Process MAY fully execute committed interchangeable / 452 candidate interchangeable / 543 MAY execute not committed interchangeable、has run 是不是 already VVE proposed block no guarantee interchangeable / 418 VVE proposed interchangeable / 353 hash points interchangeable。可以跳过「看见对这块跑过 Process 就已经套用 candidate 就不需要 guarantee interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样实现 candidate 缓存、怎样测 VVE 边界。
- When calling not every validator ran Process。那是不变量 570（472 item 1 余量）。
- at least one not proposer Process means everyone Processed。那是不变量 571（472 item 2 余量）。
- FinalizeBlock When calling ProcessProposal guarantee bundled 三事。那是不变量 472。
