# 例：看见写了 /store / 看见能带路径 / 看见键在 data is not already already engine interchangeable / already filter interchangeable / already settled interchangeable

**层次**：实现 / path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事（377 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事（377 余量）/ not 879 querypath-notengine interchangeable / not 377 querypath bundled interchangeable」，不是 querypath bundled（377），也不是 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度（878 item 1 余量）或规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有（377 item 3 余量）。不要另写怎样写 Query 路径。

## 官方三件事

规范把 Methods 里 path 按 URI 路径解释、/store 必须按键查 和「已经是写了 /store 就已经是引擎在用 interchangeable / 已经是能带路径就已经是过滤 interchangeable / 已经是键在 data 就已经交差 interchangeable / 已经是 querypath bundled interchangeable」分开写成三件独立的实现事，不是「看见写了 /store 就已经是引擎在用 interchangeable / 就已经是过滤 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见写了 /store / 看见 path 按 URI 路径解释、/store 必须按键查 / 看见写了 /store 路径 is not already 已经是引擎在用 interchangeable / 已经 engine interchangeable / 已经是引擎在用交差 interchangeable / 377 querypath bundled interchangeable / 326 peerfilter interchangeable / querypath-sold-as-store interchangeable，也不是已经 querypath bundled（377） interchangeable / 879 querypath-notengine interchangeable / 377 querypath item 2 interchangeable，也不是已经 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事 bundled（377 item 2 余量） interchangeable / 377 querypath item 2 interchangeable，也不是已经填了 data 就已经是 Query 高度（878） interchangeable / 371 queryheight interchangeable / 写了类型路径就已经是正常运转必须有（377 item 3） interchangeable，也不是已经有 /store 路径就已经是引擎在用（326） interchangeable。**  
   官方写：`path` 给应用按 URI 路径分量解释，例如路由。可以和 `data` 一起用，也可以代替 `data`。应用必须把 `/store` 或任何以 `/store/` 开头的路径当成底层店上的按键查询；这时键应当写在 `data` 里。看见写了 `/store`，不是已经是引擎在用。看见写了 /store，不是已经 engine interchangeable——377 钉 bundled 三事，本页从 item 2 侧钉 not already engine 单句。看见 path 按 URI 路径解释、/store 必须按键查，不是已经 querypath bundled（377） interchangeable——377 钉 bundled，本页钉 item 2 第一件事。看见写了 /store 路径，不是已经有 /store 路径就已经是引擎在用（326） interchangeable——326 另钉。377 querypath-vs-store bundled unbundling 在本页 item 2 续。

2. **看见能带路径 / 看见 path 能带路径 / 看见带了路径 is not already 已经是过滤 interchangeable / 已经 filter interchangeable / 已经是过滤交差 interchangeable / 377 querypath bundled interchangeable / 326 peerfilter interchangeable，也不是已经 querypath bundled（377） interchangeable / 879 querypath-notengine interchangeable / 377 querypath item 1 填了 data interchangeable / 377 querypath item 3 写了类型路径 interchangeable，也不是已经 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事 bundled（377 item 2 余量） interchangeable / 377 querypath item 2 interchangeable，也不是已经是引擎在用（本页第一件事） interchangeable。**  
   官方写：看见能带路径，不是已经是过滤。看见 path 能带路径，不是已经 filter interchangeable——本页钉 not already filter 单句。看见带了路径，不是已经是引擎在用（本页第一件事） interchangeable——三件事分开钉。377 querypath-vs-store bundled unbundling 在本页 item 2 续。

3. **看见键在 data / 看见键应当写在 data 里 / 看见键写在 data is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 377 querypath bundled interchangeable / 878 querypath-notheight interchangeable，也不是已经 querypath bundled（377） interchangeable / 879 querypath-notengine interchangeable / 377 querypath item 1 / 377 querypath item 3，也不是已经 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事 bundled（377 item 2 余量） interchangeable / 377 querypath item 2 interchangeable，也不是已经是引擎在用（本页第一件事） interchangeable / 已经是过滤（本页第二件事） interchangeable。**  
   官方写：看见键在 `data`，不是已经交差。看见键应当写在 data 里，不是已经 settled interchangeable——本页钉 not already settled 单句。看见键写在 data，不是已经是过滤（本页第二件事） interchangeable——三件事分开钉。377 querypath-vs-store bundled unbundling 在本页 item 2 续。

怎样写 Query 请求、怎样填 data / path、怎样做按键查询是规范里的做法，本页不抄。querypath bundled（377）、data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度（377 item 1 余量 / 878）、规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有（377 item 3 余量）、Query 可以对当前或过去高度查就已经是 QueryState（371）、有 /store 路径就已经是引擎在用（326）、实现了 Query 就已经是正常运转必须有（329）是另外那套，本页不抄。

## 官方为什么这样拆

- **写了 /store not already engine ≠ 377 / 326 interchangeable：** 官方把应用必须按键查和引擎眼下只用 /p2p 分开。
- **能带路径 not already filter ≠ 已经是过滤 interchangeable：** 官方把能带路径和已经是过滤分开。
- **键在 data not already settled ≠ 已经交差 interchangeable：** 官方把键在 data 和已经交差分开；377 querypath-vs-store bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写了 /store | 不是 already engine | 不是有 /store 路径就已经是引擎在用 alone（326） |
| 能带路径 | 不是 already filter | 不是填了 data already height alone（878） |
| 键在 data | 不是 already settled | 不是实现了 Query 就已经是正常运转必须有 alone（329） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事（377 余量），必须分开写了 /store 是不是 already engine interchangeable / 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable、能带路径 是不是 already filter interchangeable、键在 data 是不是 already settled interchangeable。可以跳过「看见写了 /store 就已经是引擎在用 interchangeable / 就已经是过滤 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 路径。377 querypath-vs-store bundled unbundling 在本页 item 2 续（878 + 879）。

## 本页不抄

- 怎样写 Query 请求、怎样填 data / path、怎样做按键查询。
- querypath bundled。那是不变量 377。
- data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度。那是不变量 377 item 1 余量 / 878。
- 规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有。那是不变量 377 item 3 余量。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- 有 /store 路径就已经是引擎在用。那是不变量 326。
- 实现了 Query 就已经是正常运转必须有。那是不变量 329。
