# 反模式：把 OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量）说成已经 Snapshot 字段都可信 / 已经 hash 比对就够 / 已经 OfferSnapshot app_hash 填了

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata ≠ bundled（483）](../../tracks/implementation/worked-example-offersnaptrust-notmetadata-vs-bundled.md)。

## 错在哪里

把 Only AppHash can be trusted, as it has been verified by the light client 写成已经 Snapshot.hash / metadata / 五个字段都对上就可信 interchangeable / 已经 ListSnapshots 回了本地清单就可信 interchangeable；把 Only AppHash can be trusted 写成已经引擎 hash 比对就等于轻验 interchangeable / 已经 hash / metadata 对齐 interchangeable；把 Only AppHash can be trusted 写成已经 OfferSnapshot 请求 app_hash 填了 interchangeable / 已经 OfferSnapshot 请求 bundled interchangeable，或已经和 483 offersnaptrust bundled / 651 offersnaptrust-notverify / 652 offersnaptrust-nottransition / 38 apphash-trust / 499 offersnapusage interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量），必须分开 not Snapshot metadata、not hash comparison、not OfferSnapshot app_hash 三件事，不要和 483 / 368 / 396 / 38 / 332 / 651 / 652 / 395 / 499 / 647 糊成一句。

## 和相邻反模式

- [offersnaptrust-sold-as-metadata](offersnaptrust-sold-as-metadata.md) 是 trust 专用 bundled（483），不是本页 483 item 1 单句边界。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是 Snapshot 全字段对上（368）专用，不是本页 not Snapshot metadata 单句边界。
- [offersnap-sold-as-listed](offersnap-sold-as-listed.md) 是 OfferSnapshot 请求 vs ListSnapshots（396 vs 322）专用，不是本页 not OfferSnapshot app_hash 单句边界。
- [offersnapusage-notlisted-sold-as-bundled](offersnapusage-notlisted-sold-as-bundled.md) 是 499 item 1 余量 / 647 专用，不是本页 Only AppHash can be trusted 单句边界。
