# 模式：把 ConsensusParams 字段三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.block 限制块大小和块间隔 ≠ 已经是 MaxBytes 上限](../../tracks/implementation/worked-example-paramsblock-vs-maxbytes.md)。

## 三个名字

1. **ConsensusParams.block 限制块大小和块间隔不是已经是 MaxBytes 上限：** 看见填了 block 不是已经是 next_block_delay。
2. **ConsensusParams.validator 限制验证者公钥类型不是已经带了公钥：** 看见填了 validator 不是已经选型。
3. **ConsensusParams.version 是 ABCI 应用版本不是已经是 app_version 进了头：** 看见填了 version 不是已经印进本头 AppHash。

## 为什么要分开叫

官方把 `block` 限制块大小和块间隔、`validator` 限制验证者公钥类型、`version` 是 ABCI 应用版本写成三件事。把它们叫成一个「看见填了 ConsensusParams 就已经是 MaxBytes 上限」，会把块上限、公钥和 app_version 进头一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ConsensusParams 就已经是 MaxBytes 上限」，先数清问的是 ConsensusParams.block 限制块大小和块间隔不是已经是 MaxBytes 上限、ConsensusParams.validator 限制验证者公钥类型不是已经带了公钥，还是 ConsensusParams.version 是 ABCI 应用版本不是已经是 app_version 进了头，再决定要不要同一次发布。
