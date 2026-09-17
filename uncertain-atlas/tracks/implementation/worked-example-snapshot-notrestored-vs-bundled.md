# 例：看见快照全字段（含 Metadata）对上 is not already restored interchangeable / not already complete interchangeable / not already light-verified AppHash interchangeable

**层次**：实现 / 快照全字段对上 not already restored / not already complete / not already light-verified AppHash 正式三事（368 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「快照全字段对上 not already restored / not already complete / not already light-verified AppHash 正式三事（368 余量）/ not 821 snapshot-notrestored interchangeable / not 368 snapshot-vs-identical bundled interchangeable」，不是 Snapshot 类型 bundled（368），也不是 Offer 收下就已经装完（321），也不是 ListSnapshots 回了就已经齐（322），也不是 LoadSnapshot 三列就已经是同一份（375/801）。不要另写怎样写 Snapshot 类型。

## 官方三件事

1. **看见快照全字段（含 `Metadata`）对上才算同一份、同一份才能从各节点拉 chunk / 看见对上了 / 这份同一 is not already 已经装完 interchangeable / 321 restored interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 821 snapshot-notrestored interchangeable / 822 snapshot-nothash interchangeable / 368 snapshot item 2 不解释 interchangeable，也不是已经快照全字段对上 not already restored / not already complete / not already light-verified AppHash 正式三事 bundled（368 item 1 余量） interchangeable / 368 snapshot item 1 interchangeable。**  
   官方写：一份快照只有全部字段都相等（包括 `Metadata`）才算各节点同一份。同一份才能从各节点拉 chunk。看见对上了，不是已经装完 interchangeable——本页从 368 item 1 侧钉 not already restored 单句。368 snapshot vs identical bundled unbundling 在本页 item 1 启动。

2. **看见对上了 / 看见能拉 / 这份同一 is not already 已经齐 interchangeable / 322 listed interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 821 snapshot-notrestored interchangeable / 368 snapshot item 3 至少 1 块 interchangeable / 823 snapshot-notcomplete interchangeable，也不是已经 Offer 收下就已经装完 interchangeable / 321 restored interchangeable，也不是已经 LoadSnapshot 三列就已经是同一份 interchangeable / 375 loadchunk / 801 loadchunk-notsame interchangeable。**  
   官方把能拉和已经齐分开——368 bundled 第一件事常与 321 / 322 / 375 混成「看见快照对上就已经装完或已经齐 interchangeable」，本页钉 not already complete 单句。

3. **看见对上了 / 看见 Metadata 在 / 这份同一 is not already 已经轻验 AppHash interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 821 snapshot-notrestored interchangeable / 822 snapshot-nothash interchangeable。**  
   官方把 Metadata 在和已经轻验 AppHash 分开。看见 Metadata 在，不是已经轻验 AppHash interchangeable。368 snapshot vs identical bundled unbundling 在本页 item 1 启动。

怎样编 Snapshot、怎样切块、怎样比较哈希是规范里的做法，本页不抄。

## 官方为什么这样拆

- **快照全字段对上 not already restored ≠ 321 interchangeable：** 官方把同一份和已经装完分开。
- **看见能拉 not already complete ≠ 已经齐 interchangeable：** 官方把能拉和已经齐分开。
- **看见 Metadata 在 not already light-verified ≠ 已经轻验 AppHash interchangeable：** 官方把 Metadata 在和已经轻验 AppHash 分开；368 snapshot vs identical bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 快照全字段（含 Metadata）对上 | 不是已经装完（321） | 不是不解释 format/hash（822/368 item 2） |
| 看见能拉 | 不是已经齐 | 不是 ListSnapshots 回了就已经齐（322） |
| 看见 Metadata 在 | 不是已经轻验 AppHash | 不是 LoadSnapshot 三列（375/801） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看快照全字段对上 not already restored / not already complete / not already light-verified AppHash 正式三事（368 余量），必须分开是不是已经装完 interchangeable / 321、是不是已经齐、是不是已经轻验 AppHash。可以跳过「看见快照对上就已经装完」。不要另写怎样写 Snapshot 类型。368 snapshot vs identical bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-nothash-vs-bundled.md`](worked-example-snapshot-nothash-vs-bundled.md)（不变量 822 item 2）。

## 本页不抄

- 怎样编 Snapshot、怎样切块、怎样比较哈希。
- Snapshot 类型 bundled。那是不变量 368。
- 引擎不解释 format / hash。那是不变量 368 item 2 余量 / 822。
- Offer 收下就已经装完。那是不变量 321。
- ListSnapshots 回了就已经齐。那是不变量 322。
