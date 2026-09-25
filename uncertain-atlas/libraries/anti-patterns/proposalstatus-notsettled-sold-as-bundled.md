# 反模式：把 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量）说成已经交差 / 已经必须 Accept / 已经过了四门

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了 ACCEPT not already settled ≠ bundled（376）](../../tracks/implementation/worked-example-proposalstatus-notsettled-vs-bundled.md)。

## 卖法

把回了 ACCEPT / ACCEPT 表示应用认为提案合法、共识会发 Prevote / 回了 ACCEPT 状态 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable；把会发 Prevote / 共识会发 Prevote / 发了 Prevote 写成已经必须 Accept interchangeable / 已经 mustaccept interchangeable / 已经必须 Accept 交差 interchangeable；把合法 / 应用认为提案合法 / 合法状态 写成已经过了四门 interchangeable / 已经 fourgates interchangeable / 已经过了四门交差 interchangeable，或已经和 376 proposalstatus bundled / proposalstatus-sold-as-prevote interchangeable / 876 proposalstatus-notsettled interchangeable。

## 为什么错

官方把回了 ACCEPT、不是已经必须 Accept、不是已经过了四门写成三件独立的实现事。把它们卖成 already settled interchangeable / already mustaccept interchangeable / already fourgates interchangeable，会把 not already settled、not already mustaccept、not already fourgates 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量），必须分开 not already settled、not already mustaccept、not already fourgates 三件事，不要和 376 / 347 / 875 / 33 糊成一句。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 proposalstatus bundled 全段，不是本页回了 ACCEPT item 2 单句边界。
- [proposalstatus-notfourgates-sold-as-bundled](proposalstatus-notfourgates-sold-as-bundled.md) 是回了 UNKNOWN not already fourgates（376 item 1），不是本页 not already settled 边界。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept（347），不是本页 not already mustaccept 单句。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already fourgates 边界。
