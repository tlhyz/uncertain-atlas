# 模式：把 ApplySnapshotChunk 再拉三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[应用可以再拉块或封邻居、引擎不自己做 ≠ 已经封了](../../tracks/implementation/worked-example-refetch-vs-restored.md)。

## 三个名字

1. **应用可以再拉块或封邻居、引擎不自己做不是已经封了：** 看见能再拉不是已经齐。
2. **refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐：** 看见列了块号不是已经交差。
3. **reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装：** 看见拒了人不是已经停。

## 为什么要分开叫

官方把应用可以再拉块或封邻居而引擎不自己做、`refetch_chunks` 不论 result 都再拉再装、`reject_senders` 不论 Result 都拒这些人写成三件事。把它们叫成一个「看见回了再拉就已经封了」，会把装回、增量验和拉块一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了再拉就已经封了」，先数清问的是应用可以再拉块或封邻居、引擎不自己做不是已经封了、refetch_chunks 不论 result 都再拉再装不是已经齐，还是 reject_senders 不论 Result 都拒这些人不是已经能接着装，再决定要不要同一次发布。
