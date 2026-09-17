# 模式：把 ProofOp 键三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**例**：[ProofOp.key 是这棵默克尔树里这把键 ≠ 已经是 Query 回包键](../../tracks/implementation/worked-example-proofop-vs-key.md)。

## 三个名字

1. **ProofOp.key 是这棵默克尔树里这把键不是已经是 Query 回包键：** 看见填了 key 不是已经是 ProofOp 类型。
2. **ProofOp.data 是这把键的编码证明不是已经是 proof_ops：** 看见填了 data 不是已经对上最终 AppHash。
3. **CheckTx 回包 log 是应用日志输出不是已经是 Query 日志：** 看见回了日志不是已经被引擎用了 Data。

## 为什么要分开叫

官方把 ProofOp `key` 是这棵默克尔树里这把键、`data` 是这把键的编码证明、CheckTx 回包 `log` 是应用日志输出写成三件事。把它们叫成一个「看见填了 ProofOp 键就已经是 Query 回包键」，会把 Query 回包键、proof_ops 和 Query 日志一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ProofOp 键就已经是 Query 回包键」，先数清问的是 ProofOp.key 是这棵默克尔树里这把键不是已经是 Query 回包键、ProofOp.data 是这把键的编码证明不是已经是 proof_ops，还是 CheckTx 回包 log 是应用日志输出不是已经是 Query 日志，再决定要不要同一次发布。
