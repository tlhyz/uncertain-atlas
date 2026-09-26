# 反模式：把 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量）说成已经对上 AppHash / 已经是一层树 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[勾了 prove not already matched ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notmatched-vs-bundled.md)。

## 卖法

把勾了 prove / Query 请求 prove 是能回就回默克尔证明 / prove 是能回就随回包带回默克尔证明 写成已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable / 383 queryprove bundled interchangeable / queryprove-sold-as-proof interchangeable；把能回证明 / 能回就带回默克尔证明 / 随回包带回证明 写成已经是一层树 interchangeable / 已经 tree interchangeable / 已经是一层树交差 interchangeable；把请求了 / 请求了 prove / 勾了请求 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 383 queryprove bundled / queryprove-sold-as-proof interchangeable / 896 queryprove-notmatched interchangeable。

## 为什么错

官方把勾了 prove、不是已经是一层树、不是已经交差写成三件独立的实现事。把它们卖成 already matched interchangeable / already tree interchangeable / already settled interchangeable，会把 not already matched、not already tree、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量），必须分开 not already matched、not already tree、not already settled 三件事，不要和 383 / 325 / 380 / 316 糊成一句。

## 和相邻反模式

- [queryprove-sold-as-proof](queryprove-sold-as-proof.md) 是 queryprove bundled 全段，不是本页勾了 prove item 1 单句边界。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash（325），不是本页 not already matched 边界。
- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 Query 回包 value 就已经对上 AppHash（380），不是本页 not already tree 单句。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序（316），不是本页 not already settled 边界。
