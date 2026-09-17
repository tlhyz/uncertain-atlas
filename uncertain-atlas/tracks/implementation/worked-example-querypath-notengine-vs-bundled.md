# 例：看见 path 按 URI 路径解释、/store 必须按键查 is not already engine using interchangeable / not already filter interchangeable / not already settled interchangeable

**层次**：实现 / path /store not already engine using / not already filter / not already settled 正式三事（377 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「path /store not already engine using / not already filter / not already settled 正式三事（377 余量）/ not 798 querypath-notengine interchangeable / not 377 querypath-vs-store bundled interchangeable」，不是 Query 路径 bundled（377），也不是有 /store 路径就已经是引擎在用（326），也不是 Query 回包 index 就已经是按键查（380/788），也不是 Query 回包 info 就已经是按键查（384/778）。不要另写怎样写 Query 路径。

## 官方三件事

1. **看见 `path` 按 URI 路径解释、`/store` 必须按键查 / 看见写了 `/store` / 这份路径 is not already 已经是引擎在用 interchangeable / 326 querystore interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 798 querypath-notengine interchangeable / 797 querypath-notheight interchangeable / 377 querypath item 1 data interchangeable，也不是已经 path /store not already engine using / not already filter / not already settled 正式三事 bundled（377 item 2 余量） interchangeable / 377 querypath item 2 interchangeable。**  
   官方写：`path` 给应用按 URI 路径分量解释。应用必须把 `/store` 或任何以 `/store/` 开头的路径当成底层店上的按键查询；这时键应当写在 `data` 里。看见写了 `/store`，不是已经是引擎在用 interchangeable——本页从 377 item 2 侧钉 not already engine using 单句。377 querypath vs store bundled unbundling 在本页 item 2 续。

2. **看见写了 `/store` / 看见能带路径 / 这份路径 is not already 已经是过滤 interchangeable / 326 querystore interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 798 querypath-notengine interchangeable / 377 querypath item 3 类型路径 interchangeable / 799 querypath-notrequired interchangeable，也不是已经 Query 回包 index 就已经是按键查 interchangeable / 380 queryindex / 788 queryindex-notstore interchangeable，也不是已经 Query 回包 info 就已经是按键查 interchangeable / 384 querycode / 778 querycode-notkey interchangeable。**  
   官方把能带路径和已经是过滤分开——377 bundled 第二件事常与 326 / 380 / 384 混成「看见写了 /store 就已经是引擎在用或已经是过滤 interchangeable」，本页钉 not already filter 单句。

3. **看见写了 `/store` / 看见键在 `data` / 这份路径 is not already 已经交差 interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 798 querypath-notengine interchangeable / 797 querypath-notheight interchangeable。**  
   官方把键在 data 和已经交差分开。看见键在 `data`，不是已经交差 interchangeable。377 querypath vs store bundled unbundling 在本页 item 2 续。

怎样写 Query 请求、怎样填 data / path、怎样做按键查询是规范里的做法，本页不抄。

## 官方为什么这样拆

- **path /store not already engine using ≠ 326 interchangeable：** 官方把应用必须按键查和引擎眼下只用 /p2p 分开。
- **看见能带路径 not already filter ≠ 已经是过滤 interchangeable：** 官方把能带路径和已经是过滤分开。
- **看见键在 data not already settled ≠ 已经交差 interchangeable：** 官方把键在 data 和已经交差分开；377 querypath vs store bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| path 按 URI 路径解释、/store 必须按键查 | 不是已经是引擎在用（326） | 不是 data 查询分量（797/377 item 1） |
| 看见写了 /store | 不是已经是过滤 | 不是 Query 回包 index（380/788） |
| 看见键在 data | 不是已经交差 | 不是 Query 回包 info（384/778） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 path /store not already engine using / not already filter / not already settled 正式三事（377 余量），必须分开是不是已经是引擎在用 interchangeable / 326、是不是已经是过滤、是不是已经交差。可以跳过「看见写了 /store 就已经是引擎在用」。不要另写怎样写 Query 路径。377 querypath vs store bundled unbundling 在本页 item 2 续；续 [`worked-example-querypath-notrequired-vs-bundled.md`](worked-example-querypath-notrequired-vs-bundled.md)（不变量 799 item 3）。

## 本页不抄

- 怎样写 Query 请求、怎样填 data / path、怎样做按键查询。
- Query 路径 bundled。那是不变量 377。
- data 按 URI 查询分量解释。那是不变量 377 item 1 余量 / 797。
- 有 /store 路径就已经是引擎在用。那是不变量 326。
- Query 回包 index 就已经是按键查。那是不变量 380 / 788。
