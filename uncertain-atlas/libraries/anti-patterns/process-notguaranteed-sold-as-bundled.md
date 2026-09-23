# 反模式：把通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量）说成已经保证是这一次 / 已经必须一样 / 已经是同一份调用

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[通常紧跟 Prepare、列表对得上 not already guaranteed-this ≠ bundled（351）](../../tracks/implementation/worked-example-process-notguaranteed-vs-bundled.md)。

## 卖法

把通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` / 通常对得上 / 列表对得上 写成已经保证是这一次 Prepare 的回包 interchangeable / 已经 guaranteed-this interchangeable / 已经保证这一次交差 interchangeable / 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable；把 txs 一样 / 请求 txs 等于回包 txs 写成已经必须一样 interchangeable / 已经 must-match interchangeable / 已经必须对上交差 interchangeable；把刚 Prepare 完 / 刚回了 Prepare 写成已经是同一份调用 interchangeable / 已经 same-call interchangeable / 已经同一调用交差 interchangeable，或已经和 351 processalso bundled / processalso-sold-as-matched interchangeable / 807 process-notguaranteed interchangeable。

## 为什么错

官方把通常紧跟 Prepare、列表对得上、不是已经必须一样、不是已经是同一份调用写成三件独立的实现事。把它们卖成 already guaranteed-this interchangeable / already must-match interchangeable / already same-call interchangeable，会把 not already guaranteed-this、not already must-match、not already same-call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量），必须分开 not already guaranteed-this、not already must-match、not already same-call 三件事，不要和 351 / 347 / 33 / 806 / 808 糊成一句。

## 和相邻反模式

- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫 bundled 全段，不是本页通常对得上 item 2 单句边界。
- [process-notskip-sold-as-bundled](process-notskip-sold-as-bundled.md) 是 Process 也会在提议者那边叫 not already skip-process（351 item 1），不是本页 not already guaranteed-this 边界。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept（347），不是本页 not already guaranteed-this 边界。
