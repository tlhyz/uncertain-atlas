# 模式：把 OfferSnapshot 结果枚举余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回 ≠ 已经崩](../../tracks/implementation/worked-example-offerunk-vs-crash.md)。

## 三个名字

1. **OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回不是已经崩：** 看见回了 UNKNOWN 不是已经是中止装回、不再试别份。
2. **OfferSnapshot Result ACCEPT 是收下这份、开始装块不是已经装完：** 看见回了 ACCEPT 不是已经齐。
3. **OfferSnapshot Result REJECT 是拒掉这份、换一份不是已经是拒掉这种 format：** 看见回了 REJECT 不是已经是拒掉这份。

## 为什么要分开叫

官方把 OfferSnapshot Result `UNKNOWN` 是结果不明、中止全部装回、`ACCEPT` 是收下这份、开始装块、`REJECT` 是拒掉这份、换一份写成三件事。把它们叫成一个「看见回了 OfferSnapshot 结果枚举余量就已经崩」，会把引擎当应用坏了会崩、已经装完和拒掉这种 format 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 OfferSnapshot 结果枚举余量就已经崩」，先数清问的是 OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回不是已经崩、OfferSnapshot Result ACCEPT 是收下这份、开始装块不是已经装完，还是 OfferSnapshot Result REJECT 是拒掉这份、换一份不是已经是拒掉这种 format，再决定要不要同一次发布。
