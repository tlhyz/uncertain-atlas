# 模式：把查询证明三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**例**：[头上有 AppHash ≠ 已经是交易默克尔](../../tracks/implementation/worked-example-query-proof-vs-apphash.md)。

## 三个名字

1. **头上有 AppHash 不是已经是交易默克尔：** 看见和 DataHash 并列不是已经是验证者集合。
2. **Query 回了 Proof 不是已经对上 AppHash：** 看见一条 ProofOp 不是已经是一层树之外的全部。
3. **一层 ProofOp 的根不是已经对上最终 AppHash：** 看见中间根对了不是已经交给下一层。

## 为什么要分开叫

官方把三种头哈希、回证明、多层根接值写成三件事。把它们叫成一个「看见头上有 AppHash 就已经能验应用」，会把本头时序、QueryState 和轻验快照一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「查询已经带证明」，先数清问的是头上有 AppHash 不是已经是交易默克尔、Query 回了 Proof 不是已经对上 AppHash，还是一层 ProofOp 的根不是已经对上最终 AppHash，再决定要不要同一次发布。
