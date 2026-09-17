# 反模式：看见 ConsensusParams.evidence 限制拜占庭证据是否合法就当成已经是证据 MaxBytes / 看见 ConsensusParams.abci 是 ABCI 相关参数就当成已经 Prepare 带了扩展 / 看见 ConsensusParams.synchrony 定提案时间戳合法界就当成已经是 PBTS

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.evidence 限制拜占庭证据是否合法 ≠ 已经是证据 MaxBytes](../../tracks/implementation/worked-example-paramsevidence-vs-maxbytes.md)。

## 塌法

1. 看见 ConsensusParams.`evidence` 限制拜占庭证据是否合法 / 看见填了 evidence，就当成已经是证据 MaxBytes，或当成已经盖住解绑。
2. 看见 ConsensusParams.`abci` 是 ABCI 相关参数 / 看见填了 abci，就当成已经 Prepare 带了扩展，或当成已经切到 ABCI 2.0。
3. 看见 ConsensusParams.`synchrony` 定提案时间戳合法界 / 看见填了 synchrony，就当成已经是 PBTS，或当成已经是 Precision 就已经是 MessageDelay。

## 为什么会出事

官方写：`evidence` 限制拜占庭行为证据是否合法。`abci` 是和 ABCI 有关的参数。`synchrony` 定一份提案时间戳的合法界。

## 和相邻反模式

- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是证据 MaxBytes 就已经是块 MaxBytes，不是本页这种 ConsensusParams.evidence 限制拜占庭证据是否合法不是已经是证据 MaxBytes。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 就已经 Prepare 带了扩展，不是本页这种 ConsensusParams.abci 是 ABCI 相关参数不是已经 Prepare 带了扩展。
- [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md) 是填了 Precision 就已经是 MessageDelay，不是本页这种 ConsensusParams.synchrony 定提案时间戳合法界不是已经是 PBTS。
