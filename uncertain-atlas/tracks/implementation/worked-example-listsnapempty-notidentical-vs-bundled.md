# 例：看见 ListSnapshots 回包 snapshots 是本地状态快照清单 is not already identical interchangeable / not already restored interchangeable / not already settled interchangeable

**层次**：实现 / ListSnapshots 本地清单 not already identical / not already restored / not already settled 正式三事（395 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ListSnapshots 本地清单 not already identical / not already restored / not already settled 正式三事（395 余量）/ not 735 listsnapempty-notidentical interchangeable / not 395 listsnapempty-vs-discovery bundled interchangeable」，不是 ListSnapshots 空请求 bundled（395），也不是全字段对上就已经装完（368）或 Offer 收下就已经装完（321）。不要另写怎样写 ListSnapshots 空请求。

## 官方三件事

1. **看见 ListSnapshots 回包 `snapshots` 是本地状态快照清单 / 看见回了清单 / 本地清单 is not already 已经五个字段都对上、已经是同一份 interchangeable / 368 snapidentical interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 735 listsnapempty-notidentical interchangeable / 734 listsnapempty-notcomplete interchangeable / 395 listsnapempty item 1 空请求 interchangeable，也不是已经本地清单 not already identical / not already restored / not already settled 正式三事 bundled（395 item 2 余量） interchangeable / 395 listsnapempty item 2 interchangeable。**  
   官方写：`snapshots` 是本地状态快照清单。看见回了清单，不是已经五个字段都对上、已经是同一份 interchangeable——本页从 395 item 2 侧钉 not already identical 单句。395 listsnapempty vs discovery bundled unbundling 在本页 item 2 续。

2. **看见回了清单 / 看见有本地清单 / 本地清单 is not already 已经装完 interchangeable / 321 offerrestored interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 735 listsnapempty-notidentical interchangeable / 395 listsnapempty item 3 用来发现 interchangeable / 736 listsnapempty-notchunks interchangeable。**  
   官方把本地清单和已经装完分开——395 bundled 第二件事常与 321 混成「看见回了清单就已经装完 interchangeable」，本页钉 not already restored 单句。

3. **看见回了清单 / 看见能回 / 本地清单 is not already 已经交差 interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 735 listsnapempty-notidentical interchangeable / 734 listsnapempty-notcomplete interchangeable / 396 OfferSnapshot 请求 snapshot 就已经是本地清单 interchangeable。**  
   官方把能回本地清单和已经交差、已经是 Offer 那份 snapshot 分开。看见能回，不是已经交差 interchangeable，也不是已经 396 interchangeable。395 listsnapempty vs discovery bundled unbundling 在本页 item 2 续。

怎样写 ListSnapshots 空请求、怎样填空请求、怎样填本地清单是规范里的做法，本页不抄。

## 官方为什么这样拆

- **本地清单 not already identical ≠ 368 interchangeable：** 官方把本地清单和全字段对上就已经是同一份分开。
- **本地清单 not already restored ≠ 321 interchangeable：** 官方把本地清单和已经装完分开。
- **本地清单 not already settled ≠ 已经交差 / 396 interchangeable：** 官方把能回清单和已经交差、已经是 Offer snapshot 分开；395 listsnapempty vs discovery bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ListSnapshots 回包 snapshots 是本地状态快照清单 | 不是已经是同一份（368） | 不是空请求要清单（734/395 item 1） |
| 看见回了清单 | 不是已经装完（321） | 不是 ListSnapshots 空请求 bundled（395） |
| 看见能回 | 不是已经交差 / 396 | 不是用来发现就已经在拉块（736/395 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 本地清单 not already identical / not already restored / not already settled 正式三事（395 余量），必须分开本地清单是不是已经是同一份 interchangeable / 368、是不是已经装完 interchangeable / 321、是不是已经交差 / 396。可以跳过「看见回了清单就已经是同一份」。不要另写怎样写 ListSnapshots 空请求。395 listsnapempty vs discovery bundled unbundling 在本页 item 2 续；完成 [`worked-example-listsnapempty-notchunks-vs-bundled.md`](worked-example-listsnapempty-notchunks-vs-bundled.md)（不变量 736 item 3）。

## 本页不抄

- 怎样写 ListSnapshots 空请求、怎样填空请求、怎样填本地清单。
- ListSnapshots 空请求 bundled。那是不变量 395。
- ListSnapshots 空请求要清单。那是不变量 395 item 1 余量 / 734。
- ListSnapshots 用来发现邻居上有哪些快照。那是不变量 395 item 3 余量 / 736。
- 全字段（含 Metadata）对上就已经装完。那是不变量 368。
- Offer 收下就已经装完。那是不变量 321。
- OfferSnapshot 请求 snapshot 就已经是本地清单。那是不变量 396。
