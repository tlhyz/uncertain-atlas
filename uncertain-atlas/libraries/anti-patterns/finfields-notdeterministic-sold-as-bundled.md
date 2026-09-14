# 反模式：把 Finalize 实现必须确定 not like Prepare 正式三事（407 余量）卖成 finfields bundled / 已经可以像 Prepare 那样 / findet bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Finalize 实现必须确定 not like Prepare ≠ bundled（407）](../../tracks/implementation/worked-example-finfields-notdeterministic-vs-bundled.md)。

## 卖法

- 「看见 Finalize 实现必须确定 / 看见 Usage 写了 MUST be deterministic 就已经可以像 Prepare 那样 interchangeable / 已经 Prepare 没有确定性要求 interchangeable。」
- 「看见必须确定 就已经 executes txs deterministically interchangeable / 已经 app_hash MUST be deterministic interchangeable / 已经 Req 11–12 interchangeable。」
- 「看见必须确定 就已经四门已经结算 interchangeable / 已经 Info 握手对齐 interchangeable / 已经 finfields bundled interchangeable。」

## 为什么错

官方把 `FinalizeBlock` 实现必须确定、Prepare 可以不确定、Usage determinism 三句 bundled、含刚决定那块的字段 / Info 回应用状态信息 bundled 写成独立的实现事。把它们卖成 finfields bundled、已经可以像 Prepare 那样、findet bundled，会把 not like Prepare、not findet bundled、not finfields item 1/3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 实现必须确定 not like Prepare 正式三事（407 余量），必须分开 not like Prepare、not findet bundled、not finfields item 1/3 三个名字，不要把它们卖成 finfields bundled / 已经可以像 Prepare 那样 / findet bundled。

## 和相邻反模式

- [finfields-sold-as-equiv](finfields-sold-as-equiv.md) 是 407 bundled 三事专用，不是本页 implementation must be deterministic 单句边界。
- [findet-sold-as-prepare](findet-sold-as-prepare.md) 是 470 Usage determinism 专用，不是本页 407 item 2 余量边界。
- [finfields-notsettled-sold-as-bundled](finfields-notsettled-sold-as-bundled.md) 是 573 item 1 专用，不是本页 item 2 deterministic 边界。
