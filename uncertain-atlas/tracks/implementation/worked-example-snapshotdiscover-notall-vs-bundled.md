# 例：看见问了邻居 / 看见 ListSnapshots 回了 / 看见 10 is not already already all-snapshots interchangeable / already no-cap interchangeable / already product-default-10 interchangeable

**层次**：实现 / ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量）/ not 722 snapshotdiscover-notall interchangeable / not 322 snapshotdiscover bundled interchangeable」，不是 Snapshot Discovery bundled（322），也不是挑了最高不是已经收下（723 item 2 余量）或 Offer 被拒不是已经停（724 item 3 余量）。不要另写怎样列快照或怎样挑。

## 官方三件事

规范把 Requirements 里空节点进网之后会问所有邻居用 `ListSnapshots` 报快照、**每个节点限 10 份** 和「已经是问了就已经有了全部快照 interchangeable / 已经是回了就已经没有上限 interchangeable / 已经是看见 10 就已经是不确定默认 interchangeable / 已经是 Snapshot Discovery bundled interchangeable」分开写成三件独立的实现事，不是「看见问了邻居 / 看见 ListSnapshots 回了就已经有了全部快照 interchangeable / 就已经没有上限 interchangeable / 就已经是不确定默认 interchangeable」一件事：

1. **看见问了邻居 / 看见 ListSnapshots 回了 / 看见邻居报了快照 is not already 已经有了全部快照 interchangeable / 已经 all-snapshots interchangeable / 已经齐交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 722 snapshotdiscover-notall interchangeable / 322 snapshotdiscover item 1 interchangeable，也不是已经 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事 bundled（322 item 1 余量） interchangeable / 322 snapshotdiscover item 1 interchangeable，也不是已经挑了最高不是已经收下（723） interchangeable / 724 snapshotdiscover-notstop interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：空节点进网之后，会问所有邻居用 `ListSnapshots` 报快照。看见问了邻居，不是已经有了全部快照 interchangeable——322 钉 bundled 三事，本页从 item 1 侧钉 not already all-snapshots 单句。看见 ListSnapshots 回了，不是已经 Snapshot Discovery bundled（322） interchangeable——322 钉 bundled，本页钉 item 1 第一件事。看见邻居报了快照，不是已经 Offer 收下已经装完（321） interchangeable——321 另钉装回，本页钉 Discovery item 1。322 snapshotdiscover vs offer bundled unbundling 在本页 item 1 启动。

2. **看见回了 / 看见 ListSnapshots 回了 / 看见每个节点限 10 份 is not already 已经没有上限 interchangeable / 已经 no-cap interchangeable / 已经无限快照交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 375 loadsnap interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 722 snapshotdiscover-notall interchangeable / 322 snapshotdiscover item 2 挑了最高 interchangeable / 322 snapshotdiscover item 3 Offer 被拒 interchangeable，也不是已经 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事 bundled（322 item 1 余量） interchangeable / 322 snapshotdiscover item 1 interchangeable，也不是已经有了全部快照（本页第一件事） interchangeable。**  
   官方写：每个节点限 10 份。看见回了，不是已经没有上限 interchangeable——本页钉 not already no-cap 单句。看见 ListSnapshots 回了，不是已经挑了最高不是已经收下（723） interchangeable——723 另钉 item 2，本页钉 item 1 第二件事。看见每个节点限 10 份，不是已经有了全部快照（本页第一件事） interchangeable——三件事分开钉。322 snapshotdiscover vs offer bundled unbundling 在本页 item 1 启动。

3. **看见 10 / 看见每节点 10 份 / 看见限 10 is not already 已经是不确定默认 interchangeable / 已经 product-default-10 interchangeable / 已经把 10 当产品常数交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 299 maxbytes interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 722 snapshotdiscover-notall interchangeable / 322 snapshotdiscover item 2 / 322 snapshotdiscover item 3，也不是已经 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事 bundled（322 item 1 余量） interchangeable / 322 snapshotdiscover item 1 interchangeable，也不是已经有了全部快照（本页第一件事） interchangeable / 已经没有上限（本页第二件事） interchangeable。**  
   官方把每节点限 10 份和已经是不确定默认路径分开——看见 10，不等于已经是不确定默认。看见 10，不是已经 product-default-10 interchangeable——本页钉 not already product-default-10 单句。看见每节点 10 份，不是已经没有上限（本页第二件事） interchangeable——三件事分开钉。看见限 10，不是已经把规范取值当不确定默认——本页钉产品边界。322 snapshotdiscover vs offer bundled unbundling 在本页 item 1 完成。

怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。Snapshot Discovery bundled（322）、挑了最高不是已经收下（322 item 2 余量 / 723）、Offer 被拒不是已经停（322 item 3 余量 / 724）、Offer 收下已经装完（321）、只有 AppHash 可信任（38）、启动对齐当快照重放（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **问了邻居 not already all-snapshots ≠ 322 / 33 interchangeable：** 官方把问邻居报快照单句和已经齐路径分开。
- **回了 not already no-cap ≠ 已经没有上限 interchangeable：** 官方把每节点限 10 份单句和已经无限路径分开。
- **看见 10 not already product-default-10 ≠ 已经是不确定默认 interchangeable：** 官方把规范上限和产品默认路径分开；322 snapshotdiscover vs offer bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 问了邻居 | 不是 already all-snapshots | 不是 Offer 装完 alone（321） |
| 回了 | 不是 already no-cap | 不是挑了最高 alone（723） |
| 看见 10 | 不是 already product-default-10 | 不是 Offer 被拒 alone（724） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量），必须分开问了邻居 是不是 already all-snapshots interchangeable / 322 snapshotdiscover bundled interchangeable / snapshotdiscover-sold-as-listed interchangeable、回了 是不是 already no-cap interchangeable、看见 10 是不是 already product-default-10 interchangeable。可以跳过「看见问了邻居就已经有了全部快照 interchangeable / 就已经没有上限 interchangeable / 就已经是不确定默认 interchangeable」。不要另写怎样列快照。不要把每节点 10 份当不确定默认。322 snapshotdiscover vs offer bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshotdiscover-notaccepted-vs-bundled.md`](worked-example-snapshotdiscover-notaccepted-vs-bundled.md)（不变量 723 item 2，待写）。

## 本页不抄

- 怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数。
- Snapshot Discovery bundled。那是不变量 322。
- 挑了最高不是已经收下。那是不变量 322 item 2 余量 / 723。
- Offer 被拒不是已经停。那是不变量 322 item 3 余量 / 724。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
