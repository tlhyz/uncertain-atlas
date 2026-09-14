# 例：看见 Finalize 的 `height` / `time` 对上拟议块头 / Finalize height/time match header is not already newly decided block fields / Finalize height/time match header is not already know hash 不是已经头字段对上余量 bundled interchangeable / 已经是刚决定那块的字段 interchangeable / 已经知道本头哈希 interchangeable

**层次**：实现 / 头字段对上余量 Finalize height/time match header not already newly decided fields 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize height/time match header not already newly decided fields 不是头字段对上余量 bundled interchangeable / 不是已经是刚决定那块的字段 interchangeable / 不是已经知道本头哈希 interchangeable」，不是头字段对上余量 bundled（417），也不是 Finalize 含刚决定那块的字段（407），也不是 FinalizeBlock Finalize match header not ProcessProposal match（554）。不要另写怎样写头字段对上余量。

## 官方三件事

规范把 FinalizeBlock Usage 里 Finalize 的 height 和 time 对上拟议块的头、FinalizeBlock 含刚决定那块的字段、FinalizeBlockRequest.hash 是已决块的哈希、头字段 bundled 知道本头哈希分开写成三件独立的实现事，不是「看见 Finalize 对上了 就已经是刚决定那块的字段 interchangeable、已经知道本头哈希 interchangeable、已经四门已经结算 interchangeable」一件事：

1. **看见 Finalize 的 `height` / `time` 对上拟议块头 / 看见 Finalize height/time match header is not already newly decided block fields / 看见对上了 is not already FinalizeBlock Contains newly decided block fields 不是已经头字段对上余量 bundled（417） interchangeable / 已经是刚决定那块的字段 interchangeable / 已经 proposed block 字段 interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 已经四门已经结算 interchangeable / 已经跑过 Process interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（461 / 474 / 555 余量） interchangeable / 已经 newly decided block 字段 interchangeable / 已经 fill all fields interchangeable，也不是已经 FinalizeBlock Finalize match header not ProcessProposal match bundled（554 余量） interchangeable / 已经 ProcessProposal height/time match interchangeable / 已经 Process match header interchangeable，也不是已经 ProcessProposal Process match header not Finalize newly decided fields bundled（551 余量） interchangeable / 已经 FinalizeBlockRequest 字段 interchangeable / 已经 Process match header interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（552 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable。**  
   官方写：Finalize 的 height 和 time 对上拟议块的头。看见对上了，不是已经 Finalize 含刚决定那块的字段那种已经是刚决定那块的字段——417 bundled 第三件事常被写成「看见 Finalize 对上了就已经是刚决定那块的字段」，本页钉 Finalize height/time match header not already newly decided block fields 单句。看见 match header，不是已经 Finalize 含刚决定那块的字段（407 余量） interchangeable——407 钉 Contains newly decided block fields，本页钉 Finalize Usage match 边界。看见对上了，不是已经 FinalizeBlock Contains newly decided block fields（461 / 555 余量） interchangeable——555 钉 four gates settled，本页钉 Finalize Usage match not newly decided fields 单句。
2. **看见 Finalize height/time match header is not already know hash / 看见对上了 is not already FinalizeBlockRequest.hash 是已决块的哈希 不是已经头字段对上余量 bundled（417） interchangeable / 已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经 FinalizeBlockRequest.hash 是已决块的哈希 Request栏（428 余量） interchangeable / 已经 ProcessProposalRequest.hash interchangeable / 已经知道本头 interchangeable，也不是已经头字段对上余量 Process height/time match header not header fields bundled know hash bundled（417 第二件事 / 562 余量） interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经 Process hash interchangeable，也不是已经 FinalizeBlock Finalize match header not ProcessProposal match bundled（554 余量） interchangeable / 已经 know hash interchangeable / 已经 428 Finalize hash interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（552 余量） interchangeable / 已经 header fields bundled know hash interchangeable / 已经 Usage match interchangeable，也不是已经 Prepare 没有头哈希 bundled（311 余量） interchangeable / 已经 candidate 不是 ExecuteTxState interchangeable / 已经 Prepare 没有头哈希 interchangeable。**  
   官方把 Finalize Usage match header 和 FinalizeBlockRequest.hash 是已决块的哈希、头字段 bundled 知道本头哈希分开——417 bundled 常与 428 混成「对上了就已经知道本头哈希」，本页钉 Finalize height/time match header not already know hash 单句。看见 match header，不是已经 FinalizeBlockRequest.hash 是已决块的哈希（428 余量） interchangeable——428 钉 Finalize 请求 hash 单栏，本页钉 Finalize Usage match 边界。看见对上了，不是已经 Prepare 没有头哈希（311 余量） interchangeable——311 钉 Prepare 没有头哈希，本页钉 Finalize Usage match not know hash 单句。
