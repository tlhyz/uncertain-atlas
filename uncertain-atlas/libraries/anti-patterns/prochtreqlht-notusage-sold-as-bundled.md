# 反模式：把 ProcessProposal Request height/time 栏 not Usage match 正式三事卖成 ProcessProposal height/time 对上拟议块头 bundled / 已经 Usage 那种对上了 / 已经验过票上时间

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal Request height/time 栏 not Usage match ≠ bundled](../../tracks/implementation/worked-example-prochtreqlht-notusage-vs-bundled.md)。

## 卖法

- 「看见 `ProcessProposalRequest.height` 是拟议块的高度 / `ProcessProposalRequest.time` 是拟议块的时间戳 / 看见填了 height / time 就已经 Usage 那种 match the values from the header interchangeable / 已经 Request height / time 栏 interchangeable / 已经 ProcessProposal height/time 对上拟议块头 bundled interchangeable。」
- 「看见填了 time 就已经 ExtendVoteRequest.time 那种已经验过票上 Timestamp interchangeable / 已经 304 Timestamp verified interchangeable。」
- 「看见有 height / time 栏就已经 Process 的 height / time 对上拟议块头 interchangeable / 已经头字段对上余量 bundled interchangeable / 已经 417 bundled interchangeable。」

## 为什么错

官方把 Request 表 height / time 栏描述、Usage 里 match the values from the header、票上 Timestamp 验过写成三件独立的实现事。把它们卖成 ProcessProposal height/time 对上拟议块头 bundled、已经 Usage 那种对上了、已经验过票上时间，会把 Request 栏 vs Usage match、Request time vs 304 Timestamp verified、Request 栏 vs 417 Process match bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Request height/time 栏 not Usage match 正式三事，必须分开 Request height/time 栏 not Usage match、Request height/time 栏 not verified vote timestamp、Request height/time 栏 not Process height/time match bundled 三个名字，不要把它们卖成 ProcessProposal height/time 对上拟议块头 bundled / 已经 Usage 那种对上了 / 已经验过票上时间。

## 和相邻反模式

- [procht-sold-as-header](procht-sold-as-header.md) 是 454 bundled 三事专用，不是本页 Request height / time 栏 not Usage match 单句边界。
- [procht-notverified-sold-as-bundled](procht-notverified-sold-as-bundled.md) 是 Usage match not already verified，不是本页 Request 栏 vs Usage match 边界。
- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 Process 请求栏单栏 bundled，不是本页 Request height / time 栏 not Usage match 边界。
