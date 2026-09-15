# 反模式：把 ProcessProposal Usage unless really know liveness implications 正式三事卖成 Process SHOULD Accept bundled / 已经 REJECT 是免费过滤 / 已经 Process REJECT = prevote nil 那种已经结算

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[unless really know liveness implications ≠ bundled](../../tracks/implementation/worked-example-procaccept-liveness-vs-bundled.md)。

## 卖法

- 「看见 unless they really know liveness implications 就已经 Process SHOULD Accept bundled interchangeable / 已经 REJECT 是免费过滤 interchangeable。」
- 「看见除非真的知道活性代价 就已经 Process REJECT = prevote nil interchangeable / 已经 Process REJECT = prevote nil 那种已经结算 interchangeable。」
- 「看见可以 Reject 就已经 REJECT 没有代价 interchangeable / 已经不能 Reject interchangeable。」

## 为什么错

官方把 unless really know liveness implications、not free filter Process REJECT prevote nil、can Reject not no cost 写成三件独立的实现事。把它们卖成 Process SHOULD Accept bundled、已经 REJECT 是免费过滤、已经 Process REJECT = prevote nil 那种已经结算，会把 unless 条件、not free filter、REJECT 有 liveness 代价三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage unless really know liveness implications 正式三事，必须分开 unless really know、not free filter、can Reject not no cost 三个名字，不要把它们卖成 Process SHOULD Accept bundled / 已经 REJECT 是免费过滤 / 已经 Process REJECT = prevote nil 那种已经结算。

## 和相邻反模式

- [procaccept-sold-as-req3](procaccept-sold-as-req3.md) 是 456 bundled 三事专用；本页是 unless really know liveness implications 单句边界。
- [procaccept-shouldaccept-sold-as-bundled](procaccept-shouldaccept-sold-as-bundled.md) 是 SHOULD always set ACCEPT 专用，不是本页 unless 条件边界。
- [procrespstatus-sold-as-procstatus](procrespstatus-sold-as-procstatus.md) 是 Process 回包栏 bundled，不是本页 Usage unless liveness 边界。
