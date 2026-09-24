# 模式：把 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[+2/3 precommit 才决定再调 not already will-call ≠ bundled（362）](../../tracks/implementation/worked-example-finwhen-notwillcall-vs-bundled.md)。

## 三个名字

1. **到了这一高 不是 already will-call：** 看见到了这一高 / 收到提案和全部块片、并且 +2/3 precommit 同一 `id(v)` 才决定再调 Finalize / 到了这一高，不是已经会调 Finalize interchangeable / 已经 will-call interchangeable / 已经会调交差 interchangeable，不是 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable。

2. **有提案 不是 already decided：** 看见有提案 / 有提案 *v* 和全部块片 / 同一 `id(v)` 的 +2/3 precommit，不是已经决定 interchangeable / 已经 decided interchangeable / 已经决定 *v* 交差 interchangeable，不是 361 extendwhen interchangeable / 837 finwhen-notpersist interchangeable。

3. **规范写了 When 不是 already settled：** 看见规范写了 When / When 条款在 / 决定再调写进了规范，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 838 finwhen-notprinted interchangeable / 33 fourgates interchangeable。

官方把到了这一高、不是已经决定、不是已经交差写成三个名字。把它们叫成一个「看见到了这一高就已经会调 Finalize interchangeable / 就已经决定 interchangeable / 就已经交差 interchangeable」，会把 not already will-call、not already decided、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize not already will-call / not already decided / not already settled 正式三事（362 余量），先数清问的是到了这一高 是不是 already will-call / 362 / finalizewhen-sold-as-decided，是不是有提案 是不是 already decided，还是规范写了 When 是不是 already settled，再决定要不要同一次发布。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。
