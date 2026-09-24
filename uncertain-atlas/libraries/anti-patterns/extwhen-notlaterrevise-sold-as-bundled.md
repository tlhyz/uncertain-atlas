# 反模式：把 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量）说成已经能稍后改扩展 / 已经离开关键路径 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExtendVote 同步 not already later-revise ≠ bundled（361）](../../tracks/implementation/worked-example-extwhen-notlaterrevise-vs-bundled.md)。

## 卖法

把是同步的 / CometBFT 调 `ExtendVote` 是同步的 / 引擎同步等回包 写成已经能在返回之后再改扩展 interchangeable / 已经 later-revise interchangeable / 已经能稍后改扩展交差 interchangeable / 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable；把引擎在等 / 引擎在等回包 写成已经离开关键路径 interchangeable / 已经 left-critical interchangeable / 已经离开关键路径交差 interchangeable；把回了 / 回包回来了 / 同步调用返回了 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 361 extendwhen bundled / extendwhen-sold-as-locked interchangeable / 834 extwhen-notlaterrevise interchangeable。

## 为什么错

官方把是同步的、不是已经离开关键路径、不是已经交差写成三件独立的实现事。把它们卖成 already later-revise interchangeable / already left-critical interchangeable / already settled interchangeable，会把 not already later-revise、not already left-critical、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量），必须分开 not already later-revise、not already left-critical、not already settled 三件事，不要和 361 / 354 / 350 / 833 / 835 糊成一句。

## 和相邻反模式

- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 ExtendVote 何时调用 bundled 全段，不是本页是同步的 item 2 单句边界。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能稍后改裁决（354），不是本页 not already later-revise 边界。
- [extwhen-notwillcall-sold-as-bundled](extwhen-notwillcall-sold-as-bundled.md) 是 +2/3 prevote 才锁住再调 not already will-call（361 item 1），不是本页 not already settled 边界。
