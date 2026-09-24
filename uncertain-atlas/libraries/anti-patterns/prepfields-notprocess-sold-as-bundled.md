# 反模式：把 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量）说成已经跑过 Process / 已经 Finalize / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[同一套字段 not already ran-process ≠ bundled（359）](../../tracks/implementation/worked-example-prepfields-notprocess-vs-bundled.md)。

## 卖法

把字段名对得上 / `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套 / 同一套字段 写成已经跑过 Process interchangeable / 已经 ran-process interchangeable / 已经叫过 Process 交差 interchangeable / 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable；把同一套 / 和 Process / Finalize 同一套 写成已经 Finalize interchangeable / 已经 finalize interchangeable / 已经 Finalize 交差 interchangeable；把请求在 / Prepare 请求在 / 同一套字段进了请求 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 359 preparefields bundled / preparefields-sold-as-same interchangeable / 830 prepfields-notprocess interchangeable。

## 为什么错

官方把字段名对得上、不是已经 Finalize、不是已经交差写成三件独立的实现事。把它们卖成 already ran-process interchangeable / already finalize interchangeable / already settled interchangeable，会把 not already ran-process、not already finalize、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process not already ran-process / not already finalize / not already settled 正式三事（359 余量），必须分开 not already ran-process、not already finalize、not already settled 三件事，不要和 359 / 351 / 330 / 831 / 832 糊成一句。

## 和相邻反模式

- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 请求字段 bundled 全段，不是本页字段名对得上 item 1 单句边界。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫就已经不用再 Process（351），不是本页 not already ran-process 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
