# 例：看见只留最近两份 is not already all-history interchangeable / not already five-fields interchangeable / not already settled interchangeable

**层次**：实现 / 只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量）/ not 952 snapshot-take-notall interchangeable / not 324 snapshot-take-vs-commit bundled interchangeable」，不是快照 bundled（324），也不是 ListSnapshots 已经齐（322），也不是 Snapshot Connection 已经必须实现（334）。不要另写怎样拍快照或怎样切块。

## 官方三件事

1. **看见只留最近两份 / 看见 Hash 对上了 这份保留 is not already 已经有了全部历史快照 interchangeable，也不是已经快照 bundled（324） interchangeable / 952 snapshot-take-notall interchangeable / 950 snapshot-take-notafter interchangeable / 951 snapshot-take-notcons interchangeable / 324 snapshot-take item 1 拍了这个高度 interchangeable，也不是已经只留最近两份 not already all-history / not already five-fields / not already settled 正式三事 bundled（324 item 3 余量） interchangeable / 324 snapshot-take item 3 interchangeable。**  
   官方写：旧快照过一段时间应删掉；一般只留最近两份，免得最后一份正在被别人装回时被删。看见只留两份，不是已经有了全部历史 interchangeable——本页从 324 item 3 侧钉 not already all-history 单句。324 snapshot-take vs commit bundled unbundling 在本页 item 3 完成。

2. **看见 Hash 对上 / 看见只留两份 / 这份保留 is not already 已经五个字段都相同 interchangeable，也不是已经快照 bundled（324） interchangeable / 952 snapshot-take-notall interchangeable / 324 snapshot-take item 2 没停链 interchangeable / 951 snapshot-take-notcons interchangeable，也不是已经 ListSnapshots 已经齐 interchangeable / 322 snapshot-discover interchangeable。**  
   官方写：一份快照要被当成同一份，Height / Format / Chunks / Hash / Metadata 五个字段都要相同。看见 Hash 对上，不是五个字段都对上 interchangeable。本页钉 not already five-fields 单句。

3. **看见 Hash / 看见只留两份 / 这份保留 is not already 已经交差 interchangeable，也不是已经快照 bundled（324） interchangeable / 952 snapshot-take-notall interchangeable / 950 snapshot-take-notafter interchangeable，也不是已经 Snapshot Connection 已经必须实现 interchangeable / 334 snapshot-conn interchangeable。**  
   官方把 Hash 和已经是轻验 AppHash 分开。看见 Hash，不是已经交差 interchangeable。324 snapshot-take vs commit bundled unbundling 在本页 item 3 完成。

怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份当产品常数是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **只留最近两份 not already all-history ≠ 已经有了全部历史快照 interchangeable：** 官方把生产者只留两份和发现端每节点 10 份分开。
- **看见 Hash 对上 not already five-fields ≠ 已经五个字段都相同 interchangeable：** 官方把 Hash 对上和五个字段都相同分开。
- **看见 Hash not already settled ≠ 已经交差 interchangeable：** 官方把 Hash 和已经是轻验 AppHash 分开；324 snapshot-take vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 只留最近两份 | 不是已经有了全部历史快照 | 不是 ListSnapshots 已经齐（322） |
| 看见 Hash 对上 | 不是已经五个字段都相同 | 不是 Snapshot Connection 已经必须实现（334） |
| 看见 Hash | 不是已经交差 | 不是拍了就已经交差之后拍（950） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量），必须分开是不是已经有了全部历史、是不是已经五个字段都相同、是不是已经交差。可以跳过「看见拍了就已经交差之后拍」。不要另写怎样拍快照或怎样切块。不要把最近两份当不确定默认。324 snapshot-take vs commit bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份当产品常数。
- 快照 bundled。那是不变量 324。
- ListSnapshots 已经齐。那是不变量 322。
- Snapshot Connection 已经必须实现。那是不变量 334。
