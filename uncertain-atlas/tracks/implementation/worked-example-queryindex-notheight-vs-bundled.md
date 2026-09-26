# 例：看见回了键 / 看见有键 / 看见能回 is not already already height interchangeable / already fresh interchangeable / already settled interchangeable

**层次**：实现 / Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量）/ not 888 queryindex-notheight interchangeable / not 380 queryindex bundled interchangeable」，不是 queryindex bundled（380），也不是 Query 回包 index 是树里这个键的下标不是已经是按键查（380 item 1 余量 / 887）或 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash（380 item 3 余量）。不要另写怎样写 Query 回包。

## 官方三件事

规范把 Methods 里 Query 回包 key 是对上的那份数据的键 和「已经是回了键就已经是 Query 高度 interchangeable / 已经是有键就已经新鲜 interchangeable / 已经是能回就已经交差 interchangeable / 已经是 queryindex bundled interchangeable」分开写成三件独立的实现事，不是「看见回了键就已经是 Query 高度 interchangeable / 就已经新鲜 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见回了键 / 看见 Query 回包 key 是对上的那份数据的键 / 看见回了 key is not already 已经是 Query 高度 interchangeable / 已经 height interchangeable / 已经是 Query 高度交差 interchangeable / 380 queryindex bundled interchangeable / 371 queryheight interchangeable / queryindex-sold-as-store interchangeable，也不是已经 queryindex bundled（380） interchangeable / 888 queryindex-notheight interchangeable / 380 queryindex item 2 interchangeable，也不是已经 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事 bundled（380 item 2 余量） interchangeable / 380 queryindex item 2 interchangeable，也不是已经有下标就已经是按键查（887） interchangeable / 回了值就已经对上 AppHash（380 item 3） interchangeable / 371 queryheight interchangeable，也不是已经 Query 可以对当前或过去高度查就已经是 QueryState（371） interchangeable。**  
   官方写：`key` 是对上的那份数据的键。看见回了键，不是已经填了高度。看见回了键，不是已经 height interchangeable——380 钉 bundled 三事，本页从 item 2 侧钉 not already height 单句。看见 Query 回包 key 是对上的那份数据的键，不是已经 queryindex bundled（380） interchangeable——380 钉 bundled，本页钉 item 2 第一件事。看见回了 key，不是已经 Query 可以对当前或过去高度查就已经是 QueryState（371） interchangeable——371 另钉。380 queryindex-vs-store bundled unbundling 在本页 item 2 续。

2. **看见有键 / 看见有对上的那份数据的键 / 看见有 key 字段 is not already 已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 380 queryindex bundled interchangeable / 371 queryheight interchangeable，也不是已经 queryindex bundled（380） interchangeable / 888 queryindex-notheight interchangeable / 380 queryindex item 1 有下标 interchangeable / 380 queryindex item 3 回了值 interchangeable，也不是已经 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事 bundled（380 item 2 余量） interchangeable / 380 queryindex item 2 interchangeable，也不是已经是 Query 高度（本页第一件事） interchangeable。**  
   官方写：看见有键，不是已经新鲜。看见有对上的那份数据的键，不是已经 fresh interchangeable——本页钉 not already fresh 单句。看见有 key 字段，不是已经是 Query 高度（本页第一件事） interchangeable——三件事分开钉。380 queryindex-vs-store bundled unbundling 在本页 item 2 续。

3. **看见能回 / 看见能回 key / 看见有 key 回包 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 380 queryindex bundled interchangeable / 887 queryindex-notstore interchangeable，也不是已经 queryindex bundled（380） interchangeable / 888 queryindex-notheight interchangeable / 380 queryindex item 1 / 380 queryindex item 3，也不是已经 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事 bundled（380 item 2 余量） interchangeable / 380 queryindex item 2 interchangeable，也不是已经是 Query 高度（本页第一件事） interchangeable / 已经新鲜（本页第二件事） interchangeable。**  
   官方写：看见能回，不是已经交差。看见能回 key，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有 key 回包，不是已经新鲜（本页第二件事） interchangeable——三件事分开钉。380 queryindex-vs-store bundled unbundling 在本页 item 2 续。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。queryindex bundled（380）、Query 回包 index 是树里这个键的下标不是已经是按键查（380 item 1 余量 / 887）、Query 回包 value 是对上的那份数据的值不是已经对上 AppHash（380 item 3 余量）、path /store 就必须按键查就已经是引擎在用（377）、Query 可以对当前或过去高度查就已经是 QueryState（371）、Query 回了 Proof 就已经对上 AppHash（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了键 not already height ≠ 380 / 371 interchangeable：** 官方把回包键和查询高度分开。
- **有键 not already fresh ≠ 已经新鲜 interchangeable：** 官方把有键和已经新鲜分开。
- **能回 not already settled ≠ 已经交差 interchangeable：** 官方把能回和已经交差分开；380 queryindex-vs-store bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了键 | 不是 already height | 不是 Query 可以对当前或过去高度查就已经是 QueryState alone（371） |
| 有键 | 不是 already fresh | 不是有下标 already store alone（887） |
| 能回 | 不是 already settled | 不是回了值 already matched alone（380 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（380 余量），必须分开回了键 是不是 already height interchangeable / 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable、有键 是不是 already fresh interchangeable、能回 是不是 already settled interchangeable。可以跳过「看见回了键就已经是 Query 高度 interchangeable / 就已经新鲜 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 回包。380 queryindex-vs-store bundled unbundling 在本页 item 2 续（887 + 888）。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- queryindex bundled。那是不变量 380。
- Query 回包 index 是树里这个键的下标不是已经是按键查。那是不变量 380 item 1 余量 / 887。
- Query 回包 value 是对上的那份数据的值不是已经对上 AppHash。那是不变量 380 item 3 余量。
- path /store 就必须按键查就已经是引擎在用。那是不变量 377。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
