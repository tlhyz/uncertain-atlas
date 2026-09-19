# 例：看见收下一块 / 看见回了再拉 / 看见能回指令 is not already already complete interchangeable / already banned interchangeable / already settled interchangeable

**层次**：实现 / 一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量）/ not 720 snapshotrestore-notchunkcomplete interchangeable / not 321 snapshotrestore bundled interchangeable」，不是 Snapshot Restoration bundled（321），也不是 Offer 收下不是已经装完（719 item 1 余量）或拉失败换一份不是已经能接着装（721 item 3 余量）。不要另写怎样切块或怎样装。

## 官方三件事

规范把 Requirements 里怎样装回完全由应用决定、装的过程中应用可以回收下这块等下一块 / 再拉当前这块或前面若干块 / 封禁邻居 / 拒掉或重试这份快照 和「已经是收下一块就已经齐 interchangeable / 已经是回了再拉就已经封禁 interchangeable / 已经是能回指令就已经交差 interchangeable / 已经是 Snapshot Restoration bundled interchangeable」分开写成三件独立的实现事，不是「看见 ApplySnapshotChunk 收下了一块就已经齐 interchangeable / 就已经封禁 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见收下一块 / 看见 ApplySnapshotChunk 收下了一块 / 看见回了收下这块等下一块 is not already 已经齐 interchangeable / 已经 complete interchangeable / 已经 chunk 齐交差 interchangeable / 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable / 321 snapshotrestore item 2 interchangeable，也不是已经一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事 bundled（321 item 2 余量） interchangeable / 321 snapshotrestore item 2 interchangeable，也不是已经 Offer 收下不是已经装完（719） interchangeable / 721 snapshotrestore-notresume interchangeable / 378 applysnap interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：怎样装回完全由应用决定；应用可以回收下这块等下一块。看见收下一块，不是已经齐 interchangeable——321 钉 bundled 三事，本页从 item 2 侧钉 not already complete 单句。看见 ApplySnapshotChunk 收下了一块，不是已经 Snapshot Restoration bundled（321） interchangeable——321 钉 bundled，本页钉 item 2 第一件事。看见回了收下这块等下一块，不是已经 Offer 收下不是已经装完（719） interchangeable——719 另钉 item 1，本页钉 item 2 第一件事。321 snapshotrestore vs offer bundled unbundling 在本页 item 2 续。

2. **看见回了再拉 / 看见要再拉当前这块 / 看见再拉前面若干块 is not already 已经封禁 interchangeable / 已经 banned interchangeable / 已经封禁邻居交差 interchangeable / 321 snapshotrestore bundled interchangeable / 378 applysnap interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable / 321 snapshotrestore item 1 Offer interchangeable / 321 snapshotrestore item 3 换一份 interchangeable，也不是已经一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事 bundled（321 item 2 余量） interchangeable / 321 snapshotrestore item 2 interchangeable，也不是已经齐（本页第一件事） interchangeable。**  
   官方把可以回再拉和已经封禁邻居路径分开——回了再拉，不等于已经封禁。看见回了再拉，不是已经 banned interchangeable——本页钉 not already banned 单句。看见要再拉当前这块，不是已经拉失败换一份不是已经能接着装（721） interchangeable——721 另钉 item 3，本页钉 item 2 第二件事。看见再拉前面若干块，不是已经 ApplySnapshotChunk Result 封禁（378） interchangeable——378 另钉，本页钉 item 2 第二件事。321 snapshotrestore vs offer bundled unbundling 在本页 item 2 续。

3. **看见能回指令 / 看见能回封禁邻居 / 看见能回拒掉或重试这份快照 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经装回交差 interchangeable / 321 snapshotrestore bundled interchangeable / 719 snapshotrestore-notrestored interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable / 321 snapshotrestore item 1 / 321 snapshotrestore item 3，也不是已经一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事 bundled（321 item 2 余量） interchangeable / 321 snapshotrestore item 2 interchangeable，也不是已经齐（本页第一件事） interchangeable / 已经封禁（本页第二件事） interchangeable。**  
   官方把能回指令（封禁 / 拒掉 / 重试）和已经交差 / 已经装完路径分开——能回指令，不等于已经交差。看见能回指令，不是已经 settled interchangeable——本页钉 not already settled 单句。看见能回封禁邻居，不是已经齐（本页第一件事） interchangeable——三件事分开钉。看见能回拒掉或重试这份快照，不是已经 Offer 收下就已经装完（719） interchangeable——719 另钉 Offer 收下侧。321 snapshotrestore vs offer bundled unbundling 在本页 item 2 完成。

怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk` 是规范里的取值或做法，本页不抄。Snapshot Restoration bundled（321）、Offer 收下不是已经装完（321 item 1 余量 / 719）、拉失败换一份不是已经能接着装（321 item 3 余量 / 721）、ApplySnapshotChunk Result（378）、只有 AppHash 可信任（38 / 483）、启动对齐当快照重放（314）、崩溃三步（320）是另外那套，本页不抄。

## 官方为什么这样拆

- **收下一块 not already complete ≠ 321 / 33 interchangeable：** 官方把收下一块等下一块单句和已经齐路径分开。
- **回了再拉 not already banned ≠ 已经封禁 interchangeable：** 官方把再拉指令单句和已经封禁邻居路径分开。
- **能回指令 not already settled ≠ 已经交差 interchangeable：** 官方把可回封禁/拒/重试与已经交差路径分开；321 snapshotrestore vs offer bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 收下一块 | 不是 already complete | 不是 Offer 装完 alone（719） |
| 回了再拉 | 不是 already banned | 不是换一份 alone（721） |
| 能回指令 | 不是 already settled | 不是 Apply Result alone（378） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量），必须分开收下一块 是不是 already complete interchangeable / 321 snapshotrestore bundled interchangeable / snapshotrestore-sold-as-offered interchangeable、回了再拉 是不是 already banned interchangeable、能回指令 是不是 already settled interchangeable。可以跳过「看见 ApplySnapshotChunk 收下了一块就已经齐 interchangeable / 就已经封禁 interchangeable / 就已经交差 interchangeable」。不要另写怎样切块或怎样装。321 snapshotrestore vs offer bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshotrestore-notresume-vs-bundled.md`](worked-example-snapshotrestore-notresume-vs-bundled.md)（不变量 721 item 3，待写）。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk`。
- Snapshot Restoration bundled。那是不变量 321。
- Offer 收下不是已经装完。那是不变量 321 item 1 余量 / 719。
- 拉失败换一份不是已经能接着装。那是不变量 321 item 3 余量 / 721。
- ApplySnapshotChunk Result。那是不变量 378。
- 只有 AppHash 可信任。那是不变量 38 / 483。
- 启动对齐当快照重放。那是不变量 314。
- 崩溃三步。那是不变量 320。
