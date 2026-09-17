# 例：看见一块 chunk 收下了 is not already complete interchangeable / not already banned interchangeable / not already settled interchangeable

**层次**：实现 / 一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量）/ not 960 snapshot-restore-notchunk interchangeable / not 321 snapshot-restore-vs-offer bundled interchangeable」，不是装回 bundled（321），也不是启动对齐已经是快照重放（314），也不是切进共识已经有完整历史（323/955）。不要另写怎样切块或怎样装。

## 官方三件事

1. **看见 ApplySnapshotChunk 收下了一块 / 看见回了再拉 这份回法 is not already 已经齐 interchangeable，也不是已经装回 bundled（321） interchangeable / 960 snapshot-restore-notchunk interchangeable / 959 snapshot-restore-notdone interchangeable / 321 snapshot-restore item 1 Offer 收下 interchangeable，也不是已经一块 chunk 收下 not already complete / not already banned / not already settled 正式三事 bundled（321 item 2 余量） interchangeable / 321 snapshot-restore item 2 interchangeable。**  
   官方写：怎样装回完全由应用决定。装的过程中，应用可以回：收下这块等下一块，也可以要再拉当前这块或前面若干块，也可以封禁邻居、拒掉或重试这份快照。看见收下一块，不是已经齐 interchangeable——本页从 321 item 2 侧钉 not already complete 单句。321 snapshot-restore vs offer bundled unbundling 在本页 item 2 续。

2. **看见回了再拉 / 看见收下一块 / 这份回法 is not already 已经封禁 interchangeable，也不是已经装回 bundled（321） interchangeable / 960 snapshot-restore-notchunk interchangeable / 321 snapshot-restore item 3 拉失败换一份 interchangeable / 961 snapshot-restore-notresume interchangeable，也不是已经启动对齐已经是快照重放 interchangeable / 314 querystate interchangeable。**  
   官方把回再拉和已经封禁分开。看见回了再拉，不是已经封禁 interchangeable。本页钉 not already banned 单句。

3. **看见能回指令 / 看见收下一块 / 这份回法 is not already 已经交差 interchangeable，也不是已经装回 bundled（321） interchangeable / 960 snapshot-restore-notchunk interchangeable / 959 snapshot-restore-notdone interchangeable，也不是已经切进共识已经有完整历史 interchangeable / 323/955 snapshot-switch-nothist interchangeable。**  
   官方把能回指令和已经交差分开。看见能回指令，不是已经交差 interchangeable。321 snapshot-restore vs offer bundled unbundling 在本页 item 2 续。

怎样切块、怎样序列化、怎样实现 ApplySnapshotChunk 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **一块 chunk 收下 not already complete ≠ 已经齐 interchangeable：** 官方把回再拉 / 封禁 / 拒快照和已经交差分开。
- **看见回了再拉 not already banned ≠ 已经封禁 interchangeable：** 官方把回再拉和已经封禁分开。
- **看见能回指令 not already settled ≠ 已经交差 interchangeable：** 官方把能回指令和已经交差分开；321 snapshot-restore vs offer bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一块 chunk 收下 | 不是已经齐 | 不是启动对齐已经是快照重放（314） |
| 看见回了再拉 | 不是已经封禁 | 不是切进共识已经有完整历史（323/955） |
| 看见能回指令 | 不是已经交差 | 不是拉失败换一份就已经能接着装（961） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量），必须分开是不是已经齐、是不是已经封禁、是不是已经交差。可以跳过「看见 Offer 收下就已经装完」。不要另写怎样切块或怎样装。321 snapshot-restore vs offer bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-restore-notresume-vs-bundled.md`](worked-example-snapshot-restore-notresume-vs-bundled.md)（不变量 961 item 3）。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 ApplySnapshotChunk。
- 装回 bundled。那是不变量 321。
- 启动对齐已经是快照重放。那是不变量 314。
- 切进共识已经有完整历史。那是不变量 323/955。
