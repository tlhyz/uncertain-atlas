# 反模式：把 OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled / not ListSnapshots / not Snapshot Connection 正式三事（499 余量）说成已经 OfferSnapshot 请求 bundled / 已经 ListSnapshots 发现 / 已经 offersnapusage bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled ≠ bundled（499）](../../tracks/implementation/worked-example-offersnapusage-notlisted-vs-bundled.md)。

## 错在哪里

把 bootstrapping state sync / may accept or reject 写成已经 OfferSnapshot 请求 bundled（396） interchangeable / 已经 OfferSnapshot 回包 result 栏 interchangeable / 已经 OfferSnapshot 在用 state sync 引导节点时叫 interchangeable；把 bootstrapping may accept/reject 写成已经 ListSnapshots 发现（322） interchangeable / 已经 Snapshot Discovery 问了邻居就已经齐 interchangeable / 已经 ListSnapshots 空请求 bundled（395） interchangeable / 已经本地清单 interchangeable；把 bootstrapping may accept/reject 写成已经是 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 已经 Snapshot Connection 门（334） interchangeable / 已经必须实现快照连接 interchangeable / 已经 Only AppHash can be trusted（483） interchangeable / 已经和 Upon accepting 装完 / reject in chunk ABORT bundled interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled / not ListSnapshots / not Snapshot Connection 正式三事（499 余量），必须分开 not OfferSnapshot bundled、not ListSnapshots、not Snapshot Connection / not offersnapusage bundled 三件事，不要和 499 / 396 / 322 / 395 / 334 / 483 / 648 / 649 / 401 / 321 糊成一句。

## 和相邻反模式

- [offersnapusage-bootstrap-sold-as-bundled](offersnapusage-bootstrap-sold-as-bundled.md) 是 bootstrap accept/reject 专用 bundled（499），不是本页 499 item 1 单句边界。
- [offersnap-sold-as-listed](offersnap-sold-as-listed.md) 是 OfferSnapshot 请求 vs ListSnapshots 发现（396 vs 322）专用，不是本页 499 item 1 三事边界。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 Snapshot Discovery vs ListSnapshots 回了（322 vs 395）专用，不是本页 not ListSnapshots 单句边界。
- [snapshotconn-sold-as-required](snapshotconn-sold-as-required.md) 是 Snapshot Connection 门（334）专用，不是本页 not Snapshot Connection 单句边界。
