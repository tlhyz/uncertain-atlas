# 反模式：把 FinalizeBlock Finalize match header not ProcessProposal match 正式三事卖成 FinalizeBlock height/time 对上拟议块头 bundled / 已经 ProcessProposal match / 已经知道本头哈希

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock Finalize match header not ProcessProposal match ≠ bundled](../../tracks/implementation/worked-example-finht-notprocht-vs-bundled.md)。

## 卖法

- 「看见 Finalize height / time match proposed block header / 看见 match header 就已经 ProcessProposal height/time match interchangeable / 已经 ProcessProposal height/time 对上拟议块头 interchangeable / 已经 FinalizeBlock height/time 对上拟议块头 bundled interchangeable。」
- 「看见 Finalize match header 就已经知道本头哈希 interchangeable / 已经 FinalizeBlockRequest.hash 是已决块的哈希 interchangeable / 已经头字段对上余量 bundled interchangeable。」
- 「看见 Finalize match header 就已经 newly decided block 字段 interchangeable / 已经 FinalizeBlock 含刚决定那块字段 interchangeable / 已经 CometBFT fill up all fields even if Prepare/Process passed interchangeable。」

## 为什么错

官方把 Finalize Usage 里 Finalize height/time match proposed block header、ProcessProposal Usage 里 Process height/time match、FinalizeBlockRequest.hash / newly decided block 字段写成三件独立的实现事。把它们卖成 FinalizeBlock height/time 对上拟议块头 bundled、已经 ProcessProposal match、已经知道本头哈希，会把 Finalize vs Process match、Finalize match vs know hash、Finalize match vs newly decided block fields 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Finalize match header not ProcessProposal match 正式三事，必须分开 Finalize match header not ProcessProposal match、Finalize match header not know hash、Finalize match header not newly decided block fields 三个名字，不要把它们卖成 FinalizeBlock height/time 对上拟议块头 bundled / 已经 ProcessProposal match / 已经知道本头哈希。

## 和相邻反模式

- [finht-sold-as-proposed](finht-sold-as-proposed.md) 是 462 bundled 三事专用，不是本页 Finalize match header not ProcessProposal match 单句边界。
- [procht-notfinht-sold-as-bundled](procht-notfinht-sold-as-bundled.md) 是 Process match header not Finalize fields，不是本页 Finalize vs Process match 边界。
- [finht-notverified-sold-as-bundled](finht-notverified-sold-as-bundled.md) 是 Usage match not already verified，不是本页 Finalize match not ProcessProposal match 边界。
