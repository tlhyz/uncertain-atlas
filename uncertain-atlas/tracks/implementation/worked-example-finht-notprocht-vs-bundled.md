# 例：看见 Finalize height / time match proposed block header / 看见 match header is not already ProcessProposal height/time match interchangeable / 看见 Finalize 这边 match is not already ProcessProposal height/time 对上拟议块头 bundled interchangeable / 已经 ProcessProposal height/time match interchangeable

**层次**：实现 / FinalizeBlock Finalize match header not ProcessProposal match 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize match header not ProcessProposal match 不是 FinalizeBlock height/time 对上拟议块头 bundled interchangeable / 不是已经 ProcessProposal height/time match interchangeable / 不是已经知道本头哈希 interchangeable」，不是 FinalizeBlock height/time 对上拟议块头 bundled（462），也不是 ProcessProposal Process match header not Finalize newly decided fields（551），也不是 Finalize height/time match header not already verified（552）。不要另写怎样对 height / time。

## 官方三件事

规范把 Finalize Usage 里 Finalize height/time match proposed block header、ProcessProposal Usage 里 Process height/time match、FinalizeBlockRequest.hash / newly decided block 字段分开写成三件独立的实现事，不是「看见 Finalize match header 就已经是 ProcessProposal height/time match interchangeable、已经知道本头哈希 interchangeable、已经 newly decided block 字段 interchangeable」一件事：

1. **看见 Finalize height / time match proposed block header / 看见 match header is not already ProcessProposal height/time match interchangeable / 看见 Finalize 这边 match is not already FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经 ProcessProposal height/time match interchangeable / 已经 ProcessProposal height/time 对上拟议块头 interchangeable，也不是已经 ProcessProposal height/time 对上拟议块头 bundled（454 余量） interchangeable / 已经 Process height/time match header interchangeable / 已经头字段对上余量 bundled interchangeable，也不是已经 ProcessProposal Process match header not Finalize newly decided fields bundled（551 余量） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 Process match header interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（552 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 FinalizeBlock Request height/time 栏 not Usage match bundled（553 余量） interchangeable / 已经 Usage match interchangeable / 已经 Request height / time 栏 interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（549 余量） interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经 When 里先验块头 interchangeable。**  
   官方写：The height and time values match the values from the header of the proposed block。看见 Finalize 这边 match，不是已经 ProcessProposal Usage 里 Process 的 height / time 对上拟议块头（454）就已经是同一句 interchangeable——462 bundled 第三件事常被写成「看见 Finalize match header 就已经是 ProcessProposal match interchangeable」，本页钉 Finalize match header not ProcessProposal height/time match 单句。看见 match header，不是已经 ProcessProposal Process match header not Finalize newly decided fields（551 余量） interchangeable——551 钉 Process vs Finalize newly decided fields，本页钉 Finalize Usage match 边界。看见 Finalize 这边 match，不是已经 ProcessProposal height/time 对上拟议块头 bundled（454 余量） interchangeable——454 钉 Process Usage match，本页钉 Finalize vs Process match 单句。
2. **看见 Finalize match header is not already know hash / 看见拟议块头字段对上 is not already FinalizeBlockRequest.hash 是已决块的哈希 interchangeable 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经头字段对上余量 bundled（417 余量） interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经 Finalize height/time match interchangeable，也不是已经 FinalizeBlockRequest.hash 是已决块的哈希 Request栏（428 余量） interchangeable / 已经 ProcessProposalRequest.hash interchangeable / 已经知道本头 interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（549 余量） interchangeable / 已经 header fields bundled know hash interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（552 余量） interchangeable / 已经 Usage match interchangeable / 已经 Request height / time 栏 interchangeable，也不是已经 ProcessProposal height/time 对上拟议块头 bundled（454 余量） interchangeable / 已经 Process height/time match header interchangeable / 已经 311 Prepare no header hash interchangeable。**  
   官方把 Finalize Usage match header 和 FinalizeBlockRequest.hash 是已决块的哈希、头字段 bundled 知道本头哈希分开——462 bundled 常与 428 混成「对上了就已经知道本头哈希」，本页钉 Finalize match header not know hash 单句。看见 match header，不是已经头字段对上余量 bundled（417 余量） interchangeable——417 钉 Prepare/Finalize height/time match bundled，本页钉 Finalize Usage match 边界。看见拟议块头字段对上，不是已经 FinalizeBlockRequest.hash 是已决块的哈希（428 余量） interchangeable——428 钉 Finalize 请求 hash 单栏，本页钉 Finalize match not know hash 单句。
