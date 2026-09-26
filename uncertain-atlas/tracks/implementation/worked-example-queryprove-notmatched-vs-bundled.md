# 例：看见勾了 prove / 看见能回证明 / 看见请求了 is not already already matched interchangeable / already tree interchangeable / already settled interchangeable

**层次**：实现 / Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量）/ not 896 queryprove-notmatched interchangeable / not 383 queryprove bundled interchangeable」，不是 queryprove bundled（383），也不是 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查（383 item 2 余量）或 Query 回包 height 是数据来自哪一高不是已经是请求高度（383 item 3 余量）。不要另写怎样写 Query 证明回包。

## 官方三件事

规范把 Methods 里 Query 请求 prove 是能回就回默克尔证明 和「已经是勾了 prove 就已经对上 AppHash interchangeable / 已经是能回证明就已经是一层树 interchangeable / 已经是请求了就已经交差 interchangeable / 已经是 queryprove bundled interchangeable」分开写成三件独立的实现事，不是「看见勾了 prove 就已经对上 AppHash interchangeable / 就已经是一层树 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见勾了 prove / 看见 Query 请求 prove 是能回就回默克尔证明 / 看见 prove 是能回就随回包带回默克尔证明 is not already 已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable / 383 queryprove bundled interchangeable / 325 queryproof interchangeable / queryprove-sold-as-proof interchangeable，也不是已经 queryprove bundled（383） interchangeable / 896 queryprove-notmatched interchangeable / 383 queryprove item 1 interchangeable，也不是已经 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事 bundled（383 item 1 余量） interchangeable / 383 queryprove item 1 interchangeable，也不是已经回了证明就已经是按键查（383 item 2） interchangeable / 回了高度就已经是请求高度（383 item 3） interchangeable / 325 queryproof interchangeable，也不是已经 Query 回了 Proof 就已经对上 AppHash（325） interchangeable。**  
   官方写：`prove` 是能回就随回包带回默克尔证明。看见勾了 prove，不是已经对上 AppHash。看见勾了 prove，不是已经 matched interchangeable——383 钉 bundled 三事，本页从 item 1 侧钉 not already matched 单句。看见 Query 请求 prove 是能回就回默克尔证明，不是已经 queryprove bundled（383） interchangeable——383 钉 bundled，本页钉 item 1 第一件事。看见 prove 是能回就随回包带回默克尔证明，不是已经 Query 回了 Proof 就已经对上 AppHash（325） interchangeable——325 另钉。383 queryprove-vs-proof bundled unbundling 在本页 item 1 启动。

2. **看见能回证明 / 看见能回就带回默克尔证明 / 看见随回包带回证明 is not already 已经是一层树 interchangeable / 已经 tree interchangeable / 已经是一层树交差 interchangeable / 383 queryprove bundled interchangeable / 325 queryproof interchangeable，也不是已经 queryprove bundled（383） interchangeable / 896 queryprove-notmatched interchangeable / 383 queryprove item 2 回了证明 interchangeable / 383 queryprove item 3 回了高度 interchangeable，也不是已经 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事 bundled（383 item 1 余量） interchangeable / 383 queryprove item 1 interchangeable，也不是已经对上 AppHash（本页第一件事） interchangeable。**  
   官方写：看见能回证明，不是已经是一层树。看见能回就带回默克尔证明，不是已经 tree interchangeable——本页钉 not already tree 单句。看见随回包带回证明，不是已经对上 AppHash（本页第一件事） interchangeable——三件事分开钉。383 queryprove-vs-proof bundled unbundling 在本页 item 1 启动。

3. **看见请求了 / 看见请求了 prove / 看见勾了请求 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 383 queryprove bundled interchangeable / 316 txresults interchangeable，也不是已经 queryprove bundled（383） interchangeable / 896 queryprove-notmatched interchangeable / 383 queryprove item 2 / 383 queryprove item 3，也不是已经 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事 bundled（383 item 1 余量） interchangeable / 383 queryprove item 1 interchangeable，也不是已经对上 AppHash（本页第一件事） interchangeable / 已经是一层树（本页第二件事） interchangeable。**  
   官方写：看见请求了，不是已经交差。看见请求了 prove，不是已经 settled interchangeable——本页钉 not already settled 单句。看见勾了请求，不是已经是一层树（本页第二件事） interchangeable——三件事分开钉。383 queryprove-vs-proof bundled unbundling 在本页 item 1 启动。

怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。queryprove bundled（383）、Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查（383 item 2 余量）、Query 回包 height 是数据来自哪一高不是已经是请求高度（383 item 3 余量）、Query 回了 Proof 就已经对上 AppHash（325）、Query 回包 value 就已经对上 AppHash（380）、结果列表就已经同一顺序（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **勾了 prove not already matched ≠ 383 / 325 interchangeable：** 官方把请求证明和已经验过 AppHash 分开。
- **能回证明 not already tree ≠ 已经是一层树 interchangeable：** 官方把能回证明和已经是一层树分开。
- **请求了 not already settled ≠ 已经交差 interchangeable：** 官方把请求了和已经交差分开；383 queryprove-vs-proof bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 勾了 prove | 不是 already matched | 不是 Query 回了 Proof 就已经对上 AppHash alone（325） |
| 能回证明 | 不是 already tree | 不是回了证明 already key alone（383 item 2） |
| 请求了 | 不是 already settled | 不是回了高度 already reqheight alone（383 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash not already matched / not already tree / not already settled 正式三事（383 余量），必须分开勾了 prove 是不是 already matched interchangeable / 383 queryprove bundled interchangeable / queryprove-sold-as-proof interchangeable、能回证明 是不是 already tree interchangeable、请求了 是不是 already settled interchangeable。可以跳过「看见勾了 prove 就已经对上 AppHash interchangeable / 就已经是一层树 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 证明回包。383 queryprove-vs-proof bundled unbundling 在本页 item 1 启动（896）。

## 本页不抄

- 怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops。
- queryprove bundled。那是不变量 383。
- Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查。那是不变量 383 item 2 余量。
- Query 回包 height 是数据来自哪一高不是已经是请求高度。那是不变量 383 item 3 余量。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
- Query 回包 value 就已经对上 AppHash。那是不变量 380。
- 结果列表就已经同一顺序。那是不变量 316。
