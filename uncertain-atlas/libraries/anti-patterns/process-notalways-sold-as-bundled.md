# 反模式：把失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量）说成已经每轮都会叫 / 已经是这一次刚回的那份 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[失败时可能对上更早一次或根本不调 not already every-round ≠ bundled（351）](../../tracks/implementation/worked-example-process-notalways-vs-bundled.md)。

## 卖法

把进了这一轮 / 失败时可能对上更早一次或根本不调 / 失败时不保证 写成已经每轮都会叫 Process interchangeable / 已经 every-round interchangeable / 已经每轮都会叫交差 interchangeable / 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable；把叫了 Process / `ProcessProposalRequest` 可能对上更早一次 Prepare 的回包 写成已经是这一次刚回的那份 interchangeable / 已经 this-prepare interchangeable / 已经是这一次交差 interchangeable；把失败了 / 根本不调 Process 写成已经交差 interchangeable / 已经 crossed interchangeable / 已经交差交差 interchangeable，或已经和 351 processalso bundled / processalso-sold-as-matched interchangeable / 808 process-notalways interchangeable。

## 为什么错

官方把失败时不保证、不是已经是这一次刚回的那份、不是已经交差写成三件独立的实现事。把它们卖成 already every-round interchangeable / already this-prepare interchangeable / already crossed interchangeable，会把 not already every-round、not already this-prepare、not already crossed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看失败时可能对上更早一次或根本不调不是已经每轮都会叫 not already every-round / not already this-prepare / not already crossed 正式三事（351 余量），必须分开 not already every-round、not already this-prepare、not already crossed 三件事，不要和 351 / 33 / 311 / 806 / 807 糊成一句。

## 和相邻反模式

- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫 bundled 全段，不是本页失败路径 item 3 单句边界。
- [process-notguaranteed-sold-as-bundled](process-notguaranteed-sold-as-bundled.md) 是通常紧跟 Prepare、列表对得上 not already guaranteed-this（351 item 2），不是本页 not already every-round 边界。
- [process-notskip-sold-as-bundled](process-notskip-sold-as-bundled.md) 是 Process 也会在提议者那边叫 not already skip-process（351 item 1），不是本页 not already crossed 边界。
