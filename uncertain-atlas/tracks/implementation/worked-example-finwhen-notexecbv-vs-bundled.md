# 例：看见 at least one non-byzantine ran Process is not already When calling / consensus guarantees means Application executes block v / persist decision / not FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / not FinalizeBlock When Application executes block v bundled（466） interchangeable

**层次**：实现 / FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision 正式三事（472 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision / not FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / not FinalizeBlock When Application executes block v bundled（466） interchangeable」，不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472），也不是 at least one non-byzantine ran Process not executes block v 正式三事（582 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 at least one non-byzantine validator has run ProcessProposal 和「已经 When calling guarantee 就是 persist decision / executes block v interchangeable / 已经是 FinalizeBlock When Application executes block v bundled interchangeable」分开写成三件独立的实现事，不是「看见 guarantees at least one 就已经 persist decision interchangeable、已经 executes block v interchangeable、已经 472 finwhen bundled interchangeable」一件事：

1. **看见 at least one non-byzantine validator has run ProcessProposal is not already When calling / consensus guarantees means Application executes block v / persist decision / 看见至少一名 is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经 persist decision interchangeable / 已经把块落成这一高的决定 interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经字段再填一遍 interchangeable / 已经套用先前候选 interchangeable，也不是已经 When calling guarantee not every validator bundled（570 余量） interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable。**  
   官方把 Usage 里的 at least one guarantee 和 When 第 3 步 Application executes block _v_ / persist decision 分开——472 item 3 常被写成「看见 When calling guarantee 就已经 persist decision interchangeable」，本页钉 When calling guarantee not executes block v 单句。看见 guarantees at least one，不是已经 FinalizeBlock When calling ProcessProposal guarantee（472） interchangeable——472 另钉 not every validator / not proposer 三事，本页钉 item 3 边界。看见 When calling FinalizeBlock，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 fill all fields / apply candidate bundled，本页钉 finwhen notexecbv 单句。
2. **看见 at least one non-byzantine ran Process is not already FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 看见至少一名 is not already Application executes block v interchangeable / 已经 executes block v interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 When 第 3 步 executes block _v_ interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 572 not execbv interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 362 +2/3 precommit interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（584 余量） interchangeable / 584 apply candidate interchangeable / 583 not refill interchangeable。**  
   官方把 at least one guarantee 和 When 第 3 步 Application executes block _v_ 分开——472 item 3 常与 466 混成「看见 guarantees at least one 就已经是 Application executes block v interchangeable」，本页钉 not executes block v not 466 bundled 单句。看见 at least one，不是已经 Application executes block _v_（466 余量） interchangeable——466 When 流程另钉 executes block _v_ 三事，本页钉 472 item 3 单句。看见 guarantees at least one，不是已经 apply candidate（584 余量） interchangeable——584 钉 360 item 3 边界，本页钉 finwhen notexecbv 单句。
3. **看见 at least one non-byzantine ran Process is not already at least one non-byzantine not executes block v / persist decision bundled（582 余量） interchangeable / 看见至少一名 is not already at least one not executes block v interchangeable / 582 not executes block v interchangeable / 已经 360 item 1 单句 interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 572 not execbv interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 362 +2/3 precommit interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable，也不是已经 Finalize 请求把字段再填一遍 not no need to provide again bundled（583 余量） interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。**  
   官方把 at least one guarantee 和 360 item 1 not executes block v 单句分开——472 item 3 常与 582 混成「看见 guarantees at least one 就已经是 at least one not executes block v interchangeable」，本页钉 not executes block v not 582 not executes block v 单句。看见 at least one，不是已经 +2/3 precommit same id(v)（362 余量） interchangeable——362 钉 When 流程 precommit 路径，本页钉 472 item 3 第三件事。看见 When calling guarantee，不是已经 even if already passed（568 余量） interchangeable——568 钉 473 item 2 边界，本页钉 finwhen notexecbv 单句。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径是规范里的做法，本页不抄。FinalizeBlock When calling ProcessProposal guarantee bundled（472）、FinalizeBlock When Application executes block v bundled（466 余量）、at least one non-byzantine ran Process not executes block v 正式三事（582 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **When calling guarantee not executes block v / persist decision ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 Usage guarantee 和 When 第 3 步 executes block _v_ 分开。
- **When calling guarantee not executes block v / persist decision ≠ Application executes block v bundled interchangeable：** 官方把 at least one guarantee 和 466 When 流程 executes block _v_ 分开。
- **When calling guarantee not executes block v / persist decision ≠ 582 not executes block v interchangeable：** 官方把 472 item 3 和 360 item 1 not executes block v 单句分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| at least one guarantee | 不是 already executes block v / persist decision | 不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472） |
| at least one guarantee | 不是 already Application executes block v | 不是 FinalizeBlock When Application executes block v（466） |
| at least one guarantee | 不是 already 582 not executes block v | 不是 at least one non-byzantine ran Process not executes block v 正式三事（582） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision 正式三事（472 余量），必须分开 at least one 是不是 already persist decision / executes block v interchangeable / 472 finwhen interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable、at least one 是不是 already Application executes block v interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable / 584 apply candidate interchangeable、at least one 是不是 already 582 not executes block v interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。可以跳过「看见 When calling guarantee 就已经 persist decision interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- When calling guarantee not every validator。那是不变量 570（472 item 1 余量）。
- When calling guarantee not proposer means everyone Processed。那是不变量 571（472 item 2 余量）。
- FinalizeBlock When calling ProcessProposal guarantee bundled 三事。那是不变量 472。
- at least one non-byzantine ran Process not executes block v 正式三事（360 余量）。那是不变量 582。
