# 例：看见 at least one non-byzantine validator has run ProcessProposal is not already every validator has run Process / not Finalize 时的 Process 保证 bundled（360） interchangeable / not proposer Process means everyone Processed interchangeable

**层次**：实现 / at least one non-byzantine ran Process not every validator 正式三事（360 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「at least one non-byzantine ran Process not every validator / not Finalize 时的 Process 保证 bundled（360） interchangeable / not proposer Process means everyone Processed interchangeable」，不是 Finalize 时的 Process 保证 bundled（360），也不是 FinalizeBlock When calling ProcessProposal guarantee not already every validator（570 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里调用 `FinalizeBlock` 时共识算法保证至少一名非拜占庭验证者对这块跑过 `ProcessProposal` 和「已经每个验证者都跑过 Process / 已经是提议者那边也会叫 Process / Finalize 时的 Process 保证 bundled interchangeable」分开写成三件独立的实现事，不是「看见要 Finalize 了就已经每个验证者都跑过 Process interchangeable、已经提议者 Process 过就代表全网都 Process 过 interchangeable、已经 Finalize 时的 Process 保证 bundled interchangeable」一件事：

1. **看见 When calling `FinalizeBlock`, the consensus algorithm guarantees that at least one non-byzantine validator has run `ProcessProposal` on that block / 看见至少一名非拜占庭验证者跑过 Process is not already every validator has run ProcessProposal / 看见要 Finalize 了 is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 every validator ran Process interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not already every validator bundled（472 第一件事 / 570 余量） interchangeable / 已经 When calling bundled interchangeable / 已经 guarantee interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 persist decision interchangeable / 已经每个验证者都跑过 Process interchangeable，也不是已经 at least one non-byzantine not proposer Process means everyone Processed bundled（472 第二件事 / 571 余量） interchangeable / 已经提议者 Process 过就代表全网都 Process 过 interchangeable / 已经 proposer Process interchangeable。**  
   官方 Usage 写：When calling `FinalizeBlock`, the consensus algorithm guarantees that **at least one** non-byzantine validator has run `ProcessProposal` on that block。看见至少一名，不是已经 every validator has run ProcessProposal interchangeable——360 bundled 第一件事常被写成「看见要 Finalize 了就已经每个验证者都跑过 Process」，本页钉 at least one not every validator 单句。看见 guarantees at least one，不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable——360 另钉 fill all fields / apply candidate bundled，本页钉 item 1 边界。看见 When calling FinalizeBlock，不是已经 When calling ProcessProposal guarantee not every validator（570 余量） interchangeable——570 从 472 角度钉 When calling 单句，本页从 360 角度钉 at least one 单句。
2. **看见 at least one non-byzantine validator has run ProcessProposal is not already proposer also Process means don't need Process elsewhere / 看见至少一名 is not already Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经提议者 Process 过就代表全网都 Process 过 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经字段再填一遍 interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable，也不是已经 at least one non-byzantine not proposer Process means everyone Processed bundled（472 第二件事 / 571 余量） interchangeable / 已经 local node Processed means every validator Processed interchangeable / 已经 proposer path interchangeable。**  
   官方把 at least one guarantee 和提议者也会 Process 分开——360 bundled 常与 351 混成「看见至少一名非拜占庭验证者跑过 Process 就已经是提议者那边也会叫 Process interchangeable」，本页钉 at least one not proposer means everyone Processed 单句。看见 at least one，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉 proposer path，本页钉 360 item 1 边界。看见 guarantees at least one，不是已经 at least one not proposer（571 余量） interchangeable——571 钉 472 item 2 边界，本页钉 360 item 1 单句。
3. **看见 at least one non-byzantine validator has run ProcessProposal is not already When calling / consensus guarantees means Application executes block v / persist decision / 看见至少一名 is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经 persist decision interchangeable / 已经把块落成这一高的决定 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 executes block v interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 +2/3 precommit same id(v) already will Finalize bundled（362 余量） interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable / 已经 +2/3 precommit interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360） interchangeable / 已经字段再填一遍 interchangeable / 已经套用先前候选 interchangeable。**  
   官方把 at least one guarantee 和 When 第 3 步 Application executes block _v_ / persist decision 分开——360 bundled 常与 466 混成「看见至少一名非拜占庭验证者跑过 Process 就已经 persist decision interchangeable」，本页钉 at least one not executes block v 单句。看见 guarantees at least one，不是已经 Application executes block _v_（466 余量） interchangeable——466 When 流程另钉 executes block _v_ 三事，本页钉 360 item 1 边界。看见 When calling FinalizeBlock，不是已经 +2/3 precommit same id(v)（362 余量） interchangeable——362 钉 When 流程 precommit 路径，本页钉 at least one not every validator 单句。

怎样写 Finalize、怎样缓存 candidate、怎样测失败路径是规范里的做法，本页不抄。Finalize 请求把字段再填一遍（583 余量）、可以套用先前候选不是 ExecuteTxState（584 余量）、Finalize 时的 Process 保证 bundled（360）是另外那套，本页不抄。

## 官方为什么这样拆

- **at least one non-byzantine ran Process not every validator ≠ Finalize 时的 Process 保证 bundled interchangeable：** 官方把 at least one guarantee 和 every validator ran Process 分开。
- **at least one not proposer means everyone Processed ≠ Process 也会在提议者那边叫 interchangeable：** 官方把 at least one guarantee 和 proposer path 分开。
- **at least one not executes block v / persist decision ≠ When calling guarantee bundled interchangeable：** 官方把 Usage guarantee 和 When 第 3 步 executes block _v_ 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| at least one non-byzantine ran Process | 不是 already every validator ran Process | 不是 Finalize 时的 Process 保证 bundled（360） |
| at least one non-byzantine ran Process | 不是 already proposer means everyone Processed | 不是 Process 也会在提议者那边叫（351） |
| at least one non-byzantine ran Process | 不是 already executes block v / persist decision | 不是 FinalizeBlock When Application executes block v（466） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 at least one non-byzantine ran Process not every validator 正式三事（360 余量），必须分开 at least one 是不是 already every validator ran Process interchangeable / 360 bundled interchangeable / 570 not every validator interchangeable、at least one 是不是 already proposer Process means everyone Processed interchangeable / 351 Process also on proposer interchangeable / 571 not proposer interchangeable、at least one 是不是 already executes block v / persist decision interchangeable / 466 executes block v interchangeable / 472 When calling interchangeable。可以跳过「看见要 Finalize 了就已经每个验证者都跑过 Process interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样缓存 candidate、怎样测失败路径。
- Finalize 请求把字段再填一遍不是已经不用再给。那是不变量 583（360 item 2 余量）。
- 可以套用先前候选不是已经是 ExecuteTxState。那是不变量 584（360 item 3 余量）。
- Finalize 时的 Process 保证 bundled 三事。那是不变量 360。
- FinalizeBlock When calling ProcessProposal guarantee not already every validator。那是不变量 570（472 item 1 余量）。
