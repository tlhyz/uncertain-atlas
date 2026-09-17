# 例：看见这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态 is not already header AppHash interchangeable / not already proof matched interchangeable / not already this-height settled interchangeable

**层次**：实现 / height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事（371 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事（371 余量）/ not 814 queryheight-notapphash interchangeable / not 371 queryheight-vs-committed bundled interchangeable」，不是 Query 高度 bundled（371），也不是 Query 回了 Proof 就已经对上 AppHash（325），也不是 Query 证明 height 就已经是请求高度（383/781），也不是 Query 回包 value 就已经对上 AppHash（380/790）。不要另写怎样写 Query 高度。

## 官方三件事

1. **看见这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态 / 看见填了高度 / 这份根 is not already 已经印进本头 AppHash interchangeable / 325 queryproof interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 814 queryheight-notapphash interchangeable / 812 queryheight-notstate interchangeable / 371 queryheight item 1 能查 interchangeable，也不是已经 height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事 bundled（371 item 3 余量） interchangeable / 371 queryheight item 3 interchangeable。**  
   官方写：这个高度是含应用 Merkle 根的那块，这份根代表 Height-1 提交之后的状态。看见填了高度，不是已经印进本头 AppHash interchangeable——本页从 371 item 3 侧钉 not already header AppHash 单句。371 queryheight vs committed bundled unbundling 在本页 item 3 完成。

2. **看见填了高度 / 看见有根 / 这份根 is not already 已经对上 Proof interchangeable / 325 queryproof interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 814 queryheight-notapphash interchangeable / 371 queryheight item 2 默认 0 interchangeable / 813 queryheight-notfresh interchangeable，也不是已经 Query 证明 height 就已经是请求高度 interchangeable / 383 queryprove / 781 queryprove-notreqh interchangeable，也不是已经 Query 回包 value 就已经对上 AppHash interchangeable / 380 queryindex / 790 queryindex-notapphash interchangeable。**  
   官方把有根和已经对上 Proof 分开——371 bundled 第三件事常与 325 / 383 / 380 混成「看见填了高度就已经印进本头 AppHash 或已经对上 Proof interchangeable」，本页钉 not already proof matched 单句。

3. **看见填了高度 / 看见 Height-1 / 这份根 is not already 已经是本高度交差 interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 814 queryheight-notapphash interchangeable / 812 queryheight-notstate interchangeable。**  
   官方把 Height-1 和已经是本高度交差分开。看见 Height-1，不是已经是本高度交差 interchangeable。371 queryheight vs committed bundled unbundling 在本页 item 3 完成。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。

## 官方为什么这样拆

- **height 含根 not already header AppHash ≠ 325 interchangeable：** 官方把查的高度和本头 AppHash 分开。
- **看见有根 not already proof matched ≠ 已经对上 Proof interchangeable：** 官方把有根和已经对上 Proof 分开。
- **看见 Height-1 not already this-height settled ≠ 已经是本高度交差 interchangeable：** 官方把 Height-1 和已经是本高度交差分开；371 queryheight vs committed bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态 | 不是已经印进本头 AppHash（325） | 不是能查（812/371 item 1） |
| 看见填了高度 | 不是已经对上 Proof | 不是 Query 证明 height（383/781） |
| 看见 Height-1 | 不是已经是本高度交差 | 不是 Query 回包 value（380/790） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事（371 余量），必须分开是不是已经印进本头 AppHash interchangeable / 325、是不是已经对上 Proof、是不是已经是本高度交差。可以跳过「看见填了高度就已经印进本头 AppHash」。不要另写怎样写 Query 高度。371 queryheight vs committed bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- Query 高度 bundled。那是不变量 371。
- 能查当前或过去高度。那是不变量 371 item 1 余量 / 812。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
- Query 证明 height 就已经是请求高度。那是不变量 383 / 781。
