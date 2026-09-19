# 例：看见只留最近两份 / 看见 Hash 对上了 / 看见有 Hash is not already already full-history-retained interchangeable / already five-field-same interchangeable / already apphash-light-check interchangeable

**层次**：实现 / 只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量）/ not 730 snapshottake-notretained interchangeable / not 324 snapshottake bundled interchangeable」，不是 Taking Snapshots bundled（324），也不是拍了这个高度不是已经交差之后拍的（728 item 1 余量）或没停链不是已经一致（729 item 2 余量）。不要另写怎样拍快照或怎样切块。

## 官方三件事

规范把 Requirements 里旧快照过一段时间应删掉、一般只留最近两份、同一份要五个字段都相同、`Hash` 只是任意哈希用来在拉 chunk 时比对 和「已经是只留两份就已经有了全部历史快照 interchangeable / 已经是 Hash 对上就已经五字段同一份 interchangeable / 已经是有 Hash 就已经轻验 AppHash interchangeable / 已经是 Taking Snapshots bundled interchangeable」分开写成三件独立的实现事，不是「看见只留最近两份 / 看见 Hash 对上了就已经有了全部历史 interchangeable / 就已经五字段同一份 interchangeable / 就已经轻验 AppHash interchangeable」一件事：

1. **看见只留最近两份 / 看见旧快照删了 / 看见只留两份 is not already 已经有了全部历史快照 interchangeable / 已经 full-history-retained interchangeable / 已经生产者全历史交差 interchangeable / 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 730 snapshottake-notretained interchangeable / 324 snapshottake item 3 interchangeable，也不是已经只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事 bundled（324 item 3 余量） interchangeable / 324 snapshottake item 3 interchangeable，也不是已经拍了这个高度不是已经交差之后拍的（728） interchangeable / 729 snapshottake-notconsistent interchangeable / 322 snapshotdiscover interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：旧快照过一段时间应删掉；一般只留**最近两份**，免得最后一份正在被别人装回时被删。看见只留最近两份，不是已经有了全部历史快照 interchangeable——324 钉 bundled 三事，本页从 item 3 侧钉 not already full-history-retained 单句。看见旧快照删了，不是已经 Taking Snapshots bundled（324） interchangeable——324 钉 bundled，本页钉 item 3 第一件事。看见只留两份，不是已经 ListSnapshots 已经齐（322） interchangeable——322 另钉发现端每节点 10 份，本页钉生产者只留两份。324 snapshottake vs commit bundled unbundling 在本页 item 3 完成。

2. **看见 Hash 对上了 / 看见 Hash 相同 / 看见拉 chunk 时 Hash 对 is not already 已经五字段都相同 interchangeable / 已经 five-field-same interchangeable / 已经 Height/Format/Chunks/Hash/Metadata 交差 interchangeable / 324 snapshottake bundled interchangeable / 321 snapshotrestore interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 730 snapshottake-notretained interchangeable / 324 snapshottake item 1 拍高度 interchangeable / 324 snapshottake item 2 三件保证 interchangeable，也不是已经只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事 bundled（324 item 3 余量） interchangeable / 324 snapshottake item 3 interchangeable，也不是已经有了全部历史（本页第一件事） interchangeable。**  
   官方写：一份快照要被当成同一份，**Height / Format / Chunks / Hash / Metadata 五个字段都要相同**。看见 Hash 对上了，不是已经 five-field-same interchangeable——本页钉 not already five-field-same 单句。看见 Hash 相同，不是已经有了全部历史（本页第一件事） interchangeable——三件事分开钉。看见拉 chunk 时 Hash 对，不是已经 Offer 收下就已经装完（321） interchangeable——321 另钉装回。324 snapshottake vs commit bundled unbundling 在本页 item 3 完成。

3. **看见有 Hash / 看见任意哈希字段 / 看见 Hash 在 is not already 已经是轻验 AppHash interchangeable / 已经 apphash-light-check interchangeable / 已经 AppHash 轻验交差 interchangeable / 324 snapshottake bundled interchangeable / 38 apphash interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 730 snapshottake-notretained interchangeable / 324 snapshottake item 1 / 324 snapshottake item 2，也不是已经只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事 bundled（324 item 3 余量） interchangeable / 324 snapshottake item 3 interchangeable，也不是已经有了全部历史（本页第一件事） interchangeable / 已经五字段同一份（本页第二件事） interchangeable。**  
   官方写：`Hash` 只是任意哈希，用来在拉 chunk 时比对是不是同一份。看见有 Hash，不是已经 apphash-light-check interchangeable——本页钉 not already apphash-light-check 单句。看见任意哈希字段，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界。看见 Hash 在，不是已经五字段同一份（本页第二件事） interchangeable——三件事分开钉。324 snapshottake vs commit bundled unbundling 在本页 item 3 完成。

怎样用 RocksDB / MVCC 拍、怎样切成 10 MB、把最近两份当产品常数是规范里的取值或做法，本页不抄。Taking Snapshots bundled（324）、拍了这个高度不是已经交差之后拍的（324 item 1 余量 / 728）、没停链不是已经一致（324 item 2 余量 / 729）、只有 AppHash 可信任（38）、Offer 收下已经装完（321）、ListSnapshots 已经齐（322）、切进共识已经有完整历史（323）是另外那套，本页不抄。

## 官方为什么这样拆

- **只留两份 not already full-history-retained ≠ 324 / 33 interchangeable：** 官方把生产者只留两份和已经有了全部历史分开。
- **Hash 对上 not already five-field-same ≠ 已经五字段同一份 interchangeable：** 官方把 Hash 对上和五个字段都相同分开。
- **有 Hash not already apphash-light-check ≠ 已经轻验 AppHash interchangeable：** 官方把任意 Hash 和 AppHash 轻验分开；324 snapshottake vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 只留最近两份 | 不是 already full-history-retained | 不是 ListSnapshots alone（322） |
| Hash 对上 | 不是 already five-field-same | 不是 Offer 装完 alone（321） |
| 有 Hash | 不是 already apphash-light-check | 不是 Only AppHash alone（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量），必须分开只留最近两份 是不是 already full-history-retained interchangeable / 324 snapshottake bundled interchangeable / snapshottake-sold-as-committed interchangeable、Hash 对上 是不是 already five-field-same interchangeable、有 Hash 是不是 already apphash-light-check interchangeable。可以跳过「看见只留最近两份就已经有了全部历史 interchangeable / 就已经五字段同一份 interchangeable / 就已经轻验 AppHash interchangeable」。不要另写怎样拍快照。324 snapshottake vs commit bundled unbundling 在本页 item 3 完成（728 + 729 + 730）。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份或 10 MB 当产品常数。
- Taking Snapshots bundled。那是不变量 324。
- 拍了这个高度不是已经交差之后拍的。那是不变量 324 item 1 余量 / 728。
- 没停链不是已经一致。那是不变量 324 item 2 余量 / 729。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 收下已经装完。那是不变量 321。
- ListSnapshots 已经齐。那是不变量 322。
- 切进共识已经有完整历史。那是不变量 323。
