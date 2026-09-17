# 反模式：把 FinalizeBlock When Application executes block v 卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经 persist decision / 已经 Process 跑过就不执行 / 已经 +2/3 precommit decided

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When Application executes block v ≠ bundled](../../tracks/implementation/worked-example-finexecbv-bundled.md)。

## 卖法

- 「看见 Application executes block _v_ / When 第 3 步 executes block _v_ 就已经 persist decision interchangeable / 已经 FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable。」
- 「看见 execute according to `FinalizeBlockRequest.txs` 就已经 Process 跑过就不执行 interchangeable / 584 apply candidate interchangeable。」
- 「看见 Application executes block _v_ 就已经 +2/3 precommit decided interchangeable / 362 +2/3 precommit interchangeable / 已经 ResultHash interchangeable。」

## 为什么错

官方把 When 第 3 步 Application executes block _v_、Usage 里 execute according to txs / may apply candidate、When 流程 +2/3 precommit 决定 / ResultHash 写成独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经 persist decision、已经 Process 跑过就不执行、已经 +2/3 precommit decided，会把 not persist decision / When calling guarantee、not apply candidate / Process already ran、not +2/3 precommit decided / ResultHash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v，必须分开 not persist decision / When calling guarantee、not Process already ran / apply candidate、not +2/3 precommit decided / ResultHash 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经 persist decision / 已经 Process 跑过就不执行 / 已经 +2/3 precommit decided。

## 和相邻反模式

- [finwhen-sold-as-bundled](finwhen-sold-as-bundled.md) 是 472 bundled 三事专用，不是本页 finexecbv bundled 三事边界。
- [finwhen-notexecbv-sold-as-bundled](finwhen-notexecbv-sold-as-bundled.md) 是 572（472 item 3 余量）专用，不是本页 466 parent bundled 边界。
- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是 362 When 流程专用，不是本页 executes block v not +2/3 precommit decided 单句边界。
- [finprocgua-notcand-sold-as-bundled](finprocgua-notcand-sold-as-bundled.md) 是 584（360 item 3 余量）专用，不是本页 executes block v not apply candidate 单句边界。
