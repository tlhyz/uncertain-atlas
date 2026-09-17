# 反模式：把 ProcessProposal Process match header not Finalize newly decided fields 正式三事卖成 ProcessProposal height/time 对上拟议块头 bundled / 已经 FinalizeBlockRequest 字段 / 已经 Finalize height/time match

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal Process match header not Finalize newly decided fields ≠ bundled](../../tracks/implementation/worked-example-procht-notfinht-vs-bundled.md)。

## 卖法

- 「看见 Process height / time match proposed block header / 看见 match header 就已经是 FinalizeBlockRequest 刚决定那块的字段 interchangeable / 已经 decided_last_commit interchangeable / 已经 ProcessProposal height/time 对上拟议块头 bundled interchangeable。」
- 「看见 Process match header 就已经 Finalize height/time match interchangeable / 已经 FinalizeBlockRequest.height 是已决块的高度 interchangeable / 已经 FinalizeBlockRequest.time 是已决块的时间戳 interchangeable。」
- 「看见 Process match header 就已经 CometBFT fill up all fields even if Prepare/Process passed interchangeable / 已经又填一遍 newly decided block 字段 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable。」

## 为什么错

官方把 Process Usage 里 Process height/time match proposed block header、FinalizeBlockRequest 刚决定那块的字段、Finalize height/time match 写成三件独立的实现事。把它们卖成 ProcessProposal height/time 对上拟议块头 bundled、已经 FinalizeBlockRequest 字段、已经 Finalize height/time match，会把 Process match vs Finalize newly decided fields、Process match vs Finalize height/time match、Process match vs fill all fields again 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Process match header not Finalize newly decided fields 正式三事，必须分开 Process match header not Finalize newly decided fields、Process match header not Finalize height/time match、Process match header not fill all fields again 三个名字，不要把它们卖成 ProcessProposal height/time 对上拟议块头 bundled / 已经 FinalizeBlockRequest 字段 / 已经 Finalize height/time match。

## 和相邻反模式

- [procht-sold-as-header](procht-sold-as-header.md) 是 454 bundled 三事专用，不是本页 Process match header not Finalize newly decided fields 单句边界。
- [procfull-notfinfields-sold-as-bundled](procfull-notfinfields-sold-as-bundled.md) 是 Contains all information not Finalize fields，不是本页 Process height/time match header 单句边界。
- [finht-sold-as-proposed](finht-sold-as-proposed.md) 是 Finalize height/time match bundled，不是本页 Process match header not Finalize height/time match 边界。
