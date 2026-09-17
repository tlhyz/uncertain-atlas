# 例：看见空快照也至少 1 块、网上一份快照报文最多 4 MB is not already complete interchangeable / not already consensus constant interchangeable / not already restored interchangeable

**层次**：实现 / 空快照至少 1 块 not already complete / not already consensus constant / not already restored 正式三事（368 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「空快照至少 1 块 not already complete / not already consensus constant / not already restored 正式三事（368 余量）/ not 823 snapshot-notcomplete interchangeable / not 368 snapshot-vs-identical bundled interchangeable」，不是 Snapshot 类型 bundled（368），也不是 ListSnapshots 回了就已经齐（322），也不是 LoadSnapshot 16 MB 就已经是 4 MB 快照报文（375/802），也不是 Offer 收下就已经装完（321）。不要另写怎样写 Snapshot 类型。

## 官方三件事

1. **看见空快照也至少 1 块、网上一份快照报文最多 4 MB / 看见有块数 / 这份上限 is not already 已经齐 interchangeable / 322 listed interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 823 snapshot-notcomplete interchangeable / 821 snapshot-notrestored interchangeable / 368 snapshot item 1 对上 interchangeable，也不是已经空快照至少 1 块 not already complete / not already consensus constant / not already restored 正式三事 bundled（368 item 3 余量） interchangeable / 368 snapshot item 3 interchangeable。**  
   官方写：`chunks` 是快照里的块数，至少是 1，哪怕是空快照。看见写成 1，不是已经齐 interchangeable——本页从 368 item 3 侧钉 not already complete 单句。368 snapshot vs identical bundled unbundling 在本页 item 3 完成。

2. **看见有块数 / 看见有上限 / 这份上限 is not already 已经是共识常数 interchangeable / 375 loadchunk interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 823 snapshot-notcomplete interchangeable / 368 snapshot item 2 不解释 interchangeable / 822 snapshot-nothash interchangeable，也不是已经 LoadSnapshot 16 MB 就已经是 4 MB 快照报文 interchangeable / 375 loadchunk / 802 loadchunk-not4mb interchangeable。**  
   官方把有上限和已经是共识常数分开——368 bundled 第三件事常与 322 / 375 混成「看见有块数就已经齐或已经是共识常数 interchangeable」，本页钉 not already consensus constant 单句。

3. **看见有块数 / 看见能发 / 这份上限 is not already 已经装完 interchangeable，也不是已经 Snapshot 类型 bundled（368） interchangeable / 823 snapshot-notcomplete interchangeable / 821 snapshot-notrestored interchangeable，也不是已经 Offer 收下就已经装完 interchangeable / 321 restored interchangeable。**  
   官方把能发和已经装完分开。看见能发，不是已经装完 interchangeable。368 snapshot vs identical bundled unbundling 在本页 item 3 完成。

怎样编 Snapshot、怎样切块、怎样比较哈希是规范里的做法，本页不抄。

## 官方为什么这样拆

- **空快照至少 1 块 not already complete ≠ 322 interchangeable：** 官方把至少 1 块和已经齐分开。
- **看见有上限 not already consensus constant ≠ 375 interchangeable：** 官方把 4 MB 快照报文和共识常数分开。
- **看见能发 not already restored ≠ 已经装完 interchangeable：** 官方把能发和已经装完分开；368 snapshot vs identical bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 空快照也至少 1 块、网上一份快照报文最多 4 MB | 不是已经齐（322） | 不是全字段对上（821/368 item 1） |
| 看见有上限 | 不是已经是共识常数 | 不是 LoadSnapshot 16 MB（375/802） |
| 看见能发 | 不是已经装完 | 不是 Offer 收下就已经装完（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空快照至少 1 块 not already complete / not already consensus constant / not already restored 正式三事（368 余量），必须分开是不是已经齐 interchangeable / 322、是不是已经是共识常数、是不是已经装完。可以跳过「看见有块数就已经齐」。不要另写怎样写 Snapshot 类型。368 snapshot vs identical bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 Snapshot、怎样切块、怎样比较哈希。
- Snapshot 类型 bundled。那是不变量 368。
- 全字段对上。那是不变量 368 item 1 余量 / 821。
- ListSnapshots 回了就已经齐。那是不变量 322。
- LoadSnapshot 16 MB 就已经是 4 MB 快照报文。那是不变量 375 / 802。
