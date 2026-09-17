# 例：看见自己是提议者会先走完 Prepare 那五步 / proposer prepare five steps is not already no Process / proposer prepare five steps is not already guarantee this proposal 不是已经头字段对上余量 bundled interchangeable / 已经不用再 Process interchangeable / 已经保证是这一次 interchangeable

**层次**：实现 / 头字段对上余量 proposer prepare five steps not already no Process 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「proposer prepare five steps not already no Process 不是头字段对上余量 bundled interchangeable / 不是已经不用再 Process interchangeable / 不是已经保证是这一次 interchangeable」，不是头字段对上余量 bundled（417），也不是 Process 也会在提议者那边叫（351），也不是 Process 的 height / time 对上拟议块头（417 item 2 余量 / 549 余量）。不要另写怎样写头字段对上余量。

## 官方三件事

规范把 ProcessProposal When 里若 *p* 是提议者、*p* 先执行 Prepare 那五步，和 Process 也会在提议者那边叫、通常紧跟 Prepare、列表对得上分开写成三件独立的实现事，不是「看见自己是提议者走完了 Prepare 那五步 就已经不用再 Process interchangeable、已经保证是这一次 interchangeable、已经 Process follows Prepare interchangeable」一件事：

1. **看见自己是提议者会先走完 Prepare 那五步 / 看见 proposer prepare five steps is not already no Process / 看见走完了 is not already Process also on proposer 不是已经头字段对上余量 bundled（417） interchangeable / 已经不用再 Process interchangeable / 已经 Process 也会在提议者那边叫 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经提议者也会跑 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 ProcessProposal When basic checks then async bundled（354 余量） interchangeable / 已经 will not be able to reject interchangeable / 已经 async 了还能 Reject interchangeable，也不是已经 Process 的 height / time 对上拟议块头 bundled（417 第二件事 / 549 余量） interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable，也不是已经 Finalize 的 height / time 对上拟议块头 bundled（417 第三件事 / 563 余量） interchangeable / 已经刚决定那块的字段 interchangeable / 已经知道本头哈希 interchangeable。**  
   官方 When 写：若 *p* 是提议者，*p* 先执行 Prepare 那五步。看见走完了，不是已经 Process 也会在提议者那边叫那种已经不用再 Process——417 bundled 第一件事常被写成「看见自己是提议者走完了 Prepare 就已经不用再 Process」，本页钉 proposer prepare five steps not already no Process 单句。看见先走 Prepare，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉提议者也会跑 Process，本页钉 When 先走 Prepare 五步边界。看见自己是提议者，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 Process follows Prepare，本页钉 proposer prepare not no Process 单句。
2. **看见 proposer prepare five steps is not already guarantee this proposal / 看见走完了 is not already this round / this height-round proposal 不是已经头字段对上余量 bundled（417） interchangeable / 已经保证是这一次 interchangeable / 已经列表对得上 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 已经列表对得上 interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 PrepareProposal When return / use-as-proposal bundled（506 余量） interchangeable / 已经 includes tx list in return interchangeable / 已经 guarantee this proposal interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经失败时可能对上更早一次 interchangeable / 已经每轮都会叫 interchangeable，也不是已经 ProcessProposalRequest.txs 等于 PrepareProposalResponse.txs bundled（351 余量） interchangeable / 已经保证是这一次 Prepare interchangeable / 已经 Prepare 改列表 interchangeable，也不是已经 Process 的 height / time 对上拟议块头 bundled（417 第二件事 / 549 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable。**  
   官方把 When 里先走 Prepare 那五步和通常紧跟 Prepare、列表对得上那种已经保证是这一次分开——417 bundled 常与 351 混成「走完了 Prepare 就已经保证是这一次」，本页钉 proposer prepare five steps not already guarantee this proposal 单句。看见走完了，不是已经 Process 也会在提议者那边叫（351 余量） interchangeable——351 钉失败时可能对上更早一次或根本不调，本页钉 When 先走 Prepare 边界。看见自己是提议者，不是已经 Prepare When return / use-as-proposal（506 余量） interchangeable——506 钉 includes tx list in return，本页钉 proposer prepare not guarantee this round 单句。
3. **看见 proposer prepare five steps is not already Process follows Prepare / 看见先走 Prepare is not already ProcessProposalRequest.txs equals PrepareProposalResponse.txs 不是已经头字段对上余量 bundled（417） interchangeable / 已经 Process follows Prepare interchangeable / 已经不用再 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经列表对得上 interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351 余量） interchangeable / 已经提议者也会跑 Process interchangeable / 已经不用再 Process interchangeable，也不是已经 PrepareProposal When return / use-as-proposal bundled（506 余量） interchangeable / 已经 includes tx list in return interchangeable / 已经 Process 通常紧跟 Prepare interchangeable，也不是已经 ProcessProposal When basic checks then async bundled（354 余量） interchangeable / 已经 will not be able to reject interchangeable / 已经 async 了还能 Reject interchangeable，也不是已经 Process 的 height / time 对上拟议块头 bundled（417 第二件事 / 562 余量） interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable。**  
   官方把 When 里先走 Prepare 那五步和 Process 通常紧跟 Prepare、ProcessProposalRequest.txs equals PrepareProposalResponse.txs 分开——417 bundled 常与 351 混成「走完了 Prepare 就已经 Process follows Prepare interchangeable」，本页钉 proposer prepare five steps not already Process follows Prepare 单句。看见先走 Prepare，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉列表对得上，本页钉 When 先走 Prepare 五步边界。看见走完了，不是已经 ProcessProposal When basic checks then async（354 余量） interchangeable——354 钉 When async path，本页钉 proposer prepare not Process follows Prepare 单句。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。头字段对上余量 bundled（417）、Process 也会在提议者那边叫（351）、Process 的 height / time 对上拟议块头（417 item 2 / 549）是另外那套，本页不抄。

## 官方为什么这样拆

- **proposer prepare five steps not already no Process ≠ 头字段对上余量 bundled interchangeable：** 官方把 When 里先走 Prepare 那五步和 Process 也会在提议者那边叫就已经不用再 Process 分开。
- **proposer prepare five steps not already guarantee this proposal ≠ 351 列表对得上 interchangeable：** 官方把 When 先走 Prepare 和已经保证是这一次分开。
- **proposer prepare five steps not already Process follows Prepare ≠ 351 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable：** 官方把 When 先走 Prepare 和 Process 通常紧跟 Prepare 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| proposer prepare five steps | 不是 already no Process | 不是 Process 也会在提议者那边叫（351） |
| proposer prepare five steps | 不是 already guarantee this proposal | 不是 Prepare When return / use-as-proposal（506） |
| proposer prepare five steps | 不是 already Process follows Prepare | 不是 Process 通常紧跟 Prepare（351） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 proposer prepare five steps not already no Process 正式三事，必须分开 proposer prepare five steps 是不是 already no Process interchangeable / 351 Process also on proposer interchangeable、proposer prepare five steps 是不是 already guarantee this proposal interchangeable / 351 list matches interchangeable、proposer prepare five steps 是不是 already Process follows Prepare interchangeable / 351 txs equals PrepareResponse interchangeable。可以跳过「看见自己是提议者走完了 Prepare 就已经不用再 Process interchangeable」。不要另写怎样写头字段对上余量。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- Process 的 height / time 对上拟议块头 not already verified。那是不变量 562（417 item 2 余量）。
- Finalize 的 height / time 对上拟议块头 not newly decided fields。那是不变量 563（417 item 3 余量）。
- Process 也会在提议者那边叫 bundled 三事。那是不变量 351。
- 收到带上头的提案会先验块头。那是不变量 416。
