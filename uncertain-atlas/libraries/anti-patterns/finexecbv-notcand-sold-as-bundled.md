# 反模式：把 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量）卖成 FinalizeBlock When Application executes block v bundled / 已经 Process 跑过就不执行 / 已经 apply candidate

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When Application executes block v not apply candidate / Process already ran ≠ bundled（466）](../../tracks/implementation/worked-example-finexecbv-notcand-vs-bundled.md)。

## 卖法

- 「看见 Application executes block _v_ / execute according to FinalizeBlockRequest.txs 就已经 Process 跑过就不执行 interchangeable / 已经 FinalizeBlock When Application executes block v bundled interchangeable。」
- 「看见 may apply candidate from previous Prepare or Process 就已经 apply candidate interchangeable / 584 apply candidate interchangeable。」
- 「看见 Application executes block _v_ 就已经 Process 也会在提议者那边叫 interchangeable / 351 Process also on proposer interchangeable。」

## 为什么错

官方把 Application executes block _v_、execute according to txs、may apply candidate from previous Prepare or Process 写成独立的实现事。把它们卖成 FinalizeBlock When Application executes block v bundled、已经 Process 跑过就不执行、已经 apply candidate，会把 not Process already ran、not apply candidate / ExecuteTxState、not 351 Process also on proposer 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量），必须分开 not Process already ran / no need to execute、not apply candidate / ExecuteTxState、not 351 Process also on proposer 三个名字，不要把它们卖成 FinalizeBlock When Application executes block v bundled / 已经 Process 跑过就不执行 / 已经 apply candidate。

## 和相邻反模式

- [finexecbv-sold-as-bundled](finexecbv-sold-as-bundled.md) 是 466 bundled 三事专用，不是本页 not apply candidate / Process already ran 单句边界。
- [finexecbv-notpersist-sold-as-bundled](finexecbv-notpersist-sold-as-bundled.md) 是 573（466 item 1 余量）专用，不是本页 466 item 2 单句边界。
- [finprocgua-notcand-sold-as-bundled](finprocgua-notcand-sold-as-bundled.md) 是 584（360 item 3 余量）专用，不是本页 466 item 2 单句边界。
