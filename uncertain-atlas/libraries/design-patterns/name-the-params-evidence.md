# 模式：把 ConsensusParams 余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**例**：[ConsensusParams.evidence 限制拜占庭证据是否合法 ≠ 已经是证据 MaxBytes](../../tracks/implementation/worked-example-paramsevidence-vs-maxbytes.md)。

## 三个名字

1. **ConsensusParams.evidence 限制拜占庭证据是否合法不是已经是证据 MaxBytes：** 看见填了 evidence 不是已经盖住解绑。
2. **ConsensusParams.abci 是 ABCI 相关参数不是已经 Prepare 带了扩展：** 看见填了 abci 不是已经切到 ABCI 2.0。
3. **ConsensusParams.synchrony 定提案时间戳合法界不是已经是 PBTS：** 看见填了 synchrony 不是已经是 Precision 就已经是 MessageDelay。

## 为什么要分开叫

官方把 `evidence` 限制拜占庭证据是否合法、`abci` 是 ABCI 相关参数、`synchrony` 定提案时间戳合法界写成三件事。把它们叫成一个「看见填了余下三栏就已经是证据 MaxBytes」，会把证据上限、扩展启用和 PBTS 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了余下三栏就已经是证据 MaxBytes」，先数清问的是 ConsensusParams.evidence 限制拜占庭证据是否合法不是已经是证据 MaxBytes、ConsensusParams.abci 是 ABCI 相关参数不是已经 Prepare 带了扩展，还是 ConsensusParams.synchrony 定提案时间戳合法界不是已经是 PBTS，再决定要不要同一次发布。
