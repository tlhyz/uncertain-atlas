# 例：看见 Process height / time match proposed block header / 看见 match header is not already FinalizeBlockRequest newly decided block fields / 看见 Process 这边 match is not already Finalize height/time match interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable

**层次**：实现 / ProcessProposal Process match header not Finalize newly decided fields 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process match header not Finalize newly decided fields 不是 ProcessProposal height/time 对上拟议块头 bundled interchangeable / 不是已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 不是已经 Finalize height/time match interchangeable」，不是 ProcessProposal height/time 对上拟议块头 bundled（454），也不是 FinalizeBlock 含刚决定那块字段 bundled（461 / 474），也不是 Process height/time match header not already verified（550）。不要另写怎样对 height / time。

## 官方三件事

规范把 Process Usage 里 Process height/time match proposed block header、FinalizeBlockRequest 刚决定那块的字段、Finalize height/time match 分开写成三件独立的实现事，不是「看见 Process match header 就已经是 FinalizeBlockRequest 字段 interchangeable、已经 Finalize height/time match interchangeable、已经 newly decided block 字段 interchangeable」一件事：

1. **看见 Process height / time match proposed block header / 看见 match header is not already FinalizeBlockRequest newly decided block fields / 看见 Process 这边 match is not already ProcessProposal height/time 对上拟议块头 bundled（454） interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 decided_last_commit interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（461 / 474 余量） interchangeable / 已经 newly decided block 字段 interchangeable / 已经跑过 Process interchangeable，也不是已经 FinalizeBlock 含刚决定那块字段 bundled（474 余量） interchangeable / 已经 proposed block 字段 interchangeable / 已经 ProcessProposal Contains all information interchangeable，也不是已经 ProcessProposal Contains all information not Finalize newly decided fields bundled（549 余量） interchangeable / 已经 FinalizeBlockRequest 字段 interchangeable / 已经 proposed/decided interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（550 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 ProcessProposal Request height/time 栏 not Usage match bundled（551 余量） interchangeable / 已经 Usage match interchangeable / 已经 Request height / time 栏 interchangeable。**  
   官方写：The height and time values match the values from the header of the proposed block。看见 Process 这边 match，不是已经 FinalizeBlock Usage 里 Finalize 的 height / time 对上拟议块头那种已经是刚决定那块的字段——454 bundled 第三件事常被写成「看见 Process match header 就已经是 FinalizeBlockRequest 字段」，本页钉 Process match header not Finalize newly decided fields 单句。看见 match header，不是已经 FinalizeBlock Contains newly decided block fields（461 / 474 余量） interchangeable——461 钉 newly decided block 字段，本页钉 Process Usage match 边界。看见 Process 这边 match，不是已经 ProcessProposal Contains all information not Finalize newly decided fields（549 余量） interchangeable——549 钉 Contains all information vs Finalize fields，本页钉 Process height/time match header 单句。
2. **看见 Process match header is not already Finalize height/time match interchangeable / 看见拟议块头字段对上 is not already FinalizeBlockRequest.height 是已决块的高度 / FinalizeBlockRequest.time 是已决块的时间戳 interchangeable 不是已经 ProcessProposal height/time 对上拟议块头 bundled（454） interchangeable / 已经 Finalize height/time match interchangeable / 已经 FinalizeBlockRequest 刚决定那块的字段 interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 余量） interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable，也不是已经头字段对上余量 bundled（417 余量） interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经 Finalize height/time match interchangeable，也不是已经 Finalize 请求余栏 bundled（428 余量） interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable / 已经 ProcessProposalRequest.hash interchangeable，也不是已经 Prepare 请求余栏 bundled（424 余量） interchangeable / 已经 local_last_commit interchangeable / 已经 proposed_last_commit interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（550 余量） interchangeable / 已经 Usage match interchangeable / 已经 Request height / time 栏 interchangeable。**  
   官方把 Process 和 Finalize 的 height/time match 分开——454 bundled 常与 462 混成「Process match header = Finalize height/time match interchangeable」，本页钉 Process match header not Finalize height/time match 单句。看见 Process 这边 match，不是已经 FinalizeBlock height/time 对上拟议块头（462 余量） interchangeable——462 钉 Finalize match header，本页钉 Process Usage match 边界。看见 match header，不是已经 FinalizeBlockRequest.height 是已决块的高度 / time 是已决块的时间戳（428 余量） interchangeable——428 钉 Finalize 请求 hash/height/time 单栏，本页钉 Process vs Finalize match 单句。
