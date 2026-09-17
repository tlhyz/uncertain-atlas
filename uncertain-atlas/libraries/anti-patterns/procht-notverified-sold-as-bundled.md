# 反模式：把 ProcessProposal height/time match header not already verified 正式三事卖成 ProcessProposal height/time 对上拟议块头 bundled / 已经验过块头 / 已经跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal height/time match header not already verified ≠ bundled](../../tracks/implementation/worked-example-procht-notverified-vs-bundled.md)。

## 卖法

- 「看见 Process 的 height / time 对上拟议块头 / 看见 height and time values match the values from the header 就已经验过块头 interchangeable / 已经 When 里先验块头 interchangeable / 已经 ProcessProposal height/time 对上拟议块头 bundled interchangeable。」
- 「看见 Process 对上了 就已经跑过 Process interchangeable / 已经 Process 调用之前就已经跑过 interchangeable / 已经 Process 通常紧跟 Prepare interchangeable。」
- 「看见 Process height/time match header 就已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable / 已经头字段对上余量 bundled interchangeable。」

## 为什么错

官方把 Usage 里 match the values from the header、When 里先验块头、头字段 bundled 知道本头哈希写成三件独立的实现事。把它们卖成 ProcessProposal height/time 对上拟议块头 bundled、已经验过块头、已经跑过 Process，会把 When verify header、already ran Process、header fields bundled know hash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal height/time match header not already verified 正式三事，必须分开 Process height/time match header not already verified、Process height/time match header not already ran Process、Process height/time match header not header fields bundled 三个名字，不要把它们卖成 ProcessProposal height/time 对上拟议块头 bundled / 已经验过块头 / 已经跑过 Process。

## 和相邻反模式

- [procht-sold-as-header](procht-sold-as-header.md) 是 454 bundled 三事专用，不是本页 Process height/time match header not already verified 单句边界。
- [proposetimeout-sold-as-process](proposetimeout-sold-as-process.md) 是 When 先验块头就已经跑过 Process，不是本页 Usage match not already verified 边界。
- [htmatch-sold-as-header](htmatch-sold-as-header.md) 是头字段对上余量 bundled，不是本页 Usage match not header fields bundled 边界。
