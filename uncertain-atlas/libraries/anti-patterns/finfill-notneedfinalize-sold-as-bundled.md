# 反模式：把 FinalizeBlock fill all fields not already don't need Finalize 正式三事（473 余量）卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经 Prepare/Process 给过就不用再 Finalize / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not already don't need Finalize ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notneedfinalize-vs-bundled.md)。

## 卖法

- 「看见 Currently, CometBFT will fill up all fields in `FinalizeBlockRequest` / 看见引擎会把 Finalize 请求全部字段填齐 就已经 Prepare / Process 给过就不用再 Finalize interchangeable。」
- 「看见 will fill up all fields 就已经 Finalize + Commit 交差 interchangeable / 已经 committed interchangeable。」
- 「看见 will fill up all fields 就已经 Contains newly decided block fields bundled interchangeable / 已经 fill all fields interchangeable。」

## 为什么错

官方把 Currently / CometBFT will fill up all fields in `FinalizeBlockRequest`、Prepare/Process 已经传过就不叫 Finalize、Finalize + Commit 已经交差写成三件独立的实现事。把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled、已经 Prepare/Process 给过就不用再 Finalize、已经交差，会把 not don't need Finalize、not already committed、not Contains bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not already don't need Finalize 正式三事（473 余量），必须分开 will fill up not don't need Finalize、will fill up not already committed、will fill up not Contains bundled 三个名字，不要把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经 Prepare/Process 给过就不用再 Finalize / 已经交差。

## 和相邻反模式

- [finfill-sold-as-norepeat](finfill-sold-as-norepeat.md) 是 473 bundled 三事专用，不是本页 will fill up not don't need Finalize 单句边界。
- [finnewfields-notdecprop-sold-as-bundled](finnewfields-notdecprop-sold-as-bundled.md) 是 558 461 bundled item 3 余量，不是本页 473 item 1 边界。
