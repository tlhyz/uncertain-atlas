# 例：看见 Process 的 `height` / `time` 对上拟议块头 / Process height/time match header is not already verified block header / Process height/time match header is not already ran Process 不是已经头字段对上余量 bundled interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable

**层次**：实现 / 头字段对上余量 Process height/time match header not already verified 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process height/time match header not already verified 不是头字段对上余量 bundled interchangeable / 不是已经验过块头 interchangeable / 不是已经跑过 Process interchangeable」，不是头字段对上余量 bundled（417），也不是 ProcessProposal height/time match header not already verified（549），也不是收到带上头的提案会先验块头（416）。不要另写怎样写头字段对上余量。

## 官方三件事

规范把 ProcessProposal Usage 里 Process 的 height 和 time 对上拟议块的头、When 里先验块头、Process 调用之前就已经跑过 Process、头字段 bundled 知道本头哈希分开写成三件独立的实现事，不是「看见 Process 对上了 就已经验过块头 interchangeable、已经跑过 Process interchangeable、已经知道本头哈希 interchangeable」一件事：

1. **看见 Process 的 `height` / `time` 对上拟议块头 / 看见 Process height/time match header is not already verified block header / 看见对上了 is not already When verify header 不是已经头字段对上余量 bundled（417） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经收到带上头的 Proposal 会先验块头 bundled（416 余量） interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable，也不是已经 ProcessProposal When basic checks then async bundled（354 余量） interchangeable / 已经 will not be able to reject interchangeable / 已经 async 了还能 Reject interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（454 第二件事 / 549 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 ProcessProposal height/time 对上拟议块头 bundled（454 余量） interchangeable / 已经 Process height/time match header interchangeable / 已经头字段对上余量 bundled interchangeable，也不是已经头字段对上余量 proposer prepare five steps not already no Process bundled（417 第一件事 / 561 余量） interchangeable / 已经不用再 Process interchangeable / 已经 Process 也会在提议者那边叫 interchangeable。**  
   官方写：Process 的 height 和 time 对上拟议块的头。看见对上了，不是已经 When 里收到带上头的 Proposal 会先验块头那种已经验过——417 bundled 第二件事常被写成「看见 Process 对上了就已经验过块头」，本页钉 Process height/time match header not already verified 单句。看见 match header，不是已经收到带上头的 Proposal 会先验块头（416 余量） interchangeable——416 钉 When 先验块头，本页钉 Usage match 边界。看见对上了，不是已经 ProcessProposal When basic checks then async（354 余量） interchangeable——354 钉 When async path，本页钉 Process match not verified 单句。
2. **看见 Process height/time match header is not already ran Process / 看见 Usage match 不是已经 Process 调用之前就已经跑过 Process 不是已经头字段对上余量 bundled（417） interchangeable / 已经跑过 Process interchangeable / 已经 Process 调用之前就已经跑过 interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经 Finalize 跑过 interchangeable / 已经执行那些交易 interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（454 第二件事 / 549 余量） interchangeable / 已经 ran Process interchangeable / 已经 Process follows Prepare interchangeable，也不是已经头字段对上余量 proposer prepare five steps not already no Process bundled（417 第一件事 / 561 余量） interchangeable / 已经 Process also on proposer interchangeable / 已经 guarantee this proposal interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable。**  
   官方把 Usage 里 match header 和 Process 调用之前就已经跑过 Process 分开——417 bundled 常与 351 混成「对上了就已经跑过 Process」，本页钉 Process height/time match header not already ran Process 单句。看见 match header，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 Process follows Prepare，本页钉 Usage match 边界。看见对上了，不是已经 Process 回了 ACCEPT 就已经交差 interchangeable——430 钉 Response status 后效，本页钉 Process match not ran Process 单句。
3. **看见 Process height/time match header is not header fields bundled know hash / 看见对上了 is not already Prepare 没有头哈希 / 已经知道本头哈希 不是已经头字段对上余量 bundled（417） interchangeable / 已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经 Prepare 没有头哈希 bundled（311 余量） interchangeable / 已经 candidate 不是 ExecuteTxState interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经 ProcessProposalRequest.hash 是拟议块的哈希 Request栏（419 余量） interchangeable / 已经跑过 Process interchangeable / 已经知道本头 interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（454 第二件事 / 549 余量） interchangeable / 已经 header fields bundled know hash interchangeable / 已经 417 bundled interchangeable，也不是已经 Finalize 的 height / time 对上拟议块头 bundled（417 第三件事 / 563 余量） interchangeable / 已经刚决定那块的字段 interchangeable / 已经 Finalize height/time match interchangeable。**  
   官方把 Usage match header 和头字段 bundled 知道本头哈希分开——417 bundled 常与 311 混成「对上了就已经知道本头哈希」，本页钉 Process height/time match header not header fields bundled 单句。看见 match header，不是已经 Prepare 没有头哈希（311 余量） interchangeable——311 钉 Prepare 没有头哈希，本页钉 Process Usage match 边界。看见对上了，不是已经 ProcessProposalRequest.hash 是拟议块的哈希（419 余量） interchangeable——419 钉 hash 单栏，本页钉 Process match not know hash 单句。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。头字段对上余量 bundled（417）、ProcessProposal height/time match header not already verified（549）、收到带上头的提案会先验块头（416）是另外那套，本页不抄。

## 官方为什么这样拆

- **Process height/time match header not already verified ≠ 头字段对上余量 bundled interchangeable：** 官方把 Usage match 和 When 里先验块头分开。
- **Process height/time match header not already ran Process ≠ Process follows Prepare interchangeable：** 官方把 Usage match 和 Process 调用之前就已经跑过 Process 分开。
- **Process height/time match header not header fields bundled ≠ 417 know hash interchangeable：** 官方把 Usage match 和头字段 bundled 知道本头哈希分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process height/time match header | 不是 already verified block header | 不是 When verify header（416） |
| Process Usage match header | 不是 already ran Process | 不是 Process follows Prepare（351） |
| Process match header | 不是 header fields bundled know hash | 不是 Prepare 没有头哈希（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 Process height/time match header not already verified 正式三事，必须分开 Process height/time match header 是不是 already verified block header interchangeable / 416 When verify interchangeable、Process height/time match header 是不是 already ran Process interchangeable / 351 Process follows Prepare interchangeable、Process height/time match header 是不是 header fields bundled know hash interchangeable / 311 Prepare no header hash interchangeable。可以跳过「看见 Process 对上了就已经验过块头 interchangeable」。不要另写怎样写头字段对上余量。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- 自己是提议者会先走完 Prepare 那五步 not already no Process。那是不变量 561（417 item 1 余量）。
- Finalize 的 height / time 对上拟议块头 not newly decided fields。那是不变量 563（417 item 3 余量）。
- ProcessProposal height/time match header not already verified bundled 三事。那是不变量 549（454 item 2 余量）。
- 收到带上头的提案会先验块头。那是不变量 416。
