# 例：看见 OfferSnapshot 收下了不是已经装完；看见一块 chunk 收下了不是已经齐；看见拉失败换一份不是已经能接着装

**层次**：实现 / Snapshot Restoration。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Offer 收下不是已经装完 / 一块 chunk 收下不是已经齐 / 拉失败换一份不是已经能接着装」，不是只有 AppHash 可信任，也不是启动对齐已经是快照重放。不要另写怎样切块或怎样装。

## 官方三件事

规范把快照装回写成三件独立的实现事，不是「看见 OfferSnapshot 收下就已经装完、已经齐、已经能失败后续装」一件事：

1. **看见 OfferSnapshot 收下了 / 看见选了这份快照 不是已经装完，也不是已经有了全部块。**  
   官方写：`OfferSnapshot` 收下之后，CometBFT 才开始从**元数据字段完全一样**的邻居拉 chunk。chunk 先进临时目录，再按顺序交给 `ApplySnapshotChunk`，直到全部收下。看见收下了 Offer，不是已经装完。看见选了这份，不是已经有块。看见元数据对上，不是已经验过 AppHash。
2. **看见 ApplySnapshotChunk 收下了一块 / 看见回了再拉 不是已经齐，也不是已经装完。**  
   官方写：怎样装回完全由应用决定。装的过程中，应用可以回：收下这块等下一块，也可以要再拉当前这块或前面若干块，也可以封禁邻居、拒掉或重试这份快照。看见收下一块，不是已经齐。看见回了再拉，不是已经封禁。看见能回指令，不是已经交差。
3. **看见拉一块失败 / 看见换了一份快照 不是已经能接着装，也不是已经同一份。**  
   官方写：CometBFT 一段时间拉不到一块，会拒掉这份快照，再经 `OfferSnapshot` 换一份。应用自己决定要不要支持**重新开始装**，还是直接报错退出。看见换了一份，不是已经能接着上次。看见能重试，不是已经同一份。看见失败了，不是已经装过的还能用。

怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk` 是规范里的取值或做法，本页不抄。只有 AppHash 可信任是不变量 38，本页不抄。

## 官方为什么这样拆

- **Offer 收下 ≠ 已经装完：** 官方把收下和按顺序装 chunk 分开。
- **一块 chunk 收下 ≠ 已经齐：** 官方把回再拉 / 封禁 / 拒快照和已经交差分开。
- **拉失败换一份 ≠ 已经能接着装：** 官方把换一份和能不能重新开始装分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Offer 收下 | 不是已经装完 | 不是只有 AppHash 可信任（38） |
| 一块 chunk 收下 | 不是已经齐 | 不是启动对齐已经是快照重放（314） |
| 拉失败换一份 | 不是已经能接着装 | 不是崩溃三步已经 Commit（320） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「快照已经收下」，必须分开 Offer 收下是不是已经装完、一块 chunk 收下是不是已经齐、拉失败换一份是不是已经能接着装。可以跳过「看见 Offer 收下就已经装完」。不要另写怎样切块或怎样装。321 snapshotrestore vs offer bundled unbundling 完成（719 + 720 + 721）；精读 [`worked-example-snapshotrestore-notrestored-vs-bundled.md`](worked-example-snapshotrestore-notrestored-vs-bundled.md)（不变量 719 item 1）；[`worked-example-snapshotrestore-notchunkcomplete-vs-bundled.md`](worked-example-snapshotrestore-notchunkcomplete-vs-bundled.md)（不变量 720 item 2）；[`worked-example-snapshotrestore-notresume-vs-bundled.md`](worked-example-snapshotrestore-notresume-vs-bundled.md)（不变量 721 item 3）。

## 本页不抄

- 怎样切块、怎样序列化、怎样实现 `ApplySnapshotChunk`。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
- 崩溃三步。那是不变量 320。
