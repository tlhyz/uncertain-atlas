# 反模式：把 Finalize 请求把字段再填一遍 not no need to provide again 正式三事（360 余量）卖成 Finalize 时的 Process 保证 bundled / 已经不用再给 / 已经跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Finalize 请求把字段再填一遍 not no need to provide again ≠ bundled（360）](../../tracks/implementation/worked-example-finprocgua-notrefill-vs-bundled.md)。

## 卖法

- 「看见 Currently / CometBFT will fill up all fields in FinalizeBlockRequest 就已经 Prepare / Process 给过就不用再 Finalize interchangeable / 已经不用再给 interchangeable。」
- 「看见 even if already passed via PrepareProposalRequest or ProcessProposalRequest 就已经字段名对得上就代表已经跑过 Process interchangeable / 已经 Prepare 和 Process / Finalize 同一套字段 interchangeable。」
- 「看见 all fields / 又填一遍 / 请求齐了 就已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable。」

## 为什么错

官方把 will fill up all fields、even if already passed、all fields refilled 写成独立的实现事。把它们卖成 Finalize 时的 Process 保证 bundled、已经不用再给、已经跑过 Process，会把 not no need to provide again、not field names match、not request complete means committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求把字段再填一遍 not no need to provide again 正式三事（360 余量），必须分开 not no need to provide again、not field names match means ran Process、not request complete means committed 三个名字，不要把它们卖成 Finalize 时的 Process 保证 bundled / 已经不用再给 / 已经跑过 Process。

## 和相邻反模式

- [finalize-sold-as-processed](finalize-sold-as-processed.md) 是 360 bundled 三事专用，不是本页 refill not no need to provide again 单句边界。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 359 专用，不是本页 even if passed not field names match 单句边界。
