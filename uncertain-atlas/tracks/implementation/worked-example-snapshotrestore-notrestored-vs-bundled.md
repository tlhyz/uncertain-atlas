# 例：看见 Offer 收下 / 看见选了这份 / 看见元数据对上 is not already already restored interchangeable / already all-chunks interchangeable / already AppHash-verified interchangeable

**层次**：实现 / Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量）/ not 719 snapshotrestore-notrestored interchangeable / not 321 snapshotrestore bundled interchangeable」，不是 Snapshot Restoration bundled（321），也不是一块 chunk 收下不是已经齐（720 item 2 余量）或拉失败换一份不是已经能接着装（721 item 3 余量）。不要另写怎样切块或怎样装。

## 官方三件事

规范把 Requirements 里 `OfferSnapshot` 收下之后 CometBFT 才开始从**元数据字段完全一样**的邻居拉 chunk、chunk 先进临时目录再按顺序交给 `ApplySnapshotChunk` 直到全部收下 和「已经是收下就已经装完 interchangeable / 已经是选了这份就已经有了全部块 interchangeable / 已经是元数据对上就已经验过 AppHash interchangeable / 已经是 Snapshot Restoration bundled interchangeable」分开写成三件独立的实现事，不是「看见 OfferSnapshot 收下就已经装完 interchangeable / 就已经有了全部块 interchangeable / 就已经验过 AppHash interchangeable」一件事：

1. **看见 Offer 收下 / 看见 OfferSnapshot 收下了 / 看见 Accept 了这份快照 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装回交差 interchangeable / 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 719 snapshotrestore-notrestored interchangeable / 321 snapshotrestore item 1 interchangeable，也不是已经 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事 bundled（321 item 1 余量） interchangeable / 321 snapshotrestore item 1 interchangeable，也不是已经一块 chunk 收下不是已经齐（720） interchangeable / 721 snapshotrestore-notresume interchangeable / 648 offersnapusage-notrestored interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`OfferSnapshot` 收下之后，CometBFT 才开始拉 chunk 并按顺序装。看见 Offer 收下，不是已经装完 interchangeable——321 钉 bundled 三事，本页从 item 1 侧钉 not already restored 单句。看见 OfferSnapshot 收下了，不是已经 Snapshot Restoration bundled（321） interchangeable——321 钉 bundled，本页钉 item 1 第一件事。看见 Accept 了这份快照，不是已经 OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完（648） interchangeable——648 另钉 Methods Usage 侧，本页钉 Snapshot Restoration item 1。321 snapshotrestore vs offer bundled unbundling 在本页 item 1 启动。

2. **看见选了这份 / 看见选了这份快照 / 看见开始拉 chunk is not already 已经有了全部块 interchangeable / 已经 all-chunks interchangeable / 已经有块交差 interchangeable / 321 snapshotrestore bundled interchangeable / 375 loadsnap interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 719 snapshotrestore-notrestored interchangeable / 321 snapshotrestore item 2 chunk 齐 interchangeable / 321 snapshotrestore item 3 换一份 interchangeable，也不是已经 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事 bundled（321 item 1 余量） interchangeable / 321 snapshotrestore item 1 interchangeable，也不是已经装完（本页第一件事） interchangeable。**  
   官方把收下之后才开始拉 chunk 和已经有了全部块路径分开——选了这份，不等于已经有了全部块。看见选了这份，不是已经 all-chunks interchangeable——本页钉 not already all-chunks 单句。看见选了这份快照，不是已经一块 chunk 收下不是已经齐（720） interchangeable——720 另钉 item 2，本页钉 item 1 第二件事。看见开始拉 chunk，不是已经 LoadSnapshotChunk 已经齐（375） interchangeable——375 另钉，本页钉 item 1 第二件事。321 snapshotrestore vs offer bundled unbundling 在本页 item 1 启动。

3. **看见元数据对上 / 看见元数据字段完全一样 / 看见邻居元数据对上 is not already 已经验过 AppHash interchangeable / 已经 AppHash-verified interchangeable / 已经和 Only AppHash trusted 同一句 interchangeable / 321 snapshotrestore bundled interchangeable / 38 apphash interchangeable / 483 offersnaptrust interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 719 snapshotrestore-notrestored interchangeable / 321 snapshotrestore item 2 / 321 snapshotrestore item 3，也不是已经 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事 bundled（321 item 1 余量） interchangeable / 321 snapshotrestore item 1 interchangeable，也不是已经装完（本页第一件事） interchangeable / 已经有了全部块（本页第二件事） interchangeable。**  
   官方把元数据字段完全一样用来拉 chunk 和已经验过 AppHash / 已经和 Only AppHash trusted 同一句路径分开——元数据对上，不等于已经验过 AppHash。看见元数据对上，不是已经 AppHash-verified interchangeable——本页钉 not already AppHash-verified 单句。看见元数据字段完全一样，不是已经装完（本页第一件事） interchangeable——三件事分开钉。看见邻居元数据对上，不是已经只有 AppHash 可信任（38 / 483） interchangeable——38 / 483 另钉信任边界。321 snapshotrestore vs offer bundled unbundling 在本页 item 1 完成。

怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk` 是规范里的取值或做法，本页不抄。Snapshot Restoration bundled（321）、一块 chunk 收下不是已经齐（321 item 2 余量 / 720）、拉失败换一份不是已经能接着装（321 item 3 余量 / 721）、OfferSnapshot Usage upon accepting（648）、只有 AppHash 可信任（38 / 483）、启动对齐当快照重放（314）、崩溃三步（320）是另外那套，本页不抄。

## 官方为什么这样拆

- **Offer 收下 not already restored ≠ 321 / 33 interchangeable：** 官方把收下之后才拉装单句和已经装完路径分开。
- **选了这份 not already all-chunks ≠ 已经有了全部块 interchangeable：** 官方把开始拉 chunk 单句和已经有块路径分开。
- **元数据对上 not already AppHash-verified ≠ 已经验过 AppHash interchangeable：** 官方把元数据对齐拉块与 AppHash 验信路径分开；321 snapshotrestore vs offer bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Offer 收下 | 不是 already restored | 不是 Usage upon accepting alone（648） |
| 选了这份 | 不是 already all-chunks | 不是 chunk 齐 alone（720） |
| 元数据对上 | 不是 already AppHash-verified | 不是 Only AppHash trusted alone（38 / 483） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下不是已经装完 not already restored / not already all-chunks / not already AppHash-verified 正式三事（321 余量），必须分开 Offer 收下 是不是 already restored interchangeable / 321 snapshotrestore bundled interchangeable / snapshotrestore-sold-as-offered interchangeable、选了这份 是不是 already all-chunks interchangeable、元数据对上 是不是 already AppHash-verified interchangeable。可以跳过「看见 OfferSnapshot 收下就已经装完 interchangeable / 就已经有了全部块 interchangeable / 就已经验过 AppHash interchangeable」。不要另写怎样切块或怎样装。321 snapshotrestore vs offer bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshotrestore-notchunkcomplete-vs-bundled.md`](worked-example-snapshotrestore-notchunkcomplete-vs-bundled.md)（不变量 720 item 2）。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk`。
- Snapshot Restoration bundled。那是不变量 321。
- 一块 chunk 收下不是已经齐。那是不变量 321 item 2 余量 / 720。
- 拉失败换一份不是已经能接着装。那是不变量 321 item 3 余量 / 721。
- OfferSnapshot Usage upon accepting。那是不变量 648。
- 只有 AppHash 可信任。那是不变量 38 / 483。
- 启动对齐当快照重放。那是不变量 314。
- 崩溃三步。那是不变量 320。
