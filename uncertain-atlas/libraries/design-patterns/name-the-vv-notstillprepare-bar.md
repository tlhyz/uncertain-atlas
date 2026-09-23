# 模式：把 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**例**：[validValue 非 nil not already still-prepare ≠ bundled（356）](../../tracks/implementation/worked-example-vv-notstillprepare-vs-bundled.md)。

## 三个名字

1. **直接用了 不是 already still-prepare：** 看见 validValue 非 nil / 本轮直接用它 / 直接用了，不是已经还会调 Prepare interchangeable / 已经 still-prepare interchangeable / 已经还会调 Prepare 交差 interchangeable，不是 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable。

2. **有 validValue 不是 already can-revise：** 看见有 validValue / 非 nil / 本轮有 validValue，不是已经能再改列表 interchangeable / 已经 can-revise interchangeable / 已经能再改列表交差 interchangeable，不是 355 preparedrop interchangeable / 822 vv-noteveryround interchangeable。

3. **锁住了 不是 already settled：** 看见锁住了 / 用了 validValue / 本轮锁住，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 823 vv-notraw interchangeable / 33 fourgates interchangeable。

官方把直接用了、不是已经能再改列表、不是已经交差写成三个名字。把它们叫成一个「看见直接用了就已经还会调 Prepare interchangeable / 就已经能再改列表 interchangeable / 就已经交差 interchangeable」，会把 not already still-prepare、not already can-revise、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量），先数清问的是直接用了 是不是 already still-prepare / 356 / validvalue-sold-as-prepared，是不是有 validValue 是不是 already can-revise，还是锁住了 是不是 already settled，再决定要不要同一次发布。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。
