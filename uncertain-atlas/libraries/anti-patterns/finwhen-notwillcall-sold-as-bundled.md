# 反模式：把 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量）说成已经会调 Finalize / 已经决定 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[+2/3 precommit 才决定再调 not already will-call ≠ bundled（362）](../../tracks/implementation/worked-example-finwhen-notwillcall-vs-bundled.md)。

## 卖法

把到了这一高 / 收到提案和全部块片、并且 +2/3 precommit 同一 `id(v)` 才决定再调 Finalize / 到了这一高 写成已经会调 Finalize interchangeable / 已经 will-call interchangeable / 已经会调交差 interchangeable / 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable；把有提案 / 有提案 *v* 和全部块片 写成已经决定 interchangeable / 已经 decided interchangeable / 已经决定 *v* 交差 interchangeable；把规范写了 When / When 条款在 / 决定再调写进了规范 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 362 finwhen bundled / finalizewhen-sold-as-decided interchangeable / 836 finwhen-notwillcall interchangeable。

## 为什么错

官方把到了这一高、不是已经决定、不是已经交差写成三件独立的实现事。把它们卖成 already will-call interchangeable / already decided interchangeable / already settled interchangeable，会把 not already will-call、not already decided、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量），必须分开 not already will-call、not already decided、not already settled 三件事，不要和 362 / 361 / 335 / 837 / 838 糊成一句。

## 和相邻反模式

- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是 Finalize 何时调用 bundled 全段，不是本页到了这一高 item 1 单句边界。
- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 +2/3 prevote 才锁住再调 ExtendVote（361），不是本页 not already will-call 边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 改了就已经落盘（335），不是本页 not already settled 边界。
