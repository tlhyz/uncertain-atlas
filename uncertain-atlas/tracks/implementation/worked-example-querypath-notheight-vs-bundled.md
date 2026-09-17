# 例：看见 data 按 URI 查询分量解释 is not already Query height interchangeable / not already fresh interchangeable / not already settled interchangeable

**层次**：实现 / data not already Query height / not already fresh / not already settled 正式三事（377 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「data not already Query height / not already fresh / not already settled 正式三事（377 余量）/ not 797 querypath-notheight interchangeable / not 377 querypath-vs-store bundled interchangeable」，不是 Query 路径 bundled（377），也不是 Query 高度就已经是 QueryState（371），也不是 Query 回包 key 就已经是 Query 高度（380/789），也不是 Query 证明 height 就已经是请求高度（383/781）。不要另写怎样写 Query 路径。

## 官方三件事

1. **看见 `data` 按 URI 查询分量解释、可以和 `path` 一起或代替 `path` 用 / 看见填了 `data` / 这份查询分量 is not already 已经是 Query 高度 interchangeable / 371 queryheight interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 797 querypath-notheight interchangeable / 798 querypath-notengine interchangeable / 377 querypath item 2 path interchangeable，也不是已经 data not already Query height / not already fresh / not already settled 正式三事 bundled（377 item 1 余量） interchangeable / 377 querypath item 1 interchangeable。**  
   官方写：`data` 是给应用按 URI 查询分量解释的请求参数。可以和 `path` 一起用，也可以代替 `path`。看见填了 `data`，不是已经填了高度 interchangeable——本页从 377 item 1 侧钉 not already Query height 单句。377 querypath vs store bundled unbundling 在本页 item 1 启动。

2. **看见填了 `data` / 看见能代替 `path` / 这份查询分量 is not already 已经新鲜 interchangeable / 371 queryheight interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 797 querypath-notheight interchangeable / 377 querypath item 3 类型路径 interchangeable / 799 querypath-notrequired interchangeable，也不是已经 Query 回包 key 就已经是 Query 高度 interchangeable / 380 queryindex / 789 queryindex-notheight interchangeable，也不是已经 Query 证明 height 就已经是请求高度 interchangeable / 383 queryprove / 781 queryprove-notreqh interchangeable。**  
   官方把能代替 path 和已经新鲜分开——377 bundled 第一件事常与 371 / 380 / 383 混成「看见填了 data 就已经是 Query 高度或已经新鲜 interchangeable」，本页钉 not already fresh 单句。

3. **看见填了 `data` / 看见有字节 / 这份查询分量 is not already 已经交差 interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 797 querypath-notheight interchangeable / 798 querypath-notengine interchangeable。**  
   官方把有字节和已经交差分开。看见有字节，不是已经交差 interchangeable。377 querypath vs store bundled unbundling 在本页 item 1 启动。

怎样写 Query 请求、怎样填 data / path、怎样做按键查询是规范里的做法，本页不抄。

## 官方为什么这样拆

- **data not already Query height ≠ 371 interchangeable：** 官方把查询分量和高度分开。
- **看见能代替 path not already fresh ≠ 已经新鲜 interchangeable：** 官方把能代替 path 和已经新鲜分开。
- **看见有字节 not already settled ≠ 已经交差 interchangeable：** 官方把有字节和已经交差分开；377 querypath vs store bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| data 按 URI 查询分量解释 | 不是已经是 Query 高度（371） | 不是 path /store（798/377 item 2） |
| 看见填了 data | 不是已经新鲜 | 不是 Query 回包 key（380/789） |
| 看见有字节 | 不是已经交差 | 不是 Query 证明 height（383/781） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 data not already Query height / not already fresh / not already settled 正式三事（377 余量），必须分开是不是已经是 Query 高度 interchangeable / 371、是不是已经新鲜、是不是已经交差。可以跳过「看见填了 data 就已经是 Query 高度」。不要另写怎样写 Query 路径。377 querypath vs store bundled unbundling 在本页 item 1 启动；续 [`worked-example-querypath-notengine-vs-bundled.md`](worked-example-querypath-notengine-vs-bundled.md)（不变量 798 item 2）。

## 本页不抄

- 怎样写 Query 请求、怎样填 data / path、怎样做按键查询。
- Query 路径 bundled。那是不变量 377。
- path /store 必须按键查。那是不变量 377 item 2 余量 / 798。
- Query 高度就已经是 QueryState。那是不变量 371。
- Query 回包 key 就已经是 Query 高度。那是不变量 380 / 789。
