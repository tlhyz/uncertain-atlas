# 反模式：把 ProcessProposal Usage SHOULD always set ACCEPT 正式三事卖成 Process SHOULD Accept bundled / 已经 honest proposal 必须 Accept / 已经 Requirement 3 已经测过

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[SHOULD always set ACCEPT ≠ bundled](../../tracks/implementation/worked-example-procaccept-shouldaccept-vs-bundled.md)。

## 卖法

- 「看见 application implementers SHOULD always set status to ACCEPT 就已经 Process SHOULD Accept bundled interchangeable / 已经 honest proposal 必须 Accept interchangeable。」
- 「看见 SHOULD always set ACCEPT 就已经 Requirement 3 已经测过 interchangeable / 已经 Req 3 是测试目标 interchangeable。」
- 「看见 SHOULD 就已经 MUST Accept any block interchangeable / 已经 honest proposal must Accept at Req interchangeable。」

## 为什么错

官方把 SHOULD always set ACCEPT、not already Req 3 tested、SHOULD is not MUST Accept 写成三件独立的实现事。把它们卖成 Process SHOULD Accept bundled、已经 honest proposal 必须 Accept、已经 Requirement 3 已经测过，会把 SHOULD 建议、Req 3 测试目标、SHOULD vs MUST 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD always set ACCEPT 正式三事，必须分开 SHOULD always set ACCEPT、not already Req 3 tested、SHOULD is not MUST Accept 三个名字，不要把它们卖成 Process SHOULD Accept bundled / 已经 honest proposal 必须 Accept / 已经 Requirement 3 已经测过。

## 和相邻反模式

- [procaccept-sold-as-req3](procaccept-sold-as-req3.md) 是 456 bundled 三事专用；本页是 SHOULD always set ACCEPT 单句边界。
- [verifyaccept-shouldaccept-sold-as-bundled](verifyaccept-shouldaccept-sold-as-bundled.md) 是 Verify 457 item 1 专用，不是本页 Process Usage SHOULD always set 边界。
- [procrespstatus-sold-as-procstatus](procrespstatus-sold-as-procstatus.md) 是 Process 回包栏 bundled，不是本页 Usage SHOULD always set 边界。
