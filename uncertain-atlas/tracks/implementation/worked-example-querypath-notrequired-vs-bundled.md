# 例：看见写了类型路径 / 看见建议允许 / 看见能查账户 is not already already required interchangeable / already replicated interchangeable / already fresh interchangeable

**层次**：实现 / 规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量）/ not 880 querypath-notrequired interchangeable / not 377 querypath bundled interchangeable」，不是 querypath bundled（377），也不是 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度（878 item 1 余量）或 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用（879 item 2 余量）。不要另写怎样写 Query 路径。

## 官方三件事

规范把 Methods 里规范建议允许 /accounts / /votes 这类查询 和「已经是写了类型路径就已经是正常运转必须有 interchangeable / 已经是建议允许就已经复制到各节点 interchangeable / 已经是能查账户就已经新鲜 interchangeable / 已经是 querypath bundled interchangeable」分开写成三件独立的实现事，不是「看见写了类型路径就已经是正常运转必须有 interchangeable / 就已经复制到各节点 interchangeable / 就已经新鲜 interchangeable」一件事：

1. **看见写了类型路径 / 看见规范建议允许 /accounts / /votes 这类查询 / 看见写了 /accounts 或 /votes is not already 已经是正常运转必须有 interchangeable / 已经 required interchangeable / 已经是正常运转必须有交差 interchangeable / 377 querypath bundled interchangeable / 329 query replicated interchangeable / querypath-sold-as-store interchangeable，也不是已经 querypath bundled（377） interchangeable / 880 querypath-notrequired interchangeable / 377 querypath item 3 interchangeable，也不是已经规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事 bundled（377 item 3 余量） interchangeable / 377 querypath item 3 interchangeable，也不是已经填了 data 就已经是 Query 高度（878） interchangeable / 写了 /store 就已经是引擎在用（879） interchangeable / 371 queryheight interchangeable，也不是已经实现了 Query 就已经是正常运转必须有（329） interchangeable。**  
   官方写：应用应当允许按具体类型查，例如 `/accounts/...` 或 `/votes/...`。看见写了类型路径，不是已经是正常运转必须有。看见写了类型路径，不是已经 required interchangeable——377 钉 bundled 三事，本页从 item 3 侧钉 not already required 单句。看见规范建议允许 /accounts / /votes 这类查询，不是已经 querypath bundled（377） interchangeable——377 钉 bundled，本页钉 item 3 第一件事。看见写了 /accounts 或 /votes，不是已经实现了 Query 就已经是正常运转必须有（329） interchangeable——329 另钉。377 querypath-vs-store bundled unbundling 在本页 item 3 完成。

2. **看见建议允许 / 看见规范建议允许 / 看见应当允许 is not already 已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable / 377 querypath bundled interchangeable / 329 query replicated interchangeable，也不是已经 querypath bundled（377） interchangeable / 880 querypath-notrequired interchangeable / 377 querypath item 1 填了 data interchangeable / 377 querypath item 2 写了 /store interchangeable，也不是已经规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事 bundled（377 item 3 余量） interchangeable / 377 querypath item 3 interchangeable，也不是已经是正常运转必须有（本页第一件事） interchangeable。**  
   官方写：看见建议允许，不是已经复制到各节点。看见规范建议允许，不是已经 replicated interchangeable——本页钉 not already replicated 单句。看见应当允许，不是已经是正常运转必须有（本页第一件事） interchangeable——三件事分开钉。377 querypath-vs-store bundled unbundling 在本页 item 3 完成。

3. **看见能查账户 / 看见能查 /accounts / 看见能查类型 is not already 已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 377 querypath bundled interchangeable / 878 querypath-notheight interchangeable，也不是已经 querypath bundled（377） interchangeable / 880 querypath-notrequired interchangeable / 377 querypath item 1 / 377 querypath item 2，也不是已经规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事 bundled（377 item 3 余量） interchangeable / 377 querypath item 3 interchangeable，也不是已经是正常运转必须有（本页第一件事） interchangeable / 已经复制到各节点（本页第二件事） interchangeable。**  
   官方写：看见能查账户，不是已经新鲜。看见能查 /accounts，不是已经 fresh interchangeable——本页钉 not already fresh 单句。看见能查类型，不是已经复制到各节点（本页第二件事） interchangeable——三件事分开钉。377 querypath-vs-store bundled unbundling 在本页 item 3 完成。

怎样写 Query 请求、怎样填 data / path、怎样做按键查询是规范里的做法，本页不抄。querypath bundled（377）、data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度（377 item 1 余量 / 878）、path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用（377 item 2 余量 / 879）、Query 可以对当前或过去高度查就已经是 QueryState（371）、有 /store 路径就已经是引擎在用（326）、实现了 Query 就已经是正常运转必须有（329）是另外那套，本页不抄。

## 官方为什么这样拆

- **写了类型路径 not already required ≠ 377 / 329 interchangeable：** 官方把按类型查和建议已经是必须有分开。
- **建议允许 not already replicated ≠ 已经复制到各节点 interchangeable：** 官方把建议允许和已经复制到各节点分开。
- **能查账户 not already fresh ≠ 已经新鲜 interchangeable：** 官方把能查账户和已经新鲜分开；377 querypath-vs-store bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写了类型路径 | 不是 already required | 不是实现了 Query 就已经是正常运转必须有 alone（329） |
| 建议允许 | 不是 already replicated | 不是写了 /store already engine alone（879） |
| 能查账户 | 不是 already fresh | 不是填了 data already height alone（878） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有 not already required / not already replicated / not already fresh 正式三事（377 余量），必须分开写了类型路径 是不是 already required interchangeable / 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable、建议允许 是不是 already replicated interchangeable、能查账户 是不是 already fresh interchangeable。可以跳过「看见写了类型路径就已经是正常运转必须有 interchangeable / 就已经复制到各节点 interchangeable / 就已经新鲜 interchangeable」。不要另写怎样写 Query 路径。377 querypath-vs-store bundled unbundling 在本页 item 3 完成（878 + 879 + 880）。

## 本页不抄

- 怎样写 Query 请求、怎样填 data / path、怎样做按键查询。
- querypath bundled。那是不变量 377。
- data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度。那是不变量 377 item 1 余量 / 878。
- path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用。那是不变量 377 item 2 余量 / 879。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- 有 /store 路径就已经是引擎在用。那是不变量 326。
- 实现了 Query 就已经是正常运转必须有。那是不变量 329。
