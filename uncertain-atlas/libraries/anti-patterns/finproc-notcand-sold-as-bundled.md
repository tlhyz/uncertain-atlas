# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee not apply candidate 正式三事（472 余量）卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经套用 candidate 就不需要 guarantee / 已经 Process MAY 整块执行

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not apply candidate ≠ bundled（472）](../../tracks/implementation/worked-example-finproc-notcand-vs-bundled.md)。

## 卖法

- 「看见 has run ProcessProposal on that block / 看见对这块跑过 Process 就已经套用 candidate / previously executed 就不需要 Process 保证 interchangeable。」
- 「看见 has run 就已经 ProcessProposal MAY 整块执行交差 interchangeable / 已经 candidate state interchangeable。」
- 「看见 has run 就已经 VVE hash 指拟议块无 guarantee interchangeable / 已经 exposed via ProcessProposal interchangeable。」

## 为什么错

官方把 has run `ProcessProposal` on that block、apply candidate / previously executed、Process MAY fully execute、VVE 拟议块无保证 写成三件独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经套用 candidate 就不需要 guarantee、已经 Process MAY 整块执行，会把 not apply candidate、not MAY execute committed、not VVE proposed no guarantee 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not apply candidate 正式三事（472 余量），必须分开 has run not apply candidate / previously executed、has run not Process MAY fully execute committed、has run on decided block not VVE proposed no guarantee 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经套用 candidate 就不需要 guarantee / 已经 Process MAY 整块执行。

## 和相邻反模式

- [finproc-sold-as-allvalidators](finproc-sold-as-allvalidators.md) 是 472 bundled 三事专用，不是本页 has run not apply candidate 单句边界。
- [fincand-sold-as-commit](fincand-sold-as-commit.md) 是 460 套用候选三事，不是本页 has run not apply candidate 单句边界。
