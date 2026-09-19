# 例：看见挑了 / 看见最高 / 看见排过了 is not already already accepted interchangeable / already restored interchangeable / already app-format interchangeable

**层次**：实现 / 挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事（322 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事（322 余量）/ not 723 snapshotdiscover-notaccepted interchangeable / not 322 snapshotdiscover bundled interchangeable」，不是 Snapshot Discovery bundled（322），也不是 ListSnapshots 回了不是已经有了全部快照（722 item 1 余量）或 Offer 被拒不是已经停（724 item 3 余量）。不要另写怎样列快照或怎样挑。

## 官方三件事

规范把 Requirements 里过一段时间节点挑一份最合适的（一般按高度、格式、有多少邻居）再经 `OfferSnapshot` 交给应用 和「已经是挑了就已经收下 interchangeable / 已经是最高就已经装完 interchangeable / 已经是排过了就已经是应用要的格式 interchangeable / 已经是 Snapshot Discovery bundled interchangeable」分开写成三件独立的实现事，不是「看见挑了最高就已经收下 interchangeable / 就已经装完 interchangeable / 就已经是应用要的格式 interchangeable」一件事：

1. **看见挑了 / 看见挑了最高 / 看见挑一份最合适的 is not already 已经收下 interchangeable / 已经 accepted interchangeable / 已经是应用收下的那份 interchangeable / 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 723 snapshotdiscover-notaccepted interchangeable / 322 snapshotdiscover item 2 interchangeable，也不是已经挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事 bundled（322 item 2 余量） interchangeable / 322 snapshotdiscover item 2 interchangeable，也不是已经 ListSnapshots 回了不是已经有了全部快照（722） interchangeable / 724 snapshotdiscover-notstop interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：挑一份最合适的，再经 `OfferSnapshot` 交给应用。看见挑了，不是已经收下 interchangeable——322 钉 bundled 三事，本页从 item 2 侧钉 not already accepted 单句。看见挑了最高，不是已经 Snapshot Discovery bundled（322） interchangeable——322 钉 bundled，本页钉 item 2 第一件事。看见挑一份最合适的，不是已经 ListSnapshots 回了不是已经有了全部快照（722） interchangeable——722 另钉 item 1，本页钉 item 2 第一件事。322 snapshotdiscover vs offer bundled unbundling 在本页 item 2 续。

2. **看见最高 / 看见按高度排了 / 看见挑了最高那份 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装回交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 321 snapshotrestore interchangeable / 719 snapshotrestore-notrestored interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 723 snapshotdiscover-notaccepted interchangeable / 322 snapshotdiscover item 1 ListSnapshots interchangeable / 322 snapshotdiscover item 3 Offer 被拒 interchangeable，也不是已经挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事 bundled（322 item 2 余量） interchangeable / 322 snapshotdiscover item 2 interchangeable，也不是已经收下（本页第一件事） interchangeable。**  
   官方把本地挑选和已经装完路径分开——看见最高，不等于已经装完。看见最高，不是已经 restored interchangeable——本页钉 not already restored 单句。看见按高度排了，不是已经 Offer 收下就已经装完（321 / 719） interchangeable——321 / 719 另钉装回，本页钉 item 2 第二件事。看见挑了最高那份，不是已经收下（本页第一件事） interchangeable——三件事分开钉。322 snapshotdiscover vs offer bundled unbundling 在本页 item 2 续。

3. **看见排过了 / 看见按高度、格式、邻居数排了 / 看见按格式排了 is not already 已经是应用要的格式 interchangeable / 已经 app-format interchangeable / 已经格式交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 38 apphash interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 723 snapshotdiscover-notaccepted interchangeable / 322 snapshotdiscover item 1 / 322 snapshotdiscover item 3，也不是已经挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事 bundled（322 item 2 余量） interchangeable / 322 snapshotdiscover item 2 interchangeable，也不是已经收下（本页第一件事） interchangeable / 已经装完（本页第二件事） interchangeable。**  
   官方把本地按格式等排序和已经是应用要的格式路径分开——排过了，不等于已经是应用要的格式。看见排过了，不是已经 app-format interchangeable——本页钉 not already app-format 单句。看见按高度、格式、邻居数排了，不是已经收下（本页第一件事） interchangeable——三件事分开钉。看见按格式排了，不是已经 Offer 被拒不是已经停（724） interchangeable——724 另钉拒格式侧。322 snapshotdiscover vs offer bundled unbundling 在本页 item 2 完成。

怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。Snapshot Discovery bundled（322）、ListSnapshots 回了不是已经有了全部快照（322 item 1 余量 / 722）、Offer 被拒不是已经停（322 item 3 余量 / 724）、Offer 收下已经装完（321 / 719）、只有 AppHash 可信任（38）、启动对齐当快照重放（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **挑了 not already accepted ≠ 322 / 33 interchangeable：** 官方把本地挑选和 Offer 交给应用分开。
- **最高 not already restored ≠ 已经装完 interchangeable：** 官方把挑选单句和装回路径分开。
- **排过了 not already app-format ≠ 已经是应用要的格式 interchangeable：** 官方把排序启发式和应用收下格式分开；322 snapshotdiscover vs offer bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 挑了 | 不是 already accepted | 不是 ListSnapshots 齐 alone（722） |
| 最高 | 不是 already restored | 不是 Offer 装完 alone（321 / 719） |
| 排过了 | 不是 already app-format | 不是 Offer 被拒 alone（724） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事（322 余量），必须分开挑了 是不是 already accepted interchangeable / 322 snapshotdiscover bundled interchangeable / snapshotdiscover-sold-as-listed interchangeable、最高 是不是 already restored interchangeable、排过了 是不是 already app-format interchangeable。可以跳过「看见挑了最高就已经收下 interchangeable / 就已经装完 interchangeable / 就已经是应用要的格式 interchangeable」。不要另写怎样挑。322 snapshotdiscover vs offer bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshotdiscover-notstop-vs-bundled.md`](worked-example-snapshotdiscover-notstop-vs-bundled.md)（不变量 724 item 3）。322 snapshotdiscover vs offer bundled unbundling 在 722 + 723 + 724 完成。

## 本页不抄

- 怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数。
- Snapshot Discovery bundled。那是不变量 322。
- ListSnapshots 回了不是已经有了全部快照。那是不变量 322 item 1 余量 / 722。
- Offer 被拒不是已经停。那是不变量 322 item 3 余量 / 724。
- Offer 收下已经装完。那是不变量 321 / 719。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
