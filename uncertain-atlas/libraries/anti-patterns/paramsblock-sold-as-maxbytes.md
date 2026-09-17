# 反模式：看见 ConsensusParams.block 限制块大小和块间隔就当成已经是 MaxBytes 上限 / 看见 ConsensusParams.validator 限制验证者公钥类型就当成已经带了公钥 / 看见 ConsensusParams.version 是 ABCI 应用版本就当成已经是 app_version 进了头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.block 限制块大小和块间隔 ≠ 已经是 MaxBytes 上限](../../tracks/implementation/worked-example-paramsblock-vs-maxbytes.md)。

## 塌法

1. 看见 ConsensusParams.`block` 限制块大小和块间隔 / 看见填了 block，就当成已经是 MaxBytes 上限，或当成已经是 next_block_delay。
2. 看见 ConsensusParams.`validator` 限制验证者公钥类型 / 看见填了 validator，就当成已经带了公钥，或当成已经选型。
3. 看见 ConsensusParams.`version` 是 ABCI 应用版本 / 看见填了 version，就当成已经是 app_version 进了头，或当成已经印进本头 AppHash。

## 为什么会出事

官方写：`block` 限制一块的大小和两块之间的时间。`validator` 限制验证者能用的公钥类型。`version` 是 ABCI 应用版本。

## 和相邻反模式

- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验就已经没有上限，不是本页这种 ConsensusParams.block 限制块大小和块间隔不是已经是 MaxBytes 上限。
- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 用 address 认人就已经带了公钥，不是本页这种 ConsensusParams.validator 限制验证者公钥类型不是已经带了公钥。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 app_version 进每块头就已经印进本头 AppHash，不是本页这种 ConsensusParams.version 是 ABCI 应用版本不是已经是 app_version 进了头。
