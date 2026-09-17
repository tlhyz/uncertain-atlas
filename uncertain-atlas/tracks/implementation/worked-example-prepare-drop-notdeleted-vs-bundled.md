# 例：看见从提案拿掉 tx is not already deleted from mempool interchangeable / not already never propose interchangeable / not already settled interchangeable

**层次**：实现 / 从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事（355 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事（355 余量）/ not 854 prepare-drop-notdeleted interchangeable / not 355 prepare-drop-vs-mempool bundled interchangeable」，不是 Prepare 改列表 bundled（355），也不是提案收了就已经从池里删掉（301），也不是没调 Prepare 就已经从提案拿掉 tx（356/853）。不要另写怎样改 Prepare 列表。

## 官方三件事

1. **看见从提案拿掉 tx / 看见本块不提 这份拿掉 is not already 已经从内存池删掉 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 854 prepare-drop-notdeleted interchangeable / 855 prepare-drop-notinpool interchangeable / 355 prepare-drop item 2 加新的 interchangeable，也不是已经从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事 bundled（355 item 1 余量） interchangeable / 355 prepare-drop item 1 interchangeable。**  
   官方写：应用若认为这笔不该进本块，就不要写进 `PrepareProposalResponse.txs`。这不会把它从内存池删掉，只是推迟。看见本块不提，不是已经出池 interchangeable——本页从 355 item 1 侧钉 not already deleted from mempool 单句。355 prepare-drop vs mempool bundled unbundling 在本页 item 1 启动。

2. **看见本块不提 / 看见拿掉了 / 这份拿掉 is not already 已经永远不提 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 854 prepare-drop-notdeleted interchangeable / 355 prepare-drop item 3 改成 t2 interchangeable / 856 prepare-drop-nottrace interchangeable，也不是已经提案收了就已经从池里删掉 interchangeable / 301 deleted interchangeable。**  
   官方把拿掉了和已经永远不提分开——355 bundled 第一件事常与 301 混成「看见本块不提就已经从池里删掉或已经永远不提 interchangeable」，本页钉 not already never propose 单句。

3. **看见本块不提 / 看见回包没有它 / 这份拿掉 is not already 已经交差 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 854 prepare-drop-notdeleted interchangeable / 855 prepare-drop-notinpool interchangeable，也不是已经没调 Prepare 就已经从提案拿掉 tx interchangeable / 356 validvalue / 853 validvalue-notraw interchangeable。**  
   官方把回包没有它和已经交差分开。看见回包没有它，不是已经交差 interchangeable。355 prepare-drop vs mempool bundled unbundling 在本页 item 1 启动。

怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池是规范里的做法，本页不抄。

## 官方为什么这样拆

- **从提案拿掉 tx not already deleted from mempool ≠ 已经从内存池删掉 interchangeable：** 官方把本块不提和出池分开。
- **看见拿掉了 not already never propose ≠ 已经永远不提 interchangeable：** 官方把拿掉了和已经永远不提分开。
- **看见回包没有它 not already settled ≠ 已经交差 interchangeable：** 官方把回包没有它和已经交差分开；355 prepare-drop vs mempool bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 从提案拿掉 tx | 不是已经从内存池删掉 | 不是提案收了就已经从池里删掉（301） |
| 看见拿掉了 | 不是已经永远不提 | 不是没调 Prepare 就已经从提案拿掉 tx（356/853） |
| 看见回包没有它 | 不是已经交差 | 不是整池可见就已经只能看见装得进一块的子集（345） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从提案拿掉 tx not already deleted from mempool / not already never propose / not already settled 正式三事（355 余量），必须分开是不是已经从内存池删掉、是不是已经永远不提、是不是已经交差。可以跳过「看见本块不提就已经从池里删掉」。不要另写怎样改 Prepare 列表。355 prepare-drop vs mempool bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-drop-notinpool-vs-bundled.md`](worked-example-prepare-drop-notinpool-vs-bundled.md)（不变量 855 item 2）。

## 本页不抄

- 怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池。
- Prepare 改列表 bundled。那是不变量 355。
- 往提案加了一笔新的。那是不变量 355 item 2 余量 / 855。
- 提案收了就已经从池里删掉。那是不变量 301。
- 没调 Prepare 就已经从提案拿掉 tx。那是不变量 356 / 853。
