# 反模式：把 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量）说成已经是四门已经结算 / 已经交差 / 已经选型

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了 UNKNOWN not already fourgates ≠ bundled（376）](../../tracks/implementation/worked-example-proposalstatus-notfourgates-vs-bundled.md)。

## 卖法

把回了 UNKNOWN / UNKNOWN 一律是错、引擎当应用坏了会崩 / 回了 UNKNOWN 状态 写成已经是四门已经结算 interchangeable / 已经 fourgates interchangeable / 已经是四门已经结算交差 interchangeable / 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable；把崩了 / 引擎当应用坏了会崩 / 崩 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把有枚举 / ProposalStatus 枚举 / 有 UNKNOWN/ACCEPT/REJECT 写成已经选型 interchangeable / 已经 selected interchangeable / 已经选型交差 interchangeable，或已经和 376 proposalstatus bundled / proposalstatus-sold-as-prevote interchangeable / 875 proposalstatus-notfourgates interchangeable。

## 为什么错

官方把回了 UNKNOWN、不是已经交差、不是已经选型写成三件独立的实现事。把它们卖成 already fourgates interchangeable / already settled interchangeable / already selected interchangeable，会把 not already fourgates、not already settled、not already selected 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量），必须分开 not already fourgates、not already settled、not already selected 三件事，不要和 376 / 33 / 347 / 354 糊成一句。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 proposalstatus bundled 全段，不是本页回了 UNKNOWN item 1 单句边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already fourgates 单句。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept（347），不是本页 not already settled 边界。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能在返回之后再改裁决（354），不是本页 not already selected 边界。
