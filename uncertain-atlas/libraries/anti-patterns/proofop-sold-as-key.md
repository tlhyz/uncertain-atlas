# 反模式：看见 ProofOp.key 是这棵默克尔树里这把键就当成已经是 Query 回包键 / 看见 ProofOp.data 是这把键的编码证明就当成已经是 proof_ops / 看见 CheckTx 回包 log 是应用日志输出就当成已经是 Query 日志

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**例**：[ProofOp.key 是这棵默克尔树里这把键 ≠ 已经是 Query 回包键](../../tracks/implementation/worked-example-proofop-vs-key.md)。

## 塌法

1. 看见 ProofOp `key` 是这棵默克尔树里这把键 / 看见填了 key，就当成已经是 Query 回包键，或当成已经是 ProofOp 类型。
2. 看见 ProofOp `data` 是这把键的编码证明 / 看见填了 data，就当成已经是 `proof_ops`，或当成已经对上最终 AppHash。
3. 看见 CheckTx 回包 `log` 是应用日志输出 / 看见回了日志，就当成已经是 Query 日志，或当成已经被引擎用了 Data。

## 为什么会出事

官方写：`key` 是这棵默克尔树里这把证明对应的键。`data` 是这把键的编码默克尔证明。CheckTx 回包 `log` 是应用日志的输出。

## 和相邻反模式

- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 Query 回包 key 就已经是 Query 高度，不是本页这种 ProofOp.key 是这棵默克尔树里这把键不是已经是 Query 回包键。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash，不是本页这种 ProofOp.data 是这把键的编码证明不是已经是 proof_ops。
- [querycode-sold-as-consensus](querycode-sold-as-consensus.md) 是 Query 回包 log 就已经新鲜，不是本页这种 CheckTx 回包 log 是应用日志输出不是已经是 Query 日志。
