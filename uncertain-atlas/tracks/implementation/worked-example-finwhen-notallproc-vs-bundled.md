# 例：看见 When calling FinalizeBlock / guarantees at least one non-byzantine ran Process is not already every validator has run Process / not FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / not Finalize 时的 Process 保证 bundled（360） interchangeable

**层次**：实现 / FinalizeBlock When calling ProcessProposal guarantee not every validator 正式三事（472 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When calling ProcessProposal guarantee not every validator / not FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / not Finalize 时的 Process 保证 bundled（360） interchangeable」，不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472），也不是 at least one non-byzantine ran Process not every validator 正式三事（582 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 When calling `FinalizeBlock`, the consensus algorithm guarantees that at least one non-byzantine validator has run `ProcessProposal` on that block 和「已经 every validator has run ProcessProposal / 已经是 Finalize 时的 Process 保证 bundled / 已经是 FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable」分开写成三件独立的实现事，不是「看见 When calling guarantee 就已经 every validator ran Process interchangeable、已经 Finalize 时的 Process 保证 bundled interchangeable、已经 472 finwhen bundled interchangeable」一件事：

1. **看见 When calling `FinalizeBlock`, the consensus algorithm guarantees that at least one non-byzantine validator has run `ProcessProposal` on that block / 看见至少一名非拜占庭验证者跑过 Process is not already every validator has run ProcessProposal / 看见要 Finalize 了 is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经 When calling bundled interchangeable / 已经 guarantee interchangeable / 已经 persist decision interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 every validator ran Process interchangeable，也不是已经 at least one non-byzantine ran Process not every validator bundled（582 余量） interchangeable / 582 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable。**  
   官方 Usage 写：When calling `FinalizeBlock`, the consensus algorithm guarantees that **at least one** non-byzantine validator has run `ProcessProposal` on that block。看见 When calling / guarantees at least one，不是已经 every validator has run ProcessProposal interchangeable——472 item 1 常被写成「看见要 Finalize 了就已经每个验证者都跑过 Process」，本页钉 When calling guarantee not every validator 单句。看见 guarantees at least one，不是已经 FinalizeBlock When calling ProcessProposal guarantee（472） interchangeable——472 另钉 not proposer / not executes block v 三事，本页钉 item 1 边界。看见 When calling FinalizeBlock，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 fill all fields / apply candidate bundled，本页钉 finwhen notallproc 单句。
2. **看见 When calling / guarantees at least one is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 看见至少一名 is not already at least one non-byzantine ran Process not every validator interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 persist decision interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 351 Process also on proposer interchangeable / 582 not proposer interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 583 not refill interchangeable。**  
   官方把 When calling guarantee 和 Finalize 时的 Process 保证 bundled 分开——472 item 1 常与 360 混成「看见 When calling guarantee 就已经是 Finalize 时的 Process 保证 bundled interchangeable」，本页钉 When calling not 360 bundled 单句。看见 guarantees at least one，不是已经 at least one non-byzantine ran Process（582 余量） interchangeable——582 从 360 角度钉 at least one 单句，本页钉 472 item 1 单句。看见 When calling，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉 proposer path，本页钉 finwhen notallproc 单句。
3. **看见 When calling / guarantees at least one is not already at least one non-byzantine ran Process not every validator bundled（582 余量） interchangeable / 看见至少一名 is not already at least one not every validator interchangeable / 582 not every validator interchangeable / 已经 360 item 1 单句 interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。**  
   官方把 When calling guarantee 和 360 item 1 at least one 单句分开——472 item 1 常与 582 混成「看见 When calling guarantee 就已经是 at least one not every validator interchangeable」，本页钉 When calling not 582 not every validator 单句。看见 guarantees at least one，不是已经 Application executes block v（466 余量） interchangeable——466 When 流程另钉 executes block _v_ 三事，本页钉 472 item 1 第三件事。看见 When calling FinalizeBlock，不是已经 even if already passed（568 余量） interchangeable——568 钉 473 item 2 边界，本页钉 finwhen notallproc 单句。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径是规范里的做法，本页不抄。FinalizeBlock When calling ProcessProposal guarantee bundled（472）、at least one non-byzantine not proposer Process means everyone Processed 正式三事（571 余量）、FinalizeBlock When Application executes block v bundled（466 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **When calling guarantee not every validator ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 When calling / at least one guarantee 和 every validator ran Process 分开。
- **When calling guarantee not every validator ≠ Finalize 时的 Process 保证 bundled interchangeable：** 官方把 When calling guarantee 和 360 bundled 分开。
- **When calling guarantee not every validator ≠ 582 not every validator interchangeable：** 官方把 472 item 1 和 360 item 1 at least one 单句分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| When calling guarantee | 不是 already every validator ran Process | 不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472） |
| When calling guarantee | 不是 already Finalize 时的 Process 保证 bundled | 不是 Finalize 时的 Process 保证 bundled（360） |
| When calling guarantee | 不是 already 582 not every validator | 不是 at least one non-byzantine ran Process not every validator 正式三事（582） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not every validator 正式三事（472 余量），必须分开 When calling 是不是 already every validator ran Process interchangeable / 472 finwhen interchangeable / 571 not proposer interchangeable、When calling 是不是 already Finalize 时的 Process 保证 bundled interchangeable / 360 bundled interchangeable / 582 not every validator interchangeable、When calling 是不是 already 582 not every validator interchangeable / 466 executes block v interchangeable / 351 Process also on proposer interchangeable。可以跳过「看见 When calling guarantee 就已经 every validator ran Process interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- at least one non-byzantine not proposer Process means everyone Processed。那是不变量 571（472 item 2 余量）。
- When calling guarantee not executes block v / persist decision。那是不变量 466 / 472 item 3 余量。
- FinalizeBlock When calling ProcessProposal guarantee bundled 三事。那是不变量 472。
- at least one non-byzantine ran Process not every validator 正式三事（360 余量）。那是不变量 582。
