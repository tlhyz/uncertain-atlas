# 模式：把 ConsensusParams.evidence not already evidence MaxBytes / not already unbonding / not already settled 正式三事（386 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.evidence ≠ bundled（386）](../../tracks/implementation/worked-example-paramsevidence-notmaxbytes-vs-bundled.md)。

## 三个名字

1. **evidence 不是已经是证据 MaxBytes：** 看见填了 evidence，不是已经 331 interchangeable / 770 paramsevidence-notmaxbytes interchangeable。
2. **看见填了 evidence 不是已经盖住解绑：** 看见能限证据，不是已经盖住解绑 interchangeable。
3. **看见有字段 不是已经交差：** 看见 ConsensusParams.evidence，不是已经交差 interchangeable。

官方把 ConsensusParams.evidence / abci / synchrony 三条核心句拆成三个名字。把它们叫成一个「看见填了余下三栏就已经是证据 MaxBytes」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.evidence 正式三事（386 余量），先数清问的是是不是已经是证据 MaxBytes / 331、是不是已经盖住解绑、还是看见有字段是不是已经交差，再决定要不要同一次发布。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 1 启动。
