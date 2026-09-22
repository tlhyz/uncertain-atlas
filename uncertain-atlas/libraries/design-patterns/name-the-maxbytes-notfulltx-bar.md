# 模式：把 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[MaxBytes 减去头集合证据才是交易上限 not already full-tx ≠ bundled（344）](../../tracks/implementation/worked-example-maxbytes-notfulltx-vs-bundled.md)。

## 三个名字

1. **完整块上限 不是 already full-tx：** 看见 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 完整块上限 / 填了块上限，不是已经整块都能装交易 interchangeable / 已经 full-tx interchangeable / 已经整块装交易交差 interchangeable，不是 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable。

2. **能装交易 不是 already evidence-max：** 看见能装交易 / 交易上限还在 / 扣开销之后的上限，不是已经是证据 MaxBytes interchangeable / 已经 evidence-max interchangeable / 已经证据那把尺交差 interchangeable，不是 331 evidencemaxbytes interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable。

3. **扣了开销 不是 already overhead-known：** 看见扣了开销 / 减去头集合证据 / 预期体积要扣，不是已经算出那几个字节 interchangeable / 已经 overhead-known interchangeable / 已经开销字节交差 interchangeable，不是 299 evidence-tx interchangeable / 787 maxbytes-nottimeoutfit interchangeable。

官方把完整块上限、交易上限还要扣开销、开销字节尚未算出写成三个名字。把它们叫成一个「看见填了 MaxBytes 就已经整块都能装交易 interchangeable / 就已经是证据 MaxBytes interchangeable / 就已经算出开销字节 interchangeable」，会把 not already full-tx、not already evidence-max、not already overhead-known 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量），先数清问的是完整块上限 是不是 already full-tx / 344 / maxbytesoverhead-sold-as-full，是不是能装交易 是不是 already evidence-max，还是扣了开销 是不是 already overhead-known，再决定要不要同一次发布。344 maxbytesoverhead vs full bundled unbundling 在本页 item 1 启动。
