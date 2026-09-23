# 反模式：把 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量）说成已经还会调 Prepare / 已经能再改列表 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[validValue 非 nil not already still-prepare ≠ bundled（356）](../../tracks/implementation/worked-example-vv-notstillprepare-vs-bundled.md)。

## 卖法

把 validValue 非 nil / 本轮直接用它 / 直接用了 写成已经还会调 Prepare interchangeable / 已经 still-prepare interchangeable / 已经还会调 Prepare 交差 interchangeable / 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable；把有 validValue / 非 nil 写成已经能再改列表 interchangeable / 已经 can-revise interchangeable / 已经能再改列表交差 interchangeable；把锁住了 / 用了 validValue / 本轮锁住 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 356 validvalue bundled / validvalue-sold-as-prepared interchangeable / 821 vv-notstillprepare interchangeable。

## 为什么错

官方把直接用了、不是已经能再改列表、不是已经交差写成三件独立的实现事。把它们卖成 already still-prepare interchangeable / already can-revise interchangeable / already settled interchangeable，会把 not already still-prepare、not already can-revise、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量），必须分开 not already still-prepare、not already can-revise、not already settled 三件事，不要和 356 / 311 / 338 / 822 / 823 糊成一句。

## 和相邻反模式

- [validvalue-sold-as-prepared](validvalue-sold-as-prepared.md) 是 validValue 跳过 Prepare bundled 全段，不是本页直接用了 item 1 单句边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选已经是 ExecuteTxState（311），不是本页 not already still-prepare 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
