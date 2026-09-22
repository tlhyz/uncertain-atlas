# 反模式：把 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量）说成已经测过 / 已经是引擎会帮你挡 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Req 3 是大量测试和自动验证的目标 not already tested ≠ bundled（347）](../../tracks/implementation/worked-example-req3-nottested-vs-bundled.md)。

## 卖法

把同一份代码库很可能同时踩中、多数 prevote nil / Req 3 因此是大量测试和自动验证的目标 / 写了测试目标 写成已经测过 interchangeable / 已经 tested interchangeable / 已经测过交差 interchangeable / 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable；把会 prevote nil / 多数或全部进程 prevote nil 写成已经是引擎会帮你挡 interchangeable / 已经 engine-blocks interchangeable / 已经引擎挡交差 interchangeable；把写了测试目标 / 是大量测试和自动验证的目标 写成已经交差 interchangeable / 已经 settled interchangeable / 已经测试交差 interchangeable，或已经和 347 req3coherence bundled / req3coherence-sold-as-accept interchangeable / 796 req3-nottested interchangeable。

## 为什么错

官方把必须测、不是已经是引擎会帮你挡、不是已经交差写成三件独立的实现事。把它们卖成 already tested interchangeable / already engine-blocks interchangeable / already settled interchangeable，会把 not already tested、not already engine-blocks、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量），必须分开 not already tested、not already engine-blocks、not already settled 三件事，不要和 347 / 338 / 33 / 794 / 795 糊成一句。

## 和相邻反模式

- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是 Prepare–Process 一致性 bundled 全段，不是本页测试目标 item 3 单句边界。
- [req3-notbyz-sold-as-bundled](req3-notbyz-sold-as-bundled.md) 是 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only-liveness（347 item 2），不是本页 not already tested 边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求（338），不是本页会 prevote nil ≠ 引擎会挡 边界。
