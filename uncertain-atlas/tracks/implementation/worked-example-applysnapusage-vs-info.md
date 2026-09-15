# 例：看见 verify each chunk / incrementally against AppHash 不是已经 Only AppHash 可信任就交差；看见 all chunks accepted 后 Info 对 LastBlockAppHash/Height 不是已经在装块时就 Info 对了；看见 unable to retrieve next chunk 会 reject via OfferSnapshot 不是已经 refetch/reject_senders 就齐

**层次**：实现 / ApplySnapshotChunk Usage verify/Info/unable 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「verify each chunk 不是 Only AppHash 可信任就交差 / all chunks accepted 后 Info 不是装块时就 Info 对了 / unable to retrieve next chunk 不是 refetch 就齐」，不是 ApplySnapshotChunk 再拉 bundled（378），也不是 Snapshot Verification app requirements bundled（332），也不是 Transition to Consensus（323）。不要另写怎样做增量验、怎样配 Metadata。

## 官方三件事

规范把 ApplySnapshotChunk Usage 里 verify each chunk、all chunks accepted 后 Info 核对并切进网、unable to retrieve next chunk 时 reject via OfferSnapshot 写成三件独立的实现事，不是「看见 Apply 了 chunk 就已经验完、已经 Info 对了、已经齐」一件事：

1. **看见 The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash` / 看见应用可能想验每一块、例如在 Metadata 里挂 chunk hash 或按 AppHash 增量验 不是已经 Only AppHash can be trusted（483）那种 hash/metadata 比对就够 interchangeable，也不是已经 Snapshot Verification 增量验 chunk（332） app requirements bundled 就等于 Methods Usage 这句 interchangeable。**  
   官方 Usage 写：The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash`。看见 may want to verify each chunk，不是已经 OfferSnapshot Usage trust（483）那种 Only AppHash 可信任就不需要另做验 interchangeable。看见 Metadata / incrementally against AppHash，不是已经 Snapshot Verification（332） bundled 第三件事「增量验了就不是唯一可信锚」 interchangeable——332 钉 app requirements，本页钉 Methods ApplySnapshotChunk Usage。看见验了 chunk，不是已经 ApplySnapshotChunk Result ACCEPT（401）就已经齐 interchangeable。
2. **看见 When all chunks have been accepted, CometBFT will make an ABCI `Info` call to verify that `LastBlockAppHash` and `LastBlockHeight` matches the expected values, and record the `AppVersion` in the node state. It then switches to block sync or consensus and joins the network / 看见全部 chunk 都 ACCEPT 后引擎会叫 Info 核对 LastBlockAppHash / LastBlockHeight、记下 AppVersion，再切 block sync 或 consensus 不是已经在装 chunk 过程中 Info 对了（332），也不是已经 Transition to Consensus 那套 ChainID / 版本核对（323） interchangeable，也不是已经 verified AppHash automatically checked at end of restoration（483） interchangeable。**  
   官方 Usage 写：When all chunks have been accepted, CometBFT will make an ABCI `Info` call … `LastBlockAppHash` and `LastBlockHeight` … record the `AppVersion` … switches to block sync or consensus and joins the network。看见 all chunks accepted 后才 Info，不是已经在装块时就叫 Info 对 LastBlockAppHash（332） interchangeable。看见 matches expected values + record AppVersion + switches to sync/consensus，不是已经 Transition to Consensus（323） bundled 第二件事「AppHash 对上不是已经版本也对上」 interchangeable。看见 joins the network，不是已经 Offer 收下就已经装完（321） interchangeable。
3. **看见 If CometBFT is unable to retrieve the next chunk after some time … it will reject the snapshot and try a different one via `OfferSnapshot`. The application should be prepared to reset and accept it or abort as appropriate / 看见拉不到下一块时会 reject snapshot、经 OfferSnapshot 换一份，应用应准备好 reset 后 accept 或 abort 不是已经 refetch_chunks / reject_senders（378）那种再拉就齐 interchangeable，也不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT（398） bundled 就等于 Usage 这句 interchangeable。**  
   官方 Usage 写：If CometBFT is unable to retrieve the next chunk after some time (e.g. because no suitable peers are available), it will reject the snapshot and try a different one via `OfferSnapshot`。The application should be prepared to reset and accept it or abort as appropriate。看见 unable to retrieve next chunk，不是已经 refetch_chunks 不论 result 都再拉（378） interchangeable——378 钉应用下指令再拉/封邻居，本页钉引擎拉不到下一块时的换快照路径。看见 reject via OfferSnapshot，不是已经 REJECT_SNAPSHOT 回包（398） bundled 就等于引擎换一份 interchangeable。看见 reset and accept or abort，不是已经装完又对上 LastBlockAppHash（332） interchangeable。

怎样做增量验、怎样写 Metadata chunk hash、怎样 reset 是规范里的做法，本页不抄。ApplySnapshotChunk 再拉（378）是 refetch/reject_senders 那套，Snapshot Verification（332）是 app requirements 那套，Transition to Consensus（323）是装完后再凑 ChainID 那套，OfferSnapshot Usage trust（483）是 Only AppHash 可信任那套，本页不抄。

## 官方为什么这样拆

- **verify each chunk ≠ Only AppHash 可信任就交差 / 332 incremental interchangeable：** 官方把 Methods Usage 侧可选逐块验和 OfferSnapshot trust、app requirements 增量验分开。
- **all chunks accepted 后 Info + AppVersion + switch ≠ 装块时就 Info 对了 / Transition to Consensus interchangeable：** 官方把全部 ACCEPT 后的 Info 核对切网和装过程中 Info、Transition 分开。
- **unable to retrieve next chunk → OfferSnapshot ≠ refetch 就齐 / REJECT_SNAPSHOT 回包 interchangeable：** 官方把引擎拉不到下一块换快照和应用下指令再拉分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| verify each chunk / incrementally against AppHash | 不是 Only AppHash 可信任就交差 | 不是 Snapshot Verification（332） |
| all chunks accepted 后 Info / AppVersion / switch | 不是装块时就 Info 对了 | 不是 Transition to Consensus（323） |
| unable to retrieve next chunk → OfferSnapshot | 不是 refetch 就齐 | 不是 ApplySnapshotChunk 再拉（378） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Apply 了 chunk 就已经验完、已经 Info 对了、已经齐」，必须分开 verify each chunk 是不是 Only AppHash 可信任就交差、all chunks accepted 后 Info 是不是装块时就 Info 对了 / Transition interchangeable、unable to retrieve next chunk 是不是 refetch 就齐。可以跳过「看见 Apply 了 chunk 就已经验完」。不要另写怎样做增量验。

## 本页不抄

- 怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。
- ApplySnapshotChunk 再拉 refetch/reject_senders。那是不变量 378。
- Snapshot Verification 增量验 / 装完又对上 LastBlockAppHash。那是不变量 332。
- Transition to Consensus Info 核对 / 切进共识。那是不变量 323。
- OfferSnapshot Usage trust Only AppHash can be trusted。那是不变量 483。
- Offer 收下之后拉块并装。那是不变量 401。
