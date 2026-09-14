# 反模式：把 Finalize 含刚决定那块的字段 not already settled 正式三事（407 余量）卖成 Finalize 字段余量 bundled / 已经四门已经结算 / 已经跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Finalize 含刚决定那块的字段 not already settled ≠ bundled（407）](../../tracks/implementation/worked-example-finfields-notsettled-vs-bundled.md)。

## 卖法

- 「看见 Finalize 含刚决定那块的字段 / 看见填了字段 就已经四门已经结算 interchangeable / 已经 ABCI 1.0 三步 interchangeable。」
- 「看见填了字段 就已经 Prepare / Process 同一套字段就已经跑过 Process interchangeable / 已经 Process 调用之前就已经跑过 interchangeable。」
- 「看见填了字段 就已经 Contains newly decided block fields bundled interchangeable / 已经 newly decided block 字段 interchangeable。」

## 为什么错

官方把 `FinalizeBlock` 含刚决定那块的字段、四门已经结算、Process 跑过、Contains newly decided 对象边界 写成三件独立的实现事。把它们卖成 Finalize 字段余量 bundled、已经四门已经结算、已经跑过 Process，会把 not four gates settled、not ran Process、not Contains bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 含刚决定那块的字段 not already settled 正式三事（407 余量），必须分开 not four gates settled、not ran Process、not Contains bundled 三个名字，不要把它们卖成 Finalize 字段余量 bundled / 已经四门已经结算 / 已经跑过 Process。

## 和相邻反模式

- [finfields-sold-as-equiv](finfields-sold-as-equiv.md) 是 407 bundled 三事专用，不是本页 Finalize 含刚决定那块的字段 not already settled 单句边界。
- [finnewfields-notsettled-sold-as-bundled](finnewfields-notsettled-sold-as-bundled.md) 是 555 461 角度，不是本页 407 字段余量 单句边界。
