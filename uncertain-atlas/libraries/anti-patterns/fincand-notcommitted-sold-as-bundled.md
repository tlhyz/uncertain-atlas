# 反模式：把 executes txs deterministically not already committed 正式三事（460 余量）卖成 fincand bundled / 已经交差 / 已经像 Prepare 那样

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[executes txs deterministically not already committed ≠ bundled（460）](../../tracks/implementation/worked-example-fincand-notcommitted-vs-bundled.md)。

## 卖法

- 「看见 Application executes txs deterministically before returning control 就已经 Finalize + Commit 交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable。」
- 「看见 deterministically 就已经可以像 Prepare 那样依赖非确定值 interchangeable / 已经 Prepare 没有确定性要求 interchangeable。」
- 「看见确定执行 txs 就已经套用 candidate 就不需要再执行 interchangeable / 已经 previously executed interchangeable。」

## 为什么错

官方把 executes txs deterministically before returning control、Finalize + Commit 交差、Alternatively apply candidate state 写成独立的实现事。把它们卖成 fincand bundled、已经交差、已经像 Prepare 那样，会把 not committed、not like Prepare、not apply candidate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 executes txs deterministically not already committed 正式三事（460 余量），必须分开 not committed、not like Prepare、not apply candidate 三个名字，不要把它们卖成 fincand bundled / 已经交差 / 已经像 Prepare 那样。

## 和相邻反模式

- [fincand-sold-as-commit](fincand-sold-as-commit.md) 是 460 bundled 三事专用，不是本页 executes txs not committed 单句边界。
- [findet-sold-as-prepare](findet-sold-as-prepare.md) 是 470 findet 专用，不是本页 460 item 1 余量边界。
