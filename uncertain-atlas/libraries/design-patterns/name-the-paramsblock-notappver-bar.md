# 模式：把 ConsensusParams.version not already app_version in header / not already header AppHash / not already settled 正式三事（385 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.version ≠ bundled（385）](../../tracks/implementation/worked-example-paramsblock-notappver-vs-bundled.md)。

## 三个名字

1. **version 不是已经是 app_version 进了头：** 看见填了 version，不是已经 370 interchangeable / 775 paramsblock-notappver interchangeable。
2. **看见填了 version 不是已经印进本头 AppHash：** 看见有应用版本，不是已经 370 interchangeable。
3. **看见能回 不是已经是握手对齐：** 看见 ConsensusParams.version，不是已经是握手对齐 interchangeable。

官方把 ConsensusParams.block / validator / version 三条核心句拆成三个名字。把它们叫成一个「看见填了 ConsensusParams 就已经是 MaxBytes 上限」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.version 正式三事（385 余量），先数清问的是是不是已经是 app_version 进了头 / 370、是不是已经印进本头 AppHash、还是看见能回是不是已经是握手对齐，再决定要不要同一次发布。385 paramsblock vs maxbytes bundled unbundling 在本页 item 3 完成。