3. **看见 Process match header is not CometBFT fill up all fields even if Prepare/Process passed / 看见 Process 这边 match is not already newly decided block fields filled again 不是已经 ProcessProposal height/time 对上拟议块头 bundled（454） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 FinalizeBlock Contains newly decided block fields bundled（461 余量） interchangeable / 已经 newly decided block 字段 interchangeable / 已经 proposed block interchangeable，也不是已经 ProcessProposal Contains all information not Finalize newly decided fields bundled（549 余量） interchangeable / 已经 FinalizeBlockRequest 字段 interchangeable / 已经 only txs enough interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（550 余量） interchangeable / 已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经 ProcessProposal Request height/time 栏 not Usage match bundled（551 余量） interchangeable / 已经 Usage match interchangeable / 已经 Request height / time 栏 interchangeable。**  
   官方把 Process Usage match header 和 Finalize 又填 newly decided block 字段分开——454 bundled 常与 363 混成「Process match header = 已经又填一遍 Finalize 字段」，本页钉 Process match header not fill all fields again 单句。看见 Process 这边 match，不是已经 CometBFT fill up all fields even if Prepare/Process passed（363 余量） interchangeable——363 钉 Finalize 又填一遍，本页钉 Process vs Finalize fields 边界。看见 match header，不是已经 FinalizeBlock 含刚决定那块字段（461 余量） interchangeable——461 钉 newly decided block 字段，本页钉 Process Usage match 单句。

怎样对 height、怎样对 time、怎样和 Finalize 请求栏对齐 是规范里的做法，本页不抄。ProcessProposal height/time 对上拟议块头 bundled（454）、FinalizeBlock 含刚决定那块字段 bundled（461 / 474）、CometBFT fill up all fields（363）是另外那套，本页不抄。

## 官方为什么这样拆

- **Process match header not Finalize newly decided fields ≠ ProcessProposal height/time 对上拟议块头 bundled interchangeable：** 官方把 Process Usage match 和 FinalizeBlockRequest 刚决定那块的字段分开。
- **Process match header not Finalize height/time match ≠ 462 Finalize match interchangeable：** 官方把 Process 和 Finalize 的 height/time match 分开。
- **Process match header not fill all fields again ≠ 363 fill all fields interchangeable：** 官方把 Process Usage match 和 Finalize 又填 newly decided block 字段分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process match header | 不是 Finalize newly decided fields | 不是 Contains all information not Finalize fields（549） |
| Process match header | 不是 Finalize height/time match | 不是 FinalizeBlock height/time match（462） |
| Process match header | 不是 fill all fields again | 不是 CometBFT fill up all fields（363） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Process match header not Finalize newly decided fields 正式三事，必须分开 Process match header 是不是 FinalizeBlockRequest newly decided fields interchangeable / 461 newly decided interchangeable / 549 Contains all information interchangeable、Process match header 是不是 Finalize height/time match interchangeable / 462 Finalize match interchangeable / 428 Finalize hash interchangeable、Process match header 是不是 fill all fields again interchangeable / 363 fill all fields interchangeable。可以跳过「看见 Process match header 就已经是 Finalize 字段 interchangeable」。不要另写怎样对 height / time。

## 本页不抄

- 怎样对 height、怎样对 time、怎样和 Finalize 请求栏对齐。
- Process height/time match header not already verified。那是不变量 550。
- Request height/time 栏 not Usage match。那是不变量 551。
- 头字段对上余量 bundled 三事。那是不变量 417。
