# 模式：把 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[+2/3 prevote 才锁住再调 not already will-call ≠ bundled（361）](../../tracks/implementation/worked-example-extwhen-notwillcall-vs-bundled.md)。

## 三个名字

1. **到了 prevote 步 不是 already will-call：** 看见到了 prevote 步 / 收到提案和全部块片、并且 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote / 到了 prevote 步，不是已经会调 ExtendVote interchangeable / 已经 will-call interchangeable / 已经会调交差 interchangeable，不是 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable。

2. **有提案 不是 already locked-value：** 看见有提案 / 有提案 *v* 和全部块片 / 同一 `id(v)` 的 +2/3 prevote，不是已经锁住 interchangeable / 已经 locked-value interchangeable / 已经锁住 *v* 交差 interchangeable，不是 350 extendonce interchangeable / 834 extwhen-notlaterrevise interchangeable。

3. **规范写了 When 不是 already settled：** 看见规范写了 When / When 条款在 / 锁住再调写进了规范，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 835 extwhen-notsameext interchangeable / 33 fourgates interchangeable。

官方把到了 prevote 步、不是已经锁住、不是已经交差写成三个名字。把它们叫成一个「看见到了 prevote 步就已经会调 ExtendVote interchangeable / 就已经锁住 interchangeable / 就已经交差 interchangeable」，会把 not already will-call、not already locked-value、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote not already will-call / not already locked-value / not already settled 正式三事（361 余量），先数清问的是到了 prevote 步 是不是 already will-call / 361 / extendwhen-sold-as-locked，是不是有提案 是不是 already locked-value，还是规范写了 When 是不是 already settled，再决定要不要同一次发布。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。
