# 反模式：把 ProcessProposal Usage SHOULD Accept default strategy 正式三事卖成 Process SHOULD Accept bundled / 已经不能 Reject / 已经 Process 340 SHOULD Accept 通则 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[SHOULD Accept default strategy ≠ bundled](../../tracks/implementation/worked-example-procaccept-default-vs-bundled.md)。

## 卖法

- 「看见 SHOULD Accept 默认策略 就已经 Process SHOULD Accept bundled interchangeable / 已经不能 Reject interchangeable / 已经 MUST Accept interchangeable。」
- 「看见 REJECT 时共识 assumes not valid 就已经 can't Reject interchangeable / 已经 REJECT 没有路径 interchangeable。」
- 「看见默认 Accept 就已经 Process 340 SHOULD Accept 通则 interchangeable / 已经 status 必须只依赖 interchangeable / 430 MUST Accept interchangeable。」

## 为什么错

官方把 SHOULD Accept default strategy、REJECT assumes not valid、default Accept not Process det general rule 写成三件独立的实现事。把它们卖成 Process SHOULD Accept bundled、已经 can't Reject、已经 Process 340 SHOULD Accept 通则 interchangeable，会把 default strategy、REJECT 路径存在、340 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事，必须分开 SHOULD Accept default strategy、REJECT assumes not valid、default Accept not Process det general rule 三个名字，不要把它们卖成 Process SHOULD Accept bundled / 已经 can't Reject / 已经 Process 340 SHOULD Accept 通则 interchangeable。

## 和相邻反模式

- [procaccept-sold-as-req3](procaccept-sold-as-req3.md) 是 456 bundled 三事专用；本页是 SHOULD Accept default strategy 单句边界。
- [procaccept-liveness-sold-as-bundled](procaccept-liveness-sold-as-bundled.md) 是 unless know liveness 专用，不是本页 default strategy 边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 Process 340 determinism 通则，不是本页 Usage default strategy 边界。
