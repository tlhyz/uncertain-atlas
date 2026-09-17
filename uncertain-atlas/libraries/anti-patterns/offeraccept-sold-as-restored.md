# 反模式：看见 Offer 收下之后才去拉块并装就当成已经装完 / 看见在装这块的回包里拒掉这份、还要再收 Offer 就当成已经中止 / 看见 ApplySnapshotChunk Result ACCEPT 是这块收下了就当成已经齐

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**例**：[Offer 收下之后才去拉块并装 ≠ 已经装完](../../tracks/implementation/worked-example-offeraccept-vs-restored.md)。

## 塌法

1. 看见 Offer 收下之后引擎才去拉块并经 ApplySnapshotChunk 装 / 看见收下了，就当成已经装完，或当成已经齐。
2. 看见在装这块的回包里也能拒掉这份、还要准备再收 Offer / 看见在装这块时拒了，就当成已经中止，或当成已经是拒掉这份。
3. 看见 ApplySnapshotChunk Result `ACCEPT` 是这块收下了 / 看见回了 ACCEPT，就当成已经齐，或当成已经是装这块的结果。

## 为什么会出事

官方写：收下之后，CometBFT 才去拉块，并经 `ApplySnapshotChunk` 装。应用也可以在装这块的回包里拒掉这份；这时还要准备再收 `OfferSnapshot`。`ACCEPT` 是这块收下了。

## 和相邻反模式

- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完，不是本页这种 Offer 收下之后才去拉块并装不是已经装完。
- [offerfmt-sold-as-rejectsnap](offerfmt-sold-as-rejectsnap.md) 是 OfferSnapshot Result ABORT 就已经中止，不是本页这种在装这块的回包里拒掉这份、还要再收 Offer 不是已经中止。
- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk 回包 result 就已经是 Offer 的结果，不是本页这种 ApplySnapshotChunk Result ACCEPT 是这块收下了不是已经齐。
