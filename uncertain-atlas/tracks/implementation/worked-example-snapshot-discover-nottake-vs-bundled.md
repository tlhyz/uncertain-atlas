# 例：看见挑了最高 is not already offered interchangeable / not already restored interchangeable / not already settled interchangeable

**层次**：实现 / 挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量）/ not 957 snapshot-discover-nottake interchangeable / not 322 snapshot-discover-vs-offer bundled interchangeable」，不是发现 bundled（322），也不是只有 AppHash 可信任（38），也不是拍了就已经交差之后拍（324/950）。不要另写怎样列快照或怎样挑。

## 官方三件事

1. **看见挑了最高 / 看见按高度、格式、邻居数排了 这份挑选 is not already 已经是应用收下的那份 interchangeable，也不是已经发现 bundled（322） interchangeable / 957 snapshot-discover-nottake interchangeable / 956 snapshot-discover-notfull interchangeable / 322 snapshot-discover item 1 ListSnapshots 回了 interchangeable，也不是已经挑了最高 not already offered / not already restored / not already settled 正式三事 bundled（322 item 2 余量） interchangeable / 322 snapshot-discover item 2 interchangeable。**  
   官方写：过一段时间，节点挑一份最合适的（一般按高度、格式、有多少邻居），再经 OfferSnapshot 交给应用。看见挑了，不是已经收下 interchangeable——本页从 322 item 2 侧钉 not already offered 单句。322 snapshot-discover vs offer bundled unbundling 在本页 item 2 续。

2. **看见最高 / 看见挑了 / 这份挑选 is not already 已经装完 interchangeable，也不是已经发现 bundled（322） interchangeable / 957 snapshot-discover-nottake interchangeable / 322 snapshot-discover item 3 Offer 被拒 interchangeable / 958 snapshot-discover-nothalt interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-only interchangeable。**  
   官方把本地挑选和已经装完分开。看见最高，不是已经装完 interchangeable。本页钉 not already restored 单句。

3. **看见排过了 / 看见挑了 / 这份挑选 is not already 已经交差 interchangeable，也不是已经发现 bundled（322） interchangeable / 957 snapshot-discover-nottake interchangeable / 956 snapshot-discover-notfull interchangeable，也不是已经拍了就已经交差之后拍 interchangeable / 324/950 snapshot-take-notafter interchangeable。**  
   官方把排过了和已经是应用要的格式分开。看见排过了，不是已经交差 interchangeable。322 snapshot-discover vs offer bundled unbundling 在本页 item 2 续。

怎样实现 ListSnapshots、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **挑了最高 not already offered ≠ 已经是应用收下的那份 interchangeable：** 官方把本地挑选和 Offer 交给应用分开。
- **看见最高 not already restored ≠ 已经装完 interchangeable：** 官方把挑了最高和已经装完分开。
- **看见排过了 not already settled ≠ 已经交差 interchangeable：** 官方把排过了和已经是应用要的格式分开；322 snapshot-discover vs offer bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 挑了最高 | 不是已经收下 | 不是只有 AppHash 可信任（38） |
| 看见最高 | 不是已经装完 | 不是拍了就已经交差之后拍（324/950） |
| 看见排过了 | 不是已经交差 | 不是 Offer 被拒就已经停（958） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看挑了最高 not already offered / not already restored / not already settled 正式三事（322 余量），必须分开是不是已经收下、是不是已经装完、是不是已经交差。可以跳过「看见问了就已经齐」。不要另写怎样列快照或怎样挑。不要把每节点 10 份当不确定默认。322 snapshot-discover vs offer bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-discover-nothalt-vs-bundled.md`](worked-example-snapshot-discover-nothalt-vs-bundled.md)（不变量 958 item 3）。

## 本页不抄

- 怎样实现 ListSnapshots、怎样挑、把 10 当产品常数。
- 发现 bundled。那是不变量 322。
- 只有 AppHash 可信任。那是不变量 38。
- 拍了就已经交差之后拍。那是不变量 324/950。
