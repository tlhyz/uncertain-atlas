# 反模式：把丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量）说成已经能无界攒着 / 已经永远不用再跑 / 规范已经写死条数

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[丢掉候选 not already can unboundedly accumulate ≠ bundled（311）](../../tracks/implementation/worked-example-candidate-notdiscarded-vs-bundled.md)。

## 卖法

把候选很多 / 还没 Finalize / 一轮高度披露很多提案 写成已经能无界攒着 interchangeable / 已经 can unboundedly accumulate interchangeable / 已经能一直攒 interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable；把丢掉了 / Finalize 之前丢掉候选 写成已经永远不用再跑 interchangeable / 已经 never need re-execute interchangeable；把看见有上界 / 自己限制了内存 写成规范已经写死条数 interchangeable / 已经 bound by spec interchangeable，或已经和 311 candidate bundled / candidate-sold-as-execute interchangeable / 694 candidate-notdiscarded interchangeable。

## 为什么错

官方把候选很多单句、already can unboundedly accumulate、already never need re-execute、already bound by spec 写成三件独立的实现事。把它们卖成 already can unboundedly accumulate interchangeable / already never need re-execute interchangeable / already bound by spec interchangeable，会把 not already can unboundedly accumulate、not already never need re-execute、not already bound by spec 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量），必须分开 not already can unboundedly accumulate、not already never need re-execute、not already bound by spec 三件事，不要和 311 / 33 / 692 / 693 / 5 / 310 糊成一句。

## 和相邻反模式

- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选 ≠ ExecuteTxState bundled 全段，不是本页丢掉候选 item 3 单句边界。
- [candidate-notexecute-sold-as-bundled](candidate-notexecute-sold-as-bundled.md) 是候选 not ExecuteTxState item 2，不是本页丢掉 ≠ 永远不用再跑边界。
- [candidate-notheader-sold-as-bundled](candidate-notheader-sold-as-bundled.md) 是 Prepare 没有头哈希 item 1，不是本页还没 Finalize ≠ 能无界攒着边界。
