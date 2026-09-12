# 模式：把 Prepare 回包上限三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**例**：[整池可见 ≠ 已经只能看见装得进一块的子集](../../tracks/implementation/worked-example-prepare-return-vs-pool.md)。

## 三个名字

1. **整池可见不是已经只能看见装得进一块的子集：** 看见池子都来了不是已经没有上限。
2. **聚合体积可以超过 max_tx_bytes 不是已经能回超限列表：** 看见池子比这次上限大不是已经能整包交回去。
3. **Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁：** 看见有这道要求不是引擎已经替你裁。

## 为什么要分开叫

官方把看见全部、池子可以超这次上限、回包仍不得超过写成三件事。把它们叫成一个「看见整池都给了就已经能整包交回去」，会把 -1 / 100 MB、扣开销之后的交易上限和四门一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见整池都给了就已经能整包交回去」，先数清问的是整池可见不是已经只能看见装得进一块的子集、聚合体积可以超过 max_tx_bytes 不是已经能回超限列表，还是 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁，再决定要不要同一次发布。
