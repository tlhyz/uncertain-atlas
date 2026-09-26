# 例：看见填了 data / 看见能代替 path / 看见有字节 is not already already height interchangeable / already fresh interchangeable / already settled interchangeable

**层次**：实现 / data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量）/ not 878 querypath-notheight interchangeable / not 377 querypath bundled interchangeable」，不是 querypath bundled（377），也不是 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用（377 item 2 余量）或规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有（377 item 3 余量）。不要另写怎样写 Query 路径。

## 官方三件事

规范把 Methods 里 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 和「已经是填了 data 就已经是 Query 高度 interchangeable / 已经是能代替 path 就已经新鲜 interchangeable / 已经是有字节就已经交差 interchangeable / 已经是 querypath bundled interchangeable」分开写成三件独立的实现事，不是「看见填了 data 就已经是 Query 高度 interchangeable / 就已经新鲜 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见填了 data / 看见 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 / 看见填了 data 字段 is not already 已经是 Query 高度 interchangeable / 已经 height interchangeable / 已经是 Query 高度交差 interchangeable / 377 querypath bundled interchangeable / 371 queryheight interchangeable / querypath-sold-as-store interchangeable，也不是已经 querypath bundled（377） interchangeable / 878 querypath-notheight interchangeable / 377 querypath item 1 interchangeable，也不是已经 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事 bundled（377 item 1 余量） interchangeable / 377 querypath item 1 interchangeable，也不是已经写了 /store 就已经是引擎在用（377 item 2） interchangeable / 写了类型路径就已经是正常运转必须有（377 item 3） interchangeable / 326 peerfilter interchangeable，也不是已经 Query 可以对当前或过去高度查就已经是 QueryState（371） interchangeable。**  
   官方写：`data` 是给应用按 URI 查询分量解释的请求参数。可以和 `path` 一起用，也可以代替 `path`。看见填了 `data`，不是已经填了高度。看见填了 data，不是已经 height interchangeable——377 钉 bundled 三事，本页从 item 1 侧钉 not already height 单句。看见 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用，不是已经 querypath bundled（377） interchangeable——377 钉 bundled，本页钉 item 1 第一件事。看见填了 data 字段，不是已经 Query 可以对当前或过去高度查就已经是 QueryState（371） interchangeable——371 另钉。377 querypath-vs-store bundled unbundling 在本页 item 1 启动。

2. **看见能代替 path / 看见 data 可以代替 path / 看见代替 path is not already 已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 377 querypath bundled interchangeable / 371 queryheight interchangeable，也不是已经 querypath bundled（377） interchangeable / 878 querypath-notheight interchangeable / 377 querypath item 2 写了 /store interchangeable / 377 querypath item 3 写了类型路径 interchangeable，也不是已经 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事 bundled（377 item 1 余量） interchangeable / 377 querypath item 1 interchangeable，也不是已经是 Query 高度（本页第一件事） interchangeable。**  
   官方写：看见能代替 `path`，不是已经新鲜。看见 data 可以代替 path，不是已经 fresh interchangeable——本页钉 not already fresh 单句。看见代替 path，不是已经是 Query 高度（本页第一件事） interchangeable——三件事分开钉。377 querypath-vs-store bundled unbundling 在本页 item 1 启动。

3. **看见有字节 / 看见 data 有字节 / 看见填了字节 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 377 querypath bundled interchangeable / 329 query replicated interchangeable，也不是已经 querypath bundled（377） interchangeable / 878 querypath-notheight interchangeable / 377 querypath item 2 / 377 querypath item 3，也不是已经 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事 bundled（377 item 1 余量） interchangeable / 377 querypath item 1 interchangeable，也不是已经是 Query 高度（本页第一件事） interchangeable / 已经新鲜（本页第二件事） interchangeable。**  
   官方写：看见有字节，不是已经交差。看见 data 有字节，不是已经 settled interchangeable——本页钉 not already settled 单句。看见填了字节，不是已经新鲜（本页第二件事） interchangeable——三件事分开钉。377 querypath-vs-store bundled unbundling 在本页 item 1 启动。

怎样写 Query 请求、怎样填 data / path、怎样做按键查询是规范里的做法，本页不抄。querypath bundled（377）、path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用（377 item 2 余量）、规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有（377 item 3 余量）、Query 可以对当前或过去高度查就已经是 QueryState（371）、有 /store 路径就已经是引擎在用（326）、实现了 Query 就已经是正常运转必须有（329）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了 data not already height ≠ 377 / 371 interchangeable：** 官方把查询分量和高度分开。
- **能代替 path not already fresh ≠ 已经新鲜 interchangeable：** 官方把能代替 path 和已经新鲜分开。
- **有字节 not already settled ≠ 已经交差 interchangeable：** 官方把有字节和已经交差分开；377 querypath-vs-store bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 data | 不是 already height | 不是 Query 高度就已经是 QueryState alone（371） |
| 能代替 path | 不是 already fresh | 不是写了 /store already engine alone（377 item 2） |
| 有字节 | 不是 already settled | 不是实现了 Query 就已经是正常运转必须有 alone（329） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量），必须分开填了 data 是不是 already height interchangeable / 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable、能代替 path 是不是 already fresh interchangeable、有字节 是不是 already settled interchangeable。可以跳过「看见填了 data 就已经是 Query 高度 interchangeable / 就已经新鲜 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 路径。377 querypath-vs-store bundled unbundling 在本页 item 1 启动（878）。

## 本页不抄

- 怎样写 Query 请求、怎样填 data / path、怎样做按键查询。
- querypath bundled。那是不变量 377。
- path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用。那是不变量 377 item 2 余量。
- 规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有。那是不变量 377 item 3 余量。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- 有 /store 路径就已经是引擎在用。那是不变量 326。
- 实现了 Query 就已经是正常运转必须有。那是不变量 329。
