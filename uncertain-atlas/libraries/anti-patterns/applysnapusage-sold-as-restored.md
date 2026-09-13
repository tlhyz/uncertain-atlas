# 反模式：把 ApplySnapshotChunk Usage verify/Info/unable 正式三事卖成验完 / Info 对了 / refetch 就齐

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[verify each chunk ≠ Only AppHash 可信任就交差](../../tracks/implementation/worked-example-applysnapusage-vs-info.md)。

## 卖法

- 「看见 verify each chunk / Metadata chunk hash / incrementally against AppHash 就已经 Only AppHash 可信任 / hash 比对就够 / 已经 Snapshot Verification 增量验交差。」
- 「看见 all chunks accepted / Info 对 LastBlockAppHash / LastBlockHeight / record AppVersion / switch to consensus 就已经在装块时就 Info 对了 / 已经 Transition to Consensus / 已经装完。」
- 「看见 unable to retrieve next chunk / reject via OfferSnapshot / reset and accept or abort 就已经 refetch_chunks 再拉就齐 / 已经 REJECT_SNAPSHOT 回包交差。」

## 为什么错

官方把 verify each chunk、all chunks accepted 后 Info 切网、unable to retrieve next chunk 换快照写成三件独立的实现事。把它们卖成验完 / Info 对了 / refetch 就齐，会把 Methods Usage 逐块验、收尾 Info、引擎换快照 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage verify/Info/unable，必须分开 verify each chunk、all chunks accepted 后 Info、unable to retrieve next chunk 三个名字，不要把它们卖成 Only AppHash 可信任 / 装块时就 Info 对了 / refetch 就齐。

## 和相邻反模式

- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch 就已经齐，不是本页 unable to retrieve next chunk → OfferSnapshot。
- [offersnaptrust-sold-as-metadata](offersnaptrust-sold-as-metadata.md) 是 Only AppHash 可信任，不是本页 verify each chunk Methods Usage。
