# 例：看见回了证明 / 看见有序列化证明 / 看见能回 is not already already key interchangeable / already matched interchangeable / already settled interchangeable

**层次**：实现 / Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量）/ not 897 queryprove-notkey interchangeable / not 383 queryprove bundled interchangeable」，不是 queryprove bundled（383），也不是 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash（383 item 1 / 896）或 Query 回包 height 是数据来自哪一高不是已经是请求高度（383 item 3 余量）。不要另写怎样写 Query 证明回包。

## 官方三件事

规范把 Methods 里 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 和「已经是回了证明就已经是按键查 interchangeable / 已经是有序列化证明就已经对上 AppHash interchangeable / 已经是能回就已经交差 interchangeable / 已经是 queryprove bundled interchangeable」分开写成三件独立的实现事，不是「看见回了证明就已经是按键查 interchangeable / 就已经对上 AppHash interchangeable / 就已经交差 interchangeable」一件事：

1. **看见回了证明 / 看见 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 / 看见 proof_ops 是按请求回的 is not already 已经是按键查 interchangeable / 已经 key interchangeable / 已经按 /store 按键查交差 interchangeable / 383 queryprove bundled interchangeable / 380 queryindex interchangeable / queryprove-sold-as-proof interchangeable，也不是已经 queryprove bundled（383） interchangeable / 897 queryprove-notkey interchangeable / 383 queryprove item 2 interchangeable，也不是已经 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事 bundled（383 item 2 余量） interchangeable / 383 queryprove item 2 interchangeable，也不是已经勾了 prove 就已经对上 AppHash（383 item 1 / 896） interchangeable / 回了高度就已经是请求高度（383 item 3） interchangeable / 380 queryindex interchangeable，也不是已经 Query 回包 value 就已经对上 AppHash（380） interchangeable。**  
   官方写：`proof_ops` 是按请求回的、用来对这一高 `app_hash` 验这份值的序列化证明。看见回了证明，不是已经按 `/store` 按键查。看见回了证明，不是已经 key interchangeable——383 钉 bundled 三事，本页从 item 2 侧钉 not already key 单句。看见 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明，不是已经 queryprove bundled（383） interchangeable——383 钉 bundled，本页钉 item 2 第一件事。看见 proof_ops 是按请求回的，不是已经 Query 回包 value 就已经对上 AppHash（380） interchangeable——380 另钉。383 queryprove-vs-proof bundled unbundling 在本页 item 2 续。

2. **看见有序列化证明 / 看见有要对这一高 AppHash 验的序列化证明 / 看见用来验这份值的证明 is not already 已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable / 383 queryprove bundled interchangeable / 325 queryproof interchangeable，也不是已经 queryprove bundled（383） interchangeable / 897 queryprove-notkey interchangeable / 383 queryprove item 1 勾了 prove interchangeable / 383 queryprove item 3 回了高度 interchangeable，也不是已经 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事 bundled（383 item 2 余量） interchangeable / 383 queryprove item 2 interchangeable，也不是已经是按键查（本页第一件事） interchangeable。**  
   官方写：看见有序列化证明，不是已经对上 AppHash。看见有要对这一高 AppHash 验的序列化证明，不是已经 matched interchangeable——本页钉 not already matched 单句。看见用来验这份值的证明，不是已经是按键查（本页第一件事） interchangeable——三件事分开钉。383 queryprove-vs-proof bundled unbundling 在本页 item 2 续。

3. **看见能回 / 看见能回 proof_ops / 看见按请求回了证明 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 383 queryprove bundled interchangeable / 316 txresults interchangeable，也不是已经 queryprove bundled（383） interchangeable / 897 queryprove-notkey interchangeable / 383 queryprove item 1 / 383 queryprove item 3，也不是已经 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事 bundled（383 item 2 余量） interchangeable / 383 queryprove item 2 interchangeable，也不是已经是按键查（本页第一件事） interchangeable / 已经对上 AppHash（本页第二件事） interchangeable。**  
   官方写：看见能回，不是已经交差。看见能回 proof_ops，不是已经 settled interchangeable——本页钉 not already settled 单句。看见按请求回了证明，不是已经对上 AppHash（本页第二件事） interchangeable——三件事分开钉。383 queryprove-vs-proof bundled unbundling 在本页 item 2 续。

怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。queryprove bundled（383）、Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash（383 item 1 / 896）、Query 回包 height 是数据来自哪一高不是已经是请求高度（383 item 3 余量）、Query 回了 Proof 就已经对上 AppHash（325）、Query 回包 value 就已经对上 AppHash（380）、结果列表就已经同一顺序（316）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了证明 not already key ≠ 383 / 380 interchangeable：** 官方把回包证明和回包键值分开。
- **有序列化证明 not already matched ≠ 已经对上 AppHash interchangeable：** 官方把有序列化证明和已经验过 AppHash 分开。
- **能回 not already settled ≠ 已经交差 interchangeable：** 官方把能回和已经交差分开；383 queryprove-vs-proof bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了证明 | 不是 already key | 不是 Query 回包 value 就已经对上 AppHash alone（380） |
| 有序列化证明 | 不是 already matched | 不是勾了 prove already matched alone（896） |
| 能回 | 不是 already settled | 不是回了高度 already reqheight alone（383 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量），必须分开回了证明 是不是 already key interchangeable / 383 queryprove bundled interchangeable / queryprove-sold-as-proof interchangeable、有序列化证明 是不是 already matched interchangeable、能回 是不是 already settled interchangeable。可以跳过「看见回了证明就已经是按键查 interchangeable / 就已经对上 AppHash interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 证明回包。383 queryprove-vs-proof bundled unbundling 在本页 item 2 续（897）。

## 本页不抄

- 怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops。
- queryprove bundled。那是不变量 383。
- Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash。那是不变量 383 item 1 / 896。
- Query 回包 height 是数据来自哪一高不是已经是请求高度。那是不变量 383 item 3 余量。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
- Query 回包 value 就已经对上 AppHash。那是不变量 380。
- 结果列表就已经同一顺序。那是不变量 316。