3. **看见 Finalize height/time match header is not already four gates settled / 看见 Usage match is not already Finalize + Commit committed 不是已经头字段对上余量 bundled（417） interchangeable / 已经四门已经结算 interchangeable / 已经交差 interchangeable，也不是已经 Finalize 含刚决定那块的字段 bundled（407 余量） interchangeable / 已经跑过 Process interchangeable / 已经 ABCI 1.0 equiv interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields not already settled bundled（555 余量） interchangeable / 已经 ran Process interchangeable / 已经 Process ACCEPT switched working state interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（552 余量） interchangeable / 已经 ran Process interchangeable / 已经 360 Process guarantee interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（562 余量） interchangeable / 已经验过块头 interchangeable / 已经 Process follows Prepare interchangeable。**  
   官方把 Finalize Usage match header 和 Finalize + Commit 才进提交状态、四门已经结算分开——417 bundled 常与 407 混成「对上了就已经四门已经结算」，本页钉 Finalize height/time match header not already four gates settled 单句。看见 match header，不是已经 Finalize 含刚决定那块的字段（407 余量） interchangeable——407 钉 Contains newly decided block fields not four gates settled，本页钉 Finalize Usage match 边界。看见对上了，不是已经 CometBFT fill up all fields even if Prepare/Process passed（363 余量） interchangeable——363 钉 Finalize 又填一遍，本页钉 Finalize Usage match not settled 单句。

怎样写头字段对上余量、怎样对 height、怎样对 time 是规范里的做法，本页不抄。头字段对上余量 bundled（417）、Finalize 含刚决定那块的字段（407）、FinalizeBlock Finalize match header not ProcessProposal match（554）是另外那套，本页不抄。

## 官方为什么这样拆

- **Finalize height/time match header not already newly decided block fields ≠ 头字段对上余量 bundled interchangeable：** 官方把 Finalize Usage match 和 FinalizeBlock 含刚决定那块的字段分开。
- **Finalize height/time match header not already know hash ≠ 428 Finalize hash interchangeable：** 官方把 Finalize Usage match 和 FinalizeBlockRequest.hash 是已决块的哈希分开。
- **Finalize height/time match header not already four gates settled ≠ 407 four gates settled interchangeable：** 官方把 Finalize Usage match 和 Finalize + Commit 才进提交状态分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize height/time match header | 不是 already newly decided block fields | 不是 Finalize 含刚决定那块的字段（407） |
| Finalize Usage match header | 不是 already know hash | 不是 FinalizeBlockRequest.hash 是已决块的哈希（428） |
| Finalize match header | 不是 already four gates settled | 不是 FinalizeBlock Contains newly decided not settled（555） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 Finalize height/time match header not already newly decided fields 正式三事，必须分开 Finalize height/time match header 是不是 already newly decided block fields interchangeable / 407 Contains newly decided interchangeable / 461 newly decided interchangeable、Finalize height/time match header 是不是 already know hash interchangeable / 428 Finalize hash interchangeable / 311 Prepare no header hash interchangeable、Finalize height/time match header 是不是 already four gates settled interchangeable / 407 finfields interchangeable / 363 fill all fields interchangeable。可以跳过「看见 Finalize 对上了就已经是刚决定那块的字段 interchangeable」。不要另写怎样写头字段对上余量。

## 本页不抄

- 怎样写头字段对上余量、怎样对 height、怎样对 time。
- 自己是提议者会先走完 Prepare 那五步 not already no Process。那是不变量 561（417 item 1 余量）。
- Process 的 height / time 对上拟议块头 not already verified。那是不变量 562（417 item 2 余量）。
- FinalizeBlock Finalize match header not ProcessProposal match 三事。那是不变量 554（462 item 3 余量）。
- FinalizeBlock height/time match header not already verified 三事。那是不变量 552（462 item 1 余量）。
