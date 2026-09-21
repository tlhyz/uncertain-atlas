# 反模式：把两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量）说成已经是同一份 prepared / 已经必须同一份 / 已经同一份列表

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[两边 raw 一样 not already same-prepared ≠ bundled（338）](../../tracks/implementation/worked-example-prepare-notrawsame-vs-bundled.md)。

## 卖法

把两边 raw 提案一样 / *v_p = v_q* / 同一份 raw 写成已经是同一份 prepared 提案 interchangeable / 已经 same-prepared interchangeable / 已经同一份 prepared 交差 interchangeable / 338 preparenondet bundled interchangeable / 327 preparetimeout interchangeable / preparenondet-sold-as-deterministic interchangeable；把同一高度、同一轮 / 同一高度同一轮 / 同一轮次 写成已经必须同一份 interchangeable / 已经 must-same-u interchangeable；把诚实准备 / 诚实 Prepare / 正确进程各自 Prepare 写成已经同一份列表 interchangeable / 已经 same-list interchangeable，或已经和 338 preparenondet bundled / preparenondet-sold-as-deterministic interchangeable / 768 prepare-notrawsame interchangeable。

## 为什么错

官方把两边 raw 一样单句、already same-prepared、already must-same-u、already same-list 写成三件独立的实现事。把它们卖成 already same-prepared interchangeable / already must-same-u interchangeable / already same-list interchangeable，会把 not already same-prepared、not already must-same-u、not already same-list 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量），必须分开 not already same-prepared、not already must-same-u、not already same-list 三件事，不要和 338 / 33 / 327 / 34 / 767 / 769 糊成一句。

## 和相邻反模式

- [extend-notsameext-sold-as-bundled](extend-notsameext-sold-as-bundled.md) 是同一块 ≠ 已经是同一份扩展（338 item 3），不是本页两边 raw 一样 item 2 单句边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare nondet bundled 全段，不是本页两边 raw 一样 item 2 单句边界。
- [prepare-notmustdet-sold-as-bundled](prepare-notmustdet-sold-as-bundled.md) 是 Prepare 没有确定性要求 ≠ 已经必须确定（338 item 1），不是本页两边 raw 一样 ≠ 已经是同一份提案 边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径（327），不是本页同一高度同一轮边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页诚实准备边界。
