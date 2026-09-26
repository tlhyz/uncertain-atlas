# 模式：把 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**例**：[勾了 prove not already matched ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notmatched-vs-bundled.md)。

## 三个名字

1. **勾了 prove 不是 already matched：** 看见勾了 prove / Query 请求 prove 是能回就回默克尔证明 / prove 是能回就随回包带回默克尔证明，不是已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable，不是 383 queryprove bundled interchangeable / queryprove-sold-as-proof interchangeable。

2. **能回证明 不是 already tree：** 看见能回证明 / 能回就带回默克尔证明 / 随回包带回证明，不是已经是一层树 interchangeable / 已经 tree interchangeable / 已经是一层树交差 interchangeable，不是 325 queryproof interchangeable / 383 queryprove item 2 interchangeable。

3. **请求了 不是 already settled：** 看见请求了 / 请求了 prove / 勾了请求，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 316 txresults interchangeable / 383 queryprove item 3 interchangeable。

官方把勾了 prove、不是已经是一层树、不是已经交差写成三个名字。把它们叫成一个「看见勾了 prove 就已经对上 AppHash interchangeable / 就已经是一层树 interchangeable / 就已经交差 interchangeable」，会把 not already matched、not already tree、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量），先数清问的是勾了 prove 是不是 already matched / 383 / queryprove-sold-as-proof，是不是能回证明 是不是 already tree，还是请求了 是不是 already settled，再决定要不要同一次发布。383 queryprove-vs-proof bundled unbundling 在本页 item 1 启动。
