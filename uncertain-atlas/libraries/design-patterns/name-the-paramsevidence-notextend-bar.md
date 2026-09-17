# 模式：把 ConsensusParams.abci not already Prepare extension / not already ABCI 2.0 / not already settled 正式三事（386 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.abci ≠ bundled（386）](../../tracks/implementation/worked-example-paramsevidence-notextend-vs-bundled.md)。

## 三个名字

1. **abci 不是已经 Prepare 带了扩展：** 看见填了 abci，不是已经 330 interchangeable / 771 paramsevidence-notextend interchangeable。
2. **看见填了 abci 不是已经切到 ABCI 2.0：** 看见有 ABCI 栏，不是已经 330 interchangeable。
3. **看见能填 不是已经交差：** 看见 ConsensusParams.abci，不是已经交差 interchangeable。

官方把 ConsensusParams.evidence / abci / synchrony 三条核心句拆成三个名字。把它们叫成一个「看见填了余下三栏就已经是证据 MaxBytes」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.abci 正式三事（386 余量），先数清问的是是不是已经 Prepare 带了扩展 / 330、是不是已经切到 ABCI 2.0、还是看见能填是不是已经交差，再决定要不要同一次发布。386 paramsevidence vs maxbytes bundled unbundling 在本页 item 2 续。
