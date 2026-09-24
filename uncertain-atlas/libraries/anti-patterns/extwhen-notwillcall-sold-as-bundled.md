# 反模式：把 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量）说成已经会调 ExtendVote / 已经锁住 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[+2/3 prevote 才锁住再调 not already will-call ≠ bundled（361）](../../tracks/implementation/worked-example-extwhen-notwillcall-vs-bundled.md)。

## 卖法

把到了 prevote 步 / 收到提案和全部块片、并且 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote / 到了 prevote 步 写成已经会调 ExtendVote interchangeable / 已经 will-call interchangeable / 已经会调交差 interchangeable / 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable；把有提案 / 有提案 *v* 和全部块片 写成已经锁住 interchangeable / 已经 locked-value interchangeable / 已经锁住 *v* 交差 interchangeable；把规范写了 When / When 条款在 / 锁住再调写进了规范 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 361 extendwhen bundled / extendwhen-sold-as-locked interchangeable / 833 extwhen-notwillcall interchangeable。

## 为什么错

官方把到了 prevote 步、不是已经锁住、不是已经交差写成三件独立的实现事。把它们卖成 already will-call interchangeable / already locked-value interchangeable / already settled interchangeable，会把 not already will-call、not already locked-value、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量），必须分开 not already will-call、not already locked-value、not already settled 三件事，不要和 361 / 350 / 354 / 834 / 835 糊成一句。

## 和相邻反模式

- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 ExtendVote 何时调用 bundled 全段，不是本页到了 prevote 步 item 1 单句边界。
- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮只能交出一份扩展就已经是每一高度一份（350），不是本页 not already will-call 边界。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能稍后改裁决（354），不是本页 not already settled 边界。
