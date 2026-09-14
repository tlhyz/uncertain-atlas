# 例：看见 When calling FinalizeBlock with a block / consensus algorithm guarantees is not already every validator has run ProcessProposal / 看见 When calling is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 Application executes block v persist decision interchangeable

**层次**：实现 / FinalizeBlock When calling ProcessProposal guarantee not already every validator 正式三事（472 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「When calling FinalizeBlock / consensus guarantees not already every validator ran Process / not finproc bundled（472） interchangeable / not Application executes block v interchangeable / not +2/3 precommit already Finalize interchangeable」，不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472），也不是 at least one non-byzantine not proposer（571 余量），也不是 has run ProcessProposal not apply candidate（572 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 When calling `FinalizeBlock` with a block / the consensus algorithm run by CometBFT guarantees / at least one non-byzantine validator has run `ProcessProposal` on that block 和「每个验证者都跑过 Process / 已经把块落成决定 / +2/3 precommit 就已经会 Finalize」分开写成三件独立的实现事，不是「看见要 Finalize 了就已经每个验证者都跑过 Process interchangeable、已经 Application executes block v interchangeable、已经 +2/3 precommit interchangeable」一件事：

1. **看见 When calling `FinalizeBlock` with a block, the consensus algorithm run by CometBFT guarantees / 看见要 Finalize 了有共识保证 is not already every validator has run `ProcessProposal` / 看见 When calling is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 every validator ran Process interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经字段再填一遍 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 persist decision interchangeable，也不是已经 at least one non-byzantine not proposer Process means everyone Processed bundled（472 第二件事 / 571 余量） interchangeable / 已经提议者 Process 过就代表全网都 Process 过 interchangeable / 已经 proposer Process interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经套用 candidate 就不需要 guarantee interchangeable / 已经 previously executed interchangeable。**  
   官方 Usage 写：When calling `FinalizeBlock` with a block, the consensus algorithm run by CometBFT guarantees that **at least one** non-byzantine validator has run `ProcessProposal` on that block。看见 When calling FinalizeBlock，不是已经 every validator has run ProcessProposal interchangeable——472 bundled 第一件事常被写成「看见要 Finalize 了就已经每个验证者都跑过 Process」，本页钉 When calling / consensus guarantees not every validator 单句。看见 guarantees at least one，不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable——360 钉字段再填一遍 / 套用候选 bundled，本页钉 When calling 单句。看见 consensus algorithm guarantees，不是已经 Application executes block v（466 余量） interchangeable——466 钉 When 第 3 步 executes block _v_，本页钉 Usage 这句 guarantee 边界。
2. **看见 When calling / consensus guarantees is not already `_p_`'s Application executes block _v_ / persist decision / 看见要 Finalize 了 is not already FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 persist decision interchangeable / 已经把块落成这一高的决定 interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 guarantee interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable / 已经 +2/3 precommit interchangeable，也不是已经 FinalizeBlock When Application executes block v not already every validator ran Process bundled（466 第二件事） interchangeable / 已经 ExecuteTxState interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 previously executed interchangeable / 已经 candidate 就不需要 guarantee interchangeable。**  
   官方把 When calling / consensus guarantees 和 When 第 3 步 Application executes block _v_ / persist decision 分开——472 bundled 常与 466 混成「guarantee = 已经执行完 / 已经 persist decision」，本页钉 When calling not executes block v 单句。看见 When calling FinalizeBlock，不是已经 Application executes block _v_（466 余量） interchangeable——466 When 流程另钉 executes block _v_ 三事，本页钉 Usage guarantee 单句。看见 consensus guarantees，不是已经 +2/3 precommit same id(v)（362 余量） interchangeable——362 钉 When 里 +2/3 precommit 会调 Finalize，本页钉 guarantee not every validator 边界。
3. **看见 When calling / consensus guarantees is not already +2/3 precommit same id(v) already will Finalize / 看见要 Finalize 了 is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经 +2/3 precommit interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable / 已经 +2/3 precommit interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 persist decision interchangeable / 已经每个验证者都跑过 Process interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable / 已经字段再填一遍 interchangeable，也不是已经 at least one non-byzantine not proposer Process means everyone Processed bundled（472 第二件事 / 571 余量） interchangeable / 已经提议者 Process 过 interchangeable / 已经 proposer Process interchangeable。**  
   官方把 When calling / consensus guarantees 和 When 里 +2/3 precommit 会调 Finalize 分开——472 bundled 常与 362 混成「看见 guarantee 就已经 +2/3 precommit 会 Finalize interchangeable」，本页钉 When calling not +2/3 precommit already Finalize 单句。看见 When calling FinalizeBlock，不是已经 +2/3 precommit same id(v)（362 余量） interchangeable——362 钉 When 流程 precommit 路径，本页钉 Usage guarantee 单句。看见 consensus guarantees at least one，不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable——360 另钉 fill all fields / apply candidate bundled，本页钉 472 item 1 边界。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径 是规范里的做法，本页不抄。FinalizeBlock When calling ProcessProposal guarantee bundled（472）、at least one non-byzantine not proposer（571 余量）、has run ProcessProposal not apply candidate（572 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **When calling / consensus guarantees not every validator ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 at least one guarantee 和 every validator ran Process 分开。
- **When calling not executes block v ≠ Application executes block v / persist decision interchangeable：** 官方把 Usage guarantee 和 When 第 3 步 executes block _v_ 分开。
- **When calling not +2/3 precommit already Finalize ≠ +2/3 precommit same id(v) interchangeable：** 官方把 Usage guarantee 和 When 里 precommit 路径分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| When calling / consensus guarantees | 不是 already every validator ran Process | 不是 Finalize 时的 Process 保证 bundled（360） |
| When calling / consensus guarantees | 不是 already executes block v / persist decision | 不是 FinalizeBlock When Application executes block v（466） |
| When calling / consensus guarantees | 不是 already +2/3 precommit will Finalize | 不是 +2/3 precommit same id(v)（362） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not already every validator 正式三事（472 余量），必须分开 When calling 是不是 already every validator ran Process interchangeable / 472 bundled interchangeable / 360 Process guarantee interchangeable、When calling 是不是 already executes block v / persist decision interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable、When calling 是不是 already +2/3 precommit will Finalize interchangeable / 362 When interchangeable / 360 bundled interchangeable。可以跳过「看见要 Finalize 了就已经每个验证者都跑过 Process interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- at least one non-byzantine not proposer Process means everyone Processed。那是不变量 571（472 item 2 余量）。
- has run ProcessProposal not apply candidate / previously executed。那是不变量 572（473 item 3 余量）。
- FinalizeBlock When calling ProcessProposal guarantee bundled 三事。那是不变量 472。
