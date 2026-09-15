# 反模式：把 FinalizeBlock fill all fields not no need to provide again 正式三事（473 余量）卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经不用再给 / 已经 360 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not no need to provide again ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notrefill-vs-bundled.md)。

## 卖法

- 「看见 Currently / CometBFT will fill up all fields in FinalizeBlockRequest 就已经不用再 Finalize interchangeable / 已经 Prepare / Process 给过就不用再 Finalize interchangeable。」
- 「看见 will fill up all fields 就已经 Finalize 时的 Process 保证 bundled interchangeable / 360 bundled interchangeable。」
- 「看见再填一遍 就已经 Finalize 请求把字段再填一遍 not no need to provide again interchangeable / 583 not refill interchangeable。」

## 为什么错

官方把 will fill up all fields、Finalize 时的 Process 保证 bundled、360 item 2 refill 单句 写成独立的实现事。把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled、已经不用再给、已经 360 bundled，会把 not no need to provide again、not 360 bundled、not 583 not refill 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not no need to provide again 正式三事（473 余量），必须分开 not no need to provide again、not Finalize 时的 Process 保证 bundled、not 583 not refill 三个名字，不要把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经不用再给 / 已经 360 bundled。

## 和相邻反模式

- [finfill-sold-as-bundled](finfill-sold-as-bundled.md) 是 473 bundled 三事专用，不是本页 fill all fields not no need to provide again 单句边界。
- [finprocgua-notrefill-sold-as-bundled](finprocgua-notrefill-sold-as-bundled.md) 是 583 / 360 item 2 专用，不是本页 473 item 1 单句边界。
