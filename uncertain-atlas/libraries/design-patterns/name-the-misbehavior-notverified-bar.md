# 模式：把 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**例**：[有高度 not already verified ≠ bundled（372）](../../tracks/implementation/worked-example-misbehavior-notverified-vs-bundled.md)。

## 三个名字

1. **有高度 不是 already verified：** 看见有高度 / `height` 是过错发生的高度 / 有高度，不是已经验过票上的时间 interchangeable / 已经 verified interchangeable / 已经验过票上的时间交差 interchangeable，不是 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable。

2. **有时间 不是 already settled：** 看见有时间 / `time` 是那一高已提交块的时间 / 有时间戳，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 304 Timestamp verified interchangeable / 863 misbehavior-notslashed interchangeable。

3. **对上了高度 不是 already plus23：** 看见对上了高度 / 高度对上 / 过错高度对上，不是已经是本高 +2/3 interchangeable / 已经 plus23 interchangeable / 已经是本高 +2/3 交差 interchangeable，不是 148 LastCommit interchangeable / 372 misbehavior item 3 interchangeable。

官方把有高度、不是已经交差、不是已经是本高 +2/3 写成三个名字。把它们叫成一个「看见有高度就已经验过票上的时间 interchangeable / 就已经交差 interchangeable / 就已经是本高 +2/3 interchangeable」，会把 not already verified、not already settled、not already plus23 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量），先数清问的是有高度 是不是 already verified / 372 / misbehavior-sold-as-enum，是不是有时间 是不是 already settled，还是对上了高度 是不是 already plus23，再决定要不要同一次发布。372 misbehavior-vs-enum bundled unbundling 在本页 item 2 续。
