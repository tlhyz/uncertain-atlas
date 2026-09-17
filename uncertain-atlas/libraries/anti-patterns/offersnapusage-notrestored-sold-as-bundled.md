# 反模式：把 OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 / not Offer 收下之后 bundled / not LoadSnapshotChunk 正式三事（499 余量）说成已经 Offer 装完 / 已经 Offer 收下之后 bundled / 已经 LoadSnapshotChunk 已经齐

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 ≠ bundled（499）](../../tracks/implementation/worked-example-offersnapusage-notrestored-vs-bundled.md)。

## 错在哪里

把 Upon accepting, CometBFT will retrieve and apply snapshot chunks via `ApplySnapshotChunk` 写成已经 Offer 收下就已经装完 interchangeable / 已经 Snapshot Restoration 装回流程 bundled interchangeable / 已经 Offer 收下就已经齐 interchangeable；把 upon accepting retrieve and apply 写成已经 Offer 收下之后 bundled（401） interchangeable / 已经 Accept 后拉块并装三事 bundled interchangeable / 已经 ApplySnapshotChunk Result ACCEPT 就代表已经齐 interchangeable；把 upon accepting retrieve snapshot chunks 写成已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 interchangeable / 已经 LoadSnapshotChunk height/format/chunk bundled interchangeable / 已经 LoadSnapshotChunk Usage retrieve from peers interchangeable / 已经和 499 offersnapusage bundled / 647 offersnapusage-notlisted / 649 offersnapusage-notreject / 483 Only AppHash interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 / not Offer 收下之后 bundled / not LoadSnapshotChunk 正式三事（499 余量），必须分开 not Offer 装完、not Offer 收下之后 bundled、not LoadSnapshotChunk 已经齐 三件事，不要和 499 / 321 / 401 / 375 / 501 / 397 / 378 / 483 / 647 / 649 / 323 糊成一句。

## 和相邻反模式

- [offersnapusage-bootstrap-sold-as-bundled](offersnapusage-bootstrap-sold-as-bundled.md) 是 bootstrap accept/reject 专用 bundled（499），不是本页 499 item 2 单句边界。
- [offersnapusage-notlisted-sold-as-bundled](offersnapusage-notlisted-sold-as-bundled.md) 是 499 item 1 余量 / 647 专用，不是本页 upon accepting not Offer 装完 单句边界。
- [offeraccept-sold-as-restored](offeraccept-sold-as-restored.md) 是 Offer 收下之后 vs 装完（401 vs 321）专用，不是本页 not Offer 收下之后 bundled 单句边界。
- [loadsnapusage-sold-as-bundled](loadsnapusage-sold-as-bundled.md) 是 LoadSnapshotChunk Usage retrieve（501）专用，不是本页 not LoadSnapshotChunk 已经齐 单句边界。
