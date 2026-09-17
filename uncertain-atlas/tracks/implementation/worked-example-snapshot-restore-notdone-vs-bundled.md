# 例：看见 OfferSnapshot 收下了 is not already restored interchangeable / not already has-chunks interchangeable / not already settled interchangeable

**层次**：实现 / Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量）/ not 959 snapshot-restore-notdone interchangeable / not 321 snapshot-restore-vs-offer bundled interchangeable」，不是装回 bundled（321），也不是只有 AppHash 可信任（38），也不是 Offer 被拒就已经停（322/958）。不要另写怎样切块或怎样装。

## 官方三件事

1. **看见 OfferSnapshot 收下了 / 看见选了这份快照 这份收下 is not already 已经装完 interchangeable，也不是已经装回 bundled（321） interchangeable / 959 snapshot-restore-notdone interchangeable / 960 snapshot-restore-notchunk interchangeable / 321 snapshot-restore item 2 一块 chunk 收下 interchangeable，也不是已经 Offer 收下 not already restored / not already has-chunks / not already settled 正式三事 bundled（321 item 1 余量） interchangeable / 321 snapshot-restore item 1 interchangeable。**  
   官方写：OfferSnapshot 收下之后，CometBFT 才开始从元数据字段完全一样的邻居拉 chunk。chunk 先进临时目录，再按顺序交给 ApplySnapshotChunk，直到全部收下。看见收下了 Offer，不是已经装完 interchangeable——本页从 321 item 1 侧钉 not already restored 单句。321 snapshot-restore vs offer bundled unbundling 在本页 item 1 启动。

2. **看见选了这份 / 看见收下了 Offer / 这份收下 is not already 已经有了全部块 interchangeable，也不是已经装回 bundled（321） interchangeable / 959 snapshot-restore-notdone interchangeable / 321 snapshot-restore item 3 拉失败换一份 interchangeable / 961 snapshot-restore-notresume interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-only interchangeable。**  
   官方把收下 Offer 和已经有块分开——321 bundled 第一件事常与 38 混成「看见收下就已经装完或已经可信任 interchangeable」，本页钉 not already has-chunks 单句。

3. **看见元数据对上 / 看见收下了 Offer / 这份收下 is not already 已经交差 interchangeable，也不是已经装回 bundled（321） interchangeable / 959 snapshot-restore-notdone interchangeable / 960 snapshot-restore-notchunk interchangeable，也不是已经 Offer 被拒就已经停 interchangeable / 322/958 snapshot-discover-nothalt interchangeable。**  
   官方把元数据对上和已经验过 AppHash 分开。看见元数据对上，不是已经交差 interchangeable。321 snapshot-restore vs offer bundled unbundling 在本页 item 1 启动。

怎样切块、怎样序列化、怎样实现 ApplySnapshotChunk 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Offer 收下 not already restored ≠ 已经装完 interchangeable：** 官方把收下和按顺序装 chunk 分开。
- **看见选了这份 not already has-chunks ≠ 已经有了全部块 interchangeable：** 官方把选了这份和已经有块分开。
- **看见元数据对上 not already settled ≠ 已经交差 interchangeable：** 官方把元数据对上和已经验过 AppHash 分开；321 snapshot-restore vs offer bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Offer 收下 | 不是已经装完 | 不是只有 AppHash 可信任（38） |
| 看见选了这份 | 不是已经有了全部块 | 不是 Offer 被拒就已经停（322/958） |
| 看见元数据对上 | 不是已经交差 | 不是一块 chunk 收下就已经齐（960） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下 not already restored / not already has-chunks / not already settled 正式三事（321 余量），必须分开是不是已经装完、是不是已经有了全部块、是不是已经交差。可以跳过「看见 Offer 收下就已经装完」。不要另写怎样切块或怎样装。321 snapshot-restore vs offer bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-restore-notchunk-vs-bundled.md`](worked-example-snapshot-restore-notchunk-vs-bundled.md)（不变量 960 item 2）。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 ApplySnapshotChunk。
- 装回 bundled。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 被拒就已经停。那是不变量 322/958。