3. **看见 Finalize match header is not already newly decided block fields interchangeable / 看见 Finalize 这边 match is not already FinalizeBlock Contains newly decided block fields bundled 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经 newly decided block 字段 interchangeable / 已经 proposed block 字段 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（461 / 474 余量） interchangeable / 已经 newly decided block 字段 interchangeable / 已经跑过 Process interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 ProcessProposal Process match header not Finalize newly decided fields bundled（551 余量） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 Process match header interchangeable，也不是已经 ProcessProposal Contains all information not Finalize newly decided fields bundled（548 余量） interchangeable / 已经 FinalizeBlockRequest 字段 interchangeable / 已经 only txs enough interchangeable，也不是已经 FinalizeBlock height/time match header not already verified bundled（552 余量） interchangeable / 已经 header fields bundled know hash interchangeable / 已经 Prepare 没有头哈希 interchangeable。**  
   官方把 Finalize Usage match header 和 FinalizeBlock 含刚决定那块字段 bundled 分开——462 bundled 常与 461 混成「看见 Finalize match header 就已经是 newly decided block 字段 interchangeable」，本页钉 Finalize match header not newly decided block fields 单句。看见 match header，不是已经 FinalizeBlock Contains newly decided block fields（461 / 474 余量） interchangeable——461 钉 newly decided block 字段，本页钉 Finalize Usage match 边界。看见 Finalize 这边 match，不是已经 CometBFT fill up all fields even if Prepare/Process passed（363 余量） interchangeable——363 钉 Finalize 又填一遍，本页钉 Finalize match vs newly decided fields 单句。

怎样对 height、怎样对 time、怎样和 Process 请求栏对齐 是规范里的做法，本页不抄。FinalizeBlock height/time 对上拟议块头 bundled（462）、ProcessProposal Process match header not Finalize newly decided fields（551）、FinalizeBlock 含刚决定那块字段 bundled（461 / 474）是另外那套，本页不抄。

## 官方为什么这样拆

- **Finalize match header not ProcessProposal match ≠ FinalizeBlock height/time 对上拟议块头 bundled interchangeable：** 官方把 Finalize 和 Process 的 height/time match 分开。
- **Finalize match header not know hash ≠ 428 Finalize hash interchangeable：** 官方把 Finalize Usage match 和 FinalizeBlockRequest.hash 是已决块的哈希分开。
- **Finalize match header not newly decided block fields ≠ 461 newly decided interchangeable：** 官方把 Finalize Usage match 和 FinalizeBlock 含刚决定那块字段分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize match header | 不是 ProcessProposal height/time match | 不是 ProcessProposal height/time 对上拟议块头（454） |
| Finalize match header | 不是 know hash | 不是 FinalizeBlockRequest.hash 是已决块的哈希（428） |
| Finalize match header | 不是 newly decided block fields | 不是 FinalizeBlock 含刚决定那块字段（461） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Finalize match header not ProcessProposal match 正式三事，必须分开 Finalize match header 是不是 ProcessProposal height/time match interchangeable / 454 Process match interchangeable / 551 Process not Finalize fields interchangeable、Finalize match header 是不是 know hash interchangeable / 428 Finalize hash interchangeable / 417 bundled interchangeable、Finalize match header 是不是 newly decided block fields interchangeable / 461 newly decided interchangeable / 363 fill all fields interchangeable。可以跳过「看见 Finalize match header 就已经是 ProcessProposal match interchangeable」。不要另写怎样对 height / time。

## 本页不抄

- 怎样对 height、怎样对 time、怎样和 Process 请求栏对齐。
- Finalize height/time match header not already verified。那是不变量 552。
- Finalize Request height/time 栏 not Usage match。那是不变量 553。
- ProcessProposal Process match header not Finalize newly decided fields。那是不变量 551。
