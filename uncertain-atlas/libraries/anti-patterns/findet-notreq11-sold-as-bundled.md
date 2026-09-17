# 反模式：把 implementation MUST be deterministic not Req 11–12 正式三事（470 余量）卖成 findet bundled / 已经是 Req 11–12 / finfields bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[implementation MUST be deterministic not Req 11–12 ≠ bundled（470）](../../tracks/implementation/worked-example-findet-notreq11-vs-bundled.md)。

## 卖法

- 「看见 implementation MUST be deterministic for state machine replication 就已经 Req 11–12 interchangeable / 已经 s_h / T_h 只依赖两份 interchangeable。」
- 「看见 Usage 写了必须确定 就已经 finfields bundled interchangeable / 已经 Info 用来回应用状态信息 interchangeable。」
- 「看见 implementation 必须确定 就已经 findet bundled interchangeable / 已经 executes txs deterministically interchangeable / 已经 app_hash MUST be deterministic interchangeable。」

## 为什么错

官方把 implementation MUST be deterministic、Req 11–12、finfields bundled、executes txs / app_hash 三句 bundled 写成独立的实现事。把它们卖成 findet bundled、已经是 Req 11–12、finfields bundled，会把 not Req 11–12、not finfields bundled、not findet item 1/2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 implementation MUST be deterministic not Req 11–12 正式三事（470 余量），必须分开 not Req 11–12、not finfields bundled、not findet item 1/2 三个名字，不要把它们卖成 findet bundled / 已经是 Req 11–12 / finfields bundled。

## 和相邻反模式

- [findet-sold-as-prepare](findet-sold-as-prepare.md) 是 470 bundled 三事专用，不是本页 implementation 单句边界。
- [finfields-notdeterministic-sold-as-bundled](finfields-notdeterministic-sold-as-bundled.md) 是 574 Finalize 实现必须确定 not like Prepare 专用，不是本页 470 item 3 边界。
