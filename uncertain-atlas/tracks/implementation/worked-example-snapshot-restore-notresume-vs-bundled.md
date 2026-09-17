# 例：看见拉失败换一份 is not already resumable interchangeable / not already same-snapshot interchangeable / not already settled interchangeable

**层次**：实现 / 拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量）/ not 961 snapshot-restore-notresume interchangeable / not 321 snapshot-restore-vs-offer bundled interchangeable」，不是装回 bundled（321），也不是崩溃三步已经 Commit（320），也不是 ListSnapshots 回了就已经齐（322/956）。不要另写怎样切块或怎样装。

## 官方三件事

1. **看见拉一块失败 / 看见换了一份快照 这份换法 is not already 已经能接着装 interchangeable，也不是已经装回 bundled（321） interchangeable / 961 snapshot-restore-notresume interchangeable / 959 snapshot-restore-notdone interchangeable / 960 snapshot-restore-notchunk interchangeable / 321 snapshot-restore item 1 Offer 收下 interchangeable，也不是已经拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事 bundled（321 item 3 余量） interchangeable / 321 snapshot-restore item 3 interchangeable。**  
   官方写：CometBFT 一段时间拉不到一块，会拒掉这份快照，再经 OfferSnapshot 换一份。应用自己决定要不要支持重新开始装，还是直接报错退出。看见换了一份，不是已经能接着上次 interchangeable——本页从 321 item 3 侧钉 not already resumable 单句。321 snapshot-restore vs offer bundled unbundling 在本页 item 3 完成。

2. **看见能重试 / 看见换了一份 / 这份换法 is not already 已经同一份 interchangeable，也不是已经装回 bundled（321） interchangeable / 961 snapshot-restore-notresume interchangeable / 321 snapshot-restore item 2 一块 chunk 收下 interchangeable / 960 snapshot-restore-notchunk interchangeable，也不是已经崩溃三步已经 Commit interchangeable / 320 crash-commit interchangeable。**  
   官方把能重试和已经同一份分开。看见能重试，不是已经同一份 interchangeable。本页钉 not already same-snapshot 单句。

3. **看见失败了 / 看见换了一份 / 这份换法 is not already 已经交差 interchangeable，也不是已经装回 bundled（321） interchangeable / 961 snapshot-restore-notresume interchangeable / 959 snapshot-restore-notdone interchangeable，也不是已经 ListSnapshots 回了就已经齐 interchangeable / 322/956 snapshot-discover-notfull interchangeable。**  
   官方把失败了和已经装过的还能用分开。看见失败了，不是已经交差 interchangeable。321 snapshot-restore vs offer bundled unbundling 在本页 item 3 完成。

怎样切块、怎样序列化、怎样实现 ApplySnapshotChunk 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **拉失败换一份 not already resumable ≠ 已经能接着装 interchangeable：** 官方把换一份和能不能重新开始装分开。
- **看见能重试 not already same-snapshot ≠ 已经同一份 interchangeable：** 官方把能重试和已经同一份分开。
- **看见失败了 not already settled ≠ 已经交差 interchangeable：** 官方把失败了和已经装过的还能用分开；321 snapshot-restore vs offer bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拉失败换一份 | 不是已经能接着装 | 不是崩溃三步已经 Commit（320） |
| 看见能重试 | 不是已经同一份 | 不是 ListSnapshots 回了就已经齐（322/956） |
| 看见失败了 | 不是已经交差 | 不是 Offer 收下就已经装完（959） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量），必须分开是不是已经能接着装、是不是已经同一份、是不是已经交差。可以跳过「看见 Offer 收下就已经装完」。不要另写怎样切块或怎样装。321 snapshot-restore vs offer bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 ApplySnapshotChunk。
- 装回 bundled。那是不变量 321。
- 崩溃三步已经 Commit。那是不变量 320。
- ListSnapshots 回了就已经齐。那是不变量 322/956。
