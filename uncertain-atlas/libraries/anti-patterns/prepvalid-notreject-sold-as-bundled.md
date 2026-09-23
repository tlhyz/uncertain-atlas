# 反模式：把 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量）说成已经是 Process REJECT / 已经是 Req 3 必须 Accept / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Prepare 回包验不过引擎崩溃 not already process-reject ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notreject-vs-bundled.md)。

## 卖法

把崩溃了 / Prepare 回包验不过 / 引擎当应用坏了并崩溃 写成已经是 Process REJECT interchangeable / 已经 process-reject interchangeable / 已经是 Process REJECT 交差 interchangeable / 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable；把回包坏了 / 验不过 PrepareProposalResponse 写成已经是 Req 3 必须 Accept interchangeable / 已经 req3-accept interchangeable / 已经是 Req 3 必须 Accept 交差 interchangeable；把引擎停了 / 崩溃停机 / 应用被当成故障 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 357 preparevalid bundled / preparevalid-sold-as-checked interchangeable / 825 prepvalid-notreject interchangeable。

## 为什么错

官方把崩溃了、不是已经是 Req 3 必须 Accept、不是已经交差写成三件独立的实现事。把它们卖成 already process-reject interchangeable / already req3-accept interchangeable / already settled interchangeable，会把 not already process-reject、not already req3-accept、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量），必须分开 not already process-reject、not already req3-accept、not already settled 三件事，不要和 357 / 347 / 313 / 824 / 826 糊成一句。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled 全段，不是本页崩溃了 item 2 单句边界。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept（347），不是本页 not already process-reject 边界。
- [prepvalid-notdedup-sold-as-bundled](prepvalid-notdedup-sold-as-bundled.md) 是引擎没有再验重复交易 not already dedup-checked（357 item 1），不是本页 not already settled 边界。
