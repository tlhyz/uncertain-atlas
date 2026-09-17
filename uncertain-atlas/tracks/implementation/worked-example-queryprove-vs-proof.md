# 例：看见 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash；看见 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查；看见 Query 回包 height 是数据来自哪一高不是已经是请求高度

**层次**：实现 / Query 证明回包。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash / Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 / Query 回包 height 是数据来自哪一高不是已经是请求高度」，不是 Query 回了 Proof 就已经对上 AppHash，也不是 Query 回包 value 就已经对上 AppHash。不要另写怎样写 Query 证明回包。

## 官方三件事

规范把 Query 请求 `prove` 是能回就回默克尔证明、Query 回包 `proof_ops` 是按请求回的、要对这一高 AppHash 验的序列化证明、Query 回包 `height` 是数据来自哪一高写成三件独立的实现事，不是「看见勾了 prove 就已经对上 AppHash、已经是按键查、已经是请求高度」一件事：

1. **看见 Query 请求 `prove` 是能回就回默克尔证明 / 看见勾了 prove 不是已经对上 AppHash，也不是已经是一层树。**  
   官方写：`prove` 是能回就随回包带回默克尔证明。看见勾了 prove，不是已经对上 AppHash。看见能回证明，不是已经是一层树。看见请求了，不是已经交差。
2. **看见 Query 回包 `proof_ops` 是按请求回的、要对这一高 AppHash 验的序列化证明 / 看见回了证明 不是已经是按键查，也不是已经对上 AppHash。**  
   官方写：`proof_ops` 是按请求回的、用来对这一高 `app_hash` 验这份值的序列化证明。看见回了证明，不是已经按 `/store` 按键查。看见有序列化证明，不是已经对上 AppHash。看见能回，不是已经交差。
3. **看见 Query 回包 `height` 是数据来自哪一高 / 看见回了高度 不是已经是请求高度，也不是已经新鲜。**  
   官方写：回包 `height` 是这份数据来自哪一高。看见回了高度，不是已经是请求里填的那一高。看见填了回包高度，不是已经新鲜。看见是含 Merkle 根的那块，不是已经印进本头 AppHash。

怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。Query 回了 Proof 就已经对上 AppHash 是不变量 325，本页不抄。

## 官方为什么这样拆

- **Query 请求 prove 是能回就回默克尔证明 ≠ 已经对上 AppHash：** 官方把请求证明和已经验过 AppHash 分开。
- **Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 ≠ 已经是按键查：** 官方把回包证明和回包键值分开。
- **Query 回包 height 是数据来自哪一高 ≠ 已经是请求高度：** 官方把回包高度和请求高度分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 请求 prove 是能回就回默克尔证明 | 不是已经对上 AppHash | 不是 Query 回了 Proof 就已经对上 AppHash（325） |
| Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 | 不是已经是按键查 | 不是 Query 回包 value 就已经对上 AppHash（380） |
| Query 回包 height 是数据来自哪一高 | 不是已经是请求高度 | 不是 Query 可以对当前或过去高度查就已经是 QueryState（371） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见勾了 prove 就已经对上 AppHash、已经是按键查、已经是请求高度」，必须分开 Query 请求 prove 是能回就回默克尔证明是不是已经对上 AppHash、Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明是不是已经是按键查、Query 回包 height 是数据来自哪一高是不是已经是请求高度。可以跳过「看见勾了 prove 就已经对上 AppHash」。不要另写怎样写 Query 证明回包。383 queryprove vs proof bundled unbundling 完成（779 item 1 / 780 item 2 / 781 item 3）；精读 [`worked-example-queryprove-notapphash-vs-bundled.md`](worked-example-queryprove-notapphash-vs-bundled.md)（不变量 779 item 1）。

## 本页不抄

- 怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
- Query 回包 value 就已经对上 AppHash。那是不变量 380。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
