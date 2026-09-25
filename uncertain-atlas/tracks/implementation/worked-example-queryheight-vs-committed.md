# 例：看见 Query 可以对当前或过去高度查不是已经是 QueryState；看见 height 默认 0 回最新已提交不是已经新鲜；看见这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash

**层次**：实现 / Query 高度。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Query 可以对当前或过去高度查不是已经是 QueryState / height 默认 0 回最新已提交不是已经新鲜 / 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash」，不是 Query 回了就已经复制到各节点，也不是 Query 回了 Proof 就已经对上 AppHash。不要另写怎样写 Query 高度。371 queryheight-vs-committed bundled unbundling 续（860+861）；精读 [`worked-example-queryheight-notquerystate-vs-bundled.md`](worked-example-queryheight-notquerystate-vs-bundled.md)（不变量 860 item 1）；精读 [`worked-example-queryheight-notfresh-vs-bundled.md`](worked-example-queryheight-notfresh-vs-bundled.md)（不变量 861 item 2）。

## 官方三件事

规范把 Query 可以对当前或过去高度查、`height` 默认 0 回最新已提交、这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态写成三件独立的实现事，不是「看见能查就已经是 QueryState、已经新鲜、已经印进本头 AppHash」一件事：

1. **看见 Query 可以对当前或过去高度查 / 看见能查 不是已经是 QueryState，也不是已经复制到各节点。**  
   官方写：Query 查应用在当前或过去高度的数据。看见能查，不是已经是 QueryState。看见填了高度，不是已经复制到各节点。看见能回，不是已经交差。
2. **看见 `height` 默认 0 回最新已提交 / 看见没填高度 不是已经新鲜，也不是已经是握手对齐。**  
   官方写：`height` 默认是 0，回最新已提交那块的数据。看见没填，不是已经新鲜。看见回了最新已提交，不是已经跟上正在跑的块。看见默认 0，不是已经是 Info 握手那两列。
3. **看见这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态 / 看见填了高度 不是已经印进本头 AppHash，也不是已经对上 Proof。**  
   官方写：这个高度是含应用 Merkle 根的那块，这份根代表 Height-1 提交之后的状态。看见填了高度，不是已经印进本头 AppHash。看见有根，不是已经对上 Proof。看见 Height-1，不是已经是本高度交差。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。Query 回了就已经复制到各节点是不变量 329，本页不抄。

## 官方为什么这样拆

- **Query 可以对当前或过去高度查 ≠ 已经是 QueryState：** 官方把查哪一高度和 QueryState 那份只读副本分开。
- **height 默认 0 回最新已提交 ≠ 已经新鲜：** 官方把默认回最新已提交和已经跟上尖分开。
- **这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态 ≠ 已经印进本头 AppHash：** 官方把查的高度和本头 AppHash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 可以对当前或过去高度查 | 不是已经是 QueryState | 不是 Query 回了就已经复制到各节点（329） |
| height 默认 0 回最新已提交 | 不是已经新鲜 | 不是本头 AppHash 就已经是本高度交差（147） |
| 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态 | 不是已经印进本头 AppHash | 不是 Query 回了 Proof 就已经对上 AppHash（325） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能查就已经是 QueryState、已经新鲜、已经印进本头 AppHash」，必须分开 Query 可以对当前或过去高度查是不是已经是 QueryState、height 默认 0 回最新已提交是不是已经新鲜、这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态是不是已经印进本头 AppHash。可以跳过「看见能查就已经是 QueryState」。不要另写怎样写 Query 高度。371 queryheight-vs-committed bundled unbundling 续（860+861）。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- Query 回了就已经复制到各节点。那是不变量 329。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
