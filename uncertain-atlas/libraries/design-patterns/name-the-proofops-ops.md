# 模式：把 ProofOps 链三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProofOps。  
**例**：[ProofOps.ops 是多条证明 ≠ 已经串上了](../../tracks/implementation/worked-example-proofops-vs-chain.md)。

## 三个名字

1. **ProofOps.ops 是多条证明不是已经串上了：** 看见条数在不是已经能验完。
2. **各条的 type 可以不同不是已经是同一棵树：** 看见名字一样不是已经同一套编码。
3. **最后一条的根才该对上待验根不是已经对了中间某一条：** 看见前几条全绿不是已经能停。

## 为什么要分开叫

官方把 `ops` 是一串成链的证明、各条可能类型不同、最后一条的根才该等于待验根写成三件事。把它们叫成一个「看见 `ProofOps` 有多条就已经串上了」，会把列表长度、编码种类和链的锚点一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 ProofOps 有多条就已经串上了」，先数清问的是 ProofOps.ops 是多条证明不是已经串上了、各条的 type 可以不同不是已经是同一棵树，还是最后一条的根才该对上待验根不是已经对了中间某一条，再决定要不要同一次发布。
