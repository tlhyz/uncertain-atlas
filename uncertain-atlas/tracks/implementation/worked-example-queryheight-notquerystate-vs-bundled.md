# 例：看见能查 / 看见填了高度 / 看见能回 is not already already querystate interchangeable / already replicated interchangeable / already settled interchangeable

**层次**：实现 / Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量）/ not 860 queryheight-notquerystate interchangeable / not 371 queryheight bundled interchangeable」，不是 queryheight bundled（371），也不是 height 默认 0 回最新已提交不是已经新鲜（861 item 2 余量）或这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash（862 item 3 余量）。不要另写怎样写 Query 高度。

## 官方三件事

规范把 Methods 里 Query 可以对当前或过去高度查 和「已经是能查就已经是 QueryState interchangeable / 已经是填了高度就已经复制到各节点 interchangeable / 已经是能回就已经交差 interchangeable / 已经是 queryheight bundled interchangeable」分开写成三件独立的实现事，不是「看见能查就已经是 QueryState interchangeable / 就已经复制到各节点 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见能查 / 看见 Query 可以对当前或过去高度查 / 看见能查高度 is not already 已经是 QueryState interchangeable / 已经 querystate interchangeable / 已经是 QueryState 交差 interchangeable / 371 queryheight bundled interchangeable / 314 querystate interchangeable / queryheight-sold-as-committed interchangeable，也不是已经 queryheight bundled（371） interchangeable / 860 queryheight-notquerystate interchangeable / 371 queryheight item 1 interchangeable，也不是已经 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事 bundled（371 item 1 余量） interchangeable / 371 queryheight item 1 interchangeable，也不是已经默认 0 就已经新鲜（861） interchangeable / 862 queryheight-notapphash interchangeable / 329 query-replicated interchangeable，也不是已经 QueryState 就已经是 ExecuteTxState（314） interchangeable。**  
   官方写：Query 查应用在当前或过去高度的数据。看见能查，不是已经是 QueryState。看见能查，不是已经 querystate interchangeable——371 钉 bundled 三事，本页从 item 1 侧钉 not already querystate 单句。看见 Query 可以对当前或过去高度查，不是已经 queryheight bundled（371） interchangeable——371 钉 bundled，本页钉 item 1 第一件事。看见能查，不是已经默认 0 就已经新鲜（861） interchangeable——861 另钉 item 2。看见能查，不是已经 Height-1 根就已经印进本头 AppHash（862） interchangeable——862 另钉 item 3。371 queryheight-vs-committed bundled unbundling 在本页 item 1 启动。

2. **看见填了高度 / 看见填了当前或过去高度 / 看见有高度参数 is not already 已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable / 371 queryheight bundled interchangeable / 329 query-replicated interchangeable，也不是已经 queryheight bundled（371） interchangeable / 860 queryheight-notquerystate interchangeable / 371 queryheight item 2 默认 0 interchangeable / 371 queryheight item 3 Height-1 interchangeable，也不是已经 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事 bundled（371 item 1 余量） interchangeable / 371 queryheight item 1 interchangeable，也不是已经是 QueryState（本页第一件事） interchangeable。**  
   官方写：看见填了高度，不是已经复制到各节点。看见填了当前或过去高度，不是已经 replicated interchangeable——本页钉 not already replicated 单句。看见有高度参数，不是已经是 QueryState（本页第一件事） interchangeable——三件事分开钉。371 queryheight-vs-committed bundled unbundling 在本页 item 1 启动。

3. **看见能回 / 看见能回 Query / 看见回得了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 371 queryheight bundled interchangeable / 33 fourgates interchangeable，也不是已经 queryheight bundled（371） interchangeable / 860 queryheight-notquerystate interchangeable / 371 queryheight item 2 / 371 queryheight item 3，也不是已经 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事 bundled（371 item 1 余量） interchangeable / 371 queryheight item 1 interchangeable，也不是已经是 QueryState（本页第一件事） interchangeable / 已经复制到各节点（本页第二件事） interchangeable。**  
   官方写：看见能回，不是已经交差。看见能回 Query，不是已经 settled interchangeable——本页钉 not already settled 单句。看见回得了，不是已经复制到各节点（本页第二件事） interchangeable——三件事分开钉。371 queryheight-vs-committed bundled unbundling 在本页 item 1 启动。

怎样写 Query 请求、怎样填 height、怎样对 Merkle 根是规范里的做法，本页不抄。queryheight bundled（371）、height 默认 0 回最新已提交不是已经新鲜（371 item 2 余量 / 861）、这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash（371 item 3 余量 / 862）、Query 回了就已经复制到各节点（329）、QueryState 就已经是 ExecuteTxState（314）、Query 回了 Proof 就已经对上 AppHash（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **能查 not already querystate ≠ 371 / 314 interchangeable：** 官方把查哪一高度和 QueryState 那份只读副本分开。
- **填了高度 not already replicated ≠ 已经复制到各节点 interchangeable：** 官方把填了高度和已经复制到各节点分开。
- **能回 not already settled ≠ 已经交差 interchangeable：** 官方把能回和已经交差分开；371 queryheight-vs-committed bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能查 | 不是 already querystate | 不是 QueryState 就已经是 ExecuteTxState alone（314） |
| 填了高度 | 不是 already replicated | 不是 Query 回了就已经复制到各节点 alone（329） |
| 能回 | 不是 already settled | 不是默认 0 already fresh alone（861） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量），必须分开能查 是不是 already querystate interchangeable / 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable、填了高度 是不是 already replicated interchangeable、能回 是不是 already settled interchangeable。可以跳过「看见能查就已经是 QueryState interchangeable / 就已经复制到各节点 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Query 高度。371 queryheight-vs-committed bundled unbundling 在本页 item 1 启动；完成 [`worked-example-queryheight-notfresh-vs-bundled.md`](worked-example-queryheight-notfresh-vs-bundled.md)（不变量 861 item 2）；完成 [`worked-example-queryheight-notapphash-vs-bundled.md`](worked-example-queryheight-notapphash-vs-bundled.md)（不变量 862 item 3）。

## 本页不抄

- 怎样写 Query 请求、怎样填 height、怎样对 Merkle 根。
- queryheight bundled。那是不变量 371。
- height 默认 0 回最新已提交不是已经新鲜。那是不变量 371 item 2 余量 / 861。
- 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash。那是不变量 371 item 3 余量 / 862。
- Query 回了就已经复制到各节点。那是不变量 329。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
