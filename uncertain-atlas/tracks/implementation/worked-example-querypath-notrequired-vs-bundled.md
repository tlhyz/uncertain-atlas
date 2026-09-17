# 例：看见规范建议允许 /accounts / /votes 这类查询 is not already required interchangeable / not already replicated interchangeable / not already fresh interchangeable

**层次**：实现 / 类型路径 not already required / not already replicated / not already fresh 正式三事（377 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「类型路径 not already required / not already replicated / not already fresh 正式三事（377 余量）/ not 799 querypath-notrequired interchangeable / not 377 querypath-vs-store bundled interchangeable」，不是 Query 路径 bundled（377），也不是实现了 Query 就已经是正常运转必须有（329），也不是 Query 回包 value 就已经复制到各节点（380/790），也不是 Query 回包 log 就已经新鲜（384/777）。不要另写怎样写 Query 路径。

## 官方三件事

1. **看见规范建议允许 `/accounts/` / `/votes/` 这类查询 / 看见写了类型路径 / 这份建议 is not already 已经是正常运转必须有 interchangeable / 329 queryrep interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 799 querypath-notrequired interchangeable / 797 querypath-notheight interchangeable / 377 querypath item 1 data interchangeable，也不是已经类型路径 not already required / not already replicated / not already fresh 正式三事 bundled（377 item 3 余量） interchangeable / 377 querypath item 3 interchangeable。**  
   官方写：应用应当允许按具体类型查，例如 `/accounts/...` 或 `/votes/...`。看见写了类型路径，不是已经是正常运转必须有 interchangeable——本页从 377 item 3 侧钉 not already required 单句。377 querypath vs store bundled unbundling 在本页 item 3 完成。

2. **看见写了类型路径 / 看见建议允许 / 这份建议 is not already 已经复制到各节点 interchangeable / 329 queryrep interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 799 querypath-notrequired interchangeable / 377 querypath item 2 path interchangeable / 798 querypath-notengine interchangeable，也不是已经 Query 回包 value 就已经复制到各节点 interchangeable / 380 queryindex / 790 queryindex-notapphash interchangeable，也不是已经 Query 回包 log 就已经新鲜 interchangeable / 384 querycode / 777 querycode-notfresh interchangeable。**  
   官方把建议允许和已经复制到各节点分开——377 bundled 第三件事常与 329 / 380 / 384 混成「看见写了类型路径就已经是正常运转必须有或已经复制 interchangeable」，本页钉 not already replicated 单句。

3. **看见写了类型路径 / 看见能查账户 / 这份建议 is not already 已经新鲜 interchangeable，也不是已经 Query 路径 bundled（377） interchangeable / 799 querypath-notrequired interchangeable / 797 querypath-notheight interchangeable。**  
   官方把能查账户和已经新鲜分开。看见能查账户，不是已经新鲜 interchangeable。377 querypath vs store bundled unbundling 在本页 item 3 完成。

怎样写 Query 请求、怎样填 data / path、怎样做按键查询是规范里的做法，本页不抄。

## 官方为什么这样拆

- **类型路径 not already required ≠ 329 interchangeable：** 官方把按类型查和建议已经是必须有分开。
- **看见建议允许 not already replicated ≠ 已经复制 interchangeable：** 官方把建议允许和已经复制到各节点分开。
- **看见能查账户 not already fresh ≠ 已经新鲜 interchangeable：** 官方把能查账户和已经新鲜分开；377 querypath vs store bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 规范建议允许 /accounts / /votes | 不是已经是正常运转必须有（329） | 不是 data 查询分量（797/377 item 1） |
| 看见写了类型路径 | 不是已经复制到各节点 | 不是 Query 回包 value（380/790） |
| 看见能查账户 | 不是已经新鲜 | 不是 Query 回包 log（384/777） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看类型路径 not already required / not already replicated / not already fresh 正式三事（377 余量），必须分开是不是已经是正常运转必须有 interchangeable / 329、是不是已经复制到各节点、是不是已经新鲜。可以跳过「看见写了类型路径就已经是正常运转必须有」。不要另写怎样写 Query 路径。377 querypath vs store bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Query 请求、怎样填 data / path、怎样做按键查询。
- Query 路径 bundled。那是不变量 377。
- data 按 URI 查询分量解释。那是不变量 377 item 1 余量 / 797。
- 实现了 Query 就已经是正常运转必须有。那是不变量 329。
- Query 回包 value 就已经复制。那是不变量 380 / 790。
