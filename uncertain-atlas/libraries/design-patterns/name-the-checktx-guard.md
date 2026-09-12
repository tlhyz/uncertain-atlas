# 模式：把 CheckTx 守卫余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**例**：[CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池 ≠ 已经是技术上可选](../../tracks/implementation/worked-example-checktxguard-vs-optional.md)。

## 三个名字

1. **CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池不是已经是技术上可选：** 看见先跑了不是已经是四门已经结算。
2. **这笔可以来自外部用户、也可以来自另一节点不是已经保证不重放：** 看见送来了不是已经从池里删掉。
3. **默克尔证明带自描述 type、好支持多种默克尔树和编码不是已经是 ProofOp 类型：** 看见写了 type 不是已经对上 AppHash。

## 为什么要分开叫

官方把 CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池、这笔可以来自外部用户也可以来自另一节点、默克尔证明带自描述 type 好支持多种默克尔树和编码写成三件事。把它们叫成一个「看见回了 CheckTx 守卫余量就已经是技术上可选」，会把技术上可选、去重和按键查一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 CheckTx 守卫余量就已经是技术上可选」，先数清问的是 CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池不是已经是技术上可选、这笔可以来自外部用户、也可以来自另一节点不是已经保证不重放，还是默克尔证明带自描述 type、好支持多种默克尔树和编码不是已经是 ProofOp 类型，再决定要不要同一次发布。
