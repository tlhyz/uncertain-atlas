# 模式：把 Offer 收下之后三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**例**：[Offer 收下之后才去拉块并装 ≠ 已经装完](../../tracks/implementation/worked-example-offeraccept-vs-restored.md)。

## 三个名字

1. **Offer 收下之后才去拉块并装不是已经装完：** 看见收下了不是已经齐。
2. **在装这块的回包里拒掉这份、还要再收 Offer 不是已经中止：** 看见在装这块时拒了不是已经是拒掉这份。
3. **ApplySnapshotChunk Result ACCEPT 是这块收下了不是已经齐：** 看见回了 ACCEPT 不是已经是装这块的结果。

## 为什么要分开叫

官方把 Offer 收下之后才去拉块并装、在装这块的回包里也能拒掉这份、还要准备再收 Offer、ApplySnapshotChunk Result `ACCEPT` 是这块收下了写成三件事。把它们叫成一个「看见收下了就已经装完」，会把已经装完、中止装回和一块 chunk 收下就已经齐一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收下了就已经装完」，先数清问的是 Offer 收下之后才去拉块并装不是已经装完、在装这块的回包里拒掉这份、还要再收 Offer 不是已经中止，还是 ApplySnapshotChunk Result ACCEPT 是这块收下了不是已经齐，再决定要不要同一次发布。
