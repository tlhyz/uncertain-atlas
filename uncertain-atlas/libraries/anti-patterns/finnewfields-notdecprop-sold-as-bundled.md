# 反模式：把 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事卖成 FinalizeBlock 含刚决定那块字段 bundled / 已经 decided 和 proposed 就可以混用 / 已经 Prepare/Process 传过 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not decided/proposed interchangeable ≠ bundled](../../tracks/implementation/worked-example-finnewfields-notdecprop-vs-bundled.md)。

## 卖法

- 「看见 CometBFT 会把 FinalizeBlockRequest 全部字段填齐、即使 Prepare/Process 已经传过 / 看见又填一遍 就已经 decided_last_commit 和 proposed_last_commit 就可以混用 interchangeable / 已经 FinalizeBlock 含刚决定那块字段 bundled interchangeable。」
- 「看见 even if Prepare / Process 已经传过 就已经 newly decided 和 proposed 字段 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable。」
- 「看见引擎填齐 就已经跑过 Process 就不需要 Finalize interchangeable / 已经 Prepare/Process 传过 interchangeable / 已经交差 interchangeable。」

## 为什么错

官方把 fill up all fields in FinalizeBlockRequest even if passed、decided_last_commit vs proposed_last_commit、even if passed 和 newly decided vs proposed 对象写成三件独立的实现事。把它们卖成 FinalizeBlock 含刚决定那块字段 bundled、已经 decided 和 proposed 就可以混用、已经 Prepare/Process 传过 interchangeable，会把 fill all fields not decided/proposed、fill all fields not newly decided/proposed、fill all fields not ran Process means don't need Finalize 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事，必须分开 fill all fields not decided/proposed interchangeable、fill all fields not newly decided/proposed interchangeable、fill all fields not ran Process means don't need Finalize 三个名字，不要把它们卖成 FinalizeBlock 含刚决定那块字段 bundled / 已经 decided 和 proposed 就可以混用 / 已经 Prepare/Process 传过 interchangeable。

## 和相邻反模式

- [finnewfields-sold-as-settled](finnewfields-sold-as-settled.md) 是 461 bundled 三事专用，不是本页 fill all fields not decided/proposed interchangeable 单句边界。
- [finfill-sold-as-norepeat](finfill-sold-as-norepeat.md) 是 473 fill all fields even if passed bundled，不是本页 461 item 3 单句边界。
- [finnewfields-notprocfull-sold-as-bundled](finnewfields-notprocfull-sold-as-bundled.md) 是 newly decided vs Process contains all information，不是本页 fill all fields vs decided/proposed 边界。
