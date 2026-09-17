# 例：看见没停链 is not already consistent interchangeable / not already same-bytes interchangeable / not already settled interchangeable

**层次**：实现 / 没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量）/ not 951 snapshot-take-notcons interchangeable / not 324 snapshot-take-vs-commit bundled interchangeable」，不是快照 bundled（324），也不是切进共识已经有完整历史（323），也不是 ListSnapshots 已经齐（322）。不要另写怎样拍快照或怎样切块。

## 官方三件事

1. **看见在后台拍 / 看见没停链 这份保证 is not already 已经隔离在单一高度 interchangeable，也不是已经快照 bundled（324） interchangeable / 951 snapshot-take-notcons interchangeable / 950 snapshot-take-notafter interchangeable / 324 snapshot-take item 1 拍了这个高度 interchangeable，也不是已经没停链 not already consistent / not already same-bytes / not already settled 正式三事 bundled（324 item 2 余量） interchangeable / 324 snapshot-take item 2 interchangeable。**  
   官方写：应用必须同时给三件保证。Consistent：必须拍在单一隔离高度，不受并发写影响。Asynchronous：拍可以很慢，但不得停链。看见没停链，不是已经隔离 interchangeable——本页从 324 item 2 侧钉 not already consistent 单句。324 snapshot-take vs commit bundled unbundling 在本页 item 2 续。

2. **看见在后台拍 / 看见没停链 / 这份保证 is not already 已经各节点字节相同 interchangeable，也不是已经快照 bundled（324） interchangeable / 951 snapshot-take-notcons interchangeable / 324 snapshot-take item 3 只留两份 interchangeable / 952 snapshot-take-notall interchangeable，也不是已经切进共识已经有完整历史 interchangeable / 323 snapshot-switch interchangeable。**  
   官方写：Deterministic：同一高度、同一 Format，各节点必须字节相同，含全部元数据。看见在后台拍，不是已经各节点相同 interchangeable。本页钉 not already same-bytes 单句。

3. **看见同一高度 / 看见没停链 / 这份保证 is not already 已经交差 interchangeable，也不是已经快照 bundled（324） interchangeable / 951 snapshot-take-notcons interchangeable / 950 snapshot-take-notafter interchangeable，也不是已经 ListSnapshots 已经齐 interchangeable / 322 snapshot-discover interchangeable。**  
   官方把同一高度和已经同一格式分开。看见同一高度，不是已经交差 interchangeable。324 snapshot-take vs commit bundled unbundling 在本页 item 2 续。

怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份当产品常数是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **没停链 not already consistent ≠ 已经隔离在单一高度 interchangeable：** 官方把后台拍和必须隔离在单一高度分开。
- **看见在后台拍 not already same-bytes ≠ 已经各节点字节相同 interchangeable：** 官方把异步拍和各节点字节相同分开。
- **看见同一高度 not already settled ≠ 已经交差 interchangeable：** 官方把同一高度和已经同一格式分开；324 snapshot-take vs commit bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没停链 | 不是已经一致 | 不是切进共识已经有完整历史（323） |
| 看见在后台拍 | 不是已经各节点字节相同 | 不是 ListSnapshots 已经齐（322） |
| 看见同一高度 | 不是已经交差 | 不是只留两份就已经有全部历史（952） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没停链 not already consistent / not already same-bytes / not already settled 正式三事（324 余量），必须分开是不是已经隔离、是不是已经各节点字节相同、是不是已经交差。可以跳过「看见拍了就已经交差之后拍」。不要另写怎样拍快照或怎样切块。不要把最近两份当不确定默认。324 snapshot-take vs commit bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-take-notall-vs-bundled.md`](worked-example-snapshot-take-notall-vs-bundled.md)（不变量 952 item 3）。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份当产品常数。
- 快照 bundled。那是不变量 324。
- 切进共识已经有完整历史。那是不变量 323。
- ListSnapshots 已经齐。那是不变量 322。
