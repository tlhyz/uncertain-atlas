# 反模式：把 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量）说成已经没进块 / 已经挡住拜占庭 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[拒了 not already excluded ≠ bundled（373）](../../tracks/implementation/worked-example-checktxopt-notexcluded-vs-bundled.md)。

## 卖法

把拒了 / `Code ≠ 0` 会被拒、不会广播也不会进提案 / 拒了交易 写成已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable / 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable；把没广播 / 不会广播 / 没广播给别的节点 写成已经被池子挡住拜占庭 interchangeable / 已经 blocked interchangeable / 已经挡住拜占庭交差 interchangeable；把没进提案 / 不会装进提案 / 没进提案 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 373 checktxopt bundled / checktxopt-sold-as-block interchangeable / 867 checktxopt-notexcluded interchangeable。

## 为什么错

官方把拒了、不是已经挡住拜占庭、不是已经交差写成三件独立的实现事。把它们卖成 already excluded interchangeable / already blocked interchangeable / already settled interchangeable，会把 not already excluded、not already blocked、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量），必须分开 not already excluded、not already blocked、not already settled 三件事，不要和 373 / 316 / 339 / 866 糊成一句。

## 和相邻反模式

- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 checktxopt bundled 全段，不是本页拒了 item 2 单句边界。
- [checktxopt-notfourgates-sold-as-bundled](checktxopt-notfourgates-sold-as-bundled.md) 是能回 not already fourgates（373 item 1），不是本页 not already excluded 边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Finalize 的 Code 非零就已经没进块（316），不是本页 not already excluded 单句。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
