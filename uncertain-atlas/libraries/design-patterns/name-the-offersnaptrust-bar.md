# 模式：把 OfferSnapshot Usage trust 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[Only AppHash can be trusted ≠ Snapshot 字段都可信](../../tracks/implementation/worked-example-offersnaptrust-vs-metadata.md)。

## 三个名字

1. **Only AppHash can be trusted 不是 Snapshot 字段都可信：** 看见只有 AppHash 可信任不是已经 hash / metadata / 五个字段都对上就可信 interchangeable。
2. **Any other data can be spoofed / employ additional verification 不是 hash 比对就够：** 看见其它数据可被伪造、应用还应另做验真防 DoS 不是已经 hash 比对 / 增量验 chunk 就等于交差 interchangeable。
3. **verified AppHash automatically checked at end 不是装块时就 Info 对了：** 看见装回结束时自动核对 verified AppHash 不是已经在装 chunk 过程中 Info 对了 / 已经切进共识 interchangeable。

## 为什么要分开叫

官方把 Only AppHash can be trusted、Any other data can be spoofed / employ additional verification、verified AppHash automatically checked at the end 和 Snapshot 字段都可信、hash 比对就够、装块时就 Info 对了 写成三个名字。把它们叫成一个「看见 Offer 了 AppHash 就已经全信、已经防 DoS、已经装完对了」，会把轻验锚、另做验真、装回结束核对 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage trust，先数清问的是 Only AppHash can be trusted 是不是 Snapshot 字段都可信、Any other data can be spoofed / employ additional verification 是不是 hash 比对就够 / 已经防 DoS，还是 verified AppHash automatically checked at end 是不是装块时就 Info 对了 / 已经切进共识，再决定要不要同一次发布。
