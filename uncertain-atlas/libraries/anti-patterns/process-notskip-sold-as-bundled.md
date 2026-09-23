# 反模式：把 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量）说成已经不用再 Process / 已经交差 / 已经过了 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Process 也会在提议者那边叫 not already skip-process ≠ bundled（351）](../../tracks/implementation/worked-example-process-notskip-vs-bundled.md)。

## 卖法

把 `ProcessProposal` 也会在这一轮的提议者那边叫 / 自己刚 Prepare 过 / 自己刚回了 Prepare 写成已经不用再 Process interchangeable / 已经 skip-process interchangeable / 已经跳过 Process 交差 interchangeable / 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable；把是提议者 / 这一轮是自己提议 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把列表自己编的 / txs 自己刚回 写成已经过了 Process interchangeable / 已经 already-processed interchangeable / 已经过 Process 交差 interchangeable，或已经和 351 processalso bundled / processalso-sold-as-matched interchangeable / 806 process-notskip interchangeable。

## 为什么错

官方把 Process 也会在提议者那边叫、不是已经交差、不是已经过了 Process 写成三件独立的实现事。把它们卖成 already skip-process interchangeable / already settled interchangeable / already already-processed interchangeable，会把 not already skip-process、not already settled、not already already-processed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 也会在提议者那边叫不是已经不用再 Process not already skip-process / not already settled / not already already-processed 正式三事（351 余量），必须分开 not already skip-process、not already settled、not already already-processed 三件事，不要和 351 / 33 / 311 / 807 / 808 糊成一句。

## 和相邻反模式

- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫 bundled 全段，不是本页 Process 也会在提议者那边叫 item 1 单句边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already skip-process 边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选不是已经是 ExecuteTxState（311），不是本页 not already already-processed 边界。
