# 反模式：把 VerifyVoteExtension Usage SHOULD always set ACCEPT 正式三事卖成 Verify SHOULD Accept bundled / 已经 correct process must Accept / 已经 Requirement 6 已经测过

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[SHOULD always set ACCEPT ≠ bundled](../../tracks/implementation/worked-example-verifyaccept-shouldaccept-vs-bundled.md)。

## 卖法

- 「看见 application implementers SHOULD always set status to ACCEPT 就已经 Verify SHOULD Accept bundled interchangeable / 已经 correct process must Accept interchangeable。」
- 「看见 SHOULD always set ACCEPT 就已经 Requirement 6 已经测过 interchangeable / 已经 Req 6 是测试目标 interchangeable。」
- 「看见 SHOULD 就已经 MUST Accept any extension interchangeable / 已经 Extend–Verify consistency must Accept interchangeable。」

## 为什么错

官方把 SHOULD always set ACCEPT、not already Req 6 tested、SHOULD is not MUST Accept 写成三件独立的实现事。把它们卖成 Verify SHOULD Accept bundled、已经 correct process must Accept、已经 Requirement 6 已经测过，会把 SHOULD 建议、Req 6 测试目标、SHOULD vs MUST 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD always set ACCEPT 正式三事，必须分开 SHOULD always set ACCEPT、not already Req 6 tested、SHOULD is not MUST Accept 三个名字，不要把它们卖成 Verify SHOULD Accept bundled / 已经 correct process must Accept / 已经 Requirement 6 已经测过。

## 和相邻反模式

- [verifyaccept-sold-as-req6](verifyaccept-sold-as-req6.md) 是 457 bundled 三事专用；本页是 SHOULD always set ACCEPT 单句边界。
- [verifyrespstatus-sold-as-verifystatus](verifyrespstatus-sold-as-verifystatus.md) 是 Verify 回包栏 bundled，不是本页 Usage SHOULD always set 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是 Req 6 must Accept，不是本页 Usage SHOULD 建议边界。
