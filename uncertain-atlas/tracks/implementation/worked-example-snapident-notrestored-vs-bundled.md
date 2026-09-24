# 例：看见对上了 / 看见能拉 / 看见 Metadata 在 is not already already restored interchangeable / already settled interchangeable / already complete interchangeable

**层次**：实现 / 快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量）/ not 851 snapident-notrestored interchangeable / not 368 snapident bundled interchangeable」，不是 snapident bundled（368），也不是引擎不解释 format / hash 不是已经轻验 AppHash（852 item 2 余量）或空快照也至少 1 块不是已经齐（853 item 3 余量）。不要另写怎样写 Snapshot 类型。

## 官方三件事

规范把 Methods 里一份快照只有全部字段都相等（包括 `Metadata`）才算各节点同一份、同一份才能从各节点拉 chunk 和「已经是对上了就已经装完 interchangeable / 已经是能拉就已经交差 interchangeable / 已经是 Metadata 在就已经齐 interchangeable / 已经是 snapident bundled interchangeable」分开写成三件独立的实现事，不是「看见对上了就已经装完 interchangeable / 就已经交差 interchangeable / 就已经齐 interchangeable」一件事：

1. **看见对上了 / 看见快照全字段（含 `Metadata`）对上才算同一份 / 看见同一份 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable / 368 snapident bundled interchangeable / 321 offer interchangeable / snapshot-sold-as-identical interchangeable，也不是已经 snapident bundled（368） interchangeable / 851 snapident-notrestored interchangeable / 368 snapident item 1 interchangeable，也不是已经快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事 bundled（368 item 1 余量） interchangeable / 368 snapident item 1 interchangeable，也不是已经引擎不解释就已经轻验 AppHash（852） interchangeable / 853 snapident-notcomplete interchangeable / 322 listsnap interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable。**  
   官方写：一份快照只有全部字段都相等（包括 `Metadata`）才算各节点同一份。看见对上了，不是已经装完。看见对上了，不是已经 restored interchangeable——368 钉 bundled 三事，本页从 item 1 侧钉 not already restored 单句。看见快照全字段（含 `Metadata`）对上才算同一份，不是已经 snapident bundled（368） interchangeable——368 钉 bundled，本页钉 item 1 第一件事。看见对上了，不是已经引擎不解释就已经轻验 AppHash（852） interchangeable——852 另钉 item 2。看见对上了，不是已经至少 1 块就已经齐（853） interchangeable——853 另钉 item 3。368 snapshot-vs-identical bundled unbundling 在本页 item 1 启动。

2. **看见能拉 / 看见同一份才能从各节点拉 chunk / 看见对上了就能拉 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 368 snapident bundled interchangeable / 33 fourgates interchangeable，也不是已经 snapident bundled（368） interchangeable / 851 snapident-notrestored interchangeable / 368 snapident item 2 不解释 interchangeable / 368 snapident item 3 至少 1 块 interchangeable，也不是已经快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事 bundled（368 item 1 余量） interchangeable / 368 snapident item 1 interchangeable，也不是已经装完（本页第一件事） interchangeable。**  
   官方写：看见能拉，不是已经交差。看见同一份才能从各节点拉 chunk，不是已经 settled interchangeable——本页钉 not already settled 单句。看见对上了就能拉，不是已经装完（本页第一件事） interchangeable——三件事分开钉。368 snapshot-vs-identical bundled unbundling 在本页 item 1 启动。

3. **看见 `Metadata` 在 / 看见全字段含 Metadata / 看见 Metadata 字段在 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 368 snapident bundled interchangeable / 322 listsnap interchangeable，也不是已经 snapident bundled（368） interchangeable / 851 snapident-notrestored interchangeable / 368 snapident item 2 / 368 snapident item 3，也不是已经快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事 bundled（368 item 1 余量） interchangeable / 368 snapident item 1 interchangeable，也不是已经装完（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见 `Metadata` 在，不是已经齐。看见全字段含 Metadata，不是已经 complete interchangeable——本页钉 not already complete 单句。看见 Metadata 字段在，不是已经交差（本页第二件事） interchangeable——三件事分开钉。368 snapshot-vs-identical bundled unbundling 在本页 item 1 启动。

怎样编 `Snapshot`、怎样切块、怎样比较哈希是规范里的做法，本页不抄。snapident bundled（368）、引擎不解释 format / hash 不是已经轻验 AppHash（368 item 2 余量 / 852）、空快照也至少 1 块不是已经齐（368 item 3 余量 / 853）、Offer 收下就已经装完（321）、ListSnapshots 回了就已经齐（322）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **对上了 not already restored ≠ 368 / 321 interchangeable：** 官方把同一份和已经装完分开。
- **能拉 not already settled ≠ 已经交差 interchangeable：** 官方把能拉和已经交差分开。
- **Metadata 在 not already complete ≠ 已经齐 interchangeable：** 官方把 Metadata 在和已经齐分开；368 snapshot-vs-identical bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 对上了 | 不是 already restored | 不是 Offer 收下就已经装完 alone（321） |
| 能拉 | 不是 already settled | 不是引擎不解释 already apphash-light alone（852） |
| Metadata 在 | 不是 already complete | 不是至少 1 块 already complete alone（853） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量），必须分开对上了 是不是 already restored interchangeable / 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable、能拉 是不是 already settled interchangeable、Metadata 在 是不是 already complete interchangeable。可以跳过「看见对上了就已经装完 interchangeable / 就已经交差 interchangeable / 就已经齐 interchangeable」。不要另写怎样写 Snapshot 类型。368 snapshot-vs-identical bundled unbundling 在本页 item 1 启动；完成 [`worked-example-snapident-notapphash-vs-bundled.md`](worked-example-snapident-notapphash-vs-bundled.md)（不变量 852 item 2）；完成 [`worked-example-snapident-notcomplete-vs-bundled.md`](worked-example-snapident-notcomplete-vs-bundled.md)（不变量 853 item 3）。

## 本页不抄

- 怎样编 `Snapshot`、怎样切块、怎样比较哈希。
- snapident bundled。那是不变量 368。
- 引擎不解释 format / hash 不是已经轻验 AppHash。那是不变量 368 item 2 余量 / 852。
- 空快照也至少 1 块不是已经齐。那是不变量 368 item 3 余量 / 853。
- Offer 收下就已经装完。那是不变量 321。
- ListSnapshots 回了就已经齐。那是不变量 322。
- 应用快照就已经从创世重放。那是不变量 38。
