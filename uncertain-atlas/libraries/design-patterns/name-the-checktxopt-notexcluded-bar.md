# 模式：把 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[拒了 not already excluded ≠ bundled（373）](../../tracks/implementation/worked-example-checktxopt-notexcluded-vs-bundled.md)。

## 三个名字

1. **拒了 不是 already excluded：** 看见拒了 / `Code ≠ 0` 会被拒、不会广播也不会进提案 / 拒了交易，不是已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable，不是 373 checktxopt bundled interchangeable / checktxopt-sold-as-block interchangeable。

2. **没广播 不是 already blocked：** 看见没广播 / 不会广播 / 没广播给别的节点，不是已经被池子挡住拜占庭 interchangeable / 已经 blocked interchangeable / 已经挡住拜占庭交差 interchangeable，不是 339 CheckTx weak interchangeable / 866 checktxopt-notfourgates interchangeable。

3. **没进提案 不是 already settled：** 看见没进提案 / 不会装进提案 / 没进提案，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 33 four gates interchangeable / 373 checktxopt item 3 interchangeable。

官方把拒了、不是已经挡住拜占庭、不是已经交差写成三个名字。把它们叫成一个「看见拒了就已经没进块 interchangeable / 就已经挡住拜占庭 interchangeable / 就已经交差 interchangeable」，会把 not already excluded、not already blocked、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 余量），先数清问的是拒了 是不是 already excluded / 373 / checktxopt-sold-as-block，是不是没广播 是不是 already blocked，还是没进提案 是不是 already settled，再决定要不要同一次发布。373 checktxopt-vs-block bundled unbundling 在本页 item 2 续。
