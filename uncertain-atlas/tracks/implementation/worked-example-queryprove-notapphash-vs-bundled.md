# 例：看见 Query 请求 prove 是能回就回默克尔证明 is not already AppHash matched interchangeable / not already one-layer tree interchangeable / not already settled interchangeable

**层次**：实现 / Query 请求 prove not already AppHash matched / not already one-layer tree / not already settled 正式三事（383 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 请求 prove not already AppHash matched / not already one-layer tree / not already settled 正式三事（383 余量）/ not 779 queryprove-notapphash interchangeable / not 383 queryprove-vs-proof bundled interchangeable」，不是 Query 证明回包 bundled（383），也不是 Query 回了 Proof 就已经对上 AppHash（325）。不要另写怎样写 Query 证明回包。

## 官方三件事

1. **看见 Query 请求 `prove` 是能回就回默克尔证明 / 看见勾了 prove / Query 这份证明请求 is not already 已经对上 AppHash interchangeable / 325 queryproof interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 779 queryprove-notapphash interchangeable / 780 queryprove-notstore interchangeable / 383 queryprove item 2 proof_ops interchangeable，也不是已经 prove not already AppHash matched / not already one-layer tree / not already settled 正式三事 bundled（383 item 1 余量） interchangeable / 383 queryprove item 1 interchangeable。**  
   官方写：`prove` 是能回就随回包带回默克尔证明。看见勾了 prove，不是已经对上 AppHash interchangeable——本页从 383 item 1 侧钉 not already AppHash matched 单句。383 queryprove vs proof bundled unbundling 在本页 item 1 启动。

2. **看见勾了 prove / 看见能回证明 / Query 这份证明请求 is not already 已经是一层树 interchangeable / 325 queryproof interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 779 queryprove-notapphash interchangeable / 383 queryprove item 3 height interchangeable / 781 queryprove-notreqh interchangeable。**  
   官方把请求证明和已经是一层树分开——383 bundled 第一件事常与 325 混成「看见勾了 prove 就已经对上 AppHash 或已经是一层树 interchangeable」，本页钉 not already one-layer tree 单句。

3. **看见勾了 prove / 看见请求了 / Query 这份证明请求 is not already 已经交差 interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 779 queryprove-notapphash interchangeable / 780 queryprove-notstore interchangeable。**  
   官方把请求了 prove 和已经交差分开。看见请求了，不是已经交差 interchangeable。383 queryprove vs proof bundled unbundling 在本页 item 1 启动。

怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **prove not already AppHash matched ≠ 325 interchangeable：** 官方把请求证明和已经验过 AppHash 分开。
- **prove not already one-layer tree ≠ 325 interchangeable：** 官方把能回证明和已经是一层树分开。
- **prove not already settled ≠ 已经交差 interchangeable：** 官方把请求了 prove 和已经交差分开；383 queryprove vs proof bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 请求 prove 是能回就回默克尔证明 | 不是已经对上 AppHash（325） | 不是 Query 回包 proof_ops（780/383 item 2） |
| 看见勾了 prove | 不是已经是一层树 | 不是 Query 证明回包 bundled（383） |
| 看见请求了 | 不是已经交差 | 不是 Query 回了 Proof 就已经对上 AppHash（325） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 请求 prove not already AppHash matched / not already one-layer tree / not already settled 正式三事（383 余量），必须分开 prove 是不是已经对上 AppHash interchangeable / 325、是不是已经是一层树、是不是已经交差。可以跳过「看见勾了 prove 就已经对上 AppHash」。不要另写怎样写 Query 证明回包。383 queryprove vs proof bundled unbundling 在本页 item 1 启动；续 [`worked-example-queryprove-notstore-vs-bundled.md`](worked-example-queryprove-notstore-vs-bundled.md)（不变量 780 item 2）。

## 本页不抄

- 怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops。
- Query 证明回包 bundled。那是不变量 383。
- Query 回包 proof_ops。那是不变量 383 item 2 余量 / 780。
- Query 回包 height。那是不变量 383 item 3 余量 / 781。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
