# 反模式：把头字段对上余量 Finalize height/time match header not already newly decided fields 正式三事卖成头字段对上余量 bundled / 已经是刚决定那块的字段 / 已经知道本头哈希

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[头字段对上余量 Finalize height/time match header not already newly decided fields ≠ bundled](../../tracks/implementation/worked-example-htmatch-notnewdec-vs-bundled.md)。

## 卖法

- 「看见 Finalize 的 height / time 对上拟议块头 / 看见对上了 就已经是刚决定那块的字段 interchangeable / 已经头字段对上余量 bundled interchangeable。」
- 「看见 Finalize 对上了 就已经知道本头哈希 interchangeable / 已经 FinalizeBlockRequest.hash interchangeable。」
- 「看见 Finalize 对上了 就已经四门已经结算 interchangeable / 已经交差 interchangeable。」

## 为什么错

官方把 Finalize Usage 里 height 和 time 对上拟议块的头、FinalizeBlock 含刚决定那块的字段、FinalizeBlockRequest.hash 是已决块的哈希、Finalize + Commit 才进提交状态写成三件独立的实现事。把它们卖成头字段对上余量 bundled、已经是刚决定那块的字段、已经知道本头哈希，会把 Finalize match not newly decided fields、Finalize match not know hash、Finalize match not four gates settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 Finalize height/time match header not already newly decided fields 正式三事，必须分开 Finalize match not newly decided block fields、Finalize match not know hash、Finalize match not four gates settled 三个名字，不要把它们卖成头字段对上余量 bundled / 已经是刚决定那块的字段 / 已经知道本头哈希。

## 和相邻反模式

- [htmatch-sold-as-header](htmatch-sold-as-header.md) 是 417 bundled 三事专用，不是本页 Finalize match not newly decided fields 单句边界。
- [finnewdec-sold-as-settled](finnewdec-sold-as-settled.md) 是 407 Finalize 含刚决定那块的字段，不是本页 417 bundled Finalize Usage match 边界。
- [htmatch-notverified-sold-as-bundled](htmatch-notverified-sold-as-bundled.md) 是 562 Process match not verified，不是本页 417 bundled Finalize match 边界。
- [finht-notprocht-sold-as-bundled](finht-notprocht-sold-as-bundled.md) 是 554 Finalize match not ProcessProposal match，不是本页 417 item 3 余量边界。
