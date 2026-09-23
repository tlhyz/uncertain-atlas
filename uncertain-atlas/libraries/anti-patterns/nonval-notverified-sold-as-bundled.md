# 反模式：把非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量）说成已经验过这块 / 已经交差 / 已经是提议者那边也会叫 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[非验证者可以立刻回 ACCEPT not already verified ≠ bundled（354）](../../tracks/implementation/worked-example-nonval-notverified-vs-bundled.md)。

## 卖法

把非验证者可以立刻回 `ACCEPT` / 立刻 `ACCEPT` / 立刻回了 ACCEPT 写成已经验过这块 interchangeable / 已经 verified interchangeable / 已经验过交差 interchangeable / 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable；把不是验证者 / *p* 不是验证者 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把规范允许 / 可以立刻回 / 不想让非验证者处理 写成已经是提议者那边也会叫 Process interchangeable / 已经 processalso interchangeable / 已经 processalso 交差 interchangeable，或已经和 354 processwhen bundled / processwhen-sold-as-later interchangeable / 817 nonval-notverified interchangeable。

## 为什么错

官方把立刻 ACCEPT、不是已经交差、不是已经是提议者那边也会叫 Process 写成三件独立的实现事。把它们卖成 already verified interchangeable / already settled interchangeable / already processalso interchangeable，会把 not already verified、not already settled、not already processalso 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看非验证者可以立刻回 ACCEPT 不是已经验过这块 not already verified / not already settled / not already processalso 正式三事（354 余量），必须分开 not already verified、not already settled、not already processalso 三件事，不要和 354 / 327 / 33 / 815 / 816 糊成一句。

## 和相邻反模式

- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 何时调用 bundled 全段，不是本页立刻 ACCEPT item 3 单句边界。
- [async-notreject-sold-as-bundled](async-notreject-sold-as-bundled.md) 是只做基本检查再异步 Process not already still-revise（354 item 2），不是本页 not already verified 边界。
- [sync-notlater-sold-as-bundled](sync-notlater-sold-as-bundled.md) 是 Process 调用是同步的 not already later-revise（354 item 1），不是本页 not already processalso 边界。
