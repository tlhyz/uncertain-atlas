# 模式：把 ConsensusParams.validator not already has pubkey / not already selected type / not already settled 正式三事（385 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.validator ≠ bundled（385）](../../tracks/implementation/worked-example-paramsblock-notpubkey-vs-bundled.md)。

## 三个名字

1. **validator 不是已经带了公钥：** 看见填了 validator，不是已经 364 interchangeable / 774 paramsblock-notpubkey interchangeable。
2. **看见填了 validator 不是已经选型：** 看见限了类型，不是已经 364 interchangeable。
3. **看见能填 不是已经改了集合：** 看见 ConsensusParams.validator，不是已经改了集合 interchangeable。

官方把 ConsensusParams.block / validator / version 三条核心句拆成三个名字。把它们叫成一个「看见填了 ConsensusParams 就已经是 MaxBytes 上限」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.validator 正式三事（385 余量），先数清问的是是不是已经带了公钥 / 364、是不是已经选型、还是看见能填是不是已经改了集合，再决定要不要同一次发布。385 paramsblock vs maxbytes bundled unbundling 在本页 item 2 续。
