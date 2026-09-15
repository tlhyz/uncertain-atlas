# 反模式：把 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事卖成 Verify SHOULD Accept bundled / 已经不能 Reject / 已经 Verify 341 SHOULD Accept 通则 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[SHOULD Accept default strategy ≠ bundled](../../tracks/implementation/worked-example-verifyaccept-default-vs-bundled.md)。

## 卖法

- 「看见 SHOULD Accept 默认策略 就已经 Verify SHOULD Accept bundled interchangeable / 已经不能 Reject interchangeable / 已经 MUST Accept interchangeable。」
- 「看见 REJECT 时共识拒整张票 就已经 can't Reject interchangeable / 已经 REJECT 没有路径 interchangeable。」
- 「看见默认 Accept 就已经 Verify 341 SHOULD Accept 通则 interchangeable / 已经 status 必须只依赖 interchangeable / 433 MUST Accept interchangeable。」

## 为什么错

官方把 SHOULD Accept default strategy、REJECT rejects whole vote、default Accept not Verify det general rule 写成三件独立的实现事。把它们卖成 Verify SHOULD Accept bundled、已经 can't Reject、已经 Verify 341 SHOULD Accept 通则 interchangeable，会把 default strategy、REJECT 路径存在、341 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事，必须分开 SHOULD Accept default strategy、REJECT rejects whole vote、default Accept not Verify det general rule 三个名字，不要把它们卖成 Verify SHOULD Accept bundled / 已经 can't Reject / 已经 Verify 341 SHOULD Accept 通则 interchangeable。

## 和相邻反模式

- [verifyaccept-sold-as-req6](verifyaccept-sold-as-req6.md) 是 457 bundled 三事专用；本页是 SHOULD Accept default strategy 单句边界。
- [verifyaccept-liveness-sold-as-bundled](verifyaccept-liveness-sold-as-bundled.md) 是 unless know liveness 专用，不是本页 default strategy 边界。
- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 Verify 341 determinism 通则，不是本页 Usage default strategy 边界。
