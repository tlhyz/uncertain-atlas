# 反模式：看见 OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回就当成已经崩 / 看见 OfferSnapshot Result ACCEPT 是收下这份、开始装块就当成已经装完 / 看见 OfferSnapshot Result REJECT 是拒掉这份、换一份就当成已经是拒掉这种 format

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回 ≠ 已经崩](../../tracks/implementation/worked-example-offerunk-vs-crash.md)。

## 塌法

1. 看见 OfferSnapshot Result `UNKNOWN` 是结果不明、中止全部装回 / 看见回了 UNKNOWN，就当成已经崩，或当成已经是中止装回、不再试别份。
2. 看见 OfferSnapshot Result `ACCEPT` 是收下这份、开始装块 / 看见回了 ACCEPT，就当成已经装完，或当成已经齐。
3. 看见 OfferSnapshot Result `REJECT` 是拒掉这份、换一份 / 看见回了 REJECT，就当成已经是拒掉这种 format，或当成已经是拒掉这份。

## 为什么会出事

官方写：`UNKNOWN` 是结果不明，中止全部装回。`ACCEPT` 是收下这份，开始装块。`REJECT` 是拒掉这份，换一份。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 UNKNOWN 一律是错、引擎当应用坏了会崩，不是本页这种 OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回不是已经崩。
- [offeraccept-sold-as-restored](offeraccept-sold-as-restored.md) 是 Offer 收下之后才去拉块并装就已经装完，不是本页这种 OfferSnapshot Result ACCEPT 是收下这份、开始装块不是已经装完。
- [offerfmt-sold-as-rejectsnap](offerfmt-sold-as-rejectsnap.md) 是 OfferSnapshot Result REJECT_FORMAT 就已经是拒掉这种 format，不是本页这种 OfferSnapshot Result REJECT 是拒掉这份、换一份不是已经是拒掉这种 format。
