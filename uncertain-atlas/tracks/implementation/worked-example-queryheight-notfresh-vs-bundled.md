# 例：看见没填 / 看见回了最新已提交 / 看见默认 0 is not already already fresh interchangeable / already caught-up interchangeable / already info-handshake interchangeable

**层次**：实现 / height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量）/ not 861 queryheight-notfresh interchangeable / not 371 queryheight bundled interchangeable」，不是 queryheight bundled（371），也不是 Query 可以对当前或过去高度查不是已经是 QueryState（860 item 1 余量）或这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash（862 item 3 余量）。不要另写怎样写 Query 高度。

## 官方三件事

规范把 Methods 里 `height` 默认是 0、回最新已提交那块的数据 和「已经是没填就已经新鲜 interchangeable / 已经是回了最新已提交就已经跟上正在跑的块 interchangeable / 已经是默认 0 就已经是 Info 握手那两列 interchangeable / 已经是 queryheight bundled interchangeable」分开写成三件独立的实现事，不是「看见没填就已经新鲜 interchangeable / 就已经跟上正在跑的块 interchangeable / 就已经是 Info 握手那两列 interchangeable」一件事：

1. **看见没填 / 看见 `height` 默认 0 回最新已提交 / 看见没填高度 is not already 已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 371 queryheight bundled interchangeable / 147 apphash interchangeable / queryheight-sold-as-committed interchangeable，也不是已经 queryheight bundled（371） interchangeable / 861 queryheight-notfresh interchangeable / 371 queryheight item 2 interchangeable，也不是已经 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事 bundled（371 item 2 余量） interchangeable / 371 queryheight item 2 interchangeable，也不是已经能查就已经是 QueryState（860） interchangeable / 862 queryheight-notapphash interchangeable / 370 info-handshake interchangeable，也不是已经本头 AppHash 就已经是本高度交差（147） interchangeable。**  
   官方写：`height` 默认是 0，回最新已提交那块的数据。看见没填，不是已经新鲜。看见没填，不是已经 fresh interchangeable——371 钉 bundled 三事，本页从 item 2 侧钉 not already fresh 单句。看见 `height` 默认 0 回最新已提交，不是已经 queryheight bundled（371） interchangeable——371 钉 bundled，本页钉 item 2 第一件事。看见没填，不是已经能查就已经是 QueryState（860） interchangeable——860 另钉 item 1。看见没填，不是已经 Height-1 根就已经印进本头 AppHash（862） interchangeable——862 另钉 item 3。371 queryheight-vs-committed bundled unbundling 在本页 item 2 续。

2. **看见回了最新已提交 / 看见回最新已提交那块的数据 / 看见回了最新 is not already 已经跟上正在跑的块 interchangeable / 已经 caught-up interchangeable / 已经跟上正在跑的块交差 interchangeable / 371 queryheight bundled interchangeable / 314 querystate interchangeable，也不是已经 queryheight bundled（371） interchangeable / 861 queryheight-notfresh interchangeable / 371 queryheight item 1 能查 interchangeable / 371 queryheight item 3 Height-1 interchangeable，也不是已经 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事 bundled（371 item 2 余量） interchangeable / 371 queryheight item 2 interchangeable，也不是已经新鲜（本页第一件事） interchangeable。**  
   官方写：看见回了最新已提交，不是已经跟上正在跑的块。看见回最新已提交那块的数据，不是已经 caught-up interchangeable——本页钉 not already caught-up 单句。看见回了最新，不是已经新鲜（本页第一件事） interchangeable——三件事分开钉。371 queryheight-vs-committed bundled unbundling 在本页 item 2 续。

3. **看见默认 0 / 看见 height 默认是 0 / 看见没填就按 0 is not already 已经是 Info 握手那两列 interchangeable / 已经 info-handshake interchangeable / 已经是 Info 握手那两列交差 interchangeable / 371 queryheight bundled interchangeable / 370 info-handshake interchangeable，也不是已经 queryheight bundled（371） interchangeable / 861 queryheight-notfresh interchangeable / 371 queryheight item 1 / 371 queryheight item 3，也不是已经 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事 bundled（371 item 2 余量） interchangeable / 371 queryheight item 2 interchangeable，也不是已经新鲜（本页第一件事） interchangeable / 已经跟上正在跑的块（本页第二件事） interchangeable。**  
   官方写：看见默认 0，不是已经是 Info 握手那两列。看见 height 默认是 0，不是已经 info-handshake interchangeable——本页钉 not already info-handshake 单句。看见没填就按 0，不是已经跟上正在跑的块（本页第二件事） interchangeable——三件事分开钉。371 queryheight-vs-committed bundled unbundling 在本页 item 2 续。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。queryheight bundled（371）、Query 可以对当前或过去高度查不是已经是 QueryState（371 item 1 余量 / 860）、这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash（371 item 3 余量 / 862）、Query 回了就已经复制到各节点（329）、本头 AppHash 就已经是本高度交差（147）、Query 回了 Proof 就已经对上 AppHash（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **没填 not already fresh ≠ 371 / 147 interchangeable：** 官方把默认回最新已提交和已经新鲜分开。
- **回了最新已提交 not already caught-up ≠ 已经跟上正在跑的块 interchangeable：** 官方把回了最新已提交和已经跟上尖分开。
- **默认 0 not already info-handshake ≠ 已经是 Info 握手那两列 interchangeable：** 官方把默认 0 和已经是 Info 握手那两列分开；371 queryheight-vs-committed bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没填 | 不是 already fresh | 不是本头 AppHash 就已经是本高度交差 alone（147） |
| 回了最新已提交 | 不是 already caught-up | 不是能查 already querystate alone（860） |
| 默认 0 | 不是 already info-handshake | 不是 Height-1 根 already apphash alone（862） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 默认 0 回最新已提交不是已经新鲜 not already fresh / not already caught-up / not already info-handshake 正式三事（371 余量），必须分开没填 是不是 already fresh interchangeable / 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable、回了最新已提交 是不是 already caught-up interchangeable、默认 0 是不是 already info-handshake interchangeable。可以跳过「看见没填就已经新鲜 interchangeable / 就已经跟上正在跑的块 interchangeable / 就已经是 Info 握手那两列 interchangeable」。不要另写怎样写 Query 高度。371 queryheight-vs-committed bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- queryheight bundled。那是不变量 371。
- Query 可以对当前或过去高度查不是已经是 QueryState。那是不变量 371 item 1 余量 / 860。
- 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash。那是不变量 371 item 3 余量 / 862。
- Query 回了就已经复制到各节点。那是不变量 329。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
