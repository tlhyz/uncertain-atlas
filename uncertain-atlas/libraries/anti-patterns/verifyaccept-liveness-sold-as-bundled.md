# 反模式：把 VerifyVoteExtension Usage unless really know liveness implications 正式三事卖成 Verify SHOULD Accept bundled / 已经拒整张 Precommit 是免费过滤 / 已经 Verify REJECT = 块非法

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[unless really know liveness implications ≠ bundled](../../tracks/implementation/worked-example-verifyaccept-liveness-vs-bundled.md)。

## 卖法

- 「看见 unless they really know liveness implications 就已经 Verify SHOULD Accept bundled interchangeable / 已经拒整张 Precommit 是免费过滤 interchangeable。」
- 「看见除非真的知道活性代价 就已经验签拒收整张 Precommit interchangeable / 已经 Verify REJECT = 块非法 interchangeable。」
- 「看见可以 Reject 就已经 REJECT 没有代价 interchangeable / 已经不能 Reject interchangeable。」

## 为什么错

官方把 unless really know liveness implications、not free filter reject whole precommit、can Reject not no cost 写成三件独立的实现事。把它们卖成 Verify SHOULD Accept bundled、已经拒整张 Precommit 是免费过滤、已经 Verify REJECT = 块非法，会把 unless 条件、not free filter、REJECT 有 liveness 代价三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage unless really know liveness implications 正式三事，必须分开 unless really know、not free filter、can Reject not no cost 三个名字，不要把它们卖成 Verify SHOULD Accept bundled / 已经拒整张 Precommit 是免费过滤 / 已经 Verify REJECT = 块非法。

## 和相邻反模式

- [verifyaccept-sold-as-req6](verifyaccept-sold-as-req6.md) 是 457 bundled 三事专用；本页是 unless really know liveness implications 单句边界。
- [verifyaccept-shouldaccept-sold-as-bundled](verifyaccept-shouldaccept-sold-as-bundled.md) 是 SHOULD always set ACCEPT 专用，不是本页 unless 条件边界。
- [verifywhen-keepdiscard-sold-as-bundled](verifywhen-keepdiscard-sold-as-bundled.md) 是 Verify When REJECT discard，不是本页 Usage unless liveness 边界。
