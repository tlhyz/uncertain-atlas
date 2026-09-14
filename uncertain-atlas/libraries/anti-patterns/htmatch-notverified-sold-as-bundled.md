# 反模式：把头字段对上余量 Process height/time match header not already verified 正式三事卖成头字段对上余量 bundled / 已经验过块头 / 已经跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[头字段对上余量 Process height/time match header not already verified ≠ bundled](../../tracks/implementation/worked-example-htmatch-notverified-vs-bundled.md)。

## 卖法

- 「看见 Process 的 height / time 对上拟议块头 / 看见对上了 就已经验过块头 interchangeable / 已经头字段对上余量 bundled interchangeable。」
- 「看见 Process 对上了 就已经跑过 Process interchangeable / 已经 Process follows Prepare interchangeable。」
- 「看见 Process 对上了 就已经知道本头哈希 interchangeable / 已经 Prepare 没有头哈希 interchangeable。」

## 为什么错

官方把 Process Usage 里 height 和 time 对上拟议块的头、When 里先验块头、Process 调用之前就已经跑过 Process、头字段 bundled 知道本头哈希写成三件独立的实现事。把它们卖成头字段对上余量 bundled、已经验过块头、已经跑过 Process，会把 Process match not verified、Process match not ran Process、Process match not know hash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 Process height/time match header not already verified 正式三事，必须分开 Process match not verified、Process match not ran Process、Process match not header fields bundled know hash 三个名字，不要把它们卖成头字段对上余量 bundled / 已经验过块头 / 已经跑过 Process。

## 和相邻反模式

- [htmatch-sold-as-header](htmatch-sold-as-header.md) 是 417 bundled 三事专用，不是本页 Process match not verified 单句边界。
- [procht-notverified-sold-as-bundled](procht-notverified-sold-as-bundled.md) 是 549 ProcessProposal height/time match not verified，不是本页 417 bundled Process match 边界。
- [htmatch-notproprocess-sold-as-bundled](htmatch-notproprocess-sold-as-bundled.md) 是 561 proposer prepare not no Process，不是本页 Process Usage match 边界。
