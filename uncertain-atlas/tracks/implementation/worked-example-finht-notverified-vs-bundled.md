# 例：看见 Finalize 的 `height` / `time` 对上拟议块头 / 看见 height and time values match the values from the header is not already verified block header / 看见对上了 is not already ran Process 不是已经 FinalizeBlock height/time 对上拟议块头 bundled interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable

**层次**：实现 / FinalizeBlock height/time match header not already verified 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize height/time match header not already verified 不是 FinalizeBlock height/time 对上拟议块头 bundled interchangeable / 不是已经验过块头 interchangeable / 不是已经跑过 Process interchangeable」，不是 FinalizeBlock height/time 对上拟议块头 bundled（462），也不是收到带上头的提案会先验块头（416），也不是头字段对上余量 bundled（417）。不要另写怎样对 height / time。

## 官方三件事

规范把 FinalizeBlock Usage 里 height and time values match the values from the header 和 When 里先验块头、已经跑过 Process、头字段 bundled 分开写成三件独立的实现事，不是「看见 Finalize 对上了就已经验过块头 interchangeable、已经跑过 Process interchangeable、已经知道本头哈希 interchangeable」一件事：

1. **看见 Finalize 的 `height` / `time` 对上拟议块头 / 看见 height and time values match the values from the header is not already verified block header / 看见对上了 is not already When verify header 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经收到带上头的 Proposal 会先验块头 bundled（416 余量） interchangeable / 已经验过块头 interchangeable / 已经跑过 Process interchangeable，也不是已经 ProcessProposal When basic checks then async bundled（354 余量） interchangeable / 已经 will not be able to reject interchangeable / 已经 async 了还能 Reject interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 第二件事 / 554 余量） interchangeable / 已经 Usage 那种 match the values from the header interchangeable / 已经 Request height / time 栏 interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 第三件事 / 555 余量） interchangeable / 已经 ProcessProposal height/time match interchangeable / 已经 ProcessProposal height/time 对上拟议块头 interchangeable。**  
   官方写：The height and time values match the values from the header of the proposed block。看见对上了，不是已经 When 里收到带上头的 Proposal 会先验块头那种已经验过——462 bundled 常被写成「看见 Finalize 对上了就已经验过块头」，本页钉 Finalize height/time match header not already verified 单句。看见 match header，不是已经收到带上头的 Proposal 会先验块头（416 余量） interchangeable——416 钉 When 先验块头，本页钉 Finalize Usage match 边界。看见对上了，不是已经 Process When basic checks then async（354 余量） interchangeable——354 钉 When async path，本页钉 Finalize Usage match not verified 单句。
2. **看见 Finalize height/time match header is not already ran Process / 看见 Usage match 不是已经 Process 调用之前就已经跑过 Process 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经跑过 Process interchangeable / 已经 Process 调用之前就已经跑过 interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经每个验证者都跑过 Process interchangeable / 已经至少一名非拜占庭验证者跑过 Process interchangeable，也不是已经 Process 通常紧跟 Prepare bundled（351 余量） interchangeable / 已经不用再 Process interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（550 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 第二件事 / 554 余量） interchangeable / 已经 Request height / time 栏 interchangeable / 已经 Usage match interchangeable。**  
   官方把 Finalize Usage 里 match header 和 Process 调用之前就已经跑过 Process 分开——462 bundled 常与 360 混成「Finalize 对上了就已经跑过 Process」，本页钉 Finalize height/time match header not already ran Process 单句。看见 match header，不是已经 Finalize 时的 Process 保证（360 余量） interchangeable——360 钉至少一名非拜占庭验证者跑过 Process，本页钉 Finalize Usage match 边界。看见对上了，不是已经 Process 通常紧跟 Prepare（351 余量） interchangeable——351 钉 Process follows Prepare，本页钉 Finalize Usage match not ran Process 单句。
3. **看见 Finalize height/time match header is not header fields bundled know hash / 看见对上了不是已经知道本头哈希 不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462） interchangeable / 已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable，也不是已经头字段对上余量 bundled（417 余量） interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经 Finalize height/time match interchangeable，也不是已经 FinalizeBlockRequest.hash 是已决块的哈希 Request栏（428 余量） interchangeable / 已经 ProcessProposalRequest.hash interchangeable / 已经知道本头 interchangeable，也不是已经 ProcessProposal height/time match header not already verified bundled（550 余量） interchangeable / 已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable，也不是已经 FinalizeBlock height/time 对上拟议块头 bundled（462 第二件事 / 554 余量） interchangeable / 已经 Usage match interchangeable / 已经 Request height / time 栏 interchangeable。**  
   官方把 Finalize Usage match header 和头字段 bundled 知道本头哈希分开——462 bundled 常与 417 混成「对上了就已经知道本头哈希」，本页钉 Finalize height/time match header not header fields bundled 单句。看见 match header，不是已经头字段对上余量 bundled（417 余量） interchangeable——417 钉 Prepare/Finalize height/time match bundled，本页钉 Finalize Usage match 边界。看见对上了，不是已经 FinalizeBlockRequest.hash 是已决块的哈希（428 余量） interchangeable——428 钉 Finalize 请求 hash 单栏，本页钉 Finalize Usage match not know hash 单句。

怎样对 height、怎样对 time、怎样和 Process 请求栏对齐 是规范里的做法，本页不抄。FinalizeBlock height/time 对上拟议块头 bundled（462）、收到带上头的提案会先验块头（416）、头字段对上余量 bundled（417）是另外那套，本页不抄。

## 官方为什么这样拆

- **Finalize height/time match header not already verified ≠ FinalizeBlock height/time 对上拟议块头 bundled interchangeable：** 官方把 Finalize Usage match 和 When 里先验块头分开。
- **Finalize height/time match header not already ran Process ≠ Finalize Process guarantee interchangeable：** 官方把 Finalize Usage match 和 Process 调用之前就已经跑过 Process 分开。
- **Finalize height/time match header not header fields bundled ≠ 417 know hash interchangeable：** 官方把 Finalize Usage match 和头字段 bundled 知道本头哈希分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize height/time match header | 不是 already verified block header | 不是 When verify header（416） |
| Finalize Usage match header | 不是 already ran Process | 不是 Finalize Process guarantee（360） |
| Finalize match header | 不是 header fields bundled know hash | 不是头字段对上余量 bundled（417） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock height/time match header not already verified 正式三事，必须分开 Finalize height/time match header 是不是 already verified block header interchangeable / 416 When verify interchangeable、Finalize height/time match header 是不是 already ran Process interchangeable / 360 Process guarantee interchangeable、Finalize height/time match header 是不是 header fields bundled know hash interchangeable / 417 bundled interchangeable。可以跳过「看见 Finalize 对上了就已经验过块头 interchangeable」。不要另写怎样对 height / time。

## 本页不抄

- 怎样对 height、怎样对 time、怎样和 Process 请求栏对齐。
- Request height / time 栏 ≠ Usage 那种 match the values from the header。那是不变量 554（462 item 2 余量）。
- Finalize match header ≠ ProcessProposal height/time match interchangeable。那是不变量 555（462 item 3 余量）。
- 收到带上头的提案会先验块头。那是不变量 416。
