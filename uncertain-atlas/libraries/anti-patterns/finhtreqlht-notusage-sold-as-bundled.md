# 反模式：把 FinalizeBlock Request height/time 栏 not Usage match 正式三事卖成 FinalizeBlock height/time 对上拟议块头 bundled / 已经 Usage 那种对上了 / 已经是 ProcessProposalRequest.height / time interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock Request height/time 栏 not Usage match ≠ bundled](../../tracks/implementation/worked-example-finhtreqlht-notusage-vs-bundled.md)。

## 卖法

- 「看见 `FinalizeBlockRequest.height` 是已决块的高度 / `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 height / time 就已经 Usage 那种 match the values from the header interchangeable / 已经 Request height / time 栏 interchangeable / 已经 FinalizeBlock height/time 对上拟议块头 bundled interchangeable。」
- 「看见填了 time 就已经 ExtendVoteRequest.time 那种已经验过票上 Timestamp interchangeable / 已经 304 Timestamp verified interchangeable。」
- 「看见有 height / time 栏就已经 ProcessProposalRequest.height / time interchangeable / 已经 ProcessProposal height/time 对上拟议块头 interchangeable / 已经 454 Process match interchangeable。」

## 为什么错

官方把 Finalize Request 表 height / time 栏描述、Usage 里 match the values from the header、ProcessProposalRequest.height / time 栏描述写成三件独立的实现事。把它们卖成 FinalizeBlock height/time 对上拟议块头 bundled、已经 Usage 那种对上了、已经是 ProcessProposalRequest.height / time interchangeable，会把 Request 栏 vs Usage match、Request time vs 304 Timestamp verified、Finalize Request vs Process Request 栏三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Request height/time 栏 not Usage match 正式三事，必须分开 Request height/time 栏 not Usage match、Request height/time 栏 not verified vote timestamp、Request height/time 栏 not ProcessProposalRequest height/time interchangeable 三个名字，不要把它们卖成 FinalizeBlock height/time 对上拟议块头 bundled / 已经 Usage 那种对上了 / 已经是 ProcessProposalRequest.height / time interchangeable。

## 和相邻反模式

- [finht-sold-as-proposed](finht-sold-as-proposed.md) 是 462 bundled 三事专用，不是本页 Request height / time 栏 not Usage match 单句边界。
- [finht-notverified-sold-as-bundled](finht-notverified-sold-as-bundled.md) 是 Usage match not already verified，不是本页 Request 栏 vs Usage match 边界。
- [prochtreqlht-notusage-sold-as-bundled](prochtreqlht-notusage-sold-as-bundled.md) 是 Process Request height/time 栏 not Usage match，不是本页 Finalize Request 栏边界。
