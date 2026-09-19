# 例：看见换了一份 / 看见能重试 / 看见失败了 is not already already can-resume interchangeable / already same-snapshot interchangeable / already prior-usable interchangeable

**层次**：实现 / 拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事（321 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事（321 余量）/ not 721 snapshotrestore-notresume interchangeable / not 321 snapshotrestore bundled interchangeable」，不是 Snapshot Restoration bundled（321），也不是 Offer 收下不是已经装完（719 item 1 余量）或一块 chunk 收下不是已经齐（720 item 2 余量）。不要另写怎样切块或怎样装。

## 官方三件事

规范把 Requirements 里 CometBFT 一段时间拉不到一块会拒掉这份快照再经 `OfferSnapshot` 换一份、应用自己决定要不要支持**重新开始装**还是直接报错退出 和「已经是换了一份就已经能接着上次 interchangeable / 已经是能重试就已经同一份 interchangeable / 已经是失败了就已经装过的还能用 interchangeable / 已经是 Snapshot Restoration bundled interchangeable」分开写成三件独立的实现事，不是「看见拉一块失败 / 看见换了一份快照就已经能接着装 interchangeable / 就已经同一份 interchangeable / 就已经装过的还能用 interchangeable」一件事：

1. **看见换了一份 / 看见拉一块失败换了一份快照 / 看见拒掉这份再 Offer 换一份 is not already 已经能接着装 interchangeable / 已经 can-resume interchangeable / 已经能接着上次交差 interchangeable / 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 721 snapshotrestore-notresume interchangeable / 321 snapshotrestore item 3 interchangeable，也不是已经拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事 bundled（321 item 3 余量） interchangeable / 321 snapshotrestore item 3 interchangeable，也不是已经 Offer 收下不是已经装完（719） interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable / 322 snapshotdiscover interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：一段时间拉不到一块，会拒掉这份快照，再经 `OfferSnapshot` 换一份；应用自己决定要不要支持重新开始装。看见换了一份，不是已经能接着装 interchangeable——321 钉 bundled 三事，本页从 item 3 侧钉 not already can-resume 单句。看见拉一块失败换了一份快照，不是已经 Snapshot Restoration bundled（321） interchangeable——321 钉 bundled，本页钉 item 3 第一件事。看见拒掉这份再 Offer 换一份，不是已经 Offer 收下不是已经装完（719） interchangeable——719 另钉 item 1，本页钉 item 3 第一件事。321 snapshotrestore vs offer bundled unbundling 在本页 item 3 启动。

2. **看见能重试 / 看见应用支持重新开始装 / 看见又能 Offer 一份 is not already 已经同一份 interchangeable / 已经 same-snapshot interchangeable / 已经同一份快照交差 interchangeable / 321 snapshotrestore bundled interchangeable / 322 snapshotdiscover interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 721 snapshotrestore-notresume interchangeable / 321 snapshotrestore item 1 Offer interchangeable / 321 snapshotrestore item 2 chunk interchangeable，也不是已经拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事 bundled（321 item 3 余量） interchangeable / 321 snapshotrestore item 3 interchangeable，也不是已经能接着装（本页第一件事） interchangeable。**  
   官方把换一份和已经同一份路径分开——能重试，不等于已经同一份。看见能重试，不是已经 same-snapshot interchangeable——本页钉 not already same-snapshot 单句。看见应用支持重新开始装，不是已经一块 chunk 收下不是已经齐（720） interchangeable——720 另钉 item 2，本页钉 item 3 第二件事。看见又能 Offer 一份，不是已经 Snapshot Discovery 已经列出（322） interchangeable——322 另钉，本页钉 item 3 第二件事。321 snapshotrestore vs offer bundled unbundling 在本页 item 3 启动。

3. **看见失败了 / 看见拉不到一块失败了 / 看见拒掉这份快照 is not already 已经装过的还能用 interchangeable / 已经 prior-usable interchangeable / 已经半装还能接着用 interchangeable / 321 snapshotrestore bundled interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable，也不是已经 Snapshot Restoration bundled（321） interchangeable / 721 snapshotrestore-notresume interchangeable / 321 snapshotrestore item 1 / 321 snapshotrestore item 2，也不是已经拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事 bundled（321 item 3 余量） interchangeable / 321 snapshotrestore item 3 interchangeable，也不是已经能接着装（本页第一件事） interchangeable / 已经同一份（本页第二件事） interchangeable。**  
   官方把失败拒掉这份和已经装过的还能用路径分开——失败了，不等于已经装过的还能用。看见失败了，不是已经 prior-usable interchangeable——本页钉 not already prior-usable 单句。看见拉不到一块失败了，不是已经能接着装（本页第一件事） interchangeable——三件事分开钉。看见拒掉这份快照，不是已经 chunk 齐交差（720） interchangeable——720 另钉收下一块侧。321 snapshotrestore vs offer bundled unbundling 在本页 item 3 完成。

怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk` 是规范里的取值或做法，本页不抄。Snapshot Restoration bundled（321）、Offer 收下不是已经装完（321 item 1 余量 / 719）、一块 chunk 收下不是已经齐（321 item 2 余量 / 720）、Snapshot Discovery（322）、只有 AppHash 可信任（38 / 483）、启动对齐当快照重放（314）、崩溃三步（320）是另外那套，本页不抄。

## 官方为什么这样拆

- **换了一份 not already can-resume ≠ 321 / 33 interchangeable：** 官方把换一份与应用是否支持重新开始装分开。
- **能重试 not already same-snapshot ≠ 已经同一份 interchangeable：** 官方把换一份单句和已经同一份路径分开。
- **失败了 not already prior-usable ≠ 已经装过的还能用 interchangeable：** 官方把拒掉这份与半装还能用路径分开；321 snapshotrestore vs offer bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 换了一份 | 不是 already can-resume | 不是 Offer 装完 alone（719） |
| 能重试 | 不是 already same-snapshot | 不是 Discovery alone（322） |
| 失败了 | 不是 already prior-usable | 不是 chunk 齐 alone（720） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事（321 余量），必须分开换了一份 是不是 already can-resume interchangeable / 321 snapshotrestore bundled interchangeable / snapshotrestore-sold-as-offered interchangeable、能重试 是不是 already same-snapshot interchangeable、失败了 是不是 already prior-usable interchangeable。可以跳过「看见拉一块失败 / 看见换了一份快照就已经能接着装 interchangeable / 就已经同一份 interchangeable / 就已经装过的还能用 interchangeable」。不要另写怎样切块或怎样装。321 snapshotrestore vs offer bundled unbundling 在本页 item 3 完成（719 + 720 + 721）。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk`。
- Snapshot Restoration bundled。那是不变量 321。
- Offer 收下不是已经装完。那是不变量 321 item 1 余量 / 719。
- 一块 chunk 收下不是已经齐。那是不变量 321 item 2 余量 / 720。
- Snapshot Discovery。那是不变量 322。
- 只有 AppHash 可信任。那是不变量 38 / 483。
- 启动对齐当快照重放。那是不变量 314。
- 崩溃三步。那是不变量 320。
