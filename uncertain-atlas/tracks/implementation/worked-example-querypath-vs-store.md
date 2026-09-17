# 例：看见 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度；看见 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用；看见规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有

**层次**：实现 / Query 路径。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 / path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 / 规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有」，不是 Query 高度就已经是 QueryState，也不是有 /store 路径就已经是引擎在用。不要另写怎样写 Query 路径。

## 官方三件事

规范把 data 按 URI 查询分量解释、path 按 URI 路径解释且 /store 必须按键查、建议允许按类型查写成三件独立的实现事，不是「看见能带 data / path 就已经是 Query 高度、已经是引擎在用、已经是正常运转必须有」一件事：

1. **看见 `data` 按 URI 查询分量解释、可以和 `path` 一起或代替 `path` 用 / 看见填了 `data` 不是已经是 Query 高度，也不是已经新鲜。**  
   官方写：`data` 是给应用按 [URI 查询分量](https://www.rfc-editor.org/rfc/rfc3986#section-3.4) 解释的请求参数。可以和 `path` 一起用，也可以代替 `path`。看见填了 `data`，不是已经填了高度。看见能代替 `path`，不是已经新鲜。看见有字节，不是已经交差。
2. **看见 `path` 按 URI 路径解释、`/store` 必须按键查 / 看见写了 `/store` 不是已经是引擎在用，也不是已经是过滤。**  
   官方写：`path` 给应用按 [URI 路径分量](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) 解释，例如路由。可以和 `data` 一起用，也可以代替 `data`。应用必须把 `/store` 或任何以 `/store/` 开头的路径当成底层店上的按键查询；这时键应当写在 `data` 里。看见写了 `/store`，不是已经是引擎在用。看见能带路径，不是已经是过滤。看见键在 `data`，不是已经交差。
3. **看见规范建议允许 `/accounts/` / `/votes/` 这类查询 / 看见写了类型路径 不是已经是正常运转必须有，也不是已经复制到各节点。**  
   官方写：应用应当允许按具体类型查，例如 `/accounts/...` 或 `/votes/...`。看见写了类型路径，不是已经是正常运转必须有。看见建议允许，不是已经复制到各节点。看见能查账户，不是已经新鲜。

怎样写 Query 请求、怎样填 `data` / `path`、怎样做按键查询是规范里的做法，本页不抄。Query 高度就已经是 QueryState 是不变量 371，本页不抄。

## 官方为什么这样拆

- **data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 ≠ 已经是 Query 高度：** 官方把查询分量和高度分开。
- **path 按 URI 路径解释、/store 必须按键查 ≠ 已经是引擎在用：** 官方把应用必须按键查和引擎眼下只用 /p2p 分开。
- **规范建议允许 /accounts / /votes 这类查询 ≠ 已经是正常运转必须有：** 官方把按类型查和建议已经是必须有分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 | 不是已经是 Query 高度 | 不是 Query 可以对当前或过去高度查就已经是 QueryState（371） |
| path 按 URI 路径解释、/store 必须按键查 | 不是已经是引擎在用 | 不是有 /store 路径就已经是引擎在用（326） |
| 规范建议允许 /accounts / /votes 这类查询 | 不是已经是正常运转必须有 | 不是实现了 Query 就已经是正常运转必须有（329） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能带 data / path 就已经是 Query 高度、已经是引擎在用、已经是正常运转必须有」，必须分开 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用是不是已经是 Query 高度、path 按 URI 路径解释、/store 必须按键查是不是已经是引擎在用、规范建议允许 /accounts / /votes 这类查询是不是已经是正常运转必须有。可以跳过「看见能带 data / path 就已经是 Query 高度」。不要另写怎样写 Query 路径。

## 本页不抄

- 怎样写 Query 请求、怎样填 `data` / `path`、怎样做按键查询。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- 有 /store 路径就已经是引擎在用。那是不变量 326。
- 实现了 Query 就已经是正常运转必须有。那是不变量 329。
