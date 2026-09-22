# 反模式：把正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量）说成已经是任意块都会 Accept / 已经写了默认 Accept / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[正确提议者的准备提案必须被正确接收者 Accept not already any-block ≠ bundled（347）](../../tracks/implementation/worked-example-req3-notany-vs-bundled.md)。

## 卖法

把正确提议者交出的准备提案、正确接收者 Process 必须 Accept / 正确进程之间永远过 / 正确提议者交出来的必须过 写成已经是任意块都会 Accept interchangeable / 已经 any-block interchangeable / 已经任意块过交差 interchangeable / 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable；把必须 Accept / 正确接收者 Process 必须回 Accept 写成已经写了默认 Accept interchangeable / 已经 default-accept interchangeable / 已经默认 Accept 交差 interchangeable；把正确进程之间过 / 正确提议者交出来的必须过 写成已经交差 interchangeable / 已经 settled interchangeable / 已经 Accept 交差 interchangeable，或已经和 347 req3coherence bundled / req3coherence-sold-as-accept interchangeable / 794 req3-notany interchangeable。

## 为什么错

官方把正确进程之间必须过、不是已经写了默认 Accept、不是已经交差写成三件独立的实现事。把它们卖成 already any-block interchangeable / already default-accept interchangeable / already settled interchangeable，会把 not already any-block、not already default-accept、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量），必须分开 not already any-block、not already default-accept、not already settled 三件事，不要和 347 / 33 / 348 / 795 / 796 糊成一句。

## 和相邻反模式

- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是 Prepare–Process 一致性 bundled 全段，不是本页必须 Accept item 1 单句边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是 Req 6 必须 Accept（348），不是本页提案必须 Accept 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页任意块都会 Accept 边界。
