# 反模式：看见 CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池就当成已经是技术上可选 / 看见这笔可以来自外部用户、也可以来自另一节点就当成已经保证不重放 / 看见默克尔证明带自描述 type、好支持多种默克尔树和编码就当成已经是 ProofOp 类型

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**例**：[CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池 ≠ 已经是技术上可选](../../tracks/implementation/worked-example-checktxguard-vs-optional.md)。

## 塌法

1. 看见 CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池 / 看见先跑了，就当成已经是技术上可选，或当成已经是四门已经结算。
2. 看见这笔可以来自外部用户、也可以来自另一节点 / 看见送来了，就当成已经保证不重放，或当成已经从池里删掉。
3. 看见默克尔证明带自描述 `type`、好支持多种默克尔树和编码 / 看见写了 type，就当成已经是 ProofOp 类型，或当成已经对上 AppHash。

## 为什么会出事

官方写：CheckTx 是内存池的守卫；每条节点在让一笔交易进自己本地池之前，都先跑 `CheckTx`。这笔交易可以来自外部用户，也可以来自另一节点。默克尔证明带自描述的 `type` 字段，好支持多种默克尔树和编码格式。

## 和相邻反模式

- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 CheckTx 技术上可选、不参与处理块就已经是四门已经结算，不是本页这种 CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池不是已经是技术上可选。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是内存池去重就已经保证不重放，不是本页这种这笔可以来自外部用户、也可以来自另一节点不是已经保证不重放。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash，不是本页这种默克尔证明带自描述 type、好支持多种默克尔树和编码不是已经是 ProofOp 类型。
