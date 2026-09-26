# 例：看见有下标 / 看见填了下标 / 看见有数 is not already already store interchangeable / already matched interchangeable / already settled interchangeable

**层次**：实现 / Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量）/ not 887 queryindex-notstore interchangeable / not 380 queryindex bundled interchangeable」，不是 queryindex bundled（380），也不是 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度（380 item 2 余量）或 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash（380 item 3 余量）。不要另写怎样写 Query 回包。

## 官方三件事

规范把 Methods 里 Query 回包 index 是树里这个键的下标 和「已经是有下标就已经是按键查 interchangeable / 已经是填了下标就已经对上 AppHash interchangeable / 已经是有数就已经交差 interchangeable / 已经是 queryindex bundled interchangeable」分开写成三件独立的实现事，不是「看见有下标就已经是按键查 interchangeable / 就已经对上 AppHash interchangeable / 就已经交差 interchangeable」一件事：

1. **看见有下标 / 看见 Query 回包 index 是树里这个键的下标 / 看见有 index 下标 is not already 已经是按键查 interchangeable / 已经 store interchangeable / 已经是按键查交差 interchangeable / 380 queryindex bundled interchangeable / 377 querypath interchangeable / queryindex-sold-as-store interchangeable，也不是已经 queryindex bundled（380） interchangeable / 887 queryindex-notstore interchangeable / 380 queryindex item 1 interchangeable，也不是已经 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事 bundled（380 item 1 余量） interchangeable / 380 queryindex item 1 interchangeable，也不是已经回了键就已经是 Query 高度（380 item 2） interchangeable / 回了值就已经对上 AppHash（380 item 3） interchangeable / 377 querypath interchangeable，也不是已经 path /store 就必须按键查就已经是引擎在用（377） interchangeable。**  
   官方写：`index` 是树里这个键的下标。看见有下标，不是已经按 `/store` 按键查。看见有下标，不是已经 store interchangeable——380 钉 bundled 三事，本页从 item 1 侧钉 not already store 单句。看见 Query 回包 index 是树里这个键的下标，不是已经 queryindex bundled（380） interchangeable——380 钉 bundled，本页钉 item 1 第一件事。看见有 index 下标，不是已经 path /store 就必须按键查就已经是引擎在用（377） interchangeable——377 另钉。380 queryindex-vs-store bundled unbundling 在本页 item 1 启动。

2. **看见填了下标 / 看见填了 index / 看见下标有值 is not already 已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable / 380 queryindex bundled interchangeable / 325 queryprove interchangeable，也不是已经 queryindex bundled（380） interchangeable / 887 queryindex-notstore interchangeable / 380 queryindex item 2 回了键 interchangeable / 380 queryindex item 3 回了值 interchangeable，也不是已经 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事 bundled（380 item 1 余量） interchangeable / 380 queryindex item 1 interchangeable，也不是已经是按键查（本页第一件事） interchangeable。**  
   官方写：看见填了下标，不是已经对上 AppHash。看见填了 index，不是已经 matched interchangeable——本页钉 not already matched 单句。看见下标有值，不是已经是按键查（本页第一件事） interchangeable——三件事分开钉。380 queryindex-vs-store bundled unbundling 在本页 item 1 启动。

3. **看见有数 / 看见有下标数字 / 看见 index 是数 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 380 queryindex bundled interchangeable / 371 queryheight interchangeable，也不是已经 queryindex bundled（380） interchangeable / 887 queryindex-notstore interchangeable / 380 queryindex item 2 / 380 queryindex item 3，也不是已经 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事 bundled（380 item 1 余量） interchangeable / 380 queryindex item 1 interchangeable，也不是已经是按键查（本页第一件事） interchangeable / 已经对上 AppHash（本页第二件事） interchangeable。**  
   官方写：看见有数，不是已经交差。看见有下标数字，不是已经 settled interchangeable——本页钉 not already settled 单句。看见 index 是数，不是已经对上 AppHash（本页第二件事） interchangeable——三件事分开钉。380 queryindex-vs-store bundled unbundling 在本页 item 1 启动。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。queryindex bundled（380）、Query 回包 key 是对上的那份数据的键不是已经是 Query 高度（380 item 2 余量）、Query 回包 value 是对上的那份数据的值不是已经对上 AppHash（380 item 3 余量）、path /store 就必须按键查就已经是引擎在用（377）、Query 可以对当前或过去高度查就已经是 QueryState（371）、Query 回了 Proof 就已经对上 AppHash（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **有下标 not already store ≠ 380 / 377 interchangeable：** 官方把回包下标和请求必须按键查分开。
- **填了下标 not already matched ≠ 已经对上 AppHash interchangeable：** 官方把填了下标和已经对上 AppHash 分开。
- **有数 not already settled ≠ 已经交差 interchangeable：** 官方把有数和已经交差分开；380 queryindex-vs-store bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有下标 | 不是 already store | 不是 path /store 就必须按键查就已经是引擎在用 alone（377） |
| 填了下标 | 不是 already matched | 不是 Query 回了 Proof 就已经对上 AppHash alone（325） |
| 有数 | 不是 already settled | 不是回了键 already height alone（380 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量），必须分开有下标 是不是 already store interchangeable / 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable、填了下标 是不是 already matched interchangeable、有数 是不是 already settled interchangeable。可以跳过「看见有下标就已经是按键查 interchangeable / 就已经对上 AppHash interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 回包。380 queryindex-vs-store bundled unbundling 在本页 item 1 启动（887）。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- queryindex bundled。那是不变量 380。
- Query 回包 key 是对上的那份数据的键不是已经是 Query 高度。那是不变量 380 item 2 余量。
- Query 回包 value 是对上的那份数据的值不是已经对上 AppHash。那是不变量 380 item 3 余量。
- path /store 就必须按键查就已经是引擎在用。那是不变量 377。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
