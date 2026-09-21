# 反模式：把两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量）说成已经只对诚实提案同判 / 已经可以各判各的 / 已经是 Req 3

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[两边同判 not already honest-only ≠ bundled（340）](../../tracks/implementation/worked-example-process-nothonestonly-vs-bundled.md)。

## 卖法

把两边对任意块同一裁决 / 两边同判 / 所有正确进程对一份提案反应相同 写成已经只对诚实提案同一裁决 interchangeable / 已经 honest-only interchangeable / 已经只对诚实 *u_p* 同判交差 interchangeable / 340 processdet bundled interchangeable / 347 req3-coherence interchangeable / processdet-sold-as-prepare interchangeable；把提议者是拜占庭 / 提议者坏了 / 提议者可以不诚实 写成已经可以各判各的 interchangeable / 已经 may-diverge interchangeable；把任意块 / 对任意块 *u* / 不是只对诚实准备好的提案 写成已经是 Req 3 诚实对诚实 interchangeable / 已经 req3-same interchangeable，或已经和 340 processdet bundled / processdet-sold-as-prepare interchangeable / 774 process-nothonestonly interchangeable。

## 为什么错

官方把两边同判单句、already honest-only、already may-diverge、already req3-same 写成三件独立的实现事。把它们卖成 already honest-only interchangeable / already may-diverge interchangeable / already req3-same interchangeable，会把 not already honest-only、not already may-diverge、not already req3-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量），必须分开 not already honest-only、not already may-diverge、not already req3-same 三件事，不要和 340 / 338 / 33 / 347 / 773 / 775 糊成一句。

## 和相邻反模式

- [process-notlostsafety-sold-as-bundled](process-notlostsafety-sold-as-bundled.md) 是活性不能保证 ≠ 已经丢了安全性（340 item 3），不是本页两边同判 item 2 单句边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 ProcessProposal 确定性 bundled 全段，不是本页两边同判 item 2 单句边界。
- [process-notlikeprepare-sold-as-bundled](process-notlikeprepare-sold-as-bundled.md) 是必须确定 ≠ 已经可以像 Prepare 那样（340 item 1），不是本页两边同判 ≠ 已经只对诚实提案 边界。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是诚实 Prepare 必须被诚实 Process Accept（347），不是本页任意块 ≠ 已经是 Req 3 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页提议者坏了 ≠ 已经可以各判各的 边界。
