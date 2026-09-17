# 反模式：把 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事（473 余量）卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / decided 和 proposed 就可以混用 / Prepare/Process 传过 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not decided/proposed interchangeable ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notdecprop-vs-bundled.md)。

## 卖法

- 「看见 all fields / 又填一遍 就已经 `FinalizeBlockRequest.decided_last_commit` 和 `ProcessProposalRequest.proposed_last_commit` 就可以混用 interchangeable / 已经 decided 和 proposed 就可以混用 interchangeable。」
- 「看见 all fields 就已经 Prepare / Process 传过就意味着 decided 和 proposed 语义 interchangeable / 已经 newly decided 和 proposed interchangeable。」
- 「看见 all fields 就已经 Finalize 专有栏和 Prepare / Process 同一套字段名对上就够 interchangeable / 已经字段再填一遍 interchangeable。」

## 为什么错

官方把 fill up all fields in FinalizeBlockRequest、decided_last_commit vs proposed_last_commit 语义、Prepare/Process 传过和 decided vs proposed、`syncing_to_height` 等 Finalize 专有栏写成三件独立的实现事。把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled、decided 和 proposed 就可以混用、Prepare/Process 传过 interchangeable，会把 not decided/proposed、not Prepare/Process passed means decided/proposed、not Finalize 专有栏 same as Prepare/Process 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事（473 余量），必须分开 all fields not decided/proposed interchangeable、all fields not Prepare/Process passed means decided/proposed interchangeable、all fields not Finalize 专有栏 same as Prepare/Process interchangeable 三个名字，不要把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / decided 和 proposed 就可以混用 / Prepare/Process 传过 interchangeable。

## 和相邻反模式

- [finfill-notneedfinalize-sold-as-bundled](finfill-notneedfinalize-sold-as-bundled.md) 是 562 473 item 1 余量，不是本页 all fields not decided/proposed 单句边界。
- [finfill-notpassedran-sold-as-bundled](finfill-notpassedran-sold-as-bundled.md) 是 563 473 item 2 余量，不是本页 Prepare/Process passed means decided/proposed 边界。
- [finnewfields-notdecprop-sold-as-bundled](finnewfields-notdecprop-sold-as-bundled.md) 是 558 461 bundled item 3 余量，不是本页 473 bundled item 3 边界。
