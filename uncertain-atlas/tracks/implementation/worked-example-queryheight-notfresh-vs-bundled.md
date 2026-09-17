# 例：看见 height 默认 0 回最新已提交 is not already fresh interchangeable / not already tip interchangeable / not already handshake interchangeable

**层次**：实现 / height 默认 0 not already fresh / not already tip / not already handshake 正式三事（371 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height 默认 0 not already fresh / not already tip / not already handshake 正式三事（371 余量）/ not 813 queryheight-notfresh interchangeable / not 371 queryheight-vs-committed bundled interchangeable」，不是 Query 高度 bundled（371），也不是本头 AppHash 就已经是本高度交差（147），也不是 Info 握手就已经对齐（370），也不是 Query 回包 log 就已经新鲜（384/777）。不要另写怎样写 Query 高度。

## 官方三件事

1. **看见 `height` 默认 0 回最新已提交 / 看见没填高度 / 这份默认 is not already 已经新鲜 interchangeable / 147 apphash interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 813 queryheight-notfresh interchangeable / 812 queryheight-notstate interchangeable / 371 queryheight item 1 能查 interchangeable，也不是已经 height 默认 0 not already fresh / not already tip / not already handshake 正式三事 bundled（371 item 2 余量） interchangeable / 371 queryheight item 2 interchangeable。**  
   官方写：`height` 默认是 0，回最新已提交那块的数据。看见没填，不是已经新鲜 interchangeable——本页从 371 item 2 侧钉 not already fresh 单句。371 queryheight vs committed bundled unbundling 在本页 item 2 续。

2. **看见没填高度 / 看见回了最新已提交 / 这份默认 is not already 已经跟上正在跑的块 interchangeable / 147 apphash interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 813 queryheight-notfresh interchangeable / 371 queryheight item 3 Merkle 根 interchangeable / 814 queryheight-notapphash interchangeable，也不是已经 Info 握手就已经对齐 interchangeable / 370 infohandshake interchangeable，也不是已经 Query 回包 log 就已经新鲜 interchangeable / 384 querycode / 777 querycode-notfresh interchangeable。**  
   官方把回了最新已提交和已经跟上正在跑的块分开——371 bundled 第二件事常与 147 / 370 / 384 混成「看见没填高度就已经新鲜或已经跟上尖 interchangeable」，本页钉 not already tip 单句。

3. **看见没填高度 / 看见默认 0 / 这份默认 is not already 已经是 Info 握手那两列 interchangeable，也不是已经 Query 高度 bundled（371） interchangeable / 813 queryheight-notfresh interchangeable / 812 queryheight-notstate interchangeable。**  
   官方把默认 0 和已经是 Info 握手那两列分开。看见默认 0，不是已经是 Info 握手那两列 interchangeable。371 queryheight vs committed bundled unbundling 在本页 item 2 续。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。

## 官方为什么这样拆

- **height 默认 0 not already fresh ≠ 147 interchangeable：** 官方把默认回最新已提交和已经跟上尖分开。
- **看见回了最新已提交 not already tip ≠ 已经跟上正在跑的块 interchangeable：** 官方把回了最新已提交和已经跟上正在跑的块分开。
- **看见默认 0 not already handshake ≠ 已经是 Info 握手 interchangeable：** 官方把默认 0 和已经是 Info 握手那两列分开；371 queryheight vs committed bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| height 默认 0 回最新已提交 | 不是已经新鲜（147） | 不是能查（812/371 item 1） |
| 看见没填高度 | 不是已经跟上正在跑的块 | 不是 Info 握手（370） |
| 看见默认 0 | 不是已经是 Info 握手那两列 | 不是 Query 回包 log（384/777） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 默认 0 not already fresh / not already tip / not already handshake 正式三事（371 余量），必须分开是不是已经新鲜 interchangeable / 147、是不是已经跟上正在跑的块、是不是已经是 Info 握手。可以跳过「看见没填高度就已经新鲜」。不要另写怎样写 Query 高度。371 queryheight vs committed bundled unbundling 在本页 item 2 续；续 [`worked-example-queryheight-notapphash-vs-bundled.md`](worked-example-queryheight-notapphash-vs-bundled.md)（不变量 814 item 3）。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- Query 高度 bundled。那是不变量 371。
- 能查当前或过去高度。那是不变量 371 item 1 余量 / 812。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- Info 握手就已经对齐。那是不变量 370。
