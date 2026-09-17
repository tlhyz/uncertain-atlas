# 反模式：看见 OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份就当成已经是拒掉这份 / 看见 OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份就当成已经拒了人 / 看见 OfferSnapshot Result ABORT 是中止装回、不再试别份就当成已经换一份

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份 ≠ 已经是拒掉这份](../../tracks/implementation/worked-example-offerfmt-vs-rejectsnap.md)。

## 塌法

1. 看见 OfferSnapshot Result `REJECT_FORMAT` 是拒掉这种 format、换一份 / 看见回了 REJECT_FORMAT，就当成已经是拒掉这份，或当成已经齐。
2. 看见 OfferSnapshot Result `REJECT_SENDER` 是拒掉送来这份的所有人、换一份 / 看见回了 REJECT_SENDER，就当成已经拒了人，或当成已经能接着装。
3. 看见 OfferSnapshot Result `ABORT` 是中止装回、不再试别份 / 看见回了 ABORT，就当成已经换一份，或当成已经装完。

## 为什么会出事

官方写：`REJECT_FORMAT` 是拒掉这种 `format`，换一份。`REJECT_SENDER` 是拒掉送来这份的所有人，换一份。`ABORT` 是中止装回，不再试别份。

## 和相邻反模式

- [applyretry-sold-as-refetch](applyretry-sold-as-refetch.md) 是 ApplySnapshotChunk Result REJECT_SNAPSHOT 就已经是拒掉这份，不是本页这种 OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份不是已经是拒掉这份。
- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 reject_senders 不论 Result 都拒这些人就已经能接着装，不是本页这种 OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份不是已经拒了人。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是拉失败换一份就已经能接着装，不是本页这种 OfferSnapshot Result ABORT 是中止装回、不再试别份不是已经换一份。
