# 例：看见 at least one non-byzantine validator / 看见至少一名非拜占庭 is not already proposer Process means everyone Processed / 看见 at least one is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经提议者 Process 过就代表全网都 Process 过 interchangeable / 已经 proposer Process interchangeable

**层次**：实现 / FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「at least one non-byzantine not proposer Process means everyone Processed / not finproc bundled（472） interchangeable / not Process also on proposer（351） interchangeable / not local node path interchangeable」，不是 FinalizeBlock When calling ProcessProposal guarantee bundled（472），也不是 When calling not every validator（570 余量），也不是 has run ProcessProposal not apply candidate（572 余量）。不要另写怎样写 Finalize、怎样缓存 candidate。

## 官方三件事

规范把 FinalizeBlock Usage 里 at least one non-byzantine validator has run `ProcessProposal` on that block 和「提议者 Process 过就代表全网都 Process 过 / 本节点刚 Process 过就代表每个验证者都 Process 过 / Process 也会在提议者那边叫 bundled interchangeable」分开写成三件独立的实现事，不是「看见至少一名就已经提议者 Process 过 interchangeable、已经本节点 Process 过 interchangeable、已经 Process 通常紧跟 Prepare interchangeable」一件事：

1. **看见 at least one non-byzantine validator / 看见至少一名非拜占庭 is not already proposer Process means everyone Processed / 看见 at least one is not already FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经提议者 Process 过就代表全网都 Process 过 interchangeable / 已经 proposer Process interchangeable，也不是已经 ProcessProposal 也会在这一轮的提议者那边叫 bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经自己刚 Prepare 过 interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 已经不用再 Process interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not already every validator bundled（472 第一件事 / 570 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经 When calling interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 previously executed interchangeable / 已经 candidate 就不需要 guarantee interchangeable。**  
   官方 Usage 写 guarantees that **at least one** non-byzantine validator has run `ProcessProposal` on that block。看见 at least one，不是 already every validator——472 bundled 第二件事常被写成「看见至少一名就已经提议者 Process 过就代表全网都 Process 过」，本页钉 at least one not proposer means everyone 单句。看见 non-byzantine，不是已经 ProcessProposal 也会在这一轮的提议者那边叫（351 余量） interchangeable——351 钉提议者路径 / Prepare 对得上 / 失败时不保证 bundled，本页钉 Finalize Usage at least one 单句。看见 at least one non-byzantine，不是已经 When calling not every validator（570 余量） interchangeable——570 钉 When calling 单句，本页钉 at least one 单句。
2. **看见 at least one non-byzantine is not already local node just Processed means every validator Processed / 看见至少一名 is not already this node just ran Process means all validators ran Process 不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经本节点刚 Process 过 interchangeable / 已经 local path interchangeable，也不是已经 VerifyVoteExtension local precommit not called bundled（457 余量） interchangeable / 已经 local 路径 interchangeable / 已经验完 interchangeable，也不是已经 ProcessProposal 也会在这一轮的提议者那边叫 bundled（351 余量） interchangeable / 已经提议者 Process 过 interchangeable / 已经 proposer path interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable / 已经字段再填一遍 interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not already every validator bundled（570 余量） interchangeable / 已经 every validator ran Process interchangeable / 已经 When calling interchangeable。**  
   官方把 at least one guarantee 和「本节点刚 Process 过就代表每个验证者都 Process 过」分开——472 bundled 常与 457 混成「local 路径 = 已经验完 = 每个验证者都 Process 过」，本页钉 at least one not local node means every validator 单句。看见 at least one non-byzantine，不是已经 VerifyVoteExtension 对 local precommit 不调用（457 余量） interchangeable——457 钉 VVE 门 local 路径，本页钉 Finalize Usage at least one 边界。看见至少一名，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉提议者路径，本页钉 472 item 2 not local 边界。
3. **看见 at least one non-byzantine is not already Process follows Prepare / list matches means no more Process needed / 看见至少一名 is not already ProcessProposalRequest.txs equals PrepareProposalResponse.txs means guarantee satisfied 不是已经 FinalizeBlock When calling ProcessProposal guarantee bundled（472） interchangeable / 已经列表对得上 interchangeable / 已经 Process 通常紧跟 Prepare interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经 guarantee this proposal interchangeable / 已经 list matches interchangeable，也不是已经 PrepareProposal When return / use-as-proposal bundled（506 余量） interchangeable / 已经 includes tx list in return interchangeable / 已经 Process follows Prepare interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 第三件事） interchangeable / 已经 failure may match earlier Prepare interchangeable / 已经 may not call Process interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not already every validator bundled（570 余量） interchangeable / 已经 When calling interchangeable / 已经 every validator ran Process interchangeable。**  
   官方把 at least one guarantee 和 Process 通常紧跟 Prepare / txs 对得上就不叫 Process bundled 分开——472 bundled 常与 351 混成「列表对得上 = 提议者 Process 过 = 全网都 Process 过」，本页钉 at least one not list matches means guarantee 单句。看见 at least one，不是已经 Process 通常紧跟 Prepare / txs equals PrepareResponse（351 余量） interchangeable——351 钉提议者 Process 三事，本页钉 at least one 单句。看见 guarantees at least one ran ProcessProposal，不是已经 Prepare When return / use-as-proposal（506 余量） interchangeable——506 钉 includes tx list in return，本页钉 472 item 2 边界。

怎样写 Finalize、怎样写 Process 提议者路径、怎样测失败路径 是规范里的做法，本页不抄。FinalizeBlock When calling ProcessProposal guarantee bundled（472）、When calling not every validator（570 余量）、has run ProcessProposal not apply candidate（572 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **at least one not proposer means everyone Processed ≠ FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable：** 官方把 at least one 和提议者 Process 过就代表全网都 Process 过 分开。
- **at least one not local node means every validator Processed ≠ VerifyVoteExtension local path interchangeable：** 官方把 at least one 和本节点刚 Process 过 分开。
- **at least one not list matches means guarantee satisfied ≠ Process follows Prepare bundled interchangeable：** 官方把 at least one guarantee 和 Prepare/Process 列表对得上 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| at least one non-byzantine | 不是 already proposer Process means everyone Processed | 不是 Process 也会在提议者那边叫（351） |
| at least one non-byzantine | 不是 already local node just Processed means every validator | 不是 VerifyVoteExtension local precommit not called（457） |
| at least one non-byzantine | 不是 already list matches means guarantee satisfied | 不是 Process 通常紧跟 Prepare（351） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量），必须分开 at least one 是不是 already proposer Process means everyone Processed interchangeable / 472 bundled interchangeable / 351 Process also on proposer interchangeable、at least one 是不是 already local node just Processed means every validator interchangeable / 457 VVE local interchangeable / 351 proposer path interchangeable、at least one 是不是 already list matches means guarantee satisfied interchangeable / 351 Process follows Prepare interchangeable / 506 Prepare return interchangeable。可以跳过「看见至少一名就已经提议者 Process 过就代表全网都 Process 过 interchangeable」。不要另写怎样写 Finalize。

## 本页不抄

- 怎样写 Finalize、怎样写 Process 提议者路径、怎样测失败路径。
- When calling not every validator ran Process。那是不变量 570（472 item 1 余量）。
- has run ProcessProposal not apply candidate / previously executed。那是不变量 572（472 item 3 余量）。
- FinalizeBlock When calling ProcessProposal guarantee bundled 三事。那是不变量 472。
