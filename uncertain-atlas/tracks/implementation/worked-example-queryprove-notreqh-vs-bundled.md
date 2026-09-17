# 例：看见 Query 回包 height 是数据来自哪一高 is not already request height interchangeable / not already fresh interchangeable / not already header AppHash interchangeable

**层次**：实现 / Query 回包 height not already request height / not already fresh / not already header AppHash 正式三事（383 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 height not already request height / not already fresh / not already header AppHash 正式三事（383 余量）/ not 781 queryprove-notreqh interchangeable / not 383 queryprove-vs-proof bundled interchangeable」，不是 Query 证明回包 bundled（383），也不是 Query 可以对当前或过去高度查就已经是 QueryState（371）。不要另写怎样写 Query 证明回包。

## 官方三件事

1. **看见 Query 回包 `height` 是数据来自哪一高 / 看见回了高度 / Query 这份回包高度 is not already 已经是请求里填的那一高 interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 781 queryprove-notreqh interchangeable / 779 queryprove-notapphash interchangeable / 383 queryprove item 1 prove interchangeable，也不是已经 height not already request height / not already fresh / not already header AppHash 正式三事 bundled（383 item 3 余量） interchangeable / 383 queryprove item 3 interchangeable。**  
   官方写：回包 `height` 是这份数据来自哪一高。看见回了高度，不是已经是请求里填的那一高 interchangeable——本页从 383 item 3 侧钉 not already request height 单句。383 queryprove vs proof bundled unbundling 在本页 item 3 完成。

2. **看见回了高度 / 看见填了回包高度 / Query 这份回包高度 is not already 已经新鲜 interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 781 queryprove-notreqh interchangeable / 383 queryprove item 2 proof_ops interchangeable / 780 queryprove-notstore interchangeable，也不是已经 Query 可以对当前或过去高度查就已经是 QueryState interchangeable / 371 queryheight interchangeable。**  
   官方把回包高度和已经新鲜分开——383 bundled 第三件事常与 371 混成「看见回了高度就已经是请求高度或已经是 QueryState interchangeable」，本页钉 not already fresh 单句。

3. **看见回了高度 / 看见是含 Merkle 根的那块 / Query 这份回包高度 is not already 已经印进本头 AppHash interchangeable，也不是已经 Query 证明回包 bundled（383） interchangeable / 781 queryprove-notreqh interchangeable / 779 queryprove-notapphash interchangeable。**  
   官方把含 Merkle 根的那块和已经印进本头 AppHash 分开。看见是含 Merkle 根的那块，不是已经印进本头 AppHash interchangeable。383 queryprove vs proof bundled unbundling 在本页 item 3 完成。

怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **height not already request height ≠ 已经是请求高度 interchangeable：** 官方把回包高度和请求高度分开。
- **height not already fresh ≠ 已经新鲜 interchangeable：** 官方把填了回包高度和已经新鲜分开。
- **height not already header AppHash ≠ 已经印进本头 AppHash interchangeable：** 官方把含 Merkle 根的那块和已经印进本头 AppHash 分开；383 queryprove vs proof bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 height 是数据来自哪一高 | 不是已经是请求高度 | 不是 Query 请求 prove（779/383 item 1） |
| 看见回了高度 | 不是已经新鲜 | 不是 QueryState（371） |
| 看见是含 Merkle 根的那块 | 不是已经印进本头 AppHash | 不是 Query 证明回包 bundled（383） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 height not already request height / not already fresh / not already header AppHash 正式三事（383 余量），必须分开 height 是不是已经是请求高度、是不是已经新鲜、是不是已经印进本头 AppHash。可以跳过「看见回了高度就已经是请求高度」。不要另写怎样写 Query 证明回包。383 queryprove vs proof bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Query 证明、怎样勾 prove、怎样编 proof_ops。
- Query 证明回包 bundled。那是不变量 383。
- Query 请求 prove。那是不变量 383 item 1 余量 / 779。
- Query 回包 proof_ops。那是不变量 383 item 2 余量 / 780。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
