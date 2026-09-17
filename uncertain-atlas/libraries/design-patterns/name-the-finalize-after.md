# 模式：把 Finalize 之后三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash ≠ 已经交差](../../tracks/implementation/worked-example-finalizeafter-vs-commit.md)。

## 三个名字

1. **Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 不是已经交差：** 看见回了 Finalize 不是已经落盘应用状态。
2. **落完再锁内存池、新交易不进 CheckTx 不是已经是 Commit 锁：** 看见锁了不是已经交差。
3. **可选再验池里剩下的、再解锁、再开下一高 round 0 不是已经是 Recheck：** 看见再验了不是已经交差。

## 为什么要分开叫

官方把 Finalize 回了之后引擎才落盘各笔输出 / AppHash / ResultsHash、落完再锁内存池、新交易不进 CheckTx、可选再验池里剩下的、再解锁、再开下一高 round 0 写成三件事。把它们叫成一个「看见回了 Finalize 就已经交差」，会把 ResultHash、Commit 锁和 Recheck 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 就已经交差」，先数清问的是 Finalize 之后引擎才落盘各笔输出 / AppHash / ResultsHash 不是已经交差、落完再锁内存池、新交易不进 CheckTx 不是已经是 Commit 锁，还是可选再验池里剩下的、再解锁、再开下一高 round 0 不是已经是 Recheck，再决定要不要同一次发布。
