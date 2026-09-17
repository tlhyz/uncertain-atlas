# 模式：把 OfferSnapshot 结果枚举三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份 ≠ 已经是拒掉这份](../../tracks/implementation/worked-example-offerfmt-vs-rejectsnap.md)。

## 三个名字

1. **OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份不是已经是拒掉这份：** 看见回了 REJECT_FORMAT 不是已经齐。
2. **OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份不是已经拒了人：** 看见回了 REJECT_SENDER 不是已经能接着装。
3. **OfferSnapshot Result ABORT 是中止装回、不再试别份不是已经换一份：** 看见回了 ABORT 不是已经装完。

## 为什么要分开叫

官方把 OfferSnapshot Result `REJECT_FORMAT` 是拒掉这种 format、换一份、`REJECT_SENDER` 是拒掉送来这份的所有人、换一份、`ABORT` 是中止装回、不再试别份写成三件事。把它们叫成一个「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份」，会把拒掉这份、不论 Result 都拒这些人和拉失败换一份一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份」，先数清问的是 OfferSnapshot Result REJECT_FORMAT 是拒掉这种 format、换一份不是已经是拒掉这份、OfferSnapshot Result REJECT_SENDER 是拒掉送来这份的所有人、换一份不是已经拒了人，还是 OfferSnapshot Result ABORT 是中止装回、不再试别份不是已经换一份，再决定要不要同一次发布。
