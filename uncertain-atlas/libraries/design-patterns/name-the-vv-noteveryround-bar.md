# 模式：把自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**例**：[自己是提议者 not already will-call ≠ bundled（356）](../../tracks/implementation/worked-example-vv-noteveryround-vs-bundled.md)。

## 三个名字

1. **是提议者 不是 already will-call：** 看见自己是提议者 / 是提议者 / *p* 是提议者，不是已经会调 Prepare interchangeable / 已经 will-call interchangeable / 已经会调 Prepare 交差 interchangeable，不是 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable。

2. **进了这一轮 不是 already vv-nil：** 看见进了这一轮 / 进入一轮 *r* / 进了高度 *h*，不是已经是 validValue 为 nil interchangeable / 已经 vv-nil interchangeable / 已经 validValue 为 nil 交差 interchangeable，不是 338 preparenondet interchangeable / 821 vv-notstillprepare interchangeable。

3. **规范写了 When 不是 already every-round：** 看见规范写了 When / When 写了调 Prepare / 规范写了才会调，不是已经每轮都会调 Prepare interchangeable / 已经 every-round interchangeable / 已经每轮都会调交差 interchangeable，不是 823 vv-notraw interchangeable / 33 fourgates interchangeable。

官方把是提议者、不是已经是 validValue 为 nil、不是已经每轮都会调写成三个名字。把它们叫成一个「看见是提议者就已经会调 interchangeable / 就已经是 validValue 为 nil interchangeable / 就已经每轮都会叫 interchangeable」，会把 not already will-call、not already vv-nil、not already every-round 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量），先数清问的是是提议者 是不是 already will-call / 356 / validvalue-sold-as-prepared，是不是进了这一轮 是不是 already vv-nil，还是规范写了 When 是不是 already every-round，再决定要不要同一次发布。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。
