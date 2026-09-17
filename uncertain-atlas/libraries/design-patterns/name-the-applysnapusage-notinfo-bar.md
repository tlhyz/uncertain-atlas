# 模式：把 ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load ≠ bundled（485）](../../tracks/implementation/worked-example-applysnapusage-notinfo-vs-bundled.md)。

## 三个名字

1. **all chunks accepted 后 Info 不是 Info during load：** 看见 When all chunks have been accepted, CometBFT will make an ABCI `Info` call to verify that `LastBlockAppHash` and `LastBlockHeight` matches the expected values，不是已经在装 chunk 过程中 Info 对了 interchangeable，不是 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 653 applysnapusage-notverify interchangeable。
2. **all chunks accepted 后 Info 不是 Transition to Consensus bundled：** 看见 record the `AppVersion` / switches to block sync or consensus and joins the network，不是已经 Transition to Consensus 那套 ChainID / 版本核对 interchangeable，不是 323 transition interchangeable / 370 infover interchangeable / 321 offerrestored interchangeable。
3. **all chunks accepted 后 Info 不是 verified AppHash at end：** 看见 all chunks accepted 后 Info / matches expected values，不是已经 verified AppHash automatically checked at end of restoration interchangeable，不是 483 offersnaptrust interchangeable / 652 offersnaptrust-nottransition interchangeable / 401 offerafter interchangeable。

## 为什么要分开叫

官方把 ApplySnapshotChunk Usage all chunks accepted 后 Info、装过程中 Info 核对、Transition to Consensus ChainID / Info 核对、OfferSnapshot Usage verified AppHash at end 写成三个名字。把它们叫成一个「看见 all chunks accepted 后 Info 就已经装块时就 Info 对了 interchangeable / 就已经切进共识 interchangeable / 就已经 verified AppHash at end interchangeable」，会把 not Info during load、not Transition to Consensus bundled、not verified AppHash at end 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量），先数清问的是 all chunks accepted 后 Info 是不是 Info during load / 332 / 653，是不是 Transition to Consensus bundled / 323 / 370 / 321，还是 all chunks accepted 后 Info 是不是 verified AppHash at end / 483 / 652 / 401，再决定要不要同一次发布。485 applysnapusage unbundling 在本页 item 2 续。
