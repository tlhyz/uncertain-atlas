# 模式：把 ConsensusParams.block not already MaxBytes cap / not already next_block_delay / not already settled 正式三事（385 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.block ≠ bundled（385）](../../tracks/implementation/worked-example-paramsblock-notmaxbytes-vs-bundled.md)。

## 三个名字

1. **block 不是已经是 MaxBytes 上限：** 看见填了 block，不是已经 337 interchangeable / 773 paramsblock-notmaxbytes interchangeable。
2. **看见填了 block 不是已经是 next_block_delay：** 看见能卡间隔，不是已经是 next_block_delay interchangeable。
3. **看见有字段 不是已经交差：** 看见 ConsensusParams.block，不是已经交差 interchangeable。

官方把 ConsensusParams.block / validator / version 三条核心句拆成三个名字。把它们叫成一个「看见填了 ConsensusParams 就已经是 MaxBytes 上限」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.block 正式三事（385 余量），先数清问的是是不是已经是 MaxBytes 上限 / 337、是不是已经是 next_block_delay、还是看见有字段是不是已经交差，再决定要不要同一次发布。385 paramsblock vs maxbytes bundled unbundling 在本页 item 1 启动。
