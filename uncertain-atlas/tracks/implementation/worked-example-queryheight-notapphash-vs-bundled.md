# 例：看见填了高度 / 看见有根 / 看见 Height-1 is not already already apphash interchangeable / already proof interchangeable / already settled interchangeable

**层次**：实现 / 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量）/ not 862 queryheight-notapphash interchangeable / not 371 queryheight bundled interchangeable」，不是 queryheight bundled（371），也不是 Query 可以对当前或过去高度查不是已经是 QueryState（860 item 1 余量）或 height 默认 0 回最新已提交不是已经新鲜（861 item 2 余量）。不要另写怎样写 Query 高度。

## 官方三件事

规范把 Methods 里这个高度是含应用 Merkle 根的那块、这份根代表 Height-1 提交之后的状态 和「已经是填了高度就已经印进本头 AppHash interchangeable / 已经是有根就已经对上 Proof interchangeable / 已经是 Height-1 就已经是本高度交差 interchangeable / 已经是 queryheight bundled interchangeable」分开写成三件独立的实现事，不是「看见填了高度就已经印进本头 AppHash interchangeable / 就已经对上 Proof interchangeable / 就已经是本高度交差 interchangeable」一件事：

1. **看见填了高度 / 看见这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态 / 看见填了 height is not already 已经印进本头 AppHash interchangeable / 已经 apphash interchangeable / 已经印进本头 AppHash 交差 interchangeable / 371 queryheight bundled interchangeable / 147 apphash interchangeable / queryheight-sold-as-committed interchangeable，也不是已经 queryheight bundled（371） interchangeable / 862 queryheight-notapphash interchangeable / 371 queryheight item 3 interchangeable，也不是已经这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事 bundled（371 item 3 余量） interchangeable / 371 queryheight item 3 interchangeable，也不是已经能查就已经是 QueryState（860） interchangeable / 861 queryheight-notfresh interchangeable / 325 queryproof interchangeable，也不是已经本头 AppHash 就已经是本高度交差（147） interchangeable。**  
   官方写：这个高度是含应用 Merkle 根的那块，这份根代表 Height-1 提交之后的状态。看见填了高度，不是已经印进本头 AppHash。看见填了高度，不是已经 apphash interchangeable——371 钉 bundled 三事，本页从 item 3 侧钉 not already apphash 单句。看见这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态，不是已经 queryheight bundled（371） interchangeable——371 钉 bundled，本页钉 item 3 第一件事。看见填了高度，不是已经能查就已经是 QueryState（860） interchangeable——860 另钉 item 1。看见填了高度，不是已经默认 0 就已经新鲜（861） interchangeable——861 另钉 item 2。371 queryheight-vs-committed bundled unbundling 在本页 item 3 完成。

2. **看见有根 / 看见有应用 Merkle 根 / 看见根在 is not already 已经对上 Proof interchangeable / 已经 proof interchangeable / 已经对上 Proof 交差 interchangeable / 371 queryheight bundled interchangeable / 325 queryproof interchangeable，也不是已经 queryheight bundled（371） interchangeable / 862 queryheight-notapphash interchangeable / 371 queryheight item 1 能查 interchangeable / 371 queryheight item 2 默认 0 interchangeable，也不是已经这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事 bundled（371 item 3 余量） interchangeable / 371 queryheight item 3 interchangeable，也不是已经印进本头 AppHash（本页第一件事） interchangeable。**  
   官方写：看见有根，不是已经对上 Proof。看见有应用 Merkle 根，不是已经 proof interchangeable——本页钉 not already proof 单句。看见根在，不是已经印进本头 AppHash（本页第一件事） interchangeable——三件事分开钉。371 queryheight-vs-committed bundled unbundling 在本页 item 3 完成。

3. **看见 Height-1 / 看见代表 Height-1 提交之后的状态 / 看见 Height-1 状态 is not already 已经是本高度交差 interchangeable / 已经 settled interchangeable / 已经是本高度交差交差 interchangeable / 371 queryheight bundled interchangeable / 147 apphash interchangeable，也不是已经 queryheight bundled（371） interchangeable / 862 queryheight-notapphash interchangeable / 371 queryheight item 1 / 371 queryheight item 2，也不是已经这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事 bundled（371 item 3 余量） interchangeable / 371 queryheight item 3 interchangeable，也不是已经印进本头 AppHash（本页第一件事） interchangeable / 已经对上 Proof（本页第二件事） interchangeable。**  
   官方写：看见 Height-1，不是已经是本高度交差。看见代表 Height-1 提交之后的状态，不是已经 settled interchangeable——本页钉 not already settled 单句。看见 Height-1 状态，不是已经对上 Proof（本页第二件事） interchangeable——三件事分开钉。371 queryheight-vs-committed bundled unbundling 在本页 item 3 完成。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。queryheight bundled（371）、Query 可以对当前或过去高度查不是已经是 QueryState（371 item 1 余量 / 860）、height 默认 0 回最新已提交不是已经新鲜（371 item 2 余量 / 861）、Query 回了就已经复制到各节点（329）、本头 AppHash 就已经是本高度交差（147）、Query 回了 Proof 就已经对上 AppHash（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了高度 not already apphash ≠ 371 / 147 interchangeable：** 官方把查的高度和本头 AppHash 分开。
- **有根 not already proof ≠ 已经对上 Proof interchangeable：** 官方把有根和已经对上 Proof 分开。
- **Height-1 not already settled ≠ 已经是本高度交差 interchangeable：** 官方把 Height-1 状态和已经是本高度交差分开；371 queryheight-vs-committed bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了高度 | 不是 already apphash | 不是本头 AppHash 就已经是本高度交差 alone（147） |
| 有根 | 不是 already proof | 不是 Query 回了 Proof 就已经对上 AppHash alone（325） |
| Height-1 | 不是 already settled | 不是默认 0 already fresh alone（861） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量），必须分开填了高度 是不是 already apphash interchangeable / 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable、有根 是不是 already proof interchangeable、Height-1 是不是 already settled interchangeable。可以跳过「看见填了高度就已经印进本头 AppHash interchangeable / 就已经对上 Proof interchangeable / 就已经是本高度交差 interchangeable」。不要另写怎样写 Query 高度。371 queryheight-vs-committed bundled unbundling 在本页 item 3 完成（860 + 861 + 862）。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- queryheight bundled。那是不变量 371。
- Query 可以对当前或过去高度查不是已经是 QueryState。那是不变量 371 item 1 余量 / 860。
- height 默认 0 回最新已提交不是已经新鲜。那是不变量 371 item 2 余量 / 861。
- Query 回了就已经复制到各节点。那是不变量 329。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
