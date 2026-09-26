# 例：看见回了值 / 看见有字节 / 看见能读 is not already already matched interchangeable / already replicated interchangeable / already settled interchangeable

**层次**：实现 / Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量）/ not 889 queryindex-notmatched interchangeable / not 380 queryindex bundled interchangeable」，不是 queryindex bundled（380），也不是 Query 回包 index 是树里这个键的下标不是已经是按键查（380 item 1 余量 / 887）或 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度（380 item 2 余量 / 888）。不要另写怎样写 Query 回包。

## 官方三件事

规范把 Methods 里 Query 回包 value 是对上的那份数据的值 和「已经是回了值就已经对上 AppHash interchangeable / 已经是有字节就已经复制到各节点 interchangeable / 已经是能读就已经交差 interchangeable / 已经是 queryindex bundled interchangeable」分开写成三件独立的实现事，不是「看见回了值就已经对上 AppHash interchangeable / 就已经复制到各节点 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见回了值 / 看见 Query 回包 value 是对上的那份数据的值 / 看见回了 value is not already 已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable / 380 queryindex bundled interchangeable / 325 queryprove interchangeable / queryindex-sold-as-store interchangeable，也不是已经 queryindex bundled（380） interchangeable / 889 queryindex-notmatched interchangeable / 380 queryindex item 3 interchangeable，也不是已经 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事 bundled（380 item 3 余量） interchangeable / 380 queryindex item 3 interchangeable，也不是已经有下标就已经是按键查（887） interchangeable / 回了键就已经是 Query 高度（888） interchangeable / 325 queryprove interchangeable，也不是已经 Query 回了 Proof 就已经对上 AppHash（325） interchangeable。**  
   官方写：`value` 是对上的那份数据的值。看见回了值，不是已经对上 AppHash。看见回了值，不是已经 matched interchangeable——380 钉 bundled 三事，本页从 item 3 侧钉 not already matched 单句。看见 Query 回包 value 是对上的那份数据的值，不是已经 queryindex bundled（380） interchangeable——380 钉 bundled，本页钉 item 3 第一件事。看见回了 value，不是已经 Query 回了 Proof 就已经对上 AppHash（325） interchangeable——325 另钉。380 queryindex-vs-store bundled unbundling 在本页 item 3 完成。

2. **看见有字节 / 看见有 value 字节 / 看见有值内容 is not already 已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable / 380 queryindex bundled interchangeable / 377 querypath interchangeable，也不是已经 queryindex bundled（380） interchangeable / 889 queryindex-notmatched interchangeable / 380 queryindex item 1 有下标 interchangeable / 380 queryindex item 2 回了键 interchangeable，也不是已经 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事 bundled（380 item 3 余量） interchangeable / 380 queryindex item 3 interchangeable，也不是已经对上 AppHash（本页第一件事） interchangeable。**  
   官方写：看见有字节，不是已经复制到各节点。看见有 value 字节，不是已经 replicated interchangeable——本页钉 not already replicated 单句。看见有值内容，不是已经对上 AppHash（本页第一件事） interchangeable——三件事分开钉。380 queryindex-vs-store bundled unbundling 在本页 item 3 完成。

3. **看见能读 / 看见能读 value / 看见有 value 回包 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 380 queryindex bundled interchangeable / 888 queryindex-notheight interchangeable，也不是已经 queryindex bundled（380） interchangeable / 889 queryindex-notmatched interchangeable / 380 queryindex item 1 / 380 queryindex item 2，也不是已经 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事 bundled（380 item 3 余量） interchangeable / 380 queryindex item 3 interchangeable，也不是已经对上 AppHash（本页第一件事） interchangeable / 已经复制到各节点（本页第二件事） interchangeable。**  
   官方写：看见能读，不是已经交差。看见能读 value，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有 value 回包，不是已经复制到各节点（本页第二件事） interchangeable——三件事分开钉。380 queryindex-vs-store bundled unbundling 在本页 item 3 完成。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。queryindex bundled（380）、Query 回包 index 是树里这个键的下标不是已经是按键查（380 item 1 余量 / 887）、Query 回包 key 是对上的那份数据的键不是已经是 Query 高度（380 item 2 余量 / 888）、path /store 就必须按键查就已经是引擎在用（377）、Query 可以对当前或过去高度查就已经是 QueryState（371）、Query 回了 Proof 就已经对上 AppHash（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了值 not already matched ≠ 380 / 325 interchangeable：** 官方把回包值和证明对上 AppHash 分开。
- **有字节 not already replicated ≠ 已经复制到各节点 interchangeable：** 官方把有字节和已经复制到各节点分开。
- **能读 not already settled ≠ 已经交差 interchangeable：** 官方把能读和已经交差分开；380 queryindex-vs-store bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了值 | 不是 already matched | 不是 Query 回了 Proof 就已经对上 AppHash alone（325） |
| 有字节 | 不是 already replicated | 不是有下标 already store alone（887） |
| 能读 | 不是 already settled | 不是回了键 already height alone（888） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash not already matched / not already replicated / not already settled 正式三事（380 余量），必须分开回了值 是不是 already matched interchangeable / 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable、有字节 是不是 already replicated interchangeable、能读 是不是 already settled interchangeable。可以跳过「看见回了值就已经对上 AppHash interchangeable / 就已经复制到各节点 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 回包。380 queryindex-vs-store bundled unbundling 在本页 item 3 完成（887 + 888 + 889）。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- queryindex bundled。那是不变量 380。
- Query 回包 index 是树里这个键的下标不是已经是按键查。那是不变量 380 item 1 余量 / 887。
- Query 回包 key 是对上的那份数据的键不是已经是 Query 高度。那是不变量 380 item 2 余量 / 888。
- path /store 就必须按键查就已经是引擎在用。那是不变量 377。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
