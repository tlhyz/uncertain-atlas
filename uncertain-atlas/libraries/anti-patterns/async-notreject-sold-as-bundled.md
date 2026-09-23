# 反模式：把只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量）说成已经还能改票 / 已经还能 Reject / 已经能强迫 nil

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[只做基本检查再异步 Process not already still-revise ≠ bundled（354）](../../tracks/implementation/worked-example-async-notreject-vs-bundled.md)。

## 卖法

把只做基本检查再异步 Process / 异步了 / 已经回了 `ACCEPT` 写成已经还能改票 interchangeable / 已经 still-revise interchangeable / 已经还能改票交差 interchangeable / 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable；把先回了 / 已经回了 `ACCEPT` 写成已经还能再 Reject interchangeable / 已经 still-reject interchangeable / 已经还能 Reject 交差 interchangeable；把还在跑 / 异步还在跑 / 还在处理 写成已经能强迫 `nil` interchangeable / 已经 force-nil interchangeable / 已经强迫 nil 交差 interchangeable，或已经和 354 processwhen bundled / processwhen-sold-as-later interchangeable / 816 async-notreject interchangeable。

## 为什么错

官方把异步了、不是已经还能 Reject、不是已经能强迫 nil 写成三件独立的实现事。把它们卖成 already still-revise interchangeable / already still-reject interchangeable / already force-nil interchangeable，会把 not already still-revise、not already still-reject、not already force-nil 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只做基本检查再异步 Process 不是已经还能再 Reject not already still-revise / not already still-reject / not already force-nil 正式三事（354 余量），必须分开 not already still-revise、not already still-reject、not already force-nil 三件事，不要和 354 / 327 / 33 / 815 / 817 糊成一句。

## 和相邻反模式

- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 何时调用 bundled 全段，不是本页异步了 item 2 单句边界。
- [sync-notlater-sold-as-bundled](sync-notlater-sold-as-bundled.md) 是 Process 调用是同步的 not already later-revise（354 item 1），不是本页 not already still-revise 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already still-reject 边界。
