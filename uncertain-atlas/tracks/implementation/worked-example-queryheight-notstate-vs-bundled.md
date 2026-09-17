# 例：看见 Query 可以对当前或过去高度查 is not already QueryState interchangeable / not already replicated interchangeable / not already settled interchangeable

**层次**：实现 / Query 高度 not already QueryState / not already replicated / not already settled 正式三事（371 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 高度 not already QueryState / not already replicated / not already settled 正式三事（371 余量）/ not 812 queryheight-notstate interchangeable / not 371 queryheight-vs-committed bundled interchangeable」，不是 Query 高度 bundled（371），也不是 Query 回了就已经复制到各节点（329），也不是 data 就已经是 Query 高度（377/797），也不是 Query 回包 key 就已经是 Query 高度（380/789）。不要另写怎样写 Query 高度。

## 官方三件事

1. **看见 Query 可以对当前或过去高度查 / 看见能查 / 这份高度 is not already 已经是 QueryState interchangeable / 329 queryrep interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 812 queryheight-notstate interchangeable / 813 queryheight-notfresh interchangeable / 371 queryheight item 2 默认 0 interchangeable，也不是已经 Query 高度 not already QueryState / not already replicated / not already settled 正式三事 bundled（371 item 1 余量） interchangeable / 371 queryheight item 1 interchangeable。**  
   官方写：Query 查应用在当前或过去高度的数据。看见能查，不是已经是 QueryState interchangeable——本页从 371 item 1 侧钉 not already QueryState 单句。371 queryheight vs committed bundled unbundling 在本页 item 1 启动。

2. **看见能查 / 看见填了高度 / 这份高度 is not already 已经复制到各节点 interchangeable / 329 queryrep interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 812 queryheight-notstate interchangeable / 371 queryheight item 3 Merkle 根 interchangeable / 814 queryheight-notapphash interchangeable，也不是已经 data 就已经是 Query 高度 interchangeable / 377 querypath / 797 querypath-notheight interchangeable，也不是已经 Query 回包 key 就已经是 Query 高度 interchangeable / 380 queryindex / 789 queryindex-notheight interchangeable。**  
   官方把填了高度和已经复制到各节点分开——371 bundled 第一件事常与 329 / 377 / 380 混成「看见能查就已经是 QueryState 或已经复制 interchangeable」，本页钉 not already replicated 单句。

3. **看见能查 / 看见能回 / 这份高度 is not already 已经交差 interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 812 queryheight-notstate interchangeable / 813 queryheight-notfresh interchangeable。**  
   官方把能回和已经交差分开。看见能回，不是已经交差 interchangeable。371 queryheight vs committed bundled unbundling 在本页 item 1 启动。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Query 高度 not already QueryState ≠ 329 interchangeable：** 官方把查哪一高度和 QueryState 那份只读副本分开。
- **看见填了高度 not already replicated ≠ 已经复制 interchangeable：** 官方把填了高度和已经复制到各节点分开。
- **看见能回 not already settled ≠ 已经交差 interchangeable：** 官方把能回和已经交差分开；371 queryheight vs committed bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 可以对当前或过去高度查 | 不是已经是 QueryState（329） | 不是默认 0（813/371 item 2） |
| 看见能查 | 不是已经复制到各节点 | 不是 data 就已经是 Query 高度（377/797） |
| 看见能回 | 不是已经交差 | 不是 Query 回包 key（380/789） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 高度 not already QueryState / not already replicated / not already settled 正式三事（371 余量），必须分开是不是已经是 QueryState interchangeable / 329、是不是已经复制到各节点、是不是已经交差。可以跳过「看见能查就已经是 QueryState」。不要另写怎样写 Query 高度。371 queryheight vs committed bundled unbundling 在本页 item 1 启动；续 [`worked-example-queryheight-notfresh-vs-bundled.md`](worked-example-queryheight-notfresh-vs-bundled.md)（不变量 813 item 2）。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- Query 高度 bundled。那是不变量 371。
- height 默认 0。那是不变量 371 item 2 余量 / 813。
- Query 回了就已经复制到各节点。那是不变量 329。
- data 就已经是 Query 高度。那是不变量 377 / 797。
