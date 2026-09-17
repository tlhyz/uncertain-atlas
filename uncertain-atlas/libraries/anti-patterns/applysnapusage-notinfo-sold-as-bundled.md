# 反模式：把 ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量）说成已经装块时就 Info 对了 / 已经切进共识 / 已经 verified AppHash at end

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load ≠ bundled（485）](../../tracks/implementation/worked-example-applysnapusage-notinfo-vs-bundled.md)。

## 错在哪里

把 When all chunks have been accepted, CometBFT will make an ABCI `Info` call to verify that `LastBlockAppHash` and `LastBlockHeight` matches the expected values 写成已经在装 chunk 过程中 Info 对了 interchangeable / 已经装块时就叫 Info 对 LastBlockAppHash interchangeable / 332 snapshotverify interchangeable / 653 applysnapusage-notverify interchangeable；把 record the `AppVersion` / switches to block sync or consensus and joins the network 写成已经 Transition to Consensus 那套 ChainID / 版本核对 interchangeable / 323 transition interchangeable / 370 infover interchangeable / 321 offerrestored interchangeable；把 all chunks accepted 后 Info / matches expected values 写成已经 verified AppHash automatically checked at end of restoration interchangeable / 483 offersnaptrust interchangeable / 652 offersnaptrust-nottransition interchangeable / 401 offerafter interchangeable，或已经和 485 applysnapusage bundled / 653 applysnapusage-notverify / 655 applysnapusage-notunable / 499 offersnapusage bundled interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量），必须分开 not Info during load、not Transition to Consensus bundled、not verified AppHash at end 三件事，不要和 485 / 332 / 323 / 483 / 652 / 653 / 655 / 321 / 401 / 648 / 499 / 647 糊成一句。

## 和相邻反模式

- [applysnapusage-sold-as-restored](applysnapusage-sold-as-restored.md) 是 ApplySnapshotChunk Usage verify/Info/unable 专用 bundled（485），不是本页 485 item 2 单句边界。
- [applysnapusage-notverify-sold-as-bundled](applysnapusage-notverify-sold-as-bundled.md) 是 485 item 1 余量 / 653 专用，不是本页 all chunks accepted 后 Info 单句边界。
- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是 Snapshot Verification（332）专用，不是本页 not Info during load 单句边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是 Transition to Consensus（323）专用，不是本页 not Transition to Consensus bundled 单句边界。
- [offersnaptrust-nottransition-sold-as-bundled](offersnaptrust-nottransition-sold-as-bundled.md) 是 483 item 3 余量 / 652 专用 verified AppHash at end，不是本页 ApplySnapshotChunk Usage all chunks accepted 后 Info 单句边界。
