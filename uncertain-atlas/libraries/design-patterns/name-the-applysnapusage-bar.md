# 模式：把 ApplySnapshotChunk Usage verify/Info/unable 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[verify each chunk ≠ Only AppHash 可信任就交差](../../tracks/implementation/worked-example-applysnapusage-vs-info.md)。

## 三个名字

1. **verify each chunk / incrementally against AppHash 不是 Only AppHash 可信任就交差 / 332 incremental interchangeable：** 看见 Methods Usage 侧可选逐块验，不是 OfferSnapshot trust 或 app requirements 增量验 interchangeable。
2. **all chunks accepted 后 Info / AppVersion / switch 不是装块时就 Info 对了 / Transition interchangeable：** 看见全部 ACCEPT 后引擎 Info 核对切网，不是装过程中 Info 或 Transition bundled interchangeable。
3. **unable to retrieve next chunk → OfferSnapshot 不是 refetch 就齐 / REJECT_SNAPSHOT 回包 interchangeable：** 看见引擎拉不到下一块换快照，不是应用下指令 refetch interchangeable。

## 为什么要分开叫

官方把 ApplySnapshotChunk Usage 里 verify each chunk、all chunks accepted 后 Info 切网、unable to retrieve next chunk 换快照，和再拉（378）、Snapshot Verification（332）、Transition（323）写成三个名字。把它们叫成一个「看见 Apply 了 chunk 就已经验完、已经 Info 对了、已经齐」，会把逐块验、收尾 Info、拉不到换快照 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage verify/Info/unable，先数清问的是 verify each chunk 是不是 Only AppHash 可信任就交差、all chunks accepted 后 Info 是不是装块时就 Info 对了、unable to retrieve next chunk 是不是 refetch 就齐，再决定要不要同一次发布。
