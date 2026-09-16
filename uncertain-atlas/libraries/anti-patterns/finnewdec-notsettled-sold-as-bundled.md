# 反模式：把 FinalizeBlock Contains newly decided block fields not already settled 正式三事（474 余量）卖成 FinalizeBlock Contains newly decided block fields bundled / 已经四门已经结算 / 已经跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock Contains newly decided block fields not already settled ≠ bundled（474）](../../tracks/implementation/worked-example-finnewdec-notsettled-vs-bundled.md)。

## 卖法

- 「看见 FinalizeBlock Contains the fields of the newly decided block / 看见含刚决定那块的字段 就已经四门已经结算 interchangeable / 已经 FinalizeBlock Contains newly decided block fields bundled interchangeable。」
- 「看见含刚决定那块的字段 就已经跑过 Process interchangeable / 已经交差 interchangeable。」
- 「看见 newly decided block 就已经 Process 回了 Accept 就换工作状态 interchangeable / 已经 candidate not committed interchangeable。」

## 为什么错

官方把 FinalizeBlock Usage 第一句 Contains the fields of the newly decided block 和四门已经结算、Process 跑过、Process 回了 Accept 就换工作状态写成三件独立的实现事。把它们卖成 FinalizeBlock Contains newly decided block fields bundled、已经四门已经结算、已经跑过 Process，会把 Contains not settled、Contains not ran Process、Contains not ACCEPT switched 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Contains newly decided block fields not already settled 正式三事（474 余量），必须分开 Contains not four gates settled、Contains not ran Process、Contains not Process ACCEPT switched 三个名字，不要把它们卖成 FinalizeBlock Contains newly decided block fields bundled / 已经四门已经结算 / 已经跑过 Process。

## 和相邻反模式

- [finnewdec-sold-as-settled](finnewdec-sold-as-settled.md) 是 474 bundled 三事专用，不是本页 Contains not settled 单句边界。
- [finnewfields-notsettled-sold-as-bundled](finnewfields-notsettled-sold-as-bundled.md) 是 555 461 bundled item 1 余量，不是本页 474 bundled item 1 边界。
- [finnewfields-notprocfull-sold-as-bundled](finnewfields-notprocfull-sold-as-bundled.md) 是 556 461 bundled item 2 余量，不是本页 Contains Usage 边界。
