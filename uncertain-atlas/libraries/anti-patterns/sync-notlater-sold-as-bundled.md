# 反模式：把 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量）说成已经能稍后改裁决 / 已经离开关键路径 / 已经是立刻整块执行就已经离开关键路径

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Process 调用是同步的 not already later-revise ≠ bundled（354）](../../tracks/implementation/worked-example-sync-notlater-vs-bundled.md)。

## 卖法

把 Process 调用是同步的 / 是同步的 / 引擎在等回包 写成已经能在返回之后再改裁决 interchangeable / 已经 later-revise interchangeable / 已经稍后改裁决交差 interchangeable / 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable；把引擎在等 / 引擎在等回包 写成已经离开关键路径 interchangeable / 已经 left-critical interchangeable / 已经离开关键路径交差 interchangeable；把立刻执行 / 同步立刻执行 / 立刻调 写成已经是立刻整块执行就已经离开关键路径 interchangeable / 已经 full-exec interchangeable / 已经立刻整块离开关键路径交差 interchangeable，或已经和 354 processwhen bundled / processwhen-sold-as-later interchangeable / 815 sync-notlater interchangeable。

## 为什么错

官方把是同步的、不是已经离开关键路径、不是已经是立刻整块执行就已经离开关键路径写成三件独立的实现事。把它们卖成 already later-revise interchangeable / already left-critical interchangeable / already full-exec interchangeable，会把 not already later-revise、not already left-critical、not already full-exec 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量），必须分开 not already later-revise、not already left-critical、not already full-exec 三件事，不要和 354 / 327 / 33 / 816 / 817 糊成一句。

## 和相邻反模式

- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 何时调用 bundled 全段，不是本页是同步的 item 1 单句边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行就已经离开关键路径（327），不是本页 not already later-revise 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already left-critical 边界。
