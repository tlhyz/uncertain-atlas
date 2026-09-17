# 反模式：把 executes txs deterministically not like Prepare 正式三事（470 余量）卖成 findet bundled / 已经可以像 Prepare 那样 / 套用 candidate 就不需要再执行

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[executes txs deterministically not like Prepare ≠ bundled（470）](../../tracks/implementation/worked-example-findet-notlikeprepare-vs-bundled.md)。

## 卖法

- 「看见 Application executes txs deterministically 就已经可以像 Prepare 那样依赖非确定值 interchangeable / 已经 Prepare 没有确定性要求 interchangeable。」
- 「看见 deterministically execute txs 就已经套用 candidate 就不需要再在 Finalize 执行 interchangeable / 已经 previously executed interchangeable。」
- 「看见 before returning control 就已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable。」

## 为什么错

官方把 executes txs deterministically、Prepare 可以不确定、apply candidate / previously executed 两条路、before returning control 和 committed 交差 写成独立的实现事。把它们卖成 findet bundled、已经可以像 Prepare 那样、套用 candidate 就不需要再执行，会把 not like Prepare、not apply candidate、not committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 executes txs deterministically not like Prepare 正式三事（470 余量），必须分开 not like Prepare、not apply candidate / previously executed、not committed 三个名字，不要把它们卖成 findet bundled / 已经可以像 Prepare 那样 / 套用 candidate 就不需要再执行。

## 和相邻反模式

- [findet-sold-as-prepare](findet-sold-as-prepare.md) 是 470 bundled 三事专用，不是本页 executes txs 单句边界。
- [fincand-notcommitted-sold-as-bundled](fincand-notcommitted-sold-as-bundled.md) 是 576 executes txs not committed 专用，不是本页 findet 角度边界。
